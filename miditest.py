import mido
for i in range(210):
	#name = input()
	#s = '../../../Music/bengali_midis/' + name + '.mid'
	#s = 'generated/' + name + '.mid'
	try:
		name = input()
		s = 'PianoFrench/' + name + '.mid'
		mid = mido.MidiFile(s)
		print(str(mid.tracks[0].name))
	except IOError or EOFError:
		pass
	maxidx = 0
	for j in range(len(mid.tracks)):
		if(mid.tracks[j].name == 'Piano right'):
			maxidx = j
			break
	#command = "touch " + name + ".txt"
	#for msg in mid.tracks[maxidx]:
	#	print(msg)#,dicmsg['note'],dicmsg['time']
	track = mid.tracks[maxidx]
	new = mido.MidiFile()
	new.tracks.append(track)
	s = 'PianoRight/' + name + '.mid'
	new.save(s)

#m = mido.Message('note_on', note=60)
#print(m.note)

##print(mido.parse(mid.tracks[3]))

#msg = mid.tracks[3][23]
#print(msg.dict()['note'])

#for i in mid.tracks[0]:
#	print(i)

#for msg in mid.tracks[3]:
#	if(msg.type == 'note_on'):
#		print(msg.dict()['note'],msg.dict()['time'])

#track = mid.tracks[3]
#new = mido.MidiFile()
#new.tracks.append(track)
#new.save('new.mid')
#print(new.tracks)
