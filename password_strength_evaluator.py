import re
import requests
import json
import csv
from hashlib import sha1

def print_banner():
    banner = """
    ===============================
    Password Strength Evaluator
    By : Python 2.7
    ===============================
    """
    print banner

def evaluate_password_strength(password):
    score = 0
    suggestions = []
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        score += 2
    else:
        suggestions.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 2
    else:
        suggestions.append("Include at least one number.")

    if re.search(r'[@#$%^&+=!?*]', password):
        score += 2
    else:
        suggestions.append("Include at least one special character (@, #, $, %, ^, &, +, =, !, ?).")
    
    if len(set(password)) > len(password) * 0.6:
        score += 1

    if score >= 8:
        strength = "Strong"
    elif score >= 5:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, suggestions

def check_password_breach(password):
    password_hash = sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = password_hash[:5]
    suffix = password_hash[5:]

    url = "https://api.pwnedpasswords.com/range/{}".format(prefix)
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for hash_entry in hashes:
            hash_value, count = hash_entry.split(':')
            if hash_value == suffix:
                return True, int(count)
    return False, 0

def save_evaluation_result(password, strength, suggestions):
    evaluation_data = {
        "password": password,
        "strength": strength,
        "suggestions": suggestions
    }
    try:
        with open('password_evaluations.json', 'a') as file:
            json.dump(evaluation_data, file)
            file.write("\n")
    except Exception as e:
        print "Error saving evaluation:", e

def save_evaluation_to_csv(password, strength, suggestions):
    try:
        with open('password_evaluations.csv', 'a') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Password', 'Strength', 'Suggestions'])
            writer.writerow([password, strength, "; ".join(suggestions)])
    except Exception as e:
        print "Error saving to CSV:", e

def main():
    print_banner()
    
    password = raw_input("Enter a password to evaluate: ")
    strength, suggestions = evaluate_password_strength(password)

    breached, count = check_password_breach(password)
    
    print "\nPassword Strength: {}".format(strength)
    
    if breached:
        print "Warning: This password has been exposed in {} data breaches!".format(count)
    else:
        print "Your password is not found in any known breaches."

    if strength == "Weak":
        print "Suggestions to Improve Your Password:"
        for suggestion in suggestions:
            print "- {}".format(suggestion)
    else:
        print "Your password is strong. Good job!"
    
    save_evaluation_result(password, strength, suggestions)
    save_evaluation_to_csv(password, strength, suggestions)

if __name__ == "__main__":
    main()
