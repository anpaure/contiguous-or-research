# Audit of the adaptive bulk reciprocal-`C_8` multilayer atlas

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_C8_ADAPTIVE_BULK_MULTILAYER_ATLAS_20260726.md`.

Method: independent symbolic proof audit.  No finite search, computation,
solver, or web input is used.

## 0. Verdict

The corrected report passes.

For every fixed `u in {4,5,6,7}` it constructs a literal Boolean atlas of
anchored exact factors with

\[
 M_{r,u}=2^{u-1}\left\lfloor {C_{r-2}\over2^{u-1}}\right\rfloor
        =C_{r-2}+O_u(1)
        =\left({1\over16}+o(1)\right)C_r             \tag{0.1}
\]

reciprocal `C_8` packets in every layer.  Its old/all-on ownership
components have shore size at most `2^u<=128`, and its exact constants are

\[
 \chi_r\longrightarrow1+{2^u-1\over8},
 \qquad
 \Xi_r\longrightarrow u2^{u-2}.                     \tag{0.2}
\]

The full signed carrier calculation also passes.  The construction does
not pass the critical-root hinge gate: for fixed `u`, its complete weighted
half-`l_1` action through `H=O(sqrt(m))` is `o(W_m)`.

One subtle correction is essential.  A single suspension `J(x)=1x0`
does **not** by itself kill first deletion.  It kills first insertion and
turns the local last-deletion flag into first deletion.  The atlas's
first-deletion flag vanishes only because its quantile-selected six-bit
blocks are strictly nonprefix bulk blocks.  The audited report now gives
the necessary four-boundary recursion and states the exceptional prefix
family explicitly.

## 1. The local object is a completed factor trade

The two old lower-state rows are

\[
 12,14,34,
 \qquad
 13,23,24,                                           \tag{1.1}
\]

and the two new rows are

\[
 12,23,34,
 \qquad
 13,14,24.                                           \tag{1.2}
\]

Both sides own the six lower states

\[
                 12,13,14,23,24,34                  \tag{1.3}
\]

once.  Their adjacent unions are, respectively,

\[
 124,134,123,234
 \quad\hbox{and}\quad
 123,234,134,124,                                    \tag{1.4}
\]

so both sides own exactly `123,124,134,234`.  The initial roots and
terminal complements agree rowwise.  Thus this is a sealed two-row
rooted port-factor trade, not merely an open incidence cycle.

On each row, the old and new flip words differ by one adjacent
transposition in the insertion list and one in the deletion list.  Hence

\[
                         d(P)=d(Q)=2.                \tag{1.5}
\]

The rooted one-hole context theorem transports the two equal ledgers
injectively and fixes both external ports.  It therefore makes every
contextual copy literal.

## 2. The adaptive bulk supply is exponentially full

Put

\[
 A=J(1100)=111000,
 \qquad
 B=J(1010)=110100.                                  \tag{2.1}
\]

Equal-size fringe subtrees are disjoint.  Toggling one `A/B` filling
preserves the complete ordered `A/B` occurrence list: the toggled root is
still size three, its descendants have size below three, its strict
ancestors have size above three, and disjoint subtrees do not change.

If `N(T)` is the number of these occurrences, the marking equation is

\[
 \mathcal T(z,y)=1+z\mathcal T(z,y)^2+2(y-1)z^3
 ={1-\sqrt{1-4z+8(1-y)z^4}\over2z}.                \tag{2.2}
\]

This equation is exact: the two marked size-three trees have no proper
size-three fringe occurrence, so replacing their ordinary weight `z^3`
by `yz^3` adds exactly `2(y-1)z^3`.

For `0<y<1`, the positive singular radius `rho(y)` exceeds `1/4`.
Choose `R` with `1/4<R<rho(y)`.  Coefficient positivity gives

\[
 \sum_{T\in D_r}y^{N(T)}
       \le \mathcal T(R,y)R^{-r}.                   \tag{2.3}
\]

If `N(T)<delta r`, then `y^{N(T)}>=y^(delta r)`.  Choosing `delta>0`
with `4Ry^delta>1` and dividing (2.3) by
`C_r~4^r/(sqrt(pi)r^(3/2))` proves

\[
 |{T:N(T)<\delta r}|=O(\lambda^r C_r)             \tag{2.4}
\]

for some `lambda<1`.

For a good tree, take

\[
             j_i(T)=\left\lceil {iN(T)\over u+1}\right\rceil,
             \qquad1\le i\le u.                    \tag{2.5}
\]

The chosen indices are toggle-invariant.  Consecutive indices and both
ends have at least `N/(u+1)-2` intervening occurrences.  Because those
occurrences are disjoint six-bit blocks, every selected block is
separated from the others and from both word ends by

\[
                   {3\delta r\over u+1}-O(1).       \tag{2.6}
\]

Thus the word positions are genuinely bulk; the construction is not the
fixed complete-prefix family counted by `C_aC_(r-a-2)`.

## 3. Exactness and commutation of the full factor cube

The selected toggles act freely and partition the good roots into
`2^u`-orbits.  Hence the number of available orbits is

\[
                         {C_r-o(C_r)\over2^u}.       \tag{3.1}
\]

The report uses only

\[
 L_{r,u}=\left\lfloor {C_{r-2}\over2^{u-1}}\right\rfloor
       \sim {C_r\over2^{u+3}},                       \tag{3.2}
\]

an asymptotic factor eight below the supply in (3.1).

There are two distinct exactness checks.

First, on one rooted row, the selected size-three subtrees occupy
disjoint phase slabs.  Each local shore has the same slab endpoints.
Choosing either slab path therefore still concatenates to a geodesic with
the original root and complement, and the choices commute rowwise.

Second, ledger equality is checked on pairs of roots, not on a single
row.  Fix coordinate `i` and all other slot choices.  Pair the roots of a
Boolean orbit along its `i`-edges.  The other fillings and other slab
variants agree inside each pair, so they form common exterior material.
The local reciprocal packet, including its two collars, preserves the
pair's aggregate lower-state and adjacent-union ledgers.  The
`2^(u-1)` pairs partition the orbit.  Thus an `i`-switch preserves the
complete orbit ledger.  Successive coordinate switches prove that every
`F^eta` is an anchored exact factor and that the partial involutions
commute through full ownership.

This is a genuine joint recombination proof.  It does not invoke the
automatic root-disjoint-packet theorem on overlapping coordinate layers;
within a fixed layer the packet pairs are root-disjoint, while across
layers their compatibility is supplied by the disjoint-slab argument.

## 4. Exact component structure and constants

In one selected orbit, common root ports connect identical roots on the
two shores.  For a fixed other-bit mask, the contextual images of local
states `14` and `23` cross-connect the two roots which differ in bit `i`.
Thus every Boolean axis is present in the old/all-on overlay, and the
orbit overlay is connected.

Successive sealed-packet equalities show that the complete token multiset
owned by an orbit is the same on both shores.  No ownership edge can leave
the orbit.  Exterior port closure adds only same-root diagonal edges, so
it cannot join two selected orbits.  Therefore there are exactly
`L_(r,u)` nontrivial components of shore size `2^u`; all remaining roots
give singleton components.

With `R_(r,u)=2^uL_(r,u)`, this gives

\[
 \chi_r
 ={C_r-R_{r,u}+4^uL_{r,u}\over C_r}
 =1+(2^u-1){R_{r,u}\over C_r}
 \longrightarrow1+{2^u-1\over8}.                   \tag{4.1}
\]

The limits for `u=4,5,6,7` are

\[
                {23\over8},\quad {39\over8},
                \quad {71\over8},\quad {135\over8}. \tag{4.2}
\]

Every active row has `u` local edits, hence distance `2u`.  Under the
report's size-biased edit moment normalization,

\[
 \Xi_r={2u4^uL_{r,u}\over C_r}
       \longrightarrow u2^{u-2},                    \tag{4.3}
\]

namely `16,40,96,224`.  All component sizes and moments are bounded in
`r` for fixed `u`.

## 5. Complete carrier and the boundary subtlety

For one packet, put

\[
 \partial_\beta^\gamma H
 =e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.
\]

The occurrence-resolved carrier at every proper depth is

\[
 \Delta_q=
   \partial_\beta^\gamma\operatorname{suf}(O)
  +\partial_\beta^\gamma\operatorname{suf}(E)
  -\partial_\beta^\gamma\operatorname{pre}(E)
  -\partial_\beta^\gamma\operatorname{pre}(O).      \tag{5.1}
\]

This includes both cyclic collars.  At depth one, collisions reduce it
to a four-cell vector of half-`l_1` norm two.  At every other depth its
half-`l_1` norm is at most four.  Telescoping the commuting layers gives,
for every component child,

\[
 {1\over2}\|\Delta\mu_1\|_1\le2uM_{r,u},
 \qquad
 {1\over2}\|\Delta\mu_q\|_1\le4uM_{r,u}.           \tag{5.2}
\]

The cap sign is not uniformly favourable.  At a flat four-cell cap, both
orientations create cost two; at a flat generic eight-cell depth, both
create cost four.  Relabelling or context conjugation transports all four
arms of (5.1) and cannot reverse only the exit arms.

The exact local boundary signature is

\[
          (\Delta FI,\Delta FD,\Delta LI,\Delta LD)
                  =(v,v,-v,-v),\qquad v=e_3-e_2.    \tag{5.3}
\]

Under one suspension it becomes

\[
                            (0,-Sv,Sv,0),            \tag{5.4}
\]

where `S` shifts the local labels.  In particular a top-level suspended
packet has nonzero first-deletion transfer.  The unary operations act by

\[
\begin{array}{c|c}
x\mapsto xB &(FI,FD,0,0),\\
x\mapsto Ax &(0,0,LI,LD),\\
x\mapsto J(x)&(0,LD,FI,0),
\end{array}                                          \tag{5.5}
\]

for nonempty `A,B`, up to the fixed coordinate injection.  Starting from
(5.4), first deletion survives precisely when every remaining outer
operation is a right concatenation.  Equivalently the whole six-bit
suspended atom is the prefix `J(core)` in `J(core)B`.  Such packets form
the exact exceptional family of size `C_(r-3)`.

Every quantile-selected atlas block is `Omega_u(r)` positions from the
left end and therefore is not in this prefix family.  Thus the atlas,
though not every suspended atom, satisfies

\[
                    \Delta I_{\rm root}
                    =\Delta D_{\rm root}=0.          \tag{5.6}
\]

### Mixed layer interactions

Each layer bit acts on an active row through two adjacent transpositions,
and the `2u` swap cuts are distinct.  A cyclic interval can see a swap
only at one of its two boundary cuts.  Therefore each row/start target
depends on at most two layer bits; its multilinear Boolean degree is at
most two.

For fixed bits `i,j`, choose one of the two cuts belonging to each bit
(four choices), then one of the two oriented arcs bounded by those cuts.
There are at most eight intervals which depend on both bits.  A mixed
second difference of four one-hot vectors has half-`l_1` norm at most two,
so

\[
       \sum_q{1\over2}\|\Delta_i\Delta_j\mu_q(P)\|_1\le16.
                                                               \tag{5.7}
\]

For fixed `u`, all mixed interaction terms therefore total `O_u(C_r)`,
not `Theta(W_r)`.  This confirms that the collars do not hide a growing
multilinear amplification.

## 6. Ambient normalization and implication scope

At local rank, for `H_r=ceil(A sqrt(r))` and
`S_(H_r)=sum_(q<=H_r)1/c_q`, the exact baseline has `c_1=1` and all
`c_q>=1`.  From (5.2),

\[
 {1\over2}\sum_{q\le H_r}{\|\Delta\mu_q\|_1\over c_q}
 \le(4S_{H_r}-2)uM_{r,u}
 =O_A(uC_r\sqrt r)=o(W_r).                           \tag{6.1}
\]

For a first-size-`r` fringe lift to rank `m`, the nonavoiding roots split
into exact classes of size `C_r`.  If `a_(m,r)` is the avoiding count, the
number of classes is

\[
                   {C_m-a_{m,r}\over C_r}\le {C_m\over C_r}.   \tag{6.2}
\]

An ambient adjacent transposition changes at most two starts at any proper
interval length, even when `q>r`; two transpositions per reciprocal row
therefore retain the per-packet bounds two at `q=1` and four at every
other depth, collars included.  Consequently, for
`r=Theta(sqrt(m))` and `H=ceil(A sqrt(m))`, every component child obeys

\[
 {1\over2}\sum_{q\le H}{\|\Delta\mu_q\|_1\over c_q}
 \le {C_m\over C_r}(4S_H-2)uM_{r,u}
 \le\left({u\over4}+o_u(1)\right)C_mS_H
 =O_A\left({uW_m\over\sqrt m}\right)=o(W_m).        \tag{6.3}
\]

This action estimate controls weighted balanced overload and every other
specified half-`l_1`-Lipschitz carrier functional.  It must not be stated
as an obstruction to an arbitrary unnamed defect.  Within the intended
constant-one hinge lane, however, it is decisive: an atlas with only
`2u=O(1)` adjacent inversions per active row cannot produce the required
`Omega(W_m)` physical action.

## 7. Final audited boundary

The positive theorem is genuine: adaptive occurrence ranks evade the
fixed-position Catalan ceiling and give four through seven commuting
`C_r/16`-density layers with literal completion and bounded ownership
components.

The first exact failure is also genuine.  Packet density counts local
reciprocal trades, not aligned parent-boundary carrier units.  For the
bulk atlas both root entrance flags vanish, the remaining four-arm carrier
has no background-independent favourable sign, and its total all-depth
action is `o(W)`.  A viable successor must introduce a growing number of
physically active seams per row, or a genuinely nonlocal packet which
moves `Theta(r)` starts while keeping its full port-closed overlay bounded.

