import matplotlib.pyplot as plt
import seaborn as sns

class OutliersDetector:
    def __init__(self, data):
        self.data = data
        
    def detect_outliers(self, column):
        Q1 = self.data[column].quantile(0.25)
        Q3 = self.data[column].quantile(0.75)
        # Calculating the IQR
        IQR = Q3 - Q1
        # Defining the lower and upper bounds for the outliers
        lower_bound = Q1 = 1.5 * IQR
        upper_bound = Q3 = 1.5 * IQR
        # Identifying outliers
        outliers =self.data[(self.data[column] < lower_bound) | (self.data[column] > upper_bound)]
        return outliers
    
class DataVisualisation:
    def __init__(self, data):
        self.data = data
        
    def plot_histogram(self, column, bin=50):
        plt.figure(figsize = (20,15))
        sns.histplot(self.data[column], bins=bin, kde=True)
        plt.title(f'Histogram of {column}')
        plt.show()
            
    def plot_boxplot(self, column):
        plt.figure(figsize = ( 8, 6 ))
        sns.boxplot(x=self.data[column])
        plt.title(f'Boxplot of {column}')
        plt.show()