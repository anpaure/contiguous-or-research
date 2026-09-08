# Audit: unique C8 boundary transfer and `R0` relay

**Date:** 2026-08-07  
**Method:** independent hand replay; no computation or search

The C8 normal form has five choices of removed owner label and three choices
of outside label.  The touching conditions leave only `(s,x)=(9,4)`.
Its vertex row is

```text
1100100110 1100100111 1100100101 1101100101
1101100100 1101110100 1100110100 1100110110
```

and its status word is `01010101`.

The C8 current is

```text
+1101100111 +1101101101 -1101110110 -1100101111.
```

The reverse contextual hex current after the C8 is

```text
+1101110110 +1100011111 -1100111110 -1101010111.
```

Adding the direct-face current

```text
+1100101111 +1101010111 -1100011111 -1101100111
```

leaves exactly

```text
+1101101101 -1100111110.
```

The negative target has unique witness `(5,7)`.  The relay is literal and
suffix-tensorable but not q2-support closed.

