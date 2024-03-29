ABSOLUTE_DIR_PATH=/Users/zualexander/Documents/workspace/workspace-bic/bacc-work
DOCKER_IMAGE_NAME_YOLO=yolo9000-jupyter
DOCKER_IMAGE_NAME_TF=tensorflow-jupyter
VOLUME_TEST_IMAGES_DIR=/test-images

build:
	make -j2 build-tf build-yolo

run:
	make -j2 run-tf run-yolo && cd ./bounding-box-drawer && python3 main.py && cd ..

build-tf:
	docker build -t $(DOCKER_IMAGE_NAME_TF) ./tensorflow-object-detection/

run-tf:
	docker run \
	-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/tf$(VOLUME_TEST_IMAGES_DIR) \
	-v $(ABSOLUTE_DIR_PATH)/tensorflow-object-detection/notebooks/:/tf/notebooks \
	$(DOCKER_IMAGE_NAME_TF) \

run-tf-i:
	docker run \
	-p 8888:8888 \
	-it \
	-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/tf$(VOLUME_TEST_IMAGES_DIR) \
	-v $(ABSOLUTE_DIR_PATH)/tensorflow-object-detection/notebooks/:/tf/notebooks \
	$(DOCKER_IMAGE_NAME_TF) \
	sh


build-yolo:
	docker build -t $(DOCKER_IMAGE_NAME_YOLO) ./yolo9000-object-detection/

run-yolo-interactive:
	docker run \
	-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/main$(VOLUME_TEST_IMAGES_DIR) \
	-it \
	-e GRANT_SUDO=yes \
	--user root \
	$(DOCKER_IMAGE_NAME_YOLO) \
	start.sh

run-yolo:
	docker run \
		-v $(ABSOLUTE_DIR_PATH)$(VOLUME_TEST_IMAGES_DIR):/main$(VOLUME_TEST_IMAGES_DIR) \
		-e GRANT_SUDO=yes \
		--user root \
		$(DOCKER_IMAGE_NAME_YOLO) \