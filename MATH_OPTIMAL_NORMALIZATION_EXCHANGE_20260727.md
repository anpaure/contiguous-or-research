# Equality and normalization for optimal contiguous-OR words

Date: 2026-07-27

## 1. Purpose and verdict

Put

\[
r=\lceil k/2\rceil,\qquad W=\binom kr,
\qquad L=\sum_{s=1}^{r-1}\binom ks,
\]

and let (d) be least with

\[
L\le dW+\binom{d+1}{2}.
\]

Thus (B(k)=W+d).  The finite optimal words suggest the much stronger
normal form in which (D^dA) is the complete rank-(r) layer and the first
witness depths are ordered by rank.

The conclusions of this note are:

1. Equality at (B(k)) forces a precise banded double-chain skeleton, but it
   does **not** force an arbitrary optimal representative to have a flat
   central derivative.
2. Realizability of an arbitrary *full* prescribed witness system has an
   exact coordinatewise criterion.  This upgrades the earlier lower-band pin
   criterion and gives a rigorous test for every proposed exchange.
3. Rank normalization reduces to one sharply stated cut-exchange axiom.
   Central flattening is a second, independent corner-straightening axiom.
4. A seven-entry optimum in dimension four proves that central flattening
   cannot be achieved by a general one-entry local exchange.  Any
   normalization theorem must permit a genuinely coupled retiming.

No existence claim is made for either missing exchange axiom.

## 2. What equality actually forces

Let (A=(A_1,\ldots,A_n)), (n=W+d), be a nonzero universal word.  For a
physical interval (I=[a,b]), write (U_A(I)=\bigcup_{i\in I}A_i).

Choose one witness (I_T=[a_T,b_T]) for every rank-(r) target (T), and
order these (W) intervals by their left endpoints:

\[
I_i=[a_i,b_i]\qquad(1\le i\le W).
\]

Two distinct selected equal-rank intervals cannot be nested, since physical
containment implies containment of their OR labels.  Therefore

\[
a_1<\cdots<a_W,\qquad b_1<\cdots<b_W.
\]

Since (a_i,b_i) are increasing (W)-subsets of ([W+d]),

\[
a_i\ge i,\qquad b_i\le i+d,qquad
\boxed{I_i\subseteq[i,i+d].}
\tag{2.1}
\]

Every interval of length at least (d+1) contains one of the (I_i), so
its OR has rank at least (r).  Hence every target of rank below (r) has a
witness of length at most (d).

Choosing one such witness for every lower target places the whole punctured
lower ideal into the physical band

\[
\mathcal B_{n,d}=\{[i,j]:0\le j-i<d\}.
\]

At a fixed left endpoint the labels form a strict inclusion chain; at a
fixed right endpoint they form a strict inclusion chain in the reverse
direction; and two chains meet in at most one label.  The number of unchosen
band cells is exactly

\[
\sigma=dn-\binom d2-L
=dW+\binom{d+1}{2}-L.
\tag{2.2}
\]

This is the genuine equality skeleton: an ordered orthogonal double-chain
packing with exactly (sigma) holes.  It does not choose one derivative
row for the middle layer, nor does it order incomparable Boolean labels by
rank.

There is a useful endpoint parametrization of the central witnesses.  Write

\[
a_i=i+\alpha_i,\qquad b_i=i+\beta_i.
\]

Then

\[
0\le\alpha_1\le\cdots\le\alpha_W\le d,
\quad
0\le\beta_1\le\cdots\le\beta_W\le d,
\quad \alpha_i\le\beta_i.
\tag{2.3}
\]

The observed flat central factor is the single extreme point

\[
\alpha_i=0,qquad\beta_i=d\qquad(1\le i\le W),
\tag{2.4}
\]

not a consequence of (2.3).

## 3. Exact realization theorem for a full witness system

The next theorem turns witness retiming into a precise finite condition.

### Theorem 3.1 (full witness realization)

Let (mathcal I=(I_S)_{\varnothing\ne S\subseteq[k]}) be an injective
assignment of a physical interval in ([n]) to every nonzero mask.  For each
coordinate (b\in[k]), define its legal position set

\[
Z_b(\mathcal I)
=[n]\setminus\bigcup_{S:\,b\notin S}I_S.
\tag{3.1}
\]

