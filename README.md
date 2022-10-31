# Gene Translation

We're going to start by writing a program in translate_DNA.pythat uses a given DNA sequence, and translates it to its complement sequence using the base-pair complement rules. Your job is to translate the given DNA sequence, which will be provided as a TextGrid, like this:

Change A to T
Change T to A
Change G to C
Change C to G

Here is an example. Let's take the following text grid, which represents one sequence in the genome for COVID-19:
ATTAA
AGGTT

After running python translate_DNA.py on the TextGrid, your result will be:
TAATT
TCCAA
