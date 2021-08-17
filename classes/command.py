from collections import Callable
from dataclasses import dataclass
from classes.command_controller import CommandController


@dataclass
class Command:
    method: Callable

commands = {
    'besc': Command(CommandController.besc),
    'ch': Command(CommandController.ch),
    'fr': Command(CommandController.fr),
    'gr': Command(CommandController.gr),
    'ib': Command(CommandController.ib),
    'neu': Command(CommandController.neu),
    'see': Command(CommandController.see),
    'tr': Command(CommandController.tr),
    'uk': Command(CommandController.uk),
    'europe': Command(CommandController.europe)
}