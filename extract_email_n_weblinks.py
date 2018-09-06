"""
Script Written by: Abdullah Al Imran 
Website: https://abdalimran.github.io
Email: abdalimran@gmail.com
"""

import re
import sys
import os

def email_extractor(file):
	email_match = re.compile(r"[\w\.]+\@[\w]+(?:\.[\w]{3}|\.[\w]{2}\.[\w]{2})\b")
	email_list = email_match.findall(file)
	return email_list

def weblink_extractor(file):
	web_link_match = re.compile(r"https?:\/\/[\w_-]+(?:(?:\.[\w_-]+)+[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
	web_link_list = web_link_match.findall(file)
	return web_link_list

def export_list_to_file(list, file_name):
	if len(list) != 0:
		with open(file_name, 'w') as f:
			for item in list:
				item = item
				f.write('{}\n'.format(item))

if __name__ == "__main__":

	file_name, extension =os.path.basename(sys.argv[1]).split(".")

	with open(sys.argv[1], 'r') as f:
		file = f.read()

	emails = email_extractor(file)
	export_list_to_file(emails, file_name+'_emails.txt')

	links = weblink_extractor(file)
	export_list_to_file(links, file_name+'_weblinks.txt')

	print("DONE!! :D")
