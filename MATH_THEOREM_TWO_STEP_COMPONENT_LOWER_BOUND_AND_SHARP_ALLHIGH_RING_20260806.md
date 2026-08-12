# Two-step state components: a sharp size lower bound and the matching all-high ring

## Status

This note settles the proposed constant-size state-balancing repair for the
two-owner hinge macros.  It is impossible once the trace depth grows: every
state-balanced component with distinct owner windows has more than
`(d+1)/2` macros.  In particular, oriented three- and four-macro endpoint
cycles fail for all sufficiently large `d`, regardless of endpoint labels.

The bound is sharp.  A common-core all-high rotor gives a literal balanced
component with the least possible number of macros, all owners and
immediate-lower roots distinct, and a distinct marked suffix chain at every
owner.

There is a second exact no-go.  The exponential common-spine portal bank has
a linear positional-state deficit: balancing `N` such roles requires at
least `N` roles of complementary layer profile.  A bounded or sublinear
"seasoning buffer" cannot turn that owner cover into a chronology.

## 1. Two-step trace macros

A depth-`d` two-owner macro is a word of `d+2` nonempty letters

\[
                         X=(B_0,B_1,\ldots,B_{d+1}).            \tag{1.1}
\]

Its tail and head states are

\[
 P(X)=(B_0,\ldots,B_{d-1}),\qquad
 Q(X)=(B_2,\ldots,B_{d+1}),                                  \tag{1.2}
\]

and its two owner windows are

\[
 O_0(X)=\bigcup_{j=0}^dB_j,qquad
 O_1(X)=\bigcup_{j=1}^{d+1}B_j.                              \tag{1.3}
\]

This includes the opposed-hinge macros.  A balanced integral selection of
such macros is a disjoint union of directed components under the equality
`Q(X_i)=P(X_(i+1))`.

## 2. Exact period collapse

### Theorem 2.1 (two-step component lower bound)

Let `X_0,...,X_(q-1)` form one directed state component:

\[
                         Q(X_i)=P(X_{i+1})quad(i\bmod q).       \tag{2.1}
\]

Then there is a cyclic word of `2q` nonempty letters

\[
                         L_0,L_1,\ldots,L_{2q-1}               \tag{2.2}
\]

such that

\[
                 X_i=(L_{2i},L_{2i+1},\ldots,L_{2i+d+1})       \tag{2.3}
\]

with subscripts modulo `2q`.

If

\[
                              2q\le d+1,                       \tag{2.4}
\]

then all `2q` owner windows in the component have the same union.  Hence a
component using pairwise distinct owners must satisfy

\[
 \boxed{q>{d+1\over2}.}                                      \tag{2.5}
\]

#### Proof

Put `L_(2i)=B_(i,0)` and `L_(2i+1)=B_(i,1)`.  Equation (2.1) says

\[
                         B_{i+1,j}=B_{i,j+2}qquad(0\le j<d), \tag{2.6}
\]

so induction gives (2.3); closure of the component gives the cyclic
subscripts.

The owner windows in (1.3), over all `i`, are exactly the `2q` cyclic
length-`(d+1)` windows of (2.2).  Under (2.4), every such window meets every
one of the `2q` residue positions.  Its union is therefore always

\[
                              \bigcup_{t=0}^{2q-1}L_t.          \tag{2.7}
\]

Distinct owner use is impossible, proving (2.5).  `square`

### Corollary 2.2 (constant endpoint cycles and seasoning)

A three-macro balanced component with distinct owners requires `d<=4`; a
four-macro component requires `d<=6`.  More generally, adding `s` seasoning
macros to a fixed `q_0`-macro endpoint cycle cannot make its owners distinct
unless

\[
                         s>{d+1\over2}-q_0.                    \tag{2.8}
\]

Thus no universal constant seasoning buffer works at triangular depth
`d -> infinity`.

## 3. Sharp all-high construction

The lower bound is attained at the first possible even source period.

### Theorem 3.1 (minimal state-balanced all-high ring)

Let

\[
 q_*=\left\lfloor{d+1\over2}\right\rfloor+1,qquad
 L=2q_*.                                                     \tag{3.1}
\]

