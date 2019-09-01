import sys
import os.path

#to check validity of file and return list of ip addresses
def ip_valid_file():
    ip_file = input("Enter the file name and path in correct format")

    if(os.path.isfile(ip_file)):
        print("file name is valid")
    else:
        print("Invalid file name")
        sys.exit()


    #below code is to work with the file and return list of ip addresses from the internal file
    select_ip_file =open(ip_file,"r");
    select_ip_file.seek(0);
    ip_list = select_ip_file.readlines();
    select_ip_file.close()

    return ip_list
