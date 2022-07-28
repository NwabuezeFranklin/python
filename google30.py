def email_list(domains):
	emails = []
	for keys, users in domains.items():
	  for user in users:
	  	userfull = user + '@' + keys
	  	emails.append( userfull)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))