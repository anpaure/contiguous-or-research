# Audit of the clean-C6 resident three-port upper-monotone lift

**Date:** 2026-08-05  
**Method:** direct substitution in the frozen resident `q`-port formulas;
no computation or search  
**Verdict:** PASS after making the standing hypothesis `d>=1` explicit.

## 1. Exact `q=3` indexing

The clean Boolean-diamond data are

\[
 P_i=K+a_i+a_{i+1},\qquad Q_i=K+a_i+c,
\]

with shores

\[
 E_i=P_iQ_i,\qquad E'_i=P_iQ_{i+1}.
\]

In the resident converter take

\[
 q=3,\qquad S=K,\qquad z=c.
\]

Then its port owners are literally

\[
 A_i=S+z+a_i=Q_i,\qquad
 B_i=S+a_i+a_{i+1}=P_i.
\]

Consequently its direct old shore is

\[
 \{A_iB_i\}_i=\{Q_iP_i\}_i=\{E_i\}_i,
\]

and its direct new shore is

\[
 \{A_iB_{i-1}\}_i
 =\{Q_iP_{i-1}\}_i
 =\{E'_{i-1}\}_i.
\]

The last equality follows from
`E'_(i-1)=P_(i-1)Q_i`.  Thus there is only a cyclic index shift; no
orientation or shore mismatch is hidden in the identification.  With the
forward return rail `B_i leadsto A_i`, the old state closes separately at
each port, while the new direct edge sends port `i` to port `i-1` and hence
joins all three ports into one cycle.  The declared fusion direction is
therefore exactly the clean switch `E -> E'`.

## 2. Coordinate supply

Here the resident theorem's owner rank `m` equals `r`.  Choosing
`X subset K` with `|X|=d` and retaining an anchor in `K-X` requires

\[
 |K|=r-2\ge d+1,
\]

or `r>=d+3`.  The labels used by the core, active quartet, and fresh rail
bank number

\[
 (r-2)+4+d=r+d+2.
\]

Thus on the odd ground set of size `2r-1`, fresh-label supply is equivalent
to the same inequality `r>=d+3`.  The original draft omitted only the
resident theorem's standing hypothesis `d>=1`; that hypothesis is now
explicit.

## 3. Exact scope of cyclic-deck monotonicity

Write

\[
 C_i=K\cup Y\cup\{c,a_i,a_{i+1}\},\qquad
 D_i=K\cup Y\cup\{c,a_{i-1},a_i,a_{i+1}\}.
\]

For widths at most `d+2`, the resident theorem gives equality of the old
and new cyclic interval-union multisets.  At width `d+3`, the complete
signed current is

\[
 \sum_i(e_{D_i}-e_{C_i}).
\]

When `q=3`, the three `D_i` coincide in the single value containing all
three active labels, with multiplicity three.  The three `C_i` remain
distinct.  Each `C_i` still has a new-state occurrence (the opposite
extreme crossing window).  Moreover every old-state interval of width at
least `d+2` on port `i` is already saturated at exactly `C_i`.  Hence every
old target has a new cyclic witness, proving

\[
             Deck_{\rm cyc}(H_2)\subseteq Deck_{\rm cyc}(H_3).
\]

This is precisely a **set-support** statement for nonempty cyclic owner
intervals internal to the displayed components.  It does not assert:

* equality of graded widths or multiplicities;
* transport of a fixed derivative occurrence or compiler edge;
* protection of intervals using an exterior owner;
* protection after cutting a cycle into a linear word; or
* compatibility of several resident packets in one host.

The theorem and its scope section keep all five distinctions explicit.

## 4. Conclusion

The `q=3` substitution is exact, the fusion direction is correct, and the
claimed cyclic-deck inclusion follows from the frozen `q`-port theorem.
No correction beyond the explicit `d>=1` hypothesis is required.
