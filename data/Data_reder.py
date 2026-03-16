import csv

import pytest
# @pytest.mark.parametrize("username,password", get_login_data())     

def get_login_data():
    data = []
    with open("data/login_data.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row["username"], row["password"]))
        return data 
    
