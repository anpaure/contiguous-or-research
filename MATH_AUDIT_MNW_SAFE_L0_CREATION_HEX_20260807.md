# Audit: the support-safe `L_0` creation hex

**Date:** 2026-08-07  
**Method:** independent hand replay; no computation or search

The face has core `1010010001`, active labels `9,5,2`, owners

```text
1010010011  1010110001  1110010001
```

and selected-addition pairs

```text
{4,5}  {2,4}  {8,9}.
```

Therefore the selected cycle edges alternate.  The turn ledger is

```text
1011110011 -> 1111010011
1111110001 -> 1011110011
1110010111 -> 1110110101
```

and reduces to

```text
+1111010011 +1110110101 -1111110001 -1110010111.
```

The inverse-pair replay is

```text
1111110001 : (1,10), (2,4)
1110010111 : (2,3),  (8,9)
```

so each negative retains one provider.  All three owners and all six
incidences are outside the gamma--alpha, endpoint, `H0`, and repair-`C8`
supports.

The alternative core-six face removes the unique `(2,4)` provider of
`1111100011`; the canonical core-two `\{3,6\}` face cancels its own `L_0`
gain and is disabled by the repair `C8`.  No other one-selected centre has
an alternating completion.

**Verdict:** literal q1 PASS; q2 support PASS; suffix tensor PASS;
topology/q3+ PENDING.
