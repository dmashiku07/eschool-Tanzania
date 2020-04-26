# python logic that is reponsible for all the learning resources including teacher assignment giving, textbook resources, online educational resources, and class submission

import serial # module to get information from the serial port
import mysql.connector # module to connect to the resource database
import datetime
import time
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import wikipedia # module to get infomration from the wikipedia plateform
now = datetime.datetime.now()
dateTime = now.strftime("%Y-%m-%d %H:%M:%S")


jibu = 'j'
registration4Text = "DARASA LA 4 REGISTRATION: ACCEPTED :"
registration5Text = "DARASA LA 5 REGISTRATION: ACCEPTED :"
registration7Text = "DARASA LA 7 REGISTRATION: ACCEPTED :"
geoInfo = "GEOGRAPHY:"
microcontroller_1 = serial.Serial('COM5', baudrate=57600, timeout=1)
microcontroller_2  = serial.Serial('COM6', baudrate=57600, timeout=1)


while True:
    mcu1Data = microcontroller_1.readline().decode('ascii')  # variable to store line read from the microcontroller data


    def spanishTranslator(): # translation function for spanish text
        authenticator = IAMAuthenticator('HfRcwyvVfunmczz2uSVhaagQqU43saBw_cX2CuH3--Ae')
        language_translator = LanguageTranslatorV3(version='2020-01-16', authenticator=authenticator)
        language_translator.set_service_url(
            'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a3a444fb-86ab-427b-a152-12e10e45a2d7')
        translation = language_translator.translate(text=interSpan1, model_id='es-en').get_result()
        print(translation)
        reply = jibu + ',' + studentNumber + ',' + studentName4 + ':' + translation
        registrationReply = bytes(reply, 'ascii')
        microcontroller_2.write(registrationReply)

    def spanishLanguageTranslator(): # translation function for incoming english language to spanish
        authenticator = IAMAuthenticator('HfRcwyvVfunmczz2uSVhaagQqU43saBw_cX2CuH3--Ae')
        language_translator = LanguageTranslatorV3(version='2020-01-16', authenticator=authenticator)
        language_translator.set_service_url(
            'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a3a444fb-86ab-427b-a152-12e10e45a2d7')
        translation = language_translator.translate(text=translationText, model_id='en-es').get_result()
        print(translation)
        reply = jibu + ',' + studentNumber + ',' + studentNumber + ':' + translation
        registrationReply = bytes(reply, 'ascii')
        microcontroller_2.write(registrationReply)



    def class4registration(): # function to place the registration information for grade 4 students into student database
        conn = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        mycursor = conn.cursor()
        mycursor.execute(
                """INSERT INTO darasala4 VALUES('' ,'{}', '{}' , '{}')""".format((str(studentNumber)),str(studentName4), str(dateTime)))
        conn.commit()
        mycursor.execute("SELECT * FROM darasala4")
        print(mycursor.fetchall())
    def replyRegistration4Confirmation(): #function to send back a reply confirmation with the name to the student
        reply = jibu + ',' + studentNumber + ',' + studentName4 + ':' +registration4Text
        registrationReply = bytes(reply, 'ascii')
        microcontroller_2.write(registrationReply)

    def sqlRegistrationDarasaLa5():  # function to place the registration information for grade 5 students into student database
        conn = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        mycursor = conn.cursor()
        mycursor.execute(
            """INSERT INTO darasala5 VALUES('' ,'{}', '{}' , '{}')""".format(str(studentNumber), str(studentName5), str(dateTime)))
        conn.commit()
        mycursor.execute("SELECT * FROM darasala5")
        print(mycursor.fetchall())

    def replyRegistration5Confirmation(): #function to send back a registration reply confirmation for class 5 students with the name to the student
        reply = jibu + ',' + studentNumber + ',' + studentName5 + ':' +registration5Text
        registrationReply = bytes(reply, 'ascii')
        microcontroller_2.write(registrationReply)

    def submission4Confirmation(): # function to send back a submission confirmation to student that submitted in class 4 database
        confirmationText = "ASSIGNMENT SUBMISSION: ACCEPTED"
        reply = jibu + ',' + studentNumber + ',' + studentNumber + ':' + confirmationText
        confirmationReply = bytes(reply, 'ascii')
        microcontroller_2.write(confirmationReply)

    def sqlRegistrationDarasaLa7():  # function to place the registration information for grade 7 students into student database
        conn = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        mycursor = conn.cursor()
        mycursor.execute(
            """INSERT INTO darasala7 VALUES('' ,'{}', '{}' , '{}')""".format(str(studentNumber), str(studentName7), str(dateTime)))
        conn.commit()
        mycursor.execute("SELECT * FROM darasala7")
        print(mycursor.fetchall())
    def replyRegistration7Confirmation(): #function to send back a reply confirmation with the name to the student
        reply = jibu + ',' + studentNumber + ',' + studentName7 + ':' +registration7Text
        registrationReply = bytes(reply, 'ascii')
        microcontroller_2.write(registrationReply)
    def wiki():
        summary = wikipedia.summary(searchT)
        print(summary)

    if mcu1Data[0:1] == '+': # code to get numbers from students
        studentNumber = str(mcu1Data)
        print(mcu1Data)
    if mcu1Data[10:11].upper() == '4': # darasa na 4 regiration
        studentName4 = mcu1Data[13:]
        class4registration()
        replyRegistration4Confirmation()
    if mcu1Data[10:11].upper() == '5': # darasa la 5 registration
        studentName5 = mcu1Data[13:]
        sqlRegistrationDarasaLa5()
        replyRegistration5Confirmation()
    if mcu1Data[10:11].upper() == '7': # darasa la 7 registration
        studentName7 = mcu1Data[13:]
        sqlRegistrationDarasaLa7()
        replyRegistration7Confirmation()
    if mcu1Data[5:6] == '5': # text string designation to pull information from darasala5_spanish eschool database table
        print("Spanish Inquisition")
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        sql_select_Query = "SELECT spanish FROM darasala5_spanish"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        spanishText = str(cursor.fetchall())
        interSpan1 = spanishText[2:160]
        print(interSpan1)
        spanishTranslator()
    if mcu1Data[0:3].upper() == "TES": #translate english to spanish
        print("English to Spanish Translation")
        translationText = mcu1Data[5:]
        print(translationText)
        spanishLanguageTranslator()
    if mcu1Data[0:1].upper() == 'T': # online wikipedia resource
        print("Wiki Module")
        searchT = mcu1Data[3:]
        wiki()


    if mcu1Data[7:8].upper() == '4': # teachers to send homework to darasa 4
        print("4th Grade Assingment")
        assignmentString = mcu1Data[10:]
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')

        sql_select_Query = "SELECT number FROM darasala4"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        userNum = cursor.fetchall()
        for N in userNum:
            numberS = str(*N)
            print(numberS)
            replyS = jibu + ',' + numberS + ',' + assignmentString
            print(replyS)
            replyData = bytes(replyS, 'ascii')
            microcontroller_2.write(replyData)
            time.sleep(2)
    if mcu1Data[7:8].upper() == '5': # teachers to send homework to darasa 5
        print("5th Grade Assingment")
        assignmentString = mcu1Data[10:]
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')

        sql_select_Query = "SELECT number FROM darasala5"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        userNum = cursor.fetchall()
        for N in userNum:
            numberS = str(*N)
            print(numberS)
            replyS = jibu + ',' + numberS + ',' + assignmentString
            print(replyS)
            replyData = bytes(replyS, 'ascii')
            microcontroller_2.write(replyData)
            time.sleep(2)
    if mcu1Data[7:8].upper() == '7': # teachers send homework to darasa 7
        print("7th Grade Assingment")
        assignmentString = mcu1Data[10:]
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        sql_select_Query = "SELECT number FROM darasala7"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        userNum = cursor.fetchall()
        for N in userNum:
            numberS = str(*N)
            print(numberS)
            replyS = jibu + ',' + numberS + ',' + assignmentString
            print(replyS)
            replyData = bytes(replyS, 'ascii')
            microcontroller_2.write(replyData)
            time.sleep(2)

    if mcu1Data[4:5] == '1': # text to get geography information geo 1 textbook information
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        sql_select_Query = "SELECT geography FROM darasala4_subjects"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        assingmentText = str(cursor.fetchall())
        #print(assingmentText) #print fill text content from the SQL database
        geoInformation = assingmentText[337:421]
        print("Restructured:" + geoInformation)
        assnGeo = jibu + ',' + studentNumber + ' ' + geoInfo + ':' + geoInformation
        assnGeoreply = bytes(assnGeo, 'ascii')
        microcontroller_2.write(assnGeoreply)
    if mcu1Data[4:5] == '4': # text to get world history information wor 4
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        sql_select_Query = "SELECT world_history FROM darasala4_subjects"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        assingmentText = str(cursor.fetchall())
        print(len(assingmentText))
        print(assingmentText)
    if mcu1Data[4:5] == '3': # text to get english information eng 3
        connection = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        sql_select_Query = "SELECT english_languaged FROM darasala4_subjects"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        assingmentText = str(cursor.fetchall())
        print(len(assingmentText))
        print(assingmentText)
    if mcu1Data[2:3] == '4': # darasa la 4 submission SB4
        darasa4Assn = mcu1Data[4:]
        print(darasa4Assn)
        print("Darasa La 4 submission")
        conn = mysql.connector.connect(host='127.0.0.1', database='eschool', user='root', password='reactor07')
        mycursor = conn.cursor()
        mycursor.execute(
            """INSERT INTO darasala4_assignments VALUES('' ,'{}', '{}' , '{}')""".format((str(studentNumber)), str(darasa4Assn),
                                                                             str(dateTime)))
        conn.commit()
        mycursor.execute("SELECT * FROM darasala4_assignments")
        print(mycursor.fetchall())
        submission4Confirmation()

