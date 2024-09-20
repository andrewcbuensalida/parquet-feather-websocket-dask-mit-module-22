In this activity, you will simulate running parallel operations in DASK across multiple machines.

To complete this activity, follow these steps:

In a Terminal window, run the command below to install the DASK library locally:

pip install dask

Provide a screenshot to show that you successfully installed DASK.

Depending on what operating system you are using, open the Anaconda Prompt (for Windows) or the Terminal (for Mac) and run the dask-scheduler. Provide a screenshot to show that you successfully ran the dask-scheduler.

Take note of the address of the for the dask-scheduler. Open two additional Anaconda command prompts and start two dask-worker processes. Pass the address of the dask-scheduler to each of the dask-worker processes when you run them. 
`dask-worker tcp://192.168.1.73:8786`

Provide two screenshots to show that you successfully started both of the dask-worker processes by passing the correct address to the dask-scheduler.

Create a Jupyter Notebook to simulate a client program that has complex computation. Add the following code to your Jupyter Notebook to import the required DASK libraries:

import dask.array as da
from dask.distributed import Client
Provide a screenshot to show that you created a Jupyter Notebook and successfully imported the DASK libraries.

Complete the following code to create a 50,000 by 50,000 matrix of random numbers in DASK.  Compute the mean and assign the value to the y variable:

x = da.random.random((50000, 50000))
y = da.exp(x).????
Provide a screenshot to show that you successfully executed the command to create a matrix, compute the mean, and assign the value to the y variable.

Now create a DASK client that passes the address of your dask-scheduler. Call the compute function on the y variable to instruct DASK to execute the command:

client = Client("????????")
y.??
Provide a screenshot to show that you successfully computed your calculations using DASK using the compute function.

You have completed this activity and practiced simulating running complex operations across multiple machines using DASK.