# Task manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Elenlith/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Elenlith/python-project-52/actions)
<a href="https://codeclimate.com/github/Elenlith/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/cff6a152a371c60f3979/maintainability" /></a>
<a href="https://codeclimate.com/github/Elenlith/python-project-52/test_coverage"><img src="https://api.codeclimate.com/v1/badges/cff6a152a371c60f3979/test_coverage" /></a>

## Description

Task Manager is a simple web-app which allows you to create tasks, custom statuses and labels for them, assign executors, etc. 

## The aplication is deployed here
<a href="http://python-project-52-production-5cce.up.railway.app">python-project-52-production-5cce.up.railway.app</a>

## How to install and run

1) Clone the repo:
```
git clone https://github.com/Elenlith/python-project-52.git
```
2) Go to python-project-52 directory:
```
cd python-project-52
```
3) Install dependencies (requires Poetry):
```
poetry install
```
4) Add .env file to the project root with DATABASE_URL and SECRET_KEY variables
```
##.env
DATABASE_URL=<insert your link>
SECRET_KEY=<insert your value>
```
5) Prepare databases
```
make migrate
```
6) Create superuser if necessary
```
poetry run python3 manage.py createsuperuser
```
7) Run the app
```
make dev # see Makefile for details
```
