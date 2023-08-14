FROM python:3.11
ENV PYTHONUNBUFFERED 1

# install and configure poetry
ARG POETRY_VERSION=1.5.1
ENV PATH=/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV POETRY_VIRTUALENVS_CREATE=False
COPY pyproject.toml /
RUN curl -sSL https://install.python-poetry.org \
    | POETRY_VERSION=${POETRY_VERSION} python3 - && \
    poetry install

WORKDIR /app

RUN apt-get update
RUN apt-get install gifsicle

COPY thumbor.conf /app
COPY sentry.py /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD thumbor --port=$THUMBOR_PORT --conf=/app/thumbor.conf --log-level=$THUMBOR_LOGGING_LEVEL