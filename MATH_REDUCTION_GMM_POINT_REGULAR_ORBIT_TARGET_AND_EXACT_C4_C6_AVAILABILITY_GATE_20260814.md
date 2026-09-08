# GMM Markov gate: point-regular orbit targets and exact C4/C6 availability

**Date:** 2026-08-14  
**Status:** exact target theorem and exact local availability reduction; no
all-parameter Markov theorem

## 0. Outcome

Put

\[
 n=2m+1,\qquad \mathcal X={ [n]\choose m},\quad
 \mathcal L={ [n]\choose m-1},\quad
 W=|\mathcal X|,\quad D={2W\over m+2}.             \tag{0.1}
\]

A GMM tight enumeration contracts to a lower-complete Hamilton cycle on
`\mathcal X`.  Its surplus lower load is a nonnegative integer vector `d`
of mass `D`.  Exact upper perfection forces

\[
 P_{m-1}d=\eta\mathbf1,
 \qquad \eta={D(m-1)\over n}.                       \tag{0.2}
\]

This note separates two issues which a symmetry average conflates.

1. For every `m>=2`, an abstract simple `D`-block target satisfying (0.2)
   exists.  For all `m` except the exceptional cyclic-orbit case `m=4`, it
   may be chosen as a union of complete orbits of one coordinate `n`-cycle.
   At `m=4`, no such orbit union has size `D=42`, although a regular
   `42`-block family exists by the general balancing theorem.
2. Averaging coordinate relabels of one GMM cycle proves only that the
   barycentre of its orbit is point-regular.  It does not select one
   Hamilton cycle with point-regular surplus.  Any nontrivial averaging
   denominator remains an integral orbit-choice/Markov problem.
3. A repeated-colour `C_4` is available exactly when one lower clique
   contains two **vertex-disjoint** cycle edges.  The selected edges of one
   lower clique form a path forest, so load at least three always suffices,
   while load two suffices exactly when its two occurrences are not
   consecutive on the Hamilton cycle.  Exactly one of the two alternative
   matchings is Hamilton-safe.
4. A mixed star/top `C_4` moves exactly one lower-surplus token across one
   edge of `J(n,m-1)`.  These unit transfers make the abstract nonnegative
   fixed-mass surplus digraph strongly connected.  Their actual occurrence
   is an exact two-step incidence condition between two lower-colour path
   forests, and Hamilton chronology remains a separate binary test.
5. An injective-lower rectangle `C_6` requires the explicit six owners and
   three negative edges to occur.  Conditional on occurrence, its
   Hamilton legality is an exact six-port order test: among the eight
   unoriented cyclic orders containing the negative matching, exactly four
   accept the prescribed positive matching.  Occurrence and chronology are
   not consequences of lower completeness.
6. If every surplus colour has load two, its repeated-colour `C_4` supply is
   exactly the
   number of duplicated colours whose two occurrences are nonconsecutive.
   This number can vanish at the level of the load/chronology constraints.
   Even when it is large, each selected pair exposes only the
   Hamilton-safe one of its two reconnections.

The strongest surviving theorem is therefore an occurrence/chronology
Markov statement.  At the ledger level every surplus routes conformally to
a point-regular target by unit mixed `C_4`s.  What is not known is whether
enough prescribed pairs of cycle edges occur, and whether their unique
Johnson reconnections have the required Hamilton chronology.  Symmetry
closes the target arithmetic, not the realization or reachability.

## 1. The orbit arithmetic of a regular surplus target

Let `r=m-1` and let `rho` be an `n`-cycle on the coordinate set.  Put

\[
                         g=\gcd(n,r)=\gcd(3,m-1)\in\{1,3\}.
                                                               \tag{1.1}
\]

Every `rho`-orbit of rank-`r` sets is point-regular.  Indeed, if its size is
`s`, its total point incidence is `rs`, and transitivity of `rho` makes all
`n` point degrees equal to `rs/n`.

The required mass has the divisibility

\[
                         {n\over g}\mid D.           \tag{1.2}
\]

Indeed the desired degree is the ballot number

\[
 \eta={D(m-1)\over 2m+1}
      ={2\over m}{2m\choose m-2}
      ={2m-1\choose m-2}-{2m-1\choose m-3},        \tag{1.2a}
\]

