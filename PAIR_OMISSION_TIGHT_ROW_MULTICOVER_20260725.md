# Pair-omission tight rows: an exact physical multicover and its colouring gate

Date: 2026-07-25

## 0. Outcome

Put

\[
n=2m+1,\qquad V_-={ [n]\choose m-1},\qquad
V_0={ [n]\choose m}.
\]

For every coordinate pair (P\in{[n]\choose2}), the remaining universe

\[
Q_P=[n]\setminus P
\]

has size (2m-1=2(m-1)+1).  An exact central wreath factor on (Q_P)
therefore partitions all ((m-1))-subsets of (Q_P) into cyclic rows of
length (2m-1).  Every such row simultaneously has the following exact
properties.

* Its consecutive unions are (2m-1) distinct (m)-sets.
* It is a genuine tight Johnson cycle, with present residence (m) and
  absent residence (m-1).
* For every (H\le m-1), cutting it once gives one literal radius-(H)
  rotor run.  Its lower and upper depth-(q) flags are actual cyclic
  intervals of lengths (m-q) and (m+q).

Taking one exact local factor for every pair (P) gives a finite integral
multicover whose first two rank degrees are exactly

\[
D_-={m+2\choose2},\qquad D_0={m+1\choose2}.
\]

Thus a matching of local rows which covers every lower target once covers
the same number of distinct middle owners.  It would leave only

\[
|V_0|-|V_-|={2W\over m+2}=O(W/m)
\]

middle owners, which is already below the permitted Gaussian-window
release budget.

Equivalently, if the row hypergraph admitted a proper edge-colouring with
(D_-) colours, each colour would be exactly the required tight
depth-one core.  The construction therefore absorbs long residence into
the edge definition rather than imposing it later as a growing conflict.

There is a direct one-sided q1 extraction which avoids this edge-colouring
gate.  Partition (2m) coordinates into ordered pairs and assign each
lower target to the first pair it avoids.  Taking precisely the
corresponding starts in the local factor gives every lower target once,
gives (N_1) distinct middle owners, and splits into only

\[
O\!\left({W\log ^2m\over m}\right)=o(W/H)
\]

tight runs for (H=O(\sqrt m)).  This is proved in Section 5.  What is
still not automatic is simultaneous two-sided multidepth coverage: the
deeper cyclic intervals of the selected rows need not have balanced loads.
The exact equitable-colouring formulation of that stronger gate is also
given below.

## 1. One local row is a full tight flag run

Fix (P), abbreviate (Q=Q_P), and let

\[
\pi=(x_0,x_1,\ldots,x_{2m-2})
\]

be one cyclic order in an exact middle wreath factor of (B_Q).  Put

\[
S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\tag{1.1}
\]

### Theorem 1.1 (tight pair-omission row)

The following assertions hold, with indices modulo (2m-1).

1. The (S_i)'s are distinct and

   \[
   X_i=S_i\cup S_{i+1}.
   \tag{1.2}
   \]

2. The (X_i)'s are distinct.  As all rows of the local exact factor are
   taken, their (X_i)'s partition ({Q\choose m}).

3. The owner cycle (X_0X_1\cdots X_{2m-2}X_0) has coordinate
   membership residence exactly (m) and nonmembership residence exactly
   (m-1).

4. For every (0\le q\le m-1),

   \[
   \boxed{
   \bigcap_{j=0}^{q}X_{i+j}=I_\pi(i+q,m-q),
   \qquad
   \bigcup_{j=0}^{q}X_{i+j}=I_\pi(i,m+q).
   }
   \tag{1.3}
   \]

5. For every (H\le m-1), one cut of the row gives one genuine
   radius-(H) MTF/rotor run carrying all flags in (1.3).

#### Proof

The first identity is the union of two consecutive length-((m-1))
windows.  Distinctness of all proper cyclic windows is immediate in a
cyclic order of distinct coordinates.

In a universe of size (2m-1), complementation bijects length-(m)
windows with length-((m-1)) windows, up to a cyclic shift.  Since the
local factor partitions all length-((m-1)) targets, it also partitions
all length-(m) targets.

Each coordinate lies in exactly (m) consecutive owner windows and is
absent from the other (m-1).  Finally, intersecting (q+1) consecutive
length-(m) windows removes their first (q) departing coordinates;
uniting them adds their last (q) entering coordinates.  This proves
(1.3).  The residence lengths are larger than (H), so the standard
rotor update applies at every uncut edge.  \(\square\)

