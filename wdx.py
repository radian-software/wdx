#!/usr/bin/env python3

import collections
import os
import sys
import tempfile

class WdxError(Exception):
    def __init__(self, message=None):
        self.message = message

def group(iterable, group_size):
    # Devilish hack. See [1].
    #
    # [1]: https://stackoverflow.com/a/1625023/3538165
    return zip(*((iter(iterable),) * group_size))

def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def atomic_write(filename, contents):
    temp_filename = filename + '.tmp'
    with open(temp_filename, 'wb') as f:
        f.write(contents.encode('utf-8'))
    os.rename(temp_filename, filename)
    os.unlink(temp_filename)

def die(message):
    die_raw(f'{WDX}: {message}')

def die_raw(message):
    raise WdxError(message)

def get_save_file_name():
    if 'XDG_CONFIG_HOME' in os.environ:
        home = os.environ['XDG_CONFIG_HOME']
        if os.path.exists(home):
            return os.path.join(home, 'wdx', 'points')
    return os.path.expanduser(os.path.join('~', '.config', 'wdx', 'points'))

def read_save_file(filename=None):
    if filename is None:
        filename = get_save_file_name()
    try:
        with open(filename, 'rb') as f:
            text = f.read().decode('utf-8')
            lines = text.splitlines()
            if len(lines) % 2 != 0:
                die(f'There are an odd number of lines '
                    f'in {filename}, aborting')
            return dict(group(lines, 2))
    except FileNotFoundError:
        return {}

def write_save_file(points, filename=None):
    if filename is None:
        filename = get_save_file_name()
    # Sort first by paths and then by point names.
    entries = sorted(points.items(), key=lambda item: (item[1], item[0]))
    lines = []
    for point, path in entries:
        lines.append(point)
        lines.append(path)
    atomic_write(filename, os.linesep.join(lines) + os.linesep)

COMMANDS = collections.OrderedDict([
    ('go', ('<point>', 1, 1)),
    ('show', ('<point>', 1, 1)),
    ('set', ('[[<point>] <target>] [-f]', 0, 3)),
    ('rm', ('[<point>]', 0, 1)),
    ('version', (None, 0, 0)),
    ('help', ('[<command>]', 0, 1)),
])

def usage(command=None):
    if command:
        usage = COMMANDS[command][0]
        if usage:
            return f'usage: {WDX} {command} {usage}'
        else:
            return f'usage: {WDX} {command}'
    lines = []
    lines.append(f'usage: {WDX} [<command>] [<arg>...]')
    lines.append('')
    lines.append('commands:')
    for command, data in COMMANDS.items():
        usage = data[0]
        if usage:
            lines.append(f'    {command} {usage}')
        else:
            lines.append(f'    {command}')
    return os.linesep.join(lines)

def get_default_point():
    point = os.path.basename(os.getcwd())
    if '\n' in point:
        die(f'{point}: Warp point name cannot contain newline characters')
    return point

def get_default_target():
    path = os.getcwd()
    if '\n' in path:
        die(f'${path}: Warp point target cannot contain newline characters')
    return path

def command_go(point):
    points = read_save_file()
    if point in points:
        print('cd')
        print(points[point])
    else:
        die(f'{point}: No such warp point')

def command_show(point):
    points = read_save_file()
    if point in points:
        print('echo')
        print(points[point])
    else:
        die(f'{point}: No such warp point')

def command_set(*literal_args):
    try:
        literal_index = literal_args.index('--')
    except ValueError:
        literal_index = len(literal_args)
    args = []
    force = False
    for index, arg in enumerate(literal_args):
        if index > literal_index or arg not in ['--', '-f']:
            args.append(arg)
        elif arg == '-f':
            force = True
    if len(args) == 0:
        point = get_default_point()
        target = get_default_target()
    elif len(args) == 1:
        point = args[0]
        target = get_default_target()
    elif len(args) == 2:
        point, target = args
    if '\n' in point:
        die(f'{point}: Warp point name cannot contain newline characters')
    if '\n' in target:
        die(f'{point}: Warp point target cannot contain newline characters')
    points = read_save_file()
    if point in points and points[point] != target and not force:
        die(f'{point}: Already set (use -f to override): {points[point]}')
    points[point] = target
    write_save_file(points)
    print('nop')

def command_rm(point=None):
    if not point:
        point = get_default_point()
    points = read_save_file()
    if point in points:
        del points[point]
    else:
        die(f'{point}: No such warp point')
    write_save_file(points)
    print('nop')

def command_version():
    print('echo')
    print('wdx 1.0-devel')

def command_help(command=None):
    if command in COMMANDS:
        print('echo')
        print(usage(command))
    elif command:
        die_raw(usage())
    else:
        print('echo')
        print(usage())

def handle_args(args):
    if not args:
        print_stderr(usage())
        raise WdxError
    command, *args = args
    if command not in COMMANDS:
        command, args = 'go', [command] + args
    _, min_args, max_args = COMMANDS[command]
    if len(args) < min_args or len(args) > max_args:
        die_raw(usage(command))
    try:
        handler = globals()[f'command_{command}']
    except KeyError:
        die('Internal error: Missing command handler')
    handler(*args)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print_stderr('wdx.py: Internal error: Not enough arguments')
        sys.exit(1)
    WDX = args[0]
    try:
        handle_args(args[1:])
        sys.exit(0)
    except WdxError as e:
        if e.message:
            print_stderr(e.message)
        sys.exit(1)
