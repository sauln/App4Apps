
import markov.markov_chain as markov

mc = dict()

categories = [ "business", "education", "finance", "test"]

for each in categories:
	mc[each] = markov.load_dictionary(each)


print("it worked!")
