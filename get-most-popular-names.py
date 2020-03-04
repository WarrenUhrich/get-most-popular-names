from collections import Counter # Include the Counter function.

# Dictionary for final most-popular name storage.
topNames = {}

# Open file.
with open( 'TXBabyNames.txt' ) as file_in:
  persons = []  # List
  years = {}    # Dictionary

  # Loop through lines in file.
  for line in file_in:
    # Get year.
    year = line.split( ',' )[2]
    # Get name.
    name = line.split( ',' )[3]
    # If the year key is not there...
    if not( year in years ):
      # Add the year key.
      years[year] = []
    # Add the name to the year.
    years[year].append( name )
  # Loop through collected years, with the names.
  for y, n in years.items():
    # Get totals of name use in the year.
    counts = Counter( n )
    # Get the most popular, and store it in topNames.
    topNames[y] = list( counts.keys() )[0] # Store top name per year

# Print full list.
print( topNames )
