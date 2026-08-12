# Chung--Feller automorphism maximality and the suspended-pentagon boundary

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Verdict

Let \(D_r\) be the Dyck \(r\)-subsets of \([2r]\), let
\(D_{2r}^t\), \(0\le t\le r\), be the Chung--Feller flaw layers, and put

\[
 H_r=\langle(2\ 3),(4\ 5),\ldots,(2r-2\ \ 2r-1)\rangle .
\tag{0.1}
\]

There are three different symmetry categories, and they must not be
identified.

1. The complete coordinate-permutation stabilizer of \(D_r\), and hence
   of all the Chung--Feller layers, is exactly \(H_r\).  There is no
   coordinate permutation beyond (0.1).
2. The layer-coloured Johnson graph has one additional coset.  If
   \(R(i)=2r+1-i\), \(C(X)=[2r]\setminus X\), and
   \(\omega=CR\), then
   \[
    \operatorname {Aut}\bigl(J(2r,r);D_{2r}^0,\ldots,D_{2r}^r\bigr)
       =H_r\rtimes\langle\omega\rangle .
   \tag{0.2}
   \]
   The extra element is reverse--complement.
3. A covariant automorphism of the literal lower/upper inclusion geometry
   has no complement coset, so its layer stabilizer is again \(H_r\).
   The extra coset in (0.2) has a physical *contravariant* lift: reverse
   every path in phase and reverse its coordinates.

Every genuine global symmetry in (0.2) transports the peak-erased Motzkin
normal form equivariantly.  Thus no symmetry conjugate of a leaf packet,
or of the root-scale pentagon, breaks that invariant.  A naive statewise
reverse--complement of the pentagon is not even exact: it has a nonzero
intersection-ledger defect.

The tempting positive construction obtained by suspending the rooted
size-three pentagon once by \(J(x)=1x0\) does not lie in the requested
class.  It remains an exact port-preserving packet, but suspension exchanges
the roles of the lower-state and upper-colour columns.  Its lower states no
longer preserve the individual Chung--Feller phase layers.  The pentagon's
five-cycles survive in the suspended **upper-colour** owner routing, and
some shared lower tokens also change owner across peak-erased classes, but
there is no permutation of one fixed Chung--Feller lower layer.  Thus the
global-symmetry route ends in a maximality/no-go theorem, not a new
fixed-layer construction.

## 1. Coordinate maximality

Identify a Dyck word with the set of positions of its up-steps.  Thus

\[
 D_r=\bigl\{\{p_1<\cdots<p_r\}:p_i\le2i-1\bigr\}.
\tag{1.1}
\]

For \(1\le i\le2r\), put

\[
 a_i=|\{P\in D_r:i\in P\}|.
\tag{1.2}
\]

### Lemma 1.1 (exact coordinate frequencies)

For \(1\le j<r\),

\[
 a_{2j}=a_{2j+1},
 \qquad
 a_{2j}-a_{2j+2}
   =\operatorname {Cat}_j\operatorname {Cat}_{r-j-1}>0.
\tag{1.3}
\]

Moreover

\[
 a_1-a_2=\operatorname {Cat}_{r-1}>0,
 \qquad a_{2r}=0.
\tag{1.4}
\]

#### Proof

Immediately before positions \(2j,2j+1\), a Dyck path has odd positive
height.  Interchanging those two steps therefore preserves Dyckness: only
\(10\) and \(01\) are exchanged, and the temporary down-step in the
second order starts at height at least one.  This proves the first identity
in (1.3).

For the second, use that identity and compare positions \(2j+1\) and
\(2j+2\).  Swapping the two adjacent steps pairs every Dyck path with local
pattern \(10\) to one with pattern \(01\), except when the height after
\(2j\) steps is zero.  The unpaired paths factor uniquely as

\[
 (\text{Dyck path of semilength }j)\;10\;
 (\text{Dyck path of semilength }r-j-1).
\tag{1.5}
\]

