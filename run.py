import os

import 1_dataExtractor
import 2_tweetExtractor
import 3_Modification


# 一時ファイル削除
os.remove('./twitterJSA_data.csv')
os.remove('./extracted_data.csv')
