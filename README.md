
<h1>End to End Machine Learning Projects</h1>

Date: 13-Dec-24

END TO END ML PROJECTS - KRISH NAIK YOUTUBE CHANNEL

https://www.youtube.com/watch?v=Rv6UFGNmNZg&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=2

I. Set up project with GitHub
1.	Data Ingestion
2.	Data Transformation
3.	Model Trainer
4.	Model Evaluation
5.	Model Deployment

II. CI/CD Pipelines - GitHub Actions

III. Deployment AWS

<h2>Tutorial 1 - GitHub & Code Set up</h2>
1. Set up the GitHub repository

a) new environment 

	Create new venv in VScode terminal

	conda create -p venv python==3.12 -y

	conda activate venv/

	git init
	git add README.md (first create README.md file in VScode)
	git commit -m "first commit"

	Add this for first time:
	git config --global user.email "akshaykr7775@gmail.com"
	git config --global user.name "Akshay Kumar"

	git branch -M main
	git remote add origin https://github.com/akshaykr7/mlproject.git
	git remote -v (optional)
	git push -u origin main
	create .gitignore file in GitHub webpage – create new file and select python
	git pull (to merge changes done in GitHub webpage)

b) setup.py - create ML application as a package and send to Pypi

Whenever setup.py will run it will search for folder which have __init__.py and consider that package as a package.

c) requirements.txt

-e . -> map to the setup.py and it will run

d) src folder and build the packages

	pip install -r requirements.txt
	

<h2>Tutorial 2- Project Structure, Logging And Exception Handling</h2>

1. Create components folder in src folder.
2. Create files in components folder
3. Create pipeline folder – training and prediction pipeline 

