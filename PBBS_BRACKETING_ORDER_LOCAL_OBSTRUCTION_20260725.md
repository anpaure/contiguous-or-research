# PBBS enclosing-return orders admit simultaneous constant-density saturation

Date: 2026-07-25

Pure mathematics only.  No computation or external input is used.

## 0. Outcome

The two inactive-core enclosure ledgers cannot be sharpened by a universal
local endpoint-order loss.  There is an explicit canonical PBBS component,
in every rank \(r\ge 5\), containing a linear family of pairwise
projected-edge-disjoint simple gap-five sectors with all of the following
properties.

1. The previous/next occurrence orders on each inactive core differ by only
   \(r-O(1)\) inversions, rather than a positive fraction of the
   \(\Theta(r^2)\) possible inversions.
2. After the two cores are interlaced, the joint previous/next orders still
   differ by only \(O(r)\) inversions.
3. A subfamily of size \(\Theta(r)\) is compatible with one fixed middle
   set \(T\), and both inactive cores of every selected sector are genuinely
   mixed relative to \(T\).
4. That subfamily uses a fixed positive fraction of both the \(K\)- and the
   translated \(K'\)-enclosure capacities.

Thus neither endpoint-order disorder, nor a conflict between the two
translated parity decks, can by itself supply the missing \(o(1)\) factor
in the coefficient-one quotient-packing gate.  Any successful proof must
also use a global rarity/enumeration input (or the reciprocal-binomial tail
weights), not merely the local order type of the \(2q\) enclosing pairs.

This is not a counterexample to the coefficient-one theorem.  The component
used below has only three quotient states, and the completion weights of the
mixed sectors below are exponentially small.

## 1. The explicit canonical component

Put

\[
 N=2r+1.
\]

Use the exact three-root PBBS component

\[
 \begin{aligned}
 D_0&=110100(10)^{r-3},\\
 D_1&=1011(01)^{r-3}00,\\
 D_2&=(10)^{r-3}110010.
 \end{aligned}
 \tag{1.1}
\]

As proved in `PBBS_SEAM_ENDPOINT_ORDER_COUNTEREXAMPLE_20260725.md`, after
normalizing the first omitted physical label to zero, its lifted
omitted-label word is

\[
 \boxed{
 \lambda_{3j}=j,\qquad
 \lambda_{3j+1}=j+2,\qquad
 \lambda_{3j+2}=j+6
 \pmod N.}
 \tag{1.2}
\]

For one physical label \(x\), three consecutive occurrences (on a common
integer lift) are

\[
 3x-16,\qquad 3x-5,\qquad 3x.
 \tag{1.3}
\]

Consequently, for every \(x\), the interval from \(3x-5\) to \(3x\)
is a gap-five return.  Its omitted-label word is

\[
 \boxed{x, x+4, x-1, x+1, x+5, x.}
 \tag{1.4}
\]

When \(N\ge9\), the five half-open labels in (1.4) are distinct, so this
is a simple return with \(s=2\) and inactive-core size

\[
 q=r-2.
 \tag{1.5}
\]

Its projected trace is

\[
 \boxed{
 I_x=\{3x-6,3x-4,3x-2,3x\}
 \subset \mathbb Z/(3N).}
 \tag{1.6}
\]

### Lemma 1.1 (exact trace conflict graph)

For distinct \(x,y\in\mathbb Z_N\),

\[
 I_x\cap I_y\ne\varnothing
 \quad\Longleftrightarrow\quad
 x-y\equiv \pm2\pmod N.
 \tag{1.7}
\]

#### Proof

An equality between one edge in \(I_x\) and one edge in \(I_y\) gives

\[
 3(x-y)\equiv 2d\pmod{3N},
 \qquad -3\le d\le3.
\]

The right side is divisible by three only for \(d=0,\pm3\).  These give
\(x-y\equiv0,\pm2\pmod N\), respectively.  The converse is immediate
from (1.6).  \(\square\)

Thus all \(N\) gap-five sectors have conflict graph one odd cycle, and a
maximum edge-disjoint subfamily has size \(r\).  In particular, even before
using the common-\(T\) refinement below, these sectors occupy

\[
 {4r\over3N}={2\over3}+O(r^{-1})
 \tag{1.8}
\]

of the projected edges of this component.

## 2. Exact inactive cores of one normalized sector

Normalize at \(x=0\), so the sector runs from time \(-5\) to time \(0\).
Its active labels are

\[
 a_0=0,\quad b_0=4,\quad a_1=N-1,quad b_1=1,
 \quad a_2=5.
 \tag{2.1}
\]

At time zero, the state \(0D_0\) has one-set

\[
 A_0^{\rm glob}=\{1,2,4\}\cup\{7,9,\ldots,N-2\}.
 \tag{2.2}
\]

The endpoint normal form says

\[
 A_0^{\rm glob}=K'\cup\{b_0,b_1\}.
\]

It follows that

\[
 \boxed{
 K'=\{2\}\cup\{7,9,\ldots,N-2\},
 \qquad
 K=\{3\}\cup\{6,8,\ldots,N-3\}.}
 \tag{2.3}
\]

Both sets have size \(q=r-2\).

## 3. Exact previous/next endpoint permutations

For an inactive label \(z\), let \(p(z)<-5<0<n(z)\) be the consecutive
occurrences bracketing the sector.  Formula (1.3) gives

\[
 \begin{array}{c|cc}
 z&p(z)&n(z)\\ \hline
 2&-10&1\\
 3&-7&4\\
 6\le z\le N-2&3z-3N&3z-16.
 \end{array}
 \tag{3.1}
\]

Adding five to every time converts these into the local indexing of the
sector.  In particular, the labels in \(K\) have even previous and odd next
indices, while those in \(K'\) have odd previous and even next indices, as
required by the two-enclosure lemma.

Order labels first by increasing previous occurrence and then by increasing
next occurrence.  From (3.1), the two core orders are

\[
 \begin{array}{c|c|c}
 &p\text{-order}&n\text{-order}\\ \hline
 K&6,8,\ldots,N-3,3&6,3,8,10,\ldots,N-3,\\[1mm]
 K'&7,9,\ldots,N-4,2,N-2&2,7,9,\ldots,N-2.
 \end{array}
 \tag{3.2}
\]

Therefore the two order permutations are

\[
 \boxed{
 \pi_K=(1,3,4,\ldots,q,2),
 \qquad
 \pi_{K'}=(2,3,\ldots,q-1,1,q).}
 \tag{3.3}
\]

Each has exactly \(q-2\) inversions.

There is also an exact joint statement.  Put all \(2q=N-5\) inactive
labels in one list, without separating the two parities.  Their orders are

\[
 \begin{aligned}
 P&=(6,7,\ldots,N-4,2,N-3,3,N-2),\\
 Q&=(2,6,3,7,8,\ldots,N-2).
 \end{aligned}
 \tag{3.4}
\]

For \(q\ge3\), the permutation which changes \(P\) into \(Q\) is

\[
 (2,4,5,\ldots,2q-2,1,2q-1,3,2q),
 \tag{3.5}
\]

and has exactly

\[
 \boxed{4q-8}
 \tag{3.6}
\]

inversions.  Hence its normalized Kendall distance is \(O(1/q)\).

In interval language, equal previous/next order means that the enclosing
intervals cross, while an inversion means that they nest.  Thus (3.3)--(3.6)
also say that both decks, and their joint interlacing, have the maximum
possible crossing density up to \(O(1/q)\).  In particular, no positive
density of nesting or endpoint-order disorder is forced by PBBS chronology.

## 4. A common bulk-compatible middle set

The preceding order obstruction can be made simultaneously compatible with
one fixed middle set.  Work with integer representatives
\(0,1,\ldots,N-1\), and initially put

\[
 T_0=\{z:z\equiv1,3,4\pmod6\}.
 \tag{4.1}
\]

In fact, if \(N\equiv1\) or \(3\pmod6\), then \(|T_0|=r\).  If
\(N\equiv5\pmod6\), then \(|T_0|=r+1\); remove one coordinate of residue
three.  In all cases this gives an exact \(r\)-set \(T\), changed from
\(T_0\) at at most one coordinate of residue three.

Let

\[
X=\{x: x\equiv0\pmod6,\ 6\le x\le N-7\}.
 \tag{4.2}
\]

Coordinates of residue two or three do not occur among the five active
labels

\[
 x, x+4, x-1, x+1, x+5
\]

when \(x\equiv0\pmod6\).  Hence the adjustment from \(T_0\) to \(T\)
does not affect any active pattern.  For every \(x\in X\), one has

\[
 \mathbf1_T(x),\mathbf1_T(x+4),\mathbf1_T(x-1),
 \mathbf1_T(x+1),\mathbf1_T(x+5)
 =0,1,0,1,0.
 \tag{4.3}
\]

Thus every selected sector is odd-tail compatible with the same \(T\).

The traces are pairwise disjoint.  Indeed, two members of \(X\) differ by
a nonzero multiple of six strictly smaller than \(N-2\), so Lemma 1.1
applies.  All starts \(3x-5\) also have the same parity, so both the
\(K\)-traces and their one-edge-translated \(K'\)-traces lie in the fixed
parity decks required by the enclosure ledger.  Moreover

\[
 |X|={N\over6}+O(1).
 \tag{4.4}
\]

Finally, both cores are genuinely mixed.  The translated versions of
(2.3) consist, apart from one exceptional label, of a consecutive
step-two arithmetic progression.  In every three successive terms of such
a progression, the residue set (4.1) contains either one or two terms.
The \(O(1)\) adjustment is harmless.  Uniformly for \(x\in X\),

\[
 {q\over3}-O(1)
 \le |K_x\cap T|\le
 {2q\over3}+O(1).
 \tag{4.5}
\]

Since \(T\) contains the two active \(b\)-labels and none of the three
active \(a\)-labels, its total inactive load is \(q\).  Therefore (4.5)
implies the same mixed bounds, with the two constants interchanged, for
\(|K'_x\cap T|\).  These are genuinely bulk sectors: both relevant
binomial parameters tend linearly to infinity.

## 5. Simultaneous positive utilization of both enclosure decks

Every sector above has \(|I_x|=4\) and \(|K_x|=|K'_x|=q=r-2\).  The
component has \(3N\) projected edges.  Applying the core-enclosure ledger
separately to this one component gives capacity

\[
 (r+1)3N
 \tag{5.1}
\]

on each translated parity deck.  The family from Section 4 uses, on each
deck,

\[
 \sum_{x\in X}|K_x|\,|I_x|
 =4(r-2)|X|.
 \tag{5.2}
\]

Consequently its utilization ratio on both decks is

\[
 \boxed{
 {4(r-2)|X|\over3N(r+1)}
 ={2\over9}+o(1).}
 \tag{5.3}
\]

If the common-\(T\) condition is dropped, take instead all multiples of four
in a nonwrapping interval of length \(N-O(1)\).  This is a same-start-parity
edge-disjoint family of size \(N/4+O(1)\), and the corresponding ratio is

\[
 {4(r-2)(N/4+O(1))\over3N(r+1)}={1\over3}+o(1)
 \tag{5.4}
\]

on both decks simultaneously.

## 6. Exact scope of the obstruction

Equations (3.3)--(3.6) rule out any local theorem asserting that a bulk
simple sector must create a positive density of endpoint-order defects in
one of the two inactive-core decks.  Equations (4.3)--(5.3) rule out the
stronger proposal that a common tail-compatible \(T\), genuine core mixing,
and projected-edge disjointness force the two deck utilizations to be
\(o(1)\) inside every PBBS component.

The example does not threaten the desired global theorem:

* it occupies only a three-state quotient component;
* after quotienting spatial phase, it contributes only \(O(1)\) sectors;
* in (4.5), reciprocal-binomial completion weights are exponentially small.

Thus the remaining coefficient-one gain, if obtained through the
bracketing chronology, must combine endpoint order with a global count of
which quotient components can support that order (or with the completion
kernel).  Separate or joint local residence-capacity ledgers, even with the
full previous/next order permutations retained, cannot yield the required
vanishing factor.
