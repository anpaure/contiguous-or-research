# Polynomial forbidden matchings can be avoided at polynomial repair cost

**Date:** 2026-08-06  
**Method:** Johnson spectral localization, the two sharp partial-shadow
thresholds, and directed alternating-cycle repair; no computation or search  
**Status:** unconditional graph theorem.  A polynomial protected matching
with a fixed sub-half exposure margin can be extended while avoiding an
arbitrary polynomial matching of forbidden incidences.  Moreover any
ambient completion containing the protected matching can be changed to such
an avoiding completion at polynomial Hamming cost.  This clears any
polynomially specified collection of common-edge endpoint stars, but does
not by itself prove that the iterative collection of all overloaded stars
stays polynomial.

## 1. Setting

Let

\[
 {\cal L}={ [2r-1]\choose r-1},\qquad
 {\cal U}={ [2r-1]\choose r},\qquad
 W=|{\cal L}|=|{\cal U}|,
\tag{1.1}
\]

and let `G` be their inclusion graph.  Let `F` be a matching, with lower
endpoint set `Z`, upper endpoint set `Y`, and

\[
                         f=|F|=|Z|=|Y|.             \tag{1.2}
\]

Use the all-occurrence exposures

\[
 \widehat\alpha(F)=
   \max_{x\in{\cal L}}|N_G(x)\cap Y|,
 \qquad
 \widehat\beta(F)=
   \max_{U\in{\cal U}}|N_G(U)\cap Z|.              \tag{1.3}
\]

Let `E` be a matching of forbidden incidences which is vertex-disjoint from
`F`, and put `s=|E|`.  Edges of a prospective forbidden matching incident
with `V(F)` may always be discarded first: every perfect matching
containing `F` already avoids them.

Fix constants `C<infinity` and `epsilon>0`, and assume

\[
 f+s\le r^C,
 \qquad
 \widehat\alpha(F),\widehat\beta(F)
       \le(1/2-\varepsilon)r.                       \tag{1.4}
\]

All conclusions hold for sufficiently large `r`, depending only on
`C,epsilon`.

## 2. Avoiding extension

### Theorem 2.1 (polynomial forbidden-matching avoidance)

Under (1.4), there is a perfect matching `M` of `G` such that

\[
                         F\subseteq M,
 \qquad
                         M\cap E=\varnothing.       \tag{2.1}
\]

#### Proof

Put

\[
 X={\cal L}\setminus Z,
 \qquad V={\cal U}\setminus Y,
 \qquad B=G[X,V]-E.                                 \tag{2.2}
\]

Suppose `A subseteq X` fails Hall in `B`.  Removing `Y` loses at most `f`
upper vertices from `N_G(A)`.  Removing the `s` edges of `E` can make at
most `s` further upper vertices disappear from the neighbourhood.  Hence

\[
 |N_G(A)|-|A|<f+s.                                  \tag{2.3}
\]

The Johnson spectral-surplus inequality

\[
 |N_G(A)|-|A|
 \ge {2r-1\over r^2}{|A|(W-|A|)\over W}             \tag{2.4}
\]

therefore implies

\[
 \min\{|A|,W-|A|\}< {2r^2\over2r-1}(f+s).          \tag{2.5}
\]

Take an inclusion-minimal failed shore and put `C=N_B(A)`.  Every
`x in A` has at least

\[
 D_\alpha=r-\widehat\alpha(F)-1                    \tag{2.6}
\]

neighbours in `C`: the protected upper bank removes at most
`widehat alpha(F)` neighbours, and the forbidden matching removes at most
one more.  Since `|C|<|A|`, the balanced sharp partial-shadow theorem gives

\[
                         |A|\ge {2D_\alpha-1\choose D_\alpha}.       \tag{2.7}
\]

This is exponential in `r`, contradicting the small alternative in
(2.5).

For the co-small alternative put

\[
 Q=V\setminus N_B(A),\qquad A^c=X\setminus A.       \tag{2.8}
\]

Hall failure and equality of the two residual shore sizes give

\[
                         |Q|\ge|A^c|+1.             \tag{2.9}
\]

Every `U in Q` has at most `widehat beta(F)` facets in `Z`.  Among its
remaining facets in `X`, at most one member of `A` can be hidden by `E`,
because `E` is a matching.  Thus `U` contains at least

\[
 D_\beta=r-\widehat\beta(F)-1                      \tag{2.10}
\]

