

import json
import sys
import os

if __name__ == '__main__':
    print(sys.argv)
    POSTGRES_PASSWORD = sys.argv[1]
    SUPERADMIN_PASSWORD = sys.argv[2]
    APP_SECRET = sys.argv[3]
    KUBERNETES_NETWORK = sys.argv[4]
    KUBERNETES_ADVERTISE_ADDR = sys.argv[5]
    SINGA_AUTO_VERSION = sys.argv[6]
    SINGA_AUTO_ADDR = sys.argv[7]
    ADMIN_EXT_PORT = sys.argv[8]
    WEB_ADMIN_EXT_PORT = sys.argv[9]
    POSTGRES_EXT_PORT = sys.argv[10]
    REDIS_EXT_PORT = sys.argv[11]
    ZOOKEEPER_EXT_PORT = sys.argv[12]
    KAFKA_EXT_PORT = sys.argv[13]
    HOST_WORKDIR_PATH = sys.argv[14]
    APP_MODE = sys.argv[15]
    POSTGRES_DUMP_FILE_PATH = sys.argv[16]
    DOCKER_NODE_LABEL_AVAILABLE_GPUS = sys.argv[17]
    DOCKER_NODE_LABEL_NUM_SERVICES = sys.argv[18]

    POSTGRES_USER = sys.argv[19]
    POSTGRES_DB = sys.argv[20]

    POSTGRES_HOST = sys.argv[21]
    POSTGRES_PORT = sys.argv[22]
    ADMIN_HOST = sys.argv[23]
    ADMIN_PORT = sys.argv[24]
    REDIS_HOST = sys.argv[25]
    REDIS_PORT = sys.argv[26]
    PREDICTOR_PORT = sys.argv[27]
    WEB_ADMIN_HOST = sys.argv[28]
    ZOOKEEPER_HOST = sys.argv[29]
    ZOOKEEPER_PORT = sys.argv[30]
    KAFKA_HOST = sys.argv[31]
    KAFKA_PORT = sys.argv[32]
    DOCKER_WORKDIR_PATH = sys.argv[33]
    DATA_DIR_PATH = sys.argv[34]
    LOGS_DIR_PATH = sys.argv[35]
    PARAMS_DIR_PATH = sys.argv[36]
    CONDA_ENVIORNMENT = sys.argv[37]
    WORKDIR_PATH = sys.argv[38]

    SINGA_AUTO_IMAGE_ADMIN = sys.argv[39]
    SINGA_AUTO_IMAGE_WEB_ADMIN = sys.argv[40]
    SINGA_AUTO_IMAGE_WORKER = sys.argv[41]
    SINGA_AUTO_IMAGE_PREDICTOR = sys.argv[42]

    IMAGE_POSTGRES = sys.argv[43]
    IMAGE_REDIS = sys.argv[44]
    IMAGE_ZOOKEEPER = sys.argv[45]
    IMAGE_KAFKA = sys.argv[46]

    PYTHONPATH = sys.argv[47]
    PYTHONUNBUFFERED = sys.argv[48]
    CONTAINER_MODE = sys.argv[49]
    CLUSTER_MODE = sys.argv[50]

    DB_DIR_PATH = sys.argv[51]
    INGRESS_NAME = sys.argv[52]
    INGRESS_EXT_PORT = sys.argv[53]
    REDIS_PASSWORD = sys.argv[54]

    LOGSTASH_HOST = sys.argv[55]
    LOGSTASH_PORT = sys.argv[56]
    ES_HOST = sys.argv[57]
    ES_PORT = sys.argv[58]
    ES_NODE_PORT = sys.argv[59]
    KIBANA_HOST = sys.argv[60]
    KIBANA_PORT = sys.argv[61]
    LOGSTASH_DOCKER_WORKDIR_PATH = sys.argv[62]
    KIBANA_DOCKER_WORKDIR_PATH = sys.argv[63]
    SINGA_AUTO_IMAGE_LOGSTASH = sys.argv[64]
    IMAGE_KIBANA = sys.argv[65]
    SINGA_AUTO_IMAGE_ES = sys.argv[66]
    KIBANA_EXT_PORT = sys.argv[67]
    SINGA_AUTO_IMAGE_SPARKAPP = sys.argv[68]
    SPAEK_DOCKER_JARS_PATH = sys.argv[69]
    ES_DOCKER_WORKDIR_PATH = sys.argv[70]

    #zk service
    content = {}
    content.setdefault('apiVersion', 'v1')
    content.setdefault('kind', 'Service')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', ZOOKEEPER_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', ZOOKEEPER_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'NodePort')
    ports = spec.setdefault('ports', [])
    ports.append({
        'port': int(ZOOKEEPER_PORT),
        'targetPort': int(ZOOKEEPER_PORT),
        'nodePort': int(ZOOKEEPER_EXT_PORT)
    })
    spec.setdefault('selector', {'name': ZOOKEEPER_HOST})
    with open('{}/scripts/kubernetes/start_zookeeper_service.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    #zk deployment
    content = {}
    content.setdefault('apiVersion', 'apps/v1')
    content.setdefault('kind', 'Deployment')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', ZOOKEEPER_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', ZOOKEEPER_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('replicas', 1)
    spec.setdefault('selector', {'matchLabels': {'name': ZOOKEEPER_HOST}})
    template = spec.setdefault('template', {})
    template.setdefault('metadata', {'labels': {'name': ZOOKEEPER_HOST}})
    container = {}
    container.setdefault('name', ZOOKEEPER_HOST)
    container.setdefault('image', IMAGE_ZOOKEEPER)
    env = []
    env.append({'name': 'CONTAINER_MODE', 'value': CONTAINER_MODE})
    container.setdefault('env', env)
    template.setdefault('spec', {'containers': [container]})
    with open('{}/scripts/kubernetes/start_zookeeper_deployment.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    #kafka service
    content = {}
    content.setdefault('apiVersion', 'v1')
    content.setdefault('kind', 'Service')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', KAFKA_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', KAFKA_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'NodePort')
    ports = spec.setdefault('ports', [])
    ports.append({
        'port': int(KAFKA_PORT),
        'targetPort': int(KAFKA_PORT),
        'nodePort': int(KAFKA_EXT_PORT)
    })
    spec.setdefault('selector', {'name': KAFKA_HOST})
    with open('{}/scripts/kubernetes/start_kafka_service.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    #kafka deployment
    content = {}
    content.setdefault('apiVersion', 'apps/v1')
    content.setdefault('kind', 'Deployment')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', KAFKA_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', KAFKA_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('replicas', 1)
    spec.setdefault('selector', {'matchLabels': {'name': KAFKA_HOST}})
    template = spec.setdefault('template', {})
    template.setdefault('metadata', {'labels': {'name': KAFKA_HOST}})
    container = {}
    container.setdefault('name', KAFKA_HOST)
    container.setdefault('image', IMAGE_KAFKA)
    env = []
    env.append({'name': 'CONTAINER_MODE', 'value': CONTAINER_MODE})
    env.append({'name': 'KAFKA_ZOOKEEPER_CONNECT', 'value': '{}:{}'.format(ZOOKEEPER_HOST, ZOOKEEPER_PORT)})
    env.append({'name': 'KAFKA_ADVERTISED_HOST_NAME', 'value': KAFKA_HOST})
    env.append({'name': 'KAFKA_MESSAGE_MAX_BYTES', 'value': "134217728"})
    env.append({'name': 'KAFKA_FETCH_MAX_BYTES', 'value': "134217728"})
    env.append({'name': 'KAFKA_ADVERTISED_PORT', 'value': KAFKA_PORT})
    container.setdefault('env', env)
    template.setdefault('spec', {'containers': [container]})
    with open('{}/scripts/kubernetes/start_kafka_deployment.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))


    # LogStash deployment
    content = {}
    content.setdefault('apiVersion', 'apps/v1')
    content.setdefault('kind', 'Deployment')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', LOGSTASH_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', LOGSTASH_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('replicas', 1)
    spec.setdefault('selector', {'matchLabels': {'name': LOGSTASH_HOST}})
    template = spec.setdefault('template', {})
    template.setdefault('metadata', {'labels': {'name': LOGSTASH_HOST}})
    container = {}
    container.setdefault('name', LOGSTASH_HOST)
    container.setdefault('image', '{}:{}'.format(SINGA_AUTO_IMAGE_LOGSTASH, SINGA_AUTO_VERSION))

    template.setdefault('spec', {'containers': [container]})
    env = []
    env.append({'name': 'LOGSTASH_DOCKER_WORKDIR_PATH', 'value': LOGSTASH_DOCKER_WORKDIR_PATH})
    env.append({'name': 'KAFKA_HOST', 'value': KAFKA_HOST})
    env.append({'name': 'KAFKA_PORT', 'value': KAFKA_PORT})
    container.setdefault('env', env)

    container.setdefault('volumeMounts',
                         [{'name': 'conf-path', 'mountPath': '{}/logstash.conf'.format(LOGSTASH_DOCKER_WORKDIR_PATH)}, \
                          {'name': 'log-path', 'mountPath': '{}/{}'.format(LOGSTASH_DOCKER_WORKDIR_PATH, LOGS_DIR_PATH)}, \
                          {'name': 'docker-path', 'mountPath': '/var/run/docker.sock'}])
    template['spec']['volumes'] = [
        {'name': 'conf-path', 'hostPath': {'path': '{}/scripts/config/logstash.conf'.format(HOST_WORKDIR_PATH)}}, \
        {'name': 'log-path', 'hostPath': {'path': '{}/{}'.format(HOST_WORKDIR_PATH, LOGS_DIR_PATH)}}, \
        {'name': 'docker-path', 'hostPath': {'path': '/var/run/docker.sock'}}]

    with open('{}/scripts/kubernetes/start_logstash_deployment.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # LogStash service
    content = {}
    content.setdefault('apiVersion', 'v1')
    content.setdefault('kind', 'Service')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', LOGSTASH_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', LOGSTASH_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'NodePort')
    ports = spec.setdefault('ports', [])
    ports.append({
        'port': int(LOGSTASH_PORT),
        'targetPort': int(LOGSTASH_PORT)
    })
    spec.setdefault('selector', {'name': LOGSTASH_HOST})
    with open('{}/scripts/kubernetes/start_logstash_service.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # kibana deployment
    content = {}
    content.setdefault('apiVersion', 'apps/v1')
    content.setdefault('kind', 'Deployment')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', KIBANA_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', KIBANA_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('replicas', 1)
    spec.setdefault('selector', {'matchLabels': {'name': KIBANA_HOST}})
    template = spec.setdefault('template', {})
    template.setdefault('metadata', {'labels': {'name': KIBANA_HOST}})
    container = {}
    container.setdefault('name', KIBANA_HOST)
    container.setdefault('image', '{}'.format(IMAGE_KIBANA))

    template.setdefault('spec', {'containers': [container]})

    with open('{}/scripts/kubernetes/start_kibana_deployment.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # kibana service
    content = {}
    content.setdefault('apiVersion', 'v1')
    content.setdefault('kind', 'Service')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', KIBANA_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', KIBANA_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'NodePort')
    ports = spec.setdefault('ports', [])
    ports.append({
        'port': int(KIBANA_PORT),
        'targetPort': int(KIBANA_PORT),
        'nodePort': int(KIBANA_EXT_PORT)
    })
    spec.setdefault('selector', {'name': KIBANA_HOST})
    with open('{}/scripts/kubernetes/start_kibana_service.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # es deployment
    content = {}
    content.setdefault('apiVersion', 'apps/v1')
    content.setdefault('kind', 'Deployment')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', ES_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', ES_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('replicas', 1)
    spec.setdefault('selector', {'matchLabels': {'name': ES_HOST}})
    template = spec.setdefault('template', {})
    template.setdefault('metadata', {'labels': {'name': ES_HOST}})
    container = {}
    container.setdefault('name', ES_HOST)
    container.setdefault('image', '{}:{}'.format(SINGA_AUTO_IMAGE_ES, SINGA_AUTO_VERSION))

    template.setdefault('spec', {'containers': [container]})
    env = []
    env.append({'name': 'discovery.type', 'value': 'single-node'})
    env.append({'name': 'ES_DOCKER_WORKDIR_PATH', 'value': ES_DOCKER_WORKDIR_PATH})
    container.setdefault('env', env)

    container.setdefault('volumeMounts',
                         [{'name': 'conf-path', 'mountPath': '{}/config/elasticsearch.yml'.format(LOGSTASH_DOCKER_WORKDIR_PATH)}, \
                          {'name': 'docker-path', 'mountPath': '/var/run/docker.sock'}])
    template['spec']['volumes'] = [
        {'name': 'conf-path', 'hostPath': {'path': '{}/scripts/config/elasticsearch.yml'.format(HOST_WORKDIR_PATH)}}, \
        {'name': 'docker-path', 'hostPath': {'path': '/var/run/docker.sock'}}]

    with open('{}/scripts/kubernetes/start_es_deployment.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # es service
    content = {}
    content.setdefault('apiVersion', 'v1')
    content.setdefault('kind', 'Service')
    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', ES_HOST)
    labels = metadata.setdefault('labels', {})
    labels.setdefault('name', ES_HOST)
    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'NodePort')
    ports = spec.setdefault('ports', [])
    ports.append({
        'port': int(ES_PORT),
        'targetPort': int(ES_PORT),
        'name': "{}".format(ES_PORT)
    })
    ports.append({
        'port': int(ES_NODE_PORT),
        'targetPort': int(ES_NODE_PORT),
        'name': "{}".format(ES_NODE_PORT)
    })

    spec.setdefault('selector', {'name': ES_HOST})
    with open('{}/scripts/kubernetes/start_es_service.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))

    # spark configure
    content = {}
    content.setdefault('apiVersion', "sparkoperator.k8s.io/v1beta2")
    content.setdefault('kind', 'SparkApplication')

    metadata = content.setdefault('metadata', {})
    metadata.setdefault('name', "singa-auto-monitor")
    metadata.setdefault('namespace', "default")

    spec = content.setdefault('spec', {})
    spec.setdefault('type', 'Scala')
    spec.setdefault('mode', 'cluster')
    spec.setdefault('image', '{}:{}'.format(SINGA_AUTO_IMAGE_SPARKAPP, SINGA_AUTO_VERSION))
    spec.setdefault('imagePullPolicy', 'IfNotPresent')
    spec.setdefault('mainClass', "com.singa.auto.monitor.stream.LogStreamProcess")
    spec.setdefault('mainApplicationFile', "local://{}/log_minitor-jar-with-dependencies.jar".format(SPAEK_DOCKER_JARS_PATH))
    spec.setdefault('sparkVersion', "2.4.5")

    restartPolicy = spec.setdefault('restartPolicy', {})
    restartPolicy.setdefault('type', "Always")

    driver = spec.setdefault('driver', {})
    driver.setdefault('cores', 1)
    driver.setdefault('coreLimit', "1000m")
    driver.setdefault('memory', "512m")
    driver.setdefault('labels', {"version": "2.4.5"})
    driver.setdefault('serviceAccount', "spark")

    executor = spec.setdefault('executor', {})
    executor.setdefault('cores', 1)
    executor.setdefault('instances', 2)
    executor.setdefault('memory', "512m")
    executor.setdefault('labels', {"version": "2.4.5"})

    with open('{}/scripts/kubernetes/spark-app.json'.format(PYTHONPATH), 'w') as f:
        f.write(json.dumps(content, indent=4))
