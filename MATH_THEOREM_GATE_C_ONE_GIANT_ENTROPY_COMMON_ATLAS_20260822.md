# Gate C: one giant block has factorial entropy but a subexponential atlas

**Status (2026-08-22).** Every assertion below is proved.  The simplest
unequal-block family really does evade the equal-block entropy obstruction:
one giant block and `S=Theta(b/log b)` singleton blocks give
`S!=exp(Theta(b))` distinct block orders, every one meeting the fixed factor
in `q-o(q)` flags.

Nevertheless the family is unusable for packing.  All of its giant-block
flags draw their middle targets from an atlas of size at most

\[
                              b^2 2^S.                 \tag{0.1}
\]

Thus any rankwise-target-disjoint subfamily has size at most
`exp(O(S))=exp(o(b))`, far below the required
`Theta(binomial(2b,b)/b^2)` tours.  Local factorial parameter entropy is not
macroscopic support diversity.

## 1. The family

Let `b` be odd and let `S` be even with

\[
                         2\le S<b,\qquad L=b-S.        \tag{1.1}
\]

Partition the residue circle `Z_b` into the giant domain block

\[
                         D_0=\{0,...,L-1\}             \tag{1.2}
\]

and the `S` singleton blocks `D_j={L+j-1}`, `1<=j<=S`.  The number of
blocks `K=S+1` and every block length are odd.

In the target circle, keep the giant block first, occupying
`T_0={0,...,L-1}`, and put the singleton blocks in an arbitrary order
`eta in S_S` on the remaining coordinates.  Map every block increasingly
to its target interval and take the corrected antipodal lift

\[
 \epsilon_x=\alpha(x)+x\pmod2,qquad
 \pi(x)=\alpha(x)+b\epsilon_x,qquad
 \pi(x+b)=\pi(x)+b\pmod{2b}.                           \tag{1.3}
\]

Different singleton orders give different coordinate maps, so this
normalized family has exactly

\[
                              S!                       \tag{1.4}
\]

labelled members.

## 2. Every order has coefficient-one overlap

For the giant root, list the singleton blocks in target order and let
`w(u) in {+1,-1}` be their unequal-block signs.  Its weighted prefix walk
has unit weights:

\[
 P(0)=0,qquad P(m)=\sum_{u=1}^m w(u),qquad A=P(S).    \tag{2.1}
\]

Define

\[
 \lambda=-\min_mP(m),qquad
 \upsilon=\max_m\{P(m)-A\}.                            \tag{2.2}
\]

Since every prefix and every complementary suffix contains at most `S`
unit signs,

\[
                         0\le\lambda,\upsilon\le S.    \tag{2.3}
\]

The unequal-block weighted-excursion theorem says that every giant-row
offset

\[
                 \upsilon+1\le s\le L-\lambda-3       \tag{2.4}
\]

is deep and supplies exactly `b-2` factor flags.  Consequently every
singleton order has at least

\[
 \boxed{D_S:=(b-2)[b-3S-3]_+}                         \tag{2.5}
\]

factor flags coming from giant rows.  If `M_eta` is its full factor
intersection and `q=b(b-1)`, then

\[
 q-M_\eta\le q-D_S=O(b(S+1)).                          \tag{2.6}
\]

In particular `S=o(b)` gives `M_eta=q-o(q)` uniformly over all `S!`
orders.

Now choose

\[
                         S={c b\over\log b}+O(1)       \tag{2.7}
\]

to be even, for any fixed `c>0`.  Stirling's formula gives

\[
                         \log(S!)=(c+o(1))b.           \tag{2.8}
\]

Thus `c>log 4` produces more than `4^b/poly(b)` labelled local candidates,
while (2.6) still has relative loss `O(1/log b)`.

## 3. The common middle-target atlas

Fix a giant interior row `r=s`, `1<=s<L`.  Its undeleted set is

\[
                         U_{\eta,s}=\{\pi(s),...,\pi(s+b)\}.          \tag{3.1}
\]

The giant block map is the identity.  Hence the part of (3.1) on the two
antipodal copies of `T_0` is independent of `eta`.  Every singleton domain
coordinate is also present in the interval `s,...,s+b`; its image has one
of the two antipodal lifts of one coordinate in the fixed target set

\[
                         R=\{L,...,b-1\},\qquad |R|=S. \tag{3.2}
\]

Because the singleton map is a bijection onto `R`, the variable part of
`U_{eta,s}` chooses exactly one member of every antipodal pair
`{y,y+b}`, `y in R`.  Therefore

\[
             |\{U_{\eta,s}:\eta\in S_S\}|\le2^S.       \tag{3.3}
\]

An internal factor flag in row `s` has middle target obtained by deleting
one of at most `b-1` selected coordinates from `U_{eta,s}`.  Let `A_S` be
the union, over all singleton orders and all giant rows, of these middle
targets.  From (3.3),

\[
 \boxed{|\mathcal A_S|\le(L-1)(b-1)2^S<b^2 2^S.}       \tag{3.4}
\]

### Theorem 3.1 (packing obstruction)

If `b>3S+3` (equivalently `D_S>0`), any collection of the **full factor
intersections** of these tours whose flags are rankwise-target-disjoint has
size at most

\[
 \boxed{{|\mathcal A_S|\over D_S}\le {b^2 2^S\over D_S}.}         \tag{3.5}
\]

#### Proof

Each tour contains at least `D_S` giant-row factor flags by (2.5), and
their middle targets all lie in `A_S`.  These targets are distinct within
one coherent tour: in the canonical tour they are indexed by the ordered
pair consisting of its empty and doubled coordinate pairs, and the
coordinate permutation preserves distinctness.  Rankwise target
disjointness makes the target sets disjoint between selected tours.
Counting them proves (3.5). \(\square\)

There are at most `(S+1)(b-1)=O(bS)` flags outside giant interior rows.
Thus, if `S=o(b)`, the same atlas obstruction applies when flags may be
discarded arbitrarily but each selected tour must retain `q-o(q)` flags.
Indeed each retained support then contains at least

\[
                  q-o(q)-(S+1)(b-1)=(1-o(1))q          \tag{3.6}
\]

giant-row middle targets from `A_S`.  Rankwise disjointness therefore
bounds the number of selected supports by `|A_S|/((1-o(1))q)`.

For (2.7), one has `D_S=(1-o(1))b^2`, while

\[
                 \log\left({b^22^S\over D_S}\right)
                 =O(S)=O(b/\log b)=o(b).               \tag{3.7}
\]

On the other hand the required number of tours has logarithm

\[
 \log\left({\binom{2b}{b}\over b(b-1)}\right)
 =b\log4-O(\log b).                                   \tag{3.8}
\]

Thus the family has enough labels but exponentially too few disjoint
supports.

## 4. Scope

The obstruction uses one fixed giant domain/target interval.  Allowing its
cyclic origin or reversing the construction changes the atlas by only a
polynomial factor and does not alter (3.6).  The theorem does not rule out
several macroscopic blocks, recursively shifted block boundaries, or a
genuinely multiscale family in which the variable target atlas itself has
`exp((log4+o(1))b)` size.

The companion checker
`scratch/verify_gate_c_one_giant_entropy_common_atlas_20260822.py` builds
every small singleton order directly, checks the uniform deep-row bound,
and verifies the target-atlas estimate.
