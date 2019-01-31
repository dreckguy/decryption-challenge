FROM python:3.7.2-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5000
ENV FLASK_APP=server.py
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]