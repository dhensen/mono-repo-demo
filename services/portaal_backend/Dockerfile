FROM python:3.8.5-alpine3.12

RUN apk add build-base
RUN pip install sanic

COPY src/portaal_backend /src

EXPOSE 8000

CMD ["python3", "/src/server.py"]
