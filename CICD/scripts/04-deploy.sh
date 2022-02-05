docker-compose --host tcp://$PROD --tlsverify \
    --tlscacert $ca --tlscert $cert --tlskey $key \
    -f docker-compose.yml -f docker-compose-build.yml up -d

