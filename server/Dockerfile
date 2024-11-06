FROM mirror.gcr.io/python:3.12

RUN --mount=type=cache,sharing=locked,target=/usr/local/lib/python3.11/site-packages pip install --no-cache-dir pdm==2.17.3

WORKDIR /vsnder/server

COPY ./pdm.lock ./pyproject.toml ./
RUN --mount=type=cache,sharing=locked,target=/root/.cache/pdm pdm sync --dev
RUN pip install --upgrade python-dotenv

COPY . .

CMD pdm run server
