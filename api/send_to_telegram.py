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

#send_to_telegram("<b>bold</b>")