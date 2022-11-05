# Introductory task

This project is an introductory task, which focuses on the creation of a server, which takes a provided string and search for it in a specific file.<br />
<br />
In order to provide high search speeds, we implemented some methods depending on a variable called REREAD_ON_QUERY.<br />
When it is True, we need to reread the file on every query we process, for that we used subprocess in order to execute a linux command - Grep.<br />
otherwise, We only read the file once, we chose it to be at server's start, and used pyahocorasick as an implimentation of ahocorasick used by Grep.<br />

# installation instructions

  $ python3 -m venv env<br />
  $ source env/bin/activate<br />
  $ pip3 install pyahocorasick<br />

# Execution

  $ python3 server.py
