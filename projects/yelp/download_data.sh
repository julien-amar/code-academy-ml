#!/bin/bash

wget https://s3.amazonaws.com/codecademy-content/programs/machine-learning/cumulative-projects/yelp_regression_project.zip

unzip yelp_regression_project.zip

rm -rf .ipynb_checkpoints/ *.json

mv yelp_regression_project/*.json ./
mv yelp_regression_project/.ipynb_checkpoints ./

rm -rf __MACOSX/ yelp_regression_project/
rm yelp_regression_project.zip
