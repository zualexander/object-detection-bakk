DOCKER_IMAGE_NAME=tensorflow-jupyter

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run -p 8888:8888 $(DOCKER_IMAGE_NAME)