0. Please write down the full names and netids of both your team members.
Zain Siddiqui (zas30) and Krupal Patel (kp766)

1. Briefly discuss how you implemented your recursive client functionality.
The recursive client queries the complete hostname to the root server. If a corresponding hostname entry is present within the root server, then the server sends the respective Address record stored within the DNS server back to the client. However, if a corresponding hostname is not found within the root server, then the server sends an name-server record containing the hostname to the top-level server. In this instance, when the hostname is received, we create another socket connection to the top level server and query the complete hostname to the top-level server. If a match is found, then we return the respective address record back to the client, otherwise we send an error containing the “host was not found”. Thus, this querying of the entire hostname, as a whole, mimics the recursive functionality of the client.


2. Are there known issues or functions that aren't working currently in your
 attached code? If so, explain.
After testing the code with various test cases, there seems to be no known issues with regard to the functionality of the code.

3. What problems did you face developing code for this project?
A problem we faced when developing the code was implementing the socket to the TS server in client.py, as the socket only had to be used in some instances. Originally, we had opened and closed the socket connection when needed, however this would result in abnormal functionality. However, we solved this issue by creating a socket prior to the main logic of the code, and only utilizing the socket when required. This had fixed the abnormal errors that previously occurred in the code.   

4. What did you learn by working on this project?
During this project we learned how to utilize two sockets that connect two DNS servers with a client program. Working on this project helped solidify our understanding of some of the functionality and logic that underlies DNS clients and servers. Furthermore, we obtained a better understanding of how data gets transmitted over the web through a buffer, as we had to account for data of unfixed length. Last but not least, we also learned that a DNS system as a whole is iterative as we create a socket to contact the root server then the top level server if needed individually. However, the client is recursive as we send and receive the entire hostname with the respective server. 
