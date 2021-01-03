DOCKER_IMAGE_NAME=tensorflow-jupyter

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run \
	-p 8888:8888 \
	$(DOCKER_IMAGE_NAME) \


ru2n:
	docker run \
	-p 8888:8888 \
	-e GRANT_SUDO=yes \
	$(DOCKER_IMAGE_NAME) \
	start-notebook.sh \
	--NotebookApp.allow_rootBool=True