The row contributes exactly one target at every start and every signed
depth.  Its literal initialization cost is (2H+1), followed by one
update per later owner.  Thus (J) selected rows carrying (M) distinct
middle owners have exact word cost

\[
M+(2H+1)J+O(1).
\tag{1.4}
\]

Since every row has (2m-1) owners, a lower-perfect row matching would
have

\[
J={N_1\over2m-1}+O(1)=O(W/m)=o(W/H)
\]

for every fixed Gaussian window (H=O(\sqrt m)).

## 2. Exact first-band degree ledger

Fix one exact local factor (F_P) for every (P).  Let \(\mathcal R\)
be the hypergraph whose vertices are (V_-\sqcup V_0), and whose edges
are the row target sets

\[
R(\pi)=\{S_i:i\in\mathbb Z_{2m-1}\}
       \sqcup\{X_i:i\in\mathbb Z_{2m-1}\}.
\tag{2.1}
\]

### Proposition 2.1 (biregular row multicover)

Every (S\in V_-) has row degree

\[
\boxed{D_-={m+2\choose2},}
\tag{2.2}
\]

and every (X\in V_0) has row degree

\[
\boxed{D_0={m+1\choose2}.}
\tag{2.3}
\]

Every fixed-(P) row family is already a matching on both vertex parts.

#### Proof

A lower target (S) occurs in the unique row of (F_P) containing it
exactly when (P\subseteq[n]\setminus S).  Its complement has size
(m+2), proving (2.2).  The length-(m) windows of (F_P) partition
({Q_P\choose m}), so the same argument for a middle target, whose
complement has size (m+1), proves (2.3).  The partition assertion in
each part follows from Theorem 1.1.  \(\square\)

The incidence identity

\[
|V_-|D_-=|V_0|D_0
\tag{2.4}
\]

is equivalent to

\[
{2m+1\choose m-1}{m+2\choose2}
={2m+1\choose m}{m+1\choose2}.
\]

### Corollary 2.2 (class-one colouring would solve the tight q1 gate)

If \(\mathcal R\) has a proper edge-colouring with (D_-) colours, then
every colour class covers every lower target exactly once and uses
exactly (N_1) distinct middle owners.  Its rows are pairwise disjoint and
form a tight radius-(H) rotor core for every (H\le m-1).

#### Proof

At a lower vertex the (D_-) incident rows have distinct colours, so each
colour occurs exactly once.  Properness at a middle vertex gives
at most one occurrence.  Both sides of a row have the same size, hence a
colour contains (N_1) middle occurrences and all are distinct.  Apply
Theorem 1.1 row by row.  \(\square\)

There is a harmless divisibility caveat: (2m-1) need not divide (N_1).
Accordingly an exact lower-perfect matching by whole rows can fail for
arithmetic reasons.  Covering all but (O(m)) lower targets is enough for
the asymptotic application, and one may also cut (O(1)) rows into tight
segments to repair the residue.

More generally, if

\[
\chi'(\mathcal R)\le D_-+s,
\]

then a largest colour class covers at least

\[
N_1{D_-\over D_-+s}
\]

lower targets and the same number of distinct middle owners.  Therefore

