# Final audit of the long-run MTF / atom-rounding route

## 1. Outcome

The original ``integral atom-packing theorem'' is no longer the smallest
missing statement.  Two later results remove both ends of that formulation:

* Mütze--Standke--Wiechert already give an **exact** factor of the middle
  layer in odd dimension into cyclic-interval wreaths; and
* `TRUNCATED_IDEAL_PRODUCT.md` covers both outer tails in `o(W)` entries once
  the unresolved half-band has width
  \(H=\sqrt m\,\omega(1)\).

Consequently neither a growing-uniformity near-factor for the middle layer nor
a Poisson reservoir for the deep ranks is required.  The exact remaining
OR-level theorem is a low-collision choice of an exact middle wreath factor.

This note proves an exact incremental-overlap ledger for that choice.  It also
records why every currently audited generic nibble is quantitatively or
logically insufficient.  No new all-dimensional construction is claimed.

Throughout put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m,
 \qquad N_q=\binom n{m-q}.
\tag{1.1}
\]

## 2. What is already integral

For a cyclic order \(\pi=(x_0,\ldots,x_{n-1})\), write

\[
 I_\pi(j,r)=\{x_j,x_{j+1},\ldots,x_{j+r-1}\},
 \qquad j\in\mathbb Z_n.
\tag{2.1}
\]

The Mütze--Standke--Wiechert minimum-change Chung--Feller theorem gives a
family

\[
 \mathcal F=\{\pi_1,\ldots,\pi_B\}
\tag{2.2}
\]

such that the \(nB=W\) sets \(I_{\pi_i}(j,m)\) partition
\(\binom{[n]}m\).  Equivalently, the odd graph \(KG(2m+1,m)\) has an exact
factor into its minimum odd cycles.  Every such cycle is a wreath.  Thus the
middle-block matching problem in `GROWING_NIBBLE.md` and
`PARTIAL_BLOCK_MULTISCALE.md` is obsolete for this odd-dimensional route.

The published MSW factor itself is not vertically complete: it already misses
four first-shadow targets when \(m=4\).  The theorem supplies the correct
horizontal support, not the required vertical factor.

## 3. The weakest exact missing lemma

For an exact middle wreath factor \(\mathcal F\), define its lower depth-
\(q\) colour set and defect by

\[
 \mathcal C_q(\pi)
   =\{I_\pi(j,m-q):j\in\mathbb Z_n\},
 \qquad
 M_q(\mathcal F)
   =N_q-\left|\bigcup_{\pi\in\mathcal F}\mathcal C_q(\pi)\right|.
\tag{3.1}
\]

Every \(\mathcal C_q(\pi)\) has exactly \(n\) members for \(q<m\).  The
upper intervals of length \(m+1+q\) are complements, after a cyclic shift of
the start, of the lower intervals of length \(m-q\).  Hence the upper and
lower missing counts are equal.

### Weak vertical wreath lemma

There are a function

\[
 H=\sqrt{m\,\omega(m)},\qquad
 \omega(m)\longrightarrow\infty,
 \qquad H=o(m^{2/3}),
\tag{3.2}
\]

and exact middle wreath factors \(\mathcal F_m\) such that

\[
 \boxed{\quad
   \sum_{q=1}^{H}M_q(\mathcal F_m)=o(W).
 \quad}
\tag{3.3}
\]

This is the smallest currently isolated sufficient lemma.  It asks only for
coverage.  It does **not** ask for disjoint atoms, an SCD, prescribed quotas,
nested perfect matchings, or even injectivity inside a nonmiddle rank.

### Theorem 3.1 (the weak lemma is sufficient)

If (3.3) holds, then

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{3.4}
\]

#### Proof

For each \(\pi\in\mathcal F_m\), put

\[
 E_j=I_\pi(j,m-H),
\]

and emit

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.
\tag{3.5}
\]

Overlapping cyclic intervals satisfy

\[
 E_j\cup E_{j+1}\cup\cdots\cup E_{j+r}
   =I_\pi(j,m-H+r),\qquad 0\le r\le2H+1.
\tag{3.6}
\]

Thus (3.5) realizes every cyclic interval in all ranks from \(m-H\) through
\(m+1+H\).  The total principal and seam length is

\[
 B(n+2H+1)
  =W+O(HW/n)=W+o(W).
\tag{3.7}
\]

Append every missing central target.  Complement symmetry and (3.3) make
this cost \(o(W)\).  The truncated two-tail construction has length

