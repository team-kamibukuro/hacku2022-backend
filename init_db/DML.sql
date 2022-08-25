INSERT INTO users
VALUES ('id-001', 'Tom', 'test1@test.com', 'pass', 1, 32000, '2022-08-16 08:24:36,835'),
        ('id-002', 'イカダ猫', 'test2@test.com', 'pass', 4, 15000, '2022-08-16 08:24:36,835' ),
        ('id-003', '空飛ぶ農家', 'test3@test.com', 'pass', 6, 0, '2022-08-16 08:24:36,835'),
         ('id-004', 'いちご狩り宇宙人', 'test4@test.com', 'pass', 5, 9000, '2022-08-16 08:24:36,835'),
        ('id-005', '薬剤師', 'test5@test.com', 'pass', 2, 21000, '2022-08-16 08:24:36,835'),
         ('id-006', 'サーキュレータ鯖缶', 'test6@test.com', 'pass', 3, 19000 , '2022-08-16 08:24:36,835');

INSERT INTO rooms
VALUES ('room01', 'id-001', 'タコパ', null, false, false, 4),
('room02', 'id-004', '錦鯉クラブ', null, false, false, 3),
('room03', 'id-002', '3-4クラスルーム', null, true, false, 2),
('room04', 'id-002', '野球大好き連合', null, false, true, 3),
('room05', 'id-005', '強化合宿', null, false, true, 4);

