# The PAIN of Genanki

I am having a lot of trouble debugging the `genanki` python package. I am running into a couple errors that I have yet to resolve, so I am putting together this document in order to capture my findings. Ideally, I will be able to submit a pull request back to the owner of the repository in order to improve their documentation.

## Problems

 - I must manually upload a .apkg package to Anki. I believe this should be automatic (with the program running - including an addon), however, the documentation makes reference to something called `mw` which is not further specified.
    - This refers to the line `from aqt import mw  # main window`

 - I get database errors, and the deck gets wiped out whenever I upload my new package to Anki manually.
    - based on this thread, it appears there are two conclusions that I can reach about Anki:
        - genanki is creating notes without cards in the .apkg file
        - The importer will accept corrupt data
