# Complementary-clock adjacent swaps and the canonical aperture lift

**Date:** 2026-08-13  
**Status:** unconditional local clock and erosion lemmas; exact conditional
three-clock seam criterion.  The remaining hypothesis is a protected
global clock-halo/packing condition, not local owner or palette algebra.

## 1. Canonical aperture lift of a resident Johnson cycle

Let

\[
                         O=(O_i)_{i\in\mathbb Z/n\mathbb Z}      \tag{1.1}
\]

be a cyclic sequence of rank-`R` owners, consecutive owners being Johnson
adjacent.  Fix `q<=R`.  Assume every nonempty one-run in every coordinate
trace

\[
                         (1_{z\in O_i})_i                         \tag{1.2}
\]

has length at least `q`.  Define the cyclic erosion letters

\[
                         A_j=\bigcap_{t=0}^{q-1}O_{j-t}.          \tag{1.3}
\]

### Lemma 1.1 (erosion--dilation reconstruction)

Every `A_j` is nonempty, and

\[
                         O_i=\bigcup_{j=i}^{i+q-1}A_j.            \tag{1.4}
\]

Moreover

\[
 \bigcup_{j=i+1}^{i+q-1}A_j=O_i\cap O_{i+1},qquad
 \bigcup_{j=i}^{i+q}A_j=O_i\cup O_{i+1},              \tag{1.5}
\]

and, for every `w>=1`,

\[
 \bigcup_{j=i}^{i+q+w-2}A_j
       =\bigcup_{t=i}^{i+w-1}O_t.                     \tag{1.6}
\]

Thus `A` is a literal aperture-`q` cyclic source for `O`, its immediate
lower and upper source palettes are exactly the Johnson intersection and
union palettes, and every wider owner-union witness has the expected
source interval.

#### Proof

For one coordinate, (1.3) is binary erosion by an interval of length `q`.
A one-run of length at least `q` contains, through each one-position, a
length-`q` subinterval of the same run.  Taking the union of all such
subintervals therefore recovers the run, proving (1.4) coordinatewise.

If a coordinate lies in both `O_i,O_(i+1)`, the same run contains a
length-`q` interval whose ending index lies in `[i+1,i+q-1]`.  Conversely,
every erosion letter with an index in that range is contained in both
owners.  This proves the first identity in (1.5).  The second and (1.6)
follow by the same interval-overlap argument: every erosion interval
indexed on the left meets the owner-index interval on the right, and every
one-position on the right lies in a length-`q` subinterval indexed on the
left.

Finally, `q` consecutive rank-`R` Johnson owners have nonempty
intersection: beginning with the first owner, at most one element is
deleted at each of the `q-1` transitions, so their intersection has size
at least

\[
                              R-(q-1)\ge1.             \tag{1.7}
\]

Hence every source letter is nonempty.  `square`

This lemma turns the source-lift part of a compound-cycle construction
into a trace question.  It does **not** prove the required run condition;
that must be audited at every splice.

## 2. A resident clock for one adjacent owner exchange

Let

\[
                         A=H\cup\{u\},qquad
                         B=H\cup\{v\},                 \tag{2.1}
\]

be adjacent rank-`R` owners.  Choose a `q`-set

\[
                         W=\{w_0,\ldots,w_{q-1}\}\subseteq H     \tag{2.2}
\]

and a disjoint fresh `q`-set

\[
                         V=\{v_0,\ldots,v_{q-1}\}.                \tag{2.3}
\]

On the cyclic order

\[
                         w_0,\ldots,w_{q-1},v_0,\ldots,v_{q-1}  \tag{2.4}
\]

let `D_j` be the cyclic `q`-window beginning at `j`.  Hence
`D_0=W`, `D_q=V`, and `D_(2q)=W`.  Put `J=H-W` and define the open owner
path

\[
 \begin{split}
 \Gamma(H;u,v;W,V)=(&J+u+D_0,\ldots,J+u+D_q,\\
                    &J+v+D_q,\ldots,J+v+D_{2q}).       \tag{2.5}
 \end{split}
\]

It has `2q+2` owners and `2q+1` edges.

