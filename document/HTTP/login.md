# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## ログイン


### 概要

ログイン処理

### バックエンド作成状況
<font color="#b22222">未実装</font>

### リクエスト

#### パス

`/login`

#### メソッド
- POST
  - JSON (Req/Res)

#### リクエストボディ

| パラメータ名       | 型      | 内容           |
|--------------|--------|--------------|
| userEmail       | string | ユーザーのメールアドレス |
| userPassword | string | ユーザーのパスワード   |



#### リクエストサンプル

```JSON
{
  "userEmail": "hoge@Kmail.com",
  "userPassword": "password"
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
| userId | string | ユーザーID     |
| userName     | string | ユーザ名       |

#### レスポンスサンプル

```JSON
{
  "status": 200,
  "userId": "id-0001",
  "userName": "Hamachan"
}
```





