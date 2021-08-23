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
    'uae': Command(CommandController.uae),
    'ksa': Command(CommandController.ksa),
    'ind': Command(CommandController.ind),
    'europe': Command(CommandController.europe),
    'meia': Command(CommandController.meia),
    'autoconfig': Command(CommandController.auto_config)
}