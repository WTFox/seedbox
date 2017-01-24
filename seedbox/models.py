import base64
import os
import pickle

import click
import paramiko


class SeedBox():
    """Simple interface to view recently available files."""

    def __init__(self):
        self.home_dir = os.path.expanduser('~')
        self.config_file = os.path.join(self.home_dir, '.sbconfig')

        if not self._has_creds():
            yes = click.confirm("You do not have information credentials stored. Would you like to enter them now?")
            if yes:
                self._add_auth_credentials()
            else:
                exit()

        with open(self.config_file, 'rb') as f:
            _creds = pickle.load(f)
            _creds = base64.b64decode(_creds).decode().split(';;')
            self.hostname = _creds[0]
            self.port = int(_creds[1])
            self.username = _creds[2]
            self.password = _creds[3]

        if not all([self.hostname, self.port, self.username, self.password]):
            yes = click.confirm("You do not have information credentials stored. Would you like to enter them now?")
            if yes:
                self._add_auth_credentials()
            else:
                exit()

        self.conn = None
        self.transport = None

    def _has_creds(self):
        home_dir = os.path.expanduser('~')
        if not os.path.exists(os.path.join(home_dir, '.sbconfig')):
            return False

        return True

    def _add_auth_credentials(self):
        hostname = click.prompt('Enter the hostname')
        port = click.prompt('Enter the port', type=int)
        username = click.prompt('Enter the username')
        password = click.prompt('Enter the password (input is hidden)', hide_input=True)
        _creds = "{};;{};;{};;{}".format(hostname, port, username, password)

        with open(self.config_file, 'wb') as f:
            encrypted_creds = base64.b64encode(bytes(_creds, encoding='utf8'))
            pickle.dump(encrypted_creds, f, pickle.HIGHEST_PROTOCOL)

        return

    def _login(self):
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.conn = paramiko.SFTPClient.from_transport(self.transport)
        return self.conn

    def _logout(self):
        self.conn.close()
        self.transport.close()

    def __enter__(self):
        return self._login()

    def __exit__(self, *args):
        self._logout()
