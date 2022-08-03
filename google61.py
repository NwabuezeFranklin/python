"""
In this section, we will write the body of the function named contains_domain. This function uses regex to identify the domain of the user email addresses in the user_emails.csv file.

The function takes address and domain as parameters, and its primary objective is to check whether an email address belongs to the old domain(abc.edu).

To do this, we will use a regular expression stored in the variable named domain_pattern. This variable will now match email addresses of a particular domain. If the old domain is found, then the function returns true.



The replace_domain function takes in one email address at a time, as well as the email's old domain name and its new domain name. This function's primary objective is to replace the email addresses containing the old domain name with new domain name.

In order to replace the domain name, we will use the regular expression module and make a pattern that identifies sub-strings containing the old domain name within email addresses. We will then store this pattern in a variable called old_domain_pattern. Next, we will use substitution function sub() from re module to replace the old domain name with the new one and return the updated email address.



Now store the path of the list user_emails.csv in the variable csv_file_location. Also, give a file path for the resulting updated list within the variable report_file. This updated list should be generated within the data directory.
Then, initialize an empty list where you will store the user email addresses. This is then passed to the function contains_domain, where a regular expression is used to match them and finally replace the domains using the replace_domain function.

Next, initialize the two different lists, old_domain_email_list and new_domain_email_list. The old_domain_email_list will contain all the email addresses with the old domain that the regex would match within the function contains_domain. Since the function contains_domain takes in email address passed as parameter, we will iterate over the user_email_list to pass email addresses one by one. For every matched email address, we will append it to the list old_domain_email_list.
"""


#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '/home/student-02-7525c854735d/data/user_emails.csv'
  report_file = '/home/student-02-7525c854735d/data' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()