# 启用 Termux 访问存储权限（如果尚未开启）
termux-setup-storage

# 手动开启存储权限（如果上面的命令未触发权限弹窗）
# 进入手机 设置 → 应用管理 → Termux，开启存储权限

# 创建目标目录 termux_files（如果目录已存在，不会报错）
mkdir -p /storage/emulated/0/termux_files

# 复制 Termux 目录内容到新创建的目录（-r 表示递归复制所有文件和子目录）
cp -r /data/data/com.termux/files/home/* /storage/emulated/0/termux_files/

# 进入目标目录 termux_files
cd /storage/emulated/0/termux_files

# 验证是否成功进入该目录
pwd  # 输出应为 /storage/emulated/0/termux_files

# 列出当前目录下的文件和文件夹
ls

# 使用 mt 创建 hello.py 文件
mt hello.py

# 在 hello.py 文件中输入以下代码：
# print("你好")

# 保存并退出 mt（Ctrl + S 保存，Ctrl + Q 退出）

# 运行 Python 文件
python hello.py

# 你应该会看到输出：你好

# ------------------- Lighttpd 配置相关 -------------------

# 备份原配置文件到 termux_files 目录，避免误操作丢失原配置
cp $PREFIX/etc/lighttpd/lighttpd.conf /storage/emulated/0/termux_files/

# 如果需要恢复配置文件，可以使用以下命令：
# 复制 termux_files 目录中的 lighttpd.conf 替换系统配置文件
cp /storage/emulated/0/termux_files/lighttpd.conf $PREFIX/etc/lighttpd/lighttpd.conf

# 如果 lighttpd 进程正在运行，先停止它
pkill lighttpd

# 复制完成后，重新启动 lighttpd 服务器
lighttpd -f $PREFIX/etc/lighttpd/lighttpd.conf

# 查看 Lighttpd 的错误日志，排查可能的问题
cat ~/www/error.log















