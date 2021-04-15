from shutil import copyfile
import datetime
from urllib.request import urlopen
import urllib
import os
import shutil

print("-----------------------------------------------------------------------------------")
print(" Hawke.one - Trakt Sync - Add server")
print("-----------------------------------------------------------------------------------")

print ("What would you like to do?")
print (" 1: Remove all existing server configs and re-add Hawke.one")
print (" 2: Add a new server alongside your existing configs")
print (" 3. Cancel")
ConfigChoice = input('\n Please enter your choice (1-3): ')

if ConfigChoice == "1":
   if os.path.exists(".env"):
      os.remove(".env")
   if os.path.exists(".pytrakt.json"):
      os.remove(".pytrakt.json")
   shutil.rmtree('configs')
   os.mkdir('configs')
   print ("\nRemoving existing server configs... Done!")
   print ("Resetting...\n")
   import main

elif ConfigChoice == "2":
   if os.path.exists(".env"):
      os.remove(".env")
   if os.path.exists(".pytrakt.json"):
      os.remove(".pytrakt.json")
   print ("\nCommencing new server config. \nPlease let the initial sync complete in order to succesfully add the server.\n")   
   import main
   if os.path.exists("configs/.env - 2"):
         if os.path.exists("configs/.env - 3"):
            if os.path.exists("configs/.env - 4"):
                if os.path.exists("configs/.env - 5"):
                   print("You are already syncing your maximum 5 servers, and this configuration will not be saved.")
                else:
                   copyfile('.env', 'configs/.env - 5')
                   copyfile('.pytrakt.json', 'configs/.pytrakt.json - 5')
                   print("Your new server has been configured and saved as Server 5.")
                   print("You have now reached your maximum of 5 servers.")
            else:
              copyfile('.env', 'configs/.env - 4')
              copyfile('.pytrakt.json', 'configs/.pytrakt.json - 4')
              print("Your new server has been configured and saved as Server 4")
              print("You can add 1 more server.")
         else:
           copyfile('.env', 'configs/.env - 3')
           copyfile('.pytrakt.json', 'configs/.pytrakt.json - 3')
           print("Your new server has been configured and saved as Server 3")
           print("You can add up to 2 more servers.")
   else:
        copyfile('.env', 'configs/.env - 2')
        copyfile('.pytrakt.json', 'configs/.pytrakt.json - 2')
        print("You new server has been configured and saved as Server 2")
        print("You can add up to 3 more servers.")
elif ConfigChoice == "3":
    exit()

# ConfigChoice = input('\nPress Enter to exit setup')