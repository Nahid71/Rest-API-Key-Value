# REST key-val store

## Description

It is a simple Restful API to create key-val stored. I develop this app using Django Rest Framework and Redis. The purpose of the API is to store any arbitrary length value in a persistent store with respect to a key and later fetch these values by keys. These values  have a TTL for example 5 minutes and after the TTL is over, the values will be removed from the store


### Prerequisites

Following package and library have to install into your machine to run this app
* python3
* [redis] (http://www.dropwizard.io/1.0.2/docs/)


### Installing

First clone this repository using:
```
git clone https://github.com/Nahid71/Rest-API-Key-Value.git
```
Create a virtualenv (install virtualenv if not install in your machine using "sudo pip3 install virtualenv"):
```
virtualenv --python=python3 env --no-site-packages 
```
Active the virtualenv using:
```
source env/bin/activate 
```
Now navigate to the project folder and run:
```
pip install -r requirements.txt 
```
After that run:
```
python manage.py migrate
```
And finally start the application usnig:
```
python manage.py renserver 
```
## Running the tests

You will find the test script in api/test.py. to run the test use:

```
python manage.py test 
```

### How To Use

After running the app you can use postman to test out the app.
The API has total 4 endpoints 

1. GET /values (Get all the values of the store)
  * response: {key1: value1, key2: value2, key3: value3...}

2. GET /values?keys=key1,key2 (Get one or more specific values from the store and also reset the TTL of those keys.)
  * response: {key1: value1, key2: value2}

3. POST /values (Save a value in the store)
  * request: {key1: value1, key2: value2..}
  * response: Successfully store the vaules

4. PATCH /values (Update a value in the store and also reset the TTL)
  * request: {key1: value1, key2: value2..}
  * response: Successfully updated values
