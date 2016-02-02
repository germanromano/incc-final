#! /usr/bin/env python
import nltk
import os
os.environ['STANFORD_MODELS'] = 'stanford-postagger-full-2015-04-20/models'
os.environ['CLASSPATH'] = 'stanford-postagger-full-2015-04-20/stanford-postagger.jar'


corpusReader = nltk.corpus.PlaintextCorpusReader('.','example_book.txt',encoding='latin1')
sents = corpusReader.sents()
words = corpusReader.words()

# #--------------------------------------------------------------------------
# # Total number of sentences

numberOfSentences = len(sents)

# #--------------------------------------------------------------------------
# # Average word length, Total number of words, Number of words with repeating
# # letters over number of words

numOfWords = 0
avgWordLength = 0.0
wwrl = 0.0


for w in words:
  if w not in ".,-":
    numOfWords += 1
    avgWordLength += len(w)
  for l in w:
    if w.count(l) > 1:
      wwrl += 1
      break

avgWordLength /= numOfWords

wordsWithRepeatingLetters = wwrl / numOfWords


# #--------------------------------------------------------------------------
# # Average tokens per sentence, Punctuation per sentence, Female to male pronoun
# # ratio

avgTokensPerSentence = 0.0
avgPunctuationMarksPerSentence = 0.0
femPronouns = 0.0
malePronouns = 0.0


for sentence in sents:
  avgTokensPerSentence += len(sentence)

  punctuationMarks = 0
  for word in sentence:
    word = word.lower()
    if word in ",.-!?()":
      punctuationMarks += 1
    if word == "she" or word == "her" or word == "hers":
      femPronouns += 1
    if word == "he" or word == "him" or word == "his":
      malePronouns += 1
  avgPunctuationMarksPerSentence += punctuationMarks

avgTokensPerSentence /= numberOfSentences

avgPunctuationMarksPerSentence /= numberOfSentences

femToMalePronounRatio = femPronouns / malePronouns

# #--------------------------------------------------------------------------
# # Number of adjectives / adverbs / nouns / cardinal numbers over total
# # This is way too slow to run on every book

# # Stanford POS Tagger
# # nltk.internals.config_java(options='-Xmx3024m')
# stTagger = nltk.tag.stanford.StanfordPOSTagger('english-left3words-distsim.tagger', 'stanford-postagger-full-2015-04-20/stanford-postagger.jar')

# tagged = stTagger.tag_sents(sents)
# jj = 0.0
# rb = 0.0
# nn = 0.0
# cd = 0.0
# for sent in tagged:
#   for word,use in sent:
#     if use == "JJ":
#       jj += 1
#     elif use == "RB":
#       rb += 1
#     elif use == "NN":
#       nn += 1
#     elif use == "CD":
#       cd += 1
# adjectives = jj / numOfWords
# adverbs = rb / numOfWords
# nouns = nn / numOfWords
# cardinals = cd / numOfWords


# #--------------------------------------------------------------------------
# # Prints

print "Numb. of sentences\t\t", numberOfSentences
print "Numb. of words\t\t\t", numOfWords
print "Avg. word lenght\t\t", avgWordLength
print "Numb. of words w rep. letters\t", wwrl
print "Perc. of words w rep. letters\t", wordsWithRepeatingLetters
print "Avg. token per sent.\t\t", avgTokensPerSentence
print "Avg. punc. marks per sent.\t", avgPunctuationMarksPerSentence
print "Numb. of fem. pronouns\t\t", femPronouns
print "Numb. of male pronouns\t\t", malePronouns
print "Fem. to male pr. ratio\t\t", femToMalePronounRatio
#print "Adjectives / total\t\t", adjectives
#print "Adverbs / total\t\t\t", adverbs
#print "Nouns / total\t\t\t", nouns
#print "Cardinals / total\t\t", cardinals
