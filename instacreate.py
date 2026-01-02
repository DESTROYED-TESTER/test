#!/usr/bin/env python3
"""
Test script for FakeMailService
Tests the Mail.tm API functionality
"""

from instagram_account_creator import FakeMailService
import time

def test_fakemail():
    """Test the FakeMailService functionality"""
    print("=" * 60)
    print("🧪 Testing FakeMailService")
    print("=" * 60)
    
    # Initialize service
    fake_mail = FakeMailService()
    
    # Test 1: Generate email
    print("\n📧 Test 1: Generating fake email...")
    email = fake_mail.generate_email()
    
    if email:
        print(f"✅ Email generated: {email}")
        print(f"✅ Token acquired: {fake_mail.token[:20]}..." if fake_mail.token else "❌ No token")
    else:
        print("❌ Failed to generate email")
        return False
    
    # Test 2: Get available domains
    print("\n🌐 Test 2: Getting available domains...")
    domains = fake_mail.get_domains()
    
    if domains:
        print(f"✅ Found {len(domains)} domains:")
        for i, domain in enumerate(domains[:5], 1):
            print(f"   {i}. {domain}")
        if len(domains) > 5:
            print(f"   ... and {len(domains) - 5} more")
    else:
        print("❌ Failed to get domains")
        return False
    
    # Test 3: Check messages
    print("\n📬 Test 3: Checking messages...")
    print("⏳ Waiting a moment for any potential messages...")
    time.sleep(5)
    
    messages = fake_mail.get_messages()
    
    if messages is not None:
        print(f"✅ Successfully checked inbox")
        if messages:
            print(f"📧 Found {len(messages)} message(s):")
            for msg in messages:
                print(f"   - From: {msg.get('from', {}).get('address', 'Unknown')}")
                print(f"     Subject: {msg.get('subject', 'No subject')}")
        else:
            print("📭 Inbox is empty (expected for new email)")
    else:
        print("❌ Failed to check messages")
        return False
    
    # Test 4: Display credentials
    print("\n🔐 Email Account Credentials:")
    print(f"   Email: {fake_mail.email}")
    print(f"   Password: {fake_mail.password}")
    print(f"   API Token: {fake_mail.token[:30]}..." if fake_mail.token else "   API Token: None")
    
    print("\n" + "=" * 60)
    print("✅ All tests completed successfully!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_fakemail()
