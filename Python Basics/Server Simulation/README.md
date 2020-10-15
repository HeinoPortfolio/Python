# IS211_Assignment5
Commands to run the program:

For one server:

python simulation.py --file http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv

For more than one server:

python simulation.py --file http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv --servers 2





The results that I was able to see that there is an overall reduction in the average latency time.  The simulation with one server took the longest and as you added more and more servers the times began to drop off.  If you were to extend the number of servers to the amount of items in the request queue there obviously be absolutely no latency to speak.  The reason for the drop in latency time as the number of servers is increased is because the load is no distributed across many servers as opposed to just the one.  So as jobs are processed in around robin fashion the wait time is diminished because the server is not receiving a request at every second.  So there is a little leeway between when the first request is recieved and when the next.  This lag aids in reducing the amount of time the request is in the servers queue.  

To recap as the number of available servers increases the amount of latency is reduced becasue you have more servers working on the requests.  
