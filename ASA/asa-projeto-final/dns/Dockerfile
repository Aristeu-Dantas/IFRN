FROM ubuntu:latest

RUN apt update -y
RUN apt upgrade -y
RUN apt install bind9 bind9-utils bind9-doc dnsutils -y

#RUN mkdir -p /run/named && \
#     chown -R bind:bind /etc/bind && \
#     chmod 755 /run/named


# COPY ./etc/* /etc/bind
# RUN chown bind:bind /etc/bind
# RUN chmod -R 755 /etc/bind
COPY ifrn.asa.br /etc/bind
COPY par.ifrn.asa.br /etc/bind
COPY named.conf.local /etc/bind

EXPOSE 53/tcp
EXPOSE 53/udp
#EXPOSE 953/tcp

CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]
