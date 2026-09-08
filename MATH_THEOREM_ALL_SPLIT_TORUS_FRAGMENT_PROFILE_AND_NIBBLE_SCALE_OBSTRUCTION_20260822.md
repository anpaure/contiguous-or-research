# All-split torus fragments: exact profile and the independent-residual scale obstruction

**Status (2026-08-22).**  The fragment regularity, codegree bounds, exact
boundary formulas, and scale obstruction below are proved.  They give a
genuine positive improvement over the whole-atom hypergraph: after cutting a
`b^2`-atom into length-`L` cyclic fragments, the usual local-dependence
parameter is

\[
        L\,{\Delta_2\over D_L}\le {4L\over b^2},
\]

which is `o(1)` whenever `L=o(b^2)`.  At the same time, serialization across a
band of `2H+1` ranks costs only `O(Hb/L)` of the middle-layer scale.

These two inequalities leave a nonempty formal window

\[
                         bH\ll L\ll b^2.                 \tag{0.1}
\]

However, this does **not** prove a near-perfect fragment matching.  In the DCC
regime `H=ceil(sqrt(b log b))`, every `L` satisfying the left side of (0.1) is
much larger than the logarithm of the total labelled fragment supply.  An
independently thinned residual then loses all fragment edges after only an
`o(1)` covered proportion.  Equivalently, even the ideal top-codegree term in
the strongest presently available pure-nibble bound is `1+o(1)`.  Thus the
fragment idea gives a sharply scoped no-go for an independent-residual/pure
nibble proof; it does not rule out a globally coordinated matching theorem.

Throughout, let

\[
 b=2h+1\ge5,\qquad M=b^2,\qquad
 \mathcal V={\Omega\choose b},\qquad W=|\mathcal V|={2b\choose b}.
\]

The labelled full atoms are those of
`MATH_THEOREM_ALL_SPLIT_PRODUCT_ATOM_REGULARITY_AND_BOUNDARY_PROFILE_20260822.md`.
There is one extra point which is immaterial for a full atom as a set but
essential after cutting it: cyclic orders modulo rotation do not determine a
unique relative phase between the two periodic streams.  Choosing rooted
representatives gives `b^2` pairs of stream phases.  Rotating the word by one
whole type period translates the two counters by `(h,h+1)`; this order-`b`
subgroup gives exactly the alignments defining the same unrooted cyclic word.
There are no further identifications: the cell-to-subset map is injective and
the unique consecutive `B,B` pair makes the type word primitive, so any
identifying rotation is by a whole number of type periods.  There are
therefore exactly `b` inequivalent relative alignments.  We refine every
original atom label by
`rho in Z_b` and include all relative alignments.  Every phase-refined atom is
a cyclic list

\[
                     C=(C_t)_{t\in\mathbb Z_M}             \tag{0.2}
\]

of `M` distinct middle-layer vertices.  The degree of every middle vertex in
the original labelled full-atom multihypergraph is

\[
                             D=(b!)^2,                     \tag{0.3}
\]

and two vertices at Johnson distance `d` have full-atom codegree

\[
 {\lambda_d\over D}={n_d\over N_d},\qquad
 N_d={b\choose d}^2,qquad
 n_d=4\min(d,b-d)\quad(1\le d\le b-1),                    \tag{0.4}
\]

with `lambda_b=0`.  After phase refinement the degree and pair codegrees are

\[
                    \widehat D=bD,\qquad
                    \widehat\lambda_d=b\lambda_d,        \tag{0.5}
\]

so every normalized profile in (0.4) is unchanged.  This phase refinement is
what makes the fragment family below permutation-equivariant; silently
choosing one representative alignment would not justify the symmetry counts.

## 1. The cyclic-fragment hypergraph

Fix an integer `1<=L<M`.  For every phase-refined labelled full atom `C` and every
`a in Z_M`, retain the start label and define

\[
                F(C,a)=\{C_a,C_{a+1},\ldots,C_{a+L-1}\}.  \tag{1.1}
\]

