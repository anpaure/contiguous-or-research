# Antipodal suspension of a wreath trade

## 1. Outcome

There is an exact all-dimensional **linear** suspension for the shadow
maps. Let \(n=2m+1\), add two new coordinates \(x,y\), and insert them in
two gaps of an old cyclic order whose gap distance is \(m\). Summing over
the \(n\) translates of this insertion defines an operator \(P_m\). If

\[
 B_m w=B_{m-1}w=0,
\]

then

\[
 B_{m+1}P_mw=B_mP_mw=0,                            \tag{1.1}
\]

while on either sector containing exactly one of \(x,y\),

\[
 (B_{m-1}P_mw)_{U\cup\{x\}}
 =(B_{m-1}P_mw)_{U\cup\{y\}}
 =(m-1)(B_{m-2}w)_U.                               \tag{1.2}
\]

Thus the desired shadow-space suspension exists, with an explicit
injective next-shadow map.

This does **not** by itself prove the state-level suspension lemma. The
full translate sum is never a wreath packing: already for one old cyclic
order, each relevant new middle set occurs \(m+1\) times. The exact
integral problem is a pointing and completion problem. Section 6 gives its
exact five-state/three-state local criterion. Section 7 isolates a stronger
translation-stable voltage ansatz, not a necessary condition.

Throughout, cyclic intervals are ordinary consecutive intervals. This is
equivalent to the every-other-position convention in the project because
multiplication by \(2\) permutes the positions of an odd cycle.

## 2. The gap operator

Let \(C=(c_0,\ldots,c_{n-1})\) be an oriented cyclic order. Number its gaps
by \(\mathbb Z_n\), with gap \(i\) immediately after \(c_i\). For
\(d\in\{1,\ldots,n-1\}\), let \(E_{i,d}C\) be the cyclic order obtained by
putting \(x\) in gap \(i\) and \(y\) in gap \(i+d\). Define

\[
 P_d e_C=\sum_{i\in\mathbb Z_n}e_{E_{i,d}C}.        \tag{2.1}
\]

For \(1\le \ell<n\), put

\[
 h_d(\ell)=(\ell-d)_+ +(\ell-(n-d))_+.             \tag{2.2}
\]

This is the number of directed arcs \(i\mapsto i+d\) having both ends in
an interval of \(\ell\) consecutive gaps.

### Lemma 2.1 (exact sector formula)

Let \(T\subseteq V(C)\cup\{x,y\}\) have size \(r\), let
\(t=|T\cap\{x,y\}|\), and put \(U=T\cap V(C)\). For \(r\ge3\),

\[
 (B_rP_de_C)_T=
 \begin{cases}
 h_d(n-r+1)\,\mathbf 1\{U\text{ is an }r\text{-interval of }C\},&t=0,\\
 \bigl(r-h_d(r-1)\bigr)
 \mathbf 1\{U\text{ is an }(r-1)\text{-interval of }C\},&t=1,\\
 h_d(r-1)\,\mathbf 1\{U\text{ is an }(r-2)\text{-interval of }C\},&t=2.
 \end{cases}                                        \tag{2.3}
\]

#### Proof

The gaps in which one may insert points while keeping a fixed old interval
consecutive form an interval in the gap circle.

* If neither new point is selected, both insertion gaps must avoid the
  \(r-1\) internal gaps of \(U\). The allowed gap interval has length
  \(n-r+1\), giving the first line of (2.3).
* If both are selected, their two gaps must lie in the \(r-1\) consecutive
  gaps consisting of the internal and boundary gaps of the
  \((r-2)\)-interval \(U\). This gives the third line.
* If only \(x\) is selected, there are \(r\) placements of \(x\) around the
  \((r-1)\)-interval \(U\). Exactly \(h_d(r-1)\) of them force \(y\) into
  the same \(r\)-window. The remaining \(r-h_d(r-1)\) placements give the
  second line. The argument for \(y\) is identical.

All counts depend only on the indicated old interval, so the formulas hold
target by target. \(\square\)

## 3. Exact linear suspension

Take \(d=m\). Since \(n=2m+1\),

\[
 h_m(m)=h_m(m-1)=h_m(m-2)=0.                       \tag{3.1}
\]

### Theorem 3.1 (antipodal shadow suspension)

Let \(w\) be any signed collection of cyclic orders on \(2m+1\) points
such that

