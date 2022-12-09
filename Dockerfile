FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD [ "gunicorn", "--workers", "4", "--max-requests", "128", "--bind" , "0.0.0.0:5001", "app:create_app()"]
