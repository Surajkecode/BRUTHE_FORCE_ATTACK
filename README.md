# BRUTHE_FORCE_ATTACK
![Screenshot 2024-08-31 193927](https://github.com/user-attachments/assets/cfecacde-a7bd-4219-ae7f-408b440581b8)

![Screenshot 2024-08-31 194031](https://github.com/user-attachments/assets/dbeba9fe-0028-4f89-b4bb-3eedbfa510be)






---

# Brute Force Password Loader

## Description

Brute Force Password Loader is a Tkinter-based application designed to simulate brute force attacks for educational and testing purposes. It provides an easy-to-use interface to attempt login with various passwords from a list against a specified URL and username.

## Features

- **Simple Brute Force Attack**: 
  - Easily configure and start a brute force attack by specifying the target URL, username, and password list.
  - Automatically iterates through a list of passwords to find a valid combination.

- **User-Friendly Interface**: 
  - Professional UI with a customizable background image.
  - Input fields for entering the target URL and username, and selecting a password list file.
  - Real-time updates on the status of the attack and detailed logging of attempts.

- **Large Password List Handling**: 
  - Efficiently processes large password lists by reading from a text file.
  - Supports extensive lists with millions of passwords.

- **Multithreading Support**: 
  - Keeps the user interface responsive during the brute force process using threading.

## How to Run

1. **Prepare Your Environment**:
   - Ensure you have Python and the required packages installed. You can install the necessary packages using pip:
     ```bash
     pip install tkinter pillow requests
     ```

2. **Download or Clone the Repository**:
   - Clone the repository or download the code from GitHub:
     ```bash
     git clone <repository-url>
     ```

3. **Prepare Password List**:
   - Create a text file named `passwords.txt` in the same directory as the script. List each password on a new line.

4. **Update Script with Password File Path**:
   - If your password list file is named differently or located elsewhere, update the path in the `start_brute_force` method of the `BruteForceApp` class.

5. **Run the Application**:
   - Execute the Tkinter application:
     ```bash
     python app.py
     ```
   - The application window will open. Enter the target URL, username, and select the password list file if needed.

6. **Start the Attack**:
   - Click the "Start Brute Force" button to begin the attack. The application will display status updates and log each attempt in the text area.

## Disclaimer

**Important**: This application is intended for educational purposes and for testing in controlled environments only. **Do not use this tool on live or unauthorized websites.** The creator of this application does not condone or support illegal activities. Using this tool on websites without explicit permission is illegal and unethical. **The responsibility for any misuse of this tool lies solely with the user.**

For any questions or further assistance, please contact the repository maintainer.

---

.
