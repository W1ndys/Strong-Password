# Strong-Password

这是一个使用 Python 和 tkinter 实现的简单密码生成工具，可以生成包含数字、大写字母、小写字母和特殊字符的强密码，并将生成的密码保存在文件中。

## 特性

- 生成指定数量和长度的强密码。
- 可选择是否包含数字、大写字母、小写字母和特殊字符。
- 自动生成的密码保存在 `passwords.txt` 文件中，每行一个密码。

## 使用方法

### 环境要求

- Python 3.x
- tkinter 库 (通常已经包含在 Python 安装中)

### 安装依赖

无需安装额外依赖。

### 运行项目

1. 克隆项目到本地：

   ```bash
   git clone https://github.com/W1ndys/Strong-Password.git
   ```

2. 进入项目目录：

   ```bash
   cd Strong-Password
   ```

3. 运行主程序：

   ```bash
   python Strong-Password-UI.py
   ```

## TODO

- [x] 密码长度可配置
- [x] 密码字符集可配置
- [x] 密码强度可配置
- [x] 密码生成可保存到文件
- [x] 密码生成可随机生成
- [x] UI 界面

## 注意事项

- 确保输入的密码长度和数量符合逻辑，避免过大或过小的输入。
- 生成的密码文件默认保存在当前目录的 `passwords.txt` 文件中。

## 许可证

该项目采用 MIT 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。
