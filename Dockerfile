FROM python:3.9-slim
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
# EXPOSE the application port
EXPOSE 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
