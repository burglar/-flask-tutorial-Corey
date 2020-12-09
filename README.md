# Flask tutorial

## Intro

Using this repo to follow the [tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) made by Corey Schafer. 

## Setup

### Python evironment

Create and activate a virtual environment for python

```
python -m venv venv
source venv/bin/activate
```



Install requirements with pip

```
pip install -r requirements.txt
```


Copy .env.example to .env and edit it to suit your environment

By default it is using a Postgres database that can be deployed in docker

Uncomment the sqlite configuration if you don't want to set up the container for Postgres (and comment the Postgres configuration)

&nbsp;



### Deploying the Postgres and pgAdmin stack with docker

Create folders to mount postgres and pgadmin volumes

```
mkdir database-data pgadmin-data
```

Change ownership of the pgadmin-data folder ([link](https://www.pgadmin.org/docs/pgadmin4/development/container_deployment.html#mapped-files-and-directories))

```
sudo chown 5050:5050 pgadmin-data
```

Deploy the stack

```
docker stack deploy -c stack.yml postgres
```

&nbsp;



### Initialize Database Model with SQLAlquemy migrations

```
flask db upgrade
```

&nbsp;



### Run the app

```
flask run
```
