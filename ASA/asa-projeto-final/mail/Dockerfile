FROM ubuntu:20.04

RUN apt update

RUN apt upgrade -y

RUN apt install postfix  dovecot-imapd dovecot-pop3d -y

RUN apt install -q -y syslog-ng

COPY main.cf /etc/postfix

COPY 10-auth.conf /etc/dovecot/conf.d

# Add User
RUN useradd -m joao
RUN useradd -m aristeu
RUN useradd -m maria
# Set user passord
RUN echo "joao:asa"|chpasswd
RUN echo "aristeu:asa"|chpasswd
RUN echo "maria:asa"|chpasswd

CMD ["sh", "-c", "service syslog-ng start ; service postfix start ; service dovecot start; tail -F /var/log/mail.log"]
