# Introductory task

This project is an introductory, the goal is to create a server, which takes a provided string and search for it in a specific file.<br />
<br />
In order to provide high search speeds, we implemented some methods depending on a variable called REREAD_ON_QUERY.<br />
### When it is True, we need to reread the file on every query we process<br />
for that we used subprocess in order to execute a linux command => Grep.
### otherwise, We only read the file once, we chose it to be at server's start<br />
for that we used pyahocorasick as an implimentation of the Aho–Corasick algorithm.<br />
<br />

![execution speeds graph](https://i.ibb.co/r0SqnTQ/benchmarks.jpg=400x300)

# installation instructions

  $ python3 -m venv env<br />
  $ source env/bin/activate<br />
  $ pip3 install pyahocorasick<br />

# Execution

  $ python3 server.py
