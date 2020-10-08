'''
EN
Inspired from or forked per se from https://pebbie.wordpress.com/2010/07/30/pemenggalan-suku-kata-dengan-python/

This was made due to the official KBBI having limited numbers of queries you can do.
I quote unquote improved it for my needs. There are still some imperfections but I feel like if I add more rules it'll make things complicated.

ID
Terinspirasi dari atau bisa dibilang forked dari https://pebbie.wordpress.com/2010/07/30/pemenggalan-suku-kata-dengan-python/

Ini dibuat karena KBBI resmi memiliki batasan query.
Saya dalam petik memperbagus kodenya sesuai kebutuhan saya. Masih ada ketidaksempurnaan tapi saya rasa jika saya tambah banyak aturan lagi itu hanya memperumit.
'''

vocals = list('aiueo*()-')
diftong = list('*()-')
gabungan = {'kh':'!',
			'ng':'@',
			'sy':'#',
			'ny':'$',
			'tr':'%',
			'gr':'^',
			'ai':'*',
			'ei':'(',
			'au':')',
			'oi':'-',}

def replacer(word):
	'''
	Replace the input string based on the gabungan variable
	'''
	result = word
	for letters, symbol in gabungan.items():
		result = result.replace(letters, symbol)
	return result

def unreplace(syllables):
	'''
	Unreplace the input string based on the gabungan variable
	'''
	result = []
	for syllable in syllables:
		sub_result = syllable
		for letters, symbol in gabungan.items():
			sub_result = sub_result.replace(symbol, letters)
		result.append(sub_result)
	return result

def preprocess(word):
	'''
	Split the word based on the rule:
	A consonant always has a vocal as its friend.
	'''
	result = []
	tempchar = ""
	last_consonant = False
	for letter in word:
		is_consonant = (letter not in vocals)
		if is_consonant:
			last_consonant = True
			tempchar += letter
		else:
			if last_consonant:
				# To avoid letters like 'nda' by changing it to 'n, da'
				if len(tempchar) > 1:
					result.append(tempchar[0])
					result.append(tempchar[1:] + letter)
				else:
					result.append(tempchar + letter)
				tempchar = ""
			else:
				result.append(letter)
			last_consonant = False
	# If there is an excess tempchar, dump it.
	if len(tempchar) > 0:
		result.append(tempchar)
	print(result)
	return result

def process(syllables):
	'''
	Finalize the preprocessed syllables
	'''
	result = []
	while True:
		try:
			if not contains(vocals, syllables[1]): # Checking if the next letter is a non vocal such as [ple, 'ks']
				if len(syllables[1]) == 1:
					if contains(diftong, syllables[0]): # Checking for words such as [s'ai', n] and turn it into [sa, in]
						new_word = join(unreplace(syllables[0]))
						result.append(join(new_word[:len(new_word)-1]))
						syllables.insert(0, new_word[-1])
						del syllables[1]
					else: # e.g [si, n] becomes [sin]
						result.append(join(syllables[:2]))
						del syllables[:2]
				else:
					result.append(join(syllables[:2]))
					del syllables[:2]
			elif not contains(vocals, syllables[0]):
				if not contains(vocals, syllables[2]): # Avoids [s, pe, 'k', tru, m]
					result.append(join(syllables[:3]))
					del syllables[:3]
				else:
					result.append(join(syllables[:2]))
					del syllables[:2]
			else:
				result.append(syllables[0])
				del syllables[0]
		except IndexError:
			if syllables:
				result.append(syllables[0])
				del syllables[0]
			break

	if '%an' in result:		# Special check for trans e.g tran.smi.gra.si -> trans.mi.gra.si
		indx = result.index('%an')
		try:
			if result[indx + 1][0] == 's':
				if result[indx + 1][1] not in vocals:
					result[indx] = '%ans'
					result[indx + 1] = result[indx + 1].replace('s', '')
		except IndexError:
			pass
	elif 'ek' in result:		# Special check for trans e.g ek.skre.si -> eks.kre.si
		indx = result.index('ek')
		try:
			if result[indx + 1][0] == 's':
				if result[indx + 1][1] not in vocals:
					result[indx] = 'eks'
					result[indx + 1] = result[indx + 1].replace('s', '')
		except IndexError:
			pass
	return result

def join(letters):
	'''
	Turns a list into one single string
	'''
	return ''.join(letters)

def contains(items, letters):
	'''
	Check if a string contains character from specified item
	'''
	for item in items:
		if letters.__contains__(item):
			return True
	return False


def syllabify(word):
	replaced_word = replacer(word)
	syllables = preprocess(replaced_word)
	processed_syllables = process(syllables)
	print(unreplace(processed_syllables))
	return unreplace(processed_syllables)

if __name__ == '__main__':
	word = input('Word : ')
	syllabify(word)
