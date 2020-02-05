# dtwp

#### What? 

dtwp stands for "dont type wrong please". It is a python library that attempts to solve the problem of people making typing mistakes on code input. The library provides tools to create codes with a trailing hash of various length and to check if inputted code is correct.

The nature of the hash is that it is not a Mathematical bijection so many codes share a same hash. This method can never take out 100% of the typing errors, but it should make the probability much lower.


#### Installation

    git clone https://github.com/juissi999/dtwp.git


#### Usage

dtwp does not use class-structure. It is a simple import module on python 3.
A few lines of example code:

    import dtwp

    codelist = dtwp.createcodes(start_integer, end_integer, hash_length)
    
    is_code_correct = dtwp.check_code(codestring, hash_length)