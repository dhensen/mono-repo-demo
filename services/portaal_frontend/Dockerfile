FROM node:14.9.0-alpine3.12

# yarn install would be here, but this is a demo
RUN yarn global add serve

COPY src/portaal_frontend /src

EXPOSE 5000

CMD "serve /src"
