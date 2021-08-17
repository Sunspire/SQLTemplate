import argparse
from classes.command import commands
from classes.command_controller import CommandController
import sys


def command_parser(the_command):
    the_command = the_command.strip().lower()
    
    if the_command == 'q':
        return True

    try:
        first_word_in_command = the_command.split()[0]
        command_controller.command = the_command
        command_controller.do_command(commands[first_word_in_command])
    except KeyError:
        print('Unknown command')
    
    return False


def argument_parser(arguments):
    market = arguments.market
    template = arguments.template

    if market is None:
        print('Market is missing')
        return

    if not market in commands:
        print('Unknown market')
        return

    if template is None:
        template = ''
        
    command_controller.command = market + ' ' + template
    command_controller.template_name = template
    command_controller.do_command(commands[market])

def main_loop():
    is_exit = False
    while not is_exit:
        command = input('-> ')
        is_exit = command_parser(command)


if __name__ == '__main__':
    command_controller = CommandController()
    command_controller.init()
    if len(sys.argv) <= 1:        
        print()
        print()
        print('<=== SQL Script Generator ===>')
        print()
        main_loop()

    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--market', help='specify the market. e.g. FR, Europe')
        parser.add_argument('-t', '--template', help='specify the template. Standard is the default if no template is given')
        argument_parser(parser.parse_args())