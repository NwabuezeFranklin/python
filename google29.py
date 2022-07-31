def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for keys, values in group_dictionary.items():
		# Now go through the users in the group
		for val in values:
			user_groups.get(val,[].append(keys))
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))