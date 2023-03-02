import os
from gpt_index import GPTSimpleVectorIndex, SimpleWebPageReader,GPTListIndex
from dotenv import load_dotenv
# env_path = os.path.join(os.path.dirname(__file__), '../.env')
# load_dotenv(env_path)
load_dotenv()

MYAPI = os.getenv('MYAPI')
THEURL = os.getenv('THEURL')
THEURL2 = os.getenv('THEURL2')
THEURL3 = os.getenv('THEURL3')

QUESTION1 = os.getenv('QUESTION1')
QUESTION2 = os.getenv('QUESTION2')
QUESTION3 = os.getenv('QUESTION3')

print(MYAPI)
print(THEURL)
print(THEURL2)
print(THEURL3)

# QUESTION1 = os.getenv('QUESTION1')

 
os.environ["OPENAI_API_KEY"] = MYAPI
 
json_path = "./data/wiki.json"
 
# documents = SimpleWebPageReader(html_to_text=True).load_data([url])
document1 = SimpleWebPageReader(html_to_text=True).load_data([THEURL])
document2 = SimpleWebPageReader(html_to_text=True).load_data([THEURL2])
document3 = SimpleWebPageReader(html_to_text=True).load_data([THEURL3])
 
# index = GPTSimpleVectorIndex(documents)
index1 = GPTSimpleVectorIndex(document1)
index2 = GPTSimpleVectorIndex(document2)
index3 = GPTSimpleVectorIndex(document3)

index1.set_text("summary1")
index2.set_text("summary2")
index3.set_text("summary3")

index = GPTListIndex([index1, index2,index3])




# index.save_to_disk(json_path)

# list_index.save_to_disk(json_path)

response1 = index.query(QUESTION1)
response2 = index.query(QUESTION2)
response3 = index.query(QUESTION3)
print(QUESTION1,response1)
print(QUESTION2,response2)
print(QUESTION3,response3)








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