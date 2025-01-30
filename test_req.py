import http.client
import json
import re

def get_data(prod_id: int, api=True):
    match api: 
        case True:

            conn = http.client.HTTPSConnection("api.ozon.ru")

            payload = ""

            headers = {
                'cookie': "__Secure-ETC=f79d30e25340e3dc7799f5dc6d1eda00; __Secure-ab-group=92; TS0121feed=0187c00a18a4735031ee777d6e17230e0c530489ccbb72a90f26a46fc079fd224467fbb3561c3b20a6df03249a02a41d564b8ff406; xcid=4a05c1bb4ff376f58bd034f864e29223; __Secure-ext_xcid=4a05c1bb4ff376f58bd034f864e29223; ADDRESSBOOKBAR_WEB_CLARIFICATION=1738083476; rfuid=NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxOTA3MzMzOTM0LC0xLDEzMTM1MjM4NjIsVzNzaWJtRnRaU0k2SWxCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxbElGQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMXBkVzBnVUVSR0lGWnBaWGRsY2lJc0ltUmxjMk55YVhCMGFXOXVJam9pVUc5eWRHRmliR1VnUkc5amRXMWxiblFnUm05eWJXRjBJaXdpYldsdFpWUjVjR1Z6SWpwYmV5SjBlWEJsSWpvaVlYQndiR2xqWVhScGIyNHZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlN4N0luUjVjR1VpT2lKMFpYaDBMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4xZGZTeDdJbTVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNCUVJFWWdWbWxsZDJWeUlpd2laR1Z6WTNKcGNIUnBiMjRpT2lKUWIzSjBZV0pzWlNCRWIyTjFiV1Z1ZENCR2IzSnRZWFFpTENKdGFXMWxWSGx3WlhNaU9sdDdJblI1Y0dVaU9pSmhjSEJzYVdOaGRHbHZiaTl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOUxIc2lkSGx3WlNJNkluUmxlSFF2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZWMTlMSHNpYm1GdFpTSTZJbGRsWWt0cGRDQmlkV2xzZEMxcGJpQlFSRVlpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgxZCxXeUp5ZFNKZCwwLDEsMCwyNCwyMzc0MTU5MzAsOCwyMjcxMjY1MjAsMCwxLDAsLTQ5MTI3NTUyMyxSMjl2WjJ4bElFbHVZeTRnVG1WMGMyTmhjR1VnUjJWamEyOGdWMmx1TXpJZ05TNHdJQ2hYYVc1a2IzZHpJRTVVSURFd0xqQTdJRmRwYmpZME95QjROalFwSUVGd2NHeGxWMlZpUzJsMEx6VXpOeTR6TmlBb1MwaFVUVXdzSUd4cGEyVWdSMlZqYTI4cElFTm9jbTl0WlM4eE16SXVNQzR3TGpBZ1UyRm1ZWEpwTHpVek55NHpOaUF5TURBek1ERXdOeUJOYjNwcGJHeGgsZXlKamFISnZiV1VpT25zaVlYQndJanA3SW1selNXNXpkR0ZzYkdWa0lqcG1ZV3h6WlN3aVNXNXpkR0ZzYkZOMFlYUmxJanA3SWtSSlUwRkNURVZFSWpvaVpHbHpZV0pzWldRaUxDSkpUbE5VUVV4TVJVUWlPaUpwYm5OMFlXeHNaV1FpTENKT1QxUmZTVTVUVkVGTVRFVkVJam9pYm05MFgybHVjM1JoYkd4bFpDSjlMQ0pTZFc1dWFXNW5VM1JoZEdVaU9uc2lRMEZPVGs5VVgxSlZUaUk2SW1OaGJtNXZkRjl5ZFc0aUxDSlNSVUZFV1Y5VVQxOVNWVTRpT2lKeVpXRmtlVjkwYjE5eWRXNGlMQ0pTVlU1T1NVNUhJam9pY25WdWJtbHVaeUo5ZlgxOSw2NSwtMTI4NTU1MTMsMSwxLC0xLDE2OTk5NTQ4ODcsMTY5OTk1NDg4NywxMTY0MjQ2OTU5LDEy; guest=true; TS018529d3=0187c00a1891c03d18d9cb158c13b3bf16c30d3e707330ea16fb7567f2561e2f915c60583d6e91874acdc6794f832eaa80aa7785c5; __Secure-access-token=7.63613560.355wsad4QTy5akZd_p11MQ.92.AVy5VWXmGOx2cg0c55NEeCCOf7VBKJQZNwEPHIfD_KAnXnniovGVLQspQGS1SqDvvAVzwKdNaY29K16g1fc5Npo.20210315083726.20250128185815.yUHReZTu4gB1FzxOpww1d8C1RiVvUiL7PrHls3WNbMU.1cfb2cc5625394264; __Secure-refresh-token=7.63613560.355wsad4QTy5akZd_p11MQ.92.AVy5VWXmGOx2cg0c55NEeCCOf7VBKJQZNwEPHIfD_KAnXnniovGVLQspQGS1SqDvvAVzwKdNaY29K16g1fc5Npo.20210315083726.20250128185815.08ko_8i2KFK9UA5w9Jrg17gS8RTkl6tEqo53xtws3MQ.1243b2aac69722ff0; __Secure-user-id=63613560; is_adult_confirmed=; is_alco_adult_confirmed=; abt_data=7.XWuRfqAf_I9iT-kb-8NvYxEzKjWYx0afs-Gv8ov5vQ-Wo-9wtbHef-BmLz4Bblq7HcF4grb6BZsXPGCE64GYmVfLJZ5SdA4F5AtQS15RBo1RLwYJXrtc_L022nXWRYQo4qyLHKouYokzFO2g-D9KSv60PW41-IgmV_mclWA-wbGTF2uzZk2hIisLJ0tFUqpN7a8GeTqEL92VmuNzGnYm56tznT6a6hcHFHRDRwbvdDSLfO_Fn_6EAa0a-lG1KMb6XsG49HMqAJ8TlR9r_wZEgv7bgGeNnEqRUa_qnA-DCa_Nu_WhwWk1fF8optas-4KLEbQx9FUZG115AJGNI-LPD-KIS1uFqxfmN8IcO7wbaJ5sFYw3eBX0VNbD65T-ERLD9Pg6uVEkHqXXmQxggQomGFB80kit5ngnmRGKZza3oMPCmnn745Rg23aKQf5Ah3eCSATjq8lZCojz69Jd5PIwZQ",
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                'accept-language': "ru,en;q=0.9",
                'cache-control': "max-age=0",
                'priority': "u=0, i",
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': "?0",
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': "document",
                'sec-fetch-mode': "navigate",
                'sec-fetch-site': "none",
                'sec-fetch-user': "?1",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
                }

            conn.request("GET", f"/composer-api.bx/page/json/v2?url=%2Fproduct%2F{prod_id}", payload, headers)

            res = conn.getresponse()
            data = res.read()
            exists = True if 'available' else False
            json_data = json.loads(data.decode("utf-8"))
            # print(json_data.keys())
            price_key_pattern = r"webPrice-\d+-default-1"
            title_key_pattern = r"webAspects-\d+-default-1"
            title, price = None, None
            for key in json_data['widgetStates'].keys():
                if re.match(title_key_pattern, key): 
                    title = json.loads(json_data['widgetStates'][key])['aspects'][0]['variants'][0]['data']['title']
                    break
            for key in json_data['widgetStates'].keys():
                if re.match(price_key_pattern, key):
                    # print(f'Price-key: {key}')
                    price = json.loads(json_data['widgetStates'][key])['price']
                    price = int(price.replace(' ', '').replace('₽', ''))
                    break
            print(f"Price: {price} Title: {title} Existing: {exists}")
            if title and price:
                return True
            



if __name__ == "__main__":
    get_data(1594377525)
    get_data(1635886192)
