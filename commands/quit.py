#!/usr/bin/env python
# quit - Used for quitting the REPL

def main(args, env):
    if args == []:
        raise EOFError
    else:
        print "There should be no parameters after 'quit'"
        return 1
