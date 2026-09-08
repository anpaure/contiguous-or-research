# Adjacent necklaces: repeated hub colours promote to a one-level receiver Hall problem

**Date:** 2026-08-05  
**Method:** odd-circulation petal matchings, compatible double-cut
expansions, and ordinary bipartite Hall; no computation  
**Status:** unconditional fixed-level reduction.  The one-use hub partition
constraint can be removed at one cut level by paying one distinct
next-level receiver for every excess use of a hub colour.  Existence of the
required receiver SDR, and collision-free composition between different
cut levels, remain open.

## 1. Literal cut notation

For a 2-independent cut set `H` on the odd coordinate cycle, write

\[
 x_H={\bf1}+\sum_{j\in H}(e_j-e_{j+1}).
\tag{1.1}
\]

If both `c` and `c+1` may be inserted into `H`, put

\[
 x_c=x_{H\cup\{c\}},
 \qquad
 y_c=x_{H\cup\{c+1\}}.
\tag{1.2}
\]

Then `x_c-y_c` is a shifted-cut horizontal edge and `x_H` is its
deleted-cut hub.  The odd-circulation theorem supplies a petal

\[
                         {\cal B}(H,c)
\tag{1.3}
\]

consisting of an odd cycle through `x_c,x_H` and the tail edge
`x_Hy_c`.

There are two useful matching states of this petal.

* **Active state:** use `x_Hy_c` and perfectly match the odd cycle with
  `x_H` deleted.  This covers all petal vertices.
* **Passive state:** regard `x_H` as already matched elsewhere and match
  the cycle with `x_H` deleted.  This covers `x_c` and every circulation
  interior, leaving exactly `y_c` exposed.

Reversing the shifted edge exchanges the roles of `x_c,y_c`, so either
critical endpoint can be chosen as the exposed endpoint in the passive
state.

## 2. Compatible double expansions

Fix one literal hub `x_H`.  Let

\[
 e_i=x_{c_i}y_{c_i}\qquad(0\le i<d)
\tag{2.1}
\]

be pairwise endpoint-disjoint shifted-cut edges over that hub.

### Lemma 2.1 (joint admissibility)

For `i\ne j`, every cut chosen from `{c_i,c_i+1}` is jointly admissible
with every cut chosen from `{c_j,c_j+1}`.

#### Proof

If the two shifted edges occur in different gaps of `H`, each inserted cut
has both new gap parts at least four.  The old hub cut between the gaps
therefore separates the two inserted cuts by more than the required two
coordinates.

If they occur in the same merged gap, the split-fibre classification gives
blocks `P_2` or `P_3`.  Two edges in one `P_3` block share its middle
vertex, so endpoint-disjointness excludes that case.  Distinct split
blocks start six units apart; their two adjacent cut positions are
therefore at cyclic distance at least five.  Hence every cross-choice is
2-independent. \(\square\)

Choose `e_0` as the anchor.  For every `i>0`, choose an anchor cut

\[
                         a_i\in\{c_0,c_0+1\}
\]

and an exposed donor cut

\[
                         p_i\in\{c_i,c_i+1\}.
\]

Lemma 2.1 makes the double expansion

\[
                         z_i=x_{H\cup\{a_i,p_i\}}
\tag{2.2}
\]

legal.  The exposed donor endpoint `x_{H\cup\{p_i\}}` is adjacent to
`z_i` by insertion of `a_i`.

### Theorem 2.2 (one-hub fan promotion)

If the necklace orbits `[z_i]`, `1<=i<d`, are pairwise distinct and are
not otherwise occupied, then the union of the `d` circulation petals and
the `d-1` double expansions has a perfect matching.

#### Proof

Put the anchor petal in its active state.  This covers `x_H`, both anchor
endpoints, and its circulation interior.

Put every other petal in its passive state, oriented so that the endpoint
with cut `p_i` is exposed.  This covers its other endpoint and its entire
interior.  Finally use the edge

\[
                  x_{H\cup\{p_i\}}z_i
\tag{2.3}
\]

for every `i>0`.  Distinct receiver orbits make these edges disjoint.  The
fixed-level circulation injectivity theorem separates all nonhub petal
interiors; their only former collision was the common hub, which is used
only by the anchor tail.  Thus every vertex is covered exactly once.
\(\square\)

This theorem explains the correct meaning of hub capacity.  Reusing a hub
colour is not intrinsically impossible; each excess use consumes one
fresh critical state one cut level higher.

## 3. The exact receiver Hall graph

