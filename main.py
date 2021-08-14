from termcolor import colored
from classes.command import commands
from classes.command_controller import CommandController
import sys


def command_parser(the_command):
    the_command = the_command.strip().lower()
    
    if the_command == 'q':
        confirm_exit = input(colored('are you sure (y/n)? > ', 'yellow'))

        if confirm_exit.strip().lower() == 'y':
            return True

        print(colored('ok', 'green'))
        return False

    try:
        command_controller.do_command(commands[the_command])
    except KeyError:
        print(colored('Unknown command', 'yellow'))
    
    return False


def argument_parser(arguments):
    command_controller = CommandController()
    try:
        command_controller.do_command(commands[arguments[1]])
    except KeyError:
        print(colored('Unknown argument', 'yellow'))
    command_controller = CommandController()


def main():
    is_exit = False
    while not is_exit:
        command = input(colored('-> ', 'cyan'))
        is_exit = command_parser(command)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        command_controller = CommandController()
        print()
        print()
        print(colored('<=== SQL Script Generator ===>', 'cyan'))
        print()
        main()

    else:
        argument_parser(sys.argv)