FROM python:3.10.11-slim-buster AS builder

WORKDIR /app

COPY . .

RUN pip install poetry && \
    poetry install --no-interaction

FROM python:3.10.11-slim-buster

WORKDIR /app

COPY --from=builder /app .

CMD [".venv/bin/python", "-m", "crenata"]
