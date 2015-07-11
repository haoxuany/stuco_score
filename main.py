#!/usr/bin/env python
# main.py - The minimalistic main repl

import os

def clear():
    os.system("clear")

def prompt_string(level):
    return str(level) + ":" + ">" * level + " "

def split_cmd(str):
    cmd = str.strip().split()
    for i in xrange(len(cmd)):
        cmd[i] = cmd[i].strip()

    return cmd

def run_command(cmd, env):
    try:
        exec("from commands import " + cmd[0])
        retval = None
        exec("retval = " + cmd[0] + ".main(cmd[1:], env)")

    except ImportError:
        print "'{cmdname}' is not found. Is it in commands/? "\
                .format(cmdname = cmd[0])
        return

    except AttributeError:
        print "'{cmdname}' has been found in commands/, yet there is no 'main' function in that file with parameter args"\
                .format(cmdname = cmd[0])

    return retval

def repl():
    level = 1
    current_cmd_pipe = None
    # TODO: add environment variable support
    env = {}

    while level > 0:
        try:
            cmd = split_cmd(raw_input(prompt_string(level)))
            if cmd == []:
                continue

            if current_cmd_pipe == None:
                run_func = run_command
            else:
                run_func = current_cmd_pipe

            signal = run_func(cmd, env)
            if signal != 0 and signal != None:
                if hasattr(signal, "__call__"):
                    current_cmd_pipe = signal
                else:
                    print "'{cmdname}' returned with SIGNAL {sig}"\
                            .format(cmdname = cmd[0], sig = signal)

        except EOFError:
            level -= 1
            if level <= 0:
                break

if __name__ == "__main__":
    clear()
    print \
'''
        StuCo score manager
'''
    repl()
    print "\n"
    pass
