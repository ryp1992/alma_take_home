# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import conferenceBookingSystem

def read_csv_file(file_path):
    room_booking = conferenceBookingSystem.ConferenceBookingSystem()
    rows = {}
    row_index = 0
    try:
        with open(file_path, 'r', newline='') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                seperate_input = row[0].split(",")
                if (len(seperate_input)) > 2:
                    return
                start = int(seperate_input[0])
                end = int(seperate_input[1])
                print(start, end)
                if start == 0:
                    # special case to remove previous input
                    remove_row = rows.get(end)

                    room_booking.remove_interval(remove_row[0],remove_row[1])
                else:
                    print(room_booking.book(start, end))
                    rows[row_index] = [start, end]
                row_index += 1
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = "takeHomeExamInput - Sheet1.csv"
    read_csv_file(file_path)

