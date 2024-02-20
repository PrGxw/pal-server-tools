FROM tiangolo/uwsgi-nginx-flask:python3.11
ARG APP_NAME
ARG WORK_DIR
ARG SOURCE_DIR
WORKDIR $WORK_DIR

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY $SOURCE_DIR .
