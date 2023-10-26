# MLOps Music Clustering 🎸

<p>
    <img src="/images/cassette.jpg"/>
    </p>

This is a personal MLOps project based on this [Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db) dataset with music features from Spotify. Below you can find some instructions to understand the project content. Feel free to clone this repo 😉


## Tech Stack

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23d9ead3.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)


## Project Structure

The project has been structured with the following folders and files:

-`.github/workflows`: CI/CD Pipeline
- `data`: dataset 
- `images:` images from results
- `notebooks:` EDA and Modelling performed at the beginning of the project to establish a baseline
- `model:` saved best model
- `requirements.txt:` project requirements
- `Dockerfile`: docker image for deployment
- `app.py`: FastAPI app

## Project Description

### Exploratory Data Analysis

The dataset was obtained from Kaggle and contains 232'725 rows and various columns with song features:

- genre
- danceability
  loudness      
- artist_name
- duration_ms
- mode   
- track_name
- energy
- speechiness
- track_id
- instrumentalness
- tempo
- popularity
- keys
- time_signature
- acousticness
- liveness
- valence
 			 			
To prepare the data for modelling, an **Exploratory Data Analysis** was conducted to preprocess the numerical features, and suitable scalers were chosen for the preprocessing pipeline. Prior to scaling by plotting 3 features it can be seen that they are not very correlated except from acousticness, energy and loudness. 

<p align="center">
    <img src="/images/scatter_non_scaled.png"/>
    </p>

<p align="center">
    <img src="/images/correlation.png"/>
    </p>

For chosing the scalers the distribution and boxplot of each features was analyzed. The features with significant outliers were scaled with RobustScaler, features normally distributed with StandardScaler and the rest with MinMmaxScaler. 

<p>
    <img src="/images/popularity.png"/>
    </p>
<p>
    <img src="/images/acousticness.png"/>
    </p>

Afterwards, the scaled features were fitted in a **PCA model** with the follwoing objectives: 

- reduce dimensionality to get a better visual feedback on our clustering
- use the orthogonality of the principal components so that the KMeans algorithm increases its clustering power

A threshold of **95% explained variance** was set up in order to get the number of pricipal components, which ended up being 3.

<p>
    <img src="/images/PCAs.png"/>
    </p>

Then we determine the optimal number of clusters for **K-Means** using the within-cluster sum of squares (WCSS) method and the "elbow" or "knee" point in the WCSS curve:

- **Calculate WCSS for different numbers of clusters**: The code iterates through a range of cluster numbers from 1 to max_clusters - 1 and fits a K-Means model to the data. The kmeans.inertia_ attribute returns the WCSS for the current number of clusters, which is then appended to the wcss list.

- **Determine the optimal number of clusters**: The KneeLocator is used to find the optimal number of clusters based on the WCSS values. The 'elbow' or 'knee' point represents the optimal number of clusters where adding more clusters doesn't significantly reduce the WCSS.

<p>
    <img src="/images/elbow.png"/>
    </p>

The results after scaling, getting the number of PCs (3) and clusters (5), show a clear grouping of the numerical features, as well as the distribution of the features along each cluster.

<p align="center">
    <img src="/images/scatter_scaled.png"/>
    </p>

<p align="center">
    <img src="/images/radar.png"/>
    </p>

### Modelling

After the EDA, a classifier modelling was perfomed using the following models:

- KNeighborsClassifier
- MLPClassifier
- SVC
- AdaBoostClassifier
- DecisionTreeClassifier
- GaussianNB
- RandomForestClassifier
- QuadraticDiscriminantAnalysis



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
406468071577.dkr.ecr.eu-central-1.amazonaws.com/music

## 4. Create EC2 machine (Ubuntu) 
t2.micro

Allow: HTTPS, SSH and HTTP

Get 30 instead of 8 gp2 Storage

Get keypair

## 5. Open EC2 Terminal and Install docker in EC2 Machine:
	
	

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

Check docker is installed
    docker --version

# 6. Configure EC2 as self-hosted runner:
    In GIithub repository: setting>actions>runner>new self hosted runner> choose os> then run command one by one

    Select Linux as runner image on the top

Download
# Create a folder

Press enter everywhere except in the self-hosted

mkdir actions-runner && cd actions-runner  # Download the latest runner package

curl -o actions-runner-linux-x64-2.310.2.tar.gz -L https://github.com/actions/
runner/releases/download/v2.310.2/actions-runner-linux-x64-2.310.2.tar.gz# 

Optional: Validate the hash

echo "fb28a1c3715e0a6c5051af0e6eeff9c255009e2eec6fb08bc2708277fbb49f93  actions-runner-linux-x64-2.310.2.tar.gz" | shasum -a 256 -c# Extract the installer

tar xzf ./actions-runner-linux-x64-2.310.2.tar.gz

This configures the repository
./config.sh --url https://github.com/benitomartin/mlops-music-clustering --token A3362R6P36FBFJM5W4OL2BTFGVPQ2# Last step, run it!

After this command you will see. Enter: self-hosted (see yaml file in github actions)
Enter the name of runner: [press Enter for ip-172-31-24-103]

This will connect with GitHub
./run.sh





# Use this YAML in your workflow file for each job
runs-on: self-hosted


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = eu-central-1

    AWS_ECR_LOGIN_URI = demo>>  406468071577.dkr.ecr.eu-central-1.amazonaws.com

    ECR_REPOSITORY_NAME = musicapp



If everything works, then add the port (Custom TCP) of the app (8080 in the security groups of the instance)
