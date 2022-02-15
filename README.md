# A GraphQL Server and Jenkins CICD Pipeline Built with Docker

This repository contains a GraphQL backend server wrote with Python and a Jenkins CICD pipeline. Both are built on top of various Docker images. The purpose of this project is to demonstrate how an application can be containerized easily with Docer and how to use Docker to construct a CICD pipeline. Most of the contents comes from links in the References. Feel free to take a look and raise issues if any.

## How to Run

* Run GraphQL application

  ```bash
  make app
  ```

* Run Jenkins CICD pipeline

  ```bash
  make cicd
  ```


## GraphQL Server Application

* GraphQL: API
* Flask server
	* Graphene: GraphQL Python package
	* PyMongo: MongoDB Python package
* MongoDB: Database

### Application Illustration

![alt text](https://github.com/KentHsu/GraphQL-Docker-CICD-Pipeline/tree/master/images/GraphQL-app.png)


## CICD Pipeline

* Gogs: local source code repository
* Jenkins: CICD pipeline management
* Docker Register: local image repository
* Linode: remote docker server

### CICD Pipeline Illustration

![alt text](https://github.com/KentHsu/GraphQL-Docker-CICD-Pipeline/blob/master/images/CICD-pipeline.png)

### Jenkins Pipeline

[Pull] => [Verify] => [Build] => [Test] => [Push] => [Deploy]

![alt text](https://github.com/KentHsu/GraphQL-Docker-CICD-Pipeline/blob/master/images/Jenkins-pipeline.jpg)

### Jenkins Credentials

The Jenkins Docker image has not configured for accessing Gogs server and remote Docker server. All credentials need to be configured manually including Gogs user/password and remote server CA, key pair and key certificate to run the pipeline smoothly.

![alt text](https://github.com/KentHsu/GraphQL-Docker-CICD-Pipeline/blob/master/images/Jenkins-credentials.jpg)

## Project Structure

```
GraphQL-Docker-CICD-Pipeline
|____README.md
|____.gitignore
|____Makefile
|____Jenkinsfile
|____docker-compose-build.yml     # Build GraphQL app Docker image
|____docker-compose.yml	          # Run GraphQL app containers
|____docker-compose-cicd.yml      # Run CICD pipeline containers
|
|____CICD
| |____Dockerfile                 # Jenkins Docker image
| |____scripts                    # Script files for CICD pipeline
| | |____00-verify.sh
| | |____01-build.sh
| | |____02-test.sh
| | |____03-push.sh
| | |____04-deploy.sh
|
|____GraphQL                      # Jenkins Docker image
| |____app                        # GraphQL Flask server
| | |____app.py
| | |____Dockerfile
| | |____Pipfile
| | |____Pipfile.lock
| |
| | |____schema                   # GraphQL query schema
| | | |____ __init__.py
| | | |____schema.py
| |
| | |____database                 # GraphQL app data storage
| | | |____ __init__.py
| | | |____mongodb.py
| |
| | |____tests                    # Tests for GraphQL app
| | | |____ __init__.py
| | | |____test_graphql.py
| |
| |____mongo
| | |____Dockerfile
| | |____init-mongo.js            # MongoDB initial data
| | |____secrets                  # MongoDB env/confedential setting
| | | |____mongodb.env
| | | |____password
| | | |____username
|
|____certs                        # mTLS certificates generator
| |____README.md
| |____daemon.json
| |____certs-gen.sh
|
|____images                       # images for documentation
| |____CICD-pipeline.png
| |____Jenkins-pipeline.jpg
| |____Jenkins-credentials.jpg
| |____GraphQL-app.png

```

## References

1. [Net Ninja - React GraphQL Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9iK6Qhn-QLcXCXPQUov1U7f)
2. [Learn Docker in a Month of Lunches](https://www.youtube.com/playlist?list=PLXl_isu8qxvmDOAnUkG5x16LzBzGzY_Ww)
3. [FindMind Github Repository](https://github.com/FinMind/FinMind)
4. [A Cloud Guru](https://acloudguru.com/)