\[
 O\!\left(\left(1+\frac{H^2}{m}\right)
              \binom{2m}{m-H}\right)=o\!\left(\binom{2m}{m}\right)
\tag{3.8}
\]

under (3.2), and its one-bit lift supplies the odd-dimensional tails in
\(o(W)\) entries.  Hence \(\nu(2m+1)\le W+o(W)\).  The middle-antichain
lower bound gives the reverse asymptotic inequality.  The standard trimmed
one-bit lift transfers the result to the following even dimension.  QED.

The stronger nested-matching theorem in `MSW_ATOM_FLOW.md` would give an
actual cyclic-interval SCD, but it is not needed for (3.4).

## 4. Exact lossless collision ledger

The following identity is the most useful normal form for trying to prove
(3.3).

Order the wreaths arbitrarily as \(\pi_1,\ldots,\pi_B\), put

\[
 U_{i,q}=\bigcup_{t\le i}\mathcal C_q(\pi_t),
 \qquad U_{0,q}=\varnothing,
\]

and define the number of old colours hit by the next wreath by

\[
 o_{i,q}=|\mathcal C_q(\pi_i)\cap U_{i-1,q}|.
\tag{4.1}
\]

### Theorem 4.1 (incremental-overlap identity)

For every exact middle wreath factor and every \(q<m\),

\[
 \boxed{\quad
 M_q(\mathcal F)
  =\sum_{i=1}^{B}o_{i,q}-(W-N_q).
 \quad}
\tag{4.2}
\]

In particular, every summand on the right after aggregation is constrained by

\[
 \sum_i o_{i,q}\ge W-N_q,
\tag{4.3}
\]

and the weak vertical wreath lemma is exactly

\[
 \boxed{\quad
 \sum_{q=1}^{H}
 \left(\sum_i o_{i,q}-(W-N_q)\right)=o(W).
 \quad}
\tag{4.4}
\]

#### Proof

The \(n\) cyclic intervals of a fixed proper length are distinct.  When
\(\pi_i\) is added it therefore contributes exactly \(n-o_{i,q}\) new
colours.  Since \(Bn=W\),

\[
 |U_{B,q}|=W-\sum_i o_{i,q}.
\]

Subtract this from \(N_q\), proving (4.2).  Nonnegativity of \(M_q\) proves
(4.3), and summing (4.2) proves (4.4).  QED.

This is the blockwise version of the linear duplicate identity in
`MSW_ATOM_FLOW.md`.  It shows that ordinary positive-factor expansion is far
too weak: the construction must be lossless up to an additive \(o(W)\)
*after all depths are summed*.

At the first shadow,

\[
 \frac{N_1}{W}=\frac m{m+2},
\]

so the unavoidable total overlap is

\[
 W-N_1=\frac{2W}{m+2}.
\tag{4.5}
\]

Per wreath this is only

\[
 \frac{W-N_1}{B}
   =\frac{2n}{m+2}=4-\frac6{m+2}.
\tag{4.6}
\]

Thus an asymptotically successful factor may repeat only about four
rank-\((m-1)\) colours per \(n\)-term wreath on average.  More generally,
for \(q=o(\sqrt m)\),

\[
 n\left(1-\frac{N_q}{W}\right)=\Theta(q^2)
\tag{4.7}
\]

is the entire collision allowance per wreath.  This is the exact
near-rainbow rigidity that a valid construction must exploit.

## 5. The stronger SCD version

Let \(\Omega\) be the \(W\) pointed starts of a wreath factor and put

\[
 L_q(v)=I_\pi(j,m-q),\qquad
 U_q(v)=I_\pi(j,m+1+q)
\]

for \(v=(\pi,j)\).  Make a labelled bipartite graph \(G_q\) in which start
\(v\) is the edge \(L_q(v)U_q(v)\).  A genuine interval SCD exists exactly
when there are nested sets

\[
 \Omega=A_0\supseteq A_1\supseteq\cdots\supseteq A_H
\]

such that \(G_q[A_q]\) is a perfect matching at every depth.  This is a tower
of ordinary bipartite matchings, but almost every shallow target has degree
one just before its matching is chosen: the fraction allowed degree at least
two is at most

\[
 \frac{N_{q-1}-N_q}{N_q}=\frac{2q}{m-q+1}.
\tag{5.1}
\]

Consequently normalized matching or positive expansion is not enough.  The
incidence graph itself must already be organized as an almost-bijection.

