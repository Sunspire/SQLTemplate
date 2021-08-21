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
    autoconfig = arguments.autoconfig
    if autoconfig is not None:
        command_controller.do_command(commands['autoconfig'])
        return
        
    market = arguments.market
    template = arguments.template
    file_name = arguments.filename

    if market is None and autoconfig is None:
        print('Market is missing')
        return

    if (market is not None) and (not market.lower() in commands) and (autoconfig is None):
        print('Unknown market')
        return

    if market is not None:
        market = market.lower()

    if template is None:
        template = 'standard'

    if file_name is None:
        file_name = ''

    command_controller.set_global('market', market)
    command_controller.set_global('template', template.lower())
    command_controller.set_global('file_name', file_name)
    command_controller.set_global('output_directory', arguments.outputdirectory)
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
        parser.add_argument('-fn', '--filename', help='name of output file')
        parser.add_argument('-o', '--outputdirectory', help='absolute path of output directory (no spaces allowed)')
        parser.add_argument('-auto', '--autoconfig', help='generates scripts from auto config file')
        argument_parser(parser.parse_args())