There exists a nonzero word (A=(A_1,\ldots,A_n)) satisfying

\[
U_A(I_S)=S\qquad\text{for every }S\ne\varnothing
\tag{3.2}
\]

if and only if

\[
I_S\cap Z_b(\mathcal I)\ne\varnothing
\quad(S\ne\varnothing, b\in S),
\tag{3.3}
\]

and

\[
\bigcup_{b=1}^k Z_b(\mathcal I)=[n].
\tag{3.4}
\]

When these conditions hold, the entrywise maximal realization is

\[
A_i^{\max}=\{b:i\in Z_b(\mathcal I)\}.
\tag{3.5}
\]

Every other realization is obtained by choosing, for each (b), a hitting
set (H_b\subseteq Z_b) meeting every (I_S) with (b\in S), subject to
(\bigcup_bH_b=[n]).

#### Proof

If (b\) occurs at a position belonging to a prescribed interval (I_S)
with (b\notin S), then (3.2) fails.  Thus every occurrence of (b) lies in
(Z_b).  Each positive interval must contain an occurrence, giving (3.3),
and nonzero entries give (3.4).

Conversely, use (3.5).  If (b\notin S), definition (3.1) gives
(I_S\cap Z_b=\varnothing), so (b) is absent from (U_A(I_S)).  If
(b\in S), (3.3) puts (b) into that union.  Hence the union is exactly
(S).  Condition (3.4) makes every entry nonempty.  The hitting-set
description follows by the same coordinatewise argument.  (square)

### Corollary 3.2 (interval-order gate)

Every realizable full witness assignment is order-preserving in the sense

\[
I_S\subseteq I_T\quad\Longrightarrow\quad S\subseteq T.
\tag{3.6}
\]

Consequently, if (|S|<|T|) but the assigned witness of (S) is longer
than that of (T), their two physical intervals must be incomparable.

For a proposed exchange of the labels on two intervals (I,J), the first
cheap necessary test is

\[
K(I)\subseteq\text{new label at }I\subseteq F(I),
\tag{3.7}
\]

where (K(I)) is the union of the labels on prescribed proper subintervals
of (I), and (F(I)) is the intersection of the labels on prescribed
proper superintervals of (I).  Passing (3.7) is not sufficient: the exact
remaining test is (3.3)--(3.4) after recomputing all (Z_b).

This cleanly separates an order obstruction from the global pin obstruction.

## 4. The exact missing rank-exchange axiom

For a word (A), let

\[
\tau_A(S)=\min\{|I|-1:U_A(I)=S\}
\]

be shortest-witness depth, and define the nested cut families

\[
\mathcal F_j(A)=\{S\ne\varnothing:\tau_A(S)\le j\}.
\tag{4.1}
\]

A shortest-depth profile is rank-monotone exactly when every
(mathcal F_j(A)) is rank-initial: whenever (T\in\mathcal F_j) and
(|S|<|T|), one has (S\in\mathcal F_j).

The following is the smallest one-cut exchange statement that would force
the normalization.

### Axiom CCE (cut-compression exchange)

Let (A) be a length-(B(k)) universal word and let (j<d).  If

\[
T\in\mathcal F_j(A),\qquad S\notin\mathcal F_j(A),qquad |S|<|T|,
\tag{4.2}
\]

