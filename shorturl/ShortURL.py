import pyshorteners
from colorama import Fore



print(Fore.GREEN+"Created By "+ Fore.RED+ "RaMii Karimi\n")
link = input(Fore.GREEN+"Paste Your Link Here :")
ShortURL = pyshorteners.Shortener()

Url = ShortURL.tinyurl.short(link)


print(Url)
print("Your Link Has Been Shorted")

