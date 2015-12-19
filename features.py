#! /usr/bin/env python
import nltk
import os
os.environ['STANFORD_MODELS'] = 'stanford-postagger-full-2015-04-20/models'
os.environ['CLASSPATH'] = 'stanford-postagger-full-2015-04-20/stanford-postagger.jar'


corpusReader = nltk.corpus.PlaintextCorpusReader('.','example_book.txt',encoding='latin1')
sents = corpusReader.sents()
words = corpusReader.words()

#--------------------------------------------------------------------------
# Total number of sentences

numberOfSentences = len(sents)

#--------------------------------------------------------------------------
# Average word length && Total number of words

avgWordLength = 0.0
numOfWords = 0

for w in words:
  if w not in ".,-":
    avgWordLength += len(w)
    numOfWords += 1

avgWordLength /= numOfWords

#--------------------------------------------------------------------------
# Number of words with repeating letters over number of words

wwrl = 0.0

for w in words:
  for l in w:
    if w.count(l) > 1:
      wwrl += 1
      break

wordsWithRepeatingLetters = wwrl / numOfWords

#--------------------------------------------------------------------------
# Average tokens per sentence

tokensPerSentence = [len(sentence) for sentence in sents]

avgTokensPerSentence = 0.0
for length in tokensPerSentence:
  avgTokensPerSentence += length

avgTokensPerSentence /= numberOfSentences

#--------------------------------------------------------------------------
# Punctuation per sentence

avgPunctuationMarksPerSentence = 0.0

for sentence in sents:
  punctuationMarks = 0
  for word in sentence:
    if word in ",.-!?()":
      punctuationMarks += 1
  avgPunctuationMarksPerSentence += punctuationMarks

avgPunctuationMarksPerSentence /= numberOfSentences

#--------------------------------------------------------------------------
# Number of adjectives / adverbs / nouns / cardinal numbers over total
# This is way too slow to run on every book

# Stanford POS Tagger
# nltk.internals.config_java(options='-Xmx3024m')
stTagger = nltk.tag.stanford.StanfordPOSTagger('english-left3words-distsim.tagger', 'stanford-postagger-full-2015-04-20/stanford-postagger.jar')

tagged = stTagger.tag_sents(sents)
jj = 0.0
rb = 0.0
nn = 0.0
cd = 0.0
for sent in tagged:
  for word,use in sent:
    if use == "JJ":
      jj += 1
    elif use == "RB":
      rb += 1
    elif use == "NN":
      nn += 1
    elif use == "CD":
      cd += 1
adjectives = jj / numOfWords
adverbs = rb / numOfWords
nouns = nn / numOfWords
cardinals = cd / numOfWords

#--------------------------------------------------------------------------

print [numberOfSentences, numOfWords, avgWordLength, wordsWithRepeatingLetters, avgTokensPerSentence, avgPunctuationMarksPerSentence, adjectives, adverbs, nouns, cardinals]