### Lemma 2.1 (complementary-clock swap)

The path (2.5):

1. is a simple Johnson path from `A` to `B`;
2. has simple immediate-lower and immediate-upper palettes;
3. does not use the direct-edge tickets `H` or `H+u+v`;
4. has `u` present on its first `q+1` owners and `v` present on its last
   `q+1` owners;
5. has every point of `H-W` constant; and
6. gives each clock point a positive and a zero segment of length at least
   `q`, provided the repeated midpoint `D_q` is counted in its actual
   phase.

If the path is placed in a cycle whose complementary exterior arc contains
every point of `W` throughout and no point of `V`, then every coordinate
trace created or modified by the clock has both positive and zero runs at
least `q`.

#### Proof

Clock steps exchange the oldest member of `D_j` for the next coordinate;
the midpoint exchanges `u` for `v`.  This proves adjacency.  Distinct
proper cyclic windows give owner simplicity within either phase, and the
two phases are separated by `u/v`.  At `D_q`, the two owners differ by
`u/v`, so the whole path is simple.

On a clock edge the lower and upper clock parts are the proper cyclic
`(q-1)`- and `(q+1)`-windows `D_j cap D_(j+1)` and
`D_j union D_(j+1)`.  They are simple within a phase and phases are again
separated by `u/v`.  The midpoint lower ticket contains neither `u,v`,
while its upper ticket contains both.  This also separates it from all
clock edges.  Since `V` is nonempty, neither midpoint ticket is the direct
ticket, and every other edge changes at least one member of `W`; item 3
follows.

Items 4--5 are immediate.  Along

\[
                         D_0,\ldots,D_q,D_q,\ldots,D_{2q},       \tag{2.6}
\]

each clock bit has one zero and one positive segment of length at least
`q`; the repeated antipodal state only lengthens one of them.  On the
complementary arc, the `W` bits are one and the `V` bits zero, so the two
boundary pieces of the corresponding segment join without introducing a
short run.  `square`

The exterior condition in Lemma 2.1 is essential.  An open clock placed
without it can split an old positive run into two short boundary pieces.

## 3. Three-clock repair of one context seam

Use the notation of
`MATH_THEOREM_THREE_AUXILIARY_OWNER_CONTEXT_SEAM_DIAMOND_20260813.md`:

\[
 \begin{aligned}
 U&=G+x+p,& I&=U-r,& I'&=U-s,\\
 P&=G+p,& X&=G+x,& K_a&=G+a,&K_b&=G+b,
 \end{aligned}                                       \tag{3.1}
\]

where `r,s in G` and `a,b,x,p` lie outside `G`.  Define the one auxiliary
owner

\[
                         Z_a=(G-s)+x+a.                \tag{3.2}
\]

Choose three clock pairs `(W_i,V_i)`, `i=0,1,2`, and put

\[
 \begin{aligned}
 \Gamma_0&=\Gamma(G;p,x;W_0,V_0),\\
 \Gamma_1&=\Gamma(G-s+a;s,x;W_1,V_1),\\
 \Gamma_2&=\Gamma(G-s+x;a,p;W_2,V_2).                \tag{3.3}
 \end{aligned}
\]

Their endpoints are respectively

\[
                         P\to X,qquad K_a\to Z_a,qquad
                         Z_a\to I'.                   \tag{3.4}
\]

Replace the bad seam by the two paths

\[
                         I-P-\Gamma_0-X-K_b,           \tag{3.5}
\]

where the repeated endpoints in the notation are identified, and

\[
                         K_a-\Gamma_1-Z_a-\Gamma_2-I'. \tag{3.6}
\]

Again repeated endpoints are identified.  There are `6q+1` auxiliary
owners beyond the six original boundary/endpoint owners.

### Theorem 3.1 (protected three-clock seam criterion)

Assume:

1. `W_0,W_1,W_2` are pairwise disjoint `q`-sets contained in a fixed
   coordinate set common to both complementary exterior rail arcs;
2. `r,s` lie outside every `W_i`;
3. `V_0,V_1,V_2` are pairwise disjoint, avoid all displayed coordinates,
   and are absent on the corresponding complementary exterior arcs;
