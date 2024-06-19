import random
import string


def generate_strong_password(
    length,
    include_digits=True,
    include_uppercase=True,
    include_lowercase=True,
    include_special=True,
):
    # 定义字符集
    characters = ""
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
    return "".join(password)


def generate_multiple_passwords():
    try:
        count = int(input("请输入要生成的密码数量: "))
        length = int(input("请输入每个密码的长度: "))

        # 询问用户是否包含每种字符

        # 经过 LilRan （https://github.com/Lil-Ran）(https://blog.xinshi.fun) 大佬的指点，使用 lambda 表达式简化代码

        check_include_rule = lambda x: input(x).strip().lower() in ["y", ""]
        include_digits = check_include_rule("是否包含数字 (y/n) [默认为 y]: ")
        include_uppercase = check_include_rule("是否包含大写字母 (y/n) [默认为 y]: ")
        include_lowercase = check_include_rule("是否包含小写字母 (y/n) [默认为 y]: ")
        include_special = check_include_rule("是否包含特殊字符 (y/n) [默认为 y]: ")

        # 下面是原来的代码，供参考

        # include_digits = input("是否包含数字 (y/n) [默认为 y]: ").strip().lower()
        # if include_digits == '' or include_digits == 'y':
        #     include_digits = True
        # else:
        #     include_digits = False

        # include_uppercase = input("是否包含大写字母 (y/n) [默认为 y]: ").strip().lower()
        # if include_uppercase == '' or include_uppercase == 'y':
        #     include_uppercase = True
        # else:
        #     include_uppercase = False

        # include_lowercase = input("是否包含小写字母 (y/n) [默认为 y]: ").strip().lower()
        # if include_lowercase == '' or include_lowercase == 'y':
        #     include_lowercase = True
        # else:
        #     include_lowercase = False

        # include_special = input("是否包含特殊字符 (y/n) [默认为 y]: ").strip().lower()
        # if include_special == '' or include_special == 'y':
        #     include_special = True
        # else:
        #     include_special = False

        passwords = []
        for _ in range(count):
            passwords.append(
                generate_strong_password(
                    length,
                    include_digits,
                    include_uppercase,
                    include_lowercase,
                    include_special,
                )
            )

        with open("passwords.txt", "w") as file:
            for pwd in passwords:
                file.write(pwd + "\n")

        print(f"生成的密码已保存在 'passwords.txt' 文件中。")
    except ValueError as e:
        print(f"输入错误: {e}")


# 调用函数
generate_multiple_passwords()
