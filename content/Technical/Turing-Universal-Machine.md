---
layout: post
title: Turing's Universal Machine
author: Will Engler
tags: Turing
date: 2015-05-09 13:07:30
---

> Alan Turing's definition of programming:
>
> An activity by which a digital computer is made to do a man's will, by expressing this will suitably on punched tapes.

I'm still working through Petzold's superb _The Annotated Turing_.
I've reached an important milestone.
Turing has defined a Universal Computing Machine (which I will refer to as the Universal Turing Machine - UTM).
It can replicate the operation of any other Turing machine.
In essence, it is a programmable computer.

I'd like to trace through Turing's steps to make sure I understand them.

### Step 1: Define a Computing Machine

> We have said that the computable numbers are those whose decimals are calculable by finite means. ...
> For the present I shall only say that the justification lies in the fact that the human memory is necessarily limited.
>> Alan Turing

Turing's computing machines are simple. 
He focuses in particular on _circle-free, automatic computing machines_.
_Automatic_ means it does its work with no intervention - no run-time input.
_Computing_ means it prints a sequence of 0's and 1's that represents a binary number between 0 and 1.
_Circle-free_ means that it never terminates;
even if it is computing, say, 1/4 (.01 in binary), it will keep printing trailing 0's forever.

What does he mean by _machine_?
The machine shall operate on an infinitely long roll of paper.
The paper is divided into squares, like memory addresses.
The machine can print symbols symbols onto squares and scan symbols from them.
The machine can move left or right one square at a time.

How does the machine know where to go and what symbols to print?
A machine shall have a finite number of _m-configurations_.
An m-configuration defines which operation to perform for each possible symbol it might encounter. and what m-configuration to transition to after it has performed the operation.
Here I take operation to mean what symbol to print (if any) and which direction to move (left or right).

### Step 2: Define Helper Functions

Doing anything interesting with such a basic machine gets annoying quickly.
To lay the groundwork for the UTM, Turing introduces several notational shortcuts that can always be expanded to the original definition of a computing machine.

The most important shorthand is the _m-function_ - a sort of subroutine.
Turing takes great pains to note that there is nothing dynamic about his m-functions.
Infinite nesting of m-functions is prohibited.
I like to think of the m-functions like C++ generics.
When you're writing them, it seems like they can dispatch on an arbitrary number of types.
But really, the compiler just creates all necessary forms of your generic function at compile-time.
In a similar way, Turing's m-functions always "compile down" to a finite number of m-configurations.

With the magic of function composition in hand, Turing goes on to define some useful m-functions. 
One example is a copy and erase function that will erase all symbols "marked" with a given value and add them to the end of the tape.
What "marked" means is one of **many** implementation details I'm eliding.

Petzold's writing is gold here.
He rags on Turing for unfortunate function and variable names.
In Turing's defense, _Code Complete_ was not available in 1936.
(Fun fact:Turing casually uses function overloading to define his m-functions.
That's a luxury I don't have in Python.)

### Step 3: Encode Computing Machines As Numbers

Up to now, Turing has used tables and words to define a machine's m-configurations.
As a human, I appreciate that, but it's hard for a computer to read.

Because the definition of an m-configuration is so regular, it is straightforward to translate them into strings of symbols.
Each combination of m-configuration and currently scanned symbol maps to an operation and the next m-configuration.
So we can enumerate all such mappings as a quintuple:
the current m-configuration, the current symbol, the symbol to print, the direction to move, and the next m-configuration.
I'll call each quintuple an _instruction_.
Thus, a Turing Machine can be represented as a list of instructions, each containing five symbols.

From a list of quintuples, it is easy to substitute numbers for symbols and create a massive integer.
In this way, every Turing machine is represented by a unique integer.
Conversely, a given integer may or may not represent a valid Turing machine.
Petzold notes that this conclusion should not surprise us.
After all, executables are just long binary numbers chunked into bytes.
As software developers, we transform algorithms into integers for a living.

Interestingly, a computable number can be constructed with more than one Turing machine.
Just as there are many ways to write FizzBuzz, there are many Turing machines that compute the digits of Pi.
Thus computable sequences (and computable numbers) can be represented by more than one integer.

Already, we have an enormously important takeaway.
Turing has shown that all computable numbers can be represented as integers describing their calculation through a machine.
This, the cardinality of computable numbers is less than the cardinality of natural numbers!
He states offhandedly that "The computable numbers are thus enumerable."

Turing's lack of enthusiasm hints at bigger plans.
Now that we can represent any Turing machine as a string of characters, our programmer senses should be tingling.
You know what's good at manipulating strings of characters: Turing machines!
Turing will use the symbolic, instructional representation of Turing machines as input to the UTM.

### Step 4: Create the Universal Machine

My first reaction to Turing's definition of the universal machine was similar to my reaction to the first Scheme interpreter I saw: "That's it?"
In the original paper, the UTM only takes two pages to define.
Emil Post famously pointed out a few bugs in Turing's design, but it gets the idea across.

I didn't care to read too closely into the implementation details, but here's the main idea.
The UTM is initialized with the symbolic representation of a TM (a list of instructions), written left to right.
After the list of instructions, the UTM prints the state of the machine after the first instruction is executed -
so the _entire_ tape, the position of the current symbol, and the next m-configuration.
From the first state of execution, it can find the correct instruction to execute next and print the second state after the first.
Then the third, fourth, fifth, and so on.
If it prints out the proper 0's and 1's between each state, then it produces the same sequence as the TM it is emulating.
Voilá! A universal machine.