# Base Python image
FROM python:3.9.6-slim-buster as base-image
COPY requirements.txt .
RUN pip install --quiet -r requirements.txt

COPY src/ .

# Image to test the current app.
FROM base-image as test-image

COPY test_requirements.txt .
RUN pip install --quiet -r test_requirements.txt

COPY tests/ .

ENTRYPOINT ["pytest"]