The resulting labelled multihypergraph on `mathcal V` is denoted
`mathcal G_(b,L)`.  Since the vertices of `C` are distinct, every fragment has
exactly `L` vertices.

### Theorem 1.1 (exact fragment regularity)

`mathcal G_(b,L)` is `L`-uniform and regular of degree

\[
                              D_L=L\widehat D=LbD.          \tag{1.2}
\]

It has exactly

\[
                              W\widehat D=WbD               \tag{1.3}
\]

labelled edges, independently of `L`.

#### Proof

In each phase-refined full atom containing a fixed vertex `S`, exactly `L`
cyclic starts produce a fragment containing `S`.  Equation (1.2) follows from
(0.5).
There are

\[
 bW((b-1)!)^2={W\widehat D\over b^2}
\]

labelled full atoms, and each has `M=b^2` possible starts, proving (1.3).
\(\square\)

For two positions of a cyclic `M`-list at shortest cyclic separation `z`, put

\[
 g_L(z)=(L-z)_+ +(L-(M-z))_+.                            \tag{1.4}
\]

This is exactly the number of length-`L` cyclic fragments containing both
positions.  In the range `L<=M/2` used below it reduces to
`g_L(z)=(L-z)_+`.

### Theorem 1.2 (general pair-codegree bound)

Let `Lambda_(d,L)` be the codegree in `mathcal G_(b,L)` of two distinct
vertices at Johnson distance `d`.  Then

\[
 {\Lambda_{d,L}\over D_L}
 \le {L-1\over L}\,{n_d\over N_d}
 \le {4\over b^2},                                      \tag{1.5}
\]

and consequently

\[
       L\max_{S\ne T}{\deg_{\mathcal G}(S,T)\over D_L}
                         \le {4L\over b^2}.              \tag{1.6}
\]

#### Proof

A phase-refined full atom containing both positions contributes at most `L-1` fragment
starts containing both, since `L<M`.  Hence

\[
             \Lambda_{d,L}\le (L-1)\widehat\lambda_d.
\]

Divide by `L\widehat D` and use (0.4)--(0.5) and the maximum calculation for
the full-atom profile.  \(\square\)

The bound (1.5) is asymptotically sharp in the relevant range.  The next
result records the exact boundary values.  It also verifies that fragmenting
does not remove the two Johnson boundary shells: all four boundary neighbours
of a cell lie within cyclic distance `O(b)`.

### Lemma 1.3 (exact physical boundary-distance census)

Average over a position `C_t` of one torus cycle.  Its four
Johnson-distance-one neighbours have the following shortest cyclic distances:

\[
\begin{array}{c|ccc}
z&1&2b-1&2b+1\\ \hline
\text{mean number}&2&(b+1)/b&(b-1)/b.
\end{array}                                             \tag{1.7}
\]

Its four Johnson-distance-`b-1` neighbours have census

\[
\begin{array}{c|ccc}
z&b-1&b&b+1\\ \hline
\text{mean number}&(b+1)/b&2&(b-1)/b.
\end{array}                                             \tag{1.8}
\]

#### Proof

Index the alternating type word as

\[
                  \tau=B,A,B,A,\ldots,B
\]

at phases `0,1,...,b-1`.  If `t=qb+s`, with `0<=s<b`, the two stream counters
before phase `s`, modulo `b`, are

\[
 \Phi(q,s)=
 \left(qh+\left\lfloor{s\over2}\right\rfloor,
       q(h+1)+\left\lceil{s\over2}\right\rceil\right). \tag{1.9}
\]

This is a bijection from `Z_b^2` to the counter torus.  Solving (1.9) after
adding each of

\[
       (\mathord\pm1,0),(0,\mathord\pm1)                 \tag{1.10}
\]

gives, at every phase except the unique `B,B` junction phase, the multiset

\[
                         \{1,1,2b-1,2b+1\};              \tag{1.11}
\]

at that junction it gives

