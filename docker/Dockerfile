FROM alpine:3.20 as basic

ENV PATH="$PATH:/root/.local/bin"

WORKDIR /var/app

RUN apk add --no-cache \
    pipx

FROM basic as dev

RUN pipx install flask

FROM dev as prod

RUN pipx inject --include-apps flask gunicorn