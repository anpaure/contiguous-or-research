# A three-way Boolean C6 gives an exact zero-charge vortex state splice

## Status

An exact two-component owner/root splice is obstructed by the absence of
`C4` in the middle-levels incidence graph.  This note constructs the first
possible replacement: three source components with explicit left and right
collars whose cyclic cross-splice

* inserts or deletes no source position;
* preserves every crossing OR occurrence in the displayed collars by an
  explicit cyclic bijection;
* preserves the complete rank-`r` owner and rank-`(r-1)` root multisets;
* realizes the two perfect matchings of a Boolean incidence `C6`;
* transports every occurrence ticket by the same cyclic bijection; and
* has an exact capped-age residence condition.

This closes the local algebra of a resource-disjoint zero-charge port.  It
does not plant the three collars inside the integral vortex/exterior
cover-down or prove that all arbitrary-width upper witnesses avoid the
three cuts.

## 1. The three collars

Fix an ambient owner-window width `h>=3` and owner rank `r`, with

\[
                              h\le r-1.                   \tag{1.1}
\]

Choose pairwise disjoint data

\[
 \begin{aligned}
 &K,\quad z,\quad a_0,a_1,a_2,\\
 &\lambda_1,\ldots,\lambda_{h-2},\quad
   \rho_1,\ldots,\rho_{h-2},
 \end{aligned}                                           \tag{1.2}
\]

where

\[
                              |K|=r-h-1.                  \tag{1.3}
\]

There is room on a `(2r-1)`-set because the total number of displayed
labels is `r+h-1<=2r-2`.

For `t in Z/3Z`, define an opened source component `C^t` of length at least
`2h-2`, with the two displayed collars disjoint.  Its `h-1`
letters immediately to the left of the cut have cumulative unions

\[
 L_i^t
   =K\cup\{z,a_{t+1}\}
      \cup\{\lambda_1,\ldots,\lambda_{i-1}\},
 \qquad 1\le i\le h-1,                                  \tag{1.4}
\]

and its `h-1` letters immediately to the right have cumulative unions

\[
 R_j^t
   =K\cup\{z,a_t\}
      \cup\{\rho_1,\ldots,\rho_{j-1}\},
 \qquad 1\le j\le h-1.                                  \tag{1.5}
\]

These chains are literal.  For example, on the left take the immediate
predecessor letter `K+z+a_(t+1)` and, moving farther left, use
`K+z+lambda_i`; on the right take the first letter `K+z+a_t` and then
`K+z+rho_j`.  Repeating `K+z` in every displayed letter is harmless and
makes its residence state constant through the portal.

For `i,j>=1`, put

\[
 B_{ij}=K\cup\{z\}
       \cup\{\lambda_1,\ldots,\lambda_{i-1}\}
       \cup\{\rho_1,\ldots,\rho_{j-1}\}.                \tag{1.6}
\]

Then the old crossing cell in component `t` is

\[
 V_t(i,j)=L_i^t\cup R_j^t
          =B_{ij}\cup\{a_t,a_{t+1}\},                   \tag{1.7}
\]

and has rank

\[
                         |V_t(i,j)|=r-h+i+j.              \tag{1.8}
\]

Thus crossing widths `h-1,h,h+1` have exactly the lower-root, owner, and
immediate-upper ranks `r-1,r,r+1`.

## 2. Exact three-way tensor

Cut all three components immediately before their right collars.  Rejoin
the left collar of component `t` to the right collar of component `t-1`
(indices modulo three).

### Theorem 2.1 (cyclic boundary-tensor identity)

For every `1<=i,j<=h-1`, the new crossing value after the three-way splice
is

\[
 \begin{aligned}
 N_t(i,j)
   &=L_i^t\cup R_j^{t-1}\\
   &=B_{ij}\cup\{a_{t+1},a_{t-1}\}
     =V_{t+1}(i,j).                                     \tag{2.1}
 \end{aligned}
\]

Consequently

\[
          \{\!\{N_0(i,j),N_1(i,j),N_2(i,j)\}\!\}
        = \{\!\{V_0(i,j),V_1(i,j),V_2(i,j)\}\!\}       \tag{2.2}
\]

at every displayed boundary address.  The splice preserves the complete
OR deck of all crossing intervals contained in the collars, with no
inserted source position.

#### Proof

The two cumulative chains have the common nonspecial part `B_(ij)`.  The
left special label is `a_(t+1)` and the newly attached right special label
is `a_(t-1)`.  In a three-element cyclic index set,

\[
       \{a_{t+1},a_{t-1}\}
        =\{a_{t+1},a_{t+2}\},
\]

which is the special pair in `V_(t+1)`.  This proves (2.1)--(2.2).
Intervals which cross no changed arc are literally unchanged.  No source
position was added or removed.  \(\square\)