\[
                         \{1,1,2b-1,2b-1\}.              \tag{1.12}
\]

Each phase occurs at exactly `b` of the `b^2` positions.  This proves (1.7).

Johnson distance `b-1=2h` forces local distance `h` in both factors, so the
four counter displacements are

\[
                         (\mathord\pm h,\mathord\pm h).
\]

The same substitution in (1.9) gives

\[
                         \{b-1,b,b,b+1\}                 \tag{1.13}
\]

away from the junction and

\[
                         \{b-1,b-1,b,b\}                 \tag{1.14}
\]

at the junction.  Averaging proves (1.8).  \(\square\)

### Theorem 1.4 (exact boundary codegrees)

For `1<=L<=M/2`,

\[
 {\Lambda_{1,L}\over \widehat D}
 ={1\over b^2}\left[
 2g_L(1)+{b+1\over b}g_L(2b-1)
          +{b-1\over b}g_L(2b+1)\right],                \tag{1.15}
\]

and

\[
 {\Lambda_{b-1,L}\over \widehat D}
 ={1\over b^2}\left[
 {b+1\over b}g_L(b-1)+2g_L(b)
          +{b-1\over b}g_L(b+1)\right].                 \tag{1.16}
\]

In particular, if `2b+1<=L<=M/2`, then

\[
 {\Lambda_{1,L}\over D_L}
 ={4L-4b-2+2/b\over Lb^2},                              \tag{1.17}
\]

\[
 \boxed{
 {\Lambda_{b-1,L}\over D_L}
 ={4L-4b+2/b\over Lb^2}}                               \tag{1.18}
\]

and (1.18) is the maximum normalized pair codegree of
`mathcal G_(b,L)`.

#### Proof

Count triples `(C,t,T)` with `C_t=S`, `d(S,T)=d`, and weight equal to the
number of fragment starts containing both positions.  The stabilizer of `S`
is transitive on its `N_d` distance-`d` neighbours.  Double counting first
over the `\widehat D` phase-refined full atoms through `S`, and then over `T`,
gives

\[
 {\Lambda_{d,L}\over \widehat D}
 ={1\over N_d}\,{1\over M}
   \sum_{t\in\mathbb Z_M}
   \sum_{\substack{u\ne t\\d(C_t,C_u)=d}}
                         g_L(d_{\rm cyc}(t,u)).           \tag{1.19}
\]

Now `N_1=N_(b-1)=b^2`; substituting (1.7) and (1.8) proves
(1.15) and (1.16).  When `L>=2b+1`, expanding the positive parts gives
(1.17) and (1.18).

For `2<=d<=b-2`, put `u=min(d,b-d)`.  From (1.5),

\[
 {\Lambda_{d,L}\over D_L}
 \le {4u\over {b\choose u}^2}
 \le {8\over b^2(b-1)}.                                \tag{1.20}
\]

For `b>=5` and `L>=2b+1`, the right side of (1.18) is larger than
`8/(b^2(b-1))`.  Finally (1.18) exceeds (1.17) by `2/(Lb^2)`, proving the
maximum claim.  \(\square\)

Thus for `b=o(L)` the exact worst normalized codegree is

\[
       {4\over b^2}\left(1-{b\over L}+O((bL)^{-1})\right), \tag{1.21}
\]

so the factor `4/b^2` in the coarse bound is real, not an artefact.

## 2. The seam window

Assume a matching in `mathcal G_(b,L)` covers `(1-epsilon)W` middle
vertices.  It contains

\[
                         Q={(1-\epsilon)W\over L}         \tag{2.1}
\]

literal FIFO fragments.  Under the near-half connector hypotheses

\[
 f=b+H+2,qquad H=o(b),qquad b\ge3H+5,                  \tag{2.2}
\]

each fragment can be entered from the previous one using `O(b)` emissions.
Charging both the connector and the `O(b)` boundary-crossing starts at every
one of `2H+1` window lengths gives total band damage

\[
                         O\left({HbW\over L}\right).     \tag{2.3}
\]

