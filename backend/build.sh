app=backend
version=v1
username=docker-user
password=docker-user-password

docker build -t $app . --build-arg VERSION=$version

docker login --username=$username --password=$password

docker tag $app $username/$app:$version

docker push $username/$app:$version