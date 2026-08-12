# Independent audit: Tomon `c`-partition coefficient and OR serialization

Date: 2026-08-04  
Audited file:
`MATH_THEOREM_TOMON_CPARTITION_CRITICAL_COEFFICIENT_AND_SERIALIZATION_BARRIER_20260804.md`

## 1. Source statement

The primary theorem summary states

\[
 n>500c^2
 \quad\Longrightarrow\quad
 2^{[n]}\text{ has a chain partition with at most one chain not of size }c.
\]

The exceptional chain has at most `c` members. Replacing the paper's `n`
by the OR dimension `k` is purely notational.

Audit result: **PASS**.

## 2. Critical constants

The OR depth satisfies

\[
 d^2/k\to\pi/8.
\]

Therefore

\[
 500(d+C)^2/k\to500\pi/8=196.349\ldots>1
\]

for every fixed `C`, and

\[
 500(2d+C)^2/k\to500\pi/2=785.398\ldots>1.
\]

Thus the sufficient hypothesis `k>500c^2` eventually fails at both
`c=d+C` and `c=2d+C`.

The largest theorem-certified scale is

\[
 c<\sqrt{k/500},
 \qquad
 {c\over d}\le\sqrt{8/(500\pi)}+o(1)=0.071\ldots .
\]

Audit result: **PASS**.

## 3. Lower-fragment count

Intersecting a chain with a lower ideal gives an initial segment, hence one
chain rather than several fragments. Every nonempty intersection has size
at most `c`, including the exceptional chain. Since the intersections
partition all `Lambda` lower targets,

\[
 F\ge\lceil\Lambda/c\rceil.
\]

Using `Lambda/W=d+O(1)` and `c<sqrt(k/500)` gives

\[
 F/W\ge\sqrt{500\pi/8}+o(1)=14.012\ldots+o(1).
\]

Audit result: **PASS**.

## 4. Join lower bound

A binary join of chain components lowers their number by at most one.
Producing at most `W+d+C` endpoint chains from `F` fragments therefore
requires at least

\[
 F-(W+d+C)
 \ge(\sqrt{500\pi/8}-1-o(1))W
\]

joins. Since `d+C=o(W)`, the constant is `13.012...`.

This statement permits arbitrary new comparable joins; it does not assume
that the original partition has none. It is a necessary operation count,
not a claim that the joins are impossible.

Audit result: **PASS**.

## 5. Quantifier and scope checks

1. The note says the **published theorem does not apply** at the critical
   coefficient. It does not say a `d`- or `2d`-partition is nonexistent.
2. The `Theta(W)` barrier concerns adaptations by truncation/refinement and
   the amount of additional rechainization required. It is not a lower
   bound against every new Boolean-lattice construction.
3. Abstract fragments are kept separate from owner-anchored chains. A
   fragment can be contained in an owner without being comparable to other
   fragments assigned to that owner.
4. Owner-anchored chains are kept separate from physical flags. The
   countdown recurrence is an additional adjacency condition on an ordered
   owner chronology.
5. One endpoint partition is kept separate from the two orthogonal endpoint
   systems induced by a word.
6. The Sudakov--Tomon--Wagner comparison is only asymptotic. It does not
   upgrade an `o(Lambda)` exceptional bank to `O(1)`.

Audit result: **PASS**.

## 6. Final audit verdict

**PASS, with the following exact scope.**

The theorem proves that Tomon's explicit `k>500c^2` result operates far
below the coefficient needed for sharp lower chainization. Its largest
certified equal chains leave at least `14.012...W` strict-lower fragments,
so any near-optimal endpoint construction must add at least
`13.012...W-o(W)` cross-fragment joins. It does not prove that such a
global Boolean rechainization is impossible, and it makes no claim of an OR
word.
