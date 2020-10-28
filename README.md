# Poem-Generator
Poem generator for MIT Makers Portfolio

Hi! I've never used GitHub before, so forgive me if it's all a bit messy.

The most important modules are probably Author.py and Poem.py, which writes and is the poem, respectively.
I'm sorry if it's a bit difficult to decode (pun intended), as I never really thought anyone else would be seeing it, and I'm not yet properly-versed (also a pun) in Python etiquette.
I will clean it up when I update it.

Thanks for reading and have a good day!

Emily Y



Explanation of files on here:

any txt file: lists of words. If you're interested in cool and obscure words, take a gander at the nouns, adjectives, and verbs. The articles and conjunctions are kind of boring.

PoemGenerator.py: It's sort of the UI area. It doesn't do much but set everything up.

Helper.py: It does all of the dirty work because I wanted to make the main area a little cleaner. Its main job is to set up the poem format for the Author.

Poem.py: The Poem class and all of its subclasses live here. They describe the meter, rhyme scheme, and general format of each kind of poem.

Author.py: Writes the poem! It takes an empty Poem from PoemGenerator.py and fills it with words. It is super messy, and, in the future, there will probably be different functions for each kind of poem, rather than the one-size-fits-all craziness that sort of happened as I slowly added new poem formats and the rhyming functionality.

WordList.py: A list of words that the Author can choose from. It's basically just the stuff from the text file but keeps track of meter and number of syllables. I wanted to use a pre-made Python dictionary for those fields and more, but a lot of my Cool and Obscure words don't exist in any dictionaries today, and I would be heartbroken to lose "vespertilionize" (to turn into a bat) from my vocabulary, though it would probably be for the best.

Meters.py: Just a few meters for the poems. Trochaic is my personal favorite. 