Their number is the product in (1.3).  Finally every Dyck word starts with
one and ends with zero.  Those which omit position two start with \(10\)
and have an arbitrary Dyck suffix of semilength \(r-1\), proving (1.4).
\(\square\)

### Theorem 1.2 (coordinate-stabilizer maximality)

For every \(r\ge1\),

\[
 \boxed{\operatorname {Aut}_{S_{2r}}(D_r)=H_r.}
\tag{1.6}
\]

Every member of this group preserves every Chung--Feller layer.  Hence

\[
 \boxed{
 \{\pi\in S_{2r}:\pi D_{2r}^t=D_{2r}^t\text{ for all }t\}=H_r.}
\tag{1.7}
\]

#### Proof

Lemma 1.1 shows that the coordinate-frequency classes of the set system
\(D_r\) are exactly

\[
 \{1\},\{2,3\},\{4,5\},\ldots,
 \{2r-2,2r-1\},\{2r\},
\tag{1.8}
\]

and that their frequencies are strictly decreasing from left to right.
Every coordinate automorphism preserves these classes.  It can therefore
only interchange the entries within the displayed two-element blocks.
The first paragraph of Lemma 1.1 shows that every such interchange is an
automorphism, independently of the others.  This proves (1.6).

For a general balanced word, the height immediately before positions
\(2j,2j+1\) is odd and hence nonzero.  If it is positive, both orders of
the two steps have their edge interiors on or above the axis; if it is
negative, both orders have the same number of edge interiors below the
axis.  The endpoint after the pair is unchanged.  Thus the transposition
preserves the flaw number of every balanced word, proving (1.7).  The case
\(r=1\) is trivial. \(\square\)

There are consequently no small-r exceptional coordinate enlargements:
\(H_1=1\), \(H_2=\langle(2\ 3)\rangle\), and (1.6) holds thereafter.

## 2. The unique extra Johnson-layer duality

Let \(C\) denote complementation on \(r\)-subsets and let \(R\) reverse
the \(2r\) coordinates.  Put

\[
 \omega=CR.
\tag{2.1}
\]

### Lemma 2.1 (reverse--complement fixes flaw)

If \(H_w(k)\) is the height of a balanced word \(w\) after \(k\) steps,
then

\[
 H_{\omega w}(k)=H_w(2r-k).
\tag{2.2}
\]

Consequently \(\omega\) preserves every Chung--Feller layer, including
\(D_r\).

#### Proof

If the steps of \(w\) are \(\epsilon_1,\ldots,\epsilon_{2r}\), then the
steps of \(\omega w\) are
\(-\epsilon_{2r},\ldots,-\epsilon_1\).  Since their total sum is zero,
summing the first \(k\) transformed steps gives (2.2).  Each transformed
edge is the corresponding original edge traversed in reverse, so its
position above or below the axis is unchanged. \(\square\)

### Theorem 2.2 (layer-coloured Johnson automorphisms)

For \(r\ge2\),

\[
 \boxed{
 \operatorname {Aut}\bigl(J(2r,r);D_{2r}^0,\ldots,D_{2r}^r\bigr)
 =H_r\rtimes\langle\omega\rangle .}
\tag{2.3}
\]

Conjugation by \(\omega\) sends

\[
 (2i\ \ 2i+1)\longmapsto
 (2r-2i\ \ 2r-2i+1).
\tag{2.4}
\]

#### Proof

The maximal cliques of \(J(2r,r)\) are the stars consisting of all
\(r\)-sets containing one fixed \((r-1)\)-set and the tops consisting of
all \(r\)-sets contained in one fixed \((r+1)\)-set.  An automorphism
either preserves these two types or interchanges them.  Indeed, join two
maximal cliques when their intersection has size two.  The resulting
clique-incidence graph is connected and bipartite, with stars and tops as
its two parts, so its bipartition is preserved or exchanged globally.  In
the first case, the induced action on stars descends to the Johnson graph
on \((r-1)\)-sets.  At every lower rank the two clique sizes differ;
iterating through stars reconstructs a permutation of the singleton
coordinates.  In the second case, composition with complementation reduces
to the first.  Hence every Johnson automorphism is either a coordinate
permutation \(\pi\) or \(C\pi\).

