---
layout: post
title: SICP Book Club: 3 (How Do We Organize Programs?)
author: Will Engler
tags: sicp
date: 2015-05-18 09:15:30
---

>We can model the world as a collection of separate, time-bound, interacting objects with state, 
or we can model the world as a single, timeless, stateless unity. 
Each view has powerful advantages, but neither view alone is completely satisfactory.
>> Abelson & Sussman

For anyone who enjoys following object-oriented vs. functional programming flamewars, this is the chapter of SICP to focus on.
If I have a friend who asks me, "Why should I care about functional programming?" I'll likely direct them here.

### Assignment and the Environment Model of Evaluation

Section 3.1 introduces assignment.
The next three sections deal with the aftermath.

I've known that - ceteris paribus - mutability makes programs harder to reason about, but this chapter really made that fact hit home.
Up until now, A&S had presented the "substitution model of evaluation" as the mental model readers should use when examining programs.
With the exception of special forms like conditional statements, you recursively evaluate subexpressions, substituting expressions with their values as you move up the tree. 
However, the death of referential transparency explodes the substitution model.
All of a sudden, we need to think about _time_.

So we need a new model, the "environment model."
The environment model comes close to my mental model of how programming languages work (namely Python, the one I'm most familiar with now).
Programs must be executed in some "global environment" that is probably defined by the interpreter.
This environment is where the primitive definitions of the language are bound (e.g, + means addition).
Top-level definitions also live in the global environment.
Definitions within a procedure live in their own environment that descend from the global environment.
Expressions evaluated in that environment will first look for variable bindings there before looking up to the global environment.
 
As a long time OO guy, I find it pleasantly mind-blowing when they casually introduce closures as a way to encapsulate state.
(Interestingly, they don't use the word closure.
They prefer to reserve the term for its more strict abstract algebraic usage:
when an operation on two members of a group always results in a member of the group.
This comes up in Chapter 2 when they note that `cons`'ed pairs are closed under `cons`'ing.
You can keep combining pairs in Scheme. 
Meanwhile, you can't arbitrarily combine arrays in C, so C arrays are not closed under array construction.)

### The Challenges and Opportunities of Mutability

In section 3.3, A&S ask how we can use the new power of assignment to model data.
They introduce some classic OO concepts like mutators and selectors.
Eventually, they introduce Discrete Event Simulation as an example of an application where it's helpful to represent stateful objects.
 
I made a mental note to come back to the section on constraint-based programming some day.
It seems so interesting and I'm entirely unfamiliar with it, but I didn't want to go down that rabbit hole.

In section 3.4 they address an issue that is hopefully old news to us by now: 
writing concurrent programs with shared mutable state is hard.
Are A&S the ones who first used the bank account example to illustrate data races?
If not them, then who?

### PLOT TWIST: Streams

And here is where my head cracked open and grew a few sizes.
State and encapsulation... without mutability? Woah dude.
At this point in my life, I don't have a burning desire to become a great LISP programmer,
so I'm trying to soak up the concepts without doing the exercises in Scheme.
But from what I can gather, Rust has pretty good support for writing programs in this style, so I'll play with it there. 

Until I write something nontrivial with streams, I don't want to talk at length about them.
For now I'll say that I'm closer to grasping why infinite lists in, say, Haskell, aren't just a parlor trick and why iterators and `yield` statements in Python are a big deal.

So with that, I add "do cool things with streams" to my to-do list and I move on to the metacircular evaluator!