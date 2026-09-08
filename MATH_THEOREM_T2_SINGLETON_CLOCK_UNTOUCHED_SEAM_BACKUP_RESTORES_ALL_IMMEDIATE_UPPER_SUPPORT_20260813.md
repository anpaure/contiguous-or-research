# An untouched seam backs up every immediate-upper target in the singleton `T_2` clock

**Date:** 2026-08-13  
**Status:** exact finite-prefix theorem plus symbolic all-height lift.  It
restores the complete immediate-upper row; it does not restore every wider
owner-union row.

## 1. The unique immediate-upper casualty

In the complete rank-seven `ML(13)` upper-owner factor, put

\[
                         Z=1000111011110.                    \tag{1.1}
\]

The old factor has exactly two directed seams with union `Z`:

\[
\begin{aligned}
 f=1000110011110&\longrightarrow g=1000111011010,\\
 r=1000111011100&\longrightarrow u=0000111011110.
\end{aligned}                                                \tag{1.2}
\]

The `T_2` relay deletes `f -> g` and leaves `r -> u` literal.  The switched
factor has no other seam with union `Z`.

After replacing the exceptional owner

\[
                         a=1010110011010                     \tag{1.3}
\]

by the singleton block of
`MATH_THEOREM_ONE_SINGLETON_EXCEPTION_POSITIVE_RESIDENT_CLOCK_AND_WEIGHTED_SUPPORT_20260813.md`,
the natural three-tag clock has no immediate-upper base casualty except
the deleted copy of `Z`.  Its old fibre at the deleted seam is

\[
                         \{p_0\}\cup D_0.                    \tag{1.4}
\]

## 2. The forced backup colour

The common-successor equality quotient for the singleton clock is
loop-free.  Add the one colour equality

\[
                         t(u)=t(a)=0.                         \tag{2.1}
\]

The quotient conflict graph remains three-colourable.  No block is
changed: `u` remains a normal length-`2h+2` clock block.  At the unchanged
boundary `r -> u`, the auxiliary union is therefore exactly

\[
                         \{p_{t(u)}\}\cup D_0
                         =\{p_0\}\cup D_0.                   \tag{2.2}
\]

Together with `r union u=Z`, this is a literal new witness for the deleted
old target

\[
                         C\cup Z\cup\{p_0\}\cup D_0.         \tag{2.3}
\]

### Theorem 2.1

For every `h>=2`, the singleton clock with constraint (2.1):

1. is a simple owner/lower Johnson two-factor with the same topology as
   the base rethread;
2. is positively `h`-resident;
3. retains the named new `T_0`, `B`, and `C` boundary targets; and
4. loses no old immediate-upper target.

Upper-ticket multiplicities may be at most three; upper **support**, not
upper-palette simplicity, is the assertion in item 4.

#### Proof

The quotient relation adds only a legal colour equality and creates no
conflict loop.  Hence every normal midpoint still exchanges two distinct
tags and every old/new block join remains a literal base Johnson exchange.
The singleton block and all auxiliary words are unchanged, so the graph,
owner/lower simplicity, and positive residence follow from the
one-singleton theorem.

At a normal block boundary the lifted immediate-upper value is the base
seam union together with one head tag and `D_0`.  All literal unchanged
seams keep their old fibre unless their tag colour is renamed; a global
colour renaming changes old and new occurrences together.  The finite
rank-seven seam ledger has just the one lost base value `Z`.  Equations
(1.2) and (2.2) give it a surviving occurrence with the required fibre.
The singleton boundary equations keep the `B,C` fibres, while the `T_2`
relay's created `T_0` seam keeps its prescribed fibre.  This proves all
four assertions.  \(\square\)

## 3. Exact residual width boundary

The theorem is not an all-width statement.  Exact H100 replay at heights
`2,...,12` gives total wider-deck loss

\[
                         53,74,95,\ldots,263
                         =21h+11.                           \tag{3.1}
\]

Every residual casualty has target-rank excess at least two above the
lifted owner rank.  Thus the immediate-upper row is closed exactly, while
the remaining finite-prefix problem is a linear-size wider-target backup
bank.

The verifier is

```text
scratch/audit_msw_t2_singleton_a_clock.py
```

with SHA-256

```text
d1708cac81d93996afc84e40cac76db30d05e637e58a782e616df625a590c0f4.
```

The `--force-z-backup` H100 artifact is

```text
scratch/audit_msw_t2_singleton_a_clock_backup_20260813.h100.out
```

with SHA-256

```text
add2206c200577ed812a34f60f922893b2f2acf35c6f450e628802bf6a859b89.
```

No all-`h` conclusion is inferred merely from the numerical range: the
all-height immediate-upper assertion follows symbolically from the
two-seam ledger and identical boundary fibre (2.2).  The replay only
classifies the strictly wider residual.