Consequently fragment serialization has `o(W)` aggregate damage provided

\[
                              {bH\over L}=o(1).           \tag{2.4}
\]

On the other hand (1.6) gives the standard local-dependence condition

\[
                              {L\over b^2}=o(1).          \tag{2.5}
\]

Conditions (2.4) and (2.5) are simultaneously feasible precisely at the
coarse scale `H=o(b)`, yielding (0.1).  For

\[
                         H=\lceil\sqrt{b\log b}\rceil,    \tag{2.6}
\]

one convenient balanced choice is

\[
                         L=\left\lceil b^{3/2}\sqrt H\right\rceil. \tag{2.7}
\]

Both normalized losses in (2.4) and (2.5) are then

\[
                         \Theta\left(\sqrt{H/b}\right)
       =\Theta\left(b^{-1/4}(\log b)^{1/4}\right).       \tag{2.8}
\]

This calculation is only a scale compatibility result; no matching theorem
has yet been used.

## 3. Independent residuals die before macroscopic progress

The formal window (0.1) is incompatible with an independently thinned
residual.  This is an exact first-moment obstruction, not merely a limitation
of a concentration estimate.

### Theorem 3.1 (independent-residual extinction)

Retain every vertex of `mathcal G_(b,L)` independently with probability
`x=x_b`.  Let `Z_x` be the number of labelled fragment edges entirely in the
retained set.  Then

\[
                    \mathbb E Z_x=W\widehat D x^L=WbDx^L, \tag{3.1}
\]

and

\[
                    \log(W\widehat D)=2b\log b+O(b).     \tag{3.2}
\]

In particular, if

\[
              L\log(1/x)-\log(W\widehat D)\longrightarrow+\infty, \tag{3.3}
\]

then with probability tending to one the residual contains no fragment edge.
A convenient stronger sufficient condition is

\[
              L\log(1/x)-2b\log b=\omega(b).             \tag{3.4}
\]

#### Proof

There are exactly `W\widehat D` labelled fragment edges by (1.3), and any one survives
with probability `x^L`, proving (3.1).  Stirling's formula and
`W=binom(2b,b)` give

\[
 \log D=2\log(b!)=2b\log b-2b+O(\log b),
 \qquad \log W=O(b),
\]

which proves (3.2).  Under (3.3), (3.1) tends to zero, so Markov's inequality
finishes the proof.  \(\square\)

### Corollary 3.2 (seam versus independent-residual incompatibility)

Let `H` be as in (2.6), and impose the negligible-seam condition
`L/(bH) -> infinity`.  Then:

1. for every fixed `x<1`, the independent residual has no edge with high
   probability;
2. writing `x=1-theta`, it already has no edge whenever

\[
                         \theta L\gg b\log b;             \tag{3.5}
\]

3. at the minimally seam-compatible scale `L=bH g(b)`, where `g(b)->infinity`,
   the largest covered proportion compatible with the independent-residual
   heuristic is only

\[
        \theta_*=O\left({b\log b\over L}\right)
        =O\left({\sqrt{\log b/b}\over g(b)}\right)=o(1). \tag{3.6}
\]

Therefore an iterative argument whose live hypergraph is comparable to an
induced independent residual cannot cover even a fixed positive fraction of
the middle layer in the seam-compatible fragment range.

#### Proof

The seam assumption and (2.6) imply

\[
 {L\over b\log b}\gg {H\over\log b}
     =\Theta\left(\sqrt{b/\log b}\right)\longrightarrow\infty.
\]

This and Theorem 3.1 prove Item 1.  Since
`log(1/(1-theta))>=theta`, (3.5) implies (3.3), proving Item 2.  Substitution
of `L=bHg(b)` proves (3.6).  \(\square\)

There is an even stronger near-completion incompatibility.  If `x=o(1)`, the
mere first-moment condition needed for a nonempty residual is

\[
                     L\log(1/x)\le 2b\log b+O(b),         \tag{3.7}
\]

