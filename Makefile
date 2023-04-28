build:
	docker build -t texastribune/thumbor .

run:
	docker run --rm -it texastribune/thumbor

up:
	docker-compose up