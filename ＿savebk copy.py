import os
from gpt_index import GPTSimpleVectorIndex, SimpleWebPageReader,GPTListIndex
from dotenv import load_dotenv
# env_path = os.path.join(os.path.dirname(__file__), '../.env')
# load_dotenv(env_path)
load_dotenv()

MYAPI = os.getenv('MYAPI')
THEURL = os.getenv('THEURL')
# THEURL2 = os.getenv('THEURL2')
# THEURL3 = os.getenv('THEURL3')

print(MYAPI)
print(THEURL)
# print(THEURL2)
# print(THEURL3)

# QUESTION1 = os.getenv('QUESTION1')

 
os.environ["OPENAI_API_KEY"] = MYAPI
 
json_path = "./data/wiki.json"
 
# documents = SimpleWebPageReader(html_to_text=True).load_data([url])
document1 = SimpleWebPageReader(html_to_text=True).load_data([THEURL])
# document2 = SimpleWebPageReader(html_to_text=True).load_data([THEURL2])
# document3 = SimpleWebPageReader(html_to_text=True).load_data([THEURL3])
 
# index = GPTSimpleVectorIndex(documents)
index1 = GPTSimpleVectorIndex(document1)
# index2 = GPTSimpleVectorIndex(document2)
# index3 = GPTSimpleVectorIndex(document3)

# index1.set_text("summary1")
# index2.set_text("summary2")
# index3.set_text("summary3")

# index = GPTListIndex([index1, index2,index3])




index1.save_to_disk(json_path)

# list_index.save_to_disk(json_path)

# response = index1.query("What is coffin finance？")
# print(response)








# インデックスの上に、インデックスを作成　memo
# from gpt_index import GPTSimpleVectorIndex, GPTListIndex

# # index1とindex2の作成
# index1 = GPTSimpleVectorIndex(documents1)
# index2 = GPTSimpleVectorIndex(documents2)

# # index1とindex2の要約の設定
# index1.set_text("summary1")
# index2.set_text("summary2")

# # index1とindex2の上にindex3を作成
# index3 = GPTListIndex([index1, index2])