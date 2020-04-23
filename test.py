import pandas as pd 

import matplotlib
matplotlib.use('Agg')

import warnings
warnings.filterwarnings('ignore')

test_df = pd.read_csv('./PubgData/test_V2.csv')
print(test_df.head(50))