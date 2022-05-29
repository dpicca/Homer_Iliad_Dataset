"""
This script populates the character profiling ontology with the prepared data.
"""

from owlready2 import *
from pathlib import Path
import pandas as pd 

# Paths
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

print(list(onto.classes()))

# print(onto.Emotion)