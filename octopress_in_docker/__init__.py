#!/usr/bin/env python3

import os
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--octopress-root', default='.',
                        help='directory of octopress source')
    parser.add_argument('-p', '--port', default=4000)
    parser.add_argument('--sudo', action='store_true', default=False, help='Use sudo for running docker command')
    parser.add_argument('command', nargs='+')
    args = parser.parse_args()

    root = os.path.abspath(args.octopress_root)
    try:
        _cmd = ['/wrapper']
        if args.command[:2] != ['bundle', 'exec']:
            _cmd += ['bundle', 'exec'] + args.command
        else:
            _cmd += args.command
    except Exception as exc:
        print(exc)
        return 1

    cmd = ['docker', 'run', '-it', '--rm', '-v', f'{root}:/src',
           '-p', f'{args.port}:4000', '-e', f'DOCKER_UID={os.getuid()}',
           'xupeng/octopress'] + _cmd
    if args.sudo:
        cmd = ['sudo'] + cmd
    return subprocess.call(cmd)


if __name__ == '__main__':
    main()
