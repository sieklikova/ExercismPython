"""Functions for creating, transforming, and adding prefixes to strings."""

word = ['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word
print(add_prefix_un(word[0]))
print(add_prefix_un(word[1]))
print(add_prefix_un(word[2]))
print(add_prefix_un(word[3]))
print(add_prefix_un(word[4]))
print(add_prefix_un(word[5]))

vocab_word = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
def make_word_groups(vocab_words):
    prefix = vocab_words[0] # nejdřív si stanovíme prefix
    prefixed_word = [ prefix + word for word in vocab_words[1:] ]
    return prefix + ' :: ' + ' :: '.join(prefixed_word)
print(make_word_groups(vocab_word))

vocab_word = ['pre', 'serve', 'dispose', 'position', 'requisite', 'digest',
              'natal', 'addressed', 'adolescent', 'assumption', 'mature', 'compute']
def make_word_groups(vocab_words):
    prefix = vocab_words[0] # nejdřív si stanovíme prefix
    prefixed_word = [ prefix + word for word in vocab_words[1:] ]
    return prefix + ' :: ' + ' :: '.join(prefixed_word)
print(make_word_groups(vocab_word))

vocab_word = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
              'echolalia', 'encoder', 'biography']
def make_word_groups(vocab_words):
    prefix = vocab_words[0] # nejdřív si stanovíme prefix
    prefixed_word = [ prefix + word for word in vocab_words[1:] ]
    return prefix + ' :: ' + ' :: '.join(prefixed_word)
print(make_word_groups(vocab_word))

vocab_word = ['inter', 'twine', 'connected', 'dependent', 'galactic', 'action',
              'stellar', 'cellular', 'continental', 'axial', 'operative', 'disciplinary']
def make_word_groups(vocab_words):
    prefix = vocab_words[0] # nejdřív si stanovíme prefix
    prefixed_word = [ prefix + word for word in vocab_words[1:] ]
    return prefix + ' :: ' + ' :: '.join(prefixed_word)
print(make_word_groups(vocab_word))


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    root = word[:-4]
    if root.endswith('i'):
        return root[:-1] + 'y'
    return root
print(remove_suffix_ness('heaviness'))
print(remove_suffix_ness('sadness'))
print(remove_suffix_ness('softness'))
print(remove_suffix_ness('crabbiness'))
print(remove_suffix_ness('lightness'))
print(remove_suffix_ness('artiness'))
print(remove_suffix_ness('edginess'))

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    return sentence.split()[index] + 'en'

print(adjective_to_verb('Look at the bright sky.', -2))
print(adjective_to_verb('His expression went dark', -1))
print(adjective_to_verb('The bread got hard after sitting out.', 3))
print(adjective_to_verb('The butter got soft in the sun.', 3))
print(adjective_to_verb('Her eyes were light blue.', 3))
print(adjective_to_verb('The morning fog made everything damp with mist.', -3))
print(adjective_to_verb('He cut the fence pickets short by mistake.', 4))
print(adjective_to_verb('Charles made weak crying noises.', 2))
print(adjective_to_verb('The black oil got on the white dog.', 1))

