import requests
req_url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI="
config = open("credentials.txt")
credentials = config.read().split()
username = credentials[1].strip()
password = credentials[3].strip()
post_data = {
    "userId": username,
    "password": password,
    "serviceName": "ProntoAuthentication",
    "Submit22": "Login"
}
r = requests.post(req_url, data = post_data)
if "logged" in str(r.content):
    print("Succesfully logged in!")
else:
    print("Something went wrong!")
