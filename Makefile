docker\:build:
	docker build -t wangtai/wecloud_inference_test_job:latest .

docker\:push:
	docker push wangtai/wecloud_inference_test_job:latest