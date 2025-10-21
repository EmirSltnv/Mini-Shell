import os
import subprocess

def execute_command(cmd):
    if not cmd:
        return
    if cmd == "exit":
        print("Exiting shell...")
        exit(0)
    try:
        if "|" in cmd:
            cmds = [c.strip().split() for c in cmd.split("|")]
            p1 = subprocess.Popen(cmds[0], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(cmds[1], stdin=p1.stdout)
            p1.stdout.close()
            p2.communicate()
        else:
            subprocess.run(cmd.split())
    except Exception as e:
        print("Error:", e)

def main():
    print("MiniShell — Type 'exit' to quit.")
    while True:
        cmd = input("$ ")
        execute_command(cmd)

if __name__ == "__main__":
    main()
