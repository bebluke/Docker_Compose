# Docker_Compose

## Describe 
This is a small project from BDSE DOCKER Class.  
By using the docker compose yaml file to operate three application containers including mysql, flask, nginx, we can import dataset into mysql, retreive dataset from mysql using flask, and show dataset in web page using nginx.

## Project Structure
```
.
├── data
|   ├── import.sql
|   └── titanic_full_data.csv
|
├── mysql
|   └── Dockerfile
|
├── python
|   ├── app.py
|   ├── Dockerfile
|   └── requirements.txt
|
├── mysql
|   └── Dockerfile
|
├── web
|   ├── Dockerfilenginx.conf
|   ├── index.html
|   └── nginx.conf
|
├── docker-compose.yaml
└── README.md
    
```
## Prerequisites

OS: Ubuntu Noble 24.04 (LTS)  
Docker: To install docker on Ubuntu, please follow the step provided by docker offical website as follow https://docs.docker.com/engine/install/ubuntu/  

## Deployment

Please download this project as a directory and upload into your Linux environment.  
Please do not rename any item.  
Please run the following command under this project directory.  

```
docker-compose up -d --build
```
