FROM python:3.9-slim-buster
WORKDIR /app
RUN pip install flask fabric python-dotenv
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]