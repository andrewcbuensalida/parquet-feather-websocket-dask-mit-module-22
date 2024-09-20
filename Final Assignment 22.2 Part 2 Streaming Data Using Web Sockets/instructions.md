In this module, you learned about streaming data implementation strategies and how web sockets are beneficial in implementing live data connection applications.

In Part 2 of the final assignment, you will implement web socket communication by using the Python sockets library. Through the steps of this activity, you will execute packet transfer from server to client to help you better understand how packets can be created by putting the message length as a header.

Part 2 of the final assignment is worth 40 points.

To complete this activity, follow these steps:

Download and extract the Assignment22.2 folder to your local machine. Provide a screenshot to show that you have successfully downloaded and extracted the Assignment22_2 folder on your local machine.

Open the streamServer.py file in VS Code. Change the port number to 7000. Provide a screenshot to show that you successfully opened the streamServer.py file in VS Code and changed the port number to 7000.

To start a web socket server, execute the python streamServer.py command from the Terminal window in VS Code. This will not print anything until the client connects to the server. Provide a screenshot to show that you successfully opened the command prompt in the streamServer.py folder and ran the python streamServer.py command without errors.

For Windows users:

If you are prompted, allow the private networks execution permissions to access web communication port, as shown in the image below:

Allowing private networks execution permissions for Windows security settings.
Modify line 21 in the streamServer.py file to call the thread_time()function from the time library. This function returns the value of the sum of the system and user CPU time of the current thread in fractional seconds. Provide a screenshot to show that you correctly modified the code in the streamServer.py file to call the thread_time()function from the time library.

Open the streamClient.py file in VS Code Terminal and change the port to the correct one. Provide a screenshot to show that you successfully opened the streamClient.py file in VS Code and that you changed the port correctly.

Run the python streamClient.py command in a new Terminal window. This will establish another connection with the server and receive packets from the server. Note that you will need to change the port number to the same one that you used for the streamServer.py file. Provide two screenshots. The first screenshot should show that you successfully ran the streamClient.py file. The second screenshot should show that the server is receiving messages from the client.

You have now completed this activity and practiced implementing web sockets using the socket library.