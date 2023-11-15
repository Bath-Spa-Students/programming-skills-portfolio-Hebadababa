rivers={'Ganga':'India','nile':'Egypt','fraser':'Canada','kuskokwim':'Alaska'}
for river,country in rivers.items():
    print("the"+river.title()+"flows through"+country.title()+".")
    print("\nthe following rivers are included in this data set:")
for river in rivers.keys():
    print("-"+river.title())
    print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("-"+country.title())