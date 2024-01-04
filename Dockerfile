# Образ с системными зависимостями
FROM python:3.12.1-slim-bullseye AS base-image

RUN mkdir /opt/tg_bot
WORKDIR /opt/tg_bot

RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip setuptools wheel

# Ставим python-зависимости
FROM base-image AS build-image

RUN apt-get update \
    && python -m ensurepip --upgrade \
    && python -m pip install --upgrade pip setuptools wheel
RUN pip install pipenv==2023.11.15

COPY Pipfile Pipfile.lock ./
RUN python -m venv /opt/venv && . /opt/venv/bin/activate && \
    # обязательно нужно установить wheel внутрь venv
    pip install --upgrade pip && pip install wheel==0.38.4 && \
    pipenv sync

# Используем python из venv по умолчанию
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH=/var/www/tg_bot

# Образ с приложением
FROM build-image

WORKDIR /var/www/tg_bot
COPY . .

ENTRYPOINT ["python"]
CMD ["main.py"]