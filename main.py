from termcolor import colored
from classes.command import commands
from classes.command_controller import CommandController


def command_parser(the_command):
    the_command = the_command.strip().lower()
    
    if the_command == 'q':
        confirm_exit = input(colored('are you sure (y/n)? > ', 'yellow'))

        if confirm_exit.strip().lower() == 'y':
            return True

        print(colored('ok', 'green'))
        return False
    
    for command in commands:
        if command.name == the_command:
            command_controller.do_command(command)
            break
    
    else:
        print(colored('Unknown command', 'red'))
    
    return False


command_controller = CommandController()
is_exit = False
while not is_exit:
    command = input(colored('What is your command? > ', 'cyan'))
    is_exit = command_parser(command)