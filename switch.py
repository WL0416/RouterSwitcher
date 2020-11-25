import paramiko
import time
import tkinter as tk

user_name = 'ubnt'
passwd = 'Aienglish@10'
ip = '192.168.222.1'
enable = '/home/ubnt/script/enable.sh'
disable = '/home/ubnt/script/disable.sh'


def ssh_init():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=user_name, password=passwd)
    return ssh


def ssh_enable():
    ssh = ssh_init()
    stdin, stdout, stderr = ssh.exec_command(enable)
    time.sleep(2)

    cmd_result = stdout.read(), stderr.read()

    for line in cmd_result:
        print(line)

    ssh.close()
    print('Connection Closed.')
    message['text'] = '已切到专线'


def ssh_disable():
    ssh = ssh_init()
    stdin, stdout, stderr = ssh.exec_command(disable)
    time.sleep(2)

    cmd_result = stdout.read(), stderr.read()

    for line in cmd_result:
        print(line)

    ssh.close()
    print('Connection Closed.')
    message['text'] = '已切到备线'


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Router Switch')
    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    enable_button = tk.Button(master=window, text='专用线路', width=15, height=5, bg="green", fg="yellow", command=ssh_enable)
    enable_button.grid(row=0, column=0, sticky='nsew')

    message = tk.Label(master=window, text='')
    message.grid(row=0, column=1)

    disable_button = tk.Button(master=window, text='备用线路', width=15, height=5, bg="red", fg="yellow", command=ssh_disable)
    disable_button.grid(row=0, column=2, sticky='nsew')

    window.mainloop()
