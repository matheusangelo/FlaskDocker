FROM python:3-onbuild

# We copy just the requirements.txt first to leverage Docker cache
COPY ./src /app

WORKDIR /app

CMD ["python", "app.py" ]