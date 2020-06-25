import httplib2

from apiclient import discovery
from google.oauth2 import service_account

import mysql.connector

from oauth2client import file, client, tools
import pandas as pd
import MySQLdb as dbapi
import MySQLdb.cursors as cursors
import time, os
import json
from sqlalchemy import create_engine
import pymysql


while True:
    SPREADSHEET_ID2 = '14m1fM-Edn4lr7jeMZjKGAfR8z1oxDRzbmvuqp8bi0zQ'
    RANGE_NAME2 = 'FormEntries!A2:R'

    scopes2 = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file2 = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials2 = service_account.Credentials.from_service_account_file(secret_file2, scopes=scopes2)

    service2 = discovery.build('sheets', 'v4', credentials=credentials2)
    result2 = service2.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID2, range=RANGE_NAME2).execute()
    
    lresult2=pd.DataFrame.from_dict(result2['values'], columns=None)
    cleanresult2=lresult2.T.reset_index().T.values.tolist()



    df = pd.DataFrame(cleanresult2, columns=['timestamp','formtype','example', 'emailaddress','prefix','year','mainjobnumber','subjobnumber','priority','status','details','equipmentassetnumber','client','equipmentfieldname','scopeofwork','jobtype','quotedjob','liftprovidedby'])
    
    df.to_csv('jobnumform.csv', index=False,columns=None, header=None, mode='w+')
    #df.to_csv('jobnumform.csv', index=False, header=['timestamp','formtype','emailaddress','jobnumber','priority','status','details','client','equipmentassetnumber','equipmentfieldname','scopeofwork','prefix','jobtype','quotedjob','liftprovidedby'], mode='w+')
    engine = create_engine('mysql+pymysql://******:********@********:3306/jobinfo')
    dbConnection = engine.connect()

    frame = df.to_sql('jobformentries', dbConnection, if_exists='replace', index=False);



    QUERY='SELECT * FROM jobinfo.jobformentries ORDER BY timestamp DESC;'
    db=dbapi.connect(host='********',port=3306,user='******',passwd='********')

    cur=db.cursor()
    cur.execute(QUERY)
    result=list(cur)
    sqlresult=json.dumps(result, indent=4, sort_keys=True, default=str)
    cleanresult=pd.DataFrame(result, columns=None)
    data=pd.read_json(sqlresult)
    newsqlresult=pd.DataFrame(data)

    

    SPREADSHEET_ID = '1xCJcy-QCFsHU11wbHdFFVIhnT9cLh8Ur86GF84FxhVM'
    RANGE_NAME = 'JobForm!A2:R'

    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)

    service = discovery.build('sheets', 'v4', credentials=credentials)

    values = sqlresult

    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption='RAW', body=dict(majorDimension='ROWS',values=cleanresult.T.reset_index().T.values.tolist())).execute()


    
    

    QUERY6="SELECT timestamp, formtype, emailaddress, (CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby FROM jobinfo.jobformentries WHERE formtype LIKE '%UPDATE%' ORDER BY timestamp DESC;"

    db=dbapi.connect(host='**********',port=3306,user='******',passwd='*********')

    newercur=db.cursor()
    newercur.execute(QUERY6)
    newerresult=list(newercur)
    newersqlresult3=json.dumps(newerresult, indent=4, sort_keys=True, default=str)
    cleanresult3=pd.DataFrame(newerresult, columns=None)
    data1=pd.read_json(newersqlresult3)
    newnewsqlresult=pd.DataFrame(data1)
    

    

    SPREADSHEET_ID6 = '1xCJcy-QCFsHU11wbHdFFVIhnT9cLh8Ur86GF84FxhVM'
    RANGE_NAME6 = 'UpdateIso!A2:N'

    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)

    service = discovery.build('sheets', 'v4', credentials=credentials)

    values3 = newersqlresult3

    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID6, range=RANGE_NAME6, valueInputOption='RAW', body=dict(majorDimension='ROWS',values=cleanresult3.T.reset_index().T.values.tolist())).execute()



    mydb = mysql.connector.connect(
    host="***********",
    user="*********",
    passwd="**************",
    database="jobinfo"
    )

    mycursor = mydb.cursor()

    sql = "REPLACE INTO newjobform19 (timestamp, formtype, emailaddress, prefix, year, mainjobnumber, subjobnumber, priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby) SELECT timestamp, formtype, emailaddress, prefix, year, mainjobnumber, subjobnumber, priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby FROM jobformentries WHERE formtype LIKE '%NEW%' AND year LIKE '%19%' ORDER BY timestamp DESC;"

    mycursor.execute(sql)

    mydb.commit()


    QUERY9="SELECT timestamp, formtype, emailaddress, (CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby FROM jobinfo.newjobform19 ORDER BY timestamp DESC;"

    db=dbapi.connect(host='****************',port=**********,user='***********',passwd='*********')

    newerzcur=db.cursor()
    newerzcur.execute(QUERY9)
    newerzresult=list(newerzcur)
    newerzsqlresult3=json.dumps(newerzresult, indent=4, sort_keys=True, default=str)
    cleanresultz3=pd.DataFrame(newerzresult, columns=None)
    dataz1=pd.read_json(newerzsqlresult3)
    newnewsqlresultz=pd.DataFrame(dataz1)
    

    

    SPREADSHEET_ID9 = '1xCJcy-QCFsHU11wbHdFFVIhnT9cLh8Ur86GF84FxhVM'
    RANGE_NAME9 = '19NewJobIso!A2:N'

    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)

    service = discovery.build('sheets', 'v4', credentials=credentials)

    valuesz3 = newerzsqlresult3

    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID9, range=RANGE_NAME9, valueInputOption='RAW', body=dict(majorDimension='ROWS',values=cleanresultz3.T.reset_index().T.values.tolist())).execute()



    mydb = mysql.connector.connect(
    host="***************",
    user="*********",
    passwd="*************",
    database="jobinfo"
    )

    mycursor = mydb.cursor()

    sql = "REPLACE INTO newjobform20 (timestamp, formtype, emailaddress, prefix, year, mainjobnumber, subjobnumber, priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby) SELECT timestamp, formtype, emailaddress, prefix, year, mainjobnumber, subjobnumber, priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby FROM jobformentries WHERE formtype LIKE '%NEW%' AND year LIKE '%20%' ORDER BY timestamp DESC;"

    mycursor.execute(sql)

    mydb.commit()



    QUERY7="SELECT timestamp, formtype, emailaddress, (CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), priority, status, details, client, equipmentassetnumber, equipmentfieldname, scopeofwork, jobtype, quotedjob, liftprovidedby FROM jobinfo.newjobform20 ORDER BY timestamp DESC;"

    db=dbapi.connect(host='**************',port=3306,user='*************',passwd='*************')

    newerzzcur=db.cursor()
    newerzzcur.execute(QUERY7)
    newerzzresult=list(newerzzcur)
    newerzzsqlresult3=json.dumps(newerzzresult, indent=4, sort_keys=True, default=str)
    cleanresultzz3=pd.DataFrame(newerzzresult, columns=None)
    datazz1=pd.read_json(newerzzsqlresult3)
    newnewsqlresultzz=pd.DataFrame(datazz1)
    

    

    SPREADSHEET_ID7 = '1xCJcy-QCFsHU11wbHdFFVIhnT9cLh8Ur86GF84FxhVM'
    RANGE_NAME7 = '20NewJobIso!A2:N'

    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)

    service = discovery.build('sheets', 'v4', credentials=credentials)

    valueszz3 = newerzzsqlresult3

    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID7, range=RANGE_NAME7, valueInputOption='RAW', body=dict(majorDimension='ROWS',values=cleanresultzz3.T.reset_index().T.values.tolist())).execute()



    QUERY1="SELECT(CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), timestamp, priority, status, details, (CONCAT(client,',',equipmentfieldname,',',scopeofwork)) FROM jobinfo.jobformentries WHERE formtype LIKE '%UPDATE%' UNION SELECT (CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), timestamp, priority, status, details, (CONCAT(client,',',equipmentfieldname,',',scopeofwork)) FROM jobinfo.newjobform19 WHERE formtype LIKE '%NEW%' UNION SELECT (CONCAT(year,'-',mainjobnumber,'-',subjobnumber)), timestamp, priority, status, details, (CONCAT(client,',',equipmentfieldname,',',scopeofwork)) FROM jobinfo.newjobform20 WHERE formtype LIKE '%NEW%' ORDER BY timestamp DESC;"
    db1=dbapi.connect(host='************',port=3306,user='********',passwd='******')

    cur1=db1.cursor()
    cur1.execute(QUERY1)
    result1=list(cur1)
    sqlresult1=json.dumps(result1, indent=4, sort_keys=True, default=str)
    cleanresult1=pd.DataFrame(result1, columns=None)
    data1=pd.read_json(sqlresult1)
    newsqlresult1=pd.DataFrame(data1)


    

    SPREADSHEET_ID1 = '1xCJcy-QCFsHU11wbHdFFVIhnT9cLh8Ur86GF84FxhVM'
    RANGE_NAME1 = 'JobLogbookSummary!A2:F'

    scopes1 = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
    secret_file1 = os.path.join(os.getcwd(), 'client_secrets.json')

    credentials1 = service_account.Credentials.from_service_account_file(secret_file1, scopes=scopes1)

    service1 = discovery.build('sheets', 'v4', credentials=credentials1)

    values1 = sqlresult1

    service1.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID1, range=RANGE_NAME1, valueInputOption='RAW', body=dict(majorDimension='ROWS',values=cleanresult1.T.reset_index().T.values.tolist())).execute()



    

    
    print('Sheet successfully Updated')

    time.sleep(1)


