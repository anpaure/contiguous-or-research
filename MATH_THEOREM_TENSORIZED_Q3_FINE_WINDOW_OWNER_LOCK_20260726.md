# Tensorized octahedral `Q_3` cells: exact owner lock and the surviving fine-window obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 \mathcal V=\binom{\{a,b,c,d\}}2\times
 \{uw,ux,vw,vx\}.
\tag{0.1}
\]

A perfect matching of the octahedral graph \(J(4,2)\), tensored with the
reservoir square, partitions \(\mathcal V\) into three literal \(Q_3\)'s.
Tensoring over \(r\) disjoint blocks partitions \(\mathcal V^r\) into
\(3^r\) cells \(Q_{3r}\).

The extra local direction does **not** remove the labelled
consecutive-window obstruction.  There is an explicit family
\(\mathcal T_{r,q}\) of fine rank-\((4r-q)\) targets, of cardinality

\[
 |\mathcal T_{r,q}|=\binom rq16^q24^{r-q},
\qquad 1\le q\le r,                                      \tag{0.2}
\]

such that, for every vertex-disjoint tiling by product cells

\[
 C=\prod_{i=1}^r(E_i\times R_i),
 \qquad E_i\in E(J(4,2)),                              \tag{0.2a}
\]

including every state-adaptive mosaic made from the local associator
cells, every assignment of an arbitrary cyclic direction order to every
one of its \(3^r\) cells, and every choice of resolution phases, the
number of targets in
\(\mathcal T_{r,q}\) which can even be the lower face of a consecutive
length-\(q\) window is at most

\[
 3^r(r-q+1)4^q8^{r-q}.                                  \tag{0.3}
\]

Equivalently, the reachable fraction is at most

\[
 \boxed{
 \left(\frac34\right)^q
 \frac{r-q+1}{\binom rq}.}                              \tag{0.4}
\]

This bound already allows both a different local matching box and a
different Hamming order from cell to cell.  It is therefore stronger than
the old common-order and product-corner bounds.

If \(K\) different product-cell mosaics are made available, with arbitrary
cellwise orders in every mosaic, covering a \((1-\epsilon)\)
fraction of this fine family requires

\[
 \boxed{
 K\ge (1-\epsilon)\left(\frac43\right)^q
       \frac{\binom rq}{r-q+1}.}                       \tag{0.5}
\]

At \(q=\Theta(\sqrt m)\), this is exponential in \(\sqrt m\) whenever
\(r=\Theta(\sqrt m)\), and it is
\(\exp(\Theta(q\log(r/q)))\) when \(q=o(r)\).

There are two qualifications.

* Directly resolving a \(Q_{3r}\) into isometric \(C_{6r}\)'s is
  arithmetically impossible: a vertex partition would require
  \(6r\mid2^{3r}\).  Adding spectator axes until the dimension is a power
  of two repairs this divisibility, but does not change (0.3)--(0.5).
* The theorem is a sharp no-go for the **fixed tensor-sector product-cell**
  lane.  The family (0.2) is not asserted to have positive density in the entire
  ambient middle layer.  Cross-sector routing can evade the theorem, but
  it must break the unique-cell carrier lock proved below, for example by
  using non-product carriers.

## 1. One octahedral matching gives three literal cubes

Write

\[
 J=J(4,2),\qquad R=Q_2
\]

