# A linear-size PBBS cut orbit leaves only a polynomial named whole-fan bank

**Date:** 2026-08-05  
**Method:** combine the fixed whole-fan section with the exact selected-edge
inverse fan; no computation or search  
**Status:** unconditional reduction.  It compresses arbitrary-width target
protection for a linear packet orbit to `O(m^3)` explicitly named paths.
It does not construct alternate witnesses for those paths.

## 1. Fixed named bank

Work in odd dimension `n=2m+1`.  Let `S` be the fixed gap-potential q1
section.  For every strict lower target `A`, choose the canonical complete
PBBS corridor

\[
                         \mathcal P_A=(B_0,\ldots,B_q)           \tag{1.1}
\]

contained in `S`, and choose only one corridor when the target has several.
Its owner intersection is `A`; after complementing its owners, the paired
upper path has union `[n]\A`.  Together with the immediate upper-q1 bank,
these paths give one complete proper-upper bank.

Let `E_0` be any set of selected q1 edges to be punctured by a rethread,
and write `p=|E_0|`.

## 2. Exact polynomial leave

### Theorem 2.1 (linear-cut leave bound)

The number of chosen lower corridors (1.1) meeting `E_0` is at most

\[
                         p\binom{m+1}{2}.                        \tag{2.1}
\]

The same bound holds for their paired complementary upper witnesses.
Every chosen target outside this list survives unchanged in any degree-two
rethread retaining all its corridor edges.

#### Proof

For one selected edge `e`, the inverse-fan theorem says that a chosen
depth-`q` corridor containing `e` must be one of the `q` intervals with
`u+v=q-1`.  Summing over `q=1,...,m` gives at most
`sum_q q=binom(m+1,2)` chosen corridors through `e`.  Take the union over
the `p` punctures.  Complementation pairs each lower corridor with exactly
one upper witness.  A corridor avoiding every puncture retains all of its
edges and therefore remains consecutive in the output degree-two factor.
`square`

This is an upper bound on distinct casualties; overlaps between inverse
fans only reduce it.

### Corollary 2.2 (full rigid-C6 rotation orbit)

The full coordinate orbit of the canonical rigid clean `C6` punctures at
most `3n` selected old edges.  Its named whole-fan leave consequently has
size at most

\[
               3(2m+1)\binom{m+1}{2}=O(m^3)                     \tag{2.2}
\]

on each of the lower and paired-upper shores.

This is exponentially smaller than the middle layer
`W=binom(2m+1,m)`.  Thus the raw Boolean upper cones of the local packet are
not the right global repair size when one commits in advance to the fixed
one-witness-per-target bank.

### Proposition 2.3 (the sharp private-prefix casualty is not in the named leave)

For the canonical rigid packet, the first context-dependent local upper
counterexample is

\[
 T^- =\{0,1,\ldots,m-1,m+1,2m\}.                            \tag{2.3}
\]

Its complementary lower q1 colour is

\[
 S^-=[n]\setminus T^-
     =\{m\}\cup\{m+2,m+3,\ldots,2m-1\}.                    \tag{2.4}
\]

No rotation of `S^-` is one of the three rigid cut-row types

\[
 R_0=\{1,\ldots,m-1\},\quad
 R_1=\{1,\ldots,m-2,m\},\quad
 R_2=\{1,\ldots,m-2,m+1\}.                                 \tag{2.5}
\]

Consequently the fixed gap-section q1 occurrence of `S^-` is outside every
edge in the full rigid rotation cut orbit.  Its complemented owner edge
continues to witness `T^-` after the rethread.

#### Proof

The row `R_0` has one occupied cyclic run, whereas `S^-` has two.  For a
two-run binary necklace, start at the run of length `m-2` and record the
ordered pair of zero-gap lengths before the singleton and before returning
to the long run.  The three relevant descriptors are

\[
 \begin{array}{c|c}
  R_1&(1,m+1)\\
  R_2&(2,m)\\
  S^-&(m+1,1).
 \end{array}                                                   \tag{2.6}
\]

Because the two occupied run lengths `m-2` and `1` are distinct for
`m>=4`, a rotation cannot exchange their roles.  Hence the ordered gap
pair is a rotation invariant and all three rows in (2.6) are distinct.
Every changed old edge has q1 row in a rotation orbit of one of the `R_i`,
so the selected occurrence of `S^-` is not cut.  Complement the surviving
two-owner path. `square`

Thus the explicit local necklace-current obstruction proves that raw orbit
averaging is insufficient, but it is **not** itself an obstruction to the
fixed named-bank strategy.  The deeper inverse-fan leave remains.

## 3. Rows already transported locally

For a q2-neutral clean `C6`, every named corridor of depths one and two
through a changed edge has a literal replacement.  Hence those rows need
not enter the unresolved leave.  The conservative per-edge unresolved
count is

\[
                         \sum_{q=3}^m q
                         =\binom{m+1}{2}-3.                      \tag{3.1}
\]

A prospectively planted common-history source decoration separately
transports the complete strict-lower **word/compiler** deck at every source
width, including q3 and deeper derivative rows.  It does not by itself
transport every long owner corridor in (1.1); those corridors are retained
here because their complements are the selected arbitrary-upper witnesses.

Thus, after common-history decoration, the unresolved polynomial leave is
an upper-witness/topological occurrence problem, not a lower compiler
deficiency.

## 4. Exact alternate-bank target

For every pair `(e,u,v)` in the inverse-fan triangles of the puncture set,
let

\[
                         A(e;u,v)                               \tag{4.1}
\]

be the corresponding named lower target, when that interval is the chosen
corridor, and let `U(e;u,v)=[n]\A(e;u,v)`.

The remaining theorem is now finite and explicit:

> **Polynomial alternate-witness lemma.**  Choose, simultaneously for all
> distinct unresolved `U(e;u,v)`, owner intervals avoiding `E_0` whose
> unions are the required targets, with physical degree/capacity compatible
> with the rethread and with the protected immediate palettes.

No generic multiplicity estimate proves this lemma: some upper targets have
only one or two old corridors near the deadline.  The construction must use
the special cyclic row orbits of `E_0`, a second correlated section, or
new cross-packet ladders.

## 5. Why the reduction is useful

The packet-orbit approach does not need a context-free theorem preserving
every old upper interval.  It needs only:

1. exact local lower/compiler transport, already supplied by common
   history;
2. an alternate bank for the explicit `O(m^3)` leave (2.2); and
3. the physical topology/residence/common-cap rows.

A polynomial protected bank is still not automatically plantable, but its
size is `o(W)` by an exponential margin.  This makes a direct structured
matching, a cut-thin protected-factor extension, or a second-section
argument plausible in a way the full Boolean cone is not.

## 6. Scope

Proved:

1. the exact per-puncture inverse-fan leave;
2. the `O(m^3)` bound for a full rigid packet orbit;
3. separation of lower compiler transport from the remaining upper bank;
4. the exact finite alternate-witness target.

Not proved:

1. the polynomial alternate-witness lemma;
2. coexistence/topology of the full rotation packet orbit;
3. zero-gap residence or typed common-cap transport;
4. `nu(k)<=B(k)+O(1)`.
