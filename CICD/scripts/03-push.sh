docker-compose -f docker-compose.yml -f docker-compose-build.yml push
curl http://registry:5000/v2/_catalog
