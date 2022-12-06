"Simple enough, URL gets typed in, URL gets shortened"

import pyperclip
import pyshorteners

#Get Bitly API Key from local file
with open('C:/Users/Cocada/Desktop/Github/Hello-World/URLShortener/MyKey.txt') as f:
    BitlyKey = f.read()

#Address input
long_url = input("Enter URL to be shortened: ")

#Conversion of address
type_bitly = pyshorteners.Shortener(api_key = BitlyKey)
short_url = type_bitly.bitly.short(long_url)

#Copy link to clipboard
pyperclip.copy(short_url)

#Print new (shortened) URL
print("Shortened link is here: " + short_url)