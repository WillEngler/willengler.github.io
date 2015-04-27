---
layout: post
title: How Do You Tell a Number to Sit?
date: 2014-08-21 08:58:00
tags: fundamentals
---

A Great Question
-----------------

A few weeks ago, I visited an old friend from my hometown named Carly. While I went on to study technology, she studied theater. Because we’re both curious, we like to ask each other about our vastly different specialties. Carly and I were walking through the woods when she asked,

> I know that computer programs are sequences of commands. And those commands make the computer do things. But if everything inside of a computer is a number, how does a number know how to do something? I can tell a dog, “Sit,” and it will sit down. But how do you tell a number to sit? 

I explained at length and drew logic gates in the dirt with a stick. My explanation managed to be both too high-level and too low-level to clarify anything. I’m going to try again to give a concise explanation of how a computer works.

RAM Stores Words
-----------------

Ok Carly, as you well know, computers store data in bits, which can have a value of either 0 or 1. Computers group bits into _words_. How big a word is depends on the computer. You know how Atari was “8-bit” and the N64 was “64-bit”? That’s saying that _words_ on the Atari are 8 bits long and _words_ on the N64 are 64 bits long. Taken together, these words can represent anything. They can be instructions in a program, credit card numbers in a database, or cat pictures from the internet. Just like English letters have no meaning until we arrange them into words and assign definitions to them, computer words are nothing but strings of bits. Only our interpretation gives them meaning.

While a computer is running, words are stored in _RAM_: random access memory. _Random access_ means that all of the words in memory are laid out in a long array: there’s word one, word two, word three, maybe up to word two billion if you have that much RAM. Another way of saying this is that each word has an _address_. Therefore, we can ask the RAM for the word at address 672 and get just that word. If we had _sequential access_ instead of _random access_, we’d have to go through words 1 through 671 first. Random access is like selecting a scene on a DVD. Sequential access is like needing to fast forward through a VHS to get to where you want. Because a picture is worth a thousand words (Ha!), I made a crappy MS Paint drawing of how to imagine RAM.


![I am a true artist.](/images/RAM.png)
 
The CPU Processes Words
------------------------

RAM can store words, but it can’t manipulate them. For that, RAM is connected to the central processing unit (CPU). I like to think of the CPU as a machine that follows a very precise set of instructions to read in words from RAM and spit new words back into RAM. It so happens that we build CPUs by encoding these instructions into circuits. However, a detail-oriented human being could do the same job by following the instructions very carefully.

To execute a program, the CPU will request the first word of the program from RAM. The bits in that word will specify what operation the CPU should perform, what words it should perform the operation on, and where to store the result. Maybe the first 5 bits tell the CPU which operation to perform (like addition), the next 9 bits are a number to be added, the 9 bits after that are the address of a word in RAM that will be added to, and the last 9 bits are the address in RAM where the CPU should store the result. Below is a picture of an instruction encoding scheme for one kind of CPU. Don’t read into it too much. Just look at how it blocks off different parts of a word to have different meanings.


![Everyone loo0oooves MIPS.](/images/MIPS.gif)
 
A Number Cannot Sit
--------------------

So, to review, we have a device that stores words - RAM. We also have a device that can read words in from RAM and put different words back into RAM based on coded instructions inside the words - the CPU. But I still haven’t answered your question, Carly. How does a number sit? 

It doesn't. Numbers can only be numbers. But maybe the CPU is also connected to a device like a light or a motor. If that’s the case, then the CPU can send that device numerical codes in the form of an electrical signal. Maybe when the light receives the code 110 the light flashes blue and when it receives 001 it turns red. So numbers don’t sit, but they can tell other things to sit.

The Lazy Bouncer
----------------

I’d like to tie everything together with an example. Let’s say there’s a bouncer at a Pittsburgh bar who is bored of his job. He’d like to let a computer take over while he takes a break. So he connects a CPU, RAM, and an electronically controlled gate and puts it in front of the entrance. He writes a program that lets people at the door type in their age. If they’re 21 or over, the gate lets them in. The bouncer might write this program in a high level programming language that humans can read:

	if (age >= 21)
		open the gate
	if (age < 21)
		keep the gate closed

A special computer program called a compiler can translate code that looks like English into a series of words that the CPU can execute. Below is what the program might look like once it’s been turned into words. Instead of showing them as 0’s and 1’s, I’ve shown what those 0’s and 1’s would represent.

![This is an accurate reflection of my embedded systems expertise.](/images/Program.png)

So as long as the CPU knows to start reading instructions at address 2, it will execute that instruction first. If it isn’t told to move to address 4, it will automatically just execute the next instruction and stop the program. If the age is 21 or greater, then it will move to address 4 and open the gate before halting. 

Note again how important our interpretations of the numbers are. If we told the CPU to start executing instructions at address 1 instead of address 2, the CPU would interpret the customer’s age as an instruction. It would probably result in some operation we didn’t want to happen.

Disclaimer
-----------

Obviously, I have made many simplifications. But if you get the idea that computers are machines that traverse long lists of numbers and follow a strict set of rules to perform operations on those numbers, then you know more about how computers work than most people. Now you’re ready for your starring role as [Ada Lovelace][ada] or [Grace Hopper][grace]. You’re welcome.

[ada]:	http://en.wikipedia.org/wiki/Ada_Lovelace
[grace]:	http://en.wikipedia.org/wiki/Grace_hopper