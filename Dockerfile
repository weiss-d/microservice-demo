FROM python:3-alpine

WORKDIR /usr/src/microservice-demo

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "-m", "microservice_demo.app"]
