# Higher placeholder cubes do not cross maximal ordered-core sectors

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external theorem is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-H,\qquad c=2H.
\tag{0.1}
\]

Thus

\[
                         c+d=M,\qquad c+2d=n.
\tag{0.2}
\]

Partition the coordinates as

\[
 [n]=C\sqcup
 \bigsqcup_{j=1}^{d}\{a_{j,0},a_{j,1}\},
 \qquad |C|=c,
\tag{0.3}
\]

and form the maximal Boolean top cell

\[
 \mathcal Q(C)=
 \left\{
 U_\epsilon=
 C\cup\{a_{j,\epsilon_j}:1\le j\le d\}:
 \epsilon\in\{0,1\}^d
 \right\}.
\tag{0.4}
\]

Every top in this cell contains the fixed \(2H\)-set \(C\) and one
label from each complementary pair.

Allow the complete audited move library:

1. every fixed-core directed cycle exchange;
2. every coherent \(2^r\)-corner placeholder cube,
   \(2\le r\le d\);
3. arbitrary permutations of the \(r\) variable placeholders in such a
   cube; and
4. common phase deletion and arbitrary common nested tag schedules.

This note proves the following.

1. **Every cube in the cell fixes the ordered core.**  If all corners of
   an abstract placeholder cube lie in \(\mathcal Q(C)\), each of its
   varying label pairs is one of the pairs in (0.3).  Its common core
   therefore contains \(C\).  Every allowed move fixes every label of
   \(C\) at its old cyclic position.

2. Hence the histogram of induced cyclic orders on \(C\), separately at
   every top, is an exact invariant of all cycle and higher-cube moves,
   in every dimension.  This is a positional, nonabelian invariant; it
   is not a target-load marginal.

3. The invariant is nontrivial inside an exact all-depth load fibre.
   Choose three labels of \(C\) in three positions and alternate over
   their six permutations.  The sum of the three even-permutation frame
   columns equals the sum of the three odd-permutation columns at every
   phase and every interval length.  Nevertheless the two shores have
   disjoint ordered-core histograms.

4. Applying this six-frame antisymmetrizer at every one of the \(2^d\)
   tops gives two exact frame tables with identical top, middle,
   entrance, and nested loads.  They are disconnected even after all
   coherent placeholder cubes of all available dimensions are admitted.

5. This obstruction is invisible to the previous affine top-sign
   parity sector.  The switch occurs at all \(2^d\) corners; every fixed
   core coordinate occurs \(2^d\) times and every paired coordinate
   occurs \(2^{d-1}\) times.  All these multiplicities are even.

Thus higher placeholder cubes do not by themselves connect different
ordered-core/template sectors.  The first surviving invariant is the
free-abelian ordered-core histogram, or equivalently its nonabelian
permutation representation before abelianization.

The construction is a rigorous Markov-basis obstruction on a maximal
Boolean face.  Its total promotion mass is

\[
                         3M2^{m-H}=o(W).
\tag{0.5}
\]

It therefore does not refute an \(o(W)\)-exception connectivity theorem
for the full one-frame-at-every-top table.  A global positive theorem
must, however, contain moves which explicitly change the common-core
order; enlarging only the number of placeholder coordinates cannot do
so.

## 1. The maximal Boolean face

For \(\epsilon\in\{0,1\}^d\), let

\[
                         R_\epsilon=[n]\setminus U_\epsilon
 =\{a_{j,1-\epsilon_j}:1\le j\le d\}
\tag{1.1}
\]

be the corresponding root.  Fix a rooted cyclic positional word on

\[
                         C\cup\{P_1,\ldots,P_d\}.
\tag{1.2}
\]

A labelled template substitutes \(a_{j,\epsilon_j}\) for \(P_j\) and
places the labels of \(C\) in the ordinary positions.

Let \(\mathcal E_{\mathcal Q}\) be the set of all such labelled frame
columns, with any chosen common retained-phase and nested tag schedule.
We impose top multiplicity zero outside \(\mathcal Q(C)\).  This is an
ordinary face of the global nonnegative frame-table configuration:

\[
 x_e=0\qquad
 (e\text{ based on }U\notin\mathcal Q(C)).
\tag{1.3}
\]

Any Markov move applicable on this face must have all of its positive
and negative top corners in \(\mathcal Q(C)\).

## 2. Every internal cube contains the fixed core

### Lemma 2.1 (coordinate-cube rigidity)

Let

\[
 V_\eta=D\cup\{x_{r,\eta_r}:1\le r\le s\},
 \qquad\eta\in\{0,1\}^s,
\tag{2.1}
\]

be an abstract top cube whose \(2^s\) corners all lie in
\(\mathcal Q(C)\).  Then

\[
                         C\subseteq D,
\tag{2.2}
\]

and, after reindexing, every varying pair
\(\{x_{r,0},x_{r,1}\}\) is one of the ground pairs
\(\{a_{j,0},a_{j,1}\}\).

#### Proof

