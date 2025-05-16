import requests
import time
import hashlib

url = 'https://openapi.kuajingmaihuo.com/openapi/router' #bg

type = "bg.purchaseorder.get"
timestamp = int(time.time()) # 获取时间戳
app_key = "a26c7b85bcfde56f2e441d9b1eff1ab6"
access_token = "r2ccdckajxn34oz8buntunangifigzo1a0mo9tddkx0be1qqbr3rurvp"
app_secret = "b3ae2360321f5f77a3d0e3694cafe7e6441c80aa"

#bg
data = {
    "type": type,
    "timestamp": timestamp,
    "app_key": app_key, 
    "access_token": access_token,
    "pageNo": 1,
    "pageSize": 10
    
}


# 生成签名（所有参数按字典序排序后拼接，然后计算 MD5）
sorted_params = sorted(data.items(), key=lambda x: x[0])  # 按字典序排序
sign_str = app_secret +  "".join([f"{k}{v}" for k, v in sorted_params]) + app_secret  # 拼接字符串
sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()  # 计算 MD5 并转为大写

# 将签名添加到请求参数中
data["sign"] = sign

headers = {
    'Content-Type': 'application/json'
    #'Authorization': '1'
}
response = requests.post(url, headers=headers, json=data)
#print(response.content.decode('utf-8'))
print(response.text)

