# Hawke.one Plex-Trakt-Sync

This project adds a two-way-sync between trakt.tv and hawke.one. 
It requires a trakt.tv account, but no Plex premium or Trakt VIP subscriptions.

## Download & install
Download the latest version from our [wiki](https://github.com/sirloinofbeef/PlexTraktSync/wiki) and follow the installation procedure.

## Features

 - **Two way Trakt - Plex sync without the need for a Plex Pass or Trakt VIP membership!**
 - Media in Plex can be added to Trakt collection _(Option disabled by default)_
 - Ratings can be synced (if ratings differ, Trakt takes precedence) _(Option disabled by default)_
 - Watched status can be synced (dates are not reported from Trakt to Plex) _(Option enabled by default)_
 - Liked lists in Trakt are downloaded and all movies in Plex belonging to that list can be added _(Option disabled by default)_

## Notes

 - The first execution of the script will take a long time. 
   After that, movie details and Trakt lists are cached, so it should run 
   quicker. Large sections (such as TV Shows) will still take a significant time.

 - The PyTrakt API keys are not stored securely, so if you do not want to have
   a file containing those on your harddrive, you can not use this project.
