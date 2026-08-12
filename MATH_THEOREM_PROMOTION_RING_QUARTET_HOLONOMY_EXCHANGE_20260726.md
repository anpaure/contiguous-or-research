# Promotion rings: an exact all-depth quartet holonomy exchange and its complete parity character space

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
n=2m,\qquad M=m+H,\qquad H=o(m),
\]

and consider actual labelled cyclic frames on the \(M\)-set tops.
Choose an \((M-2)\)-set \(C\), four distinct labels

\[
a_0,a_1,b_0,b_1\notin C,
\]

and the four tops

\[
U_{ij}=C\cup\{a_i,b_j\}\qquad(i,j\in\{0,1\}).
\]

Fix a cyclic positional word on \(C\cup\{A,B\}\). On \(U_{ij}\), let
\(\pi_{ij}^{+}\) replace \(A,B\) by \(a_i,b_j\), and let
\(\pi_{ij}^{-}\) replace them by \(b_j,a_i\). For every interval
length \(1\le \ell<M\), every phase \(s\), and the corresponding global
interval basis vectors \(v_{ij}^{\pm}(s,\ell)\),

\[
\boxed{\;
\sum_{i,j\in\{0,1\}}(-1)^{i+j}
\bigl(v_{ij}^{+}(s,\ell)-v_{ij}^{-}(s,\ell)\bigr)=0.
\;}
\tag{0.1}
\]

Consequently the checkerboard replacement

\[
(+,-,-,+)\longleftrightarrow(-,+,+,-)
\tag{0.2}
\]

is an exact owner-preserving compound exchange of four actual frames.
It preserves exactly:

1. the full middle load;
2. the one-hole middle load when the same positional phase is deleted;
3. every entrance load simultaneously; and
4. every common phase-tagged census, even with arbitrary real phase
   weights.

This is not a low-harmonic relation. If the placeholders have cyclic
distance greater than \(2H\), then at every depth \(0\le q\le H\),
each of the four frames has exact squared action

\[
\|c_{ij,+}^{m-q}-c_{ij,-}^{m-q}\|_2^2=4(H+q),
\tag{0.3}
\]

while their signed aggregate action is zero. At the middle row the
placeholder transposition may be chosen so that, at all four tops,

\[
\boxed{\;
\|P_H^{U_{ij}}(c_{ij,+}-c_{ij,-})\|_2^2
=4H-O(H^2/m)=(4-o(1))H.
\;}
\tag{0.4}
\]

Thus one quartet cancels \(16H-o(H)\) local top-degree exchange action
by exact cross-top Gram terms. The per-column diagonal norm remains
invariant, as it must, but it supplies no positive obstruction to this
legal compound move.

For the **unrestricted** rectangle library there is a small integral
holonomy. Root the cyclic frames so their
permutation signs are defined. A quartet flips the signs at its four
tops. The complete mod-two character space invariant under all such
rectangles consists exactly of

\[
w(U)=\alpha_0+\sum_{x\in U}\alpha_x\pmod 2.
\tag{0.5}
\]

It has dimension \(n=2m\). These \(O(m)\) syndromes can be changed by
at most \(2m\) exceptional one-top transpositions, affecting
\(O(mH)=o(W)\) interval incidences through all \(q\le H\). Thus this
parity sector cannot produce an \(\Omega(W)\) separating inequality in
the unrestricted physical atlas. This does not classify the character
space of the smaller fixed-mechanical-shore sublibrary, which may have
additional parity invariants.

The result is a positive exact compound-exchange theorem, not a
rounding theorem: the exchange is load-neutral, not energy-decreasing.
The remaining gate is nonabelian/integral connectivity of the
common-permutation clone coupling.

## 1. Positional interval columns

Let

\[
\omega=(\omega_0,\ldots,\omega_{M-1})
\tag{1.1}
\]

be a cyclic word whose symbols are the elements of \(C\), together with
the placeholders \(A,B\). For \(i,j\in\{0,1\}\), define

