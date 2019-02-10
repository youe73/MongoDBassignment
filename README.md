# MongoDBassignment

This assingment has been done solely on python jupytor notebook due to some technical issues in attempt to using docker, vagrant from window. First objective was to use docker containers and the MongoDB, python, dockerfile and the python script was implemented and build in the container. But it could not run the command, so Python script will be the only file.   

Prerequisite:
Download python and jupytor notebook with the following command:
pip install python 3
pip install jupytor notebook

It can also be done in google colab https://colab.research.google.com/notebooks/welcome.ipynb 
You will need a googledriver account

Download the data from http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip 

After the download it should be possible to run the code from the file uploaded.

Some parts have been solved with normal list and loops and not the MongoDB queries as was intended. 
The database would also slow down and the computer froze serveral times due to the large amount of data. Hence some of the assignment is not adequately solved as intended. 

1. How many Twitter users are in the database?
Made a query to retieve all those who has a username. 

2. Which Twitter users link the most to other Twitter users? (Provide the top ten.)
Find those username whose tweed has most duplicate @ in the text 

3. Who are the most mentioned Twitter users? (Provide the top five.)
Find the repeting usernames in the text

4. Who are the most active Twitter users (top ten)?
Find the users who has most tweed   

5. Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
Find those with polarity equals 0 or 4. 







 




