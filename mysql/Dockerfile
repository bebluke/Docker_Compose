FROM mysql:8.0
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=titanic
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

COPY ./data/import.sql /docker-entrypoint-initdb.d/
COPY ./data/titanic_full_data.csv /docker-entrypoint-initdb.d/

EXPOSE 3306