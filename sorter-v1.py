domains_list = []

fname = input("ENTER FILENAME : ")

with open(fname, 'r', encoding='utf-8') as f:

	for each in f:
		_ = each.strip()

		try:
			temp = '{}.txt'.format(_.split("@")[1])
			print(_ + " - " + temp)

			with open(temp, 'a+') as t:
				t.write(_ + '\n')
		except:
			print("ERROR OCCURED")

print('DONE')