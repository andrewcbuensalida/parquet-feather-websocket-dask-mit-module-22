In this activity, you will practice defining a pandas dataframe and then writing the contents to files in parallel by using the DASK library.

To complete this activity, follow these steps:

In a Terminal window, run the command below to install the DASK library locally:

pip install dask

Provide a screenshot to show that you successfully installed DASK.
Download the Activity 22_1.py file and open it using VS Code. Provide a screenshot to show that you opened the file correctly.
In the Activity 22_1.py file, use the pandas DataFrame function to create a dataframe with two columns. The first column, odd_num, will contain, as entries, all the odd numbers between 1 and 10. The second column, even_num, will contain, as entries, all the even numbers between 1 and 10. Assign this dataframe to the pandas_df variable. Provide a screenshot to show that you created the pandas_df dataframe correctly.
In the Activity 22_1.py file, set the npartitions argument inside the from_pandas function equal to 2. Provide a screenshot to show that you set the npartitions argument equal to 2.
Run and debug your code in VS Code. Provide a screenshot to show that you ran the code without any errors.
In a Terminal window, navigate to the activity22.1 folder. List the files inside of the activity22.1 folder. Provide a screenshot to show that the 0.part and 1.part files are present inside of the activity22.1 folder.
In a Terminal window, use the cat command to visualize the contents of the 0.part and 1.part files. Provide two screenshots. The first screenshot should show the contents of the 0.part file. The second screenshot should show the contents of the 1.part file.
You have now completed this activity and practiced defining a pandas dataframe and writing the contents to files in parallel by using the DASK library.