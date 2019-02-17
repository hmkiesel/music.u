# music.u

dependencies:
pip install magenta
pip install midi2audio
install_fluidsynth_with_soundfonts_osx.sh


midi files are located in short_midis directory.


script to generate midi file:

melody_rnn_generate --config=attention_rnn \
--bundle_file=attention_rnn.mag \
--output_dir=generated \
--num_outputs=1 \
--num_steps=250 \
--primer_midi=short_midis/MIDI_FILE_NAME


to convert midi file to wav/flac:

  from midi2audio import FluidSynth

  midiplay fileName.mid
  midi2audio fileName.mid outFile.wav
  
  FluidSynth().play_midi('fileName.mid')   #plays the midi file
  
  #using the default sound font in 44100 Hz sample rate
  
  fs = FluidSynth()
  fs.midi_to_audio('fileName.mid', 'outFile.wav')

  #FLAC, a lossless codec, is supported as well (and recommended to be used)
  
  fs.midi_to_audio('fileName.mid', 'outFile.flac')


or as a script:

  #synthesize MIDI to audio
  
  $ midi2audio fileName.mid outFile.wav

  #also to FLAC
  
  $ midi2audio fileName.mid outFile.flac