INSERT INTO questions
VALUES ('Q_01', 'ビンゴゲーム', 'ビンゴゲームのカードの中に何個ビンゴしているかを判定するプログラムを記述してください。ビンゴは縦、横、斜めで判定されます。
5 × 5のマスにそれぞれに1〜75までの数字と抽選番号総数(1 ≦ n ≦ 50 )、抽選番号を入力値として渡します。ビンゴカードの中の数字は一意になっています。
入力値の1 〜 5行にはビンゴカードの数字が入っています。6行目には抽選番号の数が入り、7行目には抽選番号一覧が入力値として入ります。

入力値例
32 64 55 5 7
12 41 44 18 29
70 59 11 2 25
17 54 10 36 72
22 67 23 47 34
19
59 7 3 22 45 36 25 5 11 22 70 27 7 48 32 15 17 12 74

出力値例
2'),
('Q_02', 'Hit and Blow', 'Hit and Blowという数当てゲームのプログラムを記述してください。Hit and Blowのルールは出題者がまず初めに0123〜9876(数字は一意)の範囲の数字を正解として選ぶ。次に、解答者は予想する数字を言う。出題者は同じ桁（位置）に同じ数字があればヒット、桁は違うが同じ数字があればブローの数を答えて、出題者の数字を当てるゲームになっています。
例
正解：4819 予想：3014　->　ヒット：１ ブロー：1
正解：4819 予想：0735　->　ヒット：0 ブロー：0
正解：4819 予想：9148　->　ヒット：0 ブロー：4
正解：4819 予想：4819　->　ヒット：4 ブロー：0 クリア
入力値の1行目に出題者の正解の数字が入ります。2行目に予想の数字の総数(1 ≦ n ≦ 30)が入力され、3行目以降に予想数字が入力されます。
出力値は入力値を検証し、その結果を「ヒット ブロー」の順番で表示します。ヒットが4の場合「ヒット ブロー」を表示後改行して、「クリア」と表示します。全ての予想が違う場合、最後の予想の「ヒット ブロー」を表示後改行して「失敗」と表示してください。予想の途中で正解の数字があった場合は「クリア」と表示し、以降の予想結果は表示されないようにしてください。

入力値例
5830
6
6901
4021
5263
5470
5310
5830
出力値例
0 1
0 1
1 0
2 0
2 1
4 0
クリア'),
('Q_03', '暗号解析', '暗号解析のプログラムを記述してください。暗号解析は英小文字(a 〜 z)、数字(0 〜 9)で構成されています。暗号には数字(1 〜 9)が書かれたヒントがついており、ヒントに書かれた数だけ暗号分の文字を前に進めると答えになります。例の通り「b」を前に4つ進めるとc→d→e→fとなり「f」の文字が出てきます。同様に進めると「bhksan」の答えは「flower」になります。
暗号は「z」の後はa, b, c...と続き、「9」の後は0, 1, 2...と続くものとします。
入力値の1行目は暗号文が入り、2行目はヒントの数字を入力値として入れます。
出力値には解読の答えが入るようにしてください。
例
暗号文：bhksan
ヒント：4
答え：flower

入力値例
bhksan
4
出力値例
flower
'),
('DQ_01', '偶数表示', '偶数を表示するプログラムを記述してください。入力値で指定した数値(1 ≦ n ≦100)以下の偶数を低い値から順番に表示してください。

入力値例
13
出力値例
0 2 4 6 8 10 12
');

INSERT INTO question_testcases
VALUES ('T_01_1', 'Q_01', '32 64 55 5 7
12 41 44 18 29
70 59 11 2 25
17 54 10 36 72
22 67 23 47 34
19
59 7 3 22 45 36 25 5 11 22 70 27 7 48 32 15 17 12 74', '2'),
('T_01_2', 'Q_01', '2 22 35 48 72
14 20 38 51 74
4 16 1 54 68
13 30 45 47 64
7 17 39 59 73
9
2 73 30 1 72 20 51 7 47', '2'),
('T_01_3', 'Q_01', '6 26 38 51 64
4 24 37 52 75
15 30 2 58 71
14 17 42 53 67
10 27 45 59 66
1
2', '0'),
('T_01_4', 'Q_01', '11 19 35 48 65
15 24 40 52 71
6 30 2 50 75
14 28 42 58 63
9 20 44 54 73
23
2 52 65 28 9 14 42 58 63 71 75 73 11 15 6 19 35 48 24 40 20 44 54', '6'),
('T_01_5', 'Q_01', '10 16 37 50 70
12 24 34 49 67
9 28 29 51 62
1 26 45 58 72
7 22 38 57 63
50
50 12 8 42 41 20 2 21 51 38 32 71 54 10 67 4 29 40 22 6 70 23 53 62 35 9 14 43 48 19 1 59 45 34 16 49 44 27 18 25 3 17 31 75 7 11 26 55 47 37', '4'),
('T_02_1', 'Q_02', '5830
6
6901
4021
5263
5470
5310
5830
', '0 1
0 1
1 0
2 0
2 1
4 0
クリア
'),
('T_02_2', 'Q_02', '5830
5
6901
4021
5263
5470
5310', '0 1
0 1
1 0
2 0
2 1
失敗'),
('T_02_3', 'Q_02', '6019
1
3572', '0 0
失敗'),
('T_02_4', 'Q_02', '1234
30
9876
8765
7654
6543
5432
4321
3210
2109
1098
0987
9876
8765
7654
6543
5432
4321
3210
2109
1098
0987
9876
8765
7654
6543
5432
4321
3210
2109
1098
0987
', '0 0
0 0
1 0
0 2
1 2
0 4
1 2
0 2
1 0
0 0
0 0
0 0
1 0
0 2
1 2
0 4
1 2
0 2
1 0
0 0
0 0
0 0
1 0
0 2
1 2
0 4
1 2
0 2
1 0
0 0
失敗
'),
('T_02_5', 'Q_02', '7104
11
0513
4529
1308
8107
7106
7104
5691
3518
3495
8457
0851
', '0 1
1 1
2 1
3 0
4 0
成功
'),
('T_03_1', 'Q_03', 'bhksan
4', 'flower'),
('T_03_2', 'Q_03', '42442049
8', '20220827'),
('T_03_3', 'Q_03', 'exzhr9799
3', 'hacku2022'),
('DT_01_1', 'DQ_01', '13', '0 2 4 6 8 10 12'),
('DT_01_2', 'DQ_01', '15', '0 2 4 6 8 10 12 14'),
('DT_01_3', 'DQ_01', '32', '0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32');

INSERT INTO questions_histories
VALUES ('hr-001', 'room01' ,'id-003', 'Q_01', 'python', '06:54', 2, '2022-08-21 02:31:37.149641+09:00'),
('hr-002', 'room01' ,'id-002', 'Q_01', 'python', '20:00', 4, '2022-08-21 02:31:37.149641+09:00'),
('hr-003', 'room01' ,'id-005', 'Q_01', 'python', '16:24', 3, '2022-08-21 02:31:12.149641+09:00'),
('hr-004', 'room01' ,'id-006', 'Q_01', 'python', '06:20', 1, '2022-08-21 02:31:37.149641+09:00'),
('hr-005', 'room02' ,'id-004', 'Q_03', 'python', '20:00', 3, '2022-08-21 03:51:40.149641+09:00'),
('hr-006', 'room02' ,'id-001', 'Q_03', 'python', '11:56', 2, '2022-08-21 03:53:37.149641+09:00'),
('hr-007', 'room02' ,'id-003', 'Q_03', 'python', '03:21', 1, '2022-08-21 03:51:37.149641+09:00'),
('hr-008', 'room03' ,'id-003', 'DQ_01', 'python', '19:09', 2, '2022-08-21 05:51:17.149641+09:00'),
('hr-009', 'room03' ,'id-001', 'DQ_01', 'python', '16:24', 1, '2022-08-21 05:54:41.149641+09:00'),
('hr-010', 'room04' ,'id-002', 'Q_02', 'python', '10:12', 1, '2022-08-21 02:31:37.149641+09:00');

INSERT INTO history_detail
VALUES ('hd-001', 'hr-001', 'print("Hello world")', false, false, 'Hello world', '', 0, 0, '2022-08-21 02:31:49.149641+09:00'),
('hd-002', 'hr-001', 'print("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world', '', 0, 0, '2022-08-21 02:35:21.149641+09:00'),
('hd-003', 'hr-001', 'print"Hello world")\nprint("Hello world")', false, true, '', 'syntax error', 0, 0, '2022-08-21 02:37:11.149641+09:00'),
('hd-004', 'hr-001', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-005', 'hr-001', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-006', 'hr-001', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-007', 'hr-001', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-008', 'hr-002', 'print"Hello world")\nprint("Hello world")', false, true, '', 'syntax error', 0, 0, '2022-08-21 02:37:11.149641+09:00'),
('hd-009', 'hr-002', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-010', 'hr-002', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-011', 'hr-002', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-012', 'hr-002', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-013', 'hr-003', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-014', 'hr-003', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-015', 'hr-003', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-016', 'hr-003', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-017', 'hr-004', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-018', 'hr-004', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-019', 'hr-004', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-020', 'hr-004', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-021', 'hr-005', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-022', 'hr-005', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-023', 'hr-005', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-024', 'hr-005', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-025', 'hr-006', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-026', 'hr-006', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-027', 'hr-006', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-028', 'hr-006', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-029', 'hr-007', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-030', 'hr-007', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-031', 'hr-007', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-032', 'hr-007', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-033', 'hr-008', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-034', 'hr-008', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-035', 'hr-008', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-036', 'hr-008', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-037', 'hr-009', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-038', 'hr-009', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-039', 'hr-009', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-040', 'hr-009', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00'),
('hd-041', 'hr-010', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', false, false, 'Hello world\nHello world\nHello world', '', 0, 0, '2022-08-21 02:40:21.149641+09:00'),
('hd-042', 'hr-010', 'print("Hello world")\nprint("Hello world")\nprint("Hello world")', true, true, '', 'syntax error', 5, 0, '2022-08-21 02:45:21.149641+09:00'),
('hd-043', 'hr-010', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world', '', 5, 3, '2022-08-21 02:47:21.149641+09:00'),
('hd-044', 'hr-010', 'print("Hello world")\nprint"Hello world")\nprint("Hello world")\nprint("Hello world")', true, false, 'Hello world\nHello world\nHello world\nHello world', '', 5, 5, '2022-08-21 02:50:51.149641+09:00');



