
from sklearn.preprocessing import LabelEncoder
import pandas as pd
class Encode:
    def __init__(self,df):
        self.df=df
        self.le=LabelEncoder()
    def label_encode(self):
        cat=self.df.select_dtypes(include='object')
        for i in cat[1:]:
            self.df[i]=self.le.fit_transform(self.df[i])
            
        return self.df
    
if __name__=="__main__":
    labeled=Encode('Visadataset.csv').label_encode()
    encode_df=pd.DataFrame(labeled)