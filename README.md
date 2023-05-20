# flask_login_sample

## 概要

Flaskを使用したシンプルなログイン、ログアウトを実施するだけのアプリ

## 開発目的

- 自身のスキルの棚卸

## 実行方法

### 1.コンテナをビルドする

```
docker compose up -d
```

### 2. 以下のページにアクセス

```
http://localhost:5000
```

## 機能

- ログイン
- ログアウト


## 開発言語

- Python 3.10

## フレームワーク

- Flask
- bootstrap5

## 開発言語・フレームワークプラグイン

- Flask-SQLAlchemy 3.0.3
- Flask-Login 0.6.2
- Flask-Bcrypt 1.0.1
- pymysql 1.0.3
- email-validator

## DBサーバー

- MySQL 8.0.33

## サーバー等の設定

### アプリ

- とくになし

### MySQL

- 文字コード：utf8mb4
- 照合順序：MySQL 8系デフォルト
