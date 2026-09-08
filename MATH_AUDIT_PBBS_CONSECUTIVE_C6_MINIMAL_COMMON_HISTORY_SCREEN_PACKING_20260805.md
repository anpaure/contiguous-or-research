# Audit: consecutive minimal common-history screen-packing obstruction

**Date:** 2026-08-05  
**Method:** direct index and cardinality replay; no computation or search

## Verdict

**PASS.**

For a depth-`d` source word, transition `j+s` has left screen `A_(j+s)`.
If transitions `j,...,j+d` all carry the minimal clean-C6 decoration, then
`A_(j+1),...,A_(j+d)` are all two-sets.  They are simultaneously the exact
ordered history of transition `j`.  Their union therefore has size at most
`2d`, whereas the minimal packet requires it to equal its core `K` of size
`r-2`.  This proves `r-2<=2d`, and disjointness gives equality.

The scope is correct: the argument does not apply to fewer than `d+1`
consecutive edges, sparse packet placement, nonminimal screens, or one
compound source macro.  It invalidates only independent minimal packet
stamping on a long consecutive sibling rail.
