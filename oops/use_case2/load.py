
import pandas as pd
class load:
    def __init__(self,data):
        self.data=data
    def read_data(self):
        df=pd.read_csv(self.data)
        return df

if __name__=="__main__":
    data=load(r"C:\Users\91880\Downloads\telecom_churn_data.csv").read_data()
    print(data.head())


        