whereas negligible band seams require `L/(bH)->infinity`.  For (2.6), these
two inequalities cannot hold simultaneously.

## 4. Why currently available nibble theorems do not close the gap

Classical Frankl--Rödl/Pippenger matching theorems hold with the uniformity
fixed before the degree tends to infinity.  They therefore cannot be applied
directly to `L=L(b)->infinity`.

The 2025 quantitative pure-nibble theorem of Gould and Kelly
([*Advancing the Rödl Nibble*, Theorem 1.4](https://arxiv.org/abs/2511.11375))
allows multihypergraphs and uses the full codegree sequence, but its
hypotheses are again presented in a fixed-uniformity hierarchy.  More decisively, its
matching parameter contains the unavoidable top-codegree bottleneck

\[
              B\le\left({D_L\over C_L}\right)^{1/(L-1)}, \tag{4.1}
\]

where `C_L` is the maximum multiplicity of an `L`-edge.  Even granting the
best possible value `C_L=1`,

\[
 \left(Lb(b!)^2\right)^{1/(L-1)}
 =\exp\left({2b\log b+O(b)+\log L\over L-1}\right)
 =1+o(1)                                                \tag{4.2}
\]

throughout the seam-compatible regime of Corollary 3.2.  Hence that theorem
cannot yield an `o(W)` leftover here.  Formula (4.2) is the theorem-level
counterpart of the elementary extinction calculation (3.1).

This proves the following scoped conclusion.

### Theorem 4.1 (pure-nibble route no-go; coordinated matching remains open)

For `H=ceil(sqrt(b log b))`, cutting all-split torus atoms into fragments can
simultaneously make seam damage `o(W)` and the local parameter
`L Delta_2/D_L=o(1)`.  Nevertheless:

* an independent-residual nibble becomes edge-empty after only `o(1)` covered
  proportion;
* fixed-uniformity Pippenger--Frankl--Rödl theorems do not apply;
* the full-codegree pure-nibble bound remains bottlenecked at `B=1+o(1)` even
  under ideal top codegree.

Thus degree and pair-codegree regularity, by themselves, do not presently
close the central near-factor gate.  A successful fragment proof would need
a globally coordinated packing argument which does not evolve through an
approximately independent residual.  This theorem does not assert that such
a matching is impossible.

Finally, a central fragment near-factor would still not by itself establish
common all-depth coverage.  Adding all `2H+1` nearby-rank windows to each
matching edge raises the effective uniformity by another factor of order
`H`, worsening rather than removing the obstruction above.  Any positive
route must therefore coordinate central packing and multirank collision
control in one non-nibble structure.

## 5. Independent audit of the underlying all-split note

The definitions and all enumerative claims through Corollary 3.1 of
`MATH_THEOREM_ALL_SPLIT_PRODUCT_ATOM_REGULARITY_AND_BOUNDARY_PROFILE_20260822.md`
survive an independent symbolic audit:

* every atom has `b^2` distinct cells;
* the labelled atom count is `W((b-1)!)^2`;
* the exact degree is `(b!)^2`;
* the convolution census is `n_d=4min(d,b-d)`;
* the pair-codegree formula and its unique boundary-shell maximizers are
  correct;
* the link-overlap expectation is `32/b^2+O(b^(-3))`.

Theorem 4.1 has a statement-level omission, not a failure of its counting
argument.  Its `O(b)` connector assertion uses the near-half
permutation-shift theorem, whose needed hypotheses are absent from the
statement.  In the intended DCC application it should explicitly assume

\[
 f=b+H+2,\qquad H=o(b),\qquad b\ge3H+5.                  \tag{5.1}
\]

Under (5.1), the atoms themselves are legal (`b>=H+4` suffices) and the
connector theorem applies.  The phrase saying that every connector-crossing
target is charged to a connector *position* should also include the `O(b)`
window starts straddling each cut boundary; this changes no asymptotic bound.
With these two wording repairs, the central packing reduction is correct.
