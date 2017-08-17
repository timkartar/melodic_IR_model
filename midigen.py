import mido
while(1):
	name = input()
	s = 'PianoFrench/' + name + '.mid'
	mid = mido.MidiFile(s)
	print(mid.tracks)
	new = mido.MidiFile()
	track = mido.MidiTrack()
	for i in mid.tracks:
		for j in i:
			if(j.is_meta):
				track.append(j)
	new.tracks.append(track)
	for i in mid.tracks:
		if(i.name == 'Piano left'):
			new.tracks.append(i)
			break
	s = 'PianoLeft/' + name + '.mid'
	new.save(s)
	

