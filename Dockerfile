FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python3","-m","flask","--app", "loan_status", "run", "--host=0.0.0.0"]