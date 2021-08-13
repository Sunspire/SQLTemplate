from collections import Callable
from dataclasses import dataclass
from classes.command_controller import CommandController


@dataclass
class Command:
    method: Callable
    description: str
    name: str
    
commands = [
    Command(CommandController.fr, 'Generate script for FR', 'fr'),
    Command(CommandController.uk, 'Generate script for UK', 'uk')
]