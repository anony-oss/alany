import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default='run')
@click.version_option('Alany 0.1.2, EsoByte 0.0.1')
def cli():
    pass
