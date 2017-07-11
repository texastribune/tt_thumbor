FROM python:2.7.13
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY thumbor.conf /app

CMD thumbor --port=$THUMBOR_PORT --conf=/app/thumbor.conf --log-level=$THUMBOR_LOGGING_LEVEL