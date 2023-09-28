import os
import openai
import hashlib
import json

# 指定的助手角色列表
assistant_roles = ["填写你认为聊天记录中，最有含金量的发言人"]

# 文件路径
base_path = "你的微信聊天记录的路径"
files = [base_path + '聊天记录txt文件名']
output_path = base_path + 'finetune_ready.jsonl'

# 初始化数据集列表
dataset = []

MAX_MESSAGES_PER_DIALOGUE = 2048  # 每个对话的最大消息数

# 处理每个文件
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        messages = []
        for line in f:
            parts = line.split('):')
            if len(parts) < 2:
                continue  # 跳过格式不正确的行
            
            role_and_time = parts[0].split(' (')
            role = role_and_time[0] if len(role_and_time) > 1 else 'unknown'
            
            # 检查角色是否是指定的助手角色
            adjusted_role = 'assistant' if role in assistant_roles else 'user' if role != 'system' else 'system'
            
            content = '):'.join(parts[1:]).strip()
            
            # 使用哈希处理名称
            name = hashlib.md5(role.encode('utf-8')).hexdigest()
            
            # 如果消息超过了限制，创建新的对话实例
            if len(messages) >= MAX_MESSAGES_PER_DIALOGUE:
                dataset.append({'messages': messages})
                messages = []
            
            messages.append({'role': adjusted_role, 'content': content, 'name': name})
        
        if messages:
            dataset.append({'messages': messages})

# 将数据集写入jsonl文件
with open(output_path, 'w', encoding='utf-8') as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

# 确保您的API密钥已经设置
assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY must be set"
openai.api_key = os.getenv("OPENAI_API_KEY")

# 请确认您的文件路径是否正确
file_path = "Z:\\aoligei\\finetune_ready.jsonl"

with open(file_path, "rb") as file:
    response = openai.File.create(
        file=file,
        purpose='fine-tune'
    )

print(f"{file_path} has been uploaded successfully!")
print(f"The file ID is: {response.id}")