where a binomial coefficient with negative lower index is zero.  Thus
`n|Dr`; dividing by `g=gcd(n,r)` proves (1.2).

### Theorem 1.1 (cyclic-orbit regular target)

For every `m>=2`, `m!=4`, there is a `rho`-invariant simple family

\[
                         \mathcal H\subseteq\mathcal L,
 \qquad |\mathcal H|=D,\qquad
 P_{m-1}\mathbf1_{\mathcal H}=\eta\mathbf1.         \tag{1.3}
\]

For `m=4`, no union of complete `rho`-orbits has size `D`, although a
simple family satisfying (1.3) still exists.

#### Proof

If `g=1`, every rank-`r` orbit is free of size `n`, and (1.2) says that
`D` is a multiple of `n`.  Since `D<=|\mathcal L|`, take `D/n` full
orbits.

Suppose `g=3`; write

\[
                         n=3s,\qquad r=3t.           \tag{1.4}
\]

Every orbit has size `n` or `s=n/3`.  The short orbits are obtained by
choosing `t` of the `s` triples of the order-three subgroup and developing
under the quotient `s`-cycle.  Since `s=2t+1`, their number is

\[
 {1\over s}{s\choose t}={1\over t+1}{2t\choose t}. \tag{1.5}
\]

Write `D/s=3a+b`, with `b in {0,1,2}`.  For `m>=7`, (1.5) supplies at
least `b` short orbits.  There are also enough full orbits.  Indeed, the
total short-orbit mass is at most `2^s<2^m`, whereas

\[
 |\mathcal L|-D={m-2\over m+2}W\ge {5\over9}W>2^m             \tag{1.5a}
\]

for `m>=7`; the last inequality follows from
`W>=4^m/(2m+2)`.  Hence the nonshort mass is greater than `D`, so after
taking the `b` short orbits the required `a` full orbits remain.  The first
two cases are literal:

\[
\begin{array}{c|c|c|c}
m&n&r&D\\ \hline
4&9&3&42\\
7&15&6&1430.
\end{array}                                          \tag{1.6}
\]

At `m=7`, `s=5,t=2`, so the two short orbits are the developments of the
two cyclic distance classes of two quotient points.  Their total mass is
`10`, the remaining `4995` rank-six blocks form `333` full orbits, and
`D=95n+s`; hence one short and `95` full orbits work.  At `m=4`, the
rank-three orbit sizes are `9^9,3^1`; no subcollection has size `42`.
This proves the exception.

Every selected orbit is point-regular, so their union has degree
`rD/n=eta`.  Finally, for `m=4` and in fact for every `m>=2`, minimize the
sum of squared point degrees over all simple `D`-block families.  If
`r_x>=r_y+2`, selected `x`-not-`y` blocks outnumber selected
`y`-not-`x` blocks, so some swap `R -> R-x+y` lowers the square sum.  At a
minimum all degrees differ by at most one; their average `eta` is integral,
so all are equal. \(\square\)

This is not a Hamilton statement.  Its role is only to give a structured
regular target ledger.

### Proposition 1.2 (symmetry averaging does not select a cycle)

Let `C` be any lower-complete Hamilton cycle with surplus `d`.  Averaging
over the full symmetric group gives

\[
 {1\over n!}\sum_{g\in S_n}g d={D\over|\mathcal L|}\mathbf1_{\mathcal L}.
                                                               \tag{1.7}
\]

More generally, averaging over any coordinate-transitive group `G` makes
the point degrees equal to `eta`, although its block coefficients need
only be constant on the `G`-orbits rather than globally uniform.  Either
average is only a rational convex combination of relabelled Hamilton
cycles.  It yields one integral cycle only if the relevant orbit polytope
has an integral fixed point or an additional switching theorem rounds the
combination.  Neither property follows from coordinate transitivity.

At `m=4`, the `rho`-orbit count above gives a concrete warning: even the
desired `0/1` surplus target is absent from the complete-orbit subspace.
Thus an orbit average cannot be rounded merely by selecting whole cyclic
orbits in all parameters.

## 2. Exact repeated-colour C4 availability

Fix \(R\in\mathcal L\).  Every Johnson edge of lower colour `R` joins two
of the `m+2` owners

\[
                         R+x\qquad(x\notin R).       \tag{2.1}
\]

