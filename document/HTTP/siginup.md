# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## 新規登録

### 概要

新規登録処理

### バックエンド作成状況
<font color="#00fa9a">実装</font>

### リクエスト

#### パス

`/signup`



#### メソッド
- POST
  - JSON (Req/Res)

#### リクエストボディ

| パラメータ名       | 型      | 内容           |
|--------------|--------|--------------|
| userEmail       | string | ユーザーのメールアドレス |
| userPassword | string | ユーザーのパスワード   |
| userName     | string | ユーザ名         |



#### リクエストサンプル

```JSON
{
  "userEmail": "hoge@Kmail.com",
  "userPassword": "password",
  "userName": "Hamachan"
}
```

### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスヘッダー

| パラメータ名       | 内容      |
|--------------|---------|
| Authorization       | JWTトークン |


#### レスポンスボディ

| パラメータ名       | 型      | 内容         |
|--------------|--------|------------|
| status       | int    | レスポンスステータス |
| userId | string | ユーザーのID    |
| userName     | string | ユーザ名       |

#### レスポンスサンプル

```JSON
{
  "status": 200,
  "userId": "id-0001",
  "userName": "Hamachan"
}
```


#### エラーレスポンスサンプル
```JSON
{
  "status": 400, 
  "message": "既に存在しているメールアドレスです。"
}
```





