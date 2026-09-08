# Audit: full q2 current of the H1 repair C8

The four turn rows are

```text
1111010011 -> 1011011011
1011101011 -> 1001111011
1001111011 -> 1101110011
1101011011 -> 1111001011
```

so the middle value cancels and the full current has three positive and
three negative terms.  The negative inverse lists are exactly

```text
1111010011 : (2,6)
1011101011 : (3,5)
1101011011 : (6,7)
```

Direct positive H1 has current

```text
+1111001011 +1011010111 -1111000111 -1011011011
```

and therefore does not recreate `1011101011`.

**Verdict:** incidence C8 PASS; old one-negative q2 statement RETRACTED;
full three-negative current PASS.
