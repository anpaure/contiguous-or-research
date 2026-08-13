# A deterministic central-rail factor with exponentially small owner leave

**Date:** 2026-08-13  
**Status:** unconditional positive owner-semigroup theorem.  It constructs
an explicit disjoint union of legal period-`2q+1` resident rails covering
all but an exponentially small fraction of the named middle owners.  It
does not yet give bounded leave or preserve the non-owner ticket rows.

## 1. Setup

Let

\[
 R\in\{\lfloor k/2\rfloor,\lceil k/2\rceil\},
 \qquad q=d+1\ge2,\qquad r=2q+1,\qquad c=R-q,         \tag{1.1}
\]

and assume `c>=0` and `r<=k`.  Partition a subset of `[k]` into disjoint
blocks

\[
 T_1\sqcup\cdots\sqcup T_b,
 \qquad |T_j|=r,qquad b=\lfloor k/r\rfloor,          \tag{1.2}
\]

leaving an unrestricted remainder of size less than `r`.

Call an owner `A in binom([k],R)` **hit** if

\[
 |A\cap T_j|=q                                       \tag{1.3}
\]

for at least one block.  Assign a hit owner to its first such block.

## 2. First-hit fibres are complete disjoint shells

For `j in [b]` and a `c`-set

\[
 C\subseteq[k]\setminus T_j,
\]

call `(j,C)` admissible when

\[
 |C\cap T_i|\ne q\qquad(1\le i<j).                  \tag{2.1}
\]

Put

\[
 \mathcal S(j,C)
 =\{C\cup Q:Q\in{T_j\choose q}\}.                  \tag{2.2}
\]

### Lemma 2.1 (complete-fibre property)

Every owner in `S(j,C)` is assigned to block `j`.  Conversely, every
owner assigned to `j` belongs to exactly one such shell.

#### Proof

For `A=C\cup Q` in (2.2), disjointness of the coordinate blocks gives

\[
 |A\cap T_j|=|Q|=q,
 \qquad |A\cap T_i|=|C\cap T_i|\ne q\quad(i<j).
\]

Thus `j` is its first hit.  Conversely, if `j` is the first hit of `A`,
then

\[
 C=A\setminus T_j
\]

has size `R-q=c`, is disjoint from `T_j`, obeys (2.1), and
`A in S(j,C)`.  The core is forced by `A` and `j`.  `square`

### Lemma 2.2 (shell disjointness)

The admissible shells `S(j,C)` are pairwise owner-disjoint.

#### Proof

Shells with the same block index have different forced cores and hence
are disjoint.  Suppose an owner lay in admissible shells with indices
`i<j`.  Membership in the first shell gives `|A cap T_i|=q`.  In the
second representation `A=C' union Q'`, the blocks are disjoint, so

\[
 |C'\cap T_i|=|A\cap T_i|=q,
\]

contradicting admissibility of `(j,C')`.  `square`

## 3. Literal resident rail factor

For every admissible shell, the Mütze--Standke--Wiechert central odd-graph
factor, together with the central-cycle--wreath equivalence, decomposes

\[
 {T_j\choose q}
\]

into all-start cyclic `q`-window decks of period `r=2q+1`.  After adjoining
the common core `C`, these are pure rank-`R` rails.

The period-`2q+1` residence theorem shows that every such rail is closed,
has toggle traces `1^q0^{q+1}`, is biresident at depth `d=q-1`, and has
both immediate palettes and every proper interval row simple.  Lemma 2.2
then gives:

### Theorem 3.1 (first-hit central-shell factor)

The family of all hit owners has an exact factor by pairwise
owner-disjoint, legal, period-`2q+1` resident pure rails.

This is a positive factor: every rail is selected with coefficient one;
there is no signed cancellation or fractional rounding.

## 4. Exact leave and quantitative bound

The uncovered family is exactly

\[
 \mathcal L=
 \left\{A\in{[k]\choose R}:|A\cap T_j|\ne q
        \text{ for all }j\in[b]\right\}.            \tag{4.1}
\]

Writing `s=k-br` for the remainder size, its exact cardinality is the
coefficient

\[
 \boxed{
 |\mathcal L|=[z^R]
 \left((1+z)^r-{r\choose q}z^q\right)^b(1+z)^s.}     \tag{4.1a}
\]

This follows by recording the intersection size in each disjoint block;
it may be useful for a later cover-down analysis.

Let `X subseteq [k]` be obtained by independent fair coin flips.  The
events `|X cap T_j| ne q` are independent, and

\[
 p_q:=\Pr(|X\cap T_j|=q)
 ={2q+1\choose q}2^{-(2q+1)}.                       \tag{4.2}
\]

Conditioned on `|X|=R`, the set `X` is uniform on the owner layer.  Hence

\[
 { |\mathcal L|\over {k\choose R}}
 =\Pr(X\in\mathcal L\mid |X|=R)
 \le { (1-p_q)^b\over\Pr(|X|=R)}.                  \tag{4.3}
\]

Since the central binomial coefficient is maximal among the `k+1`
coefficients in the `k`th row of Pascal's triangle,

\[
 \Pr(|X|=R)={k\choose R}2^{-k}\ge {1\over k+1},      \tag{4.4}
\]

and, by Wallis' inequality,

\[
 p_q
 ={2q+1\over2q+2}{2q\choose q}4^{-q}
 \ge {1\over4\sqrt q}.                              \tag{4.5}
\]

Using `1-x<=e^{-x}` proves the explicit bound

\[
 \boxed{
 { |\mathcal L|\over {k\choose R}}
 \le (k+1)\exp\left(-{\lfloor k/(2q+1)\rfloor
                          \over4\sqrt q}\right).}     \tag{4.6}
\]

In particular, whenever `q=Theta(sqrt(k))`,

\[
 \boxed{
 |\mathcal L|
 \le {k\choose R}\exp[-\Theta(k^{1/4})].}           \tag{4.7}
\]

The harmless polynomial prefactor is absorbed in the exponent.

## 5. Why the construction evades fixed-core divisibility

Within one selected shell, the core is fixed and the complete central
deck has the expected Catalan divisibility.  Globally, however, an owner
chooses among many possible cores according to its first hit:

\[
 C=A\setminus T_j.
\]

Thus different shells have massively overlapping possible core types,
while their **named owner supports** remain disjoint by Lemma 2.2.  The
fixed-core condition

\[
 q\mid {M-1\choose q-1}
\]

is irrelevant: no complete fixed-core fibre is being factored.  This is
an explicit overlapping-core allocation and ordering in one step.

## 6. Exact remaining boundary

The theorem removes the growing-uniformity nibble from the first
near-factor step.  Its leave is `o(W)`, indeed exponentially small as a
fraction of `W`, but remains exponentially large in absolute size.  It is
not yet a bounded-terminal theorem.

Moreover, owner-disjointness of the rails does not automatically imply
global disjointness of all compulsory lower, upper, socket, cap, phase,
or history tickets across distinct shells.  Each individual rail has a
simple proper interval deck, but different cores can still produce the
same named non-owner target.

The next exact positive gate is therefore one of:

1. recursively factor or cover down the structured avoidance family
   (4.1) to a bounded union of whole residual rails;
2. plant a reserve whose activation domain contains every possible leave
   generated by a refined first-hit construction; or
3. augment the first-hit rule with compulsory-ticket rows and prove the
   corresponding cross-shell simplicity.

Within the named-owner semigroup, however, Theorem 3.1 is unconditional
and (4.7) is a genuine near-perfect integral factor.
