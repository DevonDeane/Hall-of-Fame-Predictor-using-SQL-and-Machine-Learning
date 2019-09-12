#!/usr/bin/env python
# coding: utf-8

# In[148]:


import numpy as np
import pandas as pd
from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
import easygui
import mysql.connector
import time
import socket





def functionToCreateTables(x):
    x = mydb.cmd_query(x)
    y =mydb.get_rows(count = None)
    listA = [x]
    listA
    listB = list()
    for i in listA:
        listB.append([i])
    pd.DataFrame(x.items())
    n = x.items()
    n

    listC = list()

    for key, value in x.items():
        temp = [key,value]
        listC.append(temp)

    listC

    colnames = listC[1]
    names = colnames[1]

    nameList = list()

    for i in names:
        nameList.append(i[0])


    nameList

    listD = list()
    y[0]

    data = pd.DataFrame(y[0], columns = nameList)#columns=['q_data'])
    data = data.replace("",np.NaN) # Consider this being a pure NULLIST 
    return data




try: ## wrap this around everything
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    data = client_socket.recv(1024).decode()
    text = 'Credentials Recieved'
    datastr=str(data)
    datalist = datastr.split (",")



    mydb = mysql.connector.connect(
    host=datalist[0],
    user=datalist[1],
    passwd=datalist[2]
    )

    mydb.cmd_query("use project;")
    skip = False
    welcomeString = "Welcome to the Client/Server Predictive Analysis Classifier Model!\n\n\n"+ "In this program you will be able to:\n\n"+ "Predic whether a Batter/Pitcher is going to be nominatd to the hall of same based on its statistics.\n"+ "-Select table to use.\n"+ "-Select 10 features.\n" + "-Choose % of data used for training the model.\n"+ "-Choose Classifier used Decicion-Tree/Naive-Bayes.\n\n\nPlease select \"Continue\" if you wish to proceed and \"Cancel\" if you wish to Exit!\n"
    msg = welcomeString  
    title = "Client/Server Predictive Analysis Classifier Model"
    if easygui.ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:  # user chose Cancel
        skip = True
#     msgbox("Welcome to the Client/Server Predictive Analysis \\
#     Classifier Model!\n Select \"Continue\" if you wish to proceed!", ok_button="Good job!")
    while(True and skip == False):

       tableName = easygui.buttonbox('What table would you like to gain insight from?', 'Type Selector', ('Batting', 'Pitching'))

       # easygui.msgbox('You have selected '+ str(tableName)+'.', 'Choice Display')
       # Remove yearID
       if tableName == 'Batting':
           tab = functionToCreateTables("select * from "+ str(tableName) +" limit 1;")
           tabTrim = tab.drop(tab.columns[[-1,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )

       else:
           tab = functionToCreateTables("select * from "+ str(tableName) +" limit 1;")
           tabTrim = tab.drop(tab.columns[[-1,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           tabTrim = tabTrim.drop(tabTrim.columns[[0,]], axis=1, )
           #print(tabTrim.columns)

       while(True):
           msgA ="SELECT EXACTLY 10 FEATURES on which the classifier will train from?\n\
           Note: Failure to comply will result in an ERROR!"
           titleA = "Feature Selection"
           if tableName == "Batting":
               choices = tabTrim.columns#trainPres.columns
               choice = easygui.multchoicebox(msgA, titleA, choices)

           elif tableName == "Pitching":
               choices = tabTrim.columns
               choice = easygui.multchoicebox(msgA, titleA, choices)


    #         easygui.msgbox('You have selected:\n '+ str(split)+'.', 'Choice Display')
    
           if not(choice):
               break

           elif len(choice) < 10 or len(choice) > 10:            
               easygui.msgbox("As stated previously, select TEN (10) features!", ok_button="Retry")
           
           
            
           else:
               break
        
       if not(choice):
               break 

       str4 = ','.join(choice)
    
#        easygui.msgbox('You have selected:\n '+ str4 +'.', 'Choice Display')
       cols = choice
       # tab
       str1 = ','.join(choice)
       # print(str1)
       stringToSend = str(tableName) + "," + str1
       print(stringToSend)
       client_socket.send(stringToSend.encode())  # send message
       msg = client_socket.recv(1024).decode()  # receive response
       print(msg)  # show in terminal



       split = easygui.choicebox('What percentage of data would you like to train on?', 'Data Split', ('0.1', '0.2','0.3', '0.4','0.5', '0.6','0.7', '0.8','0.9'))
       
    
#        easygui.msgbox('You have selected '+ str(split)+'.', 'Choice Display')


       s = "Split"
       splitToSend = s + "," + str(split)
       print( "Sending: Split")
       client_socket.send(splitToSend.encode())  # send message
       msg = client_socket.recv(1024).decode()  # receive response



       classifierName = easygui.buttonbox('Please select a classifier to use for analysis?', 'Classifier Selector', ('Decision Tree Classifier', 'Naive Bayes Classifier'))
       
       easygui.msgbox('You have selected:\n\n'      
       + "Table: " +str(tableName) +" Table to analyze"+'.'+'\n'
       + "Features: "+str4 +'.'+'\n'
       + 'Split: '+ str(split)+'.'+'\n' 
       + "Classifier: "+ str(classifierName) +'.', 'Classifier Specifications Display')
       opt = ["Train/Test"]
       start = easygui.buttonbox('To proceed to classification, please select Train/Test', 'Classifier Fitting', choices = opt)  





       if classifierName == "Decision Tree Classifier":
           clName = "DT"
       elif classifierName == "Naive Bayes Classifier":
           clName = "NB"

       trainTest = start + "," +clName
       client_socket.send(trainTest.encode())  # send message
       msg = client_socket.recv(1024).decode()  # receive response
       print(msg)  # show in terminal
       vals = stringToSend,splitToSend,trainTest
       for val in vals:
       # or rather send values to server
           print(val)

    #        time.sleep(3)
       averages = msg.split (",")
       #averages = [0.5,0.6,0.7]
       # recieve values from server
       print(averages[0])  # show in terminal
       sValA = float(averages[0])
       sValB = float(averages[1])
       sValC = float(averages[2])

       acc = sValA * 100
       pre = sValB * 100
       rec = sValC * 100

       easygui.msgbox("Accuracy  : "+str(acc)+" %\nPrecision : "+str(pre)+" %\nRecall    : "+str(rec)+" %\n","Validation Results","Please press \"OK\" to continue!")

       msgC = "Would you like to run again?\nIf yes select \"Continue\", otherwise select \"Cancel\" to close the program"
       titleC = "Restart or Exit"

       if easygui.ccbox(msgC, titleC):     # show a Continue/Cancel dialog
           print( "Re-Loop")
           continue
       else:  # user chose Cancel

          break
    print( "Sending: Exit")
    message ="exit"
    client_socket.send(message.encode())  # send message
    msg = client_socket.recv(1024).decode()  # receive response
    print(msg)  # show in terminal
except:
    easygui.exceptionbox()