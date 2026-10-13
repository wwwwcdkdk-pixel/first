from dotenv import load_dotenv
import os

# 读取当前目录下的 .env 文件
load_dotenv()

# 从环境变量读取 TEST_NAME
key = os.getenv("OPENAI_API_KEY")

print(key)