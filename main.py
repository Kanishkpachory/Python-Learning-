import pandas as pd
import csv
from datetime import datetime
from data_entry import get_category , get_amount , get_date , get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date" , "Amount" , "Category" , "Description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE , index=False)

    @classmethod
    def add_entry(cls , Date , Amount , Category , Description):
        new_entry = {
            "Date" : Date,
            "Amount" : Amount,
            "Category" :Category,
            "Description" : Description
        }
        with open(cls.CSV_FILE ,"a" ,newline="") as csvfile:
            writer = csv.DictWriter(csvfile , fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entery Added Succefully")

    @classmethod
    @classmethod
    def get_transaction(cls, start_date, end_date):
       df = pd.read_csv(cls.CSV_FILE)
       df["Date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT)
       start_date = datetime.strptime(start_date, CSV.FORMAT)
       end_date = datetime.strptime(end_date, CSV.FORMAT)

       mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
       filtered_df = df.loc[mask]

       if filtered_df.empty:
        print("No transaction in the given date range.")
       else:
        print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
        print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}))
        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"] == "Expenses"]["Amount"].sum()  # Corrected here
        print("\nSummary")
        print(f"Total Income : Rs.{total_income:.2f}")
        print(f"Total Expenses : Rs.{total_expense:.2f}")
        print(f"Net Income : Rs.{(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.intialize_csv()
    date = get_date("Enter the date of transaction (dd-mm-yyyy) or 'Press Enter' for today date :",allow_default=True)
    amount = get_amount()
    category = get_category()
    description =get_description()
    CSV.add_entry(date , amount , category , description)

def plot_transaction(df) :
    df.set_index('Date' , inplace = True)
    
    income_df = df[df["Category"] == "Income"].resample("D").sum().reindex(df.index , fill_value = 0)
    expenses_df = df[df["Category"] == "Expenses"].resample("D").sum().reindex(df.index , fill_value = 0)
    
    plt.figure(figsize = (10,5))
    plt.plot(income_df.index , income_df["Amount"] , label = "Income" , color= "g")
    plt.plot(expenses_df.index , expenses_df["Amount"] , label = "Expenses" , color = "r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Overtime")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("1. Add a new Transaction")
        print("2. View trasaction summary within a range .")
        print("3. Exit ")

        choice = input("Enter your Choice(1-3) :")
        
        if choice == "1" :
            add()
        elif choice == "2" :
            start_date = get_date("Enter the starting date (dd-mm-yyyy) : ")
            end_date = get_date("Enter the ending date (dd-mm-yyyy) : ")    
            df = CSV.get_transaction(start_date , end_date)
            if input ("Do you want to see plot(y/n) :").lower() == "y":
                plot_transaction(df)
        elif choice == "3" :
            print("\nExiting...")
            break
        else:
            print("\nInvalid choices . Enter 1,2 or 3 .")

if __name__ == "__main__" :
    main()





# CSV.intialize_csv()
# # CSV.add_entry("20-3-24" , 123 , "savings" , "personal") 
# add()
# CSV.get_transaction("01-01-2023" , "31-12-2024")

