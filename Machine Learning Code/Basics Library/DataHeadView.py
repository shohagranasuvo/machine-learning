from google.colab import files
import pandas as pd
upload =files.upload()
dt=pd.read_csv(list(upload.key()[0]))
display(dt.head)
