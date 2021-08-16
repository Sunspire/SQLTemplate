from collections import Callable
from dataclasses import dataclass
from classes.command_controller import CommandController


@dataclass
class Command:
    method: Callable
    description: str


commands = {
    'besc': Command(CommandController.besc, 'Generate script for BESC'),
    'ch': Command(CommandController.ch, 'Generate script for CH'),
    'fr': Command(CommandController.fr, 'Generate script for FR'),
    'gr': Command(CommandController.gr, 'Generate script for GR'),
    'ib': Command(CommandController.fr, 'Generate script for IB'),
    'neu': Command(CommandController.fr, 'Generate script for NEU'),
    'see': Command(CommandController.fr, 'Generate script for SEE'),
    'tr': Command(CommandController.fr, 'Generate script for TR'),
    'uk': Command(CommandController.uk, 'Generate script for UK'),
    'europe': Command(CommandController.europe, 'Generate script for Europe')
}