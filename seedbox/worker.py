import os

from redis import Redis
from rq import Worker, Queue, Connection, use_connection

listen = ['high', 'default', 'low']

conn = Redis('10.10.0.9', 6379)
use_connection(conn)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
