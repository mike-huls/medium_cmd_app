from time import sleep
import sys

def cmdline():
    available_commands = ['help', 'quit', 'echo', 'pbar', 'joke']
    keepgoing = True
    while (keepgoing):
        typed = input("Type something. (Type 'help' for options)")
        words = [w for w in typed.split(" ")]
        command = words[0].lower()
        arguments = words[1:]

        if (command == ''):
            continue
        if (command not in available_commands):
            print(f"-> {command} is an invalid command. Available commands:", available_commands)
            continue

        if (command == 'help'):
            print('-> Try out the following commands', available_commands)
        if (command == 'echo'):
            print(f'-> {" ".join(arguments)}')
        if (command == 'pbar'):
            for i in range(21):
                sys.stdout.write('\r')
                # the exact output you're looking for:
                sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
                sys.stdout.flush()
                sleep(0.25)
            print(' done!')

        if (command == 'joke'):
            import requests
            joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
            print(f"-> {joke['setup']}")
            input("-> (press enter)")
            print(f"-> {joke['punchline']}")

        if (command == 'quit'):
            keepgoing = False


    else:
        print("exiting..")


if __name__ == "__main__":
    cmdline()
