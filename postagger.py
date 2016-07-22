#! /usr/bin/env python
import os
import nltk
os.environ['STANFORD_MODELS'] = 'stanford-postagger-full-2015-04-20/models'
os.environ['CLASSPATH'] = 'stanford-postagger-full-2015-04-20/stanford-postagger.jar'

dataset = open('postagger_results.txt', 'a')
books_path = './books/'
counter = 0
pending = []

for root, dirs, filenames in os.walk(books_path):
  last_book = len(filenames) - 1
  for f in filenames:
    # print f
    try:
      if f.endswith(".txt") and f[0:2] in ["F-","M-"]:
        corpusReader = nltk.corpus.PlaintextCorpusReader(books_path,f,encoding='latin1')
        sents = corpusReader.sents()

        pending.append((f, sents, sents.__len__()))
        counter += 1
        if counter % 3 == 0 or counter == last_book:
          print "HELLO"
          # #--------------------------------------------------------------------------
          # # Number of adjectives / adverbs / nouns / cardinal numbers over total
          # # This is way too slow to run on every book individually

          # # Stanford POS Tagger
          # # nltk.internals.config_java(options='-Xmx3024m')
          stTagger = nltk.tag.stanford.StanfordPOSTagger('english-left3words-distsim.tagger', 'stanford-postagger-full-2015-04-20/stanford-postagger.jar')

          full_text = pending[0][1]
          for (file_name,book,length) in pending[1:]:
            full_text += book
          tagged = stTagger.tag_sents(full_text)

          sent_count = 0
          num_of_words = 0
          current_book = pending[0]
          current_index = 0
          jj = 0.0
          rb = 0.0
          nn = 0.0
          cd = 0.0

          for sent in tagged:
            sent_count += 1
            if sent_count - 10 < current_book[2] and sent_count + 10 > current_book[2]:
              print sent_count, current_book[2]
            for word,use in sent:
              num_of_words += 1
              if use == "JJ":
                jj += 1
              elif use == "RB":
                rb += 1
              elif use == "NN":
                nn += 1
              elif use == "CD":
                cd += 1

            if sent_count == current_book[2]:
              adjectives = jj / num_of_words
              adverbs = rb / num_of_words
              nouns = nn / num_of_words
              cardinals = cd / num_of_words
              print current_book[0]
              print adjectives, adverbs, nouns, cardinals

              jj = 0.0
              rb = 0.0
              nn = 0.0
              cd = 0.0
              sent_count = 0
              current_index += 1
              if current_index < len(pending):
                current_book = pending[current_index]
          #     # #Imprimo nombre de archivo
          #     # dataset.write('#' + current_book[0] + '\n')

          #     # #Imprimo features
          #     # dataset.write(str(adjectives) + ',' + str(adverbs) + ',' + str(nouns) + ',' + str(cardinals) + '\n')

          pending = []

    except OSError:
      print f, "No file"
    except ZeroDivisionError:
      print f, "ZERO DIVISION ERROR"

dataset.close()
