# Hawke.one Plex-Trakt-Sync
Version 1.3 - released 9/04/2021  

This project adds a two-way-sync between trakt.tv and hawke.one. 
It requires a trakt.tv account, but no Plex premium or Trakt VIP subscriptions.

## Download & install
Download the latest version from our [wiki](https://github.com/sirloinofbeef/PlexTraktSync/wiki) and follow the installation procedure.

## Features

 - Media in Plex are added to Trakt collection
 - Ratings are synced (if ratings differ, Trakt takes precedence)
 - Watched status are synced (dates are not reported from Trakt to Plex)
 - Liked lists in Trakt are downloaded and all movies in Plex belonging to that
   list are added
 - You can edit the data/config.json file (it's just plain text) to choose what to sync
 - None of the above requires a Plex Pass or Trakt VIP membership.

## Notes

 - The first execution of the script will take a long time. 
   After that, movie details and Trakt lists are cached, so it should run 
   quicker. Large sections (such as TV Shows) will still take a significant time.

 - The PyTrakt API keys are not stored securely, so if you do not want to have
   a file containing those on your harddrive, you can not use this project.
