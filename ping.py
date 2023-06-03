import requests,json

with open("input.png", "rb") as f:
    x = requests.post(f"http://127.0.0.1:5000/?sampleSize={10}", files={"file" : f})

print(json.loads(x.text)["output"])