import os
import re
from typing import Union
# from functools import reduce
# import operator


file_name = "{dir}/data/day-07.txt".format(dir=os.path.dirname(__file__))

FileDir = tuple[bool, int, str]
Command = tuple[str, str, list[FileDir]]


class FileDirNode:
    def from_file(f: FileDir, parent):
        _, size, name = f
        val = FileDirNode(name, parent, size)
        return val

    def from_dir(f: FileDir, parent):
        _, _, name = f
        return FileDirNode(name, parent)

    def __init__(self, name: str, parent: Union['FileDirNode', None], size=0) -> None:
        self.name = name
        self.parent = parent
        self.size = size
        self.files, self.dirs = [], []

    def __repr__(self) -> str:
        return f'{self.name} ({self.size})'

    def update_files(self, files: list[FileDir]):
        self.files = list(map(lambda f: FileDirNode.from_file(f, self),
                              filter(lambda f: f[0] == False, files)))
        self.dirs = list(map(lambda f: FileDirNode.from_dir(f, self),
                             filter(lambda f: f[0] == True, files)))
        self.size = sum(map(lambda f: f.size, self.files))

    def get_dir(self, name: str) -> 'FileDirNode':
        for dir in self.dirs:
            if dir.name == name:
                return dir
        return None

    def calc_size(self) -> int:
        return self.size + sum(map(lambda dir: dir.calc_size(), self.dirs))

    def all_subdirs(self) -> list['FileDirNode']:
        subdirs = list(map(lambda dir: dir.all_subdirs(), self.dirs))
        return self.dirs + [dir for inner_subdirs in subdirs for dir in inner_subdirs]


class FileTree:
    def __init__(self, log: list[str]) -> None:
        self.commands = parse(log)
        self.root = None
        self.path = []

    def _run_commands(self, commands: list[Command]) -> None:
        for command in commands:
            cmd, param, files = command
            if cmd == "cd":
                if param == "..":
                    self.path.pop()
                else:
                    if self.root is None:
                        dir = FileDirNode(param, None)
                        self.root = dir
                    else:
                        dir = self.path[-1].get_dir(param)
                    self.path.append(dir)
            elif cmd == "ls":
                self.path[-1].update_files(files)

    def run(self):
        self._run_commands(self.commands)
        pass


def parse(tokens: list[str], idx: int = 0) -> list[Command]:
    commands = []
    while idx < len(tokens)-1:
        command, idx = parse_command(tokens, idx)
        commands += [command]
    return commands


def parse_additional_params(tokens: list[str], idx: int) -> tuple[list[FileDir], int]:
    file_re = '(\d+) (\S+)'
    dir_re = 'dir (\S+)'
    if idx >= len(tokens) or tokens[idx].startswith("$"):
        return [], idx

    file_match = re.search(file_re, tokens[idx])
    dir_match = re.search(dir_re, tokens[idx])

    if file_match != None:
        (size, name) = file_match.groups()
        more_params, new_idx = parse_additional_params(tokens, idx+1)
        return [(False, int(size), name)] + more_params, new_idx

    if dir_match != None:
        (name, ) = dir_match.groups()
        more_params, new_idx = parse_additional_params(tokens, idx+1)
        return [(True, 0, name)] + more_params, new_idx


def parse_command(tokens: list[str], idx: int) -> tuple[Command, int]:
    command_re = '\$ (\S+)\s?(\S*)'
    (command, param) = re.search(command_re, tokens[idx]).groups()

    if command == "ls":
        additional, idx = parse_additional_params(tokens, idx+1)
        return (command, param, additional), idx
    else:
        return (command, param, []), idx+1


def items() -> list[str]:
    with open(file_name, "rt") as file:
        return [item
                for item
                in file.read().splitlines()]


f = FileTree(items())
f.run()
# print(f.root.calc_size())

# task1
all_subdirs = []
print(sum(
    filter(
        lambda size: size <= 100000,
        map(lambda dir: dir.calc_size(), f.root.all_subdirs())
    )
))

# task 2
disk_size = 70000000
total_used = f.root.calc_size()
free_now = disk_size-total_used
need_to_free = 30000000 - free_now

big_enough = filter(lambda size: size >= need_to_free,
                    (sorted(map(lambda dir: dir.calc_size(),
                                f.root.all_subdirs()), reverse=True)))
print(list(big_enough)[-1])
