
## End to End Machine Learning Projects

Date: 13-Dec-24
END TO END ML PROJECTS - KRISH NAIK YOUTUBE CHANNEL
https://www.youtube.com/watch?v=Rv6UFGNmNZg&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=2

Set up project with GitHub
1.	Data Ingestion
2.	Data Transformation
3.	Model Trainer
4.	Model Evaluation
5.	Model Deployment

CI/CD Pipelines - GitHub Actions
Deployment AWS



Tutorial 1 - GitHub & Code Set up
1. Set up the GitHub repository
	Create new GitHub repository

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

b) setup.py
c) requirements.txt
d) src folder and build the packages
	pip install -r requirements.txt
	

Tutorial 2- Project Structure, Logging And Exception Handling
Create components folder in src folder.
Create files in components folder
Create pipeline folder – training and prediction pipeline 

