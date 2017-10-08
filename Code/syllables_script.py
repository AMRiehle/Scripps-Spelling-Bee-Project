import csv
import urllib

words = []
with open('/Users/annariehle/Desktop/Coding Projects/GA Data Science/ds-dc-21/projects/words.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		words.append(''.join(row))

def get_url(words):
	urls = []
	for word in words:
		urls.append('https://www.merriam-webster.com/dictionary/' + word)
	return urls

urls = get_url(words)

def get_syllables(url, x, y):
	syllables = []
	for link in url[x:y]:
		f = urllib.urlopen(link)
		myfile = f.read()
		start_text = myfile.find('span class="word-syllables"') + 30
		end_text = myfile.find('</span>', start_text)
		syllables_text = myfile[start_text:end_text]
		syllables.append(syllables_text)
	return syllables

def write_syllables(url, x, y):
	m = open('syllables.csv', 'a+')
	for link in url[x:y]:
		while x < y:
			m.write(str(get_syllables(url, x, x+1)) + '\n'),
			x += 1
		else:
			m.close
			break

write_syllables(urls, 1625, len(urls) - 1)