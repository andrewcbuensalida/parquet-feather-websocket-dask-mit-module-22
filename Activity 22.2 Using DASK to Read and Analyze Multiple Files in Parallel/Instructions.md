In this activity, you will practice reading multiple files in parallel using DASK. A common task for data engineers is reading and processing large numbers of files. These files can come from many sources. Some files may contain data that needs to be preprocessed and then added to a database. In other cases, large files may need to be scanned and transformed before being sent to another application. Regardless of the application, reading and analyzing files is a time-intensive and thus relatively slow task. In order to speed up this process, it is desirable to read files in parallel. DASK provides a simple and easy to implement solution for parallel processing and parallel read operations.

Prior to beginning this activity, be sure that you have watched and understood the lessons in Video 22.4 and Video 22.5. Also, ensure that you have completed Activity 22.1 as a prerequisite to this activity.

In Mini-Lesson 22.4, you should have already installed DASK on your device. Reference this mini-lesson to ensure that you have successfully installed DASK before you begin this activity.

To complete this activity, follow these steps:

First, create a folder titled Activity_22.2. Download the GenerateFilesWithDask.py file to the Activity_22.2 folder. Provide a screenshot to show the GenerateFilesWithDask.py file in the Activity_22.2 folder.

Run the GenerateFilesWithDask.py file. This should create a /data folder with some large files. Provide a screenshot to show that the /data folder has been successfully created.

Navigate out of the /data folder, within the Activity_22.2 folder, and create a new Python file called Activity22-2.py. Provide a screenshot to show the Activity22-2.py file is in the Activity_22.2 folder.

In the Activity22-2.py file, import the necessary DASK libraries using the command below:

import dask.dataframe as ddf
from dask import delayed
Provide a screenshot to show that the correct DASK libraries have been imported into the Activity22-2.py file.

Use a wildcard to read all of the files generated in the /data folder. A wildcard is a designated symbol or character which helps pattern match specific words. In this case, the * symbol directs the CSV reader to grab all files as long as the beginning starts with “data/2000” and ends with “.csv”. Add the following command to read all of the CSV files:     

df = ddf.read_csv("data/2000*.csv")
Then, display the data that you just read into the DASK dataframe using the commands below:

df.compute()
print(df.head())
Run the GenerateFilesWithDask.py Python file. Provide a screenshot to show the head of the DASK dataframe and display that the DASK dataframe correctly displays the first five rows.

Next, process the data by calculating and displaying the mean of the x column using the code below:

mean = df['x'].mean().compute()
print(f'mean: {mean}')
After you have entered the above code, run the file. Provide a screenshot of your Terminal window to show the output after you have printed the computed mean of the dataframe.

Compute the number of columns in the dataframe using the code below:

cols = len(df.columns)
print(f'columns: {cols}')
After you have entered the code above, run the GenerateFilesWithDask.py Python file again. Provide a screenshot of your Terminal window to show the number of columns in the dataframe.

Compute the number of rows in the dataframe using the code below:

rows = len(df.index)
print(f'rows:{rows}')
After you have entered the code above, run the GenerateFilesWithDask.py Python file again. Provide a screenshot of your Terminal window to show the number of rows in the dataframe.