import json
import requests

KAKAO_TOKEN = 'iFaW1uwtsID_hMYUCjXCd-6O3Hao1G6A7d1riQorDR8AAAF7E_qb2g'
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {'Authorization': 'Bearer' + KAKAO_TOKEN}


data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "Google 뉴스: drone",
                                     "link" : {
                                                 "web_url" : "https://www.google.co.kr/search?q=drone&source=lnms&tbm=nws",
                                                 "mobile_web_url" : "https://www.google.co.kr/search?q=drone&source=lnms&tbm=nws"
                                              }
    })
}

response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))













# KAKAO_TOKEN = 'iFaW1uwtsID_hMYUCjXCd-6O3Hao1G6A7d1riQorDR8AAAF7E_qb2g'


# # POST /v2/api/talk/memo/default/send HTTP/1.1
# # Host: kapi.kakao.com
# # Authorization: Bearer {ACCESS_TOKEN}


# header = {'Authorization': 'Bearer' + KAKAO_TOKEN}
# url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
# post = {
#     "object_type": "commerce",
#         "content": {
#             "title": "Hotel Sale information",
#             "image_url": discount.find('img').attrs['src'],
#             "image_width": 640,
#             "image_height": 640,
#             "link": {
#             "web_url":  discount.attrs['href'],
#             "android_execution_params": "contentId=100",
#             "ios_execution_params": "contentId=100"
#             }
#         }}

# dt = {'template_object':json.dumps(post)}
# requests.post(url, headers = header,data = dt)
https://kauth.kakao.com/oauth/authorize?client_id={a843089727664a635222385ec0c13bf5}&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message