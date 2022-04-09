# agora RTB mockup

The reccommended system OS version is Ubuntu 20.04

Firstly we need to install MongoDB in our local machine following these steps:

wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
sudo apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

We may now proceed to git clone the repository

git clone https://github.com/akiskourtis/agora.git

The application has been packaged as a Docker container

Install Docker
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

To install the Docker container, we run this command at the repository directory

sudo docker build -t agora_docker .

The command below initiates the bidder API & service and campaign API

python3 main.py &

In order to fill in the Campaign database with run this command to generate 50 campaign entries

curl -i -X PUT -H '' http://127.0.0.1:5001

Finally, we can run random tests throught the tester service

python3 tester.py
