from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess door")
    assert_equal(result, [('noun', 'bear'),
                            ('noun', 'princess'),
                            ('noun', 'door')])

def test_stops():
    assert_equal(lexicon.scan("at"), [('stop', 'at')])
    result = lexicon.scan("at in of")
    assert_equal(result, [('stop', 'at'),
                            ('stop', 'in'),
                            ('stop', 'of')])

def test_numbers():
    assert_equal(lexicon.scan("4"), [('number', 4)])
    result = lexicon.scan("3 8 5")
    assert_equal(result, [('number', 3),
                            ('number', 8),
                            ('number', 5)])
