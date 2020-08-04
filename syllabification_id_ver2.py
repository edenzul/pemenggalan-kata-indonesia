'''
EN
This is a naive approaced I did first time not knowing any better.

ID
Ini merupakan cara naif yang saya lakukan pertama kali.
'''

vocals = list('aiueoy')
consonants = list('bcdfghjklmnpqrstvwxyz')
diftong = ['ai', 'ei', 'au', 'oi']
gabungan = ['kh', 'ng', 'sy', 'ny', 'll']

def syllabify(word):
	syllables = []
	letters = list(word)
	print('Start scan')
	while True:
		try:
			print(letters)
			#							
			#	CONSONANTS
			#							
			if letters[0] in consonants:	# C
				print('0 consonant')
				if letters[1] in vocals:		# CV
					print('1 vocal')
					if letters[2] in consonants:	# CVC
						print('2 consonant')
						if join(letters[2:4]) in ['ng', 'ny']:
							print('2-3 ng ny')
							if letters[4] in vocals:	# CV'CC'V
								print('4 vocal')
								if letters[5] in consonants:	# CV'CC'VC
									print('5 consonant')
									if letters[6:7]:
										if letters[6] in consonants:
											print('6 consonant')
											syllables.append(join(letters[:4]))
											del letters[:4]
										elif letters[6] in vocals:
											print('6 vocal')
											syllables.append(join(letters[:2]))
											del letters[:2]
									else:
										print('6 nonexist')
										syllables.append(join(letters[:2]))
										del letters[:2]
								elif letters[5] in vocals:		# CV'CC'VV
									print('5 vocal')
									syllables.append(join(letters[:2]))
									del letters[:2]
							elif letters[4] in consonants:
								print('4 consonant')
								syllables.append(join(letters[:4]))
								del letters[:4]
						else:
							if letters[3] in vocals:		# CVCV
								print('3 vocal')
								syllables.append(join(letters[:2]))
								del letters[:2]
							elif letters[3] in ['r']:
								print('3 r')
								syllables.append(join(letters[:2]))
								del letters[:2]
							elif letters[3] in consonants: # CVCC
								print('3 consonant')
								if letters[4] in ['y'] + vocals:	# CVCC'V'
									print('4 y or vocal')
									syllables.append(join(letters[:3]))
									del letters[:3]
								elif letters[4] in consonants:		# CVCCC
									print('4 consonant')
									if letters[5] in vocals:			# CVCCCV
										print('5 vocal')
										syllables.append(join(letters[:3]))
										del letters[:3]
									elif letters[5] in consonants:		# CVCCCC
										print('5 consonant')
										syllables.append(join(letters[:5]))
										del letters[:5]
					elif letters[2] in vocals:	# CVV
						print('2 vocal')
						if join(letters[1:3]) in diftong:	# C'VV'
							print('1-2 diftong')
							if letters[3] in consonants:	# C'VV'C
								print('3 consonant')
								if letters[4] in vocals:	# C'VV'CV
									print('4 vocal')
									
									syllables.append(join(letters[:3]))
									del letters[:3]
								elif letters[4] in consonants:	# C'VV'CC
									print('5 consonant')
									syllables.append(join(letters[:2]))
									del letters[:2]
							elif letters[3] in vocals:	# C'VV'V
								print('3 vocal')
								syllables.append(join(letters[:2]))
								del letters[:2]
						else:
							if letters[3] in consonants:	# CVVC
								print('3 consonant')
								if join(letters[4:5]):		# Check if not a 4 letter word
									if letters[4] in consonants:	# CVVCC
										print('4 consonant')
										syllables.append(join(letters[:2]))
										del letters[:2]
									elif letters[4] in vocals:		# CVVCV
										print('4 vocal')
										if letters[5] in consonants:
											print('5 consonant')
											syllables.append(join(letters[:2]))
											del letters[:2]
										elif letters[5] in vocals:
											print('5 vocal')
											syllables.append(join(letters[:3]))
											del letters[:3]
								else:
									syllables.append(join(letters[:2]))
									del letters[:2]
							elif letters[3] in vocals:		# CVVV
								print('3 vocal')
								if join(letters[2:4]) in diftong: # CV'VV'
									syllables.append(join(letters[:2]))
									del letters[:2]
								else:
									if letters[4] in consonants:	# CVVVC
										syllables.append(join(letters[:2]))
										del letters[:2]
									elif letters[4] in vocals:		# CVVVV
										syllables.append(join(letters[:3]))
										del letters[:3]
				elif letters[1] in consonants:	# CC
					print('1 consonant')
					if join(letters[:2]) in gabungan:		#ng ny kh sy
						print('0-1 gabungan')	
						if letters[2] in consonants:	# 'CC'C
							print('2 consonant')
							if letters[3] in vocals:		# 'CC'CV
								print('3 vocal')
								syllables.append(join(letters[:4]))
								del letters[:4]
							elif letters[3] in consonants:	# 'CC'CC
								print('3 consonant')
								syllables.append(join(letters[:2]))
								del letters[:2]
						elif letters[2] in vocals:	# 'CC'V
							print('2 vocal')
							if letters[3] in consonants:	# 'CC'VC
								print('3 consonant')
								if letters[4] in consonants:	# 'CC'VCC
									print('4 consonant')
									syllables.append(join(letters[:5]))
									del letters[:5]
								elif letters[4] in vocals:		# 'CC'VCV
									print('4 vocal')
									syllables.append(join(letters[:3]))
									del letters[:3]
							elif letters[3] in vocals:		# 'CC'VV
								print('3 vocal')
								if join(letters[2:4]) in diftong:
									syllables.append(join(letters[:4]))
									del letters[:4]
								else:
									syllables.append(join(letters[:3]))
									del letters[:3]
					else:
						if letters[2] in consonants:	# CCC
							print('2 consonant')
							if letters[2] == 'y':
								syllables.append(join(letters[:3]))
								del letters[:3]
							else:
								syllables.append(join(letters[:2]))
								del letters[:2]
						elif letters[2] in vocals:		# CCV
							print('2 vocal')
							if letters[3] in consonants:	# CCVC
								print('3 consonant')
								if letters[4] in consonants:	# CCVCC
									print('4 consonant')
									syllables.append(join(letters[:4]))
									del letters[:4]
								elif letters[4] in vocals:	# CCVCV
									print('4 vocal')
									syllables.append(join(letters[:3]))
									del letters[:3]
							elif letters[3] in vocals:	# CCVV
								print('3 vocal')
								if join(letters[2:4]) in diftong:	# CC'VV'
									print('2-3 diftong')
									if letters[4] in consonants:	# CC'VV'C
										print('4 consonant')
										syllables.append(join(letters[:5]))
										del letters[:5]
									elif letters[4] in vocals:		# CC'VV'V Impossible to happen?
										print('4 vocal')
										raise IndexError
								else:
									if letters[4] in consonants:	# CCVVC
										print('4 consonant')
										syllables.append(join(letters[:5]))
										del letters[:5]
									elif letters[4] in vocals:		# CCVVV Impossible to happen?
										print('4 vocal')
										raise IndexError
								
			
			#
			#	VOCALS
			#
			elif letters[0] in vocals:		# V
				print('0 vocal')
				if letters[1] in consonants:	# VC
					print('1 consonant')
					if letters[2] in vocals:
						print('2 vocal')
						syllables.append(letters[0])
						del letters[0]
					elif letters[2] in consonants:
						print('2 consonant')
						syllables.append(join(letters[:2]))
						del letters[:2]
				elif letters[1] in vocals:		# VV
					print('1 vocal')
					if join(letters[:2]) in diftong: # 'VV'
						print('0-1 diftong')
						syllables.append(join(letters[:2]))
						del letters[:2]
					else:
						syllables.append(letters[0])
						del letters[0]
			
		except IndexError:
			if letters:
				syllables.append(join(letters))
			print('End Scan')
			break
	
	return syllables

def join(letters):
	return ''.join(letters)

if __name__ == '__main__':
	word = input('Word : ')
	print(syllabify(word))
