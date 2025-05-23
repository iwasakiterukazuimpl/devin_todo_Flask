# ToDo App

FlaskとSQLiteを使用したシンプルなToDoアプリケーションです。

## 機能

- ToDoタスクの追加
- タスクの表示
- タスクの更新（完了/未完了）
- タスクの削除

## 技術スタック

- Python 3.12
- Flask
- SQLite
- HTML/CSS

## プロジェクト構成

```
todo-app/
├── app/                  # アプリケーションコード
│   ├── __init__.py       # Flaskアプリの初期化
│   ├── db.py             # データベース操作
│   ├── models.py         # データモデル
│   ├── routes.py         # ルート定義
│   ├── schema.sql        # データベーススキーマ
│   ├── static/           # 静的ファイル
│   │   └── css/
│   │       └── style.css # CSSスタイル
│   └── templates/        # HTMLテンプレート
│       ├── base.html     # ベーステンプレート
│       └── index.html    # メインページ
├── run.py                # アプリケーション実行スクリプト
└── requirements.txt      # 依存パッケージリスト
```

## セットアップ

1. リポジトリをクローン
   ```
   git clone https://github.com/iwasakiterukazuimpl/devin_world.git
   cd devin_world
   ```

2. 仮想環境を作成して有効化
   ```
   python -m venv venv
   source venv/bin/activate  # Linuxの場合
   # または
   venv\Scripts\activate     # Windowsの場合
   ```

3. 依存パッケージをインストール
   ```
   pip install -r requirements.txt
   ```

4. データベースを初期化
   ```
   flask --app app init-db
   ```

## 実行方法

```
python run.py
```

ブラウザで http://127.0.0.1:5000 にアクセスしてアプリケーションを使用できます。

## 開発

- `flake8`を使用してコードスタイルをチェックできます。
  ```
  flake8 app
  ```
