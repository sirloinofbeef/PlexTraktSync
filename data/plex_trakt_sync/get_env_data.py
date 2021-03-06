from plexapi.myplex import MyPlexAccount
from plex_trakt_sync import util
import trakt.users
import webbrowser
import getpass
import stdiomask
import platform

from plex_trakt_sync.config import CONFIG
from plex_trakt_sync.path import pytrakt_file


def get_env_data():
    trakt.core.CONFIG_PATH = pytrakt_file
    print("")
    #plex_needed = util.input_yesno("Are you logged into hawke.one with your Plex account? (almost certainly yes)")
    plex_needed = 1
    if plex_needed:
        username = input("    Please enter your Plex username: ")
        password = stdiomask.getpass(prompt="    Please enter your Plex password: ")

        print("\nNext we will need your server name:\n\n    The server name is displayed top left (under the library title) when viewing a library on that server:\n    https://app.plex.tv/desktop \n\n    For Hawke.one your server name will most likely be one of the following:")
        print("     1) plex1.hawke.one (usually for Golden Company)")
        print("     2) plex2.hawke.one (usually for Nightswatch)")
        print("     3) plex3.hawke.one (usually for Kings Guard")
        print("     4) plex4.hawke.one (usually for Nightswatch)")
        servername = input("\n    Please select you server (1-4), or enter your custom server name: ")
        if servername == "1": servername = "plex1.hawke.one"
        if servername == "2": servername = "plex2.hawke.one"
        if servername == "3": servername = "plex3.hawke.one"
        if servername == "4": servername = "plex4.hawke.one"
        print("    Verifying server...")
        account = MyPlexAccount(username, password)
        plex = account.resource(servername).connect()  # returns a PlexServer instance
        token = plex._token
        users = account.users()
        if users:
            print("\n    The following managed Plex user(s) were found:")
            for user in users:
                if user.friend is True:
                    print("     * " + user.title)
            print(" ")
            name = input("    To use your " + username + " account, press enter (else enter the name of a managed user): ")
            while name:
                try:
                    useraccount = account.user(name)
                except:
                    if name != "_wrong":
                        print("Unknown username!")
                    name = input("Please enter a managed username (or just press enter to use your main account): ")
                    if not name:
                        print("Ok, continuing with your account " + username)
                        break
                    continue
                try:
                    token = account.user(name).get_token(plex.machineIdentifier)
                    username = name
                    break
                except:
                    print("    Impossible to find the managed user \'" + name + "\' on this server!")
                    name = "_wrong"
        CONFIG["PLEX_USERNAME"] = username
        CONFIG["PLEX_TOKEN"] = token
        CONFIG["PLEX_BASEURL"] = plex._baseurl
        CONFIG["PLEX_FALLBACKURL"] = "http://localhost:32400"

        print("    User {} configured successfully.".format(username))
        # print("PLEX_TOKEN={}".format(token))
        # print("PLEX_BASEURL={}".format(plex._baseurl))
    else:
        CONFIG["PLEX_USERNAME"] = "-"
        CONFIG["PLEX_TOKEN"] = "-"
        CONFIG["PLEX_BASEURL"] = "http://localhost:32400"

    trakt.core.AUTH_METHOD = trakt.core.DEVICE_AUTH
    print("\n\n")
    print("Now we'll setup the Trakt part of things:")
    print(" ")
    print("    Create the required Trakt client ID and secret by completing the following steps:")

    

    if platform.system() == "Windows":
        print("      1 - Press enter below to open http://trakt.tv/oauth/applications")
        print("      2 - Login to your Trakt account")
        print("      3 - Press the NEW APPLICATION button")
        print("      4 - Set the NAME field = hawke.one (or something else meaningful)")
        import pyperclip
        pyperclip.copy("urn:ietf:wg:oauth:2.0:oob")
        print("      5 - Set the REDIRECT URL field = urn:ietf:wg:oauth:2.0:oob (This has been copied to your clipboard for you)")
        input("\n    Press Enter to open http://trakt.tv/oauth/applications and complete steps 1-6: ")
        webbrowser.open('http://trakt.tv/oauth/applications')
    else:
        print("      1 - Open http://trakt.tv/oauth/applications on any computer")
        print("      2 - Login to your Trakt account")
        print("      3 - Press the NEW APPLICATION button")
        print("      4 - Set the NAME field = hawke.one")
        print("      5 - Set the REDIRECT URL field = urn:ietf:wg:oauth:2.0:oob")

    print("      6 - Press the SAVE APP button")

    print("\n    Once steps 1-6 are completed, please proceed to steps 7-8 below:\n")

    #client_id, client_secret = trakt.core._get_client_info()
    client_id = input("      7 - Copy and paste the displayed Client ID: ")
    client_secret = input("      8 - Copy and paste the displayed Client secret: ")


    if platform.system() == "Windows":
            input("\n    We will now generate a user code and open https://trakt.tv/activate for you to authenticate the app.\n    Press Enter to continue...")
            webbrowser.open('https://trakt.tv/activate')
            print("\n")

    trakt.init(client_id=client_id, client_secret=client_secret, store=True)
    trakt_user = trakt.users.User('me')
    CONFIG["TRAKT_USERNAME"] = trakt_user.username

    print("\n\n")
    print("You're all done!\n")
    print("Plex / Trakt accounts may be altered by re-running setup, or deleting the .env and .pytrakt.json files.")
    print("Expert settings may also be altered within the config.json file.")
    print(" ")
    print(" ")

    CONFIG.save()
