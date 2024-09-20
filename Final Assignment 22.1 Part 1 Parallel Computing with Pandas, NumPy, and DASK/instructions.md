The final assignment for this module is divided into two parts.

In Part 1 of the final assignment, you will compare the performance of the pandas, NumPy, and DASK libraries when performing calculations. In the first section, you will be working with NumPy and DASK arrays to analyze which library is faster. In the next section, you will make the same comparison working with pandas and DASK dataframes.

Part 1 of the final assignment is worth 60 points.

To complete this assignment, follow these steps:

Download the Assignment 22.1 folder and open it using your local instance of Jupyter Notebook. There are 14 questions throughout the Jupyter Notebook for this activity. Some questions will require you to modify code, and others will require open-ended written responses.
Read the instructions and modify the code that is provided in the related cells for the following questions:
Part 1: 1, 2, 4, 5, 6, 8, 9
Part 2: 11, 13
Read the instructions and complete the open-ended questions for questions 3, 7, 10, 12, and 14. Below each cell that contains a question, you will see a Markdown cell in which you can answer that question. Responses should fully answer the question that is provided, and each response should be approximately two to three sentences.
Submission Instructions:

Your submission for this activity should be a Jupyter Notebook that includes your completed code and your open-ended responses:

Part 1: NumPy vs. DASK

Update the code cell by filling in the ellipsis to create a two-dimensional NumPy array, arr, with entries from 1 to 1,000 and dimensions 2,000 by 2,000.
Update the code cell by setting the value of the chunks argument to be equal to a tuple with elements equal to 250 and 250 to divide the NumPy array into smaller chunks, each with dimensions 250 by 250.
Describe your observations from the result that prints from running the code provided. State the size of each chunk and how many chunks the NumPy array is divided into.
Update the code cell by calling the npartitions method on the DASK array to print the number of partitions to the screen.
Update the code cell by setting the axis argument equal to 0 to sum over the rows.
Update the code cell by calling the correct DASK function to visualize how each row is summed.
Explain your observations of the graph produced by the code provided.
Update the code cell by calling the numpy_arr_chk()function and assigning the result to the num_time variable.
Update the code cell by calling the dask_arr_chk()function and assigning the result to the dask_time variable.
Describe which library performs better, NumPy or DASK, and explain your reasoning.
Part 2: Pandas vs. DASK

Update the code cell by completing the code to read the same dataset using DASK with the DASK read_csv()function.
Describe which dataframe takes longer, pandas or DASK, and explain your reasoning.
Update the code cell by setting the npartition argument inside of the from_pandas function equal to 2 and run the code cell to compare the df_pandas_big and df_dask_big dataframes.
Describe which library takes less time to run, pandas or DASK, and explain your reasoning.