Two adjacent corners of (2.1) differ by deleting one label \(x_{r,0}\)
and inserting \(x_{r,1}\).  Two adjacent tops of \(\mathcal Q(C)\)
differ in exactly the same way in one and only one ground pair of
(0.3).  Hence \(x_{r,0},x_{r,1}\) are the two labels of that ground
pair.  Distinct cube directions change distinct ground pairs.

Every label of \(C\) belongs to every top in \(\mathcal Q(C)\), and
therefore to every corner of (2.1).  Their intersection is the cube
core \(D\), proving (2.2). \(\square\)

The lemma applies equally to a two-dimensional quartet, a directed
cycle exchange supported on pair tops, and the full \(d\)-dimensional
cube.

## 3. The ordered-core histogram

Let \(\mathfrak O(C)\) be the set of rooted cyclic orders on \(C\).
One may instead quotient by reversal; the arguments below remain valid
after choosing four fixed anchor labels to destroy accidental dihedral
identifications.

For a frame column \(e\) on \(U_\epsilon\), let

\[
                         \operatorname {ord}_C(e)\in\mathfrak O(C)
\tag{3.1}
\]

be the cyclic order induced by deleting every label outside \(C\).

For an integer frame table \(x\), define, separately at each corner,

\[
 \Theta_{C,\epsilon}(x)=
 \sum_{e\text{ on }U_\epsilon}
 x_e\,[\operatorname {ord}_C(e)]
 \in\mathbb Z[\mathfrak O(C)].
\tag{3.2}
\]

### Theorem 3.1 (all-cube ordered-core invariance)

Every fixed-core cycle move and every coherent higher placeholder cube
move applicable on the face (1.3) preserves

\[
                         \Theta_C(x)=
 \bigl(\Theta_{C,\epsilon}(x)\bigr)_
       {\epsilon\in\{0,1\}^d}.
\tag{3.3}
\]

This holds for every cube dimension \(2\le s\le d\) and every
permutation of its variable placeholders.

#### Proof

By Lemma 2.1 the common core \(D\) of every applicable cube contains
\(C\).  The higher-cube move changes only the labels occupying its
variable placeholder positions.  Every ordinary label of \(D\), hence
every label of \(C\), remains at the same rooted cyclic position on
both shores of the move.

Therefore, at each touched top separately, the old and new frames have
the same induced order on \(C\).  Their contributions to (3.2) agree
corner by corner.  Untouched tops do not change.  Directed cycle moves
are the same statement with a two-placeholder common core. \(\square\)

The invariant is much larger than a sign.  Its basis is the set of
literal ordered-core templates, and it records the full permutation
state of \(C\) at every corner.

## 4. A phasewise core antisymmetrizer

Assume \(c=2H\ge7\).  Choose three distinguished core labels

\[
                         p_1,p_2,p_3\in C
\tag{4.1}
\]

in three distinct core positions.  Fix at least four other core labels
at four asymmetric anchor positions.  All remaining core labels and all
placeholder positions are also fixed.

For \(\sigma\in S_3\), let \(\pi_{\epsilon,\sigma}\) be the frame on
\(U_\epsilon\) obtained by placing

\[
                         p_{\sigma(1)},p_{\sigma(2)},p_{\sigma(3)}
\tag{4.2}
\]

in the three distinguished positions.  Everything else is independent
of \(\sigma\).

### Theorem 4.1 (six-frame all-depth antisymmetrizer)

At every top \(U_\epsilon\), for every positional phase \(s\) and every
proper interval length \(\ell\),

\[
 \boxed{
 \sum_{\sigma\in A_3}
 e_{I_{\pi_{\epsilon,\sigma}}(s,\ell)}
 =
 \sum_{\sigma\in S_3\setminus A_3}
 e_{I_{\pi_{\epsilon,\sigma}}(s,\ell)}.}
\tag{4.3}
\]

The same identity holds for root-form targets

\[
                         R_\epsilon\cup
 I_{\pi_{\epsilon,\sigma}}(s,\ell),
\tag{4.4}
\]

and hence after arbitrary common phase deletion and every common nested
tag schedule.

#### Proof

Fix the positional interval.  Let \(J\subseteq\{1,2,3\}\) be the set of
distinguished positions it contains, and let \(K\) be the common set of
all other labels in the target.

If \(|J|=0\) or \(3\), the target set is independent of \(\sigma\), and
both sides of (4.3) contain it three times.

If \(|J|=1\), the cyclic group \(A_3\) acts regularly on the three
labels, so its three images of the selected position are

\[
                         \{p_1\},\{p_2\},\{p_3\}.
\tag{4.5}
\]

The odd coset is also regular and gives the same three singleton sets.
If \(|J|=2\), take complements inside
\(\{p_1,p_2,p_3\}\); both shores give the same three two-sets.
Adjoining the common set \(K\) proves (4.3).

The root \(R_\epsilon\) is fixed while \(\sigma\) varies, so adjoining it
proves (4.4).  Weighted summation proves the schedule assertions.
\(\square\)

