# Flask Minimum web-api example

# Local execution

## Create Environment

<https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask>

- `mkdir FlaskExample\`
- `cd .\FlaskExample`
- `python -m venv venv`
- Activate env:
  - windows: `.\venv\Scripts\activate`
  - linux: `. venv/bin/activate`
- `pip install --upgrade -r env.txt` or `pip install Flask`
- in IDE: select python.exe from venv dir!! (`\venv\Scripts\python.exe`)

## Create Web-App

<https://flask.palletsprojects.com/en/2.0.x/quickstart/>

## Run

<https://flask.palletsprojects.com/en/2.0.x/cli/>

- In IDE set working-directory (`FlaskExample`)
- In Shell:

  > export FLASK_APP=app
  > export FLASK_ENV=development
  > flask run

  - if file named `app.py`, no env-var needed. just `flask run`

### To set non-routable meta-address and Port

- `flask run --host 0.0.0.0 --port 80`

---

# Dockerized Execution

## Docker-Image

In terminal (directory of DOCKERFILE) run

- `docker build -t <IMAGE-NAME> .`  (**-t** for tag)
- check: `docker image ls`

Docker hub repo: <https://hub.docker.com/repository/docker/dasmuesli/minimum_flask_app>

## Docker run

- `docker run -p 4666:8080 -d -e "FLASK_APP_NAME=Scotty" --name <CONTAINER-NAME> <IMAGE-NAME>`  
- test: `http://127.0.0.1:4666`

Remarks:

- -p local:docker (port routing) [link](https://docs.docker.com/engine/reference/run/#expose-incoming-ports)
- -e set environment variable [link](https://docs.docker.com/engine/reference/run/#env-environment-variables)
- --name [link](https://docs.docker.com/engine/reference/run/#name---name)

## Docker Compose

Inside folder with **docker-compose.yml**

- `docker compose up`
- test with: `http://127.0.0.1:4666`
