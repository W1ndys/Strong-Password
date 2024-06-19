import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_strong_password(length, include_digits=True, include_uppercase=True, include_lowercase=True, include_special=True):
    # 定义字符集
    characters = ''
    if include_digits:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("至少要包含一种字符类型。")
    
    # 确保密码包含指定的每种字符
    password = []
    if include_digits:
        password.append(random.choice(string.digits))
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_special:
        password.append(random.choice(string.punctuation))
    
    # 填充剩余字符
    remaining_length = length - len(password)
    if remaining_length > 0:
        password += random.choices(characters, k=remaining_length)
    
    # 打乱密码字符顺序
    random.shuffle(password)
    
    # 将列表转换为字符串
    return ''.join(password)

def generate_passwords():
    try:
        count = int(entry_count.get())
        length = int(entry_length.get())
        
        include_digits = var_digits.get()
        include_uppercase = var_uppercase.get()
        include_lowercase = var_lowercase.get()
        include_special = var_special.get()
        
        passwords = []
        for _ in range(count):
            passwords.append(generate_strong_password(length, include_digits, include_uppercase, include_lowercase, include_special))
        
        with open('passwords.txt', 'w') as file:
            for pwd in passwords:
                file.write(pwd + '\n')
        
        messagebox.showinfo("密码生成完成", f"生成的密码已保存在 'passwords.txt' 文件中。")
    except ValueError as e:
        messagebox.showerror("输入错误", str(e))

# 创建主窗口
window = tk.Tk()
window.title("密码生成工具")

# 获取屏幕尺寸
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 窗口尺寸
window_width = 300
window_height = 250

# 计算窗口左上角坐标使其居中
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口的初始位置和大小
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 标签和输入框
label_count = tk.Label(window, text="生成密码数量:")
label_count.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_count = tk.Entry(window, width=10)
entry_count.grid(row=0, column=1, padx=10, pady=10)

label_length = tk.Label(window, text="密码长度:")
label_length.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_length = tk.Entry(window, width=10)
entry_length.grid(row=1, column=1, padx=10, pady=10)

# 复选框
var_digits = tk.BooleanVar()
var_digits.set(True)
check_digits = tk.Checkbutton(window, text="包含数字", variable=var_digits)
check_digits.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

var_uppercase = tk.BooleanVar()
var_uppercase.set(True)
check_uppercase = tk.Checkbutton(window, text="包含大写字母", variable=var_uppercase)
check_uppercase.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

var_lowercase = tk.BooleanVar()
var_lowercase.set(True)
check_lowercase = tk.Checkbutton(window, text="包含小写字母", variable=var_lowercase)
check_lowercase.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

var_special = tk.BooleanVar()
var_special.set(True)
check_special = tk.Checkbutton(window, text="包含特殊字符", variable=var_special)
check_special.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

# 生成密码按钮
btn_generate = tk.Button(window, text="生成密码", command=generate_passwords)
btn_generate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 运行主循环
window.mainloop()
