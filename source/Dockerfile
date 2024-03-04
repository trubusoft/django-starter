## Step 1: Building the dependency wheels
FROM python:3.11.6-slim-bullseye as builder

LABEL maintainer=rahmatnazali95@gmail.com

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

WORKDIR /wheels
COPY ./requirements.txt .
COPY ./requirements-production.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels/result -r requirements-production.txt


## Step 2: Building the final image
FROM python:3.11.6-slim-bullseye
RUN addgroup --system app
RUN adduser --system app --ingroup app

ENV PROJECT_ROOT=/home/eprocurement
ENV SOURCE_ROOT=/home/eprocurement/source
ENV WHEEL_ROOT=/home/eprocurement/wheels

RUN mkdir -p $PROJECT_ROOT
RUN mkdir -p $SOURCE_ROOT
RUN mkdir -p $WHEEL_ROOT

WORKDIR $SOURCE_ROOT

RUN pip install --upgrade pip

COPY --from=builder /wheels/requirements-production.txt $SOURCE_ROOT
COPY --from=builder /wheels/result $WHEEL_ROOT
RUN pip install --no-cache $WHEEL_ROOT/*

COPY . $SOURCE_ROOT

RUN chown -R app:app $SOURCE_ROOT
RUN chmod 775 $SOURCE_ROOT/script_collectstatic.sh && \
    chmod 775 $SOURCE_ROOT/script_migrate.sh && \
    chmod 775 $SOURCE_ROOT/script_showmigrations.sh
USER app

EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["starter.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=2"]
