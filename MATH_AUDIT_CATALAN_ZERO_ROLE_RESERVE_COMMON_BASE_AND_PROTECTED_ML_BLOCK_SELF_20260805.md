# Self-audit: Catalan zero-role reserve and the protected Middle-Levels block

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_CATALAN_ZERO_ROLE_RESERVE_COMMON_BASE_AND_PROTECTED_ML_BLOCK_20260805.md`  
**Method:** independent algebraic and quantifier replay within the same
pure-mathematical lane; no computation, search, or solver  
**Verdict:** **SELF-GO** at the stated three-level scope: static role
reservation and two-factor planting are unconditional, the SCD refinement
has an exact min--max, and literal supported-bank co-selection remains open.

## 1. Inventory

Every positive chain has one member in the top rank `q-2`, and every top
set belongs to exactly one chain.  Hence the number of positive roles is

\[
                         \binom{2q-1}{q-2}.
\]

The role count is `W=binom(2q-1,q-1)`, so the zero count is

\[
 W\left(1-{q-1\over q+1}\right)
 ={2W\over q+1}
 ={1\over q+1}\binom{2q}q.
\]

At depth `j`, one chain occurrence accounts for one target of rank
`q-1-j`; therefore the height-tail count is exactly the size of that rank.
The exact-height differences in (1.3) follow.

## 2. Static deletion Hall bound

For the inclusion graph

\[
 \binom{[2q-1]}{q-2}longleftrightarrow
 \binom{[2q-1]}{q-1},
\]

the protected-top parameters are

\[
 a=q+1,
 \qquad b=q-1,
 \qquad a(a-2)+1=q^2.
\]

Thus

\[
 \eta=\left\lfloor
 \min\left\{q,{2q^2\over q-1}\right\}
 \right\rfloor=q.
\]

Deleting any prescribed `P` with `|P|<=q` therefore leaves a matching of
every top target into a distinct containing root.  For a saturated chain

\[
 S_1\supset\cdots\supset S_h
\]

assigned to `R`, the departures

\[
 R\setminus S_1,
 S_1\setminus S_2,
 \ldots,
 S_{h-1}\setminus S_h
\]

are distinct singletons and give exactly that local static prefix.  This
checks Theorem 2.1 while also confirming its limitation: those departures
have not been made consecutive in a factor.

## 3. Common-base/SCD equivalence

Let `a=binom(2q-1,q-2)`.  A common base `E` supplies bijections

\[
 \binom{[n]}{q-2}\longleftrightarrow E,
 \qquad
 M(E)\longleftrightarrow\binom{[n]}{q+1}.
\]

They form `a` disjoint chains of ranks

\[
                         q-2,q-1,q,q+1.
\]

Every root outside `E` forms one chain of ranks `q-1,q`.  Counts and
rank symmetry close exactly, so the usual outward SCD induction applies.
Conversely every SCD with central matching `M` determines precisely this
common active set `E`.  Reserved short roots cannot lie in `E`.

Edmonds' formula for the maximum common independent set in
`E_0=mathcal L setminus P` is

\[
 \min_{A\subseteq E_0}
 \bigl(r_-(A)+r_+(E_0\setminus A)\bigr),
\]

so (3.3) is exact.

In the auxiliary graph, a root whose plus copy is matched from the lower
outer rank cannot use its identity; its minus copy must then match the
upper outer rank.  Thus both outer matchings use one common root set.
For a left shore `X dotcup B^-`, the neighbourhood is exactly

\[
                         (N_-(X)\cup B)^+
                         \mathbin{\dot\cup}N_+(B),
\]

which verifies (3.6).

The lower endpoint matching after deleting `P` is Theorem 2.1.  Complement
turns the upper endpoint graph into the same rank-`q-2` to rank-`q-1`
inclusion graph with the `|P|` forbidden roots `M(P)^c`.  Hence both full
endpoint ranks equal `a`.  This does not imply every mixed Edmonds cut.

## 4. Protected path arithmetic

A `(q-2)`-set has `q+1` exterior labels.  Distinct
`a_0,...,a_(d-1)` give distinct lower roots `K+a_i` and distinct upper
vertices `K+a_i+a_(i+1)`.  The alternating path has `d` lower vertices,
`d-1` upper vertices, and exactly

\[
                         2(d-1)=2d-2
\]

incidence edges.  It is simple and 2-bounded.  Therefore
`2d-2<=q-2` is exactly the hypothesis needed to invoke the small
protected-factor theorem for `ML_q`.

The resulting factor is spanning, so every upper vertex occurs once and
the projected lower cycles are upper-rainbow.  The protected theorem does
not bound the number of components.  For `d=Theta(sqrt(q))`, the edge cost
is `o(q)` and the inequality holds eventually.

## 5. Literal support and scope

For a fixed factor, two chain-provider sets with different top targets are
disjoint because their first intersections differ.  Therefore the
nonemptiness tests (5.3) are necessary and sufficient, with no cross-top
Hall row.  At depth one they demand surjectivity of the rank-`q-2`
intersection colours after deleting the reserved block.

A spanning Middle-Levels factor does not imply this surjectivity: it spans
rank `q-1` roots and rank `q` adjacent unions, not rank `q-2` intersections.
Nor does the static inclusion matching determine the actual successor of a
root.  Hence the theorem correctly does **not** claim:

1. a Hamilton completion of the protected path;
2. supported nested banks on the completed factor;
3. residence or a terminal safe opening in one literal chronology;
4. arbitrary-width upper coverage or a compiler; or
5. an all-dimensional coefficient-one or additive-constant construction.

The result isolates the exact remaining compatibility rather than assuming
it.  **SELF-GO.**
