下面是一个详细指南，介绍如何在 Termux 中使用 Lighttpd 快速搭建轻量级 Web 服务器，并将工作目录修改到外部存储路径下：


---

1. 安装 Termux 与 Lighttpd

1. 安装 Termux
从 Google Play 或 F-Droid 安装 Termux。


2. 初始化存储权限
为了访问外部存储，执行：

termux-setup-storage


termux-setup-storage

termux-setup-storage






这会要求授权，允许 Termux 访问手机存储。


3. 安装 Lighttpd
在 Termux 中更新软件包并安装 lighttpd：

pkg update && pkg upgrade


pkg install lighttpd




---

2. 修改工作目录

1. 创建新目录
为了将 Web 服务目录指向外部存储，先创建目录：

mkdir -p /storage/emulated/0/termux_files


2. 复制 Termux 目录内容
将现有的 Termux 目录内容复制到新目录中：

cp -r /data/data/com.termux/files/home/* /storage/emulated/0/termux_files/

这样你可以将静态页面、网站文件等内容放入外部存储路径下，便于管理和备份。




---

3. 配置 Lighttpd

1. 修改配置文件
编辑 Lighttpd 的配置文件（路径通常为 /data/data/com.termux/files/usr/etc/lighttpd/lighttpd.conf）：

vim /data/data/com.termux/files/usr/etc/lighttpd/lighttpd.conf

找到或添加如下行，修改 server.document-root 指向新目录：

server.document-root = "/storage/emulated/0/termux_files"


2. 其他配置（可选）
根据需要调整端口、日志等配置参数。例如，设置监听端口为 8080：

server.port = 8080




---

4. 启动 Lighttpd

1. 启动命令
在 Termux 中使用下面的命令启动 Lighttpd（保持在前台运行，方便调试）：

lighttpd -D -f /data/data/com.termux/files/usr/etc/lighttpd/lighttpd.conf

若希望后台运行，可以使用 nohup 或 & 命令。


2. 访问 Web 服务器
在浏览器中输入 http://127.0.0.1:8080（或设备 IP 地址与设置的端口）进行访问。




---

5. 注意事项

权限问题
修改工作目录为 /storage/emulated/0/termux_files 时，请确保 Termux 已获得存储权限，否则可能会出现读写失败的情况。

配置调试
如果 Lighttpd 启动报错，请检查日志信息（通常输出在终端），核对配置文件语法和路径是否正确。

安全性
若计划在公网环境使用，请务必配置适当的安全措施（如防火墙、访问控制等）。



---

通过以上步骤，你可以在 Termux 中快速搭建并配置一个基于 Lighttpd 的轻量级 Web 服务器，同时将工作目录修改为 /storage/emulated/0/termux_files 以便于管理你的网站文件。








