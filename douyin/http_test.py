import requests
import time

if __name__ == '__main__':
    print(round(time.time() * 1000))
    response = requests.get("https://aweme.snssdk.com/aweme/v1/aweme/post/?user_id=52909715796&max_cursor=0&count=20&retry_type=no_retry&iid=96960461524&device_id=70015318587&ac=wifi&channel=gdt_growth1_cp1&aid=1128&app_name=aweme&version_code=180&version_name=1.8.0&device_platform=android&ssmix=a&device_type=Nexus+5&device_brand=google&language=zh&os_api=23&os_version=6.0.1&openudid=2e605ca84d82e31a&manifest_version_code=180&resolution=1080*1776&dpi=480&update_version_code=1800&_rticket=1577330752501&ts=1577330752&as=aa9b2d71a85e0428409b2d&cp=71f89b2d71a89b2d71f032&mas=01999323b9b3d3197379a3b9b9451f2b3d197379a3331323731333",
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                     'Cookie': 'odin_tt=840fdb02d02dcea77ba2992a54e0720bb1c0b608126e442c3fa46b625f3711bc267212fe3e5fc49dbad39e4c65ebba153b4f1a9e60a4b0d7392cb86b78179456; qh[360]=1; install_id=96960461524; ttreq=1$641e5aed6cc4f663077637e33e984a66ef9a7359], accept-encoding=[gzip], user-agent=[com.ss.android.ugc.aweme/900 (Linux; U; Android 6.0.1; zh_CN; Nexus 5; Build/M4B30Z; Cronet/58.0.2991.0)',
                     'X-Gorgon': '',
                     'X-Khronos': '',
                     'X-SS-REQ-TICKET': '1577330752506',
                     'X-SS-TC': '0',
                 })
    print(response.text)