For the OR problem, (3.3) is strictly weaker and should be attacked first.

## 6. Why the audited nibble routes do not close (3.3)

### 6.1 Complete Pascal-strip atoms

One full long-run atom has a two-dimensional Pascal-strip certificate.  Large
rectangles of positions are determined by only their boundary coordinates.
The resulting full-codegree parameter is \(1+o(1)\) when both the row length
and radius grow.  A complete atom therefore cannot be treated as an
unstructured matching edge.

### 6.2 Partial pair-flip blocks

For middle vertices alone, a length-\(2\ell\) partial block has

\[
 \Delta_2/D=2/m^2,
 \qquad B_{\rm full}=\Omega(m/\ell).
\]

This is excellent middle-layer spread, but the middle layer is now solved
exactly by MSW.  Once the first shadow is certified, intended adjacent
chain links create relative codegree \(\Theta(1/m)\), and the edge rank is
\(\Theta(\ell\sqrt m)\).  A middle near-factor does not imply the
lossless collision identity (4.4); a random-looking factor instead leaves a
constant fraction of the first shadow absent.

### 6.3 Antipodal quotient

Before quotienting complements, shallow lower/upper masks are near twins and
the relative codegree tends to one.  After quotienting to antipodal atoms,
the exact typed cyclic-order hypergraph has

\[
 \Delta_2/D=\frac2{m+1},
 \qquad
 \max_{e,v\notin e}\Lambda(e,v)=O(H/n).
\]

This removes the projective-plane obstruction.  It still does not invoke an
available theorem.  The band contains \(\Theta(W\sqrt n)\) atoms, whereas
literal repair permits only \(o(W)\) misses, so the required relative
leftover is

\[
 o(n^{-1/2}).
\tag{6.1}
\]

The pair bottleneck gives at best a nominal full-codegree scale
\(B=O(\sqrt n)\), exactly the boundary \(n^{-1/2}\), before logarithmic
losses.  Moreover the edge rank grows as \(\Theta(n^{3/2})\).  The audited
Pippenger--Rödl, Grable, Vu, Kang--Kühn--Methuku--Osthus, and
Gould--Kelly statements either fix the uniformity or do not give the strict
little-\(o\) rate (6.1).  They cannot be cited diagonally.

### 6.4 Sparse checkpoints

A bounded number of certified depths improves full codegrees, but omitted
ranks are not forced: many distinct two-step chains may funnel through one
intermediate set.  Taking enough checkpoints to leave bounded gaps recreates
the full-strip high-codegree collapse.  Thus checkpoints need an additional
object-specific interpolation theorem.

### 6.5 Standard SCD projections

The Greene--Kleitman and known SCD-compatible Hamilton constructions have a
linear number of prefix-deletion transitions, which are not one-update MTF
moves.  The more precise Mütze--Weber contraction audit leaves
\((1-o(1))W\) MTF path components.  These SCDs are not an `o(W)` repair away
from a rotor resolution.

## 7. Exact status and recommended theorem target

The following are proved:

1. long two-sided residence has an explicit MTF factorization;
2. long-run atoms of every relevant radius exist;
3. their full coordinate orbits satisfy the exact fractional SCD ledger;
4. the odd-dimensional middle layer has an exact wreath factor;
5. arbitrary radii inside a resolved wreath family have negligible total
   initialization cost;
6. both outer tails cost `o(W)` once
   \(H=\sqrt m\,\omega(1)\); and
7. (4.2) is the exact rank-defect ledger.

The remaining statement is (3.3), or equivalently (4.4).  A proof should be
advertised as a **lossless multiscale wreath-factor theorem**, not as a
routine nibble corollary.

The first nontrivial gate is already:

> Find an exact wreath factor of \(\binom{[2m+1]}m\) whose length-
> \((m-1)\) cyclic intervals miss `o(W)` targets, equivalently whose total
> first-shadow overlap exceeds the unavoidable value \(2W/(m+2)\) by only
> `o(W)`.

Solving that gate does not automatically solve larger depths, but failing it
rules out the whole route.  After it, the credible mechanisms are
rank-by-rank absorption or a genuinely lossless randomized greedy algorithm
that tracks the excess in (4.4).  A pseudorandom algorithm which merely
preserves uniform marginals is pointed in the wrong direction: uniform
occupancy has Poisson-scale collisions, while (4.6) permits only `O(1)`
collisions per wreath.