\[
 B_mw=B_{m-1}w=0.                                  \tag{3.2}
\]

Then, on \(2m+3\) points,

\[
 B_{m+1}P_mw=B_mP_mw=0,                            \tag{3.3}
\]

and

\[
 B_{m-1}P_mw=(m-1)
 \bigl(\iota_x B_{m-2}w+\iota_y B_{m-2}w\bigr),    \tag{3.4}
\]

where \((\iota_xf)_{U\cup\{x\}}=f_U\), and similarly for \(y\); all
other sectors in (3.4) vanish. In particular, the map in (3.4) is
injective.

#### Proof

At new rank \(m+1\), the three sectors in Lemma 2.1 use respectively old
ranks \(m+1,m,m-1\). On an odd cycle, complementation identifies the
rank-\((m+1)\) interval incidence with rank-\(m\) interval incidence.
Hence all three sectors vanish by (3.2).

At new rank \(m\), the sectors use old ranks \(m,m-1,m-2\). The first two
vanish by (3.2), while the coefficient of the third is \(h_m(m-1)=0\).
This proves (3.3).

At new rank \(m-1\), the no-new sector is a scalar multiple of
\(B_{m-1}w\), the both-new coefficient is \(h_m(m-2)=0\), and either
one-new coefficient is

\[
 (m-1)-h_m(m-2)=m-1.
\]

This proves (3.4). \(\square\)

The operator commutes with every permutation of the old coordinates.
Consequently, if \(w=\tau X-X\) for a coordinate transposition \(\tau\),
then

\[
 P_mw=\tau(P_mX)-P_mX.                              \tag{3.5}
\]

So even the transposition provenance survives at the signed level.

## 4. Why the translate sum is not a factor move

The obstruction is exact, not merely a poor support count. At new middle
rank \(m+1\), for every old middle interval \(S\) of one cyclic order \(C\),
Lemma 2.1 gives

\[
 (B_{m+1}P_me_C)_{S\cup\{x\}}
 =(B_{m+1}P_me_C)_{S\cup\{y\}}=m+1.                \tag{4.1}
\]

Thus the \(n\) extended wreaths in \(P_me_C\) repeat each of these middle
sets \(m+1\) times. They cannot be contained together in an exact wreath
factor.

This proves a useful no-go statement:

> A cyclically equivariant orderwise suspension can satisfy the desired
> shadow identities, but it cannot be a \(0/1\) factor suspension. A legal
> lift must break the cyclic symmetry by choosing a point on every changed
> wreath, and those choices must be compatible across both the middle and
> first-lower occurrence graphs.

For \(d=m\), any two distinct pointed extensions \(E_{a,m}C\) and
\(E_{b,m}C\) share a new middle set. Indeed, fix an old middle interval
\(S_s=\{c_s,\ldots,c_{s+m-1}\}\). Relative to its start, the pointings
\(s,\ldots,s+m-1\) expose \(S_s\cup\{x\}\), the next \(m\) pointings
expose \(S_s\cup\{y\}\), and the remaining boundary pointing exposes both.
For any two points on a circle of size \(2m+1\), rotate this partition so
that both points lie in one of the same two classes (using the boundary
point in the antipodal case). Hence a wreath packing may use at most one
antipodal extension of a fixed old cyclic order.

## 5. A rigid translation-stable sufficient condition

Let \(\mathcal N,\mathcal P\) be two finite families of oriented cyclic
orders on \(V\), with

\[
 B_m\mathbf1_{\mathcal N}=B_m\mathbf1_{\mathcal P},
 \qquad
 B_{m-1}\mathbf1_{\mathcal N}=B_{m-1}\mathbf1_{\mathcal P}.          \tag{5.1}
\]

Assume each side is a middle-wreath packing. Equality at rank \(m\) gives
a unique pairing of the two occurrences of every middle target. For every
rank-\((m-1)\) target, choose an arbitrary bijection between its occurrence
multisets on the two sides.

If an interval \(S\) starts at position \(s_C(S)\in\mathbb Z_n\) in an
oriented order \(C\), call a family of gap points

\[
 a_C\in\mathbb Z_n
\]

**bi-flat** when every paired occurrence \(S\subset C,D\), at either rank
\(m\) or \(m-1\), satisfies

\[
 a_C-s_C(S)=a_D-s_D(S)\pmod n.                      \tag{5.2}
\]

