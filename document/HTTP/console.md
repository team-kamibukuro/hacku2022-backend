# API設計書


<!----
未実装：#b22222
実装中：#87cefa
実装：#00fa9a
--->


## コンソール実行


### 概要

コンソール実行用API。実行結果、エラー発生したかどうかを返す。

### バックエンド作成状況
<font color="#00fa9a">実装</font>

### リクエスト

#### パス

`/console`

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
| language   | string | プログラミング言語  |
| questionId | string | 問題ID       |
| roomId     | string | 部屋ID       |
| userId     | string | ユーザーId     |



#### リクエストサンプル

```JSON
{
  "code": "print(\"hello worl\")",
  "language": "java",
  "questionId": "DQ_01",
  "roomId": "uuid",
  "userId": "id-003"
}
```

### レスポンス

#### ステータスコード

- 成功: 200
- 失敗: 400


#### レスポンスボディ

| パラメータ名 | 型       | 内容                    |
|--------|---------|-----------------------|
| status | int     | レスポンスステータス,400 or 200 |
| isCompileError | boolean | コンパイルエラーをしているかどうか     |
| programError  | string  | コンパイルエラーメッセージ         |
| programOutput | string  | コンソール実行結果             |

#### レスポンスサンプル

```JSON
{
  "status":200,
  "isCompileError": false,
  "programError":"prog.cc: In function 'int main()':\n\u003ccommand-line\u003e:0:3: warning: unused variable 'hogefuga' [-Wunused-variable]\nprog.cc:2:18: note: in expansion of macro 'x'\n int main() { int x = 0; std::cout \u003c\u003c \"hoge\" \u003c\u003c std::endl; }\n                  ^\n",
  "programOutput":"hoge\n"
}
```





