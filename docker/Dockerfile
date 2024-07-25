FROM alpine:3.20 as basic

WORKDIR /var/app

RUN apk add --no-cache /
    pipx

FROM basic as dev

RUN pipx install flask

FROM dev as prod

RUN pipx inject --include-apps flask gunicorn