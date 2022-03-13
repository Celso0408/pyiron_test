#!/bin/bash
DIR_SRC=$(dirname "$(readlink -f "$0")")
DIR_CONDA=$DIR_SRC/conda-env

if [ -d "$DIR_CONDA" ]; then
  printf "Update conda environment in ${DIR_CONDA}\n"
  conda env update --prefix $DIR_CONDA -f environment.yml --prune
else
  printf "${DIR_CONDA} not found. Create a new conda environment\n"
  conda env create --prefix $DIR_CONDA -f environment.yml
fi

printf "activate conda using\n   conda activate $DIR_CONDA\n"
printf "afterwards create ~.pyiron_config that includes the directories with the script templates \n   python .ci_support/pyiron_config.py\n"





