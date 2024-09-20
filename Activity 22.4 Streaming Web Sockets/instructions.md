In this module, you learned about streaming data implementation strategies and how web sockets are beneficial in implementing live data connection apps.

In this activity, you will implement web socket communication by using the Python sockets library. Through the steps of this activity, you will execute packet transfer from server to client to help you better understand how packets can be created by putting the message length as a header.

To complete this activity, follow these steps:

Download and extract the Python code from the johntango Streaming GitHub repository Links to an external site.to your local machine. Provide a screenshot to show that you have successfully downloaded and extracted the johntango Streaming GitHub repository on your local machine.

Open the streamServer.py file in VS Code. Provide a screenshot to show that you successfully opened the streamServer.py file in VS Code.

To start a web socket server, execute the python streamServer.py command from the Terminal window in VS Code. This will not print anything until the client connects to the server. Provide a screenshot to show that you successfully opened the command prompt in the streamServer.py folder and ran the python streamServer.py command without errors.

For Windows users:

If you are prompted, allow the private networks execution permissions to access web communication port, as shown in the image below:

Allowing private networks execution permissions for Windows security settings.
To start a web socket client, open a new command line interface in the VS Code Terminal and execute the python streamClientEx1.py command from the Terminal. This will establish a connection with the server and receive packets from the server. Provide a screenshot to show that you successfully opened the command prompt in the streamClientEx1.py folder, ran the python streamClientEx1.py command, and received the message from the server.

Review the server console that indicates that the connection has been established and shows that packets that are being sent to the client. Provide a screenshot to show that after running the client code, you can view the sent messages output over the server command line interface.

To review another client communication, open a new command line interface in the VS Code Terminal and execute the python streamClient01Soln.py command from the Terminal. This will establish another connection with the server and receive packets from the server. Provide a screenshot to show that you successfully opened the command prompt in the streamClient01Soln.py file, ran the python streamClient01Soln.py command, and can view the received message from the server.

Open the streamClient01Soln.py file. Add a debugging checkpoint at line 13 and run the code to debug it. Provide a screenshot to show that you successfully opened the client code in the streamClient01Soln.py folder and added a debugging checkpoint at line 13.

The previous step will establish a connection with the server and receive packets from the server. The variables listed in the left panel in VS Code when debugging your code show that the value of the Python msg variable is “'29       The ti'”. Provide a screenshot to show that you were able to run the client code in debugging mode and see that the value of the Python msg variable is “'29       The ti'” in VS Code.

You have now completed this activity and practiced implementing web sockets using the socket library.