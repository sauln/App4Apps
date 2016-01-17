import re
f = open('corpus_finance.txt', 'r')
x = f.read()
f.close()
f = open('corpus_finance.txt', 'w')
#removes all text in between brackets in file
x = re.sub('<[^>]+>', '', x)
#x = re.sub('"[^>]+"', '', x)
x = x.lower()
x = x.split('\n')
for line in x:
    if not ":" in line and not "disclaimer" in line and not '"' in line and not "update" in line and not "/" in line and not "**" in line and not "---" in line and not "instructions" in line and not "note" in line:
        f.write(line + '\n')
        print line + '\n'

