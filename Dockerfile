FROM python

EXPOSE 5007

WORKDIR /app


COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]