If \(\pi\) preserves all layers, Theorem 1.2 gives \(\pi\in H_r\).  If
\(C\pi\) preserves them, then \(\omega^{-1}C\pi=R\pi\) is a coordinate
layer stabilizer and hence belongs to \(H_r\).  Thus the second coset is
\(\omega H_r\).  Lemma 2.1 and Theorem 1.2 show that every displayed
element really preserves all layers, and (2.4) is immediate from coordinate
reversal. \(\square\)

For \(r=1\), \(\omega\) acts trivially and the layer stabilizer is trivial.

## 3. Exact packet geometry: covariant versus contravariant actions

Let \({\cal M}_r\) be the bipartite inclusion graph on

\[
 {\cal X}=\binom{[2r]}r,
 \qquad
 {\cal Y}=\binom{[2r]}{r+1}.
\tag{3.1}
\]

An exact cut-path packet must preserve both the \({\cal X}\)-state ledger
and the \({\cal Y}\)-union ledger.

### Proposition 3.1 (covariant exact automorphisms)

The automorphisms of \({\cal M}_r\) are coordinate permutations.  Those
which preserve \(D_r\) and every Chung--Feller state layer form exactly
\(H_r\).

#### Proof

For \(r=1\) the assertion is immediate.  Assume \(r\ge2\).
An \({\cal X}\)-vertex has degree \(r\), while a \({\cal Y}\)-vertex has
degree \(r+1\), so the two shores are fixed.  Two distinct \({\cal X}\)
vertices are Johnson-adjacent exactly when they have a common
\({\cal Y}\)-neighbour.  Hence an automorphism restricts to a Johnson
automorphism.  A complement-type Johnson automorphism interchanges star
and top cliques and cannot preserve the upper-neighbourhood tops.
Therefore only coordinate permutations extend.  Theorem 1.2 finishes the
proof. \(\square\)

There is nonetheless a contravariant physical lift of the extra coset in
(2.3).  For a complete trace

\[
 X_0,X_1,\ldots,X_r,
 \qquad Y_t=X_t\cup X_{t+1},
\tag{3.2}
\]

define

\[
 \widetilde X_t=R(X_{r-t}).
\tag{3.3}
\]

Then

\[
 \widetilde Y_t
 =\widetilde X_t\cup\widetilde X_{t+1}
 =R(Y_{r-t-1}).
\tag{3.4}
\]

Coordinate reversal sends flaw layer \(r-t\) to flaw layer \(t\), so
(3.3) is phase-respecting after the phase reversal.  If the old endpoints
are \(P,\overline P\), the new endpoints are

\[
 R(\overline P)=\omega P,
 \qquad R(P)=\overline{\omega P}.
\tag{3.5}
\]

Thus (3.3) preserves both exact ledgers and realizes the root action
\(\omega\).  Combining it with \(H_r\) gives the full ambient
coordinate/phase symmetry (2.3).

For completeness, if the steps of \(w\) are \(\epsilon_i\), coordinate
reversal alone has height history

\[
 H_{Rw}(k)=-H_w(2r-k).
\tag{3.5a}
\]

It reflects every edge of the old path across the axis while reversing
its time order.  Thus the number of below-axis step pairs changes from
\(t\) to \(r-t\), which is the asserted layer reversal.

This classification concerns global ambient symmetries.  Arbitrary
permutations inside the individual finite sets \(D_{2r}^t\) form a huge
setwise group, but they do not preserve Johnson arrows or the union ledger
and are not packet conjugators.  Legal phasewise interleavings are instead
constrained packet constructions; they are not automorphisms of the
ambient incidence geometry.

### Proposition 3.2 (the statewise-duality test)

