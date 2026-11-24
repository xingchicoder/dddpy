import requests

url = "https://api.siliconflow.cn/v1/audio/speech"
payload = {
    "model": "fnlp/MOSS-TTSD-v0.5",
    "input": "你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦",
    "voice": "fnlp/MOSS-TTSD-v0.5:alex",
    "response_format": "mp3"
}
headers = {
    "Authorization": "Bearer sk-ykgorbxbkythpzudfjluwkbxwzhxkuinwwktzorcesdpsrmn",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
with open("output.mp3", "wb") as f:
    f.write(response.content)
