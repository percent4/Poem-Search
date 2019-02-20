tag=$1
# -f 指定文件 ， -t 指定生成镜像名称 ， 冒号后为版本号，最后的.表示docker_file的上下文环境
docker build -f poem_search.build -t hub.docker.com/poem_search:test.${tag} .