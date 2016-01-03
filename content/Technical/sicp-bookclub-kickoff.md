---
layout: post
title: Why You Should Read Structure and Interpretation of Computer Programs with Me
date: 2015-04-29 9:46:30
tags: sicp
---

I'm starting a trans-continental bookclub this Summer to work through the classic [_Structure and Interpretation of Computer Programs_](http://sarabander.github.io/sicp/html/index.xhtml).
So far there's me (South America - eventually), Wesley Bermbach (Germany - eventually), and hopefully Joel Roggeman (Seattle, USA - eventually).
With this post I want to convince you to join us.

## What Is It?
SICP, as the cool kids call it, was the text for MIT's [introductory computer science course](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/) for some decades.
Although it was used for first year undergrads, it gets heavy quick.
Here's a [series of lectures](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/) going along with the book that the authors Abelson and Sussman presented at Hewlett-Packard.
If you browse those lecture titles or the book's table of contents, you'll see that the book covers a _lot_ of ground starting from first principles.

## What Does it Cover?

Here's a brief (probably inaccurate) summary based on some skimming.

Using Scheme, a dialect of LISP, you start by learning the essentials of functional programming.
(For the hard-core FP-ers out there, I should note that Scheme is **not** referentially transparent.)
For most of us, this will cause some shocks. 
By the end of the first chapter, you write some cool programs - like a procedure for finding the nth root of a number - with nary a loop in sight.

In chapter 2, you move on to data structures and write things like a symbolic differentiation program.

In chapter 3, you learn about two ways to structure large programs: objects - an approach we're all familiar with, and streams, which are seeing a resurgence nowadays.

Then chapter 4 gets into the _really_ juicy stuff: "metalinguistic abstraction". 
It walks you through the creation of a "metacircular evaluator," a Scheme program that evaluates Scheme programs!
Then you go MAD with power and start tinkering with the language, adding in lazy evaluation and even making a Prolog interpreter!

But we must go Deeper! In chapter 5, you look at how Scheme is implemented on a physical machine (like with registers) and try your hand at compilation.

## Why Should I care?

You wouldn't read this book to put "experience in LISP" on your resume (although Clojure is gaining traction, for what that's worth).
You would read this book to explode your head a little, to relearn what you already know but in a different way.
[This long blog post](http://www.michaelnielsen.org/ddi/lisp-as-the-maxwells-equations-of-software/) on why LISP is the Maxwell's Law of programming really sold me on why LISP is good as a mind-expansion tool.


## I'm Sold! Now What?

The book is online in a variety of formats. I like [this HTML version](http://sarabander.github.io/sicp/html/index.xhtml#SEC_Contents).
Talk to me or leave a comment if you want to join the SICP bookclub.
I made a Slack team for informal discussions and troubleshooting that I can invite you to.
I'm posting my solutions to exercises [on Github](https://github.com/WillEngler/sicp-solutions) so that we can compare our solutions.

Also, I plan to post regularly here with my thoughts on what I've read so far.
I'd like to use the comments here to discuss the book in public so that people who are just curious but don't want to dive deep can see what we're up to.
And if you want to write posts of your own, that'd be awesome if you started discussions on your own blog.
Or send a pull request with a markdown document to [my blog](https://github.com/WillEngler/willengler.github.io/tree/prepare) and I can add a guest post.

I don't think we should have a set schedule, so this will be an asynchronous bookclub. 
When you get to a certain section in the book that's been covered, join the discussion then.
I imagine it'll be kinda like how I look at Game of Thrones episode recaps once I finally get around to them years later.

And if nobody joins me, that's ok. 
I'll blog into the void and leave chapter recaps for whomever wanders this corner of the internet years from now.