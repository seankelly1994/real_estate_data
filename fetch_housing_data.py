import os
import pandas as pd
import matplotlib.pyplot as plt

class Housing_data():
    def load_housing_data():

        csv = os.chdir('datasets/housing/')

        data_frame = pd.read_csv("housing.csv")

        return data_frame

    def plot_house_data(self):
        house_data = Housing_data

        housing = house_data.load_housing_data()

        housing.hist(bins=50, figsize=(20, 15))
        plt.show()

def main():
    house_data = Housing_data()

    # housing = house_data.load_housing_data()
    house_data.plot_house_data()

# Call
if __name__ == '__main__':
    main()