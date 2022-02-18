# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from zipfile import ZipFile
from io import BytesIO
#import fnmatch

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
Sharepoint = dataiku.Folder("ekNWzma4")
Sharepoint_info = Sharepoint.get_info()
paths = Sharepoint.list_paths_in_partition()

zipped_file = 'zippedFolder.zip'

with Sharepoint.get_download_stream(zipped_file) as stream:
    zipObj = ZipFile(BytesIO(stream.read()))
    file_list = zipObj.namelist()
    print(file_list)
    csv_file = file_list
    
    data = zipObj.open(*csv_file)

df = pd.read_csv(data,encoding='ISO-8859–1')


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

Dataiku_unzipped_df = df


# Write recipe outputs
Dataiku_unzipped = dataiku.Dataset("Dataiku_unzipped")
Dataiku_unzipped.write_with_schema(Dataiku_unzipped_df)