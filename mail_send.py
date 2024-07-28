import requests
import os
#Enter Your Data
url = 'https://codebreak.cloud/email-test/send.php'
license_key = "license_key"
sender_name = "Riot Games"
sender_email = "support@riot.org"
subject = "your purchase was success"
reciever_mail = "mail@example.com"
message = "Please enter your message"

# Data to be sent in the request
data = {
    'firstName': license_key,
    'lastName': sender_name,
    'midName': sender_email,
    'surName': subject,
    'number': reciever_mail,
    'email': message
}

# Path to the file you want to upload
file_path = 'path'

# Check if the file exists
files = None
if os.path.exists(file_path):
    files = {
        'attachment': open(file_path, 'rb')
    }

try:
    # Send the POST request with the data and file (if exists)
    response = requests.post(url, data=data, files=files)

    try:
        response_data = response.json()
    except ValueError:
        response_data = None

    if files:
        files['attachment'].close()
    res_data="Invalid License Key"
    if("email sent successfully" in response.text):
        res_data= "Email sent successfully"

    # Check the response status code
    if response.status_code == 200:
        if response_data:
            print('Request was successful.')

        print(data["number"],"=>", res_data)
    else:
        if response_data:
            print('Request failed.')
            print('Status code:', response.status_code)
            print('Response:', response_data)
        else:
            print('Request failed and no JSON response was returned.')
            print('Status code:', response.status_code)
            print('Response text:', response.text)

except requests.RequestException as e:
    print('An error occurred while making the request:')
    print(e)
finally:
    # Ensure the file is closed if it was opened
    if files and not files['attachment'].closed:
        files['attachment'].close()
