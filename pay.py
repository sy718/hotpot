import tkinter as tk
from image import *
import numpy as np

pay_set = tk.Tk()
pay_set.title("定单支付")

pay = 200  # "pay "
account = 300  # "account "

code = get_image("code.jpg", 180, 180)


def test(content):
    # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
    if content.isdigit() or content == "":
        return True
    else:
        return False


pfa = tk.StringVar()
pfa_cmd = pay_set.register(test)
pfa.set(min(pay, account))

font_size = 20  # 字体大小
entry_payfromaccount = tk.Entry(pay_set, textvariable=pfa, validate='key', validatecommand=(pfa_cmd, '%P'))

label_pay = tk.Label(pay_set, text="本次消费需支付：" + str(pay) + "元", fg="black", font=('华文行楷', font_size, 'bold'))
label_account = tk.Label(pay_set, text="账户余额：" + str(account) + "元", fg="black", font=('华文行楷', font_size, 'bold'))
label_payfromaccount = tk.Label(pay_set, text="请输入从账户中支付：", fg="black", font=('华文行楷', font_size, 'bold'))
label_yuan = tk.Label(pay_set, text="元", fg="black", font=('华文行楷', font_size, 'bold'))


def payover():
    pay_face.destroy()
    red_packet = tk.Toplevel()
    low = 0.01
    high = 0.06
    num_packet = np.random.uniform(low * pay, high * pay)
    num_packet = (int(num_packet) // 10) * 10 + 8
    label_packet = tk.Label(red_packet, text="恭喜您获得红包 " + str(num_packet) + " 元",
                            fg="black", font=('华文行楷', font_size, 'bold'))
    packet_sure = tk.Button(red_packet, text="确定", fg="black", font=('华文行楷', font_size, 'bold'), bg="white",
                            command=red_packet.destroy)
    label_packet.grid(row=0, column=0, padx=PAD, pady=PAD)
    packet_sure.grid(row=1, column=0, padx=PAD, pady=PAD)


def pay_interface():  # 支付界面
    global pay_face
    pay_face = tk.Toplevel()
    pay_fromaccount = tk.Label(pay_face, text="已从账户中支付：" + str(pfa.get()) + "元",
                               fg="black", font=('华文行楷', font_size, 'bold'))
    pay_back = tk.Button(pay_face, text="返回", fg="black", font=('华文行楷', font_size, 'bold'), bg="white",
                         command=pay_face.destroy)
    pay_over = tk.Button(pay_face, text="支付成功", fg="black", font=('华文行楷', font_size, 'bold'), bg="white",
                         command=payover)
    pfm = pay - float(pfa.get())  # 需另外支付
    if float(pfa.get()) <= account:
        if pfm > 0:
            pay_payfrommoney = tk.Label(pay_face, text="还需支付：" + str(pfm) + "元",
                                        fg="black", font=('华文行楷', font_size, 'bold'))
            pay_qrcode = tk.Label(pay_face, text="扫描下方二维码进行支付", fg="black", font=('华文行楷', font_size, 'bold'))

            global code
            pay_codejpg = tk.Label(pay_face, image=code, compound="center")
            pay_fromaccount.grid(row=0, column=0, columnspan=2, padx=PAD, pady=PAD)
            pay_payfrommoney.grid(row=1, column=0, columnspan=2, padx=PAD, pady=PAD)
            pay_qrcode.grid(row=2, column=0, columnspan=2, padx=PAD, pady=PAD)
            pay_codejpg.grid(row=3, column=0, columnspan=2, padx=PAD, pady=PAD)
            pay_over.grid(row=4, column=0, padx=PAD, pady=PAD)
            pay_back.grid(row=4, column=1, padx=PAD, pady=PAD)
        elif pfm == 0:
            # pay_finish = tk.Label(pay_face, text="支付成功！", fg="black", font=('华文行楷', font_size, 'bold'))
            pay_fromaccount.grid(row=0, column=0, padx=PAD, pady=PAD)
            # pay_finish.grid(row=1, column=0, padx=PAD, pady=PAD)
            pay_over.grid(row=1, column=0, padx=PAD, pady=PAD)
    elif float(pfa.get()) > account or pfm < 0:
        pay_error = tk.Label(pay_face, text="金额有误，请重新输入！", fg="red", font=('华文行楷', font_size, 'bold'))
        pay_error.grid(row=0, column=0, padx=PAD, pady=PAD)
        pay_back.grid(row=1, column=0, padx=PAD, pady=PAD)


bt_sure = tk.Button(pay_set, text="支付", fg="black", font=('华文行楷', font_size, 'bold'), bg="white",
                    command=pay_interface)
bt_back = tk.Button(pay_set, text="返回", fg="black", font=('华文行楷', font_size, 'bold'), bg="white",
                    command=pay_set.destroy)

ROW = 3
COL = 2
PAD = 10
label_pay.grid(row=0, column=0, columnspan=COL + 1, padx=PAD, pady=PAD)
label_account.grid(row=1, column=0, columnspan=COL + 1, padx=PAD, pady=PAD)
label_payfromaccount.grid(row=2, column=0, padx=PAD, pady=PAD)
label_yuan.grid(row=2, column=2, padx=PAD, pady=PAD)
entry_payfromaccount.grid(row=2, column=1, padx=PAD, pady=PAD)
bt_sure.grid(row=4, column=0, padx=PAD, pady=PAD)
bt_back.grid(row=4, column=1, padx=PAD, pady=PAD)

for i in range(0, COL + 1):
    pay_set.columnconfigure(i, weight=1)

for i in range(0, ROW + 1):
    pay_set.rowconfigure(i, weight=1)

pay_set.mainloop()
