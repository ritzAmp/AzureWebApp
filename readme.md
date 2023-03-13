#### This guide focuses on using the services of Azure Web App and Azure DevOps rather than the content/nature of the web app itself.
#### Step-by-step guide to build a Python web app and deploy it to Azure App Services as a Linux Web App.

##### First, proceed with the steps that are common for both deployment options.
**A. On the Azure Portal**
Create an 'App Service Plan' within a 'Resource Group'.
And within that 'App Service Plan' create a Web App.
Since we are deploying python app, pick the following instance details,
Runtime stack: Python && Operating system: Linux
Review+Create.
The web app is up and running and is ready to receive the app's code.
On the web app resource, Deployment center -> source: Local Git
Copy the Git Clone Uri (we will use this later)

**B. On the local machine**
Create the app folder, and an app's landing/default page app.py inside it.
On the VS Code terminal:
```bash session
python3 -m venv .venv
source .venv/bin/activate
pip3 install flask 
```
View the web app dependencies and list them on a file 
```bash
pip3 freeze
pip3 freeze > requirements.txt
```
Initialize git, and put the code into source-control repo 
```bash
git init
git add .
git commit -m "Initial commit"
```


##### App deeployment options:
1. From local repository to Azure App Services
2. Build a pipeline within AzureDevOps and deploy to Azure App Services 

**1. Deploying from local repository**
On the VS Code, add remote and push the code 
```bash
git remote add azure <git clone uri>    #link copied on step A
git push azure main:master           
```
If authentication fails during git push;
Azure portal -> deployment center -> user scope, and create the credentials, and used them when prompted for username, password on VScode.
After the push is successful, give it few minutes then confirm the deployment by loading/refreshing the default domain link.

**2. Creating a pipeline on Azure DevOps**
On Azure DevOps portal
Create a project
Go to Repos, copy the HTTPS link from 'Push an existing repository from command line' section.

On the local machine
```bash
git remote add origin <previously copied HTTPS link>
git remote -v           
git push -u origin --all
```

If it gives authentication failed error, find 'Generate Git Credentials' under Project -> Repos -> Clone to your computer, and authenticate with that credential.
The code is in Azure pipeline server, now we can set up a build to deploy the python web app to Azure, for that follow the following steps:
Project -> Piplines -> Azure Repos Git -> Select the repo -> Python to Linux web App on Azure -> Authenticate to Azure subscription -> pick the web App created on step A -> Validate and configure.  
YAML pipeline file is now generated and added to the repo, and it can be configured for various things.
YAML is used to build and deploy the app.
Click 'Save and Run'
The process builds and deploys the app to Azure web app.
Confirm the deployment by clicking/refreshing the default domain link of the Azure web app
Now any changes made to the local repo and pushed to Azure DevOps repo, it will trigger the YAML main, the yaml pipeline runs and it builds and deploys the changes/modification to Azure web apps
