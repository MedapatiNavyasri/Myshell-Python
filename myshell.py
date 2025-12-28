# MyShell - A custom CLI for System Diagnostics
# Created by: [Medapati Navya sri]
# Features: Process management, History, and SysInfo

import os
import subprocess
import platform

def main():
    history=[]
    while True:
        try:
            current_dir=os.getcwd()
            user_input = input(f"{current_dir}$> ").strip()
            
            if not user_input:
                continue
            history.append(user_input)
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting")
                break
                
            # Execute the command
            execute_command(user_input,history)
            
        except EOFError: # Handles Ctrl+D
            break
        except KeyboardInterrupt:
            print("\nType 'exit' to quit.")
def execute_command(user_input,history):
    # 1. Split for checking the command name (like 'cd' or 'exit')
    args = user_input.split()
    if not args:
        return
    if args[0]=="history":
        for i,cmd in enumerate(history,1):
            print(f"{i} {cmd}")
        return
    if args[0]=="sysinfo":
        print(f"OS:{platform.system()} {platform.release()}")
        print(f"Node: {platform.node()}")
        return

    # 2. Handle 'cd' internally (it's a built-in)
    if args[0] == "cd":
        try:
            path = args[1] if len(args) > 1 else os.path.expanduser("~")
            os.chdir(path)
        except Exception as e:
            print(f"cd: {e}")
            
    # 3. Handle everything else
    else:
        try:
            # On Windows, we pass the full string 'user_input' 
            # instead of the list 'args' when using shell=True
            subprocess.run(user_input, shell=True)
        except Exception as e:
            print(f"myshell: {e}")

if __name__ == "__main__":

    main()
