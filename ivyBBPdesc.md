The inner workings of the BBP formula allow you to calculate the nth hexadecimal digit of pi without knowing any of the previous digits. Putting this into a summation results in the BBP formula.

Ivy has support for loading code from a file, so that's what I'll be doing. The formula can be written like so:

```
op bbpp k = ((120 * k * k) + (151 * k) + 47) / (16 ** k) * (512 * k * k * k * k) + (1024 * k * k * k) + (712 * k * k) + (194 * k) + 15 # a piece of the BBP sum
op bbp x = +/ bbpp -1 + iota x # the BBP sum up to x iterations
```

This provides us with a usable operation, but does not change Ivy's precision. To do so, we add the following:

```
)prec 131072
```

The maximum is technically higher, but setting it to the max ends up severely slowing the interpreter, and losing efficiency. You can set it to 262144, but I wouldn't go much higher than that. For some reason, setting max bits doesn't slow the interpreter, so we'll set that:

```
)maxbits 2147483647
```

Now, we can finally set the max digits:

```
)maxdigits 1000000
```

The result displays as a fraction, by default. To display it as a decimal, you can use the following:

```
'%g' text bbp x
```

Just remember to replace x with the number of iterations, and you're done!
