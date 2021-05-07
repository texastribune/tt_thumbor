Texas Tribune Thumbor
=====================

This repo creates a containerized [Thumbor](http://thumbor.org/) service for creating thumbnails on demand. 
It is configured to use AWS S3 to store created thumbnails, Sentry for monitoring, and Prometheus for metrics.

## Usage
Create a file named `env` in the project directory to customize your configuration (see `env.sample` for the 
configuration options). Run `docker-compose build` to build the docker container then 
to start the service run `docker-compose up`. You should be able to access the service on
port 8888.