Thus the lower-colour class is the edge set of the clique `K_(m+2)` on
these owners.  Let `H_R` be the subgraph formed by the Hamilton-cycle edges
of lower colour `R`.  It is a linear forest: its maximum degree is at most
two, and a cycle component would have to be the entire Hamilton cycle
inside the proper clique (2.1).

### Theorem 2.1 (exact repeated-colour C4 criterion)

Two edges of lower colour `R` support a legal lower-load-preserving `C_4`
if and only if they are vertex-disjoint.  For every such pair, deleting
them leaves two paths, and exactly one of the two other perfect matchings
of their four endpoints reconnects those paths into one Hamilton cycle.
That reconnection has nonzero elementary-rectangle action on the upper
load.

#### Proof

Four distinct endpoints are necessary for a binary two-edge matching
switch, proving the only-if direction.  Conversely, deleting two
vertex-disjoint edges from one cycle leaves two paths.  Of the two other
endpoint matchings, one closes the two paths separately and the other
joins them crosswise.  Every endpoint pair is an edge of the clique (2.1),
so the crosswise choice is a legal Johnson reconnection.  Both old and new
shores have lower multiset `{R,R}`.  Their four upper colours are the two
pairings on four distinct outside labels, whose signed difference is a
nonzero rectangle. \(\square\)

### Corollary 2.2 (exact C4 supply count and adjacency charge)

Let `a_R` be the number of adjacent pairs of edges in `H_R`.  The number
of negative edge pairs supporting a legal repeated-colour `C_4` is exactly

\[
 A_4(C)=\sum_{R\in\mathcal L}
 \left[{\ell_C(R)\choose2}-a_R\right].             \tag{2.2}
\]

Because `H_R` is a nonempty linear forest,
`a_R<=ell_C(R)-1=d(R)`.  Hence

\[
 A_4(C)\ge\sum_R{d(R)\choose2}.                    \tag{2.3}
\]

In particular, load at least three always exposes a `C_4`.  If `d` is
simple, then exactly `D` colours have load two, but only those whose two
occurrences are nonadjacent expose a `C_4`; (2.3) then gives no positive
lower bound.  Candidate moves can also share owners or edges across their
chosen negative pairs, so `A_4(C)` is a catalogue count, not a packing.

For a fixed available pair with old outside-label pairing `ab|cd`, the two
candidate upper rectangles correspond to the reconnections `ac|bd` and
`ad|bc`.  The cyclic order of the four ports chooses exactly one.  Hence
raw repeated-colour abundance alone is not a descent theorem.

## 3. Mixed C4s give a complete conformal lower-ledger router

The preceding repeated-colour switch is not the whole `C_4` catalogue.
A Johnson `C_4` has one-unit lower action if and only if, up to cyclic
relabelling and orientation, it is obtained from an `(m-2)`-set `K` and
four distinct outside points `p,a,b,c` as

\[
 X_1=K+p+a,\quad X_2=K+p+c,\quad
 X_3=K+p+b,\quad X_4=K+a+b.                        \tag{3.1}
\]

With negative matching `12,34` and positive matching `23,41`, its exact
actions are

\[
 \boxed{\Delta_-=e_{K+a}-e_{K+b}},\qquad
 \boxed{\Delta_+=e_{K+p+b+c}-e_{K+p+a+c}}.          \tag{3.2}
\]

Thus it moves one surplus token from the lower colour `B=K+b` to the
adjacent colour `A=K+a`, and simultaneously moves one upper occurrence
between adjacent upper colours.  The negative lower colours are `K+p`
and `K+b`; the positive lower colours are `K+p` and `K+a`, so the common
`K+p` occurrence cancels in the load ledger.

### Lemma 3.1 (exact unit-action normal form)

Conversely, suppose the two lower-colour multisets differ by exactly
`e_A-e_B`.  After cancelling their common colour `P`, three consecutive
owners have the form `P+a,P+c,P+b`.  The common neighbours of `P+a` and
`P+b` are either `P+x`, which gives zero lower action, or
`(P-p)+a+b` for `p in P`.  The latter is exactly (3.1), with `K=P-p`, and
direct intersection gives (3.2).  This proves the claimed classification.

### Theorem 3.2 (constructive abstract conformal routing)

