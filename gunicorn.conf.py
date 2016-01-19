from os import environ

bind = '0.0.0.0:' + environ.get('PORT')
workers = int(environ.get('WORKERS', '4'))


def post_fork(server, worker):
    with open('/tmp/app-initialized', 'w'):
        pass
