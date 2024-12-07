FROM mirror.gcr.io/python:3.12.6

RUN --mount=type=cache,sharing=locked,target=/usr/local/lib/python3.11/site-packages pip install --no-cache-dir pdm==2.17.3

COPY ./packages/ /packages/

WORKDIR /vsnder/server

COPY ./services/server/pdm.lock ./services/server/pyproject.toml ./
RUN --mount=type=cache,sharing=locked,target=/root/.cache/pdm pdm sync --dev
RUN pip install --upgrade python-dotenv

COPY ./services/server/ /vsnder/server/

CMD pdm run watch
