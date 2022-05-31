"""
This script populates the character profiling ontology with the prepared data.
"""

from owlready2 import *
from pathlib import Path
import pandas as pd 

# Paths of the project
PROJECT_DIR = Path.cwd().parent
CHARACTER_PROFILING_ONTOLOGY = 'file://' + str(PROJECT_DIR) + '/ontologies/character-profiling-ontology/model.owl' # Owlready2 need RDF/XML format

# Get the pickled files
p = Path('pickled_files').glob('*.pkl')
files = [x for x in p if x.is_file()]

# Create dataframes from files
dataframes = list()
for pickled_file in files:
    unpickled_df = pd.read_pickle(pickled_file)
    dataframes.append(unpickled_df)

# Open the ontology
onto = get_ontology(CHARACTER_PROFILING_ONTOLOGY).load()

# Verify ontology loading
print(list(onto.classes()))

############################
### For a future development
############################

# Probably better to handle dataframe by dataframe, where each dataframe is a
# chapter of the Iliad book.

# 1. Generate speakers individuals
# Get speaker from the dataframes
# Write all speakers in the ontology with a loop

# 2. Generate speeches individuals
# For each speech, adjust properties
# then write each speech in the ontology
