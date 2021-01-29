import getpass
import telnetlib
import sys


# arguments
HOST = '192.168.10.1'
pass1 = 'khmer123'
pass2 = 'khmer123'
filepath = "quick_sw_conf.txt"

# get commands from text file
commands_f = open(filepath, "r")
commands = commands_f.readlines()
commands_f.close()


# define functions
def use_password(password):
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')


def user_login(sw_pass, en_pass):
    use_password(sw_pass)
    tn.write(b"enable\n")
    use_password(en_pass)
    tn.write(b"configure terminal\n")


def create_vlan(vid, ip):
    tn.write('vlan {}\n'.format(vid).encode('ascii'))
    tn.write('int vlan {}\n'.format(vid).encode('ascii'))
    tn.write('ip add {} 255.255.255.0\n'.format(ip).encode('ascii'))


def connect(host):
    try:
        global tn
        tn = telnetlib.Telnet(host)
    except OSError:
        print("No route to host. Please check your connection.")
        exit(1)


def main():
    # log into switch
    connect(HOST)
    user_login(pass1, pass2)

    # write commands to switch
    for line in commands:
        tn.write(line.encode('ascii'))

    # display changes to user
    print(tn.read_all().decode('ascii'))


if __name__ == "__main__":
    main()

