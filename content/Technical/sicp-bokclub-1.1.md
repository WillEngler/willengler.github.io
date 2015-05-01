---
layout: post
title: SICP Book Club: 1.1 (What Is Programming?)
author: Will Engler
tags: sicp
date: 2015-05-01 09:52:44
---

>Scheme is an easy language to learn once you get over your fear of parentheses.
>> [Scheme Community Wiki](http://community.schemewiki.org/?scheme-faq-general)

This section shouldn't be strenuous reading for the members of this book club, but don't think you should skip it!
 
On display are two pedagogical techniques A&S use that I admire.
First, they lay out in clear terms how to conceive of evaluation ("the substitution model") and then stress that it's merely a model, that we'll examine more accurate models later.
Second, they explain aspects of Scheme not as divine truths from on high but as design decisions.
They show how normal-order evaluation could also be used for a certain class of problems and explain why applicative-order was chosen instead.

I also appreciate definitions of concepts like block structure and lexical scoping. 
I understood them intuitively but couldn't put a name to them until now.

### Exercises

My code and short answers for this section are [here](https://github.com/WillEngler/sicp-solutions/tree/master/C1/S1).

The early exercises feel like the start of a Metroid game. 
You know you're going to get more powerful tools soon, but right now you just have a skimpy little gun.
The constraints can force you to be creative, but it can also be annoying.

Take for example Exercise 1.5:

>Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.

I wanted to find the two smallest arguments and then just do computation on those.
However, I haven't "unlocked" simple data structures like lists or tuples yet, so I had no way to do that.
Here's what I did instead. It feels dirty.

```Scheme
; Is candidate no greater than x and y?
(define (smallest? candidate x y) 
  (and (<= candidate  x) (<= candidate y)))

(define (sum-of-squares x y) (+ (square x) (square y)))

(define (sum-of-squares-of-two-largest x y z)  
  (cond ((smallest? x y z) (sum-of-squares y z))
        ((smallest? y x z) (sum-of-squares x z))
        ((smallest? z x y) (sum-of-squares x y))))
```

### Next time on SICP 
Recursion and big O notation with a side of number theory.

As always, I'd love to know what you thought of this section, dear reader. Let me know in the comments!