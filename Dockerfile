# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /todo_list_app

COPY ./requirements.txt /todo_list_app

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "--app", "todo_list/app.py", "run", "--host=0.0.0.0"]