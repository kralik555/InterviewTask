FROM python:3.8
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
CMD ["python3", "main.py"]
