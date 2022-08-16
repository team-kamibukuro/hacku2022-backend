# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## ルーム作成


### 概要

ルーム作成用API

### バックエンド作成状況
<font color="#b22222">未実装</font>

### リクエスト

#### パス

`/room`

#### メソッド
- POST
  - json (Req/Res)

#### リクエストヘッダー

| パラメータ名       | 内容      |
|--------------|---------|
| Authorization       | JWTトークン |

#### リクエストボディ

| パラメータ名   | 型      | 内容          |
|----------|--------|-------------|
| masterUserId   | string | マスターユーザーのID |
| roomName | string | ルーム名        |



#### リクエストサンプル

```JSON
{
  "masterUserId": "user-0001",
  "roomName": "パオーン・プログラミングクラブ"
}
```

### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名   | 型      | 内容         |
|----------|--------|------------|
| status   | int    | レスポンスステータス |
| roomId   | string | 部屋ID       |
| roomName | string | 部屋名        |
| masterUserId | string | マスターユーザID  |

#### レスポンスサンプル

```JSON
{
  "status": 200,
  "roomId": "UUID-001",
  "roomName": "パオーン・プログラミングクラブ",
  "masterUserId": "user-0001"
}
```

#### エラーレスポンスサンプル
```JSON
{
  "status": 400, 
  "message": "既に存在しているルーム名です。"
}
```