Assume `r>=d+2`.  Choose a core `K` of size `r-d-1` and `L` distinct labels

\[
                         f_0,\ldots,f_{L-1}                    \tag{3.2}
\]

outside `K`.  Put

\[
                              B_t=K\cup\{f_t\}.                \tag{3.3}
\]

For `i in Z_(q_*)`, take the macro

\[
                         X_i=(B_{2i},B_{2i+1},\ldots,
                                      B_{2i+d+1}),             \tag{3.4}
\]

with indices modulo `L`.  Then:

1. the macros form one directed state component;
2. their `L=2q_*` owner windows are pairwise distinct rank-`r` sets;
3. their `L` immediate-lower transition roots are pairwise distinct
   rank-`r-1` sets; and
4. for every `1<=j<=d`, the proper `j`-suffix unions over the `L` owners
   are `L` distinct named targets of rank

   \[
                              r-d-1+j.                         \tag{3.5}
   \]

Thus (3.1) is the exact minimum component size permitted by Theorem 2.1.

#### Proof

The head of `X_i` is

\[
                         (B_{2i+2},\ldots,B_{2i+d+1}),         \tag{3.6}
\]

which is the tail of `X_(i+1)`, proving state balance and connectedness.

By definition of `q_*`,

\[
                              L>d+1.                           \tag{3.7}
\]

An owner window beginning at phase `s` is

\[
                         K\cup\{f_s,f_{s+1},\ldots,f_{s+d}\}. \tag{3.8}
\]

It has rank `(r-d-1)+(d+1)=r`.  Proper cyclic intervals of a fixed length
strictly below `L` have distinct start points, so the `L` sets (3.8) are
distinct.  Consecutive owners intersect in

\[
                         K\cup\{f_{s+1},\ldots,f_{s+d}\},      \tag{3.9}
\]

which has rank `r-1`; these cyclic length-`d` intervals are likewise
distinct.

Finally, a proper suffix of length `j` is `K` together with a cyclic
`j`-interval of the `f` labels.  Its rank is (3.5), and `j<=d<L` makes the
`L` occurrences distinct.  `square`

The construction is the shortest possible owner-once all-high rotor at the
two-step macro scale.  It is a local exact chain packet, not a cover of all
owners or all named targets.

### Proposition 3.2 (endpoint rectangles freeze on the balanced ring)

Try to enlarge (3.4) by replacing, in every even-start macro, its first and
last letters by

\[
                 \{f_{2i}\}\cup A_i,qquad
                 \{f_{2i+d+1}\}\cup C_i,qquad
                 A_i,C_i\subseteq K,                          \tag{3.10}
\]

while keeping every interior letter equal to `K union {f_t}`.  Exact
head--tail balance around the same `q_*`-cycle forces

\[
                              A_i=C_i=K                         \tag{3.11}
\]

for every `i`.

#### Proof

The first coordinate of the head of macro `i` is the fixed interior letter
`K union {f_(2i+2)}`.  It equals the first coordinate
`{f_(2i+2)} union A_(i+1)` of the next tail only when
`A_(i+1)=K`.  The last coordinate of the former head is
`{f_(2i+d+1)} union C_i`, while the last coordinate of the next tail is the
fixed interior letter `K union {f_(2i+d+1)}`.  Hence `C_i=K`.  `square`

Thus the sharp balanced rotor and the large endpoint-hinge menu live on
opposite faces: state balance collapses every endpoint-only rectangle of
the fixed all-high ring.  Any nontrivial attachment actuator on this ring
must change interior age blocks as well, exactly as a genuine pull/C6
exchange would.

## 4. Exact positional obstruction for the exponential portal bank

The common-spine portal bank uses the opposed-hinge words

\[
 (\{a_i\},D_i,D_{d-1},\ldots,D_1,\{b\}\cup A_i),              \tag{4.1}
\]

where `|D_i|=r-d>1` and all common internal layers are singletons.  Let the
bank contain `N` roles.

### Theorem 4.1 (no sublinear seasoning of the one-spine bank)

