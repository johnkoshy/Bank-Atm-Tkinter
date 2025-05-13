Bank ATM Tkinter
A simple Bank ATM simulation built with Python and Tkinter, using MySQL for data storage.
Prerequisites

Python: Version 3.13 or later (python --version).
MySQL: MySQL Community Server installed (download here).
Git: To clone the repository (download here).
A code editor like PyCharm or VS Code (optional but recommended).

Setup Instructions

Clone the Repository:
git clone https://github.com/johnkoshy/Bank-Atm-Tkinter.git
cd Bank-Atm-Tkinter


Install Dependencies:Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

This installs mysql-connector-python for database connectivity.

Set Up MySQL Database:

Install and start MySQL Server.
Log into MySQL:mysql -u root -p


Create a database for the ATM:CREATE DATABASE bank_atm;


(Optional) Create tables as required by main.py. Example table structure:USE bank_atm;
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) UNIQUE,
    pin VARCHAR(4),
    balance DECIMAL(10,2),
    user_name VARCHAR(100)
);
INSERT INTO accounts (account_number, pin, balance, user_name)
VALUES ('1234567890', '1234', 1000.00, 'John Koshy');


Update the database credentials in src/main.py (e.g., host, user, password, database name). Example:db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bank_atm"
)




Verify Project Files:

Ensure main.py and sbi.ico are in the src folder.
The sbi.ico file is used as the window icon. main.py references it with a relative path:window.iconbitmap('sbi.ico')

No path changes are needed if both files are in src.


Run the Application:

Using a terminal:cd src
python main.py


Using PyCharm:
Open the project in PyCharm (File > Open > C:\Users\koshy\vscode_projs\Bank-Atm-Tkinter).
Right-click src/main.py and select Run 'main'.





Project Structure
Bank-Atm-Tkinter/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── src/
│   ├── main.py          # Main application script
│   └── sbi.ico          # Icon file for the Tkinter window

Troubleshooting

MySQL Errors: Ensure MySQL is running and credentials in main.py are correct. Check the database and table exist.
Icon Errors: Verify sbi.ico is in the src folder. If you get a TclError, ensure the file is a valid .ico format.
Module Errors: Run pip install -r requirements.txt to install missing packages.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. For issues, open a ticket on GitHub.
