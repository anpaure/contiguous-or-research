# Audit: positive H0 and the H1 single-owner gate

**Date:** 2026-08-07  
**Method:** independent hand replay; no computation or search

Positive H0 is alternating after the leaf face.  Its three turn changes are

```text
1010101111 -> 1011101101
1111001011 -> 1110001111
1011011101 -> 1011011011
```

At the third H1 owner `1011000011`, the selected additions are `{2,6}` and
both H1 additions `7,8` are unselected.

The unique C8 transfer has parameters `(s,x)=(3,6)`, vertex row

```text
1011000011 1011001011 1001001011 1001011011
1001010011 1101010011 1101000011 1111000011
```

and alternating status `01010101`.  It removes the unique q2 occurrence
`1111010011`, witnessed only by `(2,6)`.

**Verdict:** H0 PASS; direct H1 FAIL at one owner; C8 phase repair PASS;
q2 support after that C8 PENDING one companion relay.

