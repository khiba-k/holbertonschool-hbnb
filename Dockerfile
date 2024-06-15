FROM python3:alpine

WORKDIR /app

COPY requirments.txt .

EXPOSE 5000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]