seconds = 7340
print("seconds is",seconds)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print( hour,"hours",minutes,"minutes",seconds,"seconds")
