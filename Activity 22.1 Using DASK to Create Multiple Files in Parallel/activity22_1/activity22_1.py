import pandas as pd
from dask import dataframe as dd

#create pandas dataframe
pandas_df = pd.DataFrame({"odd_num":[num for num in range(1,11) if num % 2 != 0],"even_num":[num for num in range(1,11) if num % 2 == 0]})

#set npartition argument
df = dd.from_pandas(pandas_df,npartitions=2)

#Uncomment the line below if you are using Mac
#df.to_csv("./activity22.1/", index=False)

#Uncomment the line below if you are using Windows
df.to_csv("./activity22_1/", index=False)