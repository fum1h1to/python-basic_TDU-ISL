# jsonモジュールをimportしてみよう
import json


# jsonでデータを作成してみよう
json_text = '{"name": "Taro", "age": 12, "country": "Japan"}'


# 作成したデータから1つの値を取り出してみよう
d = json.loads(json_text)

print(d["name"])