members of `A^c`.  The strict-imbalance partial-shadow theorem gives

\[
                         |A^c|\ge {2D_\beta-1\choose D_\beta-1}+1.  \tag{2.11}
\]

Again this is exponential, contradicting the co-small alternative in
(2.5).  Hence `B` satisfies Hall.  A perfect matching of `B`, together
with `F`, proves (2.1).  \(\square\)

## 3. The avoiding residual graph is elementary

### Lemma 3.1

The graph `B` in (2.2) is connected.

#### Proof

By Theorem 2.1, `B` has a perfect matching.  If it is disconnected, choose
a component with shores `A,C` of minimum size.  Then

\[
                         |A|=|C|\le(W-f)/2.          \tag{3.1}
\]

Every old neighbour of `A` outside `C` is either in `Y`, or is the upper
endpoint of an edge of `E` which was the only surviving incidence from
`A`.  Therefore

\[
                         |N_G(A)|-|A|\le f+s.        \tag{3.2}
\]

Equations (2.4) and (3.1) imply `|A|=O(r(f+s))`.
On the other hand every member of `A` has at least `D_alpha` neighbours in
`C`, while `|A|=|C|`.  The balanced sharp partial-shadow theorem gives the
same exponential lower bound as (2.7), a contradiction.  \(\square\)

### Lemma 3.2

Every edge of `B` belongs to a perfect matching of `B`.

#### Proof

Let `h` be an edge of `B`.  Force `F+h`, and discard from `E` any edge
incident with `h`.  This changes each exposure in (1.3) by at most one and
keeps the total bank polynomial.  Theorem 2.1, with (say) `epsilon/2` in
place of `epsilon`, gives a perfect matching containing `F+h` and avoiding
the surviving forbidden bank.  Its residual part is a perfect matching of
`B` containing `h`.  \(\square\)

## 4. Directed diameter against a nonavoiding base

Let `N` be an arbitrary perfect matching between `X` and `V`; its edges
need not avoid `E`.  Label the upper shore through `N`, and define

\[
 a\longrightarrow b
 \quad\Longleftrightarrow\quad
 aN(b)\in E(B).                                     \tag{4.1}
\]

Call this digraph `D_N^B`.

### Lemma 4.1 (strong connectivity)

The digraph `D_N^B` is strongly connected.

#### Proof

For an arc corresponding to `h in E(B)`, Lemma 3.2 supplies a perfect
matching `N_h` of `B` containing `h`.  The symmetric difference
`N triangle N_h` is a union of alternating cycles, even when some edges of
`N` lie in `E`.  The cycle containing `h` shows that its arc in `D_N^B`
lies on a directed cycle.

Contracting the pairs of `N` cannot disconnect the connected graph `B`.
Thus the underlying undirected graph of `D_N^B` is connected.  Since every
arc lies on a directed cycle, its strong-component condensation has no
edge.  It therefore has one vertex.  \(\square\)

### Lemma 4.2 (polynomial directed diameter)

One has

\[
 \operatorname {diam}^{\to}(D_N^B)
 \le 8r(f+s)+16r\log W+4
 \le 8r(f+s)+32r^2+4.                               \tag{4.2}
\]

#### Proof

For `S subseteq X`, the bijection `N` gives

\[
                         |\Gamma^+(S)|=|N_B(S)|.     \tag{4.3}
\]

When `|S|<=W/2`, (2.4) and the deletion of at most `f+s` upper
neighbours give

\[
 |\Gamma^+(S)|-|S|\ge {|S|\over2r}-(f+s).           \tag{4.4}
\]

By Lemma 4.1 a forward ball gains at least one new vertex at every step
until it has `4r(f+s)` vertices.  Thereafter (4.4) gives multiplicative
growth by at least `1+1/(4r)` until the ball has more than `W/2`
vertices.  This takes at most

\[
                         4r(f+s)+8r\log W+2          \tag{4.5}
\]

steps.  The complementary-shore argument gives the same bound for a
backward ball.  Two subsets of `X` each having more than `W/2` members
intersect, proving the first inequality in (4.2).  The second follows from
`W<2^(2r-1)`.  \(\square\)

The use of an arbitrary bijection `N` in this section is load-bearing:
the starting completion may itself contain forbidden edges.

## 5. Polynomial-distance clearing

### Theorem 5.1 (avoidance by short alternating repairs)

