# music.u

midi files are located in short_midis directory.


script to generate midi file:

melody_rnn_generate --config=attention_rnn \
--bundle_file=attention_rnn.mag \
--output_dir=generated \
--num_outputs=1 \
--num_steps=250 \
--primer_midi=short_midis/MIDI_FILE_NAME
