# Employee Attrition Prediction Model Deployment


## Overview
This dataset contains information about employees, including both numerical and categorical features. It is used for predicting employee attrition- employee will leave or not depending on the features.This project involves deploying a machine learning model using Docker and Flask. The deployment is achieved through a Docker container with a Flask API.

## Features
- **Numerical Features:**
  - Joining Year
  - Payment tier
  - Age
  - Experience in current domain

- **Categorical Features:**
  - Education
  - City
  - Gender
  - Ever Benched

- **Target Variable:**
- Leave or Not

## Model Training
The machine learning model is trained to predict employee attrition based on features mentioned above after converting category variables in numerical as well using ('get dummies'). The model is saved as a joblib file (`model.joblib`) for later use.

## Flask API
The Flask API serves as the interface for making predictions using the trained model. The API endpoint (`/predict`) accepts JSON input with employee features(including both numerical and one-hot encoded categorical features) and returns the predicted attrition status.

## Dockerization
The project is Dockerized for easy deployment and reproducibility. The Dockerfile contains instructions to build an image with all dependencies and the Flask application.

## Requirements.txt 
This file lists the libraries and their versions that the project depends on. When someone wants to run or develop project, they can use these files to install the required dependencies automatically.

## Installation
1.Clone the repository.
2.Navigate to the project directory.

## Usage
To run the Python script, you'll need to use the 'Update docker-image.yml' configuration file

