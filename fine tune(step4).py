import openai
# 设置您的API密钥
openai.api_key = '你的gpt api'

# 根据您提供的指南创建一个fine-tuning job
try:
    response = openai.FineTuningJob.create(
        training_file="你训练的模型文件id",  # 请替换为您的文件ID
        model="gpt-3.5-turbo"  # 您可以选择其他的模型，如果有的话
    )
    
    # 打印响应，这里可能会包含有关fine-tuning job的有用信息
    print(response)
except openai.error.OpenAIError as e:
    print(f"Error: {e}")


import openai

# 设置API密钥
openai.api_key = 'gpt api'  # 请使用您自己的API密钥

# 检查fine-tuning job的状态
try:
    response = openai.FineTuningJob.retrieve("ftjob-J6QTl1cGO45EI3WWn8OxPZLf")  # 使用您的job ID
    print(response)
except openai.error.OpenAIError as e:
    print(f"Error: {e}")
