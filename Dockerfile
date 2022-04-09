FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install PyYAML==5.4.1
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt update
RUN apt-get install -y systemd
RUN apt install -y mongodb-org
EXPOSE 5000 5001
COPY . .
CMD ["python3", "./main.py"]