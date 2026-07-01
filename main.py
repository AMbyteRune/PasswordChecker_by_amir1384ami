import pandas as pd
import is_weak
import csv_checker

while True:
    userp = input("enter your password: ")

    if userp == "":
        print("please enter your password")
    elif len(userp) < 8:
        print("password is too short")
    elif csv_checker.csv_reader(userp) == 0:
        print("your password is in common weak passwords list")
    elif is_weak.is_weak(userp):
        print("your password has weak pattern")
    else:
        print("password is strong enough")
        break


