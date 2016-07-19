#! /usr/bin/env python
import os
import nltk

dataset = open('dataset.txt', 'a')
books_path = './books/'

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
				# # Amount of questions

				questions = 0.0

				# #--------------------------------------------------------------------------
				# # Amount of exclamations

				exclamations = 0.0

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
					  if word == "she" or word == "her" or word == "hers":
						femPronouns += 1
					  elif word == "he" or word == "him" or word == "his":
						malePronouns += 1
					  elif word == "child" or word == "children" or word == "baby" or word == "babies" or word == "son" or word == "daughter":
						childrenMentions += 1

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

				childrenMentions /= numOfWords # OBS: Aparentemente, este numero es muy chico: siempre da cero.


				# #--------------------------------------------------------------------------
				# # DATA LOAD

				#Imprimo nombre de archivo
				dataset.write('#' + f + '\n')

				#Imprimo features
				dataset.write(str(numberOfSentences) + ',' + str(numOfWords) + ',' + str(avgWordLength) + ',' + str(wwrl) +
					',' + str(wordsWithRepeatingLetters) + ',' + str(questions) + ',' +  str(exclamations) + ',' + str(avgTokensPerSentence)+
					',' + str(avgPunctuationMarksPerSentence) + ',' + str(femPronouns) + ',' + str(malePronouns) +
					',' + str(femToMalePronounRatio) + ',' + str(childrenMentions) + ',' + str(gender) + '\n')


		except OSError:
			print f, "No file"


dataset.close()
