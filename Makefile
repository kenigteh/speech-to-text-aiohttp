up:
	docker-compose pull
	docker-compose up -d --build
log:
	docker-compose logs -f --tail=200
down:
	docker-compose down