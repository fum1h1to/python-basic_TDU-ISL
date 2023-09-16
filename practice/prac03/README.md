# 課題 3

## 問題

Tech Corpの授業員データをjson形式で受け取りました。次の3つの情報をprint文で出力してください

- 会社の本部
- idが1である従業員の名前
- Eveが受け持っているprojectの名前

※ json.loadsを用い、辞書型にしてから取り出してください。

なお、受け取ったjsonデータは次のような情報が入ります。

| キー名 | 概要 | データ形式 |
| ---- | ---- | ---- |
| company | 会社名 | string |
| headquarters | 本部 | string |
| departments | 部門 | list of string |
| employees | 従業員 | list of ```Employee``` |


*Employee*

| キー名 | 概要 | データ形式 |
| ---- | ---- | ---- |
| id | ID | int |
| name | 従業員名 | string |
| department | 部門 | string |
| projects | プロジェクト | list of ```Project``` |


*Project*

| キー名 | 概要 | データ形式 |
| ---- | ---- | ---- |
| id | ID | int |
| name | プロジェクト名 | string |
| status | ステータス | string |

## 出力例

```
会社の本部: ------
idが1である従業員の名前: ------
Eveが受け持っているprojectの名前: ------, ------
```

※ 複数ある場合は```,```(カンマ)で区切る

## 提出

`共有フォルダ` に `ディレクトリ名/ファイル名` の形式で提出してください。

- 期限: 2022/12/31 23:59 まで
- 共有フォルダ: [Box]()
- ディレクトリ名: 学籍番号
- ファイル名: `prac03.py`
