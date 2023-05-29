FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    grep \
    sed

WORKDIR /scripts
COPY my_script.sh .
RUN chmod +x my_script.sh

CMD ["/bin/bash"]
