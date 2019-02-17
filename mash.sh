#!/bin/bash

 music_vae_generate \
    --config=flat-mel_16bar \
    --checkpoint_file=16bar.tar \
    --mode=interpolate \
    --num_outputs=10 \
    --input_midi_1=$1 \
    --input_midi_2=$2 \
    --output_dir=Uploaded/