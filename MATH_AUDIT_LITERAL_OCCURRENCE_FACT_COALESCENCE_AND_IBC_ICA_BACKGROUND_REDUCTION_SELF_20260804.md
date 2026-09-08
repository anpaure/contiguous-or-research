# Self-audit: literal occurrence-fact coalescence for aligned `Ibc/Ica`

**Date:** 2026-08-04  
**Method:** independent symbolic and semantic replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_LITERAL_OCCURRENCE_FACT_COALESCENCE_AND_IBC_ICA_BACKGROUND_REDUCTION_20260804.md`

## 0. Verdict

**PASS within the theorem's explicit compound-role scope.**

The positive theorem does not grant a physical cell capacity two.  It
identifies two declarations of one exact address/value/state fact and stores
them in one conjunctive record, charging that address once.  If a terminal
specification treats the roles as exclusive or requires a different type,
the theorem deliberately reverts to the capacity-one no-go.

The result removes only ordinary assignment/socket double counting.  It
does not authenticate a common terminal state, a complementary background
matching, or longer background path interiors.

## 1. Common-cap idempotence

In a fixed literal word, a cell `e` has one value `Z=OR_A(e)`.  An ordinary
assignment of `Z` to `e` contributes the usual cap constraints: letters in
`e` lie in `Z`, and retained traces cover `Z`.  A logical socket role which
reasserts the same equality adds no set constraint.  Intersecting the same
cap constraint twice is idempotent.  Thus the maximal cap and its trace
decoration are unchanged.

This argument would fail if the role imposed an additional flag-dependent
letter condition.  The theorem therefore includes logical-only acceptance
as a hypothesis rather than inferring it from the Boolean value.

## 2. Matching contraction

Forced facts `(Z_a,e_a)` are target- and cell-disjoint.  A matching on the
deleted graph plus these facts is a full matching, and deleting them from a
full matching gives the residual matching.  This is exactly the standard
forced-edge contraction and proves both directions of Theorem 2.1.

The displayed Hall condition should be read on the residual graph after
deleting `C_*`; no surplus or capacity-two term appears.  A named frozen
background path deletion can nevertheless be stronger because it may
delete a coalescible endpoint before the compound record is formed.  The
warning in Section 2 is therefore necessary.

## 3. Native-value replay

For ticket `j`, put `i=j-1`.  Consecutive owners in the first active block
are

\[
 K\cup V_L^\epsilon\cup(F-f_i),qquad
 K\cup V_L^\epsilon\cup(F-f_{i+1}).
\]

Their intersection and union are

\[
 K\cup V_L^\epsilon\cup(F-\{f_i,f_{i+1}\}),
 \qquad
 K\cup V_L^\epsilon\cup F,
\]

which are precisely the port and upper-turn values in the theorem.  The
omitted pairs `{f_(j-1),f_j}` are different as `j` varies, so the port
values are distinct.  The upper value is constant, while the interval
addresses `q_(j-1)` are distinct.  Hence one ordinary upper target may be
assigned once and all `d-1` socket terminals still have distinct physical
capacity.

The audited ambient theorem already proves pairwise address disjointness of
the ray, port, owner, and q1 records across tickets, including `d=2`.

## 4. Target-count audit

The theorem does not count the common upper value `U^epsilon` `d-1` times.
It is one Boolean target with `d-1` physical occurrences.  At most one of
those occurrences is its ordinary target assignment; all may independently
serve the occurrence-distinct socket tickets.

Conversely, it does not fuse different logical tickets onto one `q` cell.
That would violate capacity one and is explicitly excluded.  The aligned
bank avoids the issue because every ticket uses its own `q_(j-1)` address.

## 5. Typed acceptance audit

The ordinary fact at the port is `OR(r_j)=R_j^epsilon`; the polarized code
uses `(R_j^epsilon,prefix)`.  The ordinary fact at the upper turn is
`OR(u_j)=U^epsilon`; the code uses `(U^epsilon,suffix)`.  The Boolean parts
therefore agree exactly.

The role bit is metadata, but the current terminal theorem still requires
one state-aware acceptance predicate.  The new theorem does not silently
turn metadata into an accepted physical terminal type.  It proves only that
once accepted as logical-only, no second occurrence capacity or cap
constraint is needed.

## 6. Scope checklist

Proved:

- exact criterion for assignment/socket occurrence coalescence;
- unchanged maximal cap under duplicate fact assertions;
- exact forced-edge residual matching reduction;
- actual aligned `Ibc/Ica` port and upper values;
- zero extra occurrence charge for ordinary palette roles; and
- sharp capacity-one no-go under exclusive single-role semantics.

Not proved:

- terminal acceptance of the polarized product type;
- existence of the complementary background matching in the same state;
- disjointness of longer transported-background path interiors;
- global packet planting, topology, upper deck, residence, or regeneration;
- `nu(k)<=B(k)+O(1)` or exact equality.