Bi-flatness equates the **exact** relative offsets. It is deliberately
stronger than equality of the local incidence patterns seen by the two
lifted shadow rows. Its advantage is translation stability: adding the
same \(t\) to every \(a_C\) preserves (5.2), which is what makes the
averaging argument below possible.

### Theorem 5.1 (pointed legal suspension)

If a bi-flat pointing exists, then for every \(t\in\mathbb Z_n\),

\[
 \mathcal N_t^+=\{E_{a_C+t,m}C:C\in\mathcal N\},
 \qquad
 \mathcal P_t^+=\{E_{a_D+t,m}D:D\in\mathcal P\}     \tag{5.3}
\]

are middle-wreath packings with the same middle union and the same
rank-\(m\) shadow. Hence their difference is a support-feasible partial
trade preserving the top two rows.

If, in addition,

\[
 B_{m-2}(\mathbf1_{\mathcal P}-\mathbf1_{\mathcal N})\ne0,          \tag{5.4}
\]

then at least one translate \(t\) has a nonzero rank-\((m-1)\) effect.

#### Proof

No \((m+1)\)-window or \(m\)-window in \(E_{a,m}C\) contains both new
coordinates. A new middle target containing exactly one new coordinate
is determined by an old middle interval; a target containing neither is
determined by the complementary old middle interval. Condition (5.2) on
the rank-\(m\) occurrence pairing makes the corresponding local incidence
decisions identical on the two sides.

At new rank \(m\), the no-new targets are controlled by the same rank-\(m\)
pairing, and the one-new targets by the chosen rank-\((m-1)\) pairing.
Again (5.2) makes every local decision identical. This proves both shadow
equalities.

The two new-coordinate sectors are disjoint. Within either one, two equal
new middle targets would give two equal old middle targets, impossible
because the old side was a packing. The no-new sector is handled by
complementation. Thus both lifted sides remain packings.

Finally,

\[
 \sum_{t\in\mathbb Z_n}
 (\mathbf1_{\mathcal P_t^+}-\mathbf1_{\mathcal N_t^+})
 =P_m(\mathbf1_{\mathcal P}-\mathbf1_{\mathcal N}).                 \tag{5.5}
\]

The rank-\((m-1)\) image of the right side is nonzero by (3.4) and (5.4),
so at least one summand has nonzero image. \(\square\)

If the negative packing in (5.3) is contained in an exact factor, replacing
it by the positive packing gives another exact factor. This last
completion statement is immediate, but existence of the containing factor
is a separate condition; it is not implied by bi-flatness.

## 6. The exact coarse pointing criterion

The two lifted rows do not remember the full residue
\(a_C-s_C(S)\). They remember only the following finite signatures.
For \(z\in\mathbb Z_{2m+1}\), define

\[
\kappa(z)=
\begin{cases}
X_0,&0\le z\le m-2,\\
X_1,&z=m-1,\\
Y_1,&z=m,\\
Y_0,&m+1\le z\le2m-1,\\
B,&z=2m,
\end{cases}                                         \tag{6.1}
\]

and

\[
\lambda(z)=
\begin{cases}
X,&z\in\{0,\ldots,m-2,2m\},\\
0,&z=m-1,\\
Y,&m\le z\le2m-1.
\end{cases}                                         \tag{6.2}
\]

Here \(\kappa\) records, for an old middle interval \(S\), the complete
incidence vector of the four relevant lifted targets

\[
S\cup\{x\},\quad S\cup\{y\},\quad V\setminus S,\quad S
\]

at new ranks \(m+1,m+1,m+1,m\), respectively. The five values correspond
to

\[
\begin{array}{c|cc|c|c}
\kappa&S\cup\{x\}&S\cup\{y\}&V\setminus S&S\\ \hline
X_0&1&0&0&0\\
X_1&1&0&0&1\\
Y_1&0&1&0&1\\
Y_0&0&1&0&0\\
B  &1&1&1&1
\end{array}                                         \tag{6.3}
\]

The value \(\lambda\) records whether an old rank-\((m-1)\) interval
\(U\) produces \(U\cup\{x\}\), neither one-new target, or
\(U\cup\{y\}\) at new rank \(m\).

### Theorem 6.1 (necessary and sufficient pointed-shadow test)

