


export ZOOKEEPER_EXT_PORT=2181
export KAFKA_EXT_PORT=9092


export ZOOKEEPER_HOST=singa-auto-zookeeper
export ZOOKEEPER_PORT=2181
export KAFKA_HOST=singa-auto-kafka
export KAFKA_PORT=9092
export LOGSTASH_HOST=singa-auto-logstash
export LOGSTASH_PORT=9600
export ES_HOST=elasticsearch
export ES_PORT=9200
export ES_NODE_PORT=9300
export KIBANA_HOST=singa-auto-kibana
export KIBANA_PORT=5601
export KIBANA_EXT_PORT=31009


export DOCKER_WORKDIR_PATH=/root
export LOGS_DIR_PATH=logs # Shares a folder with containers that stores components' logs, relative to workdir

export WORKDIR_PATH=$HOST_WORKDIR_PATH # Specifying workdir if Python programs are run natively


export LOGSTASH_DOCKER_WORKDIR_PATH=/usr/share/logstash
export KIBANA_DOCKER_WORKDIR_PATH=/usr/share/kibana
export ES_DOCKER_WORKDIR_PATH=/usr/share/elasticsearch

# Docker images for SINGA-Auto's custom components
export SINGA_AUTO_IMAGE_LOGSTASH=singaauto/singa_auto_logstash
export SINGA_AUTO_IMAGE_ES=singaauto/singa_auto_es


# Docker images for dependent services
export IMAGE_ZOOKEEPER=zookeeper:3.5
export IMAGE_KAFKA=wurstmeister/kafka:2.12-2.1.1

export IMAGE_KIBANA=kibana:7.7.0
export IMAGE_ES=docker.elastic.co/elasticsearch/elasticsearch:7.7.0
