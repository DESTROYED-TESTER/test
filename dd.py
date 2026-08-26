#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import random
import requests
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import List, Dict, Optional, Set
import logging

# Color codes for terminal output
class Colors:
    WHITE = '\033[1;97m'
    RED = '\033[1;91m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    BLUE = '\033[1;94m'
    PURPLE = '\033[1;95m'
    CYAN = '\033[1;96m'
    ORANGE = '\033[38;2;255;127;0;1m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class InstagramCollector:
    def __init__(self):
        self.user_ids: Set[str] = set()
        self.user_data: Dict[str, Dict] = {}
        self.collected_count = 0
        self.is_running = True
        self.lock = threading.Lock()
        
        # Create data directory
        os.makedirs('data', exist_ok=True)
        os.makedirs('logs', exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/collector.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104',
            'x-ig-app-id': '1217981644879628',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        
        # Load existing data if available
        self.load_existing_data()
        
    def load_existing_data(self):
        """Load previously collected data"""
        try:
            if os.path.exists('data/user_ids.txt'):
                with open('data/user_ids.txt', 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            self.user_ids.add(line)
                self.logger.info(f"Loaded {len(self.user_ids)} existing user IDs")
        except Exception as e:
            self.logger.error(f"Error loading existing data: {e}")
            
    def save_data(self):
        """Save collected data to files"""
        try:
            with self.lock:
                # Save user IDs
                with open('data/user_ids.txt', 'w') as f:
                    for uid in sorted(self.user_ids):
                        f.write(f"{uid}\n")
                
                # Save user data
                if self.user_data:
                    with open('data/user_data.json', 'w') as f:
                        json.dump(self.user_data, f, indent=2)
                
                self.logger.info(f"Saved {len(self.user_ids)} user IDs and {len(self.user_data)} user profiles")
        except Exception as e:
            self.logger.error(f"Error saving data: {e}")
            
    def get_user_id_from_username(self, username: str) -> Optional[str]:
        """Get user ID from username using multiple methods"""
        methods = [
            self._get_user_id_api,
            self._get_user_id_graphql,
            self._get_user_id_scrape
        ]
        
        for method in methods:
            try:
                user_id = method(username)
                if user_id:
                    return user_id
            except Exception as e:
                self.logger.debug(f"Method {method.__name__} failed: {e}")
                continue
        return None
        
    def _get_user_id_api(self, username: str) -> Optional[str]:
        """Get user ID using Instagram API"""
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    return data['data']['user'].get('id')
        except Exception:
            pass
        return None
        
    def _get_user_id_graphql(self, username: str) -> Optional[str]:
        """Get user ID using GraphQL query"""
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    return data['data']['user'].get('id')
        except Exception:
            pass
        return None
        
    def _get_user_id_scrape(self, username: str) -> Optional[str]:
        """Get user ID by scraping profile page"""
        url = f'https://www.instagram.com/{username}/'
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                patterns = [
                    r'"user_id":"(\d+)"',
                    r'"profilePage_(\d+)"',
                    r'"id":"(\d+)","username":"' + username + '"'
                ]
                for pattern in patterns:
                    match = re.search(pattern, response.text)
                    if match:
                        return match.group(1)
        except Exception:
            pass
        return None
        
    def get_followers(self, user_id: str, max_count: int = None) -> List[Dict]:
        """Get followers of a user with pagination"""
        followers = []
        after = None
        has_next = True
        count = 0
        
        while has_next and (max_count is None or count < max_count):
            try:
                url = 'https://www.instagram.com/graphql/query/'
                params = {
                    'query_hash': '37479f2b8209594dde7facb0d904896a',
                    'variables': json.dumps({
                        'id': user_id,
                        'first': 50,
                        'after': after
                    })
                }
                
                response = requests.get(url, params=params, headers=self.headers, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data and 'user' in data['data']:
                        user_data = data['data']['user']
                        edges = user_data.get('edge_followed_by', {}).get('edges', [])
                        
                        for edge in edges:
                            node = edge.get('node', {})
                            if node.get('id'):
                                followers.append({
                                    'id': node.get('id'),
                                    'username': node.get('username'),
                                    'full_name': node.get('full_name', ''),
                                    'is_private': node.get('is_private', False),
                                    'is_verified': node.get('is_verified', False)
                                })
                                count += 1
                                
                                # Auto collect user IDs
                                with self.lock:
                                    if node.get('id') not in self.user_ids:
                                        self.user_ids.add(node.get('id'))
                                        self.user_data[node.get('id')] = {
                                            'username': node.get('username'),
                                            'full_name': node.get('full_name', ''),
                                            'is_private': node.get('is_private', False),
                                            'is_verified': node.get('is_verified', False),
                                            'collected_at': datetime.now().isoformat()
                                        }
                                        self.collected_count += 1
                        
                        # Check for next page
                        page_info = user_data.get('edge_followed_by', {}).get('page_info', {})
                        has_next = page_info.get('has_next_page', False)
                        after = page_info.get('end_cursor')
                        
                        self.logger.info(f"Collected {count} followers so far...")
                        
                        # Save progress periodically
                        if count % 100 == 0:
                            self.save_data()
                            
                time.sleep(random.uniform(0.5, 1.5))  # Rate limiting
                
            except Exception as e:
                self.logger.error(f"Error getting followers: {e}")
                has_next = False
                
        return followers
        
    def get_following(self, user_id: str, max_count: int = None) -> List[Dict]:
        """Get following of a user with pagination"""
        following = []
        after = None
        has_next = True
        count = 0
        
        while has_next and (max_count is None or count < max_count):
            try:
                url = 'https://www.instagram.com/graphql/query/'
                params = {
                    'query_hash': '58712303d941c6855d4e888c5f0cd22f',
                    'variables': json.dumps({
                        'id': user_id,
                        'first': 50,
                        'after': after
                    })
                }
                
                response = requests.get(url, params=params, headers=self.headers, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data and 'user' in data['data']:
                        user_data = data['data']['user']
                        edges = user_data.get('edge_follow', {}).get('edges', [])
                        
                        for edge in edges:
                            node = edge.get('node', {})
                            if node.get('id'):
                                following.append({
                                    'id': node.get('id'),
                                    'username': node.get('username'),
                                    'full_name': node.get('full_name', ''),
                                    'is_private': node.get('is_private', False),
                                    'is_verified': node.get('is_verified', False)
                                })
                                count += 1
                                
                                # Auto collect user IDs
                                with self.lock:
                                    if node.get('id') not in self.user_ids:
                                        self.user_ids.add(node.get('id'))
                                        self.user_data[node.get('id')] = {
                                            'username': node.get('username'),
                                            'full_name': node.get('full_name', ''),
                                            'is_private': node.get('is_private', False),
                                            'is_verified': node.get('is_verified', False),
                                            'collected_at': datetime.now().isoformat()
                                        }
                                        self.collected_count += 1
                        
                        # Check for next page
                        page_info = user_data.get('edge_follow', {}).get('page_info', {})
                        has_next = page_info.get('has_next_page', False)
                        after = page_info.get('end_cursor')
                        
                        self.logger.info(f"Collected {count} following so far...")
                        
                        # Save progress periodically
                        if count % 100 == 0:
                            self.save_data()
                            
                time.sleep(random.uniform(0.5, 1.5))  # Rate limiting
                
            except Exception as e:
                self.logger.error(f"Error getting following: {e}")
                has_next = False
                
        return following
        
    def collect_unlimited(self, start_username: str, max_users: int = None):
        """Collect unlimited user IDs starting from a username"""
        self.logger.info(f"Starting unlimited collection from: {start_username}")
        
        # Get initial user ID
        start_user_id = self.get_user_id_from_username(start_username)
        if not start_user_id:
            self.logger.error(f"Could not find user: {start_username}")
            return
            
        self.logger.info(f"Found user ID: {start_user_id}")
        
        # Queue for processing
        to_process = [start_user_id]
        processed = set()
        
        while to_process and (max_users is None or len(self.user_ids) < max_users):
            current_id = to_process.pop(0)
            
            if current_id in processed:
                continue
                
            processed.add(current_id)
            
            try:
                self.logger.info(f"Processing user: {current_id} (Total collected: {len(self.user_ids)})")
                
                # Get followers
                followers = self.get_followers(current_id)
                for follower in followers:
                    if follower['id'] not in processed and follower['id'] not in to_process:
                        to_process.append(follower['id'])
                        
                # Get following
                following = self.get_following(current_id)
                for follow in following:
                    if follow['id'] not in processed and follow['id'] not in to_process:
                        to_process.append(follow['id'])
                        
                # Save progress
                self.save_data()
                
                # Show progress
                self.display_stats()
                
                # Rate limiting
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                self.logger.error(f"Error processing user {current_id}: {e}")
                continue
                
        self.logger.info(f"Collection complete! Total users: {len(self.user_ids)}")
        
    def display_stats(self):
        """Display collection statistics"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")
        print(f"{Colors.CYAN}📊 Instagram Collector - Unlimited Mode{Colors.RESET}")
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")
        print(f"{Colors.WHITE}Total Users Collected: {Colors.CYAN}{len(self.user_ids)}{Colors.RESET}")
        print(f"{Colors.WHITE}Data Points: {Colors.CYAN}{len(self.user_data)}{Colors.RESET}")
        print(f"{Colors.WHITE}Last Updated: {Colors.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
        
        # Show sample users
        if len(self.user_ids) > 0:
            print(f"\n{Colors.YELLOW}Recent Collections:{Colors.RESET}")
            sample_ids = list(self.user_ids)[-5:]
            for uid in sample_ids:
                if uid in self.user_data:
                    user = self.user_data[uid]
                    print(f"  {Colors.GREEN}• {user.get('username', 'Unknown')} ({uid}){Colors.RESET}")
                    
        print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
        
    def auto_collect_loop(self, start_username: str, batch_size: int = 1000):
        """Auto collect in a loop with continuous operation"""
        self.logger.info("Starting auto-collect loop...")
        
        while self.is_running:
            try:
                # Collect in batches
                current_count = len(self.user_ids)
                target_count = current_count + batch_size
                
                self.collect_unlimited(start_username, max_users=target_count)
                
                # Wait before next batch
                self.logger.info(f"Batch complete. Waiting 60 seconds before next batch...")
                time.sleep(60)
                
            except KeyboardInterrupt:
                self.logger.info("Stopping collection...")
                self.is_running = False
                break
            except Exception as e:
                self.logger.error(f"Error in auto-collect loop: {e}")
                time.sleep(30)
                
    def export_data(self, format_type: str = 'txt'):
        """Export collected data in various formats"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"data/export_{timestamp}"
        
        if format_type == 'txt':
            # Simple text format
            with open(f"{filename}.txt", 'w') as f:
                for uid in sorted(self.user_ids):
                    if uid in self.user_data:
                        user = self.user_data[uid]
                        f.write(f"{uid}|{user.get('username', '')}|{user.get('full_name', '')}\n")
                        
        elif format_type == 'json':
            # JSON format
            with open(f"{filename}.json", 'w') as f:
                export_data = {
                    'metadata': {
                        'total_users': len(self.user_ids),
                        'export_date': datetime.now().isoformat(),
                        'version': '1.0'
                    },
                    'users': self.user_data
                }
                json.dump(export_data, f, indent=2)
                
        elif format_type == 'csv':
            # CSV format
            import csv
            with open(f"{filename}.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['User ID', 'Username', 'Full Name', 'Private', 'Verified', 'Collected At'])
                for uid in sorted(self.user_ids):
                    if uid in self.user_data:
                        user = self.user_data[uid]
                        writer.writerow([
                            uid,
                            user.get('username', ''),
                            user.get('full_name', ''),
                            user.get('is_private', False),
                            user.get('is_verified', False),
                            user.get('collected_at', '')
                        ])
                        
        self.logger.info(f"Data exported to {filename}.{format_type}")

def main():
    collector = InstagramCollector()
    
    print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.CYAN}🚀 Instagram Unlimited User ID Collector{Colors.RESET}")
    print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.YELLOW}This tool will collect user IDs in an unlimited loop{Colors.RESET}")
    print(f"{Colors.YELLOW}Data will be auto-saved to data/ folder{Colors.RESET}")
    print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")
    
    try:
        # Get starting username
        start_username = input(f"\n{Colors.WHITE}Enter starting username: {Colors.CYAN}").strip()
        if not start_username:
            start_username = 'instagram'  # Default
            
        # Get collection mode
        print(f"\n{Colors.YELLOW}Collection Modes:{Colors.RESET}")
        print(f"{Colors.WHITE}1. Unlimited Collection (Continuous){Colors.RESET}")
        print(f"{Colors.WHITE}2. Collection with Limit{Colors.RESET}")
        print(f"{Colors.WHITE}3. Export Existing Data{Colors.RESET}")
        
        choice = input(f"\n{Colors.WHITE}Select mode (1-3): {Colors.CYAN}").strip()
        
        if choice == '1':
            # Unlimited mode
            print(f"\n{Colors.GREEN}Starting unlimited collection...{Colors.RESET}")
            print(f"{Colors.YELLOW}Press Ctrl+C to stop{Colors.RESET}")
            
            try:
                collector.auto_collect_loop(start_username, batch_size=500)
            except KeyboardInterrupt:
                collector.is_running = False
                print(f"\n{Colors.RED}Stopping collection...{Colors.RESET}")
                
        elif choice == '2':
            # Limited mode
            try:
                max_users = int(input(f"\n{Colors.WHITE}Maximum users to collect: {Colors.CYAN}").strip())
                collector.collect_unlimited(start_username, max_users=max_users)
            except ValueError:
                print(f"{Colors.RED}Invalid number!{Colors.RESET}")
                
        elif choice == '3':
            # Export data
            print(f"\n{Colors.YELLOW}Export Formats:{Colors.RESET}")
            print(f"{Colors.WHITE}1. TXT{Colors.RESET}")
            print(f"{Colors.WHITE}2. JSON{Colors.RESET}")
            print(f"{Colors.WHITE}3. CSV{Colors.RESET}")
            
            format_choice = input(f"\n{Colors.WHITE}Select format: {Colors.CYAN}").strip()
            format_map = {'1': 'txt', '2': 'json', '3': 'csv'}
            export_format = format_map.get(format_choice, 'txt')
            
            collector.export_data(export_format)
            
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.RESET}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Exiting...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    finally:
        # Save final data
        collector.save_data()
        print(f"\n{Colors.GREEN}Final data saved! Total users: {len(collector.user_ids)}{Colors.RESET}")

if __name__ == "__main__":
    main()
