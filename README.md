# Introductory task

This project is an introductory, the goal is to create a server, which takes a provided string and search for it in a specific file.<br />
<br />
In order to provide high search speeds, we implemented some methods depending on a variable called REREAD_ON_QUERY.<br />
### When it is True, we need to reread the file on every query we process<br />
for that we used subprocess in order to execute a linux command => Grep.
### otherwise, We only read the file once, we chose it to be at server's start<br />
for that we used pyahocorasick as an implimentation of the Aho–Corasick algorithm.<br />
<br />

## Server Benchmarks
![execution speeds graph](https://i.ibb.co/r0SqnTQ/benchmarks.jpg=400x300)
<br />

The Tests results provided here, are done with testing 8000 requests / second on different file sizes.

# installation instructions
Aside from pyahocorasick, there's no additional libraries to install, still if you want to run it in a venv, do:<br />

  $ python3 -m venv env<br />
  $ source env/bin/activate<br />
  $ pip3 install pyahocorasick<br />

# Execution
Make sure to modify the config.py variables, if all is set, Do: <br />
  $ python3 server.py<br />
<br />
you will be needing a client script,which connects and provide the string to search for to the server
