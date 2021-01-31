


from github import Github


# or using an access token
g = Github("")
path = "elBichon/webex_experiments"

repo = g.get_repo(path)
print(repo.get_topics())
print(repo.stargazers_count)


open_issues = repo.get_issues(state='open')
for issue in open_issues:
	print(issue)

labels = repo.get_labels()
for label in labels:
	print(label)

contents = repo.get_contents("")
for content_file in contents:
	print(content_file)