\[
\begin{aligned}
\pi_{ij}^{+}&:\quad A\mapsto a_i,\quad B\mapsto b_j,\\
\pi_{ij}^{-}&:\quad A\mapsto b_j,\quad B\mapsto a_i,
\end{aligned}
\tag{1.2}
\]

leaving every label in \(C\) fixed. Both are genuine cyclic orders of
\(U_{ij}\). For \(s\in\mathbb Z_M\) and \(1\le\ell<M\), put

\[
I_{ij}^{\varepsilon}(s,\ell)
=\{\pi_{ij}^{\varepsilon}(s),\ldots,
\pi_{ij}^{\varepsilon}(s+\ell-1)\},
\tag{1.3}
\]

and let \(v_{ij}^{\varepsilon}(s,\ell)\) be its standard basis vector
in \(\mathbb R^{\binom{[n]}\ell}\). The positional phase interval is
common to all eight words.

## 2. The exact phasewise quartet identity

### Theorem 2.1 (phasewise all-length rectangle)

Identity (0.1) holds for every \(s\) and \(\ell\). More generally, for
arbitrary real weights \(w_{s,\ell}\),

\[
\sum_{i,j}(-1)^{i+j}\sum_{s,\ell}w_{s,\ell}
\bigl(v_{ij}^{+}(s,\ell)-v_{ij}^{-}(s,\ell)\bigr)=0.
\tag{2.1}
\]

#### Proof

Fix \(s,\ell\), and let \(K\subseteq C\) be the common labels in the
positional interval. If the interval contains neither placeholder, the
two sets are both \(K\). If it contains both, they are both
\(K\cup\{a_i,b_j\}\). These terms vanish individually.

If it contains \(A\) but not \(B\), its contribution to (0.1) is

\[
\sum_{i,j}(-1)^{i+j}
\left(e_{K\cup\{a_i\}}-e_{K\cup\{b_j\}}\right).
\tag{2.2}
\]

In the first part, fix \(i\) and sum over \(j\); in the second, fix
\(j\) and sum over \(i\). Both sums are zero. The case containing only
\(B\) is the negative of the same calculation. This proves (0.1).
Weighted summation proves (2.1). \(\square\)

### Corollary 2.2 (legal all-depth compound exchange)

Initially take the \(+\) frame at \(U_{00},U_{11}\), and the \(-\)
frame at \(U_{01},U_{10}\); reverse all four choices. The operation
preserves one frame at every touched top and preserves every aggregate
interval load.

It remains exact after retaining any common set of positional phases.
In particular, it remains exact after deleting one common phase and
after attaching any common phase-to-depth tag schedule.

#### Proof

The aggregate change is the negative of (0.1), or of (2.1) for a
weighted retained schedule. Every old and new object is a literal
cyclic order of the same touched top. \(\square\)

For the promotion middle row one may use the \(m\)-interval deck inside
the top. Under the root-form convention, a middle target is

\[
([n]\setminus U)\cup I_H.
\tag{2.3}
\]

Its global complement is \(U\setminus I_H\), the complementary
\(m\)-interval, with one common phase shift. Global complementation is
a coordinate permutation, so Corollary 2.2 gives literal root-form
cancellation as well. Direct entrance targets are already intervals,
so their cancellation is literal without this conversion.

### Mechanical-support variant

Fix a balanced half \(P\). If the placeholders occupy positions carrying
the same bit of the mechanical word and

\[
a_0,a_1,b_0,b_1
\]

all belong to the corresponding \(P\)-shore, then all eight orders in
(1.2) respect the same mechanical pattern. The four tops also have the
same root type. Hence the exchange lies inside the restricted mechanical
support atlas under these conditions.

## 3. Exact action of the placeholder transposition

### Lemma 3.1 (two-position action)

Let \(c_\pi^h\) be the incidence vector of the \(h\)-windows of a
cyclic order on \(M\) labels, where \(2\le h<M/2\). Swap labels at two
positions of smaller cyclic distance \(\delta\le M/2\), obtaining
\(\tau\pi\). Then

