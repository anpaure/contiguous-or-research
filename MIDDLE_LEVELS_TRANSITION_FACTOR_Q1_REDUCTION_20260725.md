# A fixed-arity middle-levels gate for a physical two-sided first band

Date: 2026-07-25

## 0. Outcome

Put (n=2m+1).  The one-sided pair-omission construction can be made
two-sided at depth one if, in each omitted-pair universe of size
(2m-1), one can choose a particular balanced transition factor of the
middle-levels graph.  This note gives the exact equivalence and the exact
global loss ledger.

The local object has fixed arity.  If (Q) has size (2r+1), a transition
is a length-two path

\[
S-C-S'
\]

in the middle-levels graph, where (|S|=|S'|=r), (|C|=r+1), and
(C=S\cup S').  It has two colours

\[
L=Q\setminus C\in {Q\choose r},\qquad
T=S\cap S'\in {Q\choose r-1}.
\]

A 2-factor of the middle-levels graph uses every (S)-vertex and every
(C)-vertex once.  Consequently its (L)-colours are automatically a
permutation of ({Q\choose r}).  The only colour condition is that the
(T)-loads be the arithmetically optimal values (1) and (2).

For the constant-one application one also needs the projected cycles to
have few category boundaries and few cuts hitting short coordinate
residence intervals.  The colour condition and the residence condition
are logically separate.

## 1. Exact local correspondence

Let

\[
Q\quad\text{have size }2r+1,qquad
A={2r+1\choose r},\qquad B={2r+1\choose r-1}.
\]

Let (mathsf{ML}(Q,r)) be the bipartite inclusion graph between the
(r)-sets and the ((r+1))-sets of (Q).  Consider a 2-factor
(mathcal D) of this graph.  Orient each component and write it as

\[
\cdots,S_i,C_i,S_{i+1},C_{i+1},\cdots,
\qquad C_i=S_i\cup S_{i+1}.
\tag{1.1}
\]

Define

\[
L_i=Q\setminus C_i,qquad T_i=S_i\cap S_{i+1},qquad
X_i=Q\setminus S_i.
\tag{1.2}
\]

### Theorem 1.1 (transition-factor dictionary)

The following hold exactly.

1.  The (L_i)'s run through every member of ({Q\choose r}) exactly
    once.
2.  The (X_i)'s run through every member of ({Q\choose r+1}) exactly
    once.
3.  Consecutive (X)-states are Johnson adjacent and

    \[
    X_i\cap X_{i+1}=L_i,
    \qquad
    X_i\cup X_{i+1}=Q\setminus T_i.
    \tag{1.3}
    \]
4.  The mean (T)-load is

    \[
    {A\over B}={r+2\over r}=1+{2\over r}.
    \tag{1.4}
    \]
    Hence the balanced integral (T)-profile is (1) on
    (B-(A-B)) targets and (2) on (A-B) targets, where

    \[
    A-B={2A\over r+2}.
    \tag{1.5}
    \]

#### Proof

Every ((r+1))-vertex (C) has degree two in the 2-factor and occurs
between exactly one consecutive pair (S_i,S_{i+1}).  Complementation
therefore makes (C_i\mapsto L_i) a bijection.  The same argument at the
(r)-vertices makes (S_i\mapsto X_i) a bijection.  Finally,

\[
(Q\setminus S_i)\cap(Q\setminus S_{i+1})
=Q\setminus(S_i\cup S_{i+1})=L_i
\]

and the union identity is its dual.  The binomial ratio in (1.4) is
immediate.  \(\square\)

Thus a balanced transition factor is already a two-sided-rainbow first
band, with only the forced (A-B=O(A/r)) repetitions on the larger-side
colour ledger.

## 2. Fixed-arity hypergraph formulation

The transition-factor problem is a fixed-uniformity integral problem.
Make four types of vertices:

* a source copy of every (r)-set (S);
* a target copy of every (r)-set (S');
* every (r)-set (L), as a mandatory colour;
* quota clones of every ((r-1))-set (T), one mandatory clone and one
  optional clone on exactly (A-B) targets.

For every directed Johnson transition

\[
S'=S-x+y,qquad x\in S,quad y\in Q\setminus S,
\]

put

\[
T=S-x,qquad L=Q\setminus(S\cup\{y\}),
\tag{2.1}
\]

and create the 4-edge

\[
(S_{\rm src},S'_{\rm tgt},L,T^{(a)}).
\tag{2.2}
\]

A perfect matching of this four-partite hypergraph is exactly a directed
cycle cover on the (r)-sets, with every (L)-colour once and the chosen
balanced (T)-quota.  Conversely every balanced transition factor gives
such a perfect matching after orienting its projected cycles.

This removes growing-depth uniformity from the first-band colour gate.
The remaining issue is not fractional feasibility: the uniform fractional
point exists by coordinate symmetry.  The issue is an integral perfect or
sufficiently accurate near-perfect matching, followed by quantitative
control of the coordinate residence of its projected cycles.

## 3. Equivalent two-matching description

There is a second exact description which is sometimes more useful.
The middle-levels inclusion graph is ((r+1))-regular and bipartite.
Therefore it has a 1-factorization.  The union of any two distinct perfect
matchings is a 2-factor.

At a fixed ((r+1))-set (C), the two selected matching edges delete two
distinct elements (a,b\in C).  The transition colour is

\[
T=C\setminus\{a,b\}.
\tag{3.1}
\]

Thus the local gate is equivalently:

> choose a degree-two spanning subgraph of the middle-levels graph so
> that the codimension-two labels (3.1) have loads (1) or (2).

The uniform fractional solution is especially transparent.  At every
(C), choose each pair ({a,b}\subset C) with probability
(1/{r+1\choose2}).  Every (r)-set has expected degree two, and every
((r-1))-set has expected load

\[
{ {r+2\choose2}\over {r+1\choose2}}={r+2\over r}.
\tag{3.2}
\]

The missing content is the simultaneous integral rounding with the
degree-two constraints kept exact.

## 4. Global pair-category extraction

Return to (n=2m+1), put (r=m-1), and partition (2m) coordinates
into ordered pairs

\[
P_1,\ldots,P_m
\]

with one leftover coordinate.  Put (Q_j=[n]\setminus P_j).  For a
rank-((m-1)) set (L), let

\[
\kappa(L)=\min\{j:L\cap P_j=\varnothing\}.
\tag{4.1}
\]

Assume that for every (j\le t) we have a balanced transition factor
(mathcal D_j) on (Q_j).  Retain the directed transitions whose lower
colour (L_i) satisfies (kappa(L_i)=j).

### Proposition 4.1 (exact two-sided loss ledger)

Before residence cuts, the retained transitions have these properties.

1. Every global rank-((m-1)) target of category at most (t) occurs
   exactly once as a lower colour.
2. All designated middle owners are distinct.
3. Upper colours belonging to different phases are distinct.
4. Inside one phase, deleting at most

   \[
   A-B={2A\over m+1}
   \tag{4.2}
   \]

   transitions makes all upper colours distinct.

#### Proof

The (L)-colours of (mathcal D_j) enumerate all rank-((m-1)) subsets
of (Q_j), so category assignment gives exact lower ownership.  The
designated owner (X_i) contains (L_i) and is contained in (Q_j);
hence it has the same category (j).  The same is true of the upper
colour (Q_j\setminus T_i), because it contains (L_i).  This proves
cross-phase disjointness for owners and upper colours.

Balanced (T)-loads are at most two.  Restricting to a category cannot
increase any load.  The total duplicate excess in the unrestricted local
factor is exactly (A-B), proving (4.2).  \(\square\)

As in the first-avoided-pair argument, the category tail satisfies

\[
N_j\le C\sqrt m\,A(3/4)^{j-1}.
\tag{4.3}
\]

Taking (t=\lceil20\log m\rceil), the total colour deletion plus the
unprocessed category tail is therefore

\[
O\left({A\log m\over m}\right)=o(W/\sqrt m).
\tag{4.4}
\]

Thus the two-sided colour ledger is already strong enough for a Gaussian
window.  Only path fragmentation and short coordinate residence remain.

## 5. Exact residence ledger

Along an oriented projected cycle (X_0,X_1,\ldots), call a coordinate
residence interval short when its cyclic length is at most (H).  Let
(	au_H(mathcal D_j)) be the minimum number of cycle edges meeting all
short residence intervals.  Cutting those edges makes every remaining
piece a genuine radius-(H) rotor path.

Category restriction also cuts a projected cycle.  Let
(sigma_j) be the number of maximal intervals on which
(kappa(L_i)=j).  After the upper-colour deletions of Proposition 4.1,
the total number of physical runs is at most

\[
J\le
\sum_{j\le t}\left(sigma_j+\tau_H(mathcal D_j)+{2A\over m+1}ight)
+O\bigl(\text{category tail}\bigr).
\tag{5.1}
\]

There is a useful unconditional bound on category fragmentation after a
coordinate relabelling.  The lower-colour sequence (L_i) is itself a
Johnson cycle.  Across all its (A) transitions, the total number of
coordinate flips is (2A).  For phase (j), relabel the (2(j-1))
earlier-pair coordinates onto coordinates of smallest flip count.  Then

\[
\boxed{\sigma_j=O(jA/m).}
\tag{5.2}
\]

Indeed, the selected coordinates have total flip count at most their
proportional share (O(jA/m)), and the truth of each earlier-pair
constraint changes only at one of those flips.

Summing (5.2) through (t=O(\log m)) gives

\[
\sum_{j\le t}\sigma_j=O(A\log^2m/m)=o(W/\sqrt m).
\tag{5.3}

We have therefore isolated the sole remaining local quantitative term:

\[
\boxed{
\sum_{j\le 20\log m}\tau_H(\mathcal D_j)=o(W/H),
\qquad H=O(\sqrt m).
}
\tag{RT}

## 6. Precise sufficient theorem

### Theorem 6.1 (balanced transition factors plus residence imply a
physical two-sided first band)

Suppose that, for (r=m-1), there are balanced transition factors
(mathcal D_j) on the omitted-pair universes (Q_j), (j\le20\log m),
which after relabelling satisfy (RT).  Then there is a literal physical
radius-(H) path system with

\[
W-o(W/H)
\]

distinct designated middle owners, whose lower first colours and upper
first colours each miss only (o(W/H)) targets, and whose total reset
cost is (o(W)).

#### Proof

Use Proposition 4.1, delete one copy of each repeated upper colour, and
discard the category tail.  Equations (4.4), (5.1), and (5.3), together
with (RT), show that both the released-owner count and the run count are
(o(W/H)).  Cutting at every run boundary and every short-residence
hitting edge gives genuine radius-(H) rotor paths.  Their initialization
cost is (O(HJ)=o(W)).  \(\square\)

The theorem does not prove constant one: balanced transition factors with
(RT) have not yet been constructed.  It does, however, replace the
phase-one clustered shadow obstruction by a fixed-arity integral
transition problem, and it proves that category fragmentation is not an
additional obstruction.  The only remaining physical statistic is the
short-residence hitting number.

## 7. Correction: cycle count belongs in the residence ledger

Let \(c_j\) denote the number of cycles of \(\mathcal D_j\).  Equations
(5.2), (5.3), and (RT) above must be read with the following correction:

\[
\sigma_j\le c_j+O(jA/m),
\tag{7.1}
\]

\[
\sum_{j\le t}(\sigma_j-c_j)
=O(A\log^2m/m)=o(W/\sqrt m),
\tag{7.2}
\]

and the required residence condition is

\[
\boxed{
\sum_{j\le20\log m}
\bigl(c_j+\tau_H(\mathcal D_j)\bigr)=o(W/H).
}
\tag{7.3}
\]

Indeed, even when a category predicate never changes, it contributes one
selected interval on each cycle.  The flip-count argument bounds only the
additional fragmentation beyond this unavoidable cycle count.  With
(7.3) substituted for (RT), Theorem 6.1 is unchanged and correct.

## 8. PBBS solves the local colour factor unconditionally

The balanced \(1/2\) hypothesis on the \(T\)-loads is stronger than
needed.  The PBBS step-two factor proved in
MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md supplies a completely
unconditional local transition factor with

\[
1\le\mu(T)\le3
\qquad(T\in{Q\choose r-1}).
\tag{8.1}
\]

Indeed, a PBBS odd-graph component
\[
\cdots,S_{i-1},S_i,S_{i+1},\cdots
\]
gives the middle-levels transition
\[
S_{i-1}-S_i^c-S_{i+1}.
\]
Its \(L\)-colour is \(S_i\), hence the \(L\)'s are a permutation, and
its \(T\)-colour is the PBBS angle
\[
T=S_{i-1}\cap S_{i+1}.
\]
The PBBS complete-shadow theorem is exactly (8.1).

Because there are \(A\) occurrences and all \(B\) targets occur, the
total duplicate excess is exactly
\[
\sum_T(\mu(T)-1)=A-B={2A\over r+2}.
\tag{8.2}
\]
Thus Proposition 4.1 and its \(O(A/m)\) colour-deletion ledger hold
without an unproved integral matching theorem.  Moreover PBBS has at most
\[
{2A\over2r+1}=O(A/r)
\tag{8.3}
\]
projected step-two cycles.

Consequently the only unproved term in the two-sided physical first-band
construction is PBBS residence.  Let \(\tau_H(P_r)\) be the minimum edge
hitting number for the short coordinate-residence intervals in the PBBS
step-two cycles.  Since \(t=\Theta(\log m)\) pair categories suffice, the
explicit sufficient bound is
\[
\boxed{
\tau_H(P_{m-1})=o\!\left({A\over H\log m}\right),
\qquad H=O(\sqrt m).
}
\tag{8.4}
\]
A Catalan-scale estimate \(\tau_H(P_{m-1})=O(A/m)\) is more than enough.

The PBBS omitted-label gap identity makes (8.4) concrete, with one necessary
projection shift.  The physical projected owners are \(X_i=Q\setminus S_i\),
so their step-two recurrence is
\[
X_{i+2}=X_i-\{\lambda_i\}+\{\lambda_{i+1}\}.
\]
If consecutive occurrences of a label have odd gap \(g=2s+1\), that label
is inserted at the projected transition immediately preceding the first
occurrence and removed at the transition indexed by the second occurrence.
Its positive projected residence is therefore \(s+1=(g+1)/2\), not \(s\).
Consequently \(\tau_H(P_r)\) is the transversal number of the circular
parity intervals arising from label gaps
\[
3\le g\le2H-1.
\tag{8.5}
\]
In particular there is no projected residence-one obstruction.  The proved
depth-two theorem controls the \(g=3\), projected-residence-two intervals at
\(O(A/r)\), but no Gaussian-window bound for the full family (8.5) is
currently proved.

Thus the sharp residual in this lane is no longer colour integrality:
it is the explicit PBBS short-gap stabbing estimate (8.4).
