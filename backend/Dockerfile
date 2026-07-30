FROM python:3.12-slim

WORKDIR /app

COPY dep.txt .

RUN pip install -r dep.txt

COPY . . 

EXPOSE 9090

CMD ["python", "app.py"]