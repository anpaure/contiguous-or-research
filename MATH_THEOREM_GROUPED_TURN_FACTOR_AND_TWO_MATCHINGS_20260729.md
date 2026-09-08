# Grouped-turn factor theorem and the two-matching fibre

Let (k=2m+1), let (ho) be cyclic rotation, and quotient the containment
graph between rank (m) and rank (m+1) by ⟨ρ⟩.  The central action is
free for every odd (k): a nontrivial stabilizer order would divide one of
(m,m+1) and also (2m+1).  Hence both quotient shores have
(N=inom{k}{m}/k) vertices and the quotient incidence graph (B) is
((m+1))-regular (with voltage-labelled edges).

## Theorem 1 (grouped sigma master is exact)

For each lower vertex (X), choose an unordered pair of its (m+1)
incidence edges.  For an upper vertex (V) and (ain V), let

\[
e_{V,a}=1
\quad\Longleftrightarrow\quad
\text{the selected incidence edge at physical neighbour }V\setminus\{a\}
\text{ is present}.
\]

Then the following are equivalent.

1. Every upper vertex has \(\sum_{a\in V}e_{V,a}=2\).
2. The selected incidence edges form a spanning 2-factor of (B).
3. Their physical voltage lift is a disjoint union of Johnson cycles which
   partitions every rank-((m+1)) set exactly once and uses every rank-(m)
   colour exactly once.

Moreover, if

\[
y_{V,\{a,b\}}=e_{V,a}e_{V,b},
\]

then exactly one of the \(\binom{m+1}{2}\) turn bits at (V) is one, and
its lower-(q_2) colour is literally

\[
V\setminus\{a,b\}.
\]

At a lower vertex (X), the selected pair has upper-(q_1) colour
(X\cup\{a,b\}).  Thus complete upper-(q_1) and lower-(q_2) coverage are
ordinary OR constraints on, respectively, the lower choice bits and the upper
turn bits.

This remains exact for quotient loops and for nonfree *shadow* orbits.  A hit
on one shadow representative covers all its distinct translates; no quotient
load-at-most-two interpretation is used on a short orbit.

## Theorem 2 (two-perfect-matching normal form)

Every binary point of Theorem 1 decomposes as

\[
F=P\sqcup Q,
\]

where (P,Q) are edge-disjoint perfect matchings of (B).  Conversely, every
such pair gives a binary point of the grouped master.  If (F) has (c)
connected quotient components, it has exactly (2^c) labelled decompositions
((P,Q)), obtained by independently swapping the alternating colours on each
component.

*Proof.*  A 2-regular bipartite component is an even cycle, so its edges have
exactly two alternating 2-colourings.  Each colour meets every vertex once.
The converse is immediate. □

Consequently the historical fixed-(M_0) model is one affine slice (P=M_0)
of the full grouped factor fibre.  Allowing both matchings is not a new
combinatorial object; it removes precisely that slice condition.  Adding
variables (p_e,q_e) with

\[
p_e+q_e=e_e,
\qquad
\sum_{e\ni v}p_e=\sum_{e\ni v}q_e=1
\]

is therefore a redundant, proof-safe propagation strengthening of the exact
factor master.

## Search consequence at (k=15)

The exact meaningful variable census is

\[
12012\ \text{lower choices}
+3432\ \text{incidence bits}
+12012\ \text{turn bits}
=27456.
\]

The optional matching labels add (2\cdot3432=6864) variables but no
restriction.  The fixed-(M_0) double-shadow factor proves that the two
palette constraints are jointly feasible; its remaining defect is residence
(1,110 short runs in the best retained fixed-(M_0) factor).  Hence the exact
experimental question is now sharply isolated:

> Does leaving both perfect matchings variable permit residence four while
> preserving the two complete turn palettes?

The 224 lower-orbit choices meeting all retained fixed-(M_0) residence-defect
windows form the first exact LNS for this question.  SAT in that neighbourhood
would be a genuine improvement over the fixed slice; UNSAT would certify only
that frozen boundary, not the full factor fibre.

