import csv

with open('world_factbook_resources.csv', 'r') as file:
	reader = csv.reader(file, delimiter=',')
	country_catalog = {}
	resources_catalog = {}
	for row in reader:
		country_catalog[row[0]] = row[1:]
		for resource in row[1:]:
			r = resource.lstrip(' ')
			if r in resources_catalog: 
				resources_catalog[r] += 1
			else:
				resources_catalog[r] = 1
	# print country_catalog
	# print resources_catalog
	for r in resources_catalog:
		print "%s: %s" % (r, resources_catalog[r])
	print len(resources_catalog)