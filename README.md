# Wordle Helper
A helper program for playing wordle

## Demo
Run [demo](https://replit.com/@ChalosChen/wordle-helper-1#.replit) on online IDE

1. Click run to show the help text.
2. Open .replit file to change the arguments. 

   Example: 
   * You want to find wordlist that 3rd word is A, the rest is unknown: argument will be: `--pattern __A__`
   * You want to exclude characters B,C,D,E,F,G from search: argument will be: `--exclude bcdefg`
   * The .replit result will be:
   ````
   language = "python3" 
   run = "python find.py --pattern __A__ --exclude bcdefg"
   ````
   * After click run, `wordlist_filter.txt` will be generated.
   
