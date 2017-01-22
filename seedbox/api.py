import os

import click

from .models import SeedBox
from .utils import convert_time, is_dir


def _latest_files(dir, count):
    """Simple function that lists the latest items from <dir>"""
    with SeedBox() as s:
        _dir = os.path.join('downloads', dir)
        try:
            s.chdir(_dir)
        except:
            click.secho("Invalid directory.", fg="red")
            return

        click.echo(click.style("Getting latest files...", fg='green'))
        files = sorted(s.listdir_attr(), key=lambda x:x.st_mtime, reverse=True)
        for file in files[:count]:
            msg = "{}\t{}".format(convert_time(file.st_mtime), file.filename)
            if is_dir(file):
                click.secho(msg, fg='blue')
            else:
                click.secho(msg, fg='white')
    return


@click.group()
def cli():
    pass


@cli.command()
@click.option('--count', default=10, help='number of files in movies to display')
def latest_movies(count):
    """lists the latest movies from the SeedBox."""
    _latest_files('movies', count)


@cli.command()
@click.option('--count', default=10, help='number of files in tvshows to display')
def latest_tv(count):
    """lists the latest tvshows from the SeedBox."""
    _latest_files('tvshows', count)


@cli.command()
@click.option('--dir', default='', help='directory to list files in. default: downloads/')
@click.option('--count', default=10, help='number of files in <dir> to display')
def latest_files(dir, count):
    """lists the latest files from <dir>."""
    _latest_files(dir, count)


if __name__ == '__main__':
    cli()

