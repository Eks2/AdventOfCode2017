def is_list_of_words_valid(word_list):
    return len(set(word_list)) == len(word_list)


def is_passphrase_valid(passphrase):
    return is_list_of_words_valid(passphrase.split())


def is_passphrase_extra_secure(passphrase):
    return is_list_of_words_valid(sort_all_words_in_list(passphrase.split()))


def number_of_valid_passphrases(filepath):
    n = 0
    with open(filepath) as f:
        for line in f:
            if is_passphrase_valid(line):
                n += 1
    return n


def sort_all_words_in_list(word_list):
    return [''.join(sorted(i)) for i in word_list]


def number_of_extra_security_valid_passphrases(filepath):
    n = 0
    with open(filepath) as f:
        for line in f:
            if is_passphrase_extra_secure(line):
                n += 1
    return n
