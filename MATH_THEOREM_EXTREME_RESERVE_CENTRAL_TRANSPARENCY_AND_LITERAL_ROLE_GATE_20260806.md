# The extreme witness reserve is transparent to the central ring host

## Status

The internal extreme-witness theorem selects `M=exp(o(q))` near-maximal
rings, one for every complement of size at most `h-1`.  Pairwise
owner/root disjointness alone did not show that this protected bank could
coexist with the remaining ring cover-down.

This note proves the strongest central-host statement available from that
construction.  The reserve can be selected so that

1. its rings are pairwise disjoint on both central shores; and
2. every unused owner and every unused root retains a
   `(1-O(1/q))` fraction of all incident near-maximal ring candidates.

The proof is a direct random-list argument using exact association-scheme
codegrees.  Thus the reserve is globally transparent to the **unconditioned
central ring hypergraph**.

There is an exact conditioning boundary.  Once a ring's cyclic filler
order, cut, occurrence tickets and terminal marker are fixed, a literal
masked companion role may have only one realization.  One collision can
then delete its whole fibre.  Central degree transparency therefore does
not imply literal masked-tree or common-cap transparency.  A prospective
filler-changing menu, or a joint selection before those coordinates are
frozen, is still required.

No computation or search is used.

## 1. The near-maximal ring hypergraphs

Put

\[
 n=2q-1,qquad s=q-h,qquad W=\binom nq.               \tag{1.1}
\]

For `u in {1,2}` put

\[
                         \ell_u=n-s-u=q+h-1-u.         \tag{1.2}
\]

A period-`ell_u` ring state consists of an `s`-set core, a `u`-set unused
bank, and an oriented cyclic order on the remaining `ell_u` moving
coordinates.  The number of states is

\[
 |\mathfrak R_u|
   =\binom ns\binom{n-s}{u}(\ell_u-1)!
   ={n!\over s!u!\ell_u}.                             \tag{1.3}
\]

Every state contains `ell_u` distinct rank-`q` owners and `ell_u`
distinct rank-`(q-1)` roots.  By transitivity, the exact number through a
fixed owner or fixed root is

\[
 D_u={|\mathfrak R_u|\ell_u\over W}
     =\boxed{{q!(q-1)!\over s!u!}}.                   \tag{1.4}
\]

Write `D=D_1`; then `D_2=D/2`.

## 2. Exact pair-codegree table

Fix an owner `O`.  For another owner `O'`, put

\[
                         d=|O-O'|.                     \tag{2.1}
\]

There are

\[
                         N_d^{OO}=\binom qd\binom{q-1}d              \tag{2.2}
\]

owners in relation `d`.  A period-`ell` ring through `O` contains exactly

\[
 a_d^{OO}=\begin{cases}
 2,&1\le d<h,\\
 \ell-2h+1,&d=h
 \end{cases}                                           \tag{2.3}
\]

other owners in that relation.

For a root `Q`, put `d=|O-Q|`; then `1<=d<=h`, the relation class has

\[
                         N_d^{OR}=\binom qd\binom{q-1}{d-1},          \tag{2.4}
\]

and one ring through `O` contains

\[
 a_d^{OR}=\begin{cases}
 2,&1\le d<h,\\
 \ell-2h+2,&d=h
 
 \end{cases}                                           \tag{2.5}
\]

roots in that relation.

Finally, for two roots at Johnson distance `d`,

\[
 N_d^{RR}=\binom{q-1}d\binom qd,qquad
 a_d^{RR}=\begin{cases}
 2,&1\le d<h-1,\\
 \ell-2h+3,&d=h-1.
 \end{cases}                                           \tag{2.6}
\]

### Lemma 2.1 (exact central pair codegrees)

For either period `ell=ell_u`, the number of ring states containing a
fixed ordered resource pair in any relation above is

\[
 D_u,{a_d^{XY}\over N_d^{XY}},qquad
 XY\in\{OO,OR,RR\}.                                   \tag{2.7}
\]

