# Ticket Viewer for Zendesk 
* [Quickstart](#Getting-Started)
* [ZIP Method](#Method-2)
* [How it all Works](#How-it-all-works)



## Introduction: 
Interactive Web Page that interacts with Zendesk's API allowing user to view ticket details. If you don't have python you can install it here. To view the Python function, go to the routes.py file which is in the apps directory. For the the Javascript and HTML front end. Go inside the template folder which is inside the apps folder and view index.html. The written test functions are also inside the apps under tests.py. Enjoy!
- [Install Python](https://www.python.org/downloads/)
- IMPORTANT!! Make sure you have pop ups enabled for http://localhost:5000/index
- 
## Requirements
- Python 3.6+
- Download .env file from email into working directory

## Getting Started
Open the command prompt to get started

1. Clone the project to your local first
```
> git clone https://github.com/mhabeeb01/zcc_habeeb.git zendesk
```
2. cd into cloned directory 
```
> cd zendesk
```
3. Copy or move the .env to your current directory, make sure you know the name of .env (sometimes it just downloads as env)
```
> mv /dir/dir/.env current_dir
```
3. or for windows users: the file will be copied to active path IMPORTANT:Make sure .env is present
```
> COPY "{file_path\env}" .env
``` 
4. Make sure that you see the .env file, the app directory, zendesk.py
```
> dir
```
5. View your Python Version
```
> python3
```
6. Activate Virtual Enviroment
```
> python3 -m venv venv
```
7. Now tell the system you want to use its virtual environment.
```
> source venv/bin/activate
```
8. or for windows:
```
> venv\Scripts\activate
```
9. It should now look like this:
```
>(venv)$ _
```
10. Now that we have the virtual enviroment running, you can finally install Flask in it.
```
> pip install flask
```
11. verify you have flask in your virtual;
```
> >>> import flask
```

12. Now that we have flask, lets get the dependencies:
```
> pip install requests
> pip install python-dotenv
```
13. Finally we can run the application!
```
> flask run
```
14. View the webpage with the link below or go to http://localhost:5000/index

- [Zendesk Ticket Viewer](http://localhost:5000/index)


## Method 2
- Download as zip file
- Extract
- move the .env file into zcc_habeeb-main directory (*make sure it is .env)
- open cmd or terminal in the zcc_habeeb-main directory 
- verify file format zcc_habeeb/
- ![image](https://user-images.githubusercontent.com/83475870/128088825-ec80678c-9980-4163-b81b-dd4d27ce4e2a.png)
 * [Follow steps](#Getting-Started)

## How it all works
So in this project, I implemented a flask backend that would go and get the API tickets using Zendesks web API call. After that, The Flask would run on a virtual environment and run that python code to get API and keep calling the API until there is no more ['next_page'] and send that to the HTML and JavaScript front end using return render_template. The dotenv would contain the requirement, which is the API credentials. The javascript would loop through the JSON, display the correct information needed, and send it to the HTML. 



                      

