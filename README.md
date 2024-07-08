# theAmalgam
An amalgamation of scripts I've produced that need to be tested as working in their exe format

# If Avast reports a file as a malicious, read below
I use pyinstaller to convert my Python (.py) files into Windows Executbles (.exe), "As there is a consistent binary signature across all pyinstaller executables it results in a lot of false positives. So the virus scanner 
knows that the pyinstaller wheel looks a LOT like a known Trojan." This also applies to all executables I make using pyinstaller. Meaning: Avast Anivirus may see it as a trojan and move it to "Quarantine" (as it does every time I make it XP), you can remove it from Quarantine by expanding the popup that appears when that happens, and clicking 'Open Quarantine', and clicking the 3 dots near the listed file (make sure it's the right one!) And clicking either "Restore" or "Restore and add exception". I'd recommend the latter but I would like some testing done to see if Avast ever moves the file back (in which case let me know and just add an exception)

![Unknown](https://github.com/DaBoiOnDaCouch/theAmalgam/assets/98932175/662487b0-e402-470e-97bf-1b106bc32344)

I recommend doing some research on it, it's pretty interesting stuff (to me anyway).


## If you're running Windows 10/11 Pro (which comes with additional security features)
it may also flag it as potentially malicious, just follow the instructions to run it anyway, the source code for each file is available to view and can be compiled individually if that's what you prefer (though you might still get the warnings, not sure, I'd like more testing.)


# Files List & Descriptions
## mainTXTv2 // txtReader
txtReader is somewhat self-explanatory, it can read text files in the txt format and output them to the terminal (The termianl being the mainTXTv2.exe window).
It can read files in the same directory as the exe, but it's untested whether it can read files outside of its directory.
txtReader also displays a history of recently read text files.

### Test this.
Try specifying the location of the text file you want to read in its name when using txtReader, i.e: if the exe is located in C://Users/USER/Downloads, try 'C://anotherDirectory/name.txt'.
Also try testing a single forward slash (/) after typing 'C:'.
And replacing forward slashes (/) with back slashes (\).
If it doesn't work, let me know, try running the program in administrator mode and try again.

## numGuesser
numGuesser is also pretty self-explanatory, the CPU will think of a number from 1-10, and you have to guess it in as little attempts as possible.

## YouTube (Audio) Downloader
Run the .EXE and paste the link of a YouTube video, and hit Enter, the .EXE will -if all goes correctly- download the audio from the provided link, simply close it when you're done!

### Test this.
Try using the shortened YouTube URLs, like youtu.be/ThisIsALink
Also try links specifying a timestamp, i.e: https://www.youtube.com/watch?v=lSLXS0bjSCs&t=30s
