version=`cat VERSION`
docker build -t pau1570/pauluv:latest .
docker tag pau1570/pauluv:latest pau1570/pauluv:$version
docker push pau1570/pauluv:latest
docker push pau1570/pauluv:$version 
