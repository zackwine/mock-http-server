FROM ubuntu:23.10

WORKDIR /usr/src/app

# Install OS packages
RUN apt-get update && apt-get -y install curl python3 pip vim iproute2

# Install app
COPY app.py .

# Ensure logs are printed real time
ENV PYTHONUNBUFFERED=1

CMD ["python3" , "/usr/src/app/app.py"]
