app=foreend
username=docker-user
password=docker-user-password

docker build -t $app .

docker login --username=$username --password=$password

docker tag $app $username/$app:latest

docker push $username/$app:latest