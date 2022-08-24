DROP DATABASE IF EXISTS hack-u-2022;

CREATE DATABASE hack-u-2022;

CREATE TABLE "users" (
  "id" text PRIMARY KEY,
  "usersName" text NOT NULL,
  "usersEmail" text NOT NULL,
  "usersPassword" text NOT NULL,
  "createdAt" text
);

CREATE TABLE "questions_histories" (
  "id" text PRIMARY KEY,
  "usersId" text,
  "questionsId" text,
  "language" text,
  "historiesTime" text,
  "historiesRanking" int DEFAULT 0,
  "createdAt" text
);

CREATE TABLE "history_detail" (
  "id" text PRIMARY KEY,
  "historiesId" text,
  "historyCode" text,
  "isExecuteTest" boolean,
  "isProgramError" boolean,
  "programOutput" text,
  "programError" text,
  "testCaseTotal" int,
  "testCaseClearTotal" int,
  "createdAt" text
);

CREATE TABLE "rooms" (
  "id" text PRIMARY KEY,
  "masterUserId" text,
  "roomName" text NOT NULL,
  "questionsId" text DEFAULT null,
  "roomIsRandom" boolean,
  "isDemo" boolean,
  "maxPlayer" int
);

CREATE TABLE "rooms_visitors" (
  "id" text PRIMARY KEY,
  "roomsId" text,
  "usersId" text
);

CREATE TABLE "visitors_test_state" (
  "id" text PRIMARY KEY,
  "roomsVisitors" text,
  "testCaseId" text
);

CREATE TABLE "questions" (
  "id" text PRIMARY KEY ,
  "questionsTitle" text NOT NULL,
  "questionsContent" text NOT NULL
);

CREATE TABLE "question_testcases" (
  "id" text PRIMARY KEY,
  "questionsId" text,
  "testcasesInput" text NOT NULL,
  "testcasesOutput" text NOT NULL
);

ALTER TABLE "questions_histories" ADD FOREIGN KEY ("usersId") REFERENCES "users" ("id");

ALTER TABLE "questions_histories" ADD FOREIGN KEY ("questionsId") REFERENCES "questions" ("id");

ALTER TABLE "history_detail" ADD FOREIGN KEY ("historiesId") REFERENCES "questions_histories" ("id");

ALTER TABLE "rooms" ADD FOREIGN KEY ("masterUserId") REFERENCES "users" ("id");

ALTER TABLE "rooms" ADD FOREIGN KEY ("questionsId") REFERENCES "questions" ("id");

ALTER TABLE "rooms_visitors" ADD FOREIGN KEY ("roomsId") REFERENCES "rooms" ("id");

ALTER TABLE "rooms_visitors" ADD FOREIGN KEY ("usersId") REFERENCES "users" ("id");

ALTER TABLE "visitors_test_state" ADD FOREIGN KEY ("roomsVisitors") REFERENCES "rooms_visitors" ("id");

ALTER TABLE "visitors_test_state" ADD FOREIGN KEY ("testCaseId") REFERENCES "question_testcases" ("id");

ALTER TABLE "question_testcases" ADD FOREIGN KEY ("questionsId") REFERENCES "questions" ("id");
