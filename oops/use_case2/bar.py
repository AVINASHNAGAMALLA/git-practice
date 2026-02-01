
import pandas as pd
import matplotlib.pyplot as plt

class Bar:
    def __init__(self,keys,values):

        self.keys=keys
        self.values=values
        

    def bar_chart(self):

        plt.bar(self.keys,self.values)
        plt.savefig('barchart.jpg')