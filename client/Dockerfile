FROM mirror.gcr.io/node:18.15 AS client

WORKDIR /vsnder/client

COPY ./package.json ./package-lock.json ./
RUN --mount=type=cache,sharing=locked,target=/root/.npm npm ci

COPY . .

CMD npm start
