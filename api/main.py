import imaplib
import email
#from send_to_telegram import send_to_telegram


#importing flask
from flask import Flask, jsonify

import requests

def send_to_telegram(message):

    apiToken = '6600888786:AAGdS1rQOnFDNzmxEzA3SbjwMZ-DpanIzsg'
    chatID = '2143276019'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response.ok)
        return(response.ok)
    except Exception as e:
        #print(e)
        return e
    

app = Flask(__name__)

#defining flask app here.
@app.route('/')
def mailReader():

    chat_id = '2143276019'
    token = '6600888786:AAGdS1rQOnFDNzmxEzA3SbjwMZ-DpanIzsg'

    #status of message sent to telegram list
    statusofmsg = []

    #output_dir = '/tmp'
    imap_server = "qasid.iitk.ac.in"
    email_address = "kcsadhan23"
    password = "cLcTcY@6156"

    imap = imaplib.IMAP4_SSL(imap_server)#encrypted connection

    #logging into the account
    try:
        imap.login(email_address, password)
    except:
        print("unable to login")
        return jsonify({"status": "unable to login!"})
        exit()

    #selecting the inbox with readonly
    imap.select("Inbox")


    status, msgnums = imap.search(None, "UNSEEN")

    #print(status)
    #print(msgnums)

    #for reading 2 emails
    #count = 0

    for msgnum in msgnums[0].split():

        #for reading 3 emails
        #count += 1

        msg_string = ''
        typ,data = imap.fetch(msgnum,"(RFC822)")
        message = email.message_from_bytes(data[0][1])

        msg_string += f"Date: {message.get('Date')}\n"
        msg_string += f"From:{message.get('From')}\n"
        #msg_string += f"BCC:{message.get('BCC')}\n"
        msg_string += f"Subject: {message.get('Subject')} \n"
        msg_string += "Content: \n"



        '''print(f"Message Number: {msgnum}\n")
        print(f"To: {message.get('To')}\n")
        print(f"BCC: {message.get('BCC')}\n")
        print(f"Date: {message.get('Date')}\n")
        print(f"Subject: {message.get('Subject')}\n")

        print("Content:\n")

        '''
        for part in message.walk():
            #print(part.get_content_type())
            if (part.get_content_type() == "text/plain")  :
                
                msg_string += str(part.as_string())
        
        #print block for testing (will be commented in the original code.)
        '''print(len(msg_string))
        print('\n')
        print('\n')
        print(msg_string)
        print('\n')
        print('\n')'''

        
        statusofmsg.append(send_to_telegram(msg_string))

        #to limit number of messages to be written.
        #if (count == 2):
        #    break

    imap.close()
    imap.logout()

    return jsonify({'status':statusofmsg})

if __name__ == '__main__':
    app.run()




     