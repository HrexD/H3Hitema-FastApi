FROM python:3.10
WORKDIR /app
RUN pip install fastapi uvicorn
COPY . .
CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port","15400"]