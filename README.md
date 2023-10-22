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







# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy for new iam user:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

    3. Get accessKey



## 3. Create ECR repo to store/save docker image
406468071577.dkr.ecr.eu-central-1.amazonaws.com/spotify

## 4. Create EC2 machine (Ubuntu) 
t2.micro
Get keypair

## 5. Open EC2 Terminal and Install docker in EC2 Machine:
	
	

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

# 6. Configure EC2 as self-hosted runner:
    In GIithub repository: setting>actions>runner>new self hosted runner> choose os> then run command one by one

Download
# Create a folder

mkdir actions-runner && cd actions-runner# Download the latest runner package

curl -o actions-runner-linux-x64-2.310.2.tar.gz -L https://github.com/actions/
runner/releases/download/v2.310.2/actions-runner-linux-x64-2.310.2.tar.gz# 

Optional: Validate the hash

echo "fb28a1c3715e0a6c5051af0e6eeff9c255009e2eec6fb08bc2708277fbb49f93  actions-runner-linux-x64-2.310.2.tar.gz" | shasum -a 256 -c# Extract the installer

tar xzf ./actions-runner-linux-x64-2.310.2.tar.gz


./config.sh --url https://github.com/benitomartin/mlops-music-clustering --token A3362R6P36FBFJM5W4OL2BTFGVPQ2# Last step, run it!

This will connect with GitHub
./run.sh

After this command you will see. Enter: self-hosted 
Enter the name of runner: [press Enter for ip-172-31-24-103]



# Use this YAML in your workflow file for each job
runs-on: self-hosted


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = eu-central-1

    AWS_ECR_LOGIN_URI = demo>>  406468071577.dkr.ecr.eu-central-1.amazonaws.com

    ECR_REPOSITORY_NAME = spotify



