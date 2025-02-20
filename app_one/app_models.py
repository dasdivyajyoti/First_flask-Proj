import csv
import os


CSV_FILE = "data.csv"

class DataModel:

    @staticmethod
    def ensure_csv_exists():

        # This method ensures data.csv file exists and adds required titles columns to the files

        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode ='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["age", "name", "email"]) # define your csv columns

    @staticmethod
    def append_data(data):

        # This method appends data into columns into csv file in correct format

        with open(CSV_FILE, mode = 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item.get("age",""), item.get("name",""), item.get("email","")] for item in data)