\[
\boxed{s=o(D_-/H)}
\tag{2.5}

is sufficient for the required (o(W/H)) released-owner count.

## 3. Exact codegrees in the symmetric orbit multicover

For clean codegree formulae, replace each (F_P) by the multiset of all
its coordinate relabellings on (Q_P).  This only multiplies all degrees
by the same orbit multiplicity (M); it does not solve the one-colour
resolution.  It makes the multihypergraph invariant under every coordinate
permutation.

Let two lower targets have Johnson distance (d):

\[
|S\setminus T|=|T\setminus S|=d,
\qquad1\le d\le m-1.
\]

### Proposition 3.1 (lower/lower relative codegree)

In the symmetric orbit multicover,

\[
\boxed{
{\deg(S,T)\over\deg(S)}
=
{{m+2-d\choose2}\over {m+2\choose2}}
{2\over {m-1\choose d}{m\choose d}}.
}
\tag{3.1}
\]

The maximum is attained at (d=1) and is (O(m^{-2})).

#### Proof

The omitted pair must avoid (S\cup T), whose complement has size
(m+2-d), giving the first ratio.  Condition on one local row containing
(S).  In a cyclic row of length (2m-1), exactly two other
length-((m-1)) windows are at Johnson distance (d) from (S), one in
each cyclic direction.  The stabilizer of (S) is transitive on the

\[
{m-1\choose d}{m\choose d}
\]

local targets at that distance.  This gives the second ratio.  \(\square\)

For middle targets at Johnson distance (d), complementation inside
(Q_P) gives similarly

\[
\boxed{
{\deg(X,Y)\over\deg(X)}
=
{{m+1-d\choose2}\over {m+1\choose2}}
{2\over {m\choose d}{m-1\choose d}},
}
\tag{3.2}

again (O(m^{-2})).

Cross-part codegree is larger.  If (S\subset X), then a local cyclic row
containing (S) has exactly two adjacent length-(m) windows containing
it.  There are (m) local (m)-supersets of (S).  Hence

\[
\boxed{
{\deg(S,X)\over\deg(S)}
=
{{m+1\choose2}\over {m+2\choose2}}{2\over m}
=O(m^{-1}).
}
\tag{3.3}

The (m^{-1}) scale is unavoidable for full rows; it is the incidence
of adjacent lower/middle windows, not accidental clustering.

For an arbitrary fixed-(P) choice (without orbit symmetrization), the
following exact pair-incidence budget is still available.  At any target
vertex (v), within either one fixed rank part,

\[
\boxed{
\sum_{w\ne v}\deg(v,w)=(2m-2)\deg(v).
}
\tag{3.4}

Thus only ((2m-2)\deg(v)/t) partners can have codegree at least (t).
This allows high-codegree pairs to be pruned locally, although it does not
by itself give the sharp edge-colouring (2.5).

## 4. Every selected colour is genuinely multidepth physical

There is no further factorability condition after a row matching is found.
If \(\mathcal M\) is any matching of local rows, then for each signed depth
(q\le H) its lower and upper target loads are

\[
\mu^-_q(T)
=\#\{R\in\mathcal M:T=I_\pi(i,m-q)\text{ in }R\},
\tag{4.1}
\]

\[
\mu^+_q(T)
=\#\{R\in\mathcal M:T=I_\pi(i,m+q)\text{ in }R\}.
\tag{4.2}

The same owner order realizes all these occurrences literally, by (1.3).
The number of rows is (O(W/m)), so their total initialization cost is

\[
O(HW/m)=o(W)
\]

on a fixed Gaussian window.

What remains is coverage rather than chronology.  A selected q1-perfect
colour need not cover deeper targets.  Across all pair-indexed factors the
average degree of a rank-((m-q)) target is exactly

\[
\boxed{
\overline D_q
={n\choose2}{2m-1\choose m-1}\bigg/{n\choose m-q}
=D_-{N_1\over N_q}.
}
\tag{4.3}

The identity is the double count

\[
{n\choose2}{n-2\choose m-1}
={n\choose m-1}{m+2\choose2}.
\]

Thus an equitable colouring into (D_-) colours would give exactly the
core mean (N_1/N_q) at every depth.  This motivates the exact remaining
statement.

> **Multidepth pair-row colouring lemma (open).**  Choose the local exact
> factors (F_P) and colour their rows with (D_-+o(D_-/H)) colours so
> that:
>
> 1. every colour is a matching on (V_-\sqcup V_0);
> 2. at every signed depth (q\le H), the colour-degrees of every target
>    differ by at most one, apart from (o(W/H)) released occurrences.

One colour would then be a genuine tight rotor core of
(N_1-o(W/H)) owners whose entire Gaussian-window load is balanced up to
the permitted release.  The omitted (O(W/m)+o(W/H)) owners can be given
arbitrary flags, with total weighted spill (o(W)).

The lemma is stronger than ordinary row edge-colouring.  Equations
(3.1)--(3.3) show precisely why: same-rank row collisions are at the
(m^{-2}) scale, but adjacent lower/middle incidence has unavoidable
(m^{-1}) codegree, and all (2H+1) rank capacities must be controlled by
one colour.  Conversely, once that colouring is obtained, Theorem 1.1
proves that there is no residual run, pin, or literal-factorization gate.

## 5. Explicit first-avoided-pair extraction

The ordinary one-sided q1 row matching can be constructed directly,
without proving the class-one colouring conjecture of Section 2.

Partition (2m) coordinates into ordered disjoint pairs

\[
P_1,P_2,\ldots,P_m
\]

and leave one coordinate (z) unpaired.  For a set (A\subseteq[n]), put

\[
\kappa(A)=\min\{j:A\cap P_j=\varnothing\},
\tag{5.1}
\]

when the set is nonempty.  Every ((m-1))-set has finite category: a set
meeting all (m) pairs has at least (m) elements.

For every (j), choose an arbitrary exact central wreath factor (F_j)
on (Q_j=[n]\setminus P_j).  In a row of (F_j), retain exactly the
starts (i) for which

\[
S_i=I_\pi(i,m-1),\qquad \kappa(S_i)=j.
\tag{5.2}
\]

Associate this lower target with the same-start length-(m) window

\[
X_i=I_\pi(i,m).
\tag{5.3}
\]

Then

\[
X_i\cap X_{i-1}=S_i.
\tag{5.4}
\]

Break the retained starts in each cyclic row into maximal consecutive
intervals, and traverse the corresponding (X_i)'s in decreasing cyclic
order.  Thus (S_i) is the outgoing lower colour of its designated owner
(X_i), including at a terminal end where the next canonical state is used
only as a collar and is not itself selected.

### Theorem 5.1 (tight q1 saturating path forest)

The extracted paths have all of the following properties.

1. Every rank-((m-1)) target occurs exactly once as an outgoing lower
   colour.
2. Their (N_1={n\choose m-1}) middle owners are all distinct.
3. Every component is a genuine tight coordinate-window rotor path and
   therefore carries literal radius-(H) flags for every (H\le m-1).
4. The number (J) of path components satisfies

   \[
   \boxed{
   J=O\!\left({N_1\log ^2m\over m}\right).
   }
   \tag{5.5}
   \]

Consequently, uniformly for

\[
H=o\!\left({m\over\log ^2m}\right),
\]

\[
J=o(W/H),\qquad 2HJ=o(W).
\tag{5.6}

#### Proof: exact coverage and distinct owners

Fix a lower target (S), and let (j=\kappa(S)).  Then (S\subseteq Q_j)
and occurs in exactly one row and one position of (F_j); it is selected
there by (5.2).  This proves exact lower coverage.

The local factor's length-(m) windows are all distinct.  Moreover
(S_i\subset X_i), so (X_i) meets every earlier pair (P_h), (h<j),
which (S_i) meets, while (X_i\subseteq Q_j).  Hence

\[
\kappa(X_i)=j.
\tag{5.7}
\]

Owners selected in different phases have different categories, and owners
inside one (F_j) are distinct by Theorem 1.1.  Thus all selected owners
are distinct.  Equation (5.4) proves the lower-colour assertion.  Reverse
orientation of a cyclic-window row is again tight.  The canonical states
just outside a maximal selected interval serve only as initialization/end
collars, so Theorem 1.1 proves tight physicality without adding an owner.

#### Proof: component count

Put

\[
L=2m-1,\qquad
A_m={2m-1\choose m-1},\qquad
R_m={A_m\over L}.
\tag{5.8}
\]

There are (R_m) rows in each local factor.  In one cyclic row of (F_j),
selection means that the length-((m-1)) window meets every pair
(P_h), (h<j).  For one fixed pair, the start positions at which the
window avoids both coordinates are the intersection of two circular arcs,
and hence have at most two circular components.  The union of the bad-start
sets for (h<j) has at most (2(j-1)) components.  Its complement, the
selected starts, has at most (2j) components.  If (N_j) is the number
of category-(j) lower targets, then

\[
J_j\le\min\{N_j,2jR_m\}.
\tag{5.9}

It remains to control the tail of (N_j).  Choose a uniform
((m-1))-subset of (Q_j).  Equivalently, let every coordinate of (Q_j)
be independently present with probability

\[
p={m-1\over2m-1}
\]

and condition on total size (m-1).  Before conditioning, the events of
meeting the disjoint pairs (P_1,\ldots,P_{j-1}) are independent and each
has probability

\[
1-(1-p)^2
=1-\left({m\over2m-1}\right)^2< {3\over4}.
\]

The central binomial point probability satisfies

\[
\Pr(\operatorname{Bin}(2m-1,p)=m-1)\ge c m^{-1/2}
\]

for an absolute (c>0).  Therefore

\[
\boxed{
N_j\le C\sqrt m\,A_m(3/4)^{j-1}
}
\tag{5.10}

for an absolute (C).

Take (t=\lceil20\log m\rceil).  Equations (5.9)--(5.10) give

\[
\begin{aligned}
J
&\le\sum_{j\le t}2jR_m+\sum_{j>t}N_j\\
&=O(R_m\log ^2m)+O(A_m m^{-2})\\
&=O\!\left({A_m\log ^2m\over m}\right).
\end{aligned}
\tag{5.11}

Finally (A_m=\Theta(N_1)) and (N_1=\Theta(W)).  Equation (5.5) gives

\[
{HJ\over W}=O\!\left({H\log ^2m\over m}\right)=o(1)
\]

throughout the displayed range of (H), proving (5.5)--(5.6).
\(\square\)

### Corollary 5.2 (literal one-sided first-band core)

For (H=o(m/\log ^2m)), one literal nonzero word of length

\[
N_1+o(W)=W-O(W/m)+o(W)
\]

has (N_1) distinct middle endpoints and represents every rank-((m-1))
target at those endpoints.  At the same endpoints it also represents the
canonical cyclic lower and upper flags through depth (H), though those
deeper load vectors are not asserted to cover their full ranks.

This is the promised positive long-residence refinement at depth one.  It
simultaneously achieves exact lower rainbowness, distinct middle ownership,
and (o(W/H)) physical runs.  The remaining constant-one issue in this
pair-omission lane is purely the multidepth distribution of the already
literal flags, not q1 synchronization or reset cost.

## 6. Two-sided q1 colour completion via PBBS; residence is the residual

There is a different local factor which closes the two-sided colour ledger
but does not yet close residence.  On \(Q_j\), use the proved PBBS
odd-graph 2-factor.  A centered PBBS two-path

\[
S_{i-1}-S_i-S_{i+1}
\]

induces the middle-levels transition

\[
S_{i-1}-S_i^c-S_{i+1}.
\]

After complementing the projected \(S\)-states, its lower colour is
\(S_i\), exactly once, and its upper-colour complement is the PBBS angle
\(S_{i-1}\cap S_{i+1}\).  The proved PBBS complete-angle theorem gives

\[
1\le \mu(T)\le3
\]

for every local rank-\((m-2)\) target \(T\).  Hence all upper targets occur,
and deleting repeated occurrences costs exactly

\[
{2m-1\choose m-1}-{2m-1\choose m-2}
=O(A_m/m)
\]

per active pair phase.  The PBBS step-two factor has only \(O(A_m/m)\)
cycles.  After the same first-avoided-pair extraction through
\(O(\log m)\) phases, both signed q1 colour defects and all category/cycle
fragmentation are therefore

\[
O(A_m\log^2m/m)=o(W/H)
\qquad(H=O(\sqrt m)).
\]

The exact remaining term is physical residence.  Let
\(\tau_H(P_{m-1})\) be the minimum number of cuts meeting all PBBS
step-two coordinate residence intervals of length at most \(H\).  The
two-sided q1 core is physical with \(o(W)\) reset cost provided

\[
\tau_H(P_{m-1})=o\!\left({A_m\over H\log m}\right).
\]

The PBBS omitted-label gap formula identifies these intervals exactly, after
accounting for complementation in the middle-level transition.  If an
omitted label repeats at odd gap \(2s+1\), its positive residence in the
projected owner cycle is \(s+1\).  Thus the outstanding q1 physical gate is
the transversal number of PBBS label-gap intervals with
\(3\le g\le2H-1\).  There is no projected residence-one obstruction.  The
\(g=3\) family (projected residence two) is already known to have Catalan
size \(O(A_m/m)\); the full Gaussian-window transversal bound is not proved.

In particular this applies at the product-tail scale

\[
H=\sqrt m\,\omega(m),\qquad
\omega(m)\longrightarrow\infty,
\qquad
\omega(m)=o\!\left({\sqrt m\over\log ^2m}\right).
\]

Thus the first-shadow and physical-residence gates are closed even at the
growing depth required for coefficient one; only the distribution of the
forced deeper flags remains.
