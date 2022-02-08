# mTLS Certificate Generator

In order to communicate with remote docker engine securely, we need to enable TLS at remote docker and provide CA, server cert and server key. To connnect the remote server, we will need to provide client cert and client key generate from the same CA. 

Below are steps for setting up remote docker access:

1. Run certs-gen.sh script file to get CA, server key and server cert, client key and client cert. (This script is copied from diamol repository. See Ref.)
2. Enable TLS at remote docker engine => put daemon.json file in remote server /etc/docker folder
3. Place CA, server-cert, server-key in correspond folder specified in daemon.json file
4. Restart remote docker to update daemon.json setup
5. Run docker command with the same CA, client key and client cert for remote docker access
	
	```docker
	docker --host "tcp://<remote-ip>:<port>"
    		--tlsverify \
    		--tlscacert=ca.pem \
    		--tlscert=server-cert.pem \
    		--tlskey=server-key.pem 
    		container ls
	```



# References

1. [diamol cert-generator for linux](https://github.com/sixeyed/diamol/tree/master/images/cert-generator/linux)
2. [Docker official doc: Protect the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/)
3. [Youtube vedio: How does HTTPS work?](https://www.youtube.com/watch?v=T4Df5_cojAs)