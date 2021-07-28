FROM node:lts-buster as builder

RUN apt-get update \
    && apt-get install -y git

WORKDIR /code

RUN git clone https://github.com/przemekk1385/izba-docs-panel.git .
COPY .env.production.local .

RUN npm install

RUN npm run build


FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY *.conf /etc/nginx/conf.d

COPY --from=builder /code/dist /usr/share/nginx/html
