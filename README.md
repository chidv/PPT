# PPT
Pattern Processing Tool

We always find it difficult to process very large text/log files and fetch only necessary information from it. 
This tool can be used to process a very large text/log file, fetch necessary information from it and store it in a variable of user's own choice. Once the required data is retrieved and stored in a variable, then it will be easier to group them as a dataset which can even be input to ML algorithms.

What to input to this tool ?
===============================

This tool requires two input files.
      1. patterns.txt
      2. log.txt
      
You need to write the patterns.txt file (sample given below). This file is used as an input in procecssing the log.txt file.

How to write patterns.txt file ?
================================

<exact pattern string to match>$ {<variable_name>, <delimiter - space/eol>}

Example of using space
----------------------

1. To get the authentication timeout present in the following log output.

28   Authentication Timeout                      11546      6167

You may write the patterns as follows

Authentication Timeout ${auth_timeout_count, space}

Then, auth_timeout_count variable value is set as 11546

2. To get multiple data from a single line.

IOT_COUNT:                       351840                 203483                     3517

IOT_COUNT:$ {activation_count,space} {acti_duration, space} {rejected_devices, space}


Example of using eol
--------------------
1. To get the counter value in the following output

Current IOT device authenticated count is 351840
Current IOT device rejected count is 3517

Current IOT device authenticated count is:$ {auth_count, eol}







