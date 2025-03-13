termux创建文件夹

1. 创建目标目录首先，确保你在内置存储中创建了一个新的目录：





mkdir -p /storage/emulated/0/termux_files


2. 复制文件到新目录将现有的 Termux 目录内容复制到新的目录中：

cp -r /data/data/com.termux/files/home/* /storage/emulated/0/termux_files/


cp -r /data/data/com.termux/files/home/* /storage/emulated/0/termux_files/



要进入 /storage/emulated/0/termux_files 目录，你可以使用 cd 命令。以下是具体步骤：1. 使用 cd 命令进入目录在 Termux 中输入以下命令：cd /storage/emulated/0/termux_files

2. 验证当前目录使用 
pwd 命令验证你是否已经进
入正确的目录：

pwd你应该会看到输出
/storage/emulated/0/termux_files

3. 列出目录内容使用 
ls 命令
列出目录中的文件和文件夹：
4. 创建并运行 Python 文件在 
/storage/emulated/0/termux_files 目录中创建并运行一个简单的 Python 文件：

用mt创建 hello.py文件

复制代码：print("你好")
粘贴到hello.py文件里

保存并退出 ，然后直接运行 Python 文件：
首先进入termux创建目标目录

cd /storage/emulated/0/termux_files2

输入python命令
python hello.py


你应该会看到输出：你好，
  
  这样，你就成功进入了 /storage/emulated/0/termux_files 目录，
  
  并创建和运行了一个简单的 Python 脚本。



 github      open ai  代码库里有  完整的termux教程


必须先开启文件访问权限


termux-setup-storage
  

手动开启 Android 权限

如果  termux-setup-storage  未触发权限弹窗，可手动开启：

进入 Android 设置：

打开手机 设置 → 应用管理 → Termux。
开启存储权限：

找到 权限（Permissions） → 开启 存储（Storage） 或 文件和媒体（Files & Media）。








  
