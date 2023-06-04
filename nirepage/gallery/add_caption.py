import sys
import json
JSON_FILE = 'captions.json'

class Caption:
	def __init__(self, date, title, description):
		self.date = datetime.date.fromisoformat(date)
		self.title = title
		self.description = description

def add_caption(filename, title, description):

	try:
		with open(JSON_FILE, 'r') as f:
			captions = json.load(f)
	except json.decoder.JSONDecodeError:
		# If the file is empty or invalid, initialize an empty dict
		captions = {}

	datestr = filename.split('_')[0]
	datestr = datestr[:4] + '/' + datestr[4:6] + '/' + datestr[6:]

	entry = dict()
	entry['date'] = datestr
	entry['title'] = title
	entry['description'] = description

	captions[filename] = entry

	with open(JSON_FILE, 'w') as f:
		json.dump(captions, f, indent = 4)

def main():
	args = sys.argv
	if len(args) < 3:
		print("USAGE: python add_caption.py FILENAME TITLE DESCRIPTION(optional)\nFilename must start with YYYYMMDD_*")
		return -1

	description = None
	if len(args) == 4:
		description = args[3]

	add_caption(args[1], args[2], description)
	print("Done")
	return -1

if __name__ == '__main__':
	main()