then there is a length-(B(k)) universal word (A') such that

\[
\mathcal F_h(A')=\mathcal F_h(A)\quad(h<j),
\tag{4.3}
\]

and

\[
\mathcal F_j(A')
=\bigl(\mathcal F_j(A)\setminus\{T\}\bigr)\cup\{S\}.
\tag{4.4}
\]

No condition is imposed on later cuts.

### Theorem 4.1 (CCE implies rank normalization)

If CCE holds in dimension (k), then every nonempty class of
length-(B(k)) universal words contains a representative whose shortest
witness depth is nondecreasing with mask rank through depths (0,ldots,d-1).

#### Proof

Order words lexicographically by the cut signatures

\[
\left(
|\mathcal F_j|,
-\sum_{S\in\mathcal F_j}|S|
\right)_{j=0}^{d-1},
\tag{4.5}
\]

with earlier cuts compared first, and choose a maximal word.  If its first
non-rank-initial cut is (j), there are (S,T) as in (4.2).  CCE preserves
all earlier signatures and strictly decreases the rank sum at cut (j), a
contradiction.  Thus every cut is rank-initial.  (square)

The axiom is not a disguised count.  A concrete proposed exchange can be
tested by selecting one shortest witness for every target, swapping the two
chosen intervals, and applying Theorem 3.1.  Even if that witness system is
realizable, (4.3)--(4.4) additionally require *faithfulness*: the maximal
realization must not create collateral shorter witnesses.  This faithfulness
condition is exactly where equality in the scalar rank count currently
stops.

## 5. The independent central-straightening axiom

Rank normalization does not make the middle witnesses all have one length.
For the offsets in (2.3), define

\[
\Gamma(\mathcal I_r)
=\sum_{i=1}^{W}\bigl(\alpha_i+d-\beta_i\bigr).
\tag{5.1}
\]

Then (Gamma\ge0), and (Gamma=0) exactly when the middle witness family
is the flat row

\[
I_i=[i,i+d],qquad 1\le i\le W.
\]

The missing central statement can therefore be isolated as follows.

### Axiom CSE (central-straightening exchange)

Whenever a length-(B(k)) universal word has (Gamma>0) for a selected
ordered system of middle witnesses, there is a realizable full witness
retiming at the same length with strictly smaller (Gamma), without
destroying universality.

Finite descent under CSE produces a representative with (D^dA) equal to a
permutation of the middle layer.  CSE and CCE solve different problems:
CSE straightens physical witness intervals, while CCE sorts incomparable
Boolean labels among the short-depth cuts.  Their bare conjunction is not
yet a simultaneous normalization theorem, because a later CCE move could
destroy the flat middle row.  One needs either CCE **relative to a fixed
flat middle witness system**, or the lexicographic coupled form in which a
CSE move never worsens the earlier rank-cut signature.  This preservation
clause is part of the genuine missing exchange statement, not bookkeeping.

Theorem 3.1 is an exact accept/reject criterion for any proposed CSE move as
well.  What is not known is why a decreasing move must always exist.

## 6. A rigorous local obstruction

Consider the dimension-four word

\[
A=(10,9,5,1,2,4,8),
\tag{6.1}
\]

with masks written in binary-decimal notation.  Its length-one values are

\[
10,9,5,1,2,4,8,
\]

its length-two values are

\[
11,13,5,3,6,12,
\]

and its length-three values include

\[
15,13,7,7,14.
\]

Together these are all fifteen nonzero four-bit masks.  Since (B(4)=7),
this is an optimal word.

However,

\[
DA=(11,13,5,3,6,12)
\]

is not the middle layer.  More strongly, no change to one nonzero entry can
make (DA) a permutation of the six two-sets.  The two rank-three unions

\[
10\cup9=11,qquad9\cup5=13
\]

can both be affected by one change only by replacing the middle entry (9).
If it is replaced by (X\ne0), requiring both (10\cup X) and (X\cup5)
to have rank two forces

\[
X\subseteq10,qquad X\subseteq5.
\]

The masks (10) and (5) are disjoint, so this forces (X=0), forbidden.

Thus arbitrary optimal representatives are not centrally flat, and even the
smallest case may require a coupled multi-entry retiming.  A normalization
proof cannot be a generic one-cell sorting argument.

## 7. Final separation

The exact logical state is

\[
\boxed{
\begin{array}{c}
\nu(k)=B(k)\\[1mm]
\Downarrow\\[-1mm]
\text{banded orthogonal double-chain skeleton + exact pin survival}
\end{array}}
\]

while the observed canonical form additionally needs

\[
\boxed{
\text{CSE (straighten the middle witness paths)}
\quad+\quad
\text{CCE (compress the shortest-depth cuts by rank)}
\quad+\quad
\text{mutual preservation}.
}
\]

Theorem 3.1 makes both axioms falsifiable cell by cell.  It also identifies
the smallest plausible route to a proof: find a class of witness swaps for
which the interval-order gates (3.7), the pin conditions (3.3)--(3.4), and
the first-witness faithfulness condition are invariant.  Pure rank slack
contains no mechanism enforcing those invariants.
