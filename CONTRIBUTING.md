# CONTRIBUTING

## How to build docker

```commandline
docker build . -t flask-smorest-api
```

## How to run the Dockerfile locally

```commandline
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
```

## How to run using redis and rq

```commandline
docker run -w /app flask-smorest-api sh -c "rq worker -u rediss://red-ce6jo9pa6gdtam24uc00:neCvN4TF9Xi5K6EZu65jV8zFrpldpSrH@oregon-redis.render.com:6379 emails"
```