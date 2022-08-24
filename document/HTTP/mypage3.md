# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## Match History Detail


### 概要

Match History Detail MyPage三番目のAPI

### バックエンド作成状況
<font color="#87cefa">未実装</font>

### リクエスト

#### パス

`/match-history/<userId>/<roomId>`

#### メソッド
- GET

#### リクエストヘッダー

| パラメータ名       | 内容      |
|--------------|---------|
| Authorization       | JWTトークン |

#### リクエストパスパラメータ

| パラメータ名 | 内容      |
|--------|---------|
| userId | ユーザーのID |
| roomId | ルームのID  |



#### リクエストサンプル
`http://localhost:8099/match-history/id-002/uuid-01`


### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名          | 型      | 内容                        |
|-----------------|--------|---------------------------|
| status          | int    | レスポンスステータス                |
| userId          | string | ユーザーID                    |
| userName        | string | ユーザー名                     |
| startTime       | string | 開始時間(yyyy/mm/dd hh:mm:ss) |
| questionId      | string | 問題ID                      |
| questionName    | string | 問題タイトル                    |
| questionContext | string | 問題文                       |
| gameResult      | array  | ゲームの対戦履歴(上から順位高め)         |
| histories       | array  | コード履歴                     |


#### gameResult配列の中のオブジェクト

| パラメータ名      | 型      | 内容                   |
|-------------|--------|----------------------|
| userName    | string | ユーザ名                 |
| scoreTime   | string | テストケースが終わった時間(mm:ss) |
| rankBadge | int    | ランクバッジを表す数値(低いほど高い) |
| ranking     | int    | ランキング                |

#### histories配列の中のオブジェクト

| パラメータ名    | 型       | 内容                            |
|-----------|---------|-------------------------------|
| historyId | string  | コード履歴ID                       |
| debugTime | string  | デバッグした時間(yyyy/mm/dd hh:mm:ss) |
| code      | string  | プログラムコード                      |
| isExecuteTest    | boolean | テストケース実行かどうか                  |
| isProgramError    | boolean | プログラムがエラーかどうか                 |
| programOutput    | boolean | 標準出力                          |
| programError    | boolean | プログラムのエラー                     |
| isClearTestCases    | boolean | テストケースが全て通ったか                 |
| testCaseTotal    | int     | テストケース数                       |
| testCaseClearTotal    | int     | テストケースがクリアした数                 |


  "isExecuteTest" boolean,
  "isProgramError" boolean,
  "programOutput" text,
  "programError" text,
  "testCaseTotal" int,
  "testCaseClearTotal" int,


#### レスポンスサンプル

```JSON
{
  "status": 200,
  "userId": "id-001",
  "userName": "パオパオ",
  "startTime": "2022/08/26 14:56:41",
  "questionId": "Q_03",
  "questionName": "暗号解読",
  "questionContext": "問題文-----問題文-----",
  "gameResult": [
    {
      "userName": "オレンジの神様",
      "scoreTime": "08:56",
      "rankBadge": 2,
      "ranking": 1
    },
    {
      "userName": "サイボーグ人間",
      "scoreTime": "10:46",
      "rankBadge": 5,
      "ranking": 2
    },
    {
      "userName": "はさみんと",
      "scoreTime": "20:00",
      "rankBadge": 3,
      "ranking": 3
    }
  ],
  "histories": [
    {
      "historyId": "hd-004",
      "debugTime": "2022/08/26 15:07:14",
      "code": "print(\"Hello\")",
      "isExecuteTest": false,
      "isProgramError": false,
      "programOutput": "Hello",
      "programError": "",
      "isClearTestCases": false,
      "testCaseTotal": 0,
      "testCaseClearTotal": 0
    },
    {
      "historyId": "hd-006",
      "debugTime": "2022/08/26 15:08:53",
      "code": "print(\"Hello)",
      "isExecuteTest": false,
      "isProgramError": true,
      "programOutput": "",
      "programError": "error!!!",
      "isClearTestCases": false,
      "testCaseTotal": 0,
      "testCaseClearTotal": 0
    },
    {
      "historyId": "hd-012",
      "debugTime": "2022/08/26 15:16:41",
      "code": "print(\"Hello, Hello\")",
      "isExecuteTest": true,
      "isProgramError": false,
      "programOutput": "Hello, Hello",
      "programError": "",
      "isClearTestCases": true,
      "testCaseTotal": 5,
      "testCaseClearTotal": 5
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





