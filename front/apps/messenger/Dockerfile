# Etap 1: Budowanie aplikacji
FROM node:22.13.0-alpine as build-stage

WORKDIR /app

COPY . .
RUN npm install
RUN npm run build

RUN rm -rf node_modules && \
  NODE_ENV=production npm install \
  --prefer-offline \
  --pure-lockfile \
  --non-interactive \
  --production=true

FROM build-stage as prod-stage

WORKDIR /app

COPY --from=build-stage /app/.output ./.output/

CMD [ "node", ".output/server/index.mjs" ]
