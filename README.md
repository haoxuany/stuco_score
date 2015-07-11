
# StuCo Grade Manager

A REPL for StuCo grade handling. lol :sunglasses:  

## Requirements

Python 2.x (not sure, but I'm running 2.76, so it works for me, probably works for you).   
Linux/Unix/\*nix/Anything that has a command prompt running the 'clear' command.   
If you're using Windows, HAHAHAHHAHA. :laughing:  

## Command File Specification (everything you need to know)

Every command description/function must be written in SEPERATE file in the commands/ 
directory with the same name, with reasonable corresponding permissions.   
For convenience, we will call that file the 'command file'.   
(Ex. the 'quit' command should be stored in 'commands/quit.py', with chmod 755)

Every command file MUST include a 'main' function, with exactly two parameters: 'args' and 'env'.   
(Ex. In 'commands/quit.py', we have:
```python
def main(args, env):
```
)

The args parameter will be the arguments from the REPL starting AFTER the command itself,
and split into a list with corresponding strings.   
(Ex. If we call:
```
1:>> write a b     c
```
The REPL will call 'main' in 'commands/write.py' with args = ['a', 'b', 'c'].
  
Calling a command itself only will produce args = [], trimming all trailling spaces.

The env parameter will be settings read from a configuration file.   
env is of type dictionary.   
TODO: implement this.   

The main function may choose to return 0 or None (which is the default behaviour of not 
returning anything), as a default exit signal. If it returns another function, it will be
treated as a callback function, and the intepreter would continue to parse the remaining 
input from the user, and call the callback function instead to process args, env.
Hence, args, env, and the return types stated here also apply to the callback function.
If it returns anything other than 0, None, or a function, it will attempt to print the signal  

And that is all.