The four fixed anchors ensure that the six induced core orders in
(4.2) remain distinct even modulo cyclic rotation and reversal.

## 5. Two disconnected tables with identical loads

Define frame tables \(X^+\) and \(X^-\) by putting, at every
\(\epsilon\in\{0,1\}^d\),

\[
\begin{aligned}
 X^+|_{U_\epsilon}
   &=\sum_{\sigma\in A_3}
        e_{\pi_{\epsilon,\sigma}},\\
 X^-|_{U_\epsilon}
   &=\sum_{\sigma\in S_3\setminus A_3}
        e_{\pi_{\epsilon,\sigma}}.
\end{aligned}
\tag{5.1}
\]

Thus each table has top multiplicity three at every corner.

### Theorem 5.1 (all-dimension template disconnection)

The tables \(X^+,X^-\) have identical:

1. top multiplicities;
2. phasewise interval loads at every length;
3. repaired middle loads;
4. signed entrance loads; and
5. common nested tag loads.

Nevertheless no sequence of fixed-core cycle moves and coherent higher
placeholder cube moves, of any dimensions \(2,\ldots,d\), connects
\(X^+\) to \(X^-\).

#### Proof

The top multiplicities are three on both sides.  Summing Theorem 4.1
over all corners proves equality of every physical load.

At each corner, \(\Theta_{C,\epsilon}(X^+)\) is supported on the three
even core permutations, while
\(\Theta_{C,\epsilon}(X^-)\) is supported on the three odd core
permutations.  The anchor choice makes these six basis elements
distinct.  Hence

\[
                         \Theta_C(X^+)\ne\Theta_C(X^-).
\tag{5.2}
\]

Theorem 3.1 makes \(\Theta_C\) constant on every allowed move component,
proving disconnection. \(\square\)

### Proposition 5.2 (the obstruction is top-parity neutral)

The previous affine mod-two top-sign characters take the same value on
\(X^+\) and \(X^-\).

#### Proof

At each top the product of the three even-permutation columns has even
sign, while the product of the three odd-permutation columns changes
sign once.  Thus the top-sign difference is the indicator of all
\(2^d\) corners of \(\mathcal Q(C)\).

For any affine character

\[
                         w(U)=\alpha_0+\sum_{x\in U}\alpha_x,
\tag{5.3}
\]

its sum over the cell is zero modulo two.  The constant and every
\(x\in C\) occur \(2^d\) times.  Each \(a_{j,b}\) occurs
\(2^{d-1}\) times.  Since \(d=m-H\ge2\), all these numbers are even.
\(\square\)

Thus Theorem 5.1 is not separated by the previously known affine
parity quotient.  The surviving charge is the complete ordered-core
template distribution.

## 6. Exceptional scale

The face \(\mathcal Q(C)\) contains \(2^d=2^{m-H}\) tops.  Each table
uses three frames per top.  At \(M\) middle phases per frame, its total
incidence mass is

\[
                         3M2^{m-H}.
\tag{6.1}
\]

Since

\[
                         W=\binom{2m}m=4^{m-o(m)}
\tag{6.2}
\]

and \(H=o(m)\),

\[
 \boxed{
                         3M2^{m-H}=o(W).}
\tag{6.3}
\]

Therefore this exact invariant is compatible with an
\(o(W)\)-exception global theorem: one may discard the entire maximal
cell within the allowed budget.  Conversely, any theorem claiming
literal connectivity with no exceptions, or using only placeholder
cubes without a core-reordering primitive, is false.

The obstruction can be repeated on disjoint Boolean faces arising from
a fixed ground pairing, but the union of maximal faces still has
promotion mass \(o(W)\).  Establishing an \(\Omega(W)\) toll would
require either:

1. a positive-density family of ordered-core charges stable under cubes
   crossing between different pair cells; or
2. a lower bound against recycling a small number of core-reordering
   catalyst frames.

Neither assertion is proved here.

## 7. Exact boundary

Proved:

1. every higher cube internal to a maximal Boolean top face contains its
   fixed \(2H\)-core;
2. the complete cornerwise ordered-core histogram is invariant under
   all directed cycle and coherent placeholder-cube moves, in every
   available dimension;
3. an exact six-frame core antisymmetrizer with identical loads phase by
   phase and length by length;
4. two parity-neutral integer frame tables in the same all-depth fibre
   but different ordered-core components;
5. persistence after one-hole deletion, root complementation, nested
   tags, and the dihedral quotient; and
6. the exact \(o(W)\) scale of this maximal-cell obstruction.

Not proved:

1. an \(o(W)\)-exception connectivity theorem for the full global
   one-frame-at-every-top fibre;
2. a positive-density ordered-core invariant under cubes which cross
   between different Boolean cells;
3. a bounded-cost core-reordering catalyst; or
4. coefficient one.

The first missing move is now explicit: it must change the induced order
on labels which belong to the common core of every corner.  No increase
in placeholder-cube dimension can perform that task inside the maximal
cell.
