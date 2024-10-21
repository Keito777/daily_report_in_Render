FROM python:3.10-slim-buster

# バイトコードの生成を抑制
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力の高速化
ENV PYTHONUNBUFFERED=1

WORKDIR /daily_report_in_render

# Dockerfileから見て../（プロジェクトルートdir）をコンテナのWORKDIRにコピー
COPY .. .
# Dockerfileから見てrequirements.txtのパスを指定
RUN pip install --no-cache-dir -r requirements.txt


# コンテナ起動時に自動実行されるコメントの設定(,は半角スペースを意味する)
# python manage.py runserver 0.0.0.0:8000を実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]