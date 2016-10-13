# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

Source : https://leetcode.com/problems/add-and-search-word-data-structure-design/
Author : hongxiaolong
Date   : 2016-10-12

"""


import unittest


class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in xrange(len(word)):
            w = word[i]
            if w not in node.childs.keys():
                child = TrieNode()
                node.childs[w] = child
            node = node.childs[w]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)

    def find(self, node, word):
        if word == "":
            return node.isWord

        w = word[0]
        if w == '.':
            for child in node.childs:
                if self.find(node.childs[child], word[1:]):
                    return True
        else:
            if w in node.childs:
                return self.find(node.childs[w], word[1:])

        return False


class WordDictionaryCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_word_dictionary(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        for i, o in [("pad", False),
                     ("bad", True),
                     (".ad", True),
                     ("b..", True)]:
            self.assertEqual(wd.search(i), o)


if __name__ == '__main__':
    unittest.main()
