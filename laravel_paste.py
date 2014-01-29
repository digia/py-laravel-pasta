from subprocess import call
import requests
import sys

file = sys.argv[1]

with open(file, 'r') as content_file: 
    content = content_file.read()

payload = { 'emp_tee': '', 'paste': content }

paste = requests.post('http://paste.jesse-obrien.ca', data=payload)

if not paste.status_code == requests.codes.ok:
    sys.exit("Post to paste.jesse-obrien.ca returned a " + paste.status_code)

call(['chrome-open', paste.url])

print "Done! \n" + paste.url
