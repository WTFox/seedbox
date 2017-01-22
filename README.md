
# seedbox

## Setup

Add the following lines to your bashrc/zshrc/etc

```
# Seedbox
export SBOX_HOSTNAME="<IP or URL HERE>"
export SBOX_PORT=22
export SBOX_USERNAME="<USERNAME_HERE>"
export SBOX_PASSWORD="<PASSWORD_HERE>"

```

## Installation

Just download or clone this project, `cd` into the dir then run

``` bash 

    python setup.py install
   
```

or 

``` bash

    pip install .

```

## Usage
``` bash
    ➜  ~ seedbox --help
    Usage: seedbox [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      ls      lists the latest files from /downloads/<dir>.
      movies  lists the latest movies from the SeedBox.
      tv      lists the latest tvshows from the SeedBox.
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

Nothing to see here yet folks

## License

MIT: [http://rem.mit-license.org](http://rem.mit-license.org)