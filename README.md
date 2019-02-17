# music.u

dependencies:
pip install tensorflow

pip install magenta

pip install midi2audio

install_fluidsynth_with_soundfonts_osx.sh



script to generate midi file:


Generating new MIDIs for 2-bar pieces after training data:

        music_vae_generate \
        --config=cat-mel_2bar_small \
        --run_dir=2bar.tar \
        --mode=sample \
        --output_dir=/result1 \
        
Generating new MIDIs based on 2 MIDI input files:

        music_vae_generate \
        --config=cat-mel_2bar_small \
        --checkpoint_file=2bar.tar \
        --mode=interpolate \
        --num_outputs=10 \
        --input_midi_1=test1.mid
        --input_midi_2=test2.mid
        --output_dir=/result1cat
        
Generating new MIDIs for 16-bar pieces after training data:
        
        music_vae_generate \
        --config=flat-mel_16bar  \
        --checkpoint_file=16bar.tar \
        --mode=sample \
        --num_outputs=5 \
        --output_dir=/result2 \
        
Generating new MIDIs based on 2 MIDI input files:

        music_vae_generate \
        --config=flat-mel_16bar \
        --checkpoint_file=16bar.tar \
        --mode=interpolate \
        --num_outputs=10 \
        --input_midi_1=n_test1.mid
        --input_midi_2=n_test2.mid
        --output_dir=/result2cat

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