#### Proof

In a cyclic order of length `ell>=2h`, compare one `h`-window with all
other `h`-windows.  Shifts `d` and `ell-d` have Johnson distance `d` for
`1<=d<h`; all `ell-2h+1` remaining shifts have distance `h`.  This proves
(2.3).  Comparing an `h`-window with the cyclic `(h-1)`-windows gives two
at each relation `d<h` and `ell-2h+2` at `d=h`, proving (2.5).  The same
calculation for two `(h-1)`-windows gives (2.6).

The stabilizer of one central resource is transitive on each displayed
relation class.  Double-count incidences between the `D_u` rings through
that resource and the class of size `N_d^(XY)`. \(\square\)

Call two central resources **compatible** when their pair codegree is
nonzero, and let `mathcal B(v)` be the compatibility ball of `v`.  From
(2.2), (2.4), and (2.6),

\[
 B:=\max_v|\mathcal B(v)|
 \le 2\sum_{d=0}^h
       \left(\binom qd\binom{q-1}d
       +\binom qd\binom{q-1}{d-1}\right)
 =\exp(O(h\log(q/h))).                                \tag{2.8}
\]

At critical width `h=O(sqrt(q))`, this is `exp(o(q))`.

## 3. One reserve ring has only `O(1/q)` local effect

### Lemma 3.1 (one-ring transparency)

Let `v` be a central resource, fix a candidate period `ell_u`, and let
`E` be one ring of either near-maximal period `ell_1` or `ell_2`, not
using `v`.  The number of period-`ell_u` ring candidates through `v` which
share any owner or root with `E` is at most

\[
                         {12\over q}D_u                \tag{3.1}
\]

for all sufficiently large `q`.

#### Proof

Use the union bound over the `2ell_u` resources of `E` and apply (2.7).
For equal-shore pairs, the largest proper relation ratio is

\[
                         {2\over q(q-1)},              \tag{3.2}
\]

and the terminal-distance ratio is smaller for `h>=3` and large `q`.
Thus all equal-shore resources of `E` contribute `O(D_u/q)`.

For an owner `O`, the only larger opposite-shore ratio is the incidence
relation `d=1`, equal to `2/q`.  A cyclic ring contains at most two roots
which are subsets of one fixed owner: after deleting its core, these are
cyclic `(h-1)`-intervals contained in one fixed `h`-set, and a proper
cyclic order has at most the two end intervals of that `h`-block.  Hence
the incidence contribution is at most `4D_u/q`.  All `d>=2` terms together
are `O(D_u/q^2)`.  The root-to-owner case is identical.  Enlarging the
absolute constant gives (3.1). \(\square\)

The constant `12` is inessential; the important uniform factor is
`O(1/q)`.

## 4. Random selection of the extreme reserve

Let

\[
 \mathcal X=\{X\subseteq R:3\le|X|\le h-1\},
 \qquad M=|\mathcal X|=\exp(o(q)).                    \tag{4.1}
\]

For each `X`, let `mathcal L_X` be the exact candidate list in
`MATH_THEOREM_EXTREME_TOP_INTERNAL_WITNESS_RESERVE_20260806.md`.  If
`j=|X|`, then

\[
 |\mathcal L_X|=N_j={j!(n-j)!\over s!},qquad
 {N_j\over D}={\binom{n-j}q\over\binom{q-1}j}.         \tag{4.2}
\]

Uniformly for `j<=h=O(sqrt(q))`,

\[
                         \alpha:=\max_X{D\over N_j}
                   =\exp(-(2\log2+o(1))q).             \tag{4.3}
\]

Choose independently one ring `E_X` uniformly from every list.

### Theorem 4.1 (central-transparent extreme reserve)

With positive probability, simultaneously:

1. the selected rings are pairwise owner/root-disjoint; and
2. for every central resource `v`, at most one selected ring contains any
   member of `mathcal B(v)`.

