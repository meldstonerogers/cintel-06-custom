# cintel-06-custom
Cintel Project 6
Melissa Stone Rogers, [GitHub](https://github.com/meldstonerogers/cintel-06-custom)

## Introduction
Professional project using python, shiny, and reactive.calc function to publish a reactive shiny app using the [Banana Quality Dataset](https://www.kaggle.com/datasets/mrmars1010/banana-quality-dataset/data). Project was created using the [Py-Shiny-Templates/dashboard](https://github.com/posit-dev/py-shiny-templates/tree/main/dashboard).
Commands were used on a Mac machine running zsh. 

## Project Set Up and Dependency Management 
### Build project in GitHub
Create project repository in Github. Create a requirements.txt and .gitignore file for Python code. Add the following to your requirements.txt: 
- faicons 
- pandas
- pyarrow
- plotly
- scipy
- shiny
- shinylive 
- shinywidgets
- seaborn
- shinylive 
- shinywidgets
- shinyswatch

Since you do not want to fork or copy the entire py-shiny-template repository, you can use [this online tool](https://download-directory.github.io/) to download just the desired template folder. Once the folder was downloaded to my machine, I uploaded the whole file to my create project reposity. Then, save and upload the [Banana Quality Dataset](https://www.kaggle.com/datasets/mrmars1010/banana-quality-dataset/data) to your main project folder. Save in folder with main app.py file, separate from other files. 

### Publish GitHub Pages for your project repository.

Add your styles.css file to a new folder named docs. Now you are ready to publish a GitHub Page for your app. 

The following instructions borrowed from Dr. Cases's Continous Intelligence Course within NWSU's School of Computer Science and Information Systems: 

1. Go to the repository on GitHub and navigate to the **Settings** tab.
2. Scroll down and click the **Pages** section down the left.
3. Select branch main as the source for the site.
4. Change from the root folder to the docs folder to publish from.
5. Click Save and wait for the site to build.
6. Eventually, be patient, your app will be published and if you scroll to the top of the Pages tab, you'll see your github.io URL for the hosted web app. Copy this to your clipboard. 
7. Back on the main repo page, find the About section of the repo (kind of upper right).
8. Edit the "About" section of the repository to include a link to your hosted web app by using the Pages URL. 

### Clone repository to your machine
```
git clone project.url
```
Verify Python version of Python 3
```
python3 --version

```
```
python3 -m venv venv
source venv/bin/activate
```
## Install required packages and dependencies into virtual enviornment

Install VS Code Extension for Shiny if you have not done so already.

Install required packages and dependencies. 
```
pip install -r requirements.txt
```
Freeze dependencies to requirements.txt  
```
python3 -m pip freeze > requirements.txt
```

### Initial Project Save
```
git add .
git commit -m "initial"                         
git push origin main
```
## Start Your Project 


### Troubleshooting
Using the following code, I attempted to run my Shiny app within a web browser. 
```
shiny run --reload --launch-browser penguins/app.py
```

I got numerous errors and my app would not run and launch. Thanks to dilligent colleagues within the NWSU's Continuous Intelligence course, the following troubleshooting was noted. To successfully launch my Shiny app, I downgraded websockets to version 10.4 from 14.0 using the following code.
```
pip install websockets==10.4
```

Once completed, I was able to successfully run my Shiny app within a web browser with the initial code provided above.

## Complete Your Project
Save your project and push back to your repository. 
```
git add .
git commit -m "final"                         
git push origin main
```
