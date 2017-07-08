#!/usr/bin/env python

from conf import Conf
from utils import Utils
import click
from tail_toolkit import __version__


conf = Conf()

def execute_cli(args):
    Utils.click_validate_required_options(click.get_current_context(), conf)
    module = click.get_current_context().info_name
    myclass = __import__("tail_toolkit.modules." + module)
    clazz = getattr(getattr(myclass.modules, module), module.title())
    getattr(clazz(conf, args), args['action'].replace("-", "_") + "_" + module)().save_config()

@click.group()
def cli(**kwargs):
    pass

@cli.command()
@click.argument('action', required=True, type=click.Choice(Utils.click_get_command_choice("tail", conf)))
@click.option('--loggroupname', '-l', help="Define the loggroupname.")
@Utils.docstring_parameter(conf)
def tail(**kwargs):
    execute_cli(kwargs)

print("Initializing tail-toolkit CLI (v" + __version__ + ") - Region: " + conf.region)
cli()