If one applies \(\omega\) to every state without reversing the phase
order, then for every Johnson edge \(X,X'\),

\[
 \omega X\cup\omega X'
 =R\bigl([2r]\setminus(X\cap X')\bigr).
\tag{3.6}
\]

Therefore a statewise \(\omega\)-image of a packet is exact if and only if
the packet's two sides have the same adjacent-intersection multiset.

#### Proof

Equation (3.6) is De Morgan's law.  The map on the right is a bijection
from \((r-1)\)-sets to \((r+1)\)-sets, so equality of the transformed
union ledgers is equivalent to equality of the old intersection ledgers.
\(\square\)

For the octahedral leaf rectangle, suppressing a common spectator \(Q\),
both sides have intersection multiset

\[
 \{Q1,Q2,Q3,Q4\}.
\tag{3.7}
\]

Hence its statewise \(\omega\)-image happens to remain exact.

For the rooted size-three pentagon, direct intersection of consecutive
states in its two displayed five-row tables gives

\[
\mathcal I^- -\mathcal I^+
 =e_{15}+e_{26}+e_{34}-e_{14}-e_{25}-e_{36}\ne0.
\tag{3.8}
\]

Indeed the old intersection multiset is

\[
 \{12,13,15,16,16,23,24,25,26,34,34,35,45,46,56\},
\tag{3.9}
\]

whereas the new one is

\[
 \{12,13,14,16,16,23,24,25,25,34,35,36,45,46,56\}.
\tag{3.10}
\]

Thus no statewise \(\omega h\)-image, \(h\in H_3\), of that pentagon is an
exact packet.  This does not contradict (3.3): the correct physical lift
of \(\omega\) reverses the whole path as well as the coordinates.

## 4. Symmetry conjugation does not break peak erasure

Write a Dyck word as

\[
 w=1\,b_1b_2\cdots b_{r-1}\,0,
 \qquad |b_i|=2,
\tag{4.1}
\]

and encode

\[
 11=U,\qquad00=D,\qquad10=L_0,\qquad01=L_1.
\tag{4.2}
\]

After forgetting the level colour, this is a Motzkin excursion \(M(w)\).
Let \(\rho(w)\) be its unique normal form under

\[
 UD\longrightarrow LL.
\tag{4.3}
\]

Let \(\dagger\) reverse a Motzkin word, interchange \(U,D\), and leave
the level colours unchanged.

### Lemma 4.1 (equivariance)

For \(h\in H_r\),

\[
 \rho(hw)=\rho(w),
\tag{4.4}
\]

after level colours are forgotten.  Moreover

\[
 M(\omega w)=M(w)^\dagger,
 \qquad
 \rho(\omega w)=\rho(w)^\dagger.
\tag{4.5}
\]

#### Proof

The generators of \(H_r\) only exchange \(10\) and \(01\) in one block,
proving (4.4).  Reverse--complement reverses the block order, interchanges
\(11\) and \(00\), and fixes each of \(10,01\).  This proves the first
identity in (4.5).  The rule \(UD\to LL\) is \(\dagger\)-equivariant, so
its unique normal form is also equivariant. \(\square\)

### Theorem 4.2 (symmetry-conjugation no-go)

No conjugate by the global symmetry group
\(H_r\rtimes\langle\omega\rangle\) can turn a
\(\rho\)-preserving packet action into a \(\rho\)-breaking action.

In particular:

1. every symmetry conjugate of a leaf packet preserves \(\rho\); and
2. every symmetry conjugate of the root-scale size-three pentagon
   preserves \(\rho\).

Even if the phase duality itself is admitted as a move, the unordered
pair

\[
 \{\rho(w),\rho(w)^\dagger\}
\tag{4.6}
\]

remains invariant.  For \(r\ge4\), the two dagger-fixed peak-free paths

\[
 L^{r-1},
 \qquad UL^{r-3}D
\tag{4.7}
\]

are distinct, so the symmetry-enlarged leaf route remains disconnected.

#### Proof

For a leaf edge, the Motzkin quotient is either unchanged or is
\(UD\leftrightarrow LL\), so its endpoints have equal \(\rho\).  Lemma
4.1 transports this equality through every symmetry conjugate.

At size three, the five Dyck roots have Motzkin words \(UD\) or \(LL\),
all with normal form \(LL\).  Hence the two pentagon five-cycles also
preserve \(\rho\), and Lemma 4.1 again applies.  Formula (4.6) and the
separation in (4.7) are immediate. \(\square\)

## 5. Why one pentagon suspension is not a fixed-layer escape

The distinction between aggregate exactness and phase-layer preservation
is visible under the elementary context \(\mathsf J(x)=1x0\).

Let the local ground set be \(K\), and let a local semilength-\(s\) trace be

\[
 X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s,
\tag{5.1}
\]

and let \(\ell,r\) be the two coordinates added by \(\mathsf J\).  All local
coordinates below are understood to be shifted into the new interval.

### Lemma 5.1 (exact ledger exchange under \(\mathsf J\))

The wrapped lower states are

\[
 \widehat X_0=\{\ell\}\cup X_0,
 \qquad
 \widehat X_{s+1}=\{r\}\cup X_s,
\tag{5.2}
\]

and, for \(1\le k\le s\),

\[
 \boxed{
 \widehat X_k
   =\{\ell,r\}\cup\bigl(K\setminus Y_{s-k}\bigr).}
\tag{5.3}
\]

The wrapped upper colours are

\[
 \widehat Y_0=\{\ell,r\}\cup X_0,
 \qquad
 \widehat Y_s=\{\ell,r\}\cup X_s,
\tag{5.4}
\]

and, for \(1\le k<s\),

\[
 \boxed{
 \widehat Y_k
   =\{\ell,r\}\cup\bigl(K\setminus X_{s-k}\bigr).}
\tag{5.5}
\]

Consequently \(\mathsf J\) preserves aggregate exactness of every rooted
packet whose two sides have equal ledgers and pointwise equal row
endpoints, but it exchanges the roles of its internal lower-state columns
and upper-colour columns.  Columnwise preservation of the old \(X\)-layers
does not imply columnwise preservation of the wrapped \(X\)-layers.

#### Proof

Write transition \(t\) of the local trace as insertion of \(a_t\) and
deletion of \(d_t\).  Its flip word is

\[
 \rho=(a_1,d_1,a_2,d_2,\ldots,a_s,d_s).
\tag{5.6}
\]

The wrapped flip word is

\[
 \widehat\rho
  =(r,d_s,a_s,d_{s-1},a_{s-1},\ldots,d_1,a_1,\ell).
\tag{5.7}
\]

Pairing its successive insertion/deletion entries gives (5.2)--(5.3).
Equivalently, the first internal state is

\[
 \{\ell,r\}\cup(X_0\setminus\{d_s\})
 =\{\ell,r\}\cup(K\setminus Y_{s-1}),
\]

and the same calculation after each reversed exchange gives the general
formula.

Now use

\[
 Y_{t-1}\cap Y_t=X_t
 \qquad(1\le t<s).
\tag{5.8}
\]

Taking unions of consecutive states in (5.3), and applying De Morgan's
law, gives (5.4)--(5.5).  Thus all internal wrapped \(X\)-states are an
injective image of all old \(Y\)-colours, and all internal wrapped
\(Y\)-colours are an injective image of all old \(X\)-states.  Aggregate
equality of both old ledgers proves aggregate equality of both wrapped
ledgers. \(\square\)

Now take the five size-three Dyck words

\[
\begin{aligned}
 T_1&=111000,&T_2&=110100,&T_3&=110010,\\
 T_4&=101010,&T_5&=101100.
\end{aligned}
\tag{5.9}
\]

The rooted pentagon has internal lower-state owner permutations

\[
 c_1=(1\ 2\ 5\ 3\ 4),
 \qquad
 c_2=(1\ 2\ 3\ 5\ 4).
\tag{5.10}
\]

Its old and new first upper-colour columns are respectively

\[
 \{1236,1246,1245,1235,1234\}
\tag{5.11}
\]

and

\[
 \{1236,1234,1235,1356,1345\}.
\tag{5.12}
\]

They are unequal.  By the injective map in (5.3), the corresponding fixed
column of wrapped lower states is unequal on the two packet sides.
Therefore the suspended pentagon, although exact after aggregation, does
not preserve the canonical Chung--Feller \(X\)-layer at that phase.

The complete internal wrapped lower-state audit, after suppressing the
fixed pair \(\{\ell,r\}\), is

\[
\begin{array}{c|ccccc}
-&(23,25,45)&(24,34,35)&(12,26,36)&(13,16,46)&(14,15,56)\\
+&(23,34,45)&(12,16,56)&(15,14,46)&(35,25,24)&(13,36,26).
\end{array}
\tag{5.12a}
\]

Each row of this display enumerates all fifteen two-subsets of the local
six-set, confirming aggregate \(X\)-exactness while exposing the
columnwise mismatch.

For clarity, the tempting Motzkin calculation itself is correct.  For
\(r\ge4\), put

\[
 K_r(x)=1x0(10)^{r-4},
 \qquad W_i=K_r(T_i).
\tag{5.13}
\]

Then

\[
\begin{array}{c|ccccc}
 &W_1&W_2&W_3&W_4&W_5\\ \hline
 M(W_i)&ULD\,L^{r-4}&ULD\,L^{r-4}&UDL\,L^{r-4}
       &L^{r-1}&LUD\,L^{r-4}\\
 \rho(W_i)&ULD\,L^{r-4}&ULD\,L^{r-4}&L^{r-1}
       &L^{r-1}&L^{r-1}.
\end{array}
\tag{5.14}
\]

Formulas (5.5) and (5.10) show that the suspended packet's
**upper-colour** owner routing crosses the two classes in (5.14).  This is
not a Chung--Feller lower-state phase automorphism and therefore is not a
counterexample to Theorem 4.2 or to the requested no-go.

There is also a literal lower-token transfer across the same partition:
after suppressing the fixed outer coordinates, the wrapped phase-two state
\(25\) is owned by row \(W_1\) on the old side and by row \(W_4\) on the
new side.  Equation (5.14) gives

\[
 \rho(W_1)=ULD\,L^{r-4},
 \qquad
 \rho(W_4)=L^{r-1}.
\tag{5.15}
\]

This is a slab-level owner reassignment, not an automorphism of the fixed
phase palette: the unequal columns (5.11)--(5.12) are still the decisive
obstruction.

## 6. Exact boundary of the result

The classification is maximal for global coordinate and ambient phase
symmetries:

\[
 \operatorname {Aut}_{\rm coord}(D_r)=H_r,
 \qquad
 \operatorname {Aut}_{\rm Johnson,layer}
   =H_r\rtimes\langle\omega\rangle .
\tag{6.1}
\]

The extra coset is a reverse--complement duality.  Its physical lift
reverses the whole trace, and its action on Motzkin normal forms is only
\(\rho\mapsto\rho^\dagger\).  Hence neither leaf packets nor the
root-scale size-three pentagon acquire a peak-erasure-breaking lower-phase
action from any admissible global conjugation.

The one-suspension calculation identifies the sharp nearby obstruction:
in this construction the pentagon breaks peak erasure in a fixed
upper-colour column while mixing the lower Chung--Feller phase columns.
Appending common zigzags does not remove this defect.  No universal
only-if statement for every possible pentagon context is asserted.

This does not classify all non-ambient tuples of phasewise row
permutations satisfying Johnson adjacency and the aggregate union ledger.
A genuine fixed-lower-layer interleaving outside the global automorphism
group remains a separate construction problem.  What is proved here is
the requested maximality/no-go for every coordinate or ambient
phase-layer symmetry conjugation.