\[
\|c_{\tau\pi}^h-c_\pi^h\|_2^2=
\begin{cases}
4\delta,&1\le\delta<h,\\
4h-4,&\delta=h,\\
4h,&h<\delta\le M/2.
\end{cases}
\tag{3.1}
\]

#### Proof

An old window is unchanged as a label set precisely when it contains
both swapped labels or neither. If \(\delta<h\), exactly \(2\delta\)
old windows contain exactly one; if \(\delta\ge h\), exactly \(2h\)
do.

Replacing one swapped label by the other turns a changed old window
into another old window only when the swapped positions are the opposite
endpoints of two consecutive \(h\)-windows, namely \(\delta=h\). Then
exactly two changed windows are interchanged. Otherwise no changed old
window remains in the new deck. The squared distance of two zero-one
vectors is their symmetric-difference size, twice the number of old
windows that leave. This gives (3.1). \(\square\)

The restriction \(h\ge2\) is necessary: for \(h=1\), every window deck
is simply the set of all singleton labels and is invariant under every
positional transposition. All applications below have \(h=H+q\ge2\).

The complement of an \(\ell\)-interval in a cyclic \(M\)-set is an
\((M-\ell)\)-interval. Hence, if \(\delta>2H\), Lemma 3.1 with
\(h=H+q\) gives (0.3) for all \(q\le H\).

Put \(d_{ij}=c_{ij,+}^{m-q}-c_{ij,-}^{m-q}\). Theorem 2.1 and (0.3)
give

\[
2\sum_{\{ij,i'j'\}}(-1)^{i+j+i'+j'}
\langle d_{ij},d_{i'j'}\rangle
=-\sum_{i,j}\|d_{ij}\|_2^2=-16(H+q).
\tag{3.2}
\]

Thus the cross-top Gram cancels the full diagonal. Deleting one common
phase preserves the aggregate identity exactly. It removes from each
\(d_{ij}\) a vector of norm at most \(\sqrt2\), changing its squared
action by \(O(\sqrt H)\); the repaired middle action is therefore
\(4H+o(H)\) per top.

## 4. Almost pure local top-degree action

For one top \(U\), let

\[
\mathbb R^{\binom UH}=E_0(U)\perp\cdots\perp E_H(U),
\]

and put \(a_j=\|P_jc_\pi^H\|_2^2\). The exact high-harmonic covariance
audit gives

\[
\sum_{j=2}^{H-1}a_j
\le \frac{M(H+2)}{m-H+2}.
\tag{4.1}
\]

We use (4.1) only to choose a transposition.

### Theorem 4.1 (high-degree quartet)

Among the \((1-o(1))\binom M2\) placeholder pairs of distance greater
than \(2H\), one can choose a pair satisfying

\[
\|P_{<H}(c_{\tau\pi}^H-c_\pi^H)\|_2^2
=O(H^2/m)=o(H).
\tag{4.2}
\]

Consequently (0.4) holds at all four tops.

#### Proof

The transposition Laplacian acts on \(E_j(U)\) by \(j(M-j+1)\).
Therefore

\[
\begin{aligned}
\sum_\tau\|P_{<H}(\tau c_\pi^H-c_\pi^H)\|_2^2
&=2\sum_{j=2}^{H-1}j(M-j+1)a_j\\
&\le 2HM\sum_{j=2}^{H-1}a_j\\
&\le \frac{2HM^2(H+2)}{m-H+2}
=O(MH^2).
\end{aligned}
\tag{4.3}
\]

Only \(O(MH)=o(M^2)\) position pairs have cyclic distance at most
\(2H\). The remaining family has \(\Theta(M^2)\) members. Averaging
(4.3) over it yields (4.2). Lemma 3.1 gives total squared action \(4H\),
so orthogonality yields

\[
\|P_H(\tau c_\pi^H-c_\pi^H)\|_2^2
=4H-O(H^2/m).
\tag{4.4}
\]

All four frame differences are related by label bijections, and Johnson
projectors commute with relabeling. Thus the same value holds at every
top. \(\square\)

At the middle row let
\(d_{ij}=c_{ij,+}^{H}-c_{ij,-}^{H}\), embedded via the root-form
complementation in the common global middle-target space. Put
\(\sigma_{ij}=(-1)^{i+j}\), and write

