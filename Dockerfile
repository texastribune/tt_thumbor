FROM python:3.11
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update
RUN apt-get install gifsicle

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY thumbor.conf /app
COPY sentry.py /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD thumbor --port=$THUMBOR_PORT --conf=/app/thumbor.conf --log-level=$THUMBOR_LOGGING_LEVEL