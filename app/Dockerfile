# Python 3の公式Dockerイメージをベースにする
FROM python:3.10

# requirements.txtをコピー
COPY ./requirements.txt .

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリを設定
WORKDIR /usr/src/apps

# ソースコードをコピー
COPY ./src /usr/src/apps