# Audit: base delta relay and positive-context return

**Date:** 2026-08-07  
**Method:** independent hand replay; no computation or search

## Base incidence face

For `K=100100` and active labels `6,3,2`, the owners are

```text
100101  101100  110100
```

and colours are

```text
101101  111100  110101.
```

The selected additions `{3,5}`, `{2}`, `{6}` make the status word
alternating.  Only the first owner is internal, and its turn changes

```text
101111 -> 110111.
```

Thus the face current is `+T3-T2`.

## Native current

Adding delta gives

```text
+T1 +T5 -T6 -T2.
```

The negative native loads are both two, so the native factor remains q2
complete.

## Positive-context current

Prefixing `1100` gives

```text
+1100011111 +1100111101 -1100111110 -1100101111.
```

The last target is `J`.  In the post-third-face state its load is one, not
the native load two of `T2`.  Therefore the carried current reopens `J`.

## Reverse-alpha overlap

The positive contextual reverse-alpha copy and the direct `J` face share
the owner `1100100101` and both incidences to colours `1100110101` and
`1100100111`, with the same required replacement.  They are not independent
alternating switches.  At owner `1100110100` neither required contextual
cycle incidence is canonical-selected, giving a second literal phase
failure.

**Verdict:** the native relay and current algebra PASS; positive-context
support closure FAILS without a compound prepared-prism realization.

