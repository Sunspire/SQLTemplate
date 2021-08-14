from collections import Callable
from dataclasses import dataclass
from classes.command_controller import CommandController


@dataclass
class Command:
    method: Callable
    description: str


commands = {
    'fr': Command(CommandController.fr, 'Generate script for FR'),
    'uk': Command(CommandController.uk, 'Generate script for UK')
}