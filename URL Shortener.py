"Simple enough, URL gets typed in, URL gets shortened"

import pyshorteners

#Address input
long_url = input("Enter URL to be shortened: ")

#Conversion of address
type_bitly = pyshorteners.Shortener(api_key = 'd1fbab372d3735b98a814c460c7d73fda58adacc')
short_url = type_bitly.bitly.short(long_url)

print("Shortened link is here! " + short_url)