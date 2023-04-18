# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

%matplotlib inline

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# %%
path='/pythonassignment (1).xlsx'

# %%
df=pd.read_excel(path,sheet_name=['Sheet1','Sheet2'])

# %%
df_sheet1=df['Sheet1']
df_sheet2=df['Sheet2']

# %%
merged_df=pd.merge(df_sheet1,df_sheet2,on='Name')

# %%
merged_df=merged_df[['Name','Team Name','uid','total_statements','total_reasons']]

# %%
merged_df

# %%
grouped=merged_df.groupby('Team Name')

# %%
output1=grouped.mean()

# %%
output1=output1.reset_index()

# %%
output1=output1.rename(columns={'total_statements':'Average Statements','total_reasons':'Average Reasons'})

# %%
output1=output1.sort_values(by=['Average Statements'],ascending= False).reset_index()

# %%
output1=output1.drop(columns=['uid','index'])

# %%
output1

# %%
output2=df_sheet2.sort_values(by=['total_statements','total_reasons'],ascending=False)

# %%
output2=output2.reset_index()

# %%
output2=output2.drop(columns=['index','S No'])

# %%
output2=output2.reset_index()

# %%
output2=output2.rename(columns={'index':'Rank'})

# %%
output2


