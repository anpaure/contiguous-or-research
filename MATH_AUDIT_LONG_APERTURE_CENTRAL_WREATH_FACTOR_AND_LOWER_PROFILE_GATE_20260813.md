# Audit: the long-aperture central wreath factor is literal and resident, but carries only the top lower band

**Date:** 2026-08-13  
**Status:** proof-safe audit.  The proposed odd-dimensional owner factor is
valid and stronger than a short pure rail on the owner/immediate-palette
rows.  It does not by itself close the strict-lower compiler.

## 1. Odd-dimensional construction

Let `k=2m+1`, `R=m+1`, and let `d<m`.  On a cyclic order of `[2m+1]`, put

\[
 Q_i=\{i,i+1,\ldots,i+m-1\},\qquad
 T_i=[2m+1]\setminus Q_i.                         \tag{1.1}
\]

The `Q_i` are the `m`-windows.  The Mütze--Standke--Wiechert wreath factor
partitions all `m`-sets into such cycles; complementing therefore partitions
all rank-`R` owners into cycles of the form (1.1).

### Theorem 1.1 (exact physical rows)

Every cycle (1.1) has:

1. every owner of rank `R` once globally under the wreath factor;
2. positive runs of length `m+1`, hence a nonempty exact depth-`d`
   antecedent for every `d<m+1`;
3. immediate intersections equal to complements of the `(m+1)`-windows,
   so globally every rank-`R-1=m` target occurs exactly once;
4. simple owner, immediate-lower, immediate-upper and proper cyclic interval
   decks inside each wreath.

#### Proof

Advancing `Q_i` deletes one point and inserts one point, so its complement
is a Johnson cycle.  A coordinate is absent in `m` consecutive owners and
present in the other `m+1`; this proves residence.  Moreover

\[
 T_i\cap T_{i+1}=[2m+1]\setminus(Q_i\cup Q_{i+1}), \tag{1.2}
\]

which is the complement of an `(m+1)`-window and has rank `m=R-1`.
Complement is a bijection between the `(m+1)`- and `m`-layers, and the
wreath factor uses every `m`-window once, proving the global immediate-lower
claim.  Proper interval simplicity follows from the cyclic order of
distinct points, exactly as for a pure rail. \(\square\)

No physical axiom forces the active window to have length exactly
`q=d+1`, nor forces a particular core size.  Those were catalogue choices,
not residence requirements.

## 2. Exact maximal antecedent and its lower profile

The maximal cyclic depth-`d` antecedent is

\[
 P_p=\bigcap_{j=0}^{d}T_{p-j}
     =[2m+1]\setminus\bigcup_{j=0}^{d}Q_{p-j}.     \tag{2.1}
\]

The union on the right is one cyclic interval of size `m+d`, so

\[
 |P_p|=m+1-d=R-d.                                  \tag{2.2}
\]

For every source width `1<=w<=d`, the union of `w` consecutive `P_p` is
again the complement of one cyclic interval and has rank

\[
 \boxed{R-d+w-1}.                                  \tag{2.3}
\]

Consequently one wreath component offers exactly one endpoint-indexed row
at each lower rank

\[
 R-d,R-d+1,\ldots,R-1,                             \tag{2.4}
\]

and offers no target at any rank below `R-d`.

#### Proof

The `d+1` consecutive `m`-windows in (2.1) enlarge their union by one point
per step, proving (2.2).  Consecutive complements `P_p` shift one endpoint;
the intersection of their omitted cyclic intervals shrinks by one point
per added source position.  Thus each added `P_p` raises the union rank by
one, proving (2.3). \(\square\)

## 3. Exact verdict

The long-aperture factor is a valid exact owner/immediate-lower/residence
construction.  Its first obstruction is not flat-source existence.  It is
rank support in the lower compiler:

\[
 \boxed{\text{the wreath antecedent misses every strict-lower rank }
        1,\ldots,R-d-1.}
\]

Thus it can replace the top-band portion of the unified rail-queue factor,
or serve as a protected owner skeleton, but it cannot replace the mixed
age-composition queues or Ferrers boundary that supply the lower ranks.
The even-dimensional split has the same logical boundary: each shell must
be audited for its exact source-width rank profile, and owner coverage does
not imply full strict-lower coverage.
