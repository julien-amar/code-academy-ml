#!/bin/bash

mkdir tmp/

cd tmp/

wget https://s3.amazonaws.com/codecademy-content/programs/machine-learning/capstone/capstone_starter.zip

unzip capstone_starter.zip

mv *.csv ../

cd ..

rm -rf tmp/