Let `d,d'` be any nonnegative integer vectors on `\mathcal L` with the
same total mass.  There is a sequence of mixed actions (3.2) sending `d`
to `d'` while every intermediate vector remains nonnegative.

Indeed, choose a surplus coordinate `B` and a deficient coordinate `A`,
route one token from `B` to `A` along any path in the connected Johnson
graph `J(n,m-1)`, and repeat.  Each step subtracts only from the coordinate
currently carrying that token.  Therefore **every GMM surplus ledger has
a conformal abstract path to every point-regular target of Section 1.**
There is no lower-lattice, parity, independent-support, or Hall obstruction
at this quotient level.  For each oriented adjacent transfer
`K+b -> K+a`, there are exactly

\[
        m(m+1)                                      \tag{3.4}
\]

labelled ambient atoms (3.1): choose `p` among the `m+1` points outside
`K+a+b`, and then `c` among the `m` points outside `K+a+b+p`.  Distinct
choices give distinct pairs of negative edges.

### Theorem 3.3 (exact occurrence and chronology gate)

For each lower colour `R`, let `H_R` be its selected path forest from
Section 2.  Regard an edge of `H_R` as its unordered pair `{x,y}` of
outside labels.  A mixed atom transferring `B` to `B-b+a` occurs in the
current cycle exactly when there are

\[
 b\in B,\qquad p,a\notin B,\quad p\ne a,\qquad
 c\notin B\cup\{p,a\}                                \tag{3.5}
\]

such that

\[
             \{p,a\}\in E(H_B),\qquad
             \{a,c\}\in E(H_{B-b+p}).              \tag{3.6}
\]

The two selected edges are automatically vertex-disjoint.  Let
`chi_C(B;b,p,a,c)` be one if the positive edges are absent and their
addition reconnects the two retained paths into one Hamilton cycle, and
zero otherwise.  Then the number of occurrence candidates, and the exact
number of legal conformal outgoing mixed arcs, are

\[
 A_{\rm occ}(C,d)=
 \sum_{B: d(B)>0}\ \sum_{b\in B}\ \sum_{(p,a)\in\vec E(H_B)}
 \ \sum_{\substack{c:\{a,c\}\in E(H_{B-b+p})\\c\ne b}}1,     \tag{3.7}
\]

\[
 A_{\rm legal}(C,d)=
 \sum_{B: d(B)>0}\ \sum_{b\in B}\ \sum_{(p,a)\in\vec E(H_B)}
 \ \sum_{\substack{c:\{a,c\}\in E(H_{B-b+p})\\c\ne b}}
                    \chi_C(B;b,p,a,c).              \tag{3.8}
\]

Here `\vec E(H_B)` contains both orientations of every edge of `H_B`;
both endpoints are
automatically outside `B`.  Equivalently, the innermost sum in (3.7) is

\[
 \deg_{H_{B-b+p}}(a)
       -\mathbf1_{\{a,b\}\in E(H_{B-b+p})}.          \tag{3.9}
\]

Thus (3.7) is the requested two-step incidence sum and gives the sharp
zero-occurrence cut:

> for every surplus `B`, every orientation `(p,a)` of every selected edge
> of `H_B`, and every `b in B`, the only possible neighbour of `a` in
> `H_{B-b+p}` is `b`.

Hamiltonicity imposes degree at most two on every owner globally and makes
each `H_R` a path forest, but it gives no pointwise lower bound on the
cross-forest continuation degree in (3.7).  Even a positive occurrence
sum is not enough: all its candidates may have `chi_C=0`.  Thus the exact
remaining theorem is an incidence-expansion plus chronology statement,
not a surplus-design or signed-lattice theorem.

As a finite audit only, exhaustive normalized enumeration at `m=2` found
`992` lower-complete Hamilton cycles, of which `880` had nonregular point
surplus; every one of those had a mixed occurrence and a legal mixed
switch.  A deterministic seeded sample of `20,981` Hamilton cycles at
`m=3` contained `366` lower-complete, point-nonregular cycles, again with
positive occurrence and legal counts.  These checks validate the formulas
and show that the gate is active in small cases; they are not an all-`m`
positivity theorem.

## 4. Exact injective-lower C6 availability

For an `(m-1)`-set `C`, distinct `a,b,c,d` outside it, and `p in C`, put
`K=C-p`.  The explicit rectangle packet has cyclic owners