Choose arbitrary pointings \(a_C\) on all cycles of
\(\mathcal N,\mathcal P\). Their antipodal extensions have equal
rank-\((m+1)\) and rank-\(m\) incidence if and only if both conditions hold:

1. For every old middle target \(S\), with unique occurrences in
   \(C\in\mathcal N\) and \(D\in\mathcal P\),

   \[
   \kappa(a_C-s_C(S))=\kappa(a_D-s_D(S)).           \tag{6.4}
   \]

2. For every old rank-\((m-1)\) target \(U\), the two occurrence multisets

   \[
   \{\!\{\lambda(a_C-s_C(U)):U\subset C,\ C\in\mathcal N\}\!\},
   \quad
   \{\!\{\lambda(a_D-s_D(U)):U\subset D,\ D\in\mathcal P\}\!\}       \tag{6.5}
   \]

   are equal.

For every choice of pointings, each lifted side is automatically a
middle-wreath packing.

#### Proof

Trace the two inserted gaps around one old interval. For an old middle
interval \(S\), the relative pointings \(0,\ldots,m-2\) expose only
\(S\cup\{x\}\); \(m-1\) also preserves \(S\) at the next row; \(m\)
exposes \(S\cup\{y\}\) and preserves \(S\); \(m+1,\ldots,2m-1\) expose
only \(S\cup\{y\}\); and the boundary value \(2m\) exposes both one-new
targets, the complement, and \(S\). This is exactly (6.3).

For an old rank-\((m-1)\) interval \(U\), direct boundary tracing gives
\(U\cup\{x\}\) for residues \(0,\ldots,m-2,2m\), no one-new target for
\(m-1\), and \(U\cup\{y\}\) for \(m,\ldots,2m-1\). This is (6.2).

Every lifted target in the two rows is of exactly one of these forms, so
(6.4)--(6.5) are necessary and sufficient target by target. The packing
claim is the same argument as in Theorem 5.1: there is no both-new middle
sector, and equal one-new or no-new targets would force equal old middle
targets. \(\square\)

Bi-flatness implies (6.4)--(6.5), but it is not necessary. For example,
distinct residues \(0\) and \(1\) have the same \(\kappa\)- and
\(\lambda\)-values whenever \(m\ge3\). Also, a coarse solution need not
remain a solution after a common translation, so equation (5.5) cannot be
used for it without an additional argument.

## 7. Voltage and holonomy for the rigid ansatz

The pointing condition is an ordinary graph-cohomology problem. Form a
bipartite multigraph \(\Gamma\) on
\(\mathcal N\mathbin{\dot\cup}\mathcal P\): include the unique
middle-occurrence edge for every rank-\(m\) target and the chosen
paired-occurrence edge for every rank-\((m-1)\) target. Orient edges from
\(\mathcal N\) to \(\mathcal P\) and label

\[
 \gamma(CD)=s_D(S)-s_C(S)\in\mathbb Z_n.            \tag{7.1}
\]

Then (5.2) is exactly

\[
 a_D-a_C=\gamma(CD).                                \tag{7.2}
\]

### Lemma 7.1 (holonomy criterion for bi-flatness)

A bi-flat pointing exists if and only if the signed sum of \(\gamma\) around
every cycle of \(\Gamma\) is zero in \(\mathbb Z_n\).

This follows by integrating \(\gamma\) along a spanning forest; the
non-tree edges are consistent precisely when all cycle sums vanish.

### The certified \(m=4\) edge is not equivariantly bi-flat

The obstruction is already visible in one pair of wreaths from the
four-for-four certificate. In ordinary cyclic-interval order, take

\[
 C=(1,6,4,3,2,8,7,5,9),\qquad
 \tau C=(2,6,4,3,1,8,7,5,9),\quad \tau=(1\ 2).
\]

The middle target

\[
 S=\{1,3,4,6\}
\]

starts at positions \(0\) and \(1\), respectively, so its occurrence edge
has voltage \(+1\). The middle target

\[
 T=\{2,3,4,6\}
\]

starts at positions \(1\) and \(0\), so the parallel occurrence edge has
voltage \(-1\). A transposition-equivariant pointing would therefore have
to satisfy simultaneously

\[
 a_{\tau C}-a_C=1,\qquad a_{\tau C}-a_C=-1\pmod 9,
\]

which is impossible. The resulting two-edge cycle has holonomy \(2\) in
\(\mathbb Z_9\).

