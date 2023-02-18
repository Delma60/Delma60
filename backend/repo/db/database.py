import pandas as pd
from os import path
import csv
print("one")
isEixst = path.exists("repo/db/db.csv")

def login_to_db(email, password):
    if isEixst:
        db = pd.read_csv("repo/db/db.csv")
        
        user = db[db["email"] == email] 
        if len(user) == 1:
            return True
        else:
            return False

def create_user_in_db(name=None, email=None, password=None):
    if isEixst:
        # verify

        ver = login_to_db(email, password)
        if ver:
            return {"message": "Email Already Exist", "error_code": 1001}
        else:
            df = pd.read_csv("repo/db/db.csv")
            last_id = df['id'].iloc[-1]
            print(last_id)
            with open("repo/db/db.csv", "a") as f:
                writee= csv.writer(f)
                writee.writerow([int(last_id)+1, name, email, password, False])
                f.close()
            return {"message": "Upload Successful", "error_code": 1000}
    else:
        fieldnames= ["id", "name", "email", "password", "is_active"]
        with open("repo/db/db.csv", "w") as f:
            writee = csv.DictWriter(f, fieldnames)
            writee.writeheader()
            writee.writerows([{'id': '0',"name": name, "email": email, "password": password, "is_active": False }])
        return {"message": "Upload Successful", "error_code": 1000}

