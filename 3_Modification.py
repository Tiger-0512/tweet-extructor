import pandas as pd
import json


# csvファイル読み込み
df = pd.read_csv('twitterJSA_data.csv')

# tweet内容が取得できなかったものに関して除外
df = df.dropna(how='any')

# indexのリセット
df = df.drop(df.columns[0], axis=1)
df = df.reset_index(drop=True)

# csvファイルへ出力
df.to_csv('final_data.csv')

# dfの行数
print('Dataframe:', len(df.index))

# Pos_Neg=1の行数
indexNum = df[df['Pos_Neg'] == 1].index
print('Pos&Neg:', len(indexNum))

# Pos=1の行数
indexNum = df[df['Pos'] == 1].index
print('Pos:', len(indexNum))

# Neg=1の行数
indexNum = df[df['Neg'] == 1].index
print('Neg:', len(indexNum))

# Neu=1の行数
indexNum = df[df['Neu'] == 1].index
print('Neu:', len(indexNum))

# Unr=1の行数
indexNum = df[df['Unr'] == 1].index
print('Unr:', len(indexNum))
