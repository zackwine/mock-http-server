# mock-http-server
A mock HTTP server that just prints the request


# Dev notes

## Building docker image for local

`docker build -t mock-http-server:latest .`

## Building for multiple architectures

Do once:
`docker buildx create --use`

For each build:
`docker buildx build --platform linux/amd64,linux/arm64 --push -t winez/mock-http-server:latest .`

## Running docker container

`docker run -p 8080:8080  mock-http-server:latest`
