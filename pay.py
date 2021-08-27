import random


# 输入金额返回红包值的函数,其中x是消费金额，c是红包金额比例，默认0.1
def Red_envelope(x, c=0.1):
    # 生成随机数
    a = random.uniform(0.01, c * x)
    # 保留两位小数
    b = round(float(a), 2)
    return b


def test(content):
    # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
    if content.isdigit() or content == "":
        return True
    else:
        return False
