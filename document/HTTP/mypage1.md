# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## MyPage Top


### 概要

MyPage Top 一番最初のAPI

### バックエンド作成状況
<font color="#87cefa">未実装</font>

### リクエスト

#### パス

`/mypage/<userId>`

#### メソッド
- GET
  

#### リクエストヘッダー

| パラメータ名       | 内容      |
|--------------|---------|
| Authorization       | JWTトークン |

#### リクエストパスパラメータ

| パラメータ名 | 内容            |
|--------|---------------|
| userId | ユーザーのID   |



#### リクエストサンプル
`http://localhost:8099/mypage/id-002`


### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名    | 型      | 内容                  |
|-----------|--------|---------------------|
| status    | int    | レスポンスステータス          |
| userId    | string | ユーザーID              |
| userName  | string | ユーザー名               |
| rankBadge | int    | ランクバッジを表す数値(低いほど高い) |
| score     | int    | スコア                 |

#### レスポンスサンプル

```JSON
{
  "status": 200,
  "userId": "id-002",
  "userName": "パパイヤ",
  "rankBadge": 3,
  "score": 18000
}
```

#### エラーレスポンスサンプル
```JSON
{
  "status": 400, 
  "message": "MyPage情報が取得できませんでした。"
}
```





