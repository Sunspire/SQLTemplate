from classes.command import commands
from classes.command_controller import CommandController
import sys


def command_parser(the_command):
    the_command = the_command.strip().lower()
    
    if the_command == 'q':
        confirm_exit = input('are you sure (y/n)? > ')

        if confirm_exit.strip().lower() == 'y':
            return True

        print('ok')
        return False

    try:
        command_controller.do_command(commands[the_command])
    except KeyError:
        print('Unknown command')
    
    return False


def argument_parser(arguments):
    command_controller = CommandController()
    try:
        command_controller.do_command(commands[arguments[1]])
    except KeyError:
        print('Unknown argument')
    command_controller = CommandController()


def main_loop():
    is_exit = False
    while not is_exit:
        command = input('-> ')
        is_exit = command_parser(command)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        command_controller = CommandController()
        print()
        print()
        print('<=== SQL Script Generator ===>')
        print()
        main_loop()

    else:
        argument_parser(sys.argv)