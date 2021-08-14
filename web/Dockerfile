FROM nginx AS dev

RUN rm /etc/nginx/conf.d/default.conf
COPY *.conf /etc/nginx/conf.d


FROM node:lts AS builder

RUN apt-get update \
    && apt-get install -y git

WORKDIR /code

RUN git clone https://github.com/przemekk1385/izba-docs-panel.git .
COPY .env.* ./

RUN npm install

RUN npm run build


FROM dev AS prod

COPY --from=builder /code/dist /usr/share/nginx/html
