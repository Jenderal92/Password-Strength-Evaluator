# Password Strength Evaluator

**Password Strength Evaluator** is a tool to evaluate the strength of passwords and provide recommendations to improve their security. This tool also checks if your password has been exposed in any data breaches using the **Have I Been Pwned** API. Additionally, it stores the evaluation results in **JSON** and **CSV** files for further analysis in the future.

## How to Use

1. **Prepare Python 2.7 Environment**
   - Ensure you have **Python 2.7** installed on your system.
   - You also need to install the **requests** library. You can do so by running:
     ```
     pip install requests
     ```

2. **Clone the Repository**
   - Clone this repository to your local machine using the following command:
     ```
     git clone https://github.com/Jenderal92/Password-Strength-Evaluator.git
     ```

3. **Run the Tool**
   - Navigate to the directory where you cloned the tool and run the script:
     ```
     python password_strength_evaluator.py
     ```

4. **Follow On-Screen Instructions**
   - The program will prompt you to enter a password for evaluation.
   - It will display the strength of the password and offer suggestions to improve it if necessary.
   - The program will also check if your password has been exposed in any breaches.

5. **Evaluation Results**
   - Evaluation results will be saved in two files:
     - **password_evaluations.json** (JSON Format)
     - **password_evaluations.csv** (CSV Format)
   
   You can open these files to analyze your password's evaluation history.

## Tool Features

1. **Password Strength Evaluation**:
   - Evaluates the password based on the following criteria:
     - Password length
     - Use of uppercase letters
     - Use of lowercase letters
     - Use of numbers
     - Use of special characters
     - Character diversity within the password

2. **Data Breach Check**:
   - Checks if your password has been exposed in any breaches using the **Have I Been Pwned** API.
   - Provides a warning if the password has been exposed and shows how many breaches it has been found in.

3. **Result Storage**:
   - Saves evaluation results in **JSON** and **CSV** formats for future analysis.
   - Makes it easier to track the strength of your passwords over time.

4. **Password Improvement Suggestions**:
   - Provides suggestions to improve your password if it is weak or does not meet security standards.

## Example Output

```
===================================================
|        Password Strength Evaluator 2050         |
|             By Future Programmer               |
|     Version 1.0 - Secure Your Digital Life     |
===================================================
Enter a password to evaluate: Password123!
Password Strength: Strong
Your password is not found in any known breaches.
Your password is strong. Good job!

[Saved evaluation to password_evaluations.json and password_evaluations.csv]
```