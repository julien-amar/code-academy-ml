#!/bin/bash

wget https://s3.amazonaws.com/codecademy-content/programs/machine-learning/cumulative-projects/masculinity_project.zip

unzip masculinity_project.zip

rm -rf .ipynb_checkpoints/ *.{csv,pdf}

mv masculinity_project/*.{csv,pdf} ./
mv masculinity_project/.ipynb_checkpoints ./

rm -rf __MACOSX/ masculinity_project/
rm masculinity_project.zip
