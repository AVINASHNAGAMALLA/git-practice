import pandas as pd
class Tables:
    def __init__(self,df,col):
        self.df=df
        self.col=col
        
    def tables(self):
        keys=self.df[self.col].value_counts().keys()
        values=self.df[self.col].value_counts().values
        freq_tbl=pd.DataFrame(zip(keys,values))
        return (keys,values,freq_tbl)
