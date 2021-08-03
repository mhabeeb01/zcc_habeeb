# Ticket Viewer for Zendesk 
Interactive Web Page that interacts with Zendesk's API allowing user to view ticket details. If you don't have python you can install it here
- [Install Python](https://www.python.org/downloads/)

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
4. Make sure that you see the .env file, the app directory.
```
> dir
```
5. View your Python Version
```
> python3
```
6. Now tell the system you want to use its virtual environment.
```
> source venv/bin/activate
```
7. or for windows:
```
> venv\Scripts\activate
```
8. It should now look like this:
```
>(venv)$ _
```
9. Now that we have the virtual enviroment running, you can finally install Flask in it.
```
> pip install flask
```
10. verify you have flask in your virtual;
```
> >>> import flask
```

11. Now that we have flask, lets get the dependencies:
```
> pip install requests
> pip install dotenv
```
12. Finally we can run the application!
```
> flask run
```
13. View the webpage with the link below or go to http://localhost:5000/index

- [Zendesk Ticket Viewer](http://localhost:5000/index)


##Method  2
- Download as zip file
- Extract
- move the .env file into zcc_habeeb-main directory (*make sure it is .env)
- open cmd or terminal in the zcc_habeeb-main directory 
- verify file format zcc_habeeb/
                       venv/
                       app/
                         test.py
                         __init__.py
                         routes.py
                         templates/
                              index.html
                             error.html
                         zendesk.py
                         .env

