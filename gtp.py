import requests
import json

cookies = {
    'session-id': '132-5312887-9428840',
    'ad-oo': '0',
    'ci': 'eyJpc0dkcHIiOmZhbHNlfQ',
    'ubid-main': '132-2202699-7637707',
    'at-main': 'Atza|IwEBIIhZ4ns4Huk1ftaJIcd2DVhJOTSlrpxLoE70QHiyetFPr7_FHsOEP_Z07q2z4drp2jhIRNUYftOMfevscGMt1g6KBvOaSgPf-VSalsZ2lAGidJ1S5DrH5ap6Rzx1GlKRQ5p6IpezphfbkTKUPOB0Fe28lAgs5BwckldNHfKWwj3AS8pc3MCKqWU6-gHiFHywOIekC5tx1571GExzpwYZVx1Cmug_ds7trK_Kdxh-awfWbA',
    'sess-at-main': 'dyh7lGTSX//CX/vXoOk3ObsKQKznw4LG+lXInveSimY=',
    'session-id-time': '2082787201l',
    'uu': 'eyJpZCI6InV1ZjRkM2Y0M2UxZTU5NDMwN2EyZjEiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=',
    'signup-offer-territory': 'IN',
    'x-main': '6kWkQsiWmVaQ6tOVl9v2eIJ3vwe9PT9sTzEC0uLpEPzmKondTasnFd5WarFJ96mF',
    'session-token': 'q2tWvYOEBpsWvtJebVgvfGwRzYHGnXKEgVL9DntSwMz3f4WDUu5myP2hlnkJvbg/VbHmXN7Yt5hduaR5pftFUFYyNYDlLFxX1tOACSK1xdnOVzoi0OZVjMEyiktbhYT6y0tH1uOM4sxRc+eRSWPBMkjPwDUPaDbRi75Np+HUC592VlUIw1t2sxAxVFdHJCJ/X7bZHd3PS1cIACyoAybB+3dpVorukTLZ6wwqY04zWHFvQalwE3rACoDYxcNw5FlTRVkXe6ITm4+bvLT2ejhq+SAWbWUV72mcBKSKMrnF22l9wOHt+YBwykzUCHEtcedCjxBZQkR6V9SojF3yQVzPTZPrPXI6V5OPgOKmS0+/adQhxH0XKG1Elr4KiFwcGbEP',
    'international-seo': 'es',
}

headers = {
    'accept': 'application/graphql+json, application/json',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
    'content-type': 'application/json',
    'origin': 'https://www.imdb.com',
    'priority': 'u=1, i',
    'referer': 'https://www.imdb.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-amzn-sessionid': '132-5312887-9428840',
    'x-imdb-client-name': 'imdb-web-next-localized',
    'x-imdb-client-rid': '0HD8HQPMX9QM9SB6XAF9',
    'x-imdb-consent-info': 'eyJpc0dkcHIiOmZhbHNlfQ',
    'x-imdb-user-country': 'MX',
    'x-imdb-user-language': 'es-MX',
    'x-imdb-weblab-treatment-overrides': '{}',
    # 'cookie': 'session-id=132-5312887-9428840; ad-oo=0; ci=eyJpc0dkcHIiOmZhbHNlfQ; ubid-main=132-2202699-7637707; at-main=Atza|IwEBIIhZ4ns4Huk1ftaJIcd2DVhJOTSlrpxLoE70QHiyetFPr7_FHsOEP_Z07q2z4drp2jhIRNUYftOMfevscGMt1g6KBvOaSgPf-VSalsZ2lAGidJ1S5DrH5ap6Rzx1GlKRQ5p6IpezphfbkTKUPOB0Fe28lAgs5BwckldNHfKWwj3AS8pc3MCKqWU6-gHiFHywOIekC5tx1571GExzpwYZVx1Cmug_ds7trK_Kdxh-awfWbA; sess-at-main=dyh7lGTSX//CX/vXoOk3ObsKQKznw4LG+lXInveSimY=; session-id-time=2082787201l; uu=eyJpZCI6InV1ZjRkM2Y0M2UxZTU5NDMwN2EyZjEiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; signup-offer-territory=IN; x-main=6kWkQsiWmVaQ6tOVl9v2eIJ3vwe9PT9sTzEC0uLpEPzmKondTasnFd5WarFJ96mF; session-token=q2tWvYOEBpsWvtJebVgvfGwRzYHGnXKEgVL9DntSwMz3f4WDUu5myP2hlnkJvbg/VbHmXN7Yt5hduaR5pftFUFYyNYDlLFxX1tOACSK1xdnOVzoi0OZVjMEyiktbhYT6y0tH1uOM4sxRc+eRSWPBMkjPwDUPaDbRi75Np+HUC592VlUIw1t2sxAxVFdHJCJ/X7bZHd3PS1cIACyoAybB+3dpVorukTLZ6wwqY04zWHFvQalwE3rACoDYxcNw5FlTRVkXe6ITm4+bvLT2ejhq+SAWbWUV72mcBKSKMrnF22l9wOHt+YBwykzUCHEtcedCjxBZQkR6V9SojF3yQVzPTZPrPXI6V5OPgOKmS0+/adQhxH0XKG1Elr4KiFwcGbEP; international-seo=es',
}

bio_text = "[url=https://click.hdfree.site/Adult/]🌐 𝖢𝖫𝖨𝖢𝖪 𝖧𝖤𝖱𝖤 🌐==►►[/url]"  # Remove adult links to pass validation

json_data = {
    'query': '''
        mutation UpdateUserBio($bioText: String!, $originalTitleText: Boolean!) {
          updateUserProfileBio(input: {bio: $bioText}) {
            status {
              updateStatus
              modifiedItem {
                plaidHtml(showLineBreak: true, showOriginalTitleText: $originalTitleText)
                markdown
              }
              updateFeedback {
                validationFeedback {
                  message {
                    value {
                      plainText
                    }
                  }
                  status
                }
              }
            }
          }
        }
    ''',
    'operationName': 'UpdateUserBio',
    'variables': {
        'bioText': bio_text,
        'originalTitleText': False,
    },
}

response = requests.post('https://api.graphql.imdb.com/', cookies=cookies, headers=headers, json=json_data)

# Check response
try:
    resp_json = response.json()
    print(json.dumps(resp_json, indent=2))
    
    status = resp_json.get("data", {}).get("updateUserProfileBio", {}).get("status", {}).get("updateStatus")
    if status == "SUCCESS":
        print("Bio updated successfully!")
    else:
        print("Failed to update bio. Validation messages:")
        feedback = resp_json.get("data", {}).get("updateUserProfileBio", {}).get("status", {}).get("updateFeedback", {}).get("validationFeedback", [])
        for f in feedback:
            print(f.get("message", {}).get("value", {}).get("plainText", "No message"))
except Exception as e:
    print("Error parsing response:", e)
    print(response.text)

