# PBBS transition factors close the two-sided pair-omission colour ledger

Date: 2026-07-25

## 0. Outcome

Put

\[
n=2m+1,\qquad H=O(\sqrt m),\qquad W={n\choose m}.
\]

The first-avoided-pair construction can be made two-sided at depth one
with only

\[
O(W\log m/m)
\]

released colours and

\[
O(W\log ^2m/m)=o(W/H)
\]

Johnson path components.  The local input is not a conjectural balanced
wreath factor.  It is the canonical PBBS step-two transition factor, whose
first-angle theorem gives every required codimension-two colour between one
and three times.

This is an actual integral two-sided-rainbow forest theorem.  It does not
yet give the desired radius-(H) physical spine: PBBS transition cycles can
have short coordinate residence intervals.  The exact remaining statistic
is the number of cuts needed to hit those intervals.

## 1. The PBBS transition dictionary

Let (Q) have size (2r+1), and put

\[
A={2r+1\choose r},\qquad B={2r+1\choose {r-1}}.
\]

Let (f) be the canonical periodic-box-ball permutation on the (r)-sets of
(Q).  Consecutive iterates are disjoint.  For every center (Z), form the
step-two Johnson edge

\[
e_Z=\{f^{-1}(Z),f(Z)\}.
\tag{1.1}
\]

