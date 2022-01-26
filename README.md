# Wordle Helper
A helper program for playing wordle

## Demo
Run [demo](https://replit.com/@ChalosChen/wordle-helper-1) on replit

1. Click run to show the help text on console.
2. On console, enter the command to run the wordle helper.

   Example: 
   * You want to find wordlist that 3rd word is A, the rest is unknown: argument will be: `--pattern __A__`
   * You want to exclude characters B,C,D,E,F,G from search: argument will be: `--exclude bcdefg`
   * The .replit result will be:
   ````
   > python find.py --pattern __A__ --exclude bcdefg
   ````
   * After enter the command, click the `Show files` button, possible answers will be on the `wordlist_filter.txt` file.
   
