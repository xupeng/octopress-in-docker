#!/usr/bin/env python

import os
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--octopress-root', default='.',
                        help='directory of octopress source')
    parser.add_argument('-p', '--port', default=4000)
    parser.add_argument('command', nargs='+')
    args = parser.parse_args()

    root = os.path.abspath(args.octopress_root)
    try:
        if args.command[:2] != ['bundle', 'exec']:
            _cmd = ['bundle', 'exec'] + args.command
        else:
            _cmd = args.command
    except Exception, exc:
        print exc
        return 1

    cmd = ['docker', 'run', '-it', '--rm', '-v', '%s:/src' % root,
           '-p', '%s:4000' % args.port, 'xupeng/octopress'] + _cmd
    return subprocess.call(cmd)


if __name__ == '__main__':
    main()
