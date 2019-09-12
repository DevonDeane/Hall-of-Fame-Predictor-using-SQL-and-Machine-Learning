# Final Project ECE 656 WInter 2019
   -Diego Cepeda 20763269
   -Devon Deane 20788525
   -Yeganeh Sana 20767809

## Description of the program##
Predic whether a Batter/Pitcher is going to be nominatd to the Hall Of Fame based on their career statistics.
   
   -Select table to use.
   -Select 10 features. 
   -Choose % of data used for training the model.
   -Choose Classifier used Decicion-Tree/Naive-Bayes.

## Required python packages can be found in the requirements.txt file located within the folder
## To automatically install these dependencies the command below can be used
   pip install -r requirements.txt

## Setup Instructions
1- In MySQL, run the baseballDump.sql file in order to create a new Lahman Baseball database.
2- Then run the Project.sql file in order to create the required stored procedures for the Database.
3- In a new terminal run the Server.py file using the command : "python Server.py"
   3.1- Enter hostname for the MySQL Database:
   3.2- Enter username for the MySQL Database:
   3.3- Enter Password for the MySQL Database:
4- In another terminal Run the Client.py file using the command : "python Client.py"
5- Then follow the instructions provided by the GUI