Assume `d>=3` and `r-d>1`.  If the `N` roles in (4.1) are part of a
state-balanced selection, then that selection contains at least `N`
additional roles outside the bank.

#### Proof

For any collection of two-step macros, let `H_t(s)` be the number of source
letters of rank `s` in macro position `t`, with positions numbered
`0,...,d+1`.  Equality of the tail-state and head-state multisets implies,
coordinatewise,

\[
                              H_t(s)=H_{t+2}(s)
                 \qquad(0\le t<d).                            \tag{4.2}
\]

In every bank role, position one is `D_i`, of rank `r-d`, while position
three is the common layer `D_(d-2)`, of rank one.  Thus the bank contributes
`N` to

\[
                         H_1(r-d)-H_3(r-d).                    \tag{4.3}
\]

Each additional macro changes (4.3) by at least `-1` and at most `1`.
Equation (4.2) forces the total difference to zero, so at least `N`
additional macros are necessary.  `square`

The same proof works with set-valued rather than rank-valued positional
histograms and is then stronger.  The rank projection already shows that
the exponential owner-cover bank cannot be repaired by `O(1)`, polynomial,
or otherwise sublinear seasoning.  A viable global construction must mix
complementary layer profiles at the same macroscopic scale.  The all-high
ring of Theorem 3.1 shows how exact balance can occur, but it does not by
itself provide the exponential mixed-profile partition.

## 5. Classification of disjoint-block cyclic rotors

One might try to obtain the missing profile mixture merely by replacing the
singleton moving labels in Theorem 3.1 by larger disjoint blocks.  The
Johnson row forbids this.

### Theorem 5.1 (gcd profile law and Johnson rigidity)

Let `D=d+1`, let `L>D`, and take a cyclic source word

\[
                         B_t=K\cup F_tqquad(t\in\mathbb Z_L), \tag{5.1}
\]

where the private blocks `F_t` are nonempty and pairwise disjoint.  Put
`c_t=|F_t|` and let `O_t` be the union of the `D` consecutive letters
beginning at `t`.

1. All owners `O_t` have the same rank if and only if

   \[
                              c_{t+D}=c_t                      \tag{5.2}
   \]

   for every `t`.  Thus the size profile has exactly
   `gcd(L,D)` free cyclic classes.
2. If consecutive owners are Johnson adjacent of common rank, then

   \[
                              c_t=1qquad(t\in\mathbb Z_L).    \tag{5.3}
   \]

#### Proof

The private part of `O_t` has size

\[
                              s_t=\sum_{j=0}^{D-1}c_{t+j}.     \tag{5.4}
\]

Since `s_(t+1)-s_t=c_(t+D)-c_t`, constant owner rank is equivalent to
(5.2).  The translation `t -> t+D` has `gcd(L,D)` orbits, proving the
first item.

Under (5.2), consecutive owner windows differ by deleting the disjoint
block `F_t` and inserting the disjoint block `F_(t+D)`, both of size
`c_t`.  Their intersection consequently has rank

\[
                              |O_t|-c_t.                       \tag{5.5}
\]

Johnson adjacency requires this to be `|O_t|-1`, so `c_t=1` for every
`t`.  `square`

Therefore a state-balanced cyclic rotor with disjoint moving blocks has no
mixed Johnson-compatible size profile: it collapses to the singleton
all-high construction.  Any successful macroscopic complement to the
portal banks must use overlapping letters, equivalently moving omissions
inside a repeated core.  This locates the required new circuit squarely in
the pull-block/age geometry rather than in a larger disjoint-block period.

## 6. Pull-decorated owner-once Johnson rings

Moving omissions inside the repeated core gives the required nontrivial
profile without changing the owner cycle.

### Theorem 6.1 (literal pull overlay)

Put `D=d+1`.  Let `L` be even with `D<L<=r+d`.  Choose disjoint sets

\[
                         K,\qquad F=\{f_0,\ldots,f_{L-1}\},
 \qquad |K|=r-D,                                             \tag{6.1}
\]

and cyclically order `F`.  For each `x in K`, choose an omission set
`I_x subset Z_L` whose cyclic connected components all have length at most
`d` (the empty set is allowed).  Define the
source letters

