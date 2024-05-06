# Tasks for quickiefiles

In chronological order (top to bottom)

Mockup:

    ● Get updater and init working

    ● Get explorer working

    ● Get server working

Design:

    ● Create sample Webpages for ui

    ● Finish icon pack v0.1.0

Future plans:

    ● Password auth

    ● Get previews and file modifications in browser working
    
    ● Get multi user handling

## Plan for updater

Have a version(.txt) file locally and in git repo.
Compare them using `requests.get` and the `==` operator.
If not equal upodater will git pull.

version(.txt) is a simple plaintext file that stores it in the format x.xx.x (e.g. 1.21.3)
the first number is for each majour update e.g. a complete rewrite, the next 2 numbers is
for each update that brings a new feature or alot of bugpatches to quickiefiles. The last
digit is for minor updates like bugpatches, security fixes or optimisations.
