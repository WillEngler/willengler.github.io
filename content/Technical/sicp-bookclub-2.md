---
layout: post
title: SICP Book Club: 2 (What Are Data Structures?)
author: Will Engler
tags: sicp
date: 2015-05-16 15:26:30
---

>The names `car` and `cdr` persist because simple combinations like `cadr` are pronounceable.
>>Abelson & Sussman

>I really hope you're joking.
>>Will Engler

A few months ago, Pitt's [Computer Science Club](http://www.pittcsc.org) held a programming contest.
When it was over, one of the contestants asked the organizers to look over a solution he couldn't get to work.
The problem required a sort.
Instead of using a Java library, he had written his own sorting algorithm.
"Why didn't you use the Java collections library here?" my friend Pete asked him.
The contestant explained that because the data he needed to sort weren't numeric, he needed his own algorithm.
Pete and I told him that he could write a custom comparator function and pass it to a sort function.
He looked at us, cocked his head, and laughed in our faces.
"Pass a function to a _function_?"

That story illustrates why this chapter wasn't as compelling to me as the first.
While the first chapter focuses on combining procedures, the second focuses on combining data.
Function composition is not emphasized at Pitt, but data composition is our bread and butter.

That's not to say this chapter is trivial.
It takes chutzpah to go from the ability to `cons` two pieces of data together to building a type system.
And there are some really nice exercises that would be good practice for classic data structures 'n algorithms coding interviews.

For me, the most interesting part of the chapter was when they introduced the type system by "tagging" data
and then introduced data-directed programming and message passing.

The treatment of list operations like map and fold was also well-done.
Again, I feel pretty comfortable there, as those operations are what got me saying 
"Hey, maybe I should look more closely at this functional programming thing," in the first place.

I'm rushing a bit because I want to pursue other programming projects but I hate having too many ongoing projects at once.
I'll probably move fast through chapter 3 as well and then slow down to write an interpreter in chapter 4, which is what I came for in the first place.
I might fold in my current interest in Rust by making a Scheme interpreter in it.