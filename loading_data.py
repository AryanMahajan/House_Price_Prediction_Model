from path import CLEANED_TEST_PATH, CLEANED_TRAIN_PATH
import csv
import pickle


def create_train_data():
    #Loads, processes, and pickles training data into lists of lists of integers.

    area, bathrooms, bedrooms, sales_price = [], [], [], []
    with open(CLEANED_TRAIN_PATH, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        next(rows)  # Skip the header row
        for row in rows:
            area.append(int(row[1]))
            bathrooms.append(int(row[2]))
            bedrooms.append(int(row[3]))
            sales_price.append(int(row[4]))

    x_train = [[a, b, c] for a, b, c in zip(area, bathrooms, bedrooms)]
    y_train = sales_price

    pickle_x_train_out = open("X_train.pickle", "wb")
    pickle.dump(x_train, pickle_x_train_out)
    pickle_x_train_out.close()

    pickle_y_train_out = open("y_train.pickle", "wb")
    pickle.dump(y_train, pickle_y_train_out)
    pickle_y_train_out.close()


def create_test_data():
    #Loads, processes, and pickles test data into lists of lists of integers.

    area, bathrooms, bedrooms, sales_price = [], [], [], []
    with open(CLEANED_TEST_PATH, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        next(rows)  # Skip the header row
        for row in rows:
            area.append(int(row[1]))
            bathrooms.append(int(row[2]))
            bedrooms.append(int(row[3]))
            sales_price.append(int(row[4]))

    x_test = [[a, b, c] for a, b, c in zip(area, bathrooms, bedrooms)]
    y_test = sales_price

    pickle_x_test_out = open("X_test.pickle", "wb")
    pickle.dump(x_test, pickle_x_test_out)
    pickle_x_test_out.close()

    pickle_y_test_out = open("y_test.pickle", "wb")
    pickle.dump(y_test, pickle_y_test_out)  # Ensure integer conversion
    pickle_y_test_out.close()


