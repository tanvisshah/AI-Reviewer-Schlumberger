# ENG 573 Spring 2021 Project
## Schlumberger AI Report Reviewer
___

This project is for the ENG 573 Capstone Project for Spring 2021

Below is a link to the Final Report for the project
    https://docs.google.com/document/d/1NiFe47H0pdAAa_Oi8QMvLlpRrnyIxDp9nG_U_JMabO0/edit?usp=sharing





# How to Set up on any server with Docker installed

(Assuming that the migrations directory and database.db files already exist)

To build the docker container and to run it on port 8018 of the server, run the start script by:

    sh start.sh

This will create a docker image called reviewtool and run it with the same name. If this script needs to be rerun, the following error will show up:

docker: Error response from daemon: Conflict. The container name "/reviewtool" is already in use by container "306c5721f36529c2082f08f2cdceac3882696b95ed6bd5721641d1a2e2e54f9b". You have to remove (or rename) that container to be able to reuse that name.

To fix this, stop and remove the docker containers by running the following commands:

    docker stop reviewtool
    docker rm reviewtool

The Web Application will now be hosted at the following address:

    <IP Address of the Server>:8018

There is a default user: 
Username: admin
Password: admin

Or you can register a new user to get started.

# How to reset the database and delete all previous data

Enter the root directory of the repository

1. Create a Python3 Virtual Environment 

     python3 -m venv venv 
     source venv/bin/activate

2. Install all the dependencies in requirements.txt obtained via pip freeze (There exists another file, pythonLibrariesUsed.txt which contains a list of the different libraries used in the project)

    pip3 install -r requirements.txt 

To first set up the database tables and the migrations folder runt the following commands. This only needs to be run once.

    flask db init
    flask db migrate
    flask db upgrade   

After this step, ensure that the following directories and files exist in the root of the repository:

- migrations: Generated after running the init/migrate/upgrade sequence above
- database.db: Generated after running the init/migrate/upgrade sequence above



## Porting the information to another server and preserving data:

If the Web App needs to be hosted on a different server or cloud service, then the database.db file, migrations folder, and the data folder is important. These contain information and metadata of the files that are stored and the registered users.


## Running the webapplication for development locally:

Run Steps 1 and 2 from above to create the virtual environment.

Run the command:

    python3 run.py

This will start the flask server, and the application can now be accessed at 

    localhost:5000