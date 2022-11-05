
import pytest
import server
import ahocorasick

proper_path = '/home/one/Desktop/5_days_test/200k.txt'
malformer_path = '/home/one/Desktop/5_days_test/200k.'

def test_file_to_list():

    # test proper path
    assert isinstance(server.file_to_list(proper_path), list)

    # test wrong path
    assert server.file_to_list(malformer_path) == None

def test_search_file():

    automaton = ahocorasick.Automaton()
    for idx, key in enumerate(server.file_to_list()):
        automaton.add_word(key, (idx, key))

    ## test proper search word
    assert server.search_file('ff', automaton)[1] == 'STRING NOT FOUND\n'

    ## test proper search word
    assert server.search_file('6;0;1;26;0;7;3;0;', automaton)[1] == 'STRING EXISTS\n'

