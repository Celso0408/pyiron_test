#!/bin/bash
# Absolute path to this script
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in
SCRIPTPATH=$(dirname "$SCRIPT")
DIR_CONDA=$SCRIPTPATH/conda-env


if [ -d "$DIR_CONDA" ]; then
  printf "Update conda environment in ${DIR_CONDA}\n"
  conda env update --prefix $DIR_CONDA -f environment.yml --prune
else
  printf "Error: ${DIR_CONDA} not found. Create new conda environment\n"
  conda env create --prefix $DIR_CONDA -f environment.yml
fi

DIR_TEMPLATES=$DIR_CONDA/share/pyiron/templates
DIR_TENSILETEST=$DIR_TEMPLATES/tensiletest
mkdir -p $DIR_TENSILETEST
cp $SCRIPTPATH/script.py $DIR_TENSILETEST/.
cp $SCRIPTPATH/input.json $DIR_TENSILETEST/.

printf "activate conda using\n   conda activate $DIR_CONDA\n"