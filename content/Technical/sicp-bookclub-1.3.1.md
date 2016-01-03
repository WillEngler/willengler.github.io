---
layout: post
title: SICP Book Club: 1.3.1 (What Are Higher-Order Procedures?)
author: Will Engler
tags: sicp
date: 2015-05-15 11:02:30
---

>The world was so recent that many things lacked names, and in order to indicate them it was necessary to point.
>> Gabriel Garciá Márquez on Anonymous Functions

_A dialogue between two seekers of knowledge_

**Alexis**: Tael'r, I beseech your aid.

**Tael'r**: What is it, friend?

**Alexis**: I am uncovering the mysteries of higher-order procedures, but I am battling a bug.

**Tael'r**: Pray, show me your code.

**Alexis**: Very well. I am trying to implement Simpson's Rule as specified in Exercise 1.29.

```Scheme
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (cube x) (* x x x))

(define (inc x) (+ x 1))

(define (simpson n f a b) 
  ((let ((h (/ (- b a) n)))
     (define (simpson-term k) 
       (let ((y (f (+ a (* k h)))))
         (if (or (= k 0) (= k n))
             y
             (if (even? k) 
                 (* 2 y)
                 (* 4 y)))))
     (* (/ h 3) 
        (sum simpson-term a inc b)))))
```

**Tael'r**: Do you know where the bug hides?

**Alexis**: No. The interpreter tells me that `The object 1/75000000 is not applicable.`. 
But I lack the skill with the debugger to tell where this is happening.

**Tael'r**: Well then, I recommend you simplify.
We don't need to abandon all we have learned because we are working with a new language.
When you don't understand a problem, break it down.

**Alexis**: Of course. Thank you, my wise friend.

_Alexis returns to the mountain where she does her coding and returns some minutes later._

**Alexis**: I got it to work! But it's a bit... janky.

**Tael'r**: Let me see.

```Scheme
(define (simpson-term a h k n f)
; Compute y sub k
  (let ((y (f (+ a (* k h)))))
;Special cases for first and final term
    (cond ((or (= k 0) (= k n)) y)
          ((even? k) (* 2 y))
          ((odd? k) (* 4 y)))))

(define (curry-simpson a h n f)
  (lambda (k)
    (simpson-term a h k n f)))

(define (simpson f a b n) 
  (let ((h (/ (- b a) n)))
    (* 
     (/ h 3)
     (sum (curry-simpson a h n f) a inc n))))
```

**Tael'r**: Ah, I see. 
To break the problem apart you had to find a way to bind variables local to `simpson` to `simpson-term`.

**Alexis**: Yes, I think this is more complex than it needs to be.

**Tael'r**: Perhaps.
And I think you're abusing the term "curry", but I get what you mean.
That's ok.
One must write ugly code before writing elegant code.

**Alexis**: The road to enlightenment will be long.