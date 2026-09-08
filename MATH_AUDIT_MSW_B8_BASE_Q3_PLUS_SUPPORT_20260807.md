# Audit: B8 base q3+ support

Canonical q3 multiplicities by omitted coordinate:

```text
1 2 3 4 5 6 7 8
5 5 2 2 2 2 5 5
```

Post-B8 multiplicities:

```text
1 2 3 4 5 6 7 8
5 3 3 2 2 2 7 3
```

The exact q3 current is

```text
+2*11111101 +11011111 +11010111
-2*10111111 -2*11111110.
```

At q4 the full-set count is `14 -> 3`; the five nonfull new windows omit
`7,7,3,3,4`.  At q5 there are only gains, and every q>=6 window is full.

**Verdict:** z-free q3+ support PASS; signed transparency FAILS (benign);
marked closure-seam audit and literal annulus host PENDING.
