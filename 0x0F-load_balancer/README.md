# 0x0F Load balancer :wrench:

At the end of this project, I was able to:

* Improve a web stack so that there is redundancy for our web servers. 
* Accept more traffic by doubling the number of web servers.
* Make a infrastructure more reliable. 

## Tasks :heavy_check_mark:

0. Bash script that configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
1. Bash script that install and configure HAproxy on your lb-01 server.
2. Automating the task of creating a custom HTTP header response, but with Puppet based on script 0
