
source $HOST_WORKDIR_PATH/scripts/.env.sh
source $HOST_WORKDIR_PATH/scripts/base_utils.sh

ES_LOG_FILE_PATH=$PWD/$LOGS_DIR_PATH/es_monitor.log
KIBANA_LOG_FILE_PATH=$PWD/$LOGS_DIR_PATH/kibana_monitor.log
LOGSTADH_LOG_FILE_PATH=$PWD/$LOGS_DIR_PATH/logstash_monitor.log

title "Starting SINGA-Auto's Monitor..."

# start logstash

(docker run --rm --name $LOGSTASH_HOST \
     --network $DOCKER_NETWORK \
     -e LOGSTASH_DOCKER_WORKDIR_PATH=$LOGSTASH_DOCKER_WORKDIR_PATH \
     -e KAFKA_HOST=$KAFKA_HOST \
     -e KAFKA_HOST=$KAFKA_HOST \
     -p $LOGSTASH_PORT:$LOGSTASH_PORT  \
     -v $HOST_WORKDIR_PATH/$LOGS_DIR_PATH:$LOGSTASH_DOCKER_WORKDIR_PATH/$LOGS_DIR_PATH \
     -v $HOST_WORKDIR_PATH/scripts/config/logstash.conf:$LOGSTASH_DOCKER_WORKDIR_PATH/logstash.conf  \
     -d $SINGA_AUTO_IMAGE_LOGSTASH:$SINGA_AUTO_VERSION \
     &> LOGSTADH_LOG_FILE_PATH) &

# start es
(docker run --rm --name $ES_HOST  \
   --network $DOCKER_NETWORK \
   -e ES_DOCKER_WORKDIR_PATH=$ES_DOCKER_WORKDIR_PATH \
   -p $ES_PORT:$ES_PORT \
   -p $ES_NODE_PORT:$ES_NODE_PORT  \
   -e "discovery.type=single-node" \
   -d  $SINGA_AUTO_IMAGE_ES:$SINGA_AUTO_VERSION \
   &> ES_LOG_FILE_PATH) &

# start
(docker run --rm --name $KIBANA_HOST \
    --network $DOCKER_NETWORK \
    -p $KIBANA_PORT:$KIBANA_PORT \
    -d $IMAGE_KIBANA \
    &> KIBANA_LOG_FILE_PATH) &
