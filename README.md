# Tasha's Hideous Laughter Simulations
Decks are recorded in the CMCs list, starting with 0-cost cards (and lands).

For example, Izzet Blitz as listed at https://www.mtggoldfish.com/archetype/modern-blitz becomes [19, 25, 11, 0, 0, 4, 0, 0, 1].

19 lands, 25 1 cost cards (including 3 mutagenic growth, which costs 1 phyrexian mana), etc.

This simulation ignores possible sideboarding (because a. sideboarding usually does not change average CMC to a great extent and b. the permutations of possible changes is very high)

It then generates a graph with an 'average' bar in green. Also possible is adding bars for one or two standard deviations from the mean, to show 68% and 95% of the data (under a normal distribution)

I've commented this out, although most decks tend to present as close to a normal distribution - I may extend this in the future to fit a better distribution and get more accurate 2/3rds / 95% bars.

Cheers!
