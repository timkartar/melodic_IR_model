import mido
for i in range(198):
	name = input()
	s = 'PianoRight/' + name + '.mid'
	try:
		mid = mido.MidiFile(s)
	except IOError :
		pass
	txtname = 'Piano_right_texts/' + name + '.txt'
	f = open(txtname,'a')
	for msg in mid.tracks[0]:
		if(msg.type == 'note_on'):
			dic  = msg.dict()
			#print(''.join([str(dic['note']),str(dic['time'])]))
			if(dic['velocity'] != 0):
				f.write(''.join([str(dic['note']),'\n']))
	f.close()
