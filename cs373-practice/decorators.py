#!/usr/bin/env python3

# -------------
# Decorators.py
# -------------

def cache_1 (f) :
    def g (n) :
        return f(n)
    return g

def pre_gtz (f) :
    def g (n) :
        assert n > 0
        return f(n)
    return g

def post_gtz (f) :
    def g (n) :
        v = f(n)
        assert v > 0
        return v
    return g

@cache_1
@pre_gtz
@post_gtz
def cycle_length_1 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

class cache_2 :
    def __init__ (self, f) :
        self.f = f

    def __call__ (self, n) :
        return self.f(n)

@cache_2
@pre_gtz
@post_gtz
def cycle_length_2 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

def test (f) :
    assert f( 1) == 1
    assert f( 5) == 6
    assert f(10) == 7

print("Decorators.py")

test(cycle_length_1)
test(cycle_length_2)

print("Done.")