Let `H` be any perfect matching of `G` containing `F`.  Under (1.4), there
is a perfect matching `M` satisfying (2.1) and

\[
 |M\mathbin\triangle H|
 \le 2s\bigl(8r(f+s)+32r^2+5\bigr).                 \tag{5.1}
\]

#### Proof

Delete `V(F)` and let `N` be the residual part of the current matching,
initially `H-F`.  If `N` contains a forbidden edge `e=N(z)`, then `e` is
not an edge of `B`.  Hence every outgoing arc `z->w` in `D_N^B` has
`w!=z`.  Such an arc exists because `B` has positive minimum degree.

By Lemma 4.2 there is a directed path from `w` back to `z` of length at
most the right side of (4.2).  Together with `z->w` it contains a directed
cycle through `z`.  Switch `N` around a simple directed cycle contained in
that closed walk.  The switch removes `N(z)=e`, introduces only edges of
`B`, and hence introduces no forbidden edge.  It also leaves `F`
untouched.

Each switch removes at least one member of `E` and changes at most twice
`8r(f+s)+32r^2+5` matching edges.  There are at most `s` switches.  The
triangle inequality gives (5.1).  \(\square\)

## 6. Common-star clearing corollary

Fix another perfect matching `J`.  Let
`A subseteq \mathcal L` and `Q subseteq \mathcal U` be any row banks.
Define `E_(A,Q)` to be the edges of
`J` whose upper endpoint contains a member of `A`, or whose lower endpoint
is contained in a member of `Q`.  Remove from this bank every edge incident
with `V(F)`, and assume the remainder is polynomial.

### Corollary 6.1

Every perfect matching `H` containing `F` can be changed at polynomial
Hamming cost into a perfect matching `M` containing `F` such that every
common edge of `M` and `J` incident with a row in `A union Q` is already
forced by `F`.

#### Proof

Apply Theorem 5.1 to the residual matching `E_(A,Q)`.  Any common edge in a
selected row which survives is incident with `V(F)`; since both `M` and
`J` are matchings and `M` contains `F`, such a common edge must itself be
the corresponding edge of `F`.  \(\square\)

## 7. Deleting a whole perfect matching has at most three base components

The local theorem above deliberately forbids only polynomially many edges.
There is nevertheless a useful exact fact about the unavailable extreme in
which a whole perfect matching is deleted.

### Proposition 7.1 (three-component bound)

For every perfect matching `J` of `G`, the regular bipartite graph `G-J`
has at most three connected components.

#### Proof

Let `A,C` be the two shores of one component.  The graph `G-J` is
`(r-1)`-regular, so

\[
                         |A|=|C|.                  \tag{7.1}
\]

Every member of `A` has `r-1` neighbours in `C`.  The balanced sharp
partial-shadow theorem therefore gives

\[
 |A|\ge {2r-3\choose r-1}.                          \tag{7.2}
\]

But

\[
 {W\over {2r-3\choose r-1}}
 ={2(2r-1)\over r}=4-{2\over r}<4.                 \tag{7.3}
\]

Four components would have more than `W` lower vertices.  Hence there are
at most three.  \(\square\)

This does not prove that a protected matching extends inside `G-J`.
Connected regular bipartite graphs need not be highly extendable.  It does
show that the failure of full one-factor avoidance is concentrated in at
most three giant base components, rather than an uncontrolled component
census.  Any successful full-avoidance proof may therefore be organized as
an internal protected-extendability theorem on these components plus an
at-most-three-component balance correction.

## 8. Exact scope for spread damage

Corollary 6.1 proves a strong local statement: any *already specified*
polynomial collection of overloaded common-edge stars can be cleared
without losing the Hamilton-near polynomial-distance property.

It does not prove that repeatedly clearing newly overloaded rows
terminates after polynomially many rows.  A repair cycle can create new
common edges outside the forbidden row bank.  Therefore the theorem does
not yet imply the spread bound

\[
 \max_x|N(x)\cap Y_D|,
 \quad
 \max_U|N(U)\cap Z_D|<r/6.                           \tag{8.1}
\]

What is now isolated is a finite-capacity closure statement rather than a
matching-existence statement:

> choose one polynomial row bank which contains every row that can become
> overloaded during its own short avoiding repair.

Equivalently, prove a bounded-congestion version of the directed cycles in
Theorem 5.1.  Once that row-closure statement is available, the precharged
root-transversal theorem applies and zero common-edge elimination is
unnecessary.
