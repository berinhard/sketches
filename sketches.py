#!/usr/bin/env python3
import click
import os
import subprocess
import shlex
import random
from datetime import date
from cprint import cprint
from shutil import copyfile
from unipath import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

SKETCH_DIR = Path(__file__).parent
TEMPLATES_DIR = SKETCH_DIR.child('templates')

templates = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
)

@click.group()
def cli():
    pass

@cli.command('new')
@click.argument('sketch_name')
def configure_new_sketch(sketch_name):
    """
    Create dir and configure boilerplate
    """
    new_dir = SKETCH_DIR.child(sketch_name)
    new_sketch = new_dir.child(f'{sketch_name}.pyde')
    base_sketch = TEMPLATES_DIR.child('base_sketch.pyde')

    if new_dir.exists():
        cprint.err(f"There's already a sketch \"{sketch_name}\"", interrupt=True)

    os.mkdir(new_dir)
    copyfile(base_sketch, new_sketch)

@cli.command('export')
@click.argument('sketch_name')
@click.option('--frame-rate', '-r', default=24)
@click.option('--output', '-o', default=None)
@click.option('--clean-after', '-c', is_flag=True, default=False)
def export_to_video(sketch_name, frame_rate, output, clean_after):
    """
    Export frames from sketch to a MP4 video
    """
    sketch_dir = SKETCH_DIR.child(sketch_name)

    if not sketch_dir.exists():
        cprint.err(f"There's no directory for the sketch {sketch_name}", interrupt=True)

    output = output or sketch_dir.child('output.mp4')
    cprint.info(f"Generating {output} from sketch sketch_name")
    query = sketch_dir + "/*.png"
    command = ' '.join([str(c) for c in [
        'ffmpeg', '-framerate', frame_rate, '-pattern_type', 'glob', '-i', query, '-c:v', 'libx264', '-r', frame_rate, '-pix_fmt', 'yuv420p', output
    ]])

    cprint.info(f"Command:\n\t$ {command}")

    convert = subprocess.Popen(
        shlex.split(command),
    )
    convert.wait()

    if clean_after:
        pngs = sketch_dir.listdir("*.png")
        cover = random.choice(pngs)
        cover.rename("cover.png")
        for png in pngs:
            png.remove()

@cli.command('update_index')
@click.argument('sketch_name')
@click.option('--title', '-t', default='')
@click.option('--cover', '-c', default='cover.png')
def update_index_with_sketch(sketch_name, title, cover):
    """
    Updates index.html with new the new sketch
    """
    sketch_dir = SKETCH_DIR.child(sketch_name)

    if not sketch_dir.exists():
        cprint.err(f"There's no directory for the sketch {sketch_name}", interrupt=True)

    desc, desc_ptbr = '', ''
    while not desc:
        desc = input("Enter with sketch's description: ").strip()
    while not desc_ptbr:
        desc_ptbr = input("Entre com a descrição do sketch (PT-BR): ").strip()

    title = title or f'#{sketch_name}'
    template = templates.get_template('new_entry_snippet.html')
    today = date.today()
    ctx = {
        'sketch_id': sketch_name,
        'title': title,
        'cover': cover,
        'sketch_date': f'{today:%m/%d/%Y}',
        'description': desc,
    }

    content = template.render(ctx)
    index_template = templates.get_template('index_base.html')
    new_index_content = index_template.render(new_sketch_content=content)

    with open(SKETCH_DIR.child('index.html'), 'w') as fd:
        fd.write(new_index_content)

    content = template.render(ctx)
    index_template = templates.get_template('index_base.html')
    base_index_content = index_template.render(new_sketch_content='{{ new_sketch_content }}\n\n' + content)

    with open(TEMPLATES_DIR.child('index_base.html'), 'w') as fd:
        fd.write(base_index_content)


if __name__ == '__main__':
    cli()