\[
 A_t=\bigl(K-\{x:t\in I_x\}\bigr)\cup\{f_t\}.                 \tag{6.2}
\]

Then:

1. every length-`D` owner window is

   \[
             O_t=K\cup\{f_t,f_{t+1},\ldots,f_{t+d}\},         \tag{6.3}
   \]

   so the `L` owners are distinct rank-`r` sets and form a Johnson cycle;
2. taking the `L/2` two-step macros beginning at the even phases gives one
   exact state-balanced component using every owner once;
3. the `L` immediate-lower roots are the distinct rank-`r-1` sets

   \[
             K\cup\{f_{t+1},\ldots,f_{t+d}\};                 \tag{6.4}
   \]
4. for every proper cyclic source interval `J=[s,s+q-1]`, `1<=q<=d`,

   \[
     \bigcup_{t\in J}A_t
       =\{f_s,\ldots,f_{s+q-1}\}
          \cup\bigl(K-H(J)\bigr),                             \tag{6.5}
   \]

   where

   \[
                         H(J)=\{x\in K:J\subseteq I_x\};       \tag{6.6}
   \]
5. at every fixed width `q`, the `L` values in (6.5) are pairwise distinct.

#### Proof

No omission set `I_x` contains `D` consecutive phases.  Hence every length-`D`
window contains a source letter which still contains `x`; this holds for
every `x in K` and proves (6.3).  Distinct proper cyclic `D`-intervals of
the `f` labels give distinct owners.  Consecutive owners delete `f_t` and
insert `f_(t+D)`, proving Johnson adjacency and (6.4).

The even-start macros advance by two source positions.  Since `L` is even,
they form one cycle on the even phases and their two owner windows begin at
all `L` phases exactly once.

For a proper interval `J`, the private contribution is its displayed
`f`-interval.  A core coordinate `x` is absent from the union exactly when
it is omitted at every position of `J`, equivalently `J subseteq I_x`.
This gives (6.5)--(6.6).  Finally the private cyclic `q`-intervals are
distinct because `q<L`; they are disjoint from `K`, so adding arbitrary
core parts cannot identify two values.  `square`

### Corollary 6.2 (exact staircase blocks on an owner-once ring)

Choose pairwise disjoint cyclic runs.  A block of type `(delta,j)` assigns
the same run `I` of length `j<=d` to exactly `delta` core coordinates and
assigns no other omission run overlapping `I`.  Relative to the all-high
ring, this block creates exactly

\[
                         j-q+1                                \tag{6.7}
\]

width-`q` windows of rank `|K|+q-delta` for every `q<=j`, and no other
rank changes.  Thus its lower-rank incidence is exactly the pull-clock
staircase tile.

Any integral multiset of pull blocks satisfying

\[
                         \sum_{\delta,j}(j+1)n_{\delta,j}\le L \tag{6.8}
\]

can be placed with one separating high phase after every run.  It gives a
literal state-balanced, owner-once, q1-simple Johnson ring whose complete
proper-window deck is named-simple at each fixed width.

#### Proof

A width-`q` interval loses one of the `delta` coordinates exactly when it is
contained in the common length-`j` omission run.  There are `j-q+1` such
subintervals.  Pairwise disjoint runs prevent a window from being contained
in two block runs, so the effects add without nonlinear overlap.  The
packing inequality (6.8) places all runs and their separators on the cyclic
timeline.  Apply Theorem 6.1.  `square`

This is the first literal construction in this note which simultaneously
has nontrivial pull profiles, exact state balance, one-copy distinct owners,
distinct q1 roots, and no same-width named-target collision.  It does not
yet solve the all-owner problem: one ring has

\[
                         L\le |[2r-1]-K|=r+d                  \tag{6.9}
\]

because its private phase labels must be distinct.  The remaining global
task is to partition the complete owner/target demand into many such rings
with compatible integer block histograms and no cross-ring target
collisions.  The canonical rational pull coefficients need not have
denominators fitting any one `L`; integral trades among rings remain
necessary.
