from collections import Callable
from dataclasses import dataclass
from classes.command_controller import CommandController


@dataclass
class Command:
    method: Callable
    description: str


commands = {
    'ch': Command(CommandController.ch, 'Generate script for CH'),
    'fr': Command(CommandController.fr, 'Generate script for FR'),
    'uk': Command(CommandController.uk, 'Generate script for UK'),
    'europe': Command(CommandController.generate_europe_script, 'Generate script for Europe')
}