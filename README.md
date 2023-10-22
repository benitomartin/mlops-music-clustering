In POSTMAN

Key: Content-Type: 
Value: application/json

Post request
http://localhost:9696/predict

Body
{
    "popularity": 1,
    "acousticness": 1,
    "danceability": 1,
    "duration_ms": 1,
    "energy": 1,
    "instrumentalness": 1,
    "liveness": 1,
    "loudness": 1,
    "speechiness": 1,
    "tempo": 1,
    "valence": 1
}


ECR
406468071577.dkr.ecr.eu-central-1.amazonaws.com/spotify

EC2 Instance

	sudo apt-get update -y	
    sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

docker --version to see that is running