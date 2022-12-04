# CONTRIBUTING

## How to run the Dockerfile locally

```commandline
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"
```