where the vertices of \(J\) are the six two-subsets of
\(\{a,b,c,d\}\), and two vertices are adjacent when their intersection
has size one.  Let \(M\) be a perfect matching of \(J\).  For an edge
\(E=\{X,X'\}\in M\), put

\[
 \ell(E)=X\cap X'.                                      \tag{1.1}
\]

Then

\[
 E\times R                                               \tag{1.2}
\]

is a literal \(Q_3\): its three axes exchange the two noncommon special
coordinates in \(X,X'\), exchange \(u,v\), and exchange \(w,x\).
Because the three edges of \(M\) partition \(V(J)\),

\[
 \mathcal V=\mathop{\dot\bigcup}_{E\in M}(E\times R)    \tag{1.3}
\]

is a partition into three \(Q_3\)'s.

The companion classification theorem
`MATH_THEOREM_LOCAL_V_Q3_RESOLUTION_CLASSIFICATION_20260726.md` proves
that every three-\(Q_3\) partition of \(\mathcal V\) is of this form.
There are exactly eight: among their \(\binom82=28\) unordered pairs,
sixteen are edge-disjoint and give connected three-versus-three ownership
associators, while twelve share one complete \(Q_3\) and reduce after its
cancellation to a connected two-versus-two associator.

### Lemma 1.1 (the omitted singleton)

The three values \(\ell(E)\), \(E\in M\), are distinct.  Thus there is
a unique

\[
 o(M)\in\{a,b,c,d\}                                     \tag{1.4}
\]

which is not equal to \(\ell(E)\) for any \(E\in M\).

#### Proof

For a fixed special coordinate \(z\), precisely three vertices of
\(J(4,2)\) contain \(z\).  Two vertex-disjoint matching edges with
intersection label \(z\) would require four distinct such vertices.
Hence two edges of \(M\) cannot have the same intersection label.  There
are three edges and four labels, proving the claim. \(\square\)

Consequently a local lower target

\[
 \{z\}\cup Y,\qquad Y\in\{uw,ux,vw,vx\},               \tag{1.5}
\]

is the lower face of a special axis of (1.3) if and only if
\(z\ne o(M)\).  When it exists, both the matching edge and the \(Q_3\)
cell producing it are unique.

## 2. Tensor cells and the exact divisibility mismatch

Take \(r\) disjoint copies of the eight-coordinate block and choose a
perfect matching \(M_i\) in block \(i\).  Tensoring (1.3) gives

\[
 \mathcal V^r
  =\mathop{\dot\bigcup}_{(E_1,\ldots,E_r)\in
                         M_1\times\cdots\times M_r}
       \prod_{i=1}^r(E_i\times R_i).                    \tag{2.1}
\]

There are \(3^r\) cells, and every cell is a literal \(Q_{3r}\).  Give
its axes the abstract labels

\[
 s_i, u_i, w_i\qquad(1\le i\le r),                   \tag{2.2}
\]

where \(s_i\) is the special matching edge in block \(i\), and
\(u_i,w_i\) are the two reservoir axes.

We shall also allow the following state-adaptive version.

### Definition 2.1 (hybrid product-cell mosaic)

A hybrid mosaic is a vertex partition of \(\mathcal V^r\) into cells

\[
 C=\prod_{i=1}^r(E_i\times R_i),                       \tag{2.2a}
\]

where each \(E_i\) is an arbitrary edge of the local \(J(4,2)\).  The
choice of \(E_i\) may depend on the whole global cell; no fixed matching
\(M_i\) is assumed.  Every cell has \(8^r\) vertices, so every hybrid
mosaic has exactly

\[
 \frac{24^r}{8^r}=3^r                                  \tag{2.2b}
\]

cells.  The fixed tensor corners in (2.1) are special cases.

An isometric \(C_{2h}\) in \(Q_h\) has transition word \(\sigma\sigma\)
for a permutation \(\sigma\) of its \(h\) axes.  A vertex resolution by
such cycles requires

\[
 2h\mid2^h,                                             \tag{2.3}
\]

and hence \(h\) is a power of two.  With \(h=3r\), condition (2.3) is
impossible because the left side has a factor three and the right side
does not.

One may append \(d\) spectator \(Q_1\)-axes so that

\[
 h=3r+d=2^t.                                            \tag{2.4}
\]

The power-of-two cube theorem then supplies a vertex resolution in every
extended cell, for every prescribed cyclic permutation of its axes.  All
arguments below permit arbitrary spectator axes.  Since the targets under
study force windows consisting solely of the \(s_i\)'s, spectators cannot
weaken the resulting bound.  Formally, fix one orientation of every
spectator pair in the target family.  A window avoiding the spectator axes
must retain that orientation, so all target and carrier counts below are
unchanged.

## 3. A fine target family whose carrier cell is unique

Fix \(1\le q\le r\).  Define \(\mathcal T_{r,q}\) as follows.  Choose a
set \(I\in\binom{[r]}q\).  In every block \(i\in I\), choose

\[
 T_i=\{z_i\}\cup Y_i,qquad
 z_i\in\{a_i,b_i,c_i,d_i\},\quad Y_i\in R_i.            \tag{3.1}
\]

There are \(4\cdot4=16\) choices.  In every block \(i\notin I\), choose
an arbitrary middle state

\[
 T_i=X_i\cup Y_i\in\mathcal V_i,                       \tag{3.2}
\]

giving \(24\) choices.  The union of the local restrictions has rank
\(4r-q\), and

\[
 |\mathcal T_{r,q}|=\binom rq16^q24^{r-q}.              \tag{3.3}
\]

An arbitrary fixed outside core may be adjoined without changing any
count or argument.

### Lemma 3.1 (unique-cell carrier)

Relative to the tensor partition (2.1), a target \(T\in\mathcal T_{r,q}\)
can be produced by a \(q\)-window only if

\[
 z_i\ne o(M_i)\qquad(i\in I).                           \tag{3.4}
\]

If (3.4) holds, then the product cell which could carry the window is
unique, and the window is forced to use exactly the axes

\[
 S_I=\{s_i:i\in I\}.                                    \tag{3.5}
\]

#### Proof

In a touched block, a reservoir-axis lower face contains a special
two-set, whereas (3.1) contains only one special coordinate.  Hence the
used direction must be the special axis.  Lemma 1.1 says that this axis
exists precisely under (3.4), and then its matching edge is unique.

In an untouched block, the middle vertex \(X_i\cup Y_i\) belongs to the
unique matching edge of \(M_i\) incident with \(X_i\).  Thus every local
cell, and hence the product cell, is fixed.  Since the rank deficit is
exactly one in each block of \(I\) and zero elsewhere, the direction set
is exactly (3.5). \(\square\)

For each fixed \(I\), condition (3.4) leaves \(3\cdot4=12\) choices in
every touched block.  Therefore the number of targets compatible with the
tensor partition before imposing consecutiveness is exactly

\[
 \binom rq12^q24^{r-q}
   =\left(\frac34\right)^q|\mathcal T_{r,q}|.            \tag{3.6}
\]

Moreover these compatible targets are partitioned by their unique carrier
cells.  In a fixed product cell and for a fixed touched set \(I\), their
number is

\[
 4^q8^{r-q}.                                            \tag{3.7}
\]

Indeed, in a touched block the special lower singleton is fixed by the
cell and only the four reservoir orientations vary; in an untouched block
any of the eight cell vertices may occur.

The preceding conclusion does not require one globally fixed matching in
each block; we now use the hybrid mosaics of Definition 2.1.

### Lemma 3.2 (mosaic owner lock)

In an arbitrary hybrid product-cell mosaic, a target
\(T\in\mathcal T_{r,q}\) has at most one carrier cell.  For every fixed
\(I\in\binom{[r]}q\), the exact number of targets having a carrier is

\[
 3^r4^q8^{r-q}.                                        \tag{3.9}
\]

Consequently the fraction having any carrier, before imposing
consecutiveness, is exactly \((3/4)^q\).

#### Proof

Suppose two product cells \(C,C'\) both carried the same target.  In a
touched block \(i\in I\), their special edges \(E_i,E'_i\) would both
have intersection label \(z_i\).  The three vertices of \(J(4,2)\)
which contain \(z_i\) form a triangle, so any two of its edges share a
vertex.  Thus \(E_i\cap E'_i\ne\varnothing\).  In an untouched block,
both special edges contain the prescribed vertex \(X_i\).  The reservoir
factor is the full \(R_i\) on both sides.  Choosing a common special
vertex in every touched block and the prescribed vertex in every
untouched block therefore gives a vertex of \(C\cap C'\), contradicting
the disjointness of the mosaic.  The carrier is unique.

For fixed \(I\), each cell carries exactly \(4^q8^{r-q}\) targets, by
the same local count as (3.7).  Uniqueness makes these target sets
disjoint across the \(3^r\) cells, proving (3.9).  Finally,

\[
 \frac{\binom rq3^r4^q8^{r-q}}
      {\binom rq16^q24^{r-q}}
 =\left(\frac34\right)^q.                            \tag{3.10}
\]

This proves the last assertion. \(\square\)

## 4. How many all-special windows can one order expose?

### Lemma 4.1 (cyclic run bound)

Let a cyclic order contain the \(r\) distinguished symbols
\(s_1,\ldots,s_r\), together with at least one nondistinguished symbol.
Then at most

\[
 r-q+1                                                   \tag{4.1}
\]

of the sets \(S_I\), \(I\in\binom{[r]}q\), occur as a cyclic interval
of length \(q\).

#### Proof

Break the distinguished positions into cyclic runs of lengths
\(\ell_1,\ldots,\ell_t\).  A length-\(q\) interval containing only
distinguished symbols lies in one run, so their number is

\[
 \sum_{j=1}^t(\ell_j-q+1)_+.
\]

If no term is positive the result is immediate.  Otherwise, summing only
over the positive terms gives at most

\[
 \sum_j\ell_j-(q-1)\le r-q+1.
\]

Equality is attained by putting all \(s_i\)'s in one consecutive run.
\(\square\)

In a \(Q_{3r}\) cell the \(2r\) reservoir axes provide the required
nondistinguished symbols.  Additional spectator axes do not affect the
bound.  Since every isometric maximal cycle has word \(\sigma\sigma\),
its length-\(q\) direction sets are precisely the cyclic \(q\)-intervals
of \(\sigma\).  Repetition of the order gives a second occurrence, not a
new direction set.

## 5. The exact tensor no-go

### Theorem 5.1 (cell-adaptive fine-window bound)

Fix an arbitrary hybrid product-cell mosaic \(\mathscr P\).  In every one of
its product cells, choose independently and arbitrarily:

1. any number of spectator axes needed for a legal power-of-two cube;
2. any cyclic order of all cell and spectator axes;
3. any vertex-resolution phase class having that order.

Then the number of distinct targets in \(\mathcal T_{r,q}\) which can be
produced by a consecutive length-\(q\) window is at most (0.3), and hence
their fraction is at most (0.4).

#### Proof

By Lemma 3.2, every compatible target belongs to a unique carrier cell and
forces a set \(S_I\) of special axes.  Lemma 4.1 permits at most
\(r-q+1\) such touched sets in that cell.  For each one, (3.7) gives at
most \(4^q8^{r-q}\) candidate targets.  There are \(3^r\) cells, so the
number reachable is at most

\[
 3^r(r-q+1)4^q8^{r-q}.
\]

Dividing by (3.3) gives

\[
 \frac{3^r(r-q+1)4^q8^{r-q}}
      {\binom rq16^q24^{r-q}}
 =\left(\frac34\right)^q
   \frac{r-q+1}{\binom rq}.
\]

Resolution phases can only remove or repeat candidate affine faces; they
cannot create a noninterval direction set or move a target to a different
cell. \(\square\)

### Corollary 5.2 (number of product-cell mosaics required)

Suppose \(K\) possibly different hybrid product-cell mosaics are used, and
allow arbitrary cellwise cyclic orders and phase classes in every one.
The union of their reachable subsets of \(\mathcal T_{r,q}\) has size at
most \(K\) times (0.3).  Hence covering a \((1-\epsilon)\)-fraction
requires (0.5).

This applies in particular to any bounded collection of alternative
octahedral associator shores, including state-adaptive box mosaics obtained
by switching disconnected ownership components.  Changing local perfect
matchings changes omitted singletons and physical special edges; within a
vertex-disjoint product-cell tiling it never removes the unique-cell
carrier law.

### Proposition 5.3 (all \(8^r\) corners evade the count only collectively)

For every \(T\in\mathcal T_{r,q}\), exactly

\[
 6^q8^{r-q}                                             \tag{5.1}
\]

of the standard \(8^r\) tensor corners are locally compatible with \(T\).
Moreover, for all sufficiently large \(r\), one can assign cyclic
direction orders separately to every cell occurrence in all \(8^r\)
corners so that every target in \(\mathcal T_{r,q}\) has its forced set
\(S_I\) consecutive in at least one compatible corner.

#### Proof

In a touched block with singleton label \(z\), there are three
octahedral edges centred at \(z\).  Every octahedral edge belongs to
exactly two of the eight perfect matchings, and one matching cannot contain
two edges with the same centre.  Hence exactly six local matchings are
compatible.  An untouched middle state belongs to a unique cell in every
one of the eight local partitions.  Independence over blocks proves
(5.1).

For every cell occurrence in every corner, put its \(r\) special axes in
one consecutive run, in a uniformly random order, and put all reservoir
and spectator axes in the complementary run.  For a fixed
\(I\in\binom{[r]}q\), the probability that \(S_I\) is an interval is

\[
 p_{r,q}=\frac{r-q+1}{\binom rq}.                       \tag{5.2}
\]

Thus a fixed target has mean number of favorable compatible corners

\[
 \mu_{r,q}
 =6^q8^{r-q}\frac{r-q+1}{\binom rq}
 =8^r\left(\frac34\right)^q
       \frac{r-q+1}{\binom rq}.                         \tag{5.3}
\]

For \(q\le r\), the inequalities
\(\binom rq\le2^r\), \((3/4)^q\ge(3/4)^r\), and
\(r-q+1\ge1\) give

\[
 \mu_{r,q}\ge3^r.                                      \tag{5.4}
\]

The miss probability of a fixed target is at most
\(e^{-\mu_{r,q}}\).  Also

\[
 |\mathcal T_{r,q}|
 \le2^r24^r=48^r.                                      \tag{5.5}
\]

Therefore

\[
 |\mathcal T_{r,q}|e^{-\mu_{r,q}}
 \le48^r e^{-3^r}<1
\]

for all sufficiently large \(r\).  The union bound proves the existence
of the asserted order assignment. \(\square\)

Proposition 5.3 is only a direction-support statement; Hamming phase
selection and physical affine-face multiplicities remain additional
constraints.  More importantly, the \(8^r\) corners are \(8^r\) different
vertex partitions of the same middle support.  Using them all
simultaneously repeats every middle owner \(8^r\) times.  The proposition
therefore does not give a coefficient-one factor.  Theorem 5.1 shows that
fusing their choices into any single vertex-disjoint mosaic of literal
product cells restores the no-go (0.4).

## 6. Gaussian-depth asymptotics

The exact reciprocal of (0.4) is

\[
 \left(\frac43\right)^q
 \frac{\binom rq}{r-q+1}.                              \tag{6.1}
\]

If \(q=o(r)\), Stirling's formula gives

\[
 \log\binom rq
   =q\log\frac rq+q+O\left(\frac{q^2}{r}+\log(q+1)\right).\tag{6.2}
\]

Consequently

\[
 \begin{aligned}
 \log\frac{|\mathcal T_{r,q}|}{\#\text{ reachable}}
 \ge{}&q\log\frac rq+\bigl(1+\log(4/3)\bigr)q\\
     &-O\left(\frac{q^2}{r}+\log r+\log(q+1)\right).
 \end{aligned}                                         \tag{6.3}
\]

At \(q=A\sqrt m+O(1)\) and \(q=o(r)\), the right side is
\((1+o(1))q\log(r/q)+O(q)\).  If \(r=cq+O(1)\), with \(c\ge1\) fixed,
then instead

\[
 \log\frac{|\mathcal T_{r,q}|}{\#\text{ reachable}}
 \ge \left(cH(1/c)+\log(4/3)\right)q-O(\log q),          \tag{6.4}
\]

where \(H(x)=-x\log x-(1-x)\log(1-x)\).  Thus the loss is exponential
throughout the mesoscopic regime \(q=\Theta(\sqrt m)\), whether
\(r=\Theta(q)\) or \(q=o(r)\).

## 7. Why an unlabelled direction design gives a false positive

If carrier labels are forgotten, the \(3^r\) product cells look like a
large reservoir of independent orders.  This remains true after the
divisibility repair.  Put \(N=3r\), place all added spectator axes in one
consecutive block, and in every cell choose an independent uniform linear
order of the \(N\) genuine axes in the complementary block.  For a fixed
abstract \(q\)-set \(D\subset[N]\), the number of cell orders in which
\(D\) is a genuine interval has mean

\[
 \mu=3^r\frac{N-q+1}{\binom Nq}.                        \tag{7.1}
\]

When \(q=o(r)\),

\[
 \log\mu=r\log3-o(r),                                  \tag{7.2}
\]

so Chernoff's inequality and a union bound give a choice of the cell
orders for which every abstract \(q\)-set has
\((1+o(1))\mu\) occurrences.  Thus the unlabelled direction histogram
really can be mixed.

Theorem 5.1 identifies why this does not solve the physical problem.  A
fine target cannot choose whichever cell happened to receive a favorable
order.  Lemma 3.2 fixes its carrier cell first; that one cell exposes only
\(r-q+1\) of its \(\binom rq\) forced all-special direction sets.  The
missing information is precisely the joined owner/cell label.

## 8. Proved boundary

The three-\(Q_3\) partition is therefore useful but not by itself a
constant-one bypass.

* It raises the local cube dimension from two to three.
* It gives exponentially many product cells and enough entropy to balance
  **unlabelled** direction histograms when \(q=o(r)\).
* It does not balance labelled consecutive windows, even with arbitrary
  cell-adaptive orders inside any one vertex-disjoint product-cell mosaic.
  The exact loss is (0.4).
* The replicated library of all \(8^r\) corners has enough entropy to
  cover the direction support collectively.  Its failure is coefficient
  one: it uses every middle owner \(8^r\) times.

A successor construction must violate at least one hypothesis used in
Lemma 3.2.  Concretely, it must leave the vertex-disjoint product-cell
model, give a fine lower target several different carriers in one integral
factor, or route the target from other middle macrosectors.  Merely
replicating alternative perfect matchings, spectator directions,
resolution phases, or independently chosen orders does not produce a
coefficient-one fusion.
