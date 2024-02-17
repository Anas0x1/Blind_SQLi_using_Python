# Blind SQL Injection Exploit Scripts
These Python scripts are implemented to perform Blind SQL Injection attacks on three different PortSwigger Web Security Academy labs. They are designed to replace the functionalities of Burp Intruder and SQLMap for these labs.

# Links
`Conditional Responses Lab` https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

`Conditional Errors Lab` https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

`Time Delays and Information Retrieval Lab` https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

# Script Descriptions
1. conditional_responses_blind_sqli.py
This script exploits the Blind SQL Injection vulnerability present in the "Conditional Responses Lab" by sending crafted requests to the vulnerable application, analyzing the responses, and extracting the administrator password.

2. conditional_errors_blind_sqli.py
This script automates the exploitation of the Blind SQL Injection vulnerability in the "Conditional Errors Lab" by sending payloads to trigger conditional SQL errors, allowing retrieval of data through analyzing the application's responses and retrieving the administrator password.

3. time_delays_and_information_retrieval_blind_sqli.py
This script exploits the Blind SQL Injection vulnerability in the "Time Delays & Information Retrieval Lab" by using time-based techniques to infer information from the database through analyzing the application's response times and retrieving the administrator password.

# Usage:
1. Clone this repository:

   `git clone https://github.com/0x0anas/Blind_SQLi_using_Python.git`

2. Navigate to the cloned directory:

   `cd Blind_SQLi_using_Python`

4. Run the help menu to display how you can use this tool:

    `python3 <script_name>.py -h`

    ![sqli2](https://github.com/0x0anas/Blind_SQLi_using_Python/assets/78263620/a7fdbe1e-deab-44ed-a395-d0b9fb18a74e)


4. If you forgot to add the lab link as an argument after the `-u` option, the tool will remind you:

   `python2 <script_name>.py -u`.

    ![sqli3](https://github.com/0x0anas/Blind_SQLi_using_Python/assets/78263620/af959f2c-4ada-4f93-b4aa-f1ae9aee0efc)

5. Replace <script_name>, and <lab_url> with appropriate values.

6. Run the desired script with Python, providing the URL of the lab as a command-line argument:

   `python3 <script_name>.py -u <lab_url>`

   Then the tool retrieved administrator password

   ![sqli4](https://github.com/0x0anas/Blind_SQLi_using_Python/assets/78263620/41d3b219-42b4-47ce-8227-830d075edb49)


