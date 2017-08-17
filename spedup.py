import mido

mid = mido.MidiFile('PianoFrench/elise.mid')
print(mid.tracks)
new = mido.MidiFile()
track = mido.MidiTrack()
track.append(mido.MetaMessage('set_tempo',tempo=867303,time=0))
new.tracks.append(track)
track = mid.tracks[1]
new.tracks.append(track)
new.save('elise_right.mid')
