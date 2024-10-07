FROM nginx:latest
#COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

#CMD ["mkdir","/etc/nginx/ssl/"]

RUN mkdir /etc/nginx/ssl

COPY aristeu.com.crt /etc/nginx/ssl/

COPY aristeu.com.key /etc/nginx/ssl/

RUN chown -R root:root /etc/nginx/ssl

RUN chmod -R 600 /etc/nginx/ssl

#CMD ["chmod", "+755", "/etc/nginx/ssl/certificado.crt"]
