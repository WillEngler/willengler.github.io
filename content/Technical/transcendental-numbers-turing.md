---
layout: post
title: Transcendental Numbers and Computability
date: 2015-05-06 06:03:00
tags: fundamentals, Turing
---

>If an a-machine prints two kinds of symbols, of which the first kind (called figures) consists entirely of 0 and 1 ... then the machine will be called a computing machine.
>> Alan Turing, _On Computable Numbers_

Now that I'm done with school, I've picked up a book that's been on my backlog for a year now: _The Annotated Turing_ by Charles Petzold.
In it, Petzold walks you through Turing's revolutionary _On Computable Numbers, With an Application to the Entscheidungsproblem_.

Petzold starts with a mix of history and background theory, going from Diophantus to Cantor's transfinite mathematics.
I thought I might be able to skip this section. 
However, I was pleasantly surprised to find I had some big gaps in my knowledge of the topology of the real numbers.

Specifically, I didn't grok that it is the transcendental numbers that make the reals uncountably infinite.
After reading this section, I remembered proving back in freshman year that one can make a bijective map from the integers to the algebraic numbers, but for whatever reason this fact didn't stick.
When I thought about the reals being dense in the rationals, I just thought, "Yeah, it's irrational numbers where things get out of hand."
But understanding that there are countably many _irrational algebraic_ numbers like the square root of two gives me a more nuanced understanding.
Given that the Entscheidungsproblem is phrased "Entscheidung ger Lösbarkeit einer diophantischen Gleichung" (Determination of the solvability of a Diophantine equation), it seems like the border between the algebraic and the transcendental will play into Turing's proof.

### Enough Numbers. I Want a Turing Machine!

I'm on to the next section now, where Turing defines and gives examples of his computing machines.
It's not a novel observation to say, "That Turing fellow sure was smart," but damn, reading this is remarkable.
Obviously, there is the brilliant conceptual breakthrough of defining a universal computing machine.
But as a programmer, I'm equally awed by his ingenuity.
I remember back in our intro to computer organization course when everyone complained about writing assembly code.
Dealing with registers seems luxurious compared to a machine that can move back and forth across one memory location at a time!
And it's a hypothetical machine, so enjoy debugging it **in your mind**!

Anyways, Alan Turing is cool, and Charles Petzold is an exceptional technical writer.
I'm only partway through it, but I recommend _The Annotated Turing_. 
