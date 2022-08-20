# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## テストケース実行


### 概要

テストケース実行用API。テストケースにどれだけ通っているか、エラー発生したかどうかを返す。

### バックエンド作成状況
<font color="#00fa9a">実装</font>

### リクエスト

#### パス

`/testcase`

#### メソッド
- POST
  - json (Req/Res)

#### リクエストヘッダー

| パラメータ名       | 内容      |
|--------------|---------|
| Authorization       | JWTトークン |

#### リクエストボディ

| パラメータ名     | 型      | 内容         |
|------------|--------|------------|
| code       | string | プログラミングコード |
| questionId | string | 問題文ID      |
| language | string | プログラミング言語  |



#### リクエストサンプル

```JSON
{
  "code": "print(\"hello worl\")",
  "language": "python",
  "testId": "test-00001"
}
```

### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名             | 型       | 内容                |
|--------------------|---------|-------------------|
| status             | int     | レスポンスステータス        |
| questionId         | string  | 問題ID              |
| isClearTestCases   | boolean | テストケースが全て成功したかどうか |
| testCaseTotal      | int     | テストケースの合計         |
| testCaseClearTotal | int     | テストケースが通った数       |
| testCases          | Array   | テストケースの結果         |

##### testCases中のオブジェクト

| パラメータ名             | 型       | 内容                |
|--------------------|---------|-------------------|
| testCaseId         | string  | テストケースID          |
| isCompileError     | boolean | コンパイルエラーをしているかどうか |
| compilerError      | string  | コンパイルエラーメッセージ     |
| isClearTestCase    | boolean | テストケースが通ったかどうか    |


#### レスポンスサンプル

```JSON
{
  "status":200,
  "questionId": "q-0002",
  "isClearTestCases": false,
  "testCaseTotal": 5,
  "testCaseClearTotal": 3,
  "testCases": [
    {
      "testCaseId": "qt-001",
      "isCompileError": true,
      "compilerError": "",
      "isClearTestCase": true
    },
    {
      "testCaseId": "qt-002",
      "isCompileError": true,
      "compilerError": "",
      "isClearTestCase": true
    },
    {
      "testCaseId": "qt-003",
      "isCompileError": true,
      "compilerError": "",
      "isClearTestCase": false
    },
    {
      "testCaseId": "qt-004",
      "isCompileError": false,
      "compilerError": "syntax error",
      "isClearTestCase": false
    },
    {
      "testCaseId": "qt-005",
      "isCompileError": true,
      "compilerError": "",
      "isClearTestCase": true
    }
  ]
}
```