4. the first and last clock labels are ordered so that no two boundary
   lower tickets agree; pairwise disjoint `W_i` and `r,s notin W_i` are a
   sufficient choice; and
5. all selected owner and ticket signatures avoid the previously protected
   exterior.

Then (3.5)--(3.6), with the retained exterior half-edges:

* is owner-simple;
* has simple immediate-lower and immediate-upper palettes;
* uses `U` exactly once, on `I-P`, and `G` exactly once, on `X-K_b`;
* is positive- and zero-resident with threshold `q`; and
* may be installed identically in both states of the context-square
  telescope, contributing zero signed owner and immediate-palette current.

Each resulting closed component has the literal canonical aperture-`q`
source (1.3), with exact immediate palettes and all wider identities
(1.6).

#### Proof

Each clock has the conclusions of Lemma 2.1.  Every internal owner of
clock `i` contains a point of the private set `V_i`; hence internal owners
from different clocks, and internal owners versus the exterior, are
separated.  The same private signatures separate all upper clock tickets.

Every non-boundary lower clock ticket contains `V_i`.  The two boundary
lower tickets of clock `i` are

\[
                         H_i-w_i^{\rm first}+u_i,qquad
                         H_i-w_i^{\rm last}+v_i.       \tag{3.7}
\]

They are separated by the missing `W_i` label and by the anchors
`a,x,p,s`.  Conditions 2 and 4 separate them from the two retained lower
tickets

\[
                         (G-r)+p,qquad G.             \tag{3.8}
\]

This proves local palette simplicity; condition 5 supplies separation
from the exterior.  The direct tickets of the replaced swaps are absent by
Lemma 2.1, leaving `U` only on `I-P` and `G` only on `X-K_b`.

The paths have the required degree ledger: their four boundary owners have
one patch edge and one retained exterior edge; all other owners have patch
degree two.  Owner simplicity follows from the same private signatures.

For residence, apply Lemma 2.1 to all three clocks.  The direct edge
`I-P` is an original boundary transition; the first clock only lengthens
the ensuing `p` and `x` phases.  Similarly `X-K_b` begins the original
exterior phase of `b`.  On the second path, the first clock changes
`s` to `x`, and the second changes `a` to `p`; each old and new coordinate
has a clock phase of length `q+1`, while `a` is common through the first
clock and `x` through the second.  The common-coordinate and fresh-clock
conditions prevent boundary splitting.  No other trace is shortened.

Both telescope states contain the same six original seam owners as a set.
All auxiliary owners and all patch edges are chosen identically, giving
zero signed local current.  Finally Lemma 1.1 produces the literal source
and palettes on every closed resident component.  `square`

## 4. What this closes and what it leaves

The theorem closes the **local** owner, immediate-palette, residence, and
source-realization obstruction at a context seam.  It replaces the
multiplicity-two pair `(G,G+x+p)` by one occurrence of each plus three
protected complementary clocks.

Its hypotheses are not automatic at the multicommodity scale.  In the
central regime, two `c`-cores contained in one context have intersection
at least

\[
                              c-q+1.                  \tag{4.1}
\]

Thus three disjoint clock bases exist whenever `c-q+1>=3q`.  What remains
is the named-order assertion that the fresh clock sets have the required
zero halos on the complementary exterior arcs, and that all
`q(q-1) O(R/q)` seam banks avoid one another and the protected factor.

The all-width current across intervals which enter and leave the compound
bank is also not implied merely by identical local owner sets.  It requires
the phase-and-endpoint-refined exterior correspondence isolated in
`MATH_THEOREM_PHASE_CLOCK_DILATION_RESIDENT_ALLWIDTH_LOCAL_AND_CENTRAL_ODD_HOST_20260813.md`,
or a direct full-width ledger for the complete compound braid.

Accordingly the remaining Gate-A statement is now sharper:

\[
 \boxed{\text{protected multicommodity clock-halo packing}
        +\text{ refined all-width exterior matching}.}
\]

No local rank, Johnson adjacency, immediate-palette, residence, or source
erosion problem remains for a seam satisfying Theorem 3.1.
