import sys

import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

class CurvesDataManager:

    def __init__(self, input_folder_path,file_names, sheet_names):

        self.input_folder_path = input_folder_path
        self.file_names = file_names
        self.sheet_names = sheet_names

        self.curve_data = {}

    def load_curve_data(self):

        for file in self.file_names:
            for sheet in self.sheet_names:

                df = pd.read_excel(self.input_folder_path + file, sheet_name = sheet)

                df = df.round(2)
                row_count = df.shape[0]

                column_names_df = df.iloc[2].astype(str)
                column_names_list = column_names_df.values.tolist()
                column_names_list[0] = "date"

                df = df.iloc[4:row_count]

                df.columns = column_names_list
                df["date"] = pd.to_datetime(df["date"])

                column_names_list.pop(0)
                df = df.dropna(subset=column_names_list, how="all", inplace=False)

                self.curve_data[file + " " + sheet] = df


    def visualize_term_structure_all(self, df, dataset_name):

        fig = plt.subplots(figsize=(16, 10))

        # Adding a plot title and customizing its font size
        plt.title('Term Structure - ' + ' ' + dataset_name, fontsize=10)

        # Adding axis labels and customizing their font size
        plt.xlabel('Date', fontsize=10)
        plt.ylabel('Rate %', fontsize=10)

        plt.xlim(df["date"].min(), df["date"].max())
        # Defining and displaying all time axis ticks
        ticks = list(df["date"])
        plt.xticks(ticks, rotation=45)

        column_names_list = list(df.columns)
        column_names_list.pop(0)

        for col in column_names_list:
            plt.plot(df["date"], df[col])
        plt.show()

    def visualize_yield_curve_all(self, df, dataset_name):

        df['date'] = df['date'].astype(str)

        column_names_list = df['date'].tolist()
        column_names_list.insert(0, 'tenor')

        df = df.T
        df = df.reset_index().rename(columns={"index": "tenor"})

        row_count = df.shape[0]
        df = df.iloc[1:row_count]

        df.columns = column_names_list

        df["tenor"] = df["tenor"].astype(float)

        fig = plt.subplots(figsize=(16, 10))

        # Adding a plot title and customizing its font size
        plt.title('Yield/Rate Curve - ' + ' ' + dataset_name, fontsize=10)

        # Adding axis labels and customizing their font size
        plt.xlabel('Tenor', fontsize=10)
        plt.ylabel('Rate %', fontsize=10)

        ticks = list(df["tenor"])
        plt.xticks(ticks, rotation=45)

        column_names_list = list(df.columns)
        column_names_list.pop(0)

        for col in column_names_list:
            plt.plot(df["tenor"], df[col])
        plt.show()



if __name__ == '__main__':

    input_folder_path = 'E:\\pyprojects\\curves\\curves\\sample-data\\'

    file_names = ['GLC Nominal daily data current month.xlsx',
                  'GLC Inflation daily data current month.xlsx',
                  'GLC Real daily data current month.xlsx',
                  'OIS daily data current month.xlsx']

    sheet_names = ['1. fwds, short end', '2. fwd curve', '3. spot, short end', '4. spot curve']

    dm = CurvesDataManager(input_folder_path, file_names, sheet_names)

    dm.load_curve_data()

    print(dm.curve_data['GLC Nominal daily data current month.xlsx' + " " + '1. fwds, short end'])

    dataset_name = 'GLC Nominal daily data current month.xlsx' + " " + '1. fwds, short end'

    dm.visualize_term_structure_all(dm.curve_data[dataset_name], dataset_name)
    dm.visualize_yield_curve_all(dm.curve_data[dataset_name], dataset_name)