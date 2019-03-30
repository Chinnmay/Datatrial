#import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import operator

tokenizer = RegexpTokenizer(r'\w+')


stop_words = set(stopwords.words('english'))

emo_results = []
emo_data  = pd.read_csv('/home/sarvasva/Documents/BE-project/Text Emotion/Emotion.csv')
main_data  = pd.read_csv('/home/sarvasva/Documents/BE-project/Text Emotion/main_data(copy).csv')
#print(main_data)
fear_words = emo_data['Fear words']
happy_words = emo_data['Happy words']
anger_words = emo_data['Anger words']
sad_words = emo_data['Sad words']
neg_words = emo_data['Negative words']
neg_words = neg_words[:16]
trigg_dataframe = main_data[['Manual Textual Emotion labelling(7 categories)', 'Combined trigger words']]
angry_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'angry']
happy_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'happy']
neutral_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'neutral']
disgust_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'disgust']
sad_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'sad']
fear_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'fear']
surprise_trigger_words = trigg_dataframe[trigg_dataframe['Manual Textual Emotion labelling(7 categories)'] == 'surprise']
angry_trigger_words = angry_trigger_words['Combined trigger words']
happy_trigger_words = happy_trigger_words['Combined trigger words']
neutral_trigger_words = neutral_trigger_words['Combined trigger words']
disgust_trigger_words = disgust_trigger_words['Combined trigger words']
sad_trigger_words = sad_trigger_words['Combined trigger words']
fear_trigger_words = fear_trigger_words['Combined trigger words']
surprise_trigger_words = surprise_trigger_words['Combined trigger words']
temp = []
for i in angry_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
angry_trigger_words = set(temp)
temp = []
for i in happy_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
happy_trigger_words = set(temp)
temp = []
for i in neutral_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
neutral_trigger_words = set(temp)
#print(neutral_trigger_words)
temp = []
for i in disgust_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
disgust_trigger_words = set(temp)
temp = []
for i in sad_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
sad_trigger_words = set(temp)
temp = []
for i in fear_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
fear_trigger_words = set(temp)
temp = []
for i in surprise_trigger_words:
	i = tokenizer.tokenize(i)
	for x in i:
		temp.append(x.lower())
surprise_trigger_words = set(temp)

def opposite_of(emotion):
#	print("in opposite_of")
	if emotion == 'sad':
		return 'happy'
	elif emotion == 'happy':
		return 'sad'	
	elif emotion == 'surprise':
		return 'neutral'	
	elif emotion == 'neutral':
		return 'surprise'
	elif emotion == 'fear':
		return 'happy'
	elif emotion == 'disgust':
		return 'happy'
	else: 
		return 'happy'		

def find_neg(w):
	for t in neg_words:
		
		if w == t:
			return True
	#print("word not found :", w)
	return False


def negation(emotion, sent, senten, index):
	v = 0
	p = 0
	if find_neg(sent[index - 1]):
		#print(sent[index - 1])
		v = -1
	if find_neg(sent[index - 2]):
		#print(sent[index - 2])
		if v == 0:
			v = -1
		else :
			v = 0

	'''for i in range(index, 0, -1):
		if sent[]

		#print(" i = " , i)
		for k in pos:
			#print(senten[i][1])
			if senten[i][1] == k:
				p = 1
		#print("p = ", p)
		#if p != 1:
		for t in neg_words:
			#print(t)
			if t == senten[i][0]:
				if v == 0:
					v = -1
				else :
					v = 0'''
	if v == 0:
		#print("emotion same = ", emotion)
		return emotion
	else:
		#print("emotio opposite_of ", emotion , opposite_of(emotion))
		return opposite_of(emotion)


for sent in main_data['Text on image (Manual)']:
	#print(image_name)
	sent = sent.lower()
	sent = word_tokenize(sent)
	senten = nltk.pos_tag(sent)
	filtered_sentence = []
	emo_words = []
	for w in sent: 
		if w not in stop_words: 
			filtered_sentence.append(w)
	#xprint(filtered_sentence)
	for w in sent: 
		#print("word is  :" , w)
		for k in anger_words: 
			if w == k: 
				emo = negation('anger', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in happy_words: 
			if w == k: 
				emo = negation('happy', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
			#emo_words.append(negation('happy', sent, senten, sent.index(w) ))
		for k in sad_words: 
			if w == k: 
				emo = negation('sad', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in fear_words: 
			if w == k: 
				emo = negation('fear', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in angry_trigger_words: 
			if w == k: 
				emo = negation('anger', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in happy_trigger_words: 
			if w == k: 
				#print(w , 'happy')
				emo = negation('happy', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in sad_trigger_words: 
			if w == k: 
				emo = negation('sad', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in neutral_trigger_words: 
			if w == k: 
				emo = negation('neutral', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in disgust_trigger_words: 
			if w == k: 
				emo = negation('disgust', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in surprise_trigger_words: 
			if w == k: 
				emo = negation('surprise', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
		for k in fear_trigger_words: 
			if w == k: 
				emo = negation('fear', sent, senten, sent.index(w))
				#print(w, emo)
				emo_words.append(emo)
	emo_results.append(emo_words)
i = 0
k = 0
p = 0
for t in emo_results:
	counts = Counter(t)
	total = len(t)
	for x in counts:
		counts[x] = (counts[x]/total)*100
	if len(counts) != 0:
		result = main_data['Manual Textual Emotion labelling(7 categories)'].iloc[i]
		if result == max(counts.items(), key=operator.itemgetter(1))[0]:
			k += 1
			#print("Sentence",t)
			print( i + 2 , max(counts.items(), key=operator.itemgetter(1))[0] )
		else:
			print("")
			#print( i + 2, " wrong ", max(counts.items(), key=operator.itemgetter(1))[0])
	else:
		p += 1
		#print( i + 2, " ************************************")
	i += 1
	#print(counts)
print("Accuracy",k / 183, p / 183)


#print(emo_results)