### Corollary 2.2 (occurrence-ticket transport)

Attach to every old boundary occurrence `V_t(i,j)` any ticket depending on
its value, width, and local typed role.  Give the new occurrence
`N_t(i,j)` the ticket formerly carried by `V_(t+1)(i,j)`.  This is a
bijection preserving the value, width, and role of every ticket.

In particular, all owner, lower-root, immediate-upper, short compiler, and
named local-upper tickets in the displayed tensor survive simultaneously.

#### Proof

Equation (2.1) is an equality at the same `(i,j)` address type, and cyclic
translation of `t` is a bijection.  \(\square\)

For arbitrary-width upper targets, either extend the displayed collars and
the same cumulative-chain identity to the largest protected crossing
width, or choose their retained witnesses disjoint from the three cuts.
The theorem makes no claim about an unpriced longer crossing witness.

## 3. Exact owner/root C6 trade

At source width `h`, equation (1.8) gives rank-`r` owners.  At the extreme
split `i=1,j=h-1`, put

\[
 S=K\cup\{z,\rho_1,\ldots,\rho_{h-2}\}.                 \tag{3.1}
\]

Then `|S|=r-2`, the three right roots are

\[
                              Q_t=S\cup\{a_t\},           \tag{3.2}
\]

and the three old owners are

\[
                              O_t=S\cup\{a_t,a_{t+1}\}.  \tag{3.3}
\]

### Theorem 3.1 (minimal exact incidence trade)

The old incidences and new incidences are the two alternating perfect
matchings of the Boolean `C6` on

\[
 Q_0,Q_1,Q_2,qquad
 S+\{a_0,a_1\},S+\{a_1,a_2\},S+\{a_2,a_0\}.             \tag{3.4}
\]

All six resources are distinct.  At every other crossing owner split the
three owner values undergo the same cyclic permutation (2.1), while the
extreme split above witnesses the literal incidence `C6`.  Hence the splice
preserves the exact owner and lower-root multisets and is the minimum
possible resource-disjoint factor trade.

#### Proof

Before splicing, root `Q_t` is incident with owner `O_t`.  After the cyclic
tail reassignment, (2.1) makes it incident with the other pair-owner
containing `a_t`.  These are precisely the two alternating matchings of
the displayed six-cycle.  Distinctness follows from the three private
special labels.  A nontrivial two-edge trade would be a `C4`, which does
not exist in the middle-levels incidence graph, so three edges are
minimal.  \(\square\)

Across different crossing splits of a fixed width, the lambda/rho prefix
in `B_(ij)` records the split address.  The special pair records `t`.
Thus no two displayed crossing owners or roots of the same rank collide,
apart from the intended reuse of a resource on the two sides of the trade.

## 4. Component count and residence

If the three opened words were three cyclic components, the reassignment
`left(t)->right(t-1)` joins them into one cyclic component: its permutation
on the three old components is a three-cycle.

The exact residence condition is the ordinary capped-age condition at the
three new seams.  Namely, for every coordinate, concatenate its capped
trailing age at `left(t)` with its capped leading age at `right(t-1)`;
every resulting nonconstant positive run, and every zero gap when
biresidence is in scope, must have length at least `h`.  Constant-coordinate
flags are retained separately.  This condition is necessary and sufficient
because no run away from a changed seam is altered.

For the displayed portal there is a transparent sufficient realization:

1. keep every coordinate of `K+z` present throughout all three component
   completions;
2. use no `a`, `lambda`, or `rho` label outside its displayed portal
   occurrences; and
3. after the three-way joining, make consecutive source occurrences of
   each repeated noncore label cyclically separated by at least `2h`.

Then every noncore source occurrence creates an owner run of length `h`,
and successive such runs have zero gap at least `h`; core coordinates are
constant.  Thus the portal is biresident.  More generally the capped-age
test, rather than these sufficient spacing rules, is the exact interface.

## 5. Lift and remaining planting lemma

Adjoining a fixed set `A` to every displayed source letter preserves every
identity above.  Fixed-present coordinates become constant positive and
fixed-absent coordinates remain constant zero.  Therefore the C6 portal
lifts functorially into a balanced vortex or its exterior collar.

The exact remaining global row is now:

> co-select three phase-appropriate antipodal vortex/exterior components
> containing the collars (1.4)--(1.5), retain or reroute every longer upper
> witness away from the three cuts, and satisfy the capped-age spacing in
> one integral packet cover-down.

Once those planted components exist, Theorems 2.1 and 3.1 fuse them with
zero additive length and zero owner/root defect.  Thus neither deadline
arithmetic, local phase choice, two-cut `C4` obstruction, nor the literal
three-way state tensor remains an obstruction; only protected integral
planting and regeneration do.