Write its endpoints as (S,S'), and define

\[
C=S\cup S',\qquad T=S\cap S',\qquad
L=Q\setminus C,qquad X=Q\setminus S.
\tag{1.2}
\]

### Theorem 1.1 (exact PBBS local ledger)

The edges (e_Z) form a spanning (2)-factor on the (r)-sets.  As (Z) runs
over all centers:

1. (C=Z^c) runs through every ((r+1))-set once;
2. (L) runs through every (r)-set once;
3. (X) runs through every ((r+1))-set once;
4. every ((r-1))-set (T) occurs between one and three times.

Consequently the duplicate excess in the (T)-ledger is exactly

\[
\sum_T(\mu(T)-1)=A-B={2A\over r+2}.
\tag{1.3}
\]

Moreover consecutive complemented states satisfy

\[
X_i\cap X_{i+1}=L_i,
\qquad
X_i\cup X_{i+1}=Q\setminus T_i.
\tag{1.4}
\]

#### Proof

The PBBS map is a permutation, so its step-two graph is a spanning
(2)-factor (one or two step-two cycles for each PBBS component).  The
centered-edge identity gives

\[
f^{-1}(Z)\cup f(Z)=Z^c,
\]

hence (C=Z^c), proving the first assertion.  Complementation gives the
second and third assertions.  The PBBS complete-shadow and
multiplicity-three theorem gives (1\le\mu(T)\le3).  Since there are (A)
occurrences and every one of the (B) targets occurs, (1.3) follows.
Finally (1.4) is De Morgan's law.  \(\square\)

The point of (1.3) is that floor/ceiling balance is unnecessary here.
Complete support already makes the number of deletions needed for an
injective colour subfamily equal to the arithmetically forced excess.

## 2. Global first-avoided-pair extraction

Return to (n=2m+1), partition (2m) coordinates into ordered disjoint
pairs

\[
P_1,\ldots,P_m
\]

and leave one coordinate unpaired.  Put

\[
Q_j=[n]\setminus P_j,
\qquad |Q_j|=2m-1,
\]

and, for a rank-((m-1)) set (L), define

\[
\kappa(L)=\min\{j:L\cap P_j=\varnothing\}.
\tag{2.1}
\]

On each (Q_j), take the PBBS transition factor of Theorem 1.1 with
(r=m-1).  Retain precisely the transitions whose lower colour satisfies
(\kappa(L)=j).

### Proposition 2.1 (exact cross-phase separation)

The retained transitions satisfy:

1. every processed lower target occurs exactly once;
2. all designated middle owners are distinct;
3. upper colours from different phases are distinct;
4. deleting at most

   \[
   A-B={2A\over m+1},
   \qquad A={2m-1\choose {m-1}},
   \tag{2.2}
   \]

   transitions in one phase makes its upper colours injective.

#### Proof

The (L)-colours in phase (j) enumerate all ((m-1))-sets of (Q_j), so the
first-avoided rule assigns every processed lower target once.  By (1.4),

\[
L_i\subset X_i\subset Q_j,
\qquad
L_i\subset Q_j\setminus T_i\subset Q_j.
\]

If (\kappa(L_i)=j), upward stability of the first-avoided rule therefore
gives category (j) to both the owner and the upper colour.  This proves
cross-phase disjointness.

Inside one phase, restriction to a category cannot increase any (T)-load.
Delete all but one retained occurrence of each repeated (T).  The number
deleted is at most the unrestricted duplicate excess (1.3), which is
(2.2).  Complementation transfers injectivity to the upper colours.
\(\square\)

## 3. Tail and component ledger

Let (N_j) be the number of lower targets of category (j).  The same
conditioned-binomial calculation as in the pair-omission construction gives

\[
N_j\le C\sqrt m\,A(3/4)^{j-1}.
\tag{3.1}
\]

Take

\[
t=\lceil20\log m\rceil.
\tag{3.2}
\]

The unprocessed category tail is (O(Am^{-2})).  The upper-colour deletion
over all processed phases is

\[
t(A-B)=O(A\log m/m)=o(W/H).
\tag{3.3}
\]

It remains to count the category intervals along PBBS transition cycles.
The lower-colour sequence on such a cycle is a Johnson cycle: adjacent
lower colours differ by one deletion and one insertion.  Across all local
cycles there are exactly (2A) coordinate flips.  Before embedding phase
(j), relabel the (2(j-1)) earlier-pair coordinates onto coordinates with
the smallest flip counts.  Their total flip count is

\[
O(jA/m).
\tag{3.4}
\]

The truth of the condition that every earlier pair is met changes only at
one of these flips.  PBBS has at most (O(A/m)) step-two cycles, so the
number (\sigma_j) of selected category intervals satisfies

\[
\sigma_j=O((j+1)A/m).
\tag{3.5}
\]

Deleting a transition raises the number of path components by at most one.
Equations (3.1)--(3.5) therefore prove:

### Theorem 3.1 (two-sided low-component q1 forest)

There is an integral Johnson path forest with

\[
N_1-o(W/H)
\]

distinct middle owners such that its lower colours and upper colours are
both injective and each misses only (o(W/H)) targets.  Its number of path
components is

\[
\boxed{
J=O(W\log ^2m/m)=o(W/H).}
\tag{3.6}
\]

#### Proof

Use the retained transitions of Proposition 2.1, discard the tail, and
delete repeated upper colours.  The owner and both colour ledgers follow
from Proposition 2.1 and (3.1)--(3.3).  Cutting every projected cycle at
the category boundaries and deleted transitions gives a linear forest.
Its component count is bounded by

\[
\sum_{j\le t}\sigma_j+t(A-B)+O(Am^{-2}),
\]

which is (3.6).  \(\square\)

By the facet-braid literalization theorem, Theorem 3.1 already gives a
literal two-sided first-band word with additive (o(W)) cost.  Its new
content is the stronger (o(W/H)) component ledger in a completely explicit
transition factor.

## 4. The exact remaining physical statistic

For an oriented PBBS transition cycle, a coordinate support is used when
that coordinate enters or leaves the current middle owner.  Let
(\tau_H(\mathcal D)) be the minimum number of cycle edges meeting every
coordinate residence or nonresidence interval of length at most (H).
After cutting those edges, every remaining path is an actual radius-(H)
tight/rotor path.

Thus Theorem 3.1 upgrades to the desired pair-omission physical spine if

\[
\sum_{j\le20\log m}\tau_H(\mathcal D_j)=o(W/H).
\tag{4.1}
\]

No such bound is proved here.  It is the sole missing assertion in this
PBBS realization: colour support, owner injectivity, category tail, upper
collision deletion, and the required component scale have all been proved
integrally.

The distinction is essential.  PBBS angle completeness controls the
depth-one colour ledger, but short repeated omitted labels control physical
residence.  The former does not by itself bound the latter.
