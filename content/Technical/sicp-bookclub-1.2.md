---
layout: post
title: SICP Book Club: 1.2 (What Are Processes?)
author: Will Engler
tags: sicp
date: 2015-05-14 14:34:44
---

>In testing primality of very large numbers chosen at random, the chance of stumbling upon a value that fools the
>Fermat test is less than the chance that cosmic radiation will cause the computer to make an error in 
>carrying out a “correct” algorithm. Considering an algorithm to be inadequate for the first reason 
>but not for the second illustrates the difference between mathematics and engineering.

### Processes and Procedures

In my CS curriculum, I didn't come across the distinction between programs and processes until my first systems programming course.
The focus there was on defining a process at a systems level: i.e., a state of execution of a program with its own stack and heap. 
However, distinguishing between the blueprints that are programs and the growing, pulsing things that are processes is a good idea.

By making this distinction early on, A&S gave me a few big "Oh! Right," moments.
The biggest was when they note that recursively defined procedures do not necessarily create recursive processes.
The way they distinguish the two is helpful.
Deferred operation characterizes recursive processes.
Meanwhile, a limited number of variables that completely define the state of the process characterizes iterative processes.

A related revelation was that loops can be rewritten as recursively defined procedures.
It's obvious in hindsight, but I never stopped to think about it.

### Recursion Is The Easy Way

I always chuckle when A&S note how much easier it is to direct a recursive process than an iterative process.
I remember not seeing recursion until my second programming course.
It was presented as this crazy thing that we might not be able to wrap our heads around.
But to A&S (and the field of computer science at large), it is fundamental.
I'm not saying Pitt presented the material badly; it's just funny to see it presented so differently.

### Exercises

I was pickier this chapter.
I skipped over all of the primality testing exercises because I feel I spent enough time on that in my life already.
I just did enough to make sure I was grasping the difference between recursive and iterative processes and getting some Scheme practice.
My partial solutions are available [here](https://github.com/WillEngler/sicp-solutions/tree/master/C1/S2).