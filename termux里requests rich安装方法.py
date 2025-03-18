获取 DeepSeek API Key
访问 DeepSeek 官网 注册并获取 API Key
安装依赖在 Termux 中运行以下命令：
BASH

pkg install python
pip install requests rich


📝 完整代码

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


在 Termux 中安装 requests 库（用于 Python 网络请求），请按照以下步骤操作：

1. 更新 Termux 软件包

首先，确保你的 Termux 软件包是最新的：

pkg update && pkg upgrade

2. 安装 Python（如果尚未安装）

如果你的 Termux 没有 Python，先安装它：

pkg install python

3. 安装 pip（Python 的包管理器）

如果 pip 没有安装，先安装它：

pkg install python-pip

4. 使用 pip 安装 requests 库

运行以下命令安装 requests：

pip install requests

5. 测试安装

安装完成后，你可以运行 Python 并导入 requests 来检查是否安装成功：

python

然后在 Python 交互环境中输入：

import requests
print(requests.__version__)

如果没有报错并输出版本号，说明安装成功！🎉

如果你在安装过程中遇到问题，可以尝试：

pip install --upgrade pip
pip install --upgrade requests

这样可以确保 pip 和 requests 版本是最新的。


pip install requests rich 和 pkg install requests 的主要区别在于安装方式和适用范围：

1. pip install requests rich（使用 Python 的 pip 安装）

pip 是 Python 的包管理工具，它可以安装 Python 生态系统中的库，比如 requests（HTTP 请求库）和 rich（终端美化库）。

适用于 Python 代码运行时使用，安装后的库存放在 Python 的 site-packages 目录中。

示例命令：

pip install requests rich



---

2. pkg install requests（使用 Termux 的软件包管理器安装）

pkg（Termux 的 APT 前端）是用于管理 Termux 的 Linux 软件包的，它安装的是 C 语言或其他底层语言 编写的系统级软件包，而 不是 Python 库。

在 Termux 里，requests 这个包并不是 Python 的 requests，而可能是某个系统工具。

示例命令：

pkg install requests  # 并不会安装 Python 的 requests 库



---

总结

✅ 如果你要在 Python 代码中使用 requests 和 rich，应该使用 pip install requests rich。
⚠ pkg install requests 并不会安装 Python 的 requests 库，而是某个系统级的包。














