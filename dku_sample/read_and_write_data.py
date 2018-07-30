# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# <b>Declare libraries</b>

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Declare input and output objects
dku_input = dataiku.Dataset("westnile_data_1")
dku_output = dataiku.Dataset("transfo_py")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# <b>Transform input as Pandas Dataframe</b>
# With this method, the input data must fit into memory

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_input = dku_input.get_dataframe(sampling='head', limit=1000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_input['date'] = pd.to_datetime(df_input['date'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# <b>Here, the code to create the output Dataframe</b>

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_output = df_input

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# <b>Write results into the DSS flow</b>
# Use the schema of the Pandas Dataframe as output schema

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dku_output.write_with_schema(df_output)
