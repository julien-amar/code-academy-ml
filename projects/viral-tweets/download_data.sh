#!/bin/bash

wget https://s3.amazonaws.com/codecademy-content/programs/machine-learning/cumulative-projects/twitter_classification_project.zip

unzip twitter_classification_project.zip

rm -rf .ipynb_checkpoints/ *.json

mv twitter_classification_project/*.json ./
mv twitter_classification_project/.ipynb_checkpoints ./

rm -rf __MACOSX/ twitter_classification_project/
rm twitter_classification_project.zip
