# Audit: ordered two-hex repair of positive H2

Initial selected pairs:

```text
1011000101 : {6,7}
1011000110 : {2,6}
1011010100 : {2}
```

First face: core `1011000100`, active `6,2,10`; it changes

```text
1011010100 : 2 -> 10
1111000100 : 10 -> 6
1011000101 : 6 -> 2
```

Second face: core `1001000101`, active `3,2,9`; it changes

```text
1011000101 : 2 -> 9
1101000101 : 9 -> 3
1001000111 : 3 -> 2
```

The resulting H2 phase is `{7,9},{2,6},{10}` and is alternating.  The
complete repair-plus-H2 current is

```text
+1111001101 +1101100111 +1111000111
-1101001111 -1011100111 -1111010110.
```

The inverse lists are

```text
1101001111 : (7,9)
1011100111 : (3,5), (6,7)
1111010110 : (2,6)
```

**Verdict:** literal phase PASS; exact q2 current PASS; q2 support FAILS at
the first and third negative; topology PENDING.
