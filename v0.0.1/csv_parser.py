"""
This CSV parser is looking at the same world_factbook_resources.csv document, but is modified to pull out the following
resources:

* Iron
* Copper
* Gold

"""

import csv

with open('../world_factbook_resources.csv', 'r') as file:
	reader = csv.reader(file, delimiter=',')
	country_catalog = {}
	resources_catalog = {}
	accept = ['iron', 'copper', 'gold']
	for row in reader:
		for resource in row[1:]:
			r = resource.lstrip(' ')
			if r in accept:
				if row[0] not in country_catalog:
					country_catalog[row[0]] = []
				country_catalog[row[0]].append(r)
				if r in resources_catalog: 
					resources_catalog[r] += 1
				else:
					resources_catalog[r] = 1

	# The following print statements will print JS objects
	print country_catalog
	print resources_catalog