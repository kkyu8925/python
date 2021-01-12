import requests
res = requests.get("http://naver.com")
res.raise_for_status()  # 문제생기면 err 생성
# print("응답코드 : ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("success")
# else:
#     print("err! [errcode", res.status_code, "]")

print(len(res.text))
