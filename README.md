# Ticky-Log-Reports
Consists of two scripts: ticky_log_to_csv.py and csv_to_html.py to generate easily viewable reports in HTML files from a log file.

# ticky_log_to_csv.py
Takes a log file, in this case 'syslog.log' and uses it to generate two sorted CSV files, one csv report has error types and their count, sorted from highest number of errors to lowest, the other has user statistics on events (number of 'INFO' and 'ERROR' events) sorted by username.

# csv_to_html.py
Opens a csv file provided as an argument and creates an HTML file presenting the csv data in neatly arranged rows for easy viewing.

The log file, generated CSV files, and resulting HTML files are all included for visualization.

Here is an example of how the tables look in the HTML file:

![alt text](https://github.com/Cambuchi/Ticky-Log-Reports/blob/main/table_example.jpg?raw=true)

Created to satisfy the final Qwiklabs assessment in in the coursera course "Using Python to Interact with the Operating System" for Google's IT Automation with Python Professional Certificate.
