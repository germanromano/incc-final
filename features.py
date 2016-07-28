#! /usr/bin/env python
import nltk
# import os
# os.environ['STANFORD_MODELS'] = 'stanford-postagger-full-2015-04-20/models'
# os.environ['CLASSPATH'] = 'stanford-postagger-full-2015-04-20/stanford-postagger.jar'


corpusReader = nltk.corpus.PlaintextCorpusReader('./books/','F-pg1342.txt',encoding='latin1')
sents = corpusReader.sents()

# #--------------------------------------------------------------------------
# # Total number of sentences

numberOfSentences = len(sents)

# #--------------------------------------------------------------------------
# # Average word length, Total number of words, Number of words with repeating
# # letters over number of words

numOfWords = 0
avgWordLength = 0.0
wwrl = 0.0

# #--------------------------------------------------------------------------
# # Amount of questions and exclamations

questions = 0.0
exclamations = 0.0

# #--------------------------------------------------------------------------
# # Relationship mentions, displays of affection, mentions of happiness or sadness.
# # Mentions of colors

relationships = 0.0
colors = 0.0
happiness = 0.0
sadness = 0.0
affection = 0.0


# #--------------------------------------------------------------------------
# # Average tokens per sentence, Punctuation per sentence, Female to male pronoun
# # ratio

avgTokensPerSentence = 0.0
avgPunctuationMarksPerSentence = 0.0
femPronouns = 0.0
malePronouns = 0.0

# #--------------------------------------------------------------------------
# # Mentions of children

childrenMentions = 0.0


# #--------------------------------------------------------------------------
# # FEATURE EXTRACTION

for sentence in sents:
  avgTokensPerSentence += len(sentence)

  punctuationMarks = 0
  for word in sentence:
    word = word.lower()
    if word in ",.-!?()":
      punctuationMarks += 1
      if word == "?":
        questions += 1
      elif word == "!":
        exclamations += 1
    else:
      numOfWords += 1
      avgWordLength += len(word)
      if word in ["she","her","hers","she's","she'd"]:
        femPronouns += 1
      elif word in ["he","him","his","he's","he'd"]:
        malePronouns += 1
      elif word in ["child","children","baby","babies","son","daughter"]:
        childrenMentions += 1
      elif word in ["love","lovely","marriage","enamoured","fancy","care","seduce","girlfriend","boyfriend","fiance","fiancee","engaged"]:
        relationships += 1
      elif word in ["blue","brown","yellow","green","red","purple","violet","orange","black","white","lilac","turquoise","gray","pink"]:
        colors += 1
      elif word in ["happy","happiness","joy","exultant","exaltation","ecstatic"]:
        happiness += 1
      elif word in ["sad","sadness","depression","depressed","cry","crying","tears","cried"]:
        sadness += 1
      elif word in ["hug","hugging","kiss","kissing","kissed","hugged","embrace","embracing","embraced","caress","caressing","caressed"]:
        affection += 1

      for l in word:
        if word.count(l) > 1:
          wwrl += 1
          break


avgPunctuationMarksPerSentence += punctuationMarks

avgWordLength /= numOfWords

wordsWithRepeatingLetters = wwrl / numOfWords

questions /= numOfWords

exclamations /= numOfWords

avgTokensPerSentence /= numberOfSentences

avgPunctuationMarksPerSentence /= numberOfSentences

femToMalePronounRatio = femPronouns / malePronouns

childrenMentions /= numOfWords

happiness /= numOfWords

sadness /= numOfWords

colors /= numOfWords

relationships /= numOfWords

affection /= numOfWords

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
print "Questions / total\t\t", '{:.20f}'.format(questions)
print "Exclamations / total\t\t", '{:.20f}'.format(exclamations)
print "Avg. token per sent.\t\t", avgTokensPerSentence
print "Avg. punc. marks per sent.\t", avgPunctuationMarksPerSentence
print "Numb. of fem. pronouns\t\t", femPronouns
print "Numb. of male pronouns\t\t", malePronouns
print "Fem. to male pr. ratio\t\t", '{:.20f}'.format(femToMalePronounRatio)
print "Children mentions / total\t", '{:.20f}'.format(childrenMentions)
print "Relationship mentions / total\t", '{:.20f}'.format(relationships)
print "Color mentions / total\t", '{:.20f}'.format(colors)
print "Happiness mentions / total\t", '{:.20f}'.format(happiness)
print "Sadness mentions / total\t", '{:.20f}'.format(sadness)
print "Displays of affection mentions / total\t", '{:.20f}'.format(affection)
#print "Adjectives / total\t\t", adjectives
#print "Adverbs / total\t\t\t", adverbs
#print "Nouns / total\t\t\t", nouns
#print "Cardinals / total\t\t", cardinals
