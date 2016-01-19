from os import environ

bind = 'unix:/tmp/nginx.socket'
workers = int(environ.get('WORKERS', '4'))


def post_fork(server, worker):
    with open('/tmp/app-initialized', 'w'):
        pass
