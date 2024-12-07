FROM mirror.gcr.io/node:18.15 AS client

WORKDIR /vsnder/client

COPY ./services/client/package.json ./services/client/package-lock.json ./
RUN --mount=type=cache,sharing=locked,target=/root/.npm npm ci

COPY ./services/client/ /vsnder/client/

CMD npm start
