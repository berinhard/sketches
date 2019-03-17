#!/usr/bin/env python3
import click
import os
from cprint import cprint
from shutil import copyfile
from unipath import Path

SKETCH_DIR = Path(__file__).parent
TEMPLATES_DIR = SKETCH_DIR.child('templates')

@click.group()
def cli():
    pass

@cli.command()
@click.argument('dir_name')
def configure_new_sketch(dir_name):
    new_dir = SKETCH_DIR.child(dir_name)
    new_sketch = new_dir.child(f'{dir_name}.pyde')
    base_sketch = TEMPLATES_DIR.child('base_sketch.pyde')

    if os.path.exists(new_dir):
        cprint.err(f"There's already a sketch name {dir_name}", interrupt=True)

    os.mkdir(new_dir)
    copyfile(base_sketch, new_sketch)


if __name__ == '__main__':
    cli()
