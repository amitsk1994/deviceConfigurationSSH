import paramiko
import os.path
import sys
import re
import time

user_file= input("Enter the file and path in the correct format");

#to check if valid file
if(os.path.isfile(user_file)):
    print("valid file")
else:
    print("invalid file")
    sys.exit()


#to check if cmd file is valid
cmd_file=input("Enter the command file and path with correct format")

if(os.path.isfile(cmd_file)):
    print("valid command file")
else:
    print("invalid file")
    sys.exit()

def ssh_connection(ip):
    global user_file
    global cmd_file

    try:

        selected_user_file=open(user_file,"r")
        selected_user_file.seek(0)

        username = selected_user_file.readlines()[0].split(",")[0].rstrip("\n")

        selected_user_file.seek(0)

        password = selected_user_file.readlines()[0].split(",")[1].rstrip("\n")

        session = paramiko.SSHClient()

        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        session.connect(ip.rstrip("\n"),username=username,password=password)

        #invoke CLI
        connection = session.invoke_shell()

        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        selected_cmd_file=open(cmd_file,"r")
        selected_cmd_file.seek(0)

        for eachline in selected_cmd_file.readlines():
            connection.send(eachline+"\n")
            time.sleep(2)

        selected_user_file.close()
        selected_cmd_file.close()


        router_output=connection.recv(65535)

        if re.search(b"% invalid input",router_output):
            print("There was a invalid input in the command file {}".format(ip))
        else:
            print("Executed on device {}\n".format(ip))

        print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(router_output)))
        print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(router_output))[1])

        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")
