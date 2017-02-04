import os

import click

from .models import SeedBox
from .utils import convert_time, is_dir

PAGER_LIMIT = 12


def _latest_files(dir, count=10, all_files=False):
    """Simple function that lists the latest items from <dir>"""
    output = []
    with SeedBox() as s:
        try:
            s.chdir(os.path.join('downloads', dir))
            files = sorted(s.listdir_attr(), key=lambda x:x.st_mtime, reverse=True)
        except:
            click.secho("Invalid directory.", fg="red")
            return

    for index, file in enumerate(files):
        filename = file.filename.encode('ascii', errors='replace')
        msg = "{}  {}".format(
            convert_time(file.st_mtime),
            click.format_filename(filename)
        )
        _id = click.style(str(index), fg="yellow")
        if is_dir(file):
            output.append("{} {}".format(_id, click.style(msg, fg='blue')))
        else:
            output.append("{} {}".format(_id, click.style(msg, fg='white')))

        if not all_files:
            output = output[:count]

    if len(output) <= PAGER_LIMIT:
        echo_func = click.echo
    else:
        echo_func = click.echo_via_pager

    output = '\n'.join(output)
    echo_func(output)
    return


@click.group()
def cli():
    pass


@cli.command()
@click.option('--count', '-c', default=10, help='Number of files in movies to display.')
@click.option('--all-files', '-a', is_flag=True, help='Display all files.')
def movies(count, all_files):
    """lists the latest movies from the SeedBox."""
    _latest_files('movies', count, all_files)


@cli.command()
@click.option('--count', '-c', default=10, help='Number of files in tvshows to display.')
@click.option('--all-files', '-a', is_flag=True, help='Display all files.')
def tv(count, all_files):
    """lists the latest tvshows from the SeedBox."""
    _latest_files('tvshows', count, all_files)


@cli.command()
@click.option('--dir', '-d', default='', help='directory to list files in. default: downloads/')
@click.option('--count', '-c', default=10, help='number of files in <dir> to display')
@click.option('--all-files', '-a', is_flag=True, help='Display all files.')
def ls(dir, count, all_files):
    """lists the latest files from /downloads/<dir>."""
    _latest_files(dir, count, all_files)


if __name__ == '__main__':
    cli()

