# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## Match History


### 概要

Match History MyPage二番目のAPI

### バックエンド作成状況
<font color="#87cefa">未実装</font>

### リクエスト

#### パス

`/match-history/<userId>`

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
`http://localhost:8099/match-history/id-002`


### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名 | 型     | 内容         |
|--------|-------|------------|
| status | int   | レスポンスステータス |
| rooms  | array | 対戦履歴の配列    |


#### rooms配列の中のオブジェクト

| パラメータ名      | 型      | 内容                        |
|-------------|--------|---------------------------|
| roomId      | string | ルームID                     |
| roomName    | string | ルーム名                      |
| startTime   | string | ゲーム開始時間(yyyy/mm/dd hh:mm) |
| playerCount | int    | プレイヤー数                    |
| players     | array  | プレイヤーの名前が格納               |


#### レスポンスサンプル

```JSON
{
  "status": 200,
  "rooms": [
   {
      "roomId": "uuid-002",
      "roomName": "パパイヤ",
      "startTime": "2022/08/26 14:54",
      "playerCount": 3,
      "players": ["かぼじい", "淀義橋太郎", "パワーマントヒヒ"]
    }, 
    {
      "roomId": "uuid-002",
      "roomName": "パオーンクラブ",
      "startTime": "2022/08/26 16:29",
      "playerCount": 4,
      "players": ["サーキュレーター佐藤", "サンタ", "パワーマントヒヒ", "java大好きマン"]
    }
  ]
  
}
```

#### エラーレスポンスサンプル
```JSON
{
  "status": 400, 
  "message": "Match History情報が取得できませんでした。"
}
```