\[
 d_{ij}=h_{ij}+\ell_{ij},\qquad
 h_{ij}=P_H^{U_{ij}}d_{ij},\qquad
 \ell_{ij}=P_{<H}^{U_{ij}}d_{ij}.
\tag{4.5}
\]

The phasewise quartet identity gives
\(\sum_{ij}\sigma_{ij}d_{ij}=0\).  Hence, by (4.2),

\[
 \left\|\sum_{ij}\sigma_{ij}h_{ij}\right\|_2^2
 =\left\|\sum_{ij}\sigma_{ij}\ell_{ij}\right\|_2^2
 \le4\sum_{ij}\|\ell_{ij}\|_2^2
 =O(H^2/m).
\tag{4.6}
\]

Expanding the left side and using (4.4) at the four tops yields the
exact quantitative cross-top cancellation

\[
 2\sum_{ij<i'j'}\sigma_{ij}\sigma_{i'j'}
       \langle h_{ij},h_{i'j'}\rangle
 =-16H+O(H^2/m).
\tag{4.7}
\]

Thus the cross terms cancel all but \(O(H^2/m)=o(H)\) of the summed
local top-degree diagonal action.  Notice that the local projectors are
different; (4.6), rather than any commutation between them, is what
supplies the cancellation.

For the mechanical-support variant, the same proof applies whenever one
mechanical colour occupies \(\Omega(M)\) positions and has four available
outside labels. Same-colour far pairs then number \(\Omega(M^2)\), while
their total lower-harmonic action is bounded by (4.3).

Theorem 4.1 answers the local \(j=H-O(1)\) question sharply enough for
the present gate: the large local \(E_H\) exchange action is physically
traversed and cancelled exactly by three companion tops. The invariant
per-column norm is therefore not, by itself, an owner-sensitive positive
separator.

## 5. Complete mod-two character audit for the unrestricted library

Mark a phase in every oriented cyclic frame, so rotation is removed and
the sign of its linear order is defined relative to a reference order
of its top. Write this sign additively as

\[
\epsilon_U\in\mathbb F_2.
\]

Every quartet move transposes the placeholders at all four tops, hence
adds the rectangle vector

\[
r(C;a_0,a_1,b_0,b_1)
=\sum_{i,j\in\{0,1\}}e_{C\cup\{a_i,b_j\}}
\tag{5.1}
\]

to the top-sign vector.

Throughout this section every choice of the four outside labels is
allowed. Thus Theorem 5.1 concerns the full physical rectangle lattice,
not the sublattice obtained by requiring all labels and both placeholder
positions to lie in one fixed mechanical colour.

### Theorem 5.1 (all linear parity invariants are affine)

Let \(2\le M\le n-2\). A function

\[
w:\binom{[n]}M\longrightarrow\mathbb F_2
\]

annihilates every rectangle (5.1) if and only if

\[
w(U)=\alpha_0+\sum_{x\in U}\alpha_x
\tag{5.2}
\]

for some \(\alpha_0,\alpha_x\in\mathbb F_2\). This function space has
dimension exactly \(n\).

#### Proof

Functions (5.2) annihilate every rectangle because each coordinate
belongs to zero, two, or four of its tops.

Conversely, for distinct \(x,y\), and an \((M-1)\)-set \(S\) disjoint
from them, put

\[
\Delta_{xy}(S)=w(S\cup\{x\})+w(S\cup\{y\}).
\tag{5.3}
\]

