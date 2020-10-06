import itertools
import pickle
import json
from time import sleep
import get_tweets
import argparse
import csv
import pandas as pd


def extract():
    anno = [list(line.strip().split(',')) for line in open(args.csvPath)]
    # anno = [list(map(int, line.strip().split(','))) for line in open(args.csvPath)]
    for i in range(1, len(anno)):
        anno[i] = list(map(int, anno[i]))
    anno = anno[1:]

    alldata = []

    df = pd.DataFrame({'TweetId': [],
                    'GenreId': [],
                    'StatusId': [],
                    'Pos_Neg': [],
                    'Pos': [],
                    'Neg': [],
                    'Neu': [],
                    'Unr': [],
                    'Text': []},
                    index=[])

    for i,batch in enumerate(itertools.zip_longest(*[iter(anno)]*100)):
        print('%d/%d'%(i+1,len(anno)//100))
        batch = [b for b in batch if b is not None]
        tweets = getTweets([line[3] for line in batch])  # 100ツイートを一度に取得

        for line in batch:
            df.loc[line[0]] = [line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], tweets[line[3]] if line[3] in tweets else '']
            print(df)

            '''
            # json, pickleでデータを取得したい場合、コメントアウトを外す
            data = {'id':line[1],
                    'topic':line[2],
                    'status':line[3],
                    'label':line[4:],
                    'text':tweets[line[3]] if line[3] in tweets else ''
                    # 'text':getTweets(line[3])
            }
            alldata.append(data)
            '''

        # 出力できているかの確認
        # print(df.tail())
        # sleep
        sleep(1)
    df.to_csv('twitterJSA_data.csv')

    '''
    # json, pickleでデータを取得したい場合、コメントアウトを外す
    pickle.dump(alldata, open('twitterJSA_data.pickle','wb'))
    json.dump(alldata, open('twitterJSA_data.json','w'))
    '''


parser = argparse.ArgumentParser()
parser.add_argument('-cp','--csvPath',type=str,default='extracted_data.csv',
                    help='path to extracted_data.csv')
args = parser.parse_args()

getTweets = get_tweets.getTweets
extract()