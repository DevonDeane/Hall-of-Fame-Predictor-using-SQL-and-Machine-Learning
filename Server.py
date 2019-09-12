#!/usr/bin/env python


import mysql.connector
import socket
import numpy as np
import sklearn
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
def functionToCreateTables(x):
    x = mydb.cmd_query(x)
    y =mydb.get_rows(count = None)
    # y = [i for i in x]
    # x
    #mydb.get_rows(count = None)
    listA = [x]
    listA
    listB = list()
    for i in listA:
        listB.append([i])

    # listB[0].split(',')
    # x.
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
    # for key, value in y.items():
    #     temp = [key,value]
    #     listC.append(temp)

    data = pd.DataFrame(y[0], columns = nameList)#columns=['q_data'])
    data = data.replace("",np.NaN) # Consider this being a pure NULLIST 
    return data


#Host="localhost"
#User ="root"
#Password ="admin"

if __name__ == '__main__':

    # Enter Database Credentials
    print("Enter Host Name:")
    Host = input()
    print("Enter User Name:")
    User = input()
    print("Enter Password:")
    Password = input()

    # Server Socket Creation
    host = socket.gethostname()
    port = 5000  
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print("Server Started")

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()
    credentials=Host+','+User+','+Password
    conn.send(credentials.encode())

    mydb = mysql.connector.connect(
       host=Host,
       user=User,
       passwd=Password
    )

    cursor = mydb.cursor()
    mydb.cmd_query("use project;")
    print("Connection from: " + str(address))



    while True:
      data = conn.recv(1024).decode()
      text = 'Recieved'
      datastr=str(data)

      datalist = datastr.split (",")

      if datalist[0]=="Batting" or datalist[0]=="Pitching":
         print('Table and features selected')
         print(datalist)
         conn.send(text.encode())
         cursor.callproc('Data_Mining', datalist)
         
      elif datalist[0]=="Split":
         print('Data Split')
         print(datalist)
         conn.send(text.encode())
         args = (datalist[1],) # 0 is to hold value of the OUT parameter sum
         cursor.callproc('Data_Split', args)
     
      elif datalist[0]=="Train/Test":
         print('Selected Classifier')
         print(datalist)
         traindf = functionToCreateTables("select * from Train;")
         testdf = functionToCreateTables("select * from Test;")
        
         ## format Query Resposes to pandas dataframe
         train = traindf.drop(traindf.columns[[-1,]], axis=1, )
         train = train.drop(traindf.columns[[0,]], axis=1, )
         test = testdf.drop(testdf.columns[[-1,]], axis=1, )
         test = test.drop(testdf.columns[[0,]], axis=1, )
         trainLabName = [traindf.columns[-1]]
         testLabName = [testdf.columns[-1]]
         trainLabel = pd.DataFrame(traindf.values[:, -1], columns=trainLabName)
         testLabel = pd.DataFrame(testdf.values[:, -1], columns=testLabName)
         trainLabel = pd.Series(traindf.values[:, -1])
         testLabel = pd.Series(testdf.values[:, -1])
         trainLabel = trainLabel.values
         testLabel = testLabel.values
         trainLabel=trainLabel.astype('int')
         testLabel=testLabel.astype('int')
         train = train.values
         ###############################################

         if datalist[1]=="DT":
            clf = DecisionTreeClassifier()
         if datalist[1]=="NB":
            clf = GaussianNB()
         # Fit the data into the classifier
         clf = clf.fit(train, trainLabel)
         observed = testLabel.tolist()
         prediction = clf.predict(test).tolist()
         y_true = testLabel
         y_pred = clf.predict(test)
         
      
         acc=str(accuracy_score(observed,y_pred))
         class_report=classification_report(observed,prediction,output_dict=True)
         averagres=class_report['macro avg']
         precision = str(averagres['precision'])
         recall = str(averagres['recall'])
         results= acc+','+ precision+','+recall
         conn.send(results.encode())


      elif str(data)=="exit":
         print("exit")
         exit="exit"
         conn.send(exit.encode())
         break






