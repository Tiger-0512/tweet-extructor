import pandas as pd


# csvファイル読み込み
df = pd.read_csv('tweets_open.csv')

# 2つ以上の項目が1となっているIndexについて除外
indexNames = df[(df['Pos_Neg'] + df['Pos'] + df['Neg'] + df['Neu'] + df['Unr']) >= 2].index
df.drop(indexNames, inplace=True)
print(df)

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

# csvファイルへ出力
df.to_csv('extracted_data.csv')
