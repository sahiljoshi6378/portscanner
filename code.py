# Importing all modules that will be used in the program
import time
import socket
from IPy import IP
from termcolor import colored


# Paste the whole code in restart function "restart_scanner()"
def restart_scanner():
    # list of options for port scanning
    global pings
    option_list = ['Scan only Web ports', 'Scan FTP ports', 'Scan All well-known port numbers', 'Custom Scan'];

    # list of some well-known ports will be used in option 3 of above given list
    well_known_ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 143, 161, 194, 443]

    # Extra useless function just to improve user experience
    def user_experience():
        time.sleep(0.2)
        print(colored('Establishing connection  with the Target', 'green'))
        time.sleep(1)
        print()
        print(colored('Almost dome', 'green'))
        time.sleep(0.5)
        print(colored('Srarting Port Scanner', 'green'))
        print()
        print('---------------------------------------------')

    # This is the function that tries to converts the given target into ip using "IPy IP"
    # if any Error occurred it will convert the given target into ip using "gethostbyname(user_target)"
    def target_checker(user_target):
        try:
            actual_ip = IP(user_target)
            return actual_ip
        except:
            actual_ip = socket.gethostbyname(user_target)
            return actual_ip

    # Main PORT scanner function
    def port_scanner(ip_address, given_port):

        # first we call the " target_checker(user_target) " to convert the target;s ip form given url
        try:
            target_checker(user_target)

            # here we tries to establishing connecting with the given target on given port
            try:
                sock = socket.socket()
                sock.settimeout(accuracy_level)
                sock.connect((ip_address, given_port))

                # after success connection also checking if we can get data form port to,
                # recognise the running service on the port
                try:
                    data = sock.recv(1024)

                    # Printing port number with service running in Decoded format
                    print(colored('Port number ' + str(given_port) + ' is open :' + data.decode().strip('\n'), 'red'))
                except:

                    # Else printing only open port number without service data
                    print(colored('Port number ' + str(given_port) + ' is open :' + 'No data found!', 'red'))

            except:
                pass
                # we are not Printing closed ports
        except:

            # here we tries to establishing connecting with the given target on given port
            try:
                sock = socket.socket()
                sock.settimeout(accuracy_level)
                sock.connect((ip_address, given_port))

                # after success connection also checking if we can get data form port to,
                # recognise the running service on the port
                try:

                    # Printing port number with service running in Decoded format
                    data = sock.recv(1024)
                    print(colored('Port number ' + str(given_port) + ' is open :' + data.decode().strip('\n'), 'red'))
                except:

                    # Else printing only open port number without service data
                    print(colored('Port number ' + str(given_port) + ' is open :' + 'No data found!', 'red'))

            except:
                pass
                # we are not Printing closed ports

    user_target = input('Enter the target\'s ip\'s or url address\'s :')
    print('Please select from the below list')
    print()
    m = 0
    for i in option_list:
        m = m + 1
        print({m}, i)
    scanning_type = int(input(':::::--------:'))
    accuracy_level = int(input('Choose the Accuracy level [From 1-5] :'))
    if accuracy_level > 5:
        print('you should enter value form 1 to 5 only')
        print()
        print('It will take ', accuracy_level, 'seconds to establishing connection with each port')
        print()
    else:
        pass
    if scanning_type == 1:
        user_experience()
        if ',' in user_target:
            pings = user_target.split(',')
            for p in pings:
                print(colored(('scanning for :' + p), 'blue'))
                for l in range(0, 1):
                    port_scanner(p, 80)
                    port_scanner(p, 443)
                    print()
                    print('---------------------------------------------')
        else:
            print(colored(('scanning for :' + user_target), 'blue'))
            port_scanner(user_target, 80)
            port_scanner(user_target, 443)
        should_restart = input('Want to restart [y,n]:')
        if should_restart == 'y':
            restart_scanner()
        else:
            exit()
    elif scanning_type == 2:
        user_experience()
        if ',' in user_target:
            pings = user_target.split(',')
            for p in pings:
                print(colored(('scanning for :' + p), 'blue'))
                for l in range(0, 1):
                    port_scanner(p, 20)
                    port_scanner(p, 21)
                    print()
                    print('---------------------------------------------')
        else:
            print(colored(('scanning for :' + user_target), 'blue'))
            port_scanner(user_target, 20)
            port_scanner(user_target, 21)
        should_restart = input('Want to restart [y,n]:')
        if should_restart == 'y':
            restart_scanner()
        else:
            exit()
    elif scanning_type == 3:
        user_experience()
        if ',' in user_target:
            pings = user_target.split(',')
            for p in pings:
                print(colored(('scanning for :' + p), 'blue'))
                for i in well_known_ports:
                    port_scanner(p, i)
                print()
                print('---------------------------------------------')
        else:
            print(colored(('scanning for :' + user_target), 'blue'))
            for i in well_known_ports:
                port_scanner(user_target, i)
        should_restart = input('Want to restart [y,n]:')
        if should_restart == 'y':
            restart_scanner()
        else:
            exit()
    elif scanning_type == 4:
        if ',' in user_target:
            pings = user_target.split(',')
            print('Please enter how many ports do you want to scan :')
            port_start = int(input('Enter the starting port number :'))
            port_end = int(input('Enter the Ending port number :'))
            user_experience()
            for p in pings:
                print(colored(('scanning for :' + p), 'blue'))
                for port in range(port_start, port_end + 1):
                    port_scanner(p, port)
                print()
                print('---------------------------------------------')
        else:
            print('Please enter how many ports do you want to scan :')
            port_start = int(input('Enter the starting port number :'))
            port_end = int(input('Enter the Ending port number :'))
            user_experience()
            print(colored(('scanning for :' + user_target), 'blue'))
            for port in range(port_start, port_end + 1):
                port_scanner(user_target, port)
        should_restart = input('Want to restart [y,n]:')
        if should_restart == 'y':
            restart_scanner()
        else:
            exit()


# Calling the Main Function
restart_scanner()
