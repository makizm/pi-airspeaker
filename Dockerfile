FROM mikebrady/shairport-sync:latest

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-rpigpio

# allow user running shairport-sync service to access
# raspberry pi gpio pins
RUN addgroup -g 997 gpio && addgroup shairport-sync gpio

COPY mute.py /usr/local/bin/mute.py
COPY shairport-sync.conf /etc/shairport-sync.conf