Consequently there is a deterministic reserve with those properties.

#### Proof

After one candidate ring is fixed, a second target's ring shares one of
its at most `2ell_1` central resources with probability at most

\[
                         2\ell_1\alpha.                 \tag{4.4}
\]

Therefore the probability of any pairwise collision is at most

\[
                         \binom M2,2\ell_1\alpha=o(1). \tag{4.5}
\]

For fixed `v` and fixed `X`, a union bound over `mathcal B(v)` gives

\[
 \Pr(E_X\cap\mathcal B(v)\ne\varnothing)\le B\alpha.  \tag{4.6}
\]

The probability that two different selected rings both meet this ball is
at most `M^2B^2alpha^2/2`.  Union-bound over the `2W` central resources.
Using `log W=(2log2+o(1))q`, while `M,B=exp(o(q))`, gives

\[
                         2W M^2B^2\alpha^2=o(1).        \tag{4.7}
\]

Equations (4.5) and (4.7) have sum below one for all sufficiently large
`q`; hence a simultaneous outcome exists. \(\square\)

### Corollary 4.2 (uniform surviving central degree)

Delete all owner and root resources used by the reserve of Theorem 4.1.
Every undeleted owner and root `v` retains at least

\[
                         \left(1-{12\over q}\right)D_u \tag{4.8}
\]

incident period-`ell_u` ring candidates, for each `u in {1,2}`.

#### Proof

A deleted resource can kill a candidate through `v` only if it belongs to
`mathcal B(v)`.  By Theorem 4.1, all compatible deleted resources lie in
at most one selected reserve ring.  Apply Lemma 3.1. \(\square\)

Thus the prescribed extreme bank does not create a central degree or
local central Hall bottleneck of positive density.

## 5. Why literal masked roles do not follow

The conclusion above concerns the full symmetric ring lists before the
cyclic filler state is conditioned.  A full-period masked collar records

\[
                         (K,G,x,\pi_G,\text{cut}),      \tag{5.1}
\]

where `G=F-{x}` is the ordered nonterminal filler bank.  Given this state
and one active triple, the two companion partitions and their cumulative
profiles are fixed.  The corresponding literal role fibre can therefore
have size one.

### Proposition 5.1 (conditioning obstruction)

No estimate of the form (4.8), by itself, implies that every fixed literal
masked-collar role retains a `(1-o(1))` fraction of its realizations.

#### Proof

Take a literal role with one realization.  If one owner, root, filler
occurrence, or cap ticket of either forced companion lies in the protected
reserve, the surviving fraction is zero.  Nevertheless (4.8) may hold at
every individual owner and root, because it averages over the exponentially
large unconditioned ring list through that resource.  Thus the implication
is false without an additional lower bound and spread condition on the
conditioned role list. \(\square\)

A sufficient upgrade would be a **prospective literal-role spread theorem**:
each required role has `L_role` complete filler/cut/ticket realizations,
every protected resource occurs in `o(L_role/M)` of them, and the same
bound survives earlier role choices.  The present masked full-tensor
regeneration instead preserves `G`, so it does not supply that theorem.

## 6. Exact consequence and remaining gate

The extreme witness reserve now has all of the following properties:

* one internal witness for every extreme target;
* pairwise owner/root disjointness;
* total size `exp(o(q))=o(W)`; and
* `(1-O(1/q))` residual degree at every unused central resource.

Therefore it can be inserted before any approximate or robust central
cover-down whose hypotheses depend only on these unconditioned degrees
and codegrees.

The exact one-copy theorem still needs more: co-select the cyclic filler
orders, masked companion states, arbitrary-width occurrence tickets and
common-cap resources so that the conditioned literal role fibres remain
nonempty.  The sparse reserve is not the obstruction at the central
owner/root level; the surviving obstruction is precisely the order of
quantifiers between central rounding and literal role conditioning.
