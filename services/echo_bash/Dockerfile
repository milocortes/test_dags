FROM alpine:3.14
RUN apk add --no-cache bash
COPY test.sh ./
RUN chmod +x ./test.sh
ENTRYPOINT ["./test.sh"]
