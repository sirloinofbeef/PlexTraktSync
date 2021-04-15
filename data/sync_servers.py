from shutil import copyfile
import datetime
from urllib.request import urlopen
import urllib
import os
import sys


# ------------- START VERSION CHECK ------------------------
data = urlopen("https://raw.githubusercontent.com/sirloinofbeef/PlexTraktSync/master/data/plex_trakt_sync/version.txt")
vlatest = data.readline().decode('utf8').rstrip()

with open('plex_trakt_sync/version.txt') as f: vinstalled = f.readline()

if 'b' in vinstalled:
   print("You are using a beta: v" + vinstalled)
elif vlatest == vinstalled:
    print("You are using the latest version: v" + vinstalled)
else:
    print("An update is available!\nInstalled: v" + vinstalled + "\nNew:       v" + vlatest + "\n\nPlease update from https://github.com/sirloinofbeef/PlexTraktSync/wiki\n")
# ------------- END VERSION CHECK ------------------------

# ------------- START CACHE WARNING ----------------------
try:
    with open('trakt_cache.sqlite') as f:
        print()
except IOError:
    print("\n")
    print("   ****************************************************************************")
    print("   *  As you have yet to complete a full sync a cache has yet to be created.  *")
    print("   *  THE INTIAL SYNC MAY TAKE UP TO 12 HOURS!                                *")
    print("   *  Subsequent syncs will be MUCH faster.                                   *")
    print("   *                                                                          *")
    print("   ****************************************************************************\n")
# ------------- END CACHE WARNING ----------------------


# ----- Start If lone config exists then backup as hawke config ----------------------

def BackupHawkeConfig():
   if os.path.exists("configs/.env - hawke"):
          print ("")
   else:
      print ("No Hawke.one config found. Running setup..")
      if os.path.exists(".env"):
             copyfile('.env', 'configs/.env - hawke')
             print("Creating Hawke.one config.. Done!")
             copyfile('.pytrakt.json', 'configs/.pytrakt.json - hawke')
      else:
        print("-----------------------------------------------------------------------------------")
        print(" Hawke.one - Trakt Sync - setup")
        print("-----------------------------------------------------------------------------------")
        exec(open("main.py").read())

# ----- End If lone config exists then backup as hawke config ---------------------

BackupHawkeConfig()

f = open("last_synced_server.txt", "r")
last_synced_server = (f.read())

if last_synced_server == "hawke": sync_server = "2"
if last_synced_server == "2": sync_server = "3"
if last_synced_server == "3": sync_server = "4"
if last_synced_server == "4": sync_server = "5"
if last_synced_server == "5": sync_server = "hawke"

if os.path.exists("configs/.env - " + sync_server):
        if os.path.exists(".env"): os.remove(".env")
        if os.path.exists(".pytrakt.json"): os.remove(".pytrakt.json")
        copyfile('configs/.env - ' + sync_server, '.env')
        copyfile('configs/.pytrakt.json - ' + sync_server, '.pytrakt.json')
        today = datetime.datetime.now()
        print("-----------------------------------------------------------------------------------")
        print(" Server " + sync_server + " - Trakt Sync started on " + str(today.strftime("%B %d %Y at %H:%M:%S")))
        print("-----------------------------------------------------------------------------------")
        print("Connecting to server..")
        exec(open("main.py").read())

        f = open("last_synced_server.txt", "w")
        f.write(sync_server)
        f.close()

        if sync_server != "5": 
           os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
        else:
           input("\nProcess complete! Press Enter to exit. ")
else:
        f = open("last_synced_server.txt", "w")
        f.write("5")
        f.close()
        input("\nProcess complete! Press Enter to exit. ")