import os

import paramiko


class SeedBox():
    """Simple interface to view recently available files."""

    def __init__(self):
        self.hostname = os.environ.get('SBOX_HOSTNAME', None)
        self.port = int(os.environ.get('SBOX_PORT', None))
        self.username = os.environ.get('SBOX_USERNAME', None)
        self.password = os.environ.get('SBOX_PASSWORD', None)
        if not all([self.hostname, self.port, self.username, self.password]):
            raise ValueError("Please provide all login information.")

        self.conn = None
        self.transport = None

    def __enter__(self):
        return self._login()

    def __exit__(self, *args):
        self._logout()

    def _login(self):
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.conn = paramiko.SFTPClient.from_transport(self.transport)
        return self.conn

    def _logout(self):
        self.conn.close()
        self.transport.close()