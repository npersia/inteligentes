
import warnings
warnings.filterwarnings('ignore')
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


data = pd.read_csv("data2.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
#data = data.drop(13505)


#data = data.drop(['Unnamed: 80','Unnamed: 81','Unnamed: 82','Unnamed: 83'],axis=1)

data = data.drop(['major'],axis=1)


data = data.drop(['country'],axis=1)

feature = data.drop('nerdy',axis=1)
label = data['nerdy']


import warnings
warnings.filterwarnings('ignore')
data.loc[[13510]]

data['race'] = \
       np.where(data['race_other'] == '1', 'race_other',
       np.where(data['race_nativeau'] == '1', 'race_nativeau',
       np.where(data['race_nativeam'] == '1', 'race_nativeam',
       np.where(data['race_hispanic'] == '1', 'race_hispanic',
       np.where(data['race_white'] == '1', 'race_white',
       np.where(data['race_black'] == '1', 'race_black',
       np.where(data['race_asian'] == '1', 'race_asian',
       np.where(data['race_arab'] == '1', 'race_arab', '0')
                     )
                     )
                     )
                     )
                     )
                     )
                     )


data.drop('race_other', axis=1, inplace=True)
data.drop('race_nativeau', axis=1, inplace=True)
data.drop('race_nativeam', axis=1, inplace=True)
data.drop('race_hispanic', axis=1, inplace=True)
data.drop('race_white', axis=1, inplace=True)
data.drop('race_black', axis=1, inplace=True)
data.drop('race_asian', axis=1, inplace=True)
data.drop('race_arab', axis=1, inplace=True)



data.to_csv('processed_data2.csv', index=False)