Now let `M_k` be any matching of critical necklace vertices having `k`
cuts.  Group its edges by their unpointed `(k-1)`-cut hub colour.  In every
nonempty group choose one anchor edge.  Make one **job** for every other
edge in that group.

For a job `j`, let `L_j` be the necklace orbits of all legal double
expansions (2.2), over all:

1. alignments of the job and anchor occurrences over a common literal hub;
2. two choices of anchor endpoint;
3. two choices of exposed donor endpoint;
4. exclusions imposed by protected sockets or already contracted banks.

Let `Z_k` be the set of admissible `(k+1)`-cut receiver orbits and form the
bipartite graph

\[
                         {\cal R}_k=(J_k,Z_k;E),
 \qquad jz\in E\iff z\in L_j.
\tag{3.1}
\]

All quotient coalescence is priced here: two pointed double expansions
which are rotations of one another are one right vertex, not two.

### Theorem 3.1 (fixed-level hub-capacity elimination)

Within the fan-promotion architecture of Theorem 2.2, the matching `M_k`
has a vertex-disjoint circulation lift using arbitrary hub multiplicities
and distinct next-level receivers if and only if `\mathcal R_k` has a
matching saturating `J_k`.  Equivalently, the exact condition is

\[
                         |N(X)|\ge |X|
 \qquad\text{for every }X\subseteq J_k.
\tag{3.2}
\]

#### Proof

Necessity is immediate: every excess petal leaves one donor endpoint after
the common hub is assigned to the anchor, and a physical receiver can be
used only once.

For sufficiency, choose an SDR of the lists `L_j`.  Apply Theorem 2.2 in
every hub group.  Different groups have different hub orbits.  At fixed
cut level, the nonhub circulation interiors are injective in their pointed
edge data, so petals from different groups do not collide.  The SDR
separates the receiver orbits.  Receiver states have `k+1` cuts, whereas a
nonhub circulation state from a `k`-cut endpoint has `k` or `k-1` zeroes;
hence a receiver cannot be a petal interior.  The resulting union is a
vertex-disjoint matching bank.  Hall's theorem gives (3.2). \(\square\)

Every uncontracted job has a nonempty pointed menu: before rotations and
external exclusions, Lemma 2.1 supplies all four endpoint choices.  This
does not by itself prove (3.2), because several pointed choices can
coalesce to one necklace receiver and receivers can be shared across
different hubs.

## 4. Interaction with the special reset

The special three-tail reset contracts two explicit hub colours.  Delete
from `M_k` every edge using either colour before forming (3.1), and delete
from `Z_k` every receiver already occupied by the reset.  Theorem 3.1 is
unchanged.  Thus the robust ordinary-sector problem has the exact
two-stage form

\[
 \boxed{
 \begin{array}{l}
 \text{choose critical edge matchings }M_k,\\
 \text{then satisfy the receiver Hall systems }{\cal R}_k
 \text{ after the reset contractions.}
 \end{array}}
\tag{4.1}
\]

The receiver is itself a critical `(k+1)`-cut state.  Therefore using it
must be coordinated with the matching chosen at level `k+1`; an
independent level-by-level solution can reopen its mate.  One needs either
a top-down alternating-ear order or one joint matching of all systems
(3.1).  This is the remaining regeneration issue, not a hidden failure of
the local fan promotion.

## 5. Corrected smallest repeated-colour witness

The formerly stated example over `(9,9,h)` did not have the same literal
deleted-cut hub.  A correct rooted witness is the hub

\[
                         (21,4,6),
\]

which supports the disjoint shifted-cut edges

\[
 (4,17,4,6)-(5,16,4,6),
 \qquad
 (10,11,4,6)-(11,10,4,6).
\tag{5.1}
\]

Theorem 2.2 absorbs this duplicate colour by choosing either endpoint cut
from the first split block, either endpoint cut from the second block, and
adjoining their legal double expansion.  The split positions are at least
five apart.

## 6. Scope

Proved:

1. every family of repeated petals over one literal hub has an exact fan
   matching after one receiver is supplied per excess petal;
2. all four pointed receiver choices are legal;
3. exact fixed-level reduction of arbitrary hub multiplicity to one
   ordinary bipartite Hall system on occurrence-coalesced receiver orbits;
4. compatibility of that reduction with the two contracted colours of the
   special reset.

Not proved:

1. Hall inequalities (3.2) for every ordinary capacity-two sector;
2. simultaneous use of a receiver at level `k+1` and the matching of that
   next level;
3. cross-level separation of all circulation interiors without a phased
   ear order;
4. preservation of one arbitrary radial/PBBS socket; or
5. the complete adjacent-necklace theorem.
