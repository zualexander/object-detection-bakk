ABSOLUTE_DIR_PATH=/Users/zualexander/Documents/workspace/bic/bacc-work
DOCKER_IMAGE_NAME_YOLO=yolo9000-jupyter
DOCKER_IMAGE_NAME_TF=tensorflow-jupyter
VOLUME_TEST_IMAGES_DIR=/test-images

build:
	make build-tf && make build-yolo

run:
	make run-tf && make run-yolo

build-tf:
	docker build -t $(DOCKER_IMAGE_NAME_TF) ./tensorflow-object-detection/

run-tf:
	docker run \
	-p 8888:8888 \
	$(DOCKER_IMAGE_NAME_TF) \


ru2n-tf:
	docker run \
	-p 8888:8888 \
	-e GRANT_SUDO=yes \
	$(DOCKER_IMAGE_NAME_TF) \
	start-notebook.sh \
	--NotebookApp.allow_root=True

build-yolo:
	docker build -t $(DOCKER_IMAGE_NAME_YOLO) ./yolo9000-object-detection/

run-yolo:
	docker run \
	-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/main$(VOLUME_TEST_IMAGES_DIR) \
	-it \
	-e GRANT_SUDO=yes \
	--user root \
	$(DOCKER_IMAGE_NAME_YOLO) \
	start.sh

run-yolo2:
	docker run \
	-p 8888:8888 \
	-e GRANT_SUDO=yes \
	-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/main$(VOLUME_TEST_IMAGES_DIR) \
	$(DOCKER_IMAGE_NAME_YOLO) \
	start-notebook.sh \
	--NotebookApp.allow_root=True \
