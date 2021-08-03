# Ticket Viewer for Zendesk 
Interactive Web Page that interacts with Zendesk's API allowing user to view ticket details

## Requirements
-Python 3.6+
-.env file from email.

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
3. Copy or move the .env file to into this directory; the file will be copied to active path 
```
> COPY "{file_path\env}" .env
```
4. Make sure that you see the .env file, the app directory, and the zendesk.py file. Also check you have the correct python version.
```
> dir
>python3
```
5. Now tell the system you want to use its virtual environment.
```
> source venv/bin/activate
>(venv)$ _
```
6. Now that we have the virtual enviroment running, you can finally install Flask in it.
```
> pip install flask
```

7. Now that we have flask, lets get the dependencies:
```
> pip install requests
> pip install dotenv
```
8. Finally we can run the application
```
> flask run
```


### Windows
