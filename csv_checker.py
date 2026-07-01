import pandas as pd
def csv_reader(userp):

    df = pd.read_csv('passwords_rank.csv')
    password_column = df['password']

    for found_password in password_column:
        if found_password == userp:
            return 0 ##as weak pass

    return 1
        ##as strong pass
