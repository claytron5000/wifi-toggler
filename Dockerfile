# FROM python:3.9
# ADD app.py .
# ADD toggle_wifi/ .
# RUN pip install flask fabric python-dotenv
# EXPOSE 5000
# CMD ["flask", "run"] 

FROM python:3.9-slim-buster
WORKDIR /app
ADD app.py .
ADD toggle_wifi.py .
RUN pip install flask fabric python-dotenv
COPY . .
EXPOSE 5000
# ENV FLASK_APP=my_flask.py
CMD ["flask", "run", "--host", "0.0.0.0"]