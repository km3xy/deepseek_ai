

使用termux安装依赖

pkg install python
pip install requests rich






# 📂 文件名：deepseek_chat.py
import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# 🌟 初始化
console = Console()
API_KEY = "你的 DeepSeek API Key"
API_URL = "https://api.deepseek.com/v1/chat/completions"
CHAT_HISTORY = []

# 🎨 小红书风格标题
console.print(Panel.fit("🤖 DeepSeek 智能聊天工具", style="bold blue"))
console.print("✨ 输入 '退出' 结束对话\n")

# 🚀 调用 DeepSeek API
def call_deepseek(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": CHAT_HISTORY + [{"role": "user", "content": message}],
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ 错误：{response.status_code} - {response.text}"

# 🎮 主循环
while True:
    # 用户输入
    user_input = console.input("[bold green]👤 你：[/] ")
    if user_input.lower() in ["退出", "exit"]:
        break

    # 调用 API
    console.print("\n🔄 正在生成回复...\n")
    reply = call_deepseek(user_input)

    # 保存聊天记录
    CHAT_HISTORY.append({"role": "user", "content": user_input})
    CHAT_HISTORY.append({"role": "assistant", "content": reply})

    # 小红书风格输出
    console.print(Panel.fit(
        Markdown(f"🤖 AI：\n{reply}"),
        style="bold cyan"
    ))
    console.print("\n---\n")

# 🎉 结束
console.print(Panel.fit("🎉 对话已结束，欢迎下次使用！", style="bold yellow"))
