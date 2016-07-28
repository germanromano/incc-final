#! /usr/bin/env python
import os
import nltk

dataset = open('datasetWithFeeling.txt', 'a')
books_path = '../books/'

def outformat(f):
	return '{:.20f}'.format(f)

for root, dirs, filenames in os.walk(books_path):
	for f in filenames:
		try:
			if f.endswith(".txt") and f[0:2] in ["F-","M-"]:

				print f

				if f[0] == "F":
					gender = 0
				else:
					gender = 1

				corpusReader = nltk.corpus.PlaintextCorpusReader(books_path, f, encoding='latin1')
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
				dreams = 0.0


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
				      elif word in ["love","lovely","marriage","enamoured","fancy","seduce","girlfriend","boyfriend","fiance","fiancee","engaged","wedding","wedded","married","wife","husband","spouse"]:
				        relationships += 1
				      elif word in ["blue","brown","yellow","green","red","purple","violet","orange","black","white","lilac","turquoise","gray","pink"]:
				        colors += 1
				      elif word in ["happy","happiness","joy","exultant","exaltation","ecstatic"]:
				        happiness += 1
				      elif word in ["sad","sadness","depression","depressed","cry","crying","tears","cried"]:
				        sadness += 1
				      elif word in ["hug","hugging","kiss","kissing","kissed","hugged","embrace","embracing","embraced","caress","caressing","caressed"]:
				        affection += 1
				      elif word in ["dream","fantasy","dreamed","nightmare","fantasize","imagination","imagine","dreams"]:
				      	dreams += 1

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

				dreams /= numOfWords

				# #--------------------------------------------------------------------------
				# # DATA LOAD

				#Imprimo nombre de archivo
				dataset.write('#' + f + '\n')

				#Imprimo features
				dataset.write(str(numberOfSentences) + ',' + str(numOfWords) + ',' + outformat(avgWordLength) + ',' + outformat(wwrl) +
					',' + outformat(wordsWithRepeatingLetters) + ',' + outformat(questions) + ',' +  outformat(exclamations) + ',' + outformat(avgTokensPerSentence)+
					',' + outformat(avgPunctuationMarksPerSentence) + ',' + str(femPronouns) + ',' + str(malePronouns) +
					',' + outformat(femToMalePronounRatio) + ',' + outformat(childrenMentions) +
					',' + outformat(happiness) + ',' + outformat(sadness) + ',' + outformat(relationships) + ',' + outformat(colors) + ',' +
					outformat(affection) + ',' + outformat(dreams) + ',' + str(gender) + '\n')

		except OSError:
			print f, "No file"
		except ZeroDivisionError:
			print f, "ZERO DIVISION ERROR"

dataset.close()