Thus Theorem 5.1 does not directly lift the known \(m=4\) edge while
retaining its final transposition provenance **within the rigid bi-flat
ansatz**. This is not an obstruction to the coarse criterion of Theorem
6.1. Indeed, for these two parallel edges alone, \(a_C=a_{\tau C}=1\)
places all four relative offsets in the class \(X_0\), so both coarse
conditions are locally compatible despite the nonzero exact voltage.

There is a further rigidity point. Suppose the old trade is completed by a
common family \(\mathcal H\), so
\(\mathcal F=\mathcal N\dot\cup\mathcal H\) and
\(\mathcal G=\mathcal P\dot\cup\mathcal H\) are exact factors. The middle
targets covered by \(\mathcal H\) are disjoint from the common middle union
of \(\mathcal N,\mathcal P\). Hence the rank-\(m\) occurrence graph of the
two full factors is the disjoint union of the old trade graph and the
identity graph on \(\mathcal H\). Its nonzero voltage cycle survives
unchanged.

Consequently, merely applying pointed order-preserving extensions to the
common old completion cannot make the **exact-offset** cochain bi-flat.
This says nothing by itself about the coarse signature constraints, which
may be satisfied without cancelling the voltage.

The all-translate operator \(P_m\) is the derived
\(\mathbb Z_n\)-cover of this voltage graph. A closed walk of nonzero
voltage \(\lambda\) joins \((C,a)\) to \((C,a+\lambda)\) in one lifted
component. Section 4 shows that these two extensions of \(C\) overlap in
their new middle wreaths. Therefore a nontrivial holonomy class is an
exact obstruction to obtaining a wreath-packing component from the natural
**exact-offset derived-cover** suspension. It is not an obstruction to an
arbitrary pointed thinning.

This explains both sides of the situation:

* averaging all pointings proves the clean linear identity (3.3)--(3.4);
* nonzero voltage cycles force repeated base wreaths in the corresponding
  integral component.

## 8. The reduced all-dimensional gate

There are now two honest routes.

1. **Rigid translation-stable route.** Cancel the voltage holonomy, obtain
   a bi-flat pointing, and embed one translated negative packing from
   Theorem 5.1 into a reachable exact factor. Translation averaging then
   guarantees that some legal translate carries the deeper effect.
2. **General coarse route.** Solve the exact five-state/three-state
   constraints (6.4)--(6.5), complete the resulting partial packing, and
   separately prove that the selected coarse solution has nonzero deeper
   effect. No voltage cancellation is required, but the averaging argument
   is unavailable.

The completion to an exact reachable factor is common to both routes.
Any proposed Dyck recursion should therefore be audited against the exact
coarse criterion first; voltage is a useful structured sufficient ansatz,
not the full obstruction theory.

### Finite status of the certified \(m=4\) edge

The coarse criterion has been exhaustively checked for the known
four-for-four trade. With the fixed antipodal direction \(d=4\), all
\(9^4=6561\) point choices on either side are middle packings, and they
give \(6561\) distinct combined \(B_5,B_4\) signatures on each side; the
two signature sets are disjoint. Allowing either antipodal direction
\(d=4\) or \(d=5\) independently on every changed wreath gives
\(18^4=104976\) distinct signatures on each side, again with zero
intersection.

Therefore the certified edge has no direct one-extension-per-changed-wreath
antipodal suspension from \(m=4\) to \(m=5\), even under the exact coarse
criterion. This is a finite certified no-go, not an all-\(m\) theorem and
not a consequence of voltage holonomy. The exhaustive checker is
[search_haar_pointed_thinning.cpp](./search_haar_pointed_thinning.cpp).

The standalone check
[verify_haar_antipodal_suspension.cpp](./verify_haar_antipodal_suspension.cpp)
applies the operator to the certified \(m=4\) Haar trade. It verifies
\(B_5P_4w=B_4P_4w=0\), the two scaled copies of \(B_2w\) at rank \(3\),
and the middle-target multiplicity \(5\) that prevents the translate sum
from being a packing.

The complete Hall/group-ring classification of the rigid bi-flat
extension problem, its owner-transfer gain graph for a transposition, and
the three-target coarse obstruction for the certified seed are in
[HAAR_HOLONOMY_CLASSIFICATION.md](./HAAR_HOLONOMY_CLASSIFICATION.md).
