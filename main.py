from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# loads BAAI/bge-small-en
# embed_model = HuggingFaceEmbedding()

# loads BAAI/bge-small-en-v1.5
embed_model = HuggingFaceEmbedding(model_name="bge-large-zh-v1.5")
embeddings = embed_model.get_text_embedding("Hello World!")
print(len(embeddings))
print(embeddings[:5])

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
# 加载文档
documents = SimpleDirectoryReader("data").load_data()

# 设置嵌入模型和LLM
Settings.embed_model = embed_model
Settings.llm = Ollama(model="llama2-chinese", request_timeout=300.0)

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 创建问答引擎
query_engine = index.as_query_engine()

# 循环提问
while True:
    # 获取用户输入
    query = input("请输入您的问题（输入'exit'以退出）：")

    # 检查退出条件
    if query.lower() == 'exit':
        break

    # 提问并打印答案
    response = query_engine.query(query)
    print(response)
