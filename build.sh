version=`cat VERSION`
docker build -t ghcr.io/pau1570/pauluv.com:latest .
docker push ghcr.io/pau1570/pauluv.com:latest
