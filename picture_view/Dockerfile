ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    bash \
    curl \
    jq \
    python3 \
    py3-pip

RUN pip3 install --break-system-packages flask pillow

RUN mkdir -p /app/templates /data/images

COPY app/ /app/
COPY run.sh /run.sh
RUN chmod +x /run.sh

WORKDIR /app
CMD ["/run.sh"]