\[
 Kab,\ Kbc,\ Kbp,\ Kpd,\ Kap,\ Kac,                \tag{4.1}
\]

negative matching `12,34,56`, and positive matching `23,45,61`.  Both
shores use the distinct lower colours `Kb,Kp,Ka`, once each, and its upper
action is

\[
                         e_{Cbc}+e_{Cad}-e_{Cbd}-e_{Cac}.       \tag{4.2}
\]

### Theorem 4.1 (literal C6 criterion)

The packet (4.1) is a legal move at a Hamilton cycle if and only if:

1. its three negative edges occur in the cycle;
2. its three positive edges are absent after the negative edges are
   removed; and
3. the retained three-path endpoint matching, together with the positive
   matching, is one six-cycle.

Equivalently, write the ports as `A,B,C,D,E,F` with negative matching
`AB,CD,EF`.  Up to dihedral symmetry, the eight cyclic orders containing
that matching are

\[
\begin{array}{c|c}
\text{order}&\text{positive }BC,DE,FA\text{ is Hamilton-safe}\\ \hline
ABCDEF&0\\
ABCDFE&0\\
ABDCEF&0\\
ABDCFE&1\\
ABEFCD&1\\
ABEFDC&1\\
ABFECD&1\\
ABFEDC&0.
\end{array}                                                   \tag{4.3}
\]

Thus exactly four of the eight possible port orders are safe for this
orientation.  Reversing the rectangle orientation exchanges the relevant
four.

#### Proof

Deleting three disjoint edges from one Hamilton cycle leaves three paths.
Contract them.  The retained outside pairing is a perfect matching on the
six ports.  Adding the positive matching gives a connected two-regular
quotient exactly when it is a six-cycle.  Enumerating the eight cyclic
orders of the three negative blocks gives (4.3); equivalently, it is the
four-of-eight perfect-matching calculation. \(\square\)

The occurrence condition is much stronger than lower-colour availability.
It requires three prescribed edges on six prescribed owners, not merely
one occurrence of each of `Kb,Kp,Ka`.  Lower completeness therefore gives
no positive lower bound on the number of eligible packets (4.1).

## 5. The directed Markov gate

Let `G` have as vertices lower-complete Hamilton cycles on \(\mathcal X\), and
join two states when one legal `C_4` or injective-lower rectangle `C_6`
connects them.  The preceding theorems determine its local arcs exactly:

- every vertex-disjoint pair in a repeated lower-colour forest exposes a
  `C_4`, but only its current Hamilton-safe reconnection;
- a lower-moving `C_4` requires two surplus-bearing occurrences in one
  two-step path-forest incidence and the Hamilton-safe orientation; its
  mixed unit actions route every abstract fixed-mass surplus ledger, but
  the occurrence/chronology-restricted digraph may have sinks;
- a `C_6` arc exists only after both the six-edge support test and the
  four-of-eight chronology test;
- the defect derivative depends on the current upper occupancies, so an
  available arc need not descend; and
- after a move, both the repeated-colour bank and all port orders change.

The abstract orbit family \(\mathcal H\) from Theorem 1.1 is therefore a
target ledger, not a vertex of `G`.  The missing positive statement is:

> **Point-regular GMM Markov theorem.**  Some GMM lower-complete Hamilton
> cycle has surplus \(\mathbf1_{\mathcal H}\) for a regular family
> \(\mathcal H\),
> or its component of `G` contains such a state; from there the same
> component contains an upper-perfect state.

The first clause is a prescribed-surplus Hamilton theorem.  At the ledger
level the second clause is now supplied constructively by Theorem 3.2; its
remaining content is the changing occurrence/chronology support.  The
final clause is the injective-lower `C_6`/larger-trade chronology theorem.
None follows from symmetry averaging alone.

## 6. Scope

This note proves the existence of structured point-regular surplus
targets, the exact cyclic-orbit exception at `m=4`, the complete conformal
lower-ledger routing by mixed unit `C_4`s, its exact two-step
path-forest occurrence sum and zero-occurrence cut, and the exact local
availability/chronology tests for the repeated-colour `C_4` and explicit
rectangle `C_6` catalogues.  It proves no GMM selection with that surplus,
no legal monotone path in the Hamilton state space, and no upper-perfect
Hamilton cycle.
