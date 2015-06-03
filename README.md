# Python-Server
This is a solution (with threading) of Socket Programming Assignment 1 from "Computer Networking A Top-Down Approach 6th ed." by James F. Kurose and Keith W. Ross.

"Assignment 1: Web Server
In this assignment, you will develop a simply Web server in Python that is capable of processing only one request. Specifically, your Web Server will (i) create a connection socket when contacted by a client (browser); (ii) receive the HTTP request from this connection; (iii) parse the request to determine the specific file being requested; (iv) get the requested file from the server's file system; (v) create an HTTP response message consisting of the requested file preceded by header lines; and (vi) send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present on your server, your server should return a "404 Not Found" error message.
    In the companion Web site, we provide the skeleton code for your server. Your job is to complete the code, run your server, and then test your server on a host that already has a Web server running on it, then you should use a different port than port 80 for your Web server."
