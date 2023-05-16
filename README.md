# Funle-ai README

# Introduction 
Funnle scrapes assignments from multiple sources on the internet 4 times a day. 
To get the assignments to the right developers, these assignments are categorised for a more accessible 
and better specified and jobsearching experiance. 
Funnle categorises all assignments into 1 of 7 categories:
  1. Other
  2. Analysis
  3. Development
  4. Management
  5. Operations
  6. Security
  7. Testing

#Description
The dataset used to train the AIs is compiled by Funle en consists of over 3000 categorised assignments. 
The AIs are trained using the titles as X value (input) and CategoryId as y_value (result).

The application uses 4 AI algorithms in conjunction with each other and pools the results.
The AIs give a probability between 1 and 0 (100%-0%) for each category.

To improve accuracy and to prevent filter out false predictions as much as possible, 
the results of all 4 AIs are pooled. The AI's must predict the same category Id 
with a probability over a threshold value (80%) for the categoryId to be updated.


# Getting Started
- Install sure [Python 3.9](https://www.python.org/downloads/release/python-3912/)
- Install [pip](https://phoenixnap.com/kb/install-pip-windows).
- make sure to assign the right DB connection info in the .env file.
- Install all dependencies  and tensorflow,
  - (tensorflow is not included in requirements.txt because of deployment issues),

```bash
pip install -r requirements.txt
pip install tensorflow
```


# Development
Funle-ai can now run locally the AI's locally for testing and development purposes. 
run the application in the terminal with command-line arguments:
- funle-ai command-line arguments:
  - -h: Help
  - -p: Predict
  - -t: Train
  - -u: Update active AI
  - -r: Restore old AI
  - -c: Compare performance
```bash
python main.py -h
```


# Build and Test
For testing purposes you can create a docker image of the application and run the application in a cointainer like it 
does on the production server.

The docker image is build using the westmere tensorflow.whl. This compiled version of tensorflowed is required  for the
application to be runnable on the funle server.

A docker volume is used to save trained AI models between containers.

- Create docker volume:
```bash
docker volume create funle-ai-volume
```
- Build a docker image: 
```bash
docker build -t funle-ai .
```
- Run docker: 
  - -it: interactive terminal 
  - -v: assign volume (local-volume:container-mountpoint)
```bash
docker run -it -v funle-ai-volume:/app/ml_models funle-ai -p
```


# Deploy new build:
- Commit and push to [git origin/main](https://dev.azure.com/semantica-nl/funle.nl/_git/funle-ai).
- Run funle-ai pipeline on [Azure DevOps](https://dev.azure.com/semantica-nl/funle.nl/_build).
- The latest funle-ai image is automaticly in use and is called by cronjob when needed.
  - The new Image can be manualy run with a docker run command.
    - --rm: Remove container when done
    - --network=funle-internal: connect to funle-internal network for db connection
```bash
docker run -t --rm --network=funle-internal -v funle-ai-volume:/app/ml_models semanticasoftware/funle-ai -p
```

#Project status
The application v1.0 is currenly running in production.

//todo, implement application versions
