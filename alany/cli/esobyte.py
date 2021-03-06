import click
from ..esobyte import compiler
from .main import cli


@cli.group(help='EsoByte interpreter')
@click.version_option('EsoByte 0.0.1')
def esobyte():
    pass


@esobyte.command()
@click.argument('file')
def run(file):
    compiler.run_file(file)
