#!/usr/bin/env python3

# ticky_log_to_csv.py - script that takes a log file and creates two CSVs. One report has error types and their count,
# sorted from highest number of errors to lowest number, the other has user statistics on events sorted by username.
# Created to satisfy the final assessment in Course 2 of 'Google IT Automation with Python Professional Certificate'.

import re
import csv
import operator
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG) # un/comment to un/block debug log messages


def parse_log():
    """ Parses the syslog.log file and gathers the necessary information into lists to be printed. """
    error_dict = {}
    user_dict = {}
    pattern = r': (INFO|ERROR) (.*) \((.*)\)'

    with open('syslog.log', 'r') as log_file:
        for line in log_file.readlines():
            capture_groups = re.findall(pattern, line)
            main = capture_groups[0][0]
            detail = capture_groups[0][1]
            user = capture_groups[0][2]
            if user not in user_dict:
                user_dict[user] = {}
            if main == 'ERROR':
                error_dict[detail] = error_dict.get(detail, 0) + 1
                user_dict[user]['ERROR'] = user_dict[user].get('ERROR', 0) + 1
            else:
                user_dict[user]['INFO'] = user_dict[user].get('INFO', 0) + 1

    # cover use cases where users never have 'ERRORS' or 'INFO' events in their usage history.
    for user in user_dict:
        if 'INFO' not in user_dict[user]:
            user_dict[user]['INFO'] = user_dict[user].get('INFO', 0)
        if 'ERROR' not in user_dict[user]:
            user_dict[user]['ERROR'] = user_dict[user].get('ERROR', 0)

    sorted_errors = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_users = sorted(user_dict.items())
    logging.debug(sorted_errors)
    logging.debug(sorted_users)

    return sorted_errors, sorted_users


def write_csv(error_list, user_list):
    """ Takes in two lists, one for errors and one for user stats, and writes out the report CSV files """

    with open('error_log.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ERROR', 'COUNT'])
        for value in error_list:
            writer.writerow(value)

    with open('user_statistics.csv', 'w', newline='') as csv_file:
        fields = ['USER', 'ERROR', 'INFO']
        writer = csv.DictWriter(csv_file, fields)
        writer.writeheader()
        for key, value in user_list:
            row = {'USER': key}
            row.update(value)
            writer.writerow(row)


if __name__ == '__main__':
    errors, users = parse_log()
    write_csv(errors, users)
