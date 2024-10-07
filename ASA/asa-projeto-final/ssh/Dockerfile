FROM ubuntu:latest


RUN apt update && \
    apt upgrade -y && \
    apt install -y openssh-server openssh-client


RUN mkdir /var/run/sshd

RUN useradd -m aristeu && \
    echo 'aristeu:12345' | chpasswd


RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config


EXPOSE 22


CMD ["/usr/sbin/sshd", "-D"]