If \(S=C\cup\{c\}\) and \(S'=C\cup\{d\}\) are adjacent
\((M-1)\)-sets avoiding \(x,y\), the rectangle equation on
\(C;x,y,c,d\) gives \(\Delta_{xy}(S)=\Delta_{xy}(S')\). The Johnson
graph on the \((M-1)\)-subsets of \([n]\setminus\{x,y\}\) is connected,
so (5.3) is independent of \(S\); call it \(d_{xy}\).

Using a common \((M-1)\)-set disjoint from \(x,y,z\) gives

\[
d_{xy}+d_{yz}=d_{xz}.
\]

Fix \(x_0\), set \(\alpha_x=d_{x x_0}\), and choose \(\alpha_0\) so
that (5.2) agrees with \(w\) at one \(M\)-set. The two functions have
equal differences across every edge of the connected graph \(J(n,M)\),
so they agree everywhere.

Finally, the \(n+1\) displayed generators have exactly one relation,

\[
\sum_{x\in[n]}\mathbf1_{\{x\in U\}}=M\pmod2.
\]

Thus their function space has dimension \(n\). \(\square\)

### Corollary 5.2 (parity holonomy is \(o(W)\)-cheap)

Given two top-sign vectors, at most \(n\) exceptional one-top sign flips
make all their affine syndromes agree. Their remaining sign difference
then lies in the linear span of the quartet rectangles.

An adjacent transposition in one cyclic frame changes at most four
unphased interval-incidence coordinates at any fixed length. Hence the
exceptional correction changes at most

\[
4n(H+1)=O(mH)=o(W)
\tag{5.4}
\]

incidences through all \(0\le q\le H\).

#### Proof

The syndrome map has rank \(n\). Choose a basis of at most \(n\) of its
top columns. Every syndrome difference is the sum of a subset of those
columns, so at most \(n\) one-top flips suffice. By Theorem 5.1, a sign
vector with zero syndrome lies in the rectangle span.

For adjacent positions, exactly two cyclic intervals of any fixed
proper length contain one position but not the other. Swapping the
labels removes at most two interval sets and adds at most two. Summing
over at most \(n\) flips and \(H+1\) depths proves (5.4). Since
\(H\asymp\sqrt{m\log m}\), this is \(o(W)\). \(\square\)

If the mechanical pattern forbids adjacent cross-colour swaps, use two
same-colour positions. At depth \(q\le H\), this changes at most
\(4(H+q)\le8H\) coordinates. The all-depth exceptional cost is then
\(O(mH^2)=O(m^2\log m)=o(W)\).

This last cost estimate applies when the required syndrome-changing
one-top swaps are available within the chosen support. The unrestricted
theorem guarantees them in the full atlas; it does not prove that the
fixed-mechanical-shore rectangle sublattice has only the affine
syndromes of Theorem 5.1.

## 6. Exact boundary

Proved here:

1. an explicit four-top compound exchange of actual cyclic frames;
2. exact cancellation phase by phase at every interval length;
3. exact preservation of a common deleted phase and arbitrary common
   phase-tag schedules;
4. exact per-frame action \(4(H+q)\) through all \(q\le H\);
5. a choice carrying \(4H-O(H^2/m)\) local \(E_H\) action per top while
   having zero aggregate action;
6. the complete mod-two character space of the unrestricted quartet move
   lattice; and
7. the \(O(mH)=o(W)\) cost of correcting every parity syndrome.

Not proved here:

1. that quartet relations connect every two common-permutation clone
   couplings with the same target loads;
2. that arbitrary separate clone-Hall matchings deform into literal
   cyclic frames;
3. an energy-decreasing, rather than energy-flat, compound move; or
4. coefficient one.

The new exact boundary is a nonabelian/integral connectivity question.
The first large local harmonic is cancelled by a physical quartet, and
in the unrestricted physical atlas the sign/odd-parity projection has
only \(2m\) cheap charges. A surviving
obstruction must detect more than aggregate interval loads and
permutation sign, such as a higher representation of the rootwise
permutation group or a genuine odd-set inequality of the global
frame-matching polytope. If one insists on never leaving one fixed
mechanical support atlas, its restricted rectangle character space is an
additional, presently unaudited gate.

## 7. Inputs used

The common-permutation gate and its lag-\(H\) completion equations are
from MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md.
The exact bound (4.1) is from
MATH_THEOREM_L_PROMOTION_RING_HIGH_HARMONIC_COVARIANCE_AND_LOAD_ONLY_NOGO_20260726.md.
All compound-exchange, action, and parity arguments above are new and
self-contained.
