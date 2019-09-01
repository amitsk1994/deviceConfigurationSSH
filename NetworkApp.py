import sys
from ip_valid_file import ip_valid_file
from ip_addr_valid import ip_addr_valid
from check_reach import check_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

ip_list=ip_valid_file()

try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n Program aborted by user\n")
    sys.exit()


try:
    check_reach(ip_list)
except KeyboardInterrupt:
    print("\n Program aborted by user\n")
    sys.exit()

create_threads(ip_list,ssh_connection)
