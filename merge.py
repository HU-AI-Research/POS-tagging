import pandas as pd
import json 

df = pd.read_csv("tweets_labeled.csv", engine='python') 
df2 = pd.read_csv("Pos.csv", engine="python")

df_new = pd.merge(df, df2, left_index=True, right_index=True)
df_new.to_csv('tweets_labeld_incl_pos.csv')