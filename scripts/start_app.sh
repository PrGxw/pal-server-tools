export APP_NAME="oneline-resume"
export ROOT_DIR=$(dirname $(realpath $0))/..
export WORK_DIR=/$APP_NAME
export ENV="development"
export LOG_DIR="/logs"
export IMAGE_DIR="/images"
export SOURCE_DIR=$ROOTDIR/src
export ENTRY_PROGRAM=src/entry.py
export PYTHONPATH=$PYTHONPATH:$WORK_DIR
cd $ROOT_DIR

docker compose down
docker compose build
docker compose up -d
