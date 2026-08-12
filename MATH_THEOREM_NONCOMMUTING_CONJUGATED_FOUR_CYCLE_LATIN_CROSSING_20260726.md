# A noncommuting four-cycle Latin crossing with literal trace transport

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

There is an exact local escape from the fixed-matching commuting
obstruction.  It is not an independently programmable pair-by-pair
crossing.  Its minimal proved granularity is one four-cycle label cell.

Choose three coordinate directions `a,b,c` having the same syndrome and
put

\[
 \tau=(a\ b),\qquad \rho=(b\ c),\qquad
 \upsilon=\rho\tau\rho^{-1}=(a\ c),                 \tag{0.1}
\]

with displacement vectors

\[
 \delta=e_a+e_b,\qquad \gamma=e_b+e_c,\qquad
 \zeta=e_a+e_c=\delta+\gamma.                       \tag{0.2}
\]

The coordinate transpositions do not commute.  Nevertheless, on every
coset of

\[
                         H=\langle\delta,\gamma\rangle,          \tag{0.3}
\]

the following operation is legal:

1. start with arbitrary, independently chosen `tau`-shore bits on the two
   `delta`-pairs in the coset;
2. conjugate all four cycles in the coset by `rho`; and
3. regard the two transported bits as independent `upsilon`-shore bits on
   the two `zeta`-pairs.

Every `H`-coset is a disjoint owner cell, so the conjugation bit can be
chosen independently on every cell.  The input-to-output map on the two
switch slots is a bijection.  Thus this is a genuine cycle-level Latin
crossing

\[
                         S\longmapsto RSR^{-1},                   \tag{0.4}
\]

not a commuting square with the old matching.

The crossing is literal at every signed depth.  For every consecutive
window `X_0,...,X_q`,

\[
 \bigcap_{j=0}^q\rho X_j=\rho\!\left(\bigcap_{j=0}^qX_j\right),
 \qquad
 \bigcup_{j=0}^q\rho X_j=\rho\!\left(\bigcup_{j=0}^qX_j\right).  \tag{0.5}
\]

Consequently the construction transports the actual Boolean lower and
upper targets, preserves their ranks, preserves chronology, and preserves
trace injectivity inside each cell.  An orientation-packet embedding turns
`rho` into an actual permutation of the physical coordinate pairs, so
(0.5) is not a formal direction-word identity.

There are two sharp qualifications.

* If the conjugator is refined to independent bits on the two
  `gamma`-pairs, the exact phasewise Latin condition admits only ten of the
  sixteen formal two-layer states.  Hence no Cartesian pair-granular Latin
  crossing exists in this local bank.  The four-cycle move is essential.
* Independent cellwise coordinate images need not have disjoint target
  ranges in different cells.  Formula (5.6) below is the exact remaining
  cross-cell trace condition.  Moreover a nontrivial crossing cannot be
  trace-*invisible* inside one split-pair packet: equality of the lower
  depth-one target multiset already fixes the edge set.

Thus the local conjugated crossing theorem is positive.  What remains
open is a composition theorem for overlapping four-cycle cells together
with cross-cell target separation.  The theorem does not by itself give a
rearrangeable Beneš network or coefficient one.

## 1. Syndrome-cycle setting

Let

\[
                         V=\mathbb F_2^h                         \tag{1.1}
\]

and let `Psi:V -> A` be a syndrome map whose prefix syndromes are a
transversal.  Write

\[
 p_0=0,\qquad p_i=e_0+\cdots+e_{i-1}\quad(0\le i<h),             \tag{1.2}
\]

and let

\[
 P=(p_0,p_1,\ldots,p_{h-1},
       {\bf1}+p_0,{\bf1}+p_1,\ldots,{\bf1}+p_{h-1})             \tag{1.3}
\]

be the standard doubled-permutation cycle.  Put `K=ker(Psi)`.

Assume that `a,b,c` have one common syndrome column.  Then the vectors in
(0.2) lie in `K`, and every permutation of `a,b,c` preserves `Psi`.
Since `H` consists of the even vectors supported on `{a,b,c}`, we have
`1 notin H` as soon as there is a spectator coordinate.  Choose

\[
 \eta:K\longrightarrow\mathbb F_2,
 \qquad \eta({\bf1})=1,
 \qquad \eta(H)=0,                                  \tag{1.4}
\]

and set

\[
                         K_0=\ker\eta.                            \tag{1.5}
\]

Then

\[
                         K=K_0\oplus\langle{\bf1}\rangle,
\]

and the cycles

\[
                         P+k\qquad(k\in K_0)                    \tag{1.6}
\]

factor `V` exactly.

Every `sigma in <tau,rho> = S_{\{a,b,c\}}` has

\[
 \sigma x+x\in H,\qquad
 \sigma p_i+p_i\in H,
 \qquad \eta(\sigma x)=\eta(x).                    \tag{1.7}
\]

The first two statements hold because each difference is an even vector
supported on `{a,b,c}`; the third follows from (1.4).

For a coset `Q=k+H` in `K_0/H`, define its phase-complete owner cell

\[
 \mathcal O_Q=
 \bigcup_{i=0}^{h-1}
 \bigl((p_i+Q)\mathbin{\dot\cup}({\bf1}+p_i+Q)\bigr).           \tag{1.8}
\]

The cells `O_Q` are pairwise disjoint, each has `8h` owners, and they
partition `V`.  Equation (1.7) also gives

\[
                         \sigma\mathcal O_Q=\mathcal O_Q          \tag{1.9}
\]

for every `sigma in S_{\{a,b,c\}}`.  Notice that the cell is fixed
setwise, not sent to another cell.

## 2. The entering matching and its independent controls

Let

\[
 \epsilon:K_0\longrightarrow\mathbb F_2,
 \qquad
 \epsilon(k)=\epsilon(k+\delta).                    \tag{2.1}
\]

The associated cycle-label involution is

\[
                 S_\delta^\epsilon(k)=k+\epsilon(k)\delta.      \tag{2.1a}
\]

Pair constancy in (2.1) is exactly the identity
`(S_delta^epsilon)^2=1`; its nontrivial orbits are the selected switch
components.

Define

\[
                         C_k^\epsilon=\tau^{\epsilon(k)}P+k.     \tag{2.2}
\]

The literal pair-layer lemma says that

\[
                         \mathcal F_\epsilon
                   =\{C_k^\epsilon:k\in K_0\}                  \tag{2.3}
\]

is an exact isometric cycle factor.  On a `delta`-pair
`{k,k+delta}`, either both rows are unchanged or both are conjugated by
`tau`; at every phase the two new owners either equal or exchange the two
old owners.  Hence the two shores partition the same `4h` owners.

Each four-point cell `Q` contains exactly two `delta`-pairs.  Condition
(2.1) leaves their two bits arbitrary and independent.  The restriction
of (2.3) to `O_Q` is therefore a four-cycle factor for every one of the
four bit patterns.

## 3. Four-cycle conjugated crossing theorem

Choose an arbitrary cell field

\[
                         r:K_0/H\longrightarrow\mathbb F_2.     \tag{3.1}
\]

On one cell put

\[
 \mathcal F_{\epsilon,r}|_{\mathcal O_Q}
   =\rho^{r(Q)}\bigl(\mathcal F_\epsilon|_{\mathcal O_Q}\bigr), \tag{3.2}
\]

where `rho` acts on every actual owner of every cycle.

### Theorem 3.1 (noncommuting four-cycle Latin crossing)

For all fields `epsilon` and `r` satisfying (2.1) and (3.1):

1. `F_(epsilon,r)` is an exact factor of `V` into isometric `C_(2h)`'s;
2. every cell choice `r(Q)` is independent of every other cell choice;
3. on a crossed cell the entering `delta`-matching is transported
   bijectively to the outgoing `zeta`-matching;
4. the two entering shore bits remain independent outgoing shore bits;
5. all four corner factors have one common phase partition, and the
   conjugation preserves the phase index and antipodal pairing.

#### Proof

The restriction `F_epsilon|O_Q` partitions `O_Q` by Section 2.
Equation (1.9) says that `rho` is a bijection of this same owner cell.
Therefore both choices in (3.2) partition exactly `O_Q`.  The cells are
disjoint, so their choices may be made independently and their union is
an exact factor.  Coordinate permutations take doubled-permutation cycles
to doubled-permutation cycles, proving isometry.

Conjugation gives

\[
             \rho\tau\rho^{-1}=\upsilon,
 \qquad      \rho\delta=\zeta.                       \tag{3.3}
\]

Thus

\[
 \rho\{k,k+\delta\}
   =\{\rho k,\rho k+\zeta\}.                         \tag{3.4}
\]

Since `rho` is a permutation of `Q`, (3.4) is a bijection from the two
edges of the entering perfect matching to the two edges of the outgoing
perfect matching.  If

\[
                 \epsilon^\rho(\rho k)=\epsilon(k),              \tag{3.5}
\]

then (2.1) and (3.4) imply

\[
                 \epsilon^\rho(l)=\epsilon^\rho(l+\zeta).       \tag{3.6}
\]

Hence the two independent entering bits are exactly the two independent
outgoing bits, merely transported to new slots.  This is the Latin
property.

Finally, (1.7) shows that every coordinate permutation in question keeps
`p_i+Q` and `1+p_i+Q` setwise.  It therefore preserves the phase index.
It also fixes `1` and hence commutes with antipodal complementation. □

The local table is especially transparent if

\[
                         Q=x+\{0,\delta,\gamma,\zeta\}.           \tag{3.7}
\]

The entering and outgoing matchings are

\[
\begin{aligned}
 \mathcal M_\delta(Q)
   &=\{\{x,x+\delta\},\{x+\gamma,x+\zeta\}\},\\
 \mathcal M_\zeta(Q)
   &=\{\{\rho x,\rho x+\zeta\},
        \{\rho x+\gamma,\rho x+\delta\}\}.
                                                               \tag{3.8}
\end{aligned}
\]

Both rows of (3.8) partition all four roots once.  The map induced by
`rho` uses every input and every output switch slot once, which is the
two-slot Latin resolution.

Equivalently, on each cell the payload map is a permutation of
`F_2^2`: all four entering two-bit shore patterns occur once among the
four outgoing patterns.  In the standard syndrome factor, if

\[
                         N=|K_0|={2^h\over2h},
\]

then the layer has exactly `N/4` independent conjugation bits and carries
exactly `N/2` independently chosen entering switch bits to `N/2` outgoing
switch bits.  No payload bit is identified or discarded.

## 4. The exact conjugation square

The theorem can be displayed as a square of literal factor restrictions:

\[
\begin{array}{ccc}
 \mathcal F_0|_{\mathcal O_Q}
   &\xrightarrow{\ S_\delta^\epsilon\ }&
 \mathcal F_\epsilon|_{\mathcal O_Q}\\[2mm]
 \big\downarrow\rho^{r(Q)}&&\big\downarrow\rho^{r(Q)}\\[2mm]
 \rho^{r(Q)}\mathcal F_0|_{\mathcal O_Q}
   &\xrightarrow{\ S_{\rho^{r(Q)}\delta}^{\epsilon^{\rho^{r(Q)}}}\ }&
 \rho^{r(Q)}\mathcal F_\epsilon|_{\mathcal O_Q}.
                                                               \tag{4.1}
\end{array}
\]

For `r(Q)=1`, the lower switch is `S_zeta`, not `S_delta`.
Equation (4.1) is precisely

\[
                  S_\zeta^{\epsilon^\rho}
                    =R S_\delta^\epsilon R^{-1}.                \tag{4.2}
\]

Indeed, on a root `l`, the right side equals

\[
 \rho\bigl(\rho^{-1}l+\epsilon(\rho^{-1}l)\delta\bigr)
     =l+\epsilon^\rho(l)\zeta.                                  \tag{4.3}
\]

Because `tau rho != rho tau`, this square does not satisfy the
fixed-matching commutation law.  The orbit-rank theorem for commuting
fixed matchings therefore does not apply to this single crossing.

There is an important granularity point.  The vertical arrows in (4.1)
are four-cycle owner trades on `O_Q`.  They need not decompose into two
independently chosen old `gamma`-pair trades after an arbitrary entering
bit pattern.  Section 6 proves that such a refinement is impossible.

## 5. Literal trace theorem and packet lift

For a consecutive window

\[
                         W=(X_0,X_1,\ldots,X_q)                   \tag{5.1}
\]

write

\[
 L_q(W)=\bigcap_{j=0}^qX_j,
 \qquad
 U_q(W)=\bigcup_{j=0}^qX_j.                         \tag{5.2}
\]

### Theorem 5.1 (simultaneous literal trace transport)

On every crossed cell and for every `q`,

\[
 L_q(\rho W)=\rho L_q(W),
 \qquad
 U_q(\rho W)=\rho U_q(W).                           \tag{5.3}
\]

The occurrence map

\[
 (Q,C,i,q,\pm)\longmapsto
 (Q,\rho C,i,q,\pm)                                 \tag{5.4}
\]

is a bijection and carries the old literal target to its coordinate image.
It preserves target rank, return-freeness, phase, sign, and all nesting
relations between depths.

#### Proof

A coordinate permutation commutes with intersection, union, cardinality,
and inclusion.  It maps consecutive vertices of a cycle to consecutive
vertices of the image cycle without changing their phase indices.  This
proves every assertion simultaneously. □

In particular, if `T_(q,sign)(Q)` denotes the target occurrence multiset
of one cell, then the exact global ledger is

\[
 \boxed{
 \mathcal T_{q,\pm}(\mathcal F_{\epsilon,r})
  =\mathop{\biguplus}_{Q\in K_0/H}
       \rho^{r(Q)}\mathcal T_{q,\pm}
          (\mathcal F_\epsilon|_{\mathcal O_Q}).}                \tag{5.5}
\]

This is stronger than a word or profile identity: every term is an actual
Boolean target.

For completeness, (5.5) also isolates what the theorem does not give.
Arbitrary cell choices preserve global target injectivity if and only if,
for every two distinct cells `Q,Q'` and every `e,e' in {0,1}`,

\[
 \rho^e\operatorname{supp}\mathcal T_{q,\pm}(Q)
 \ \cap\
 \rho^{e'}\operatorname{supp}\mathcal T_{q,\pm}(Q')
                         =\varnothing,                            \tag{5.6}
\]

together with injectivity inside each transformed cell.  For one fixed
field `r`, only the corresponding choice `e=r(Q),e'=r(Q')` is needed.
Thus (5.6) is the exact collision criterion for fully independent crossing
bits; owner Latinness alone does not imply it.

### Physical orientation-packet lift

Let the Boolean axis `i` be represented by a physical coordinate pair

\[
                         E_i=\{x_i^0,x_i^1\},                     \tag{5.7}
\]

and let a packet owner choose exactly one endpoint from every `E_i`, with
all exterior coordinates fixed.  Lift `rho` by

\[
             x_i^s\longmapsto x_{\rho(i)}^s
             \qquad(s\in\{0,1\}),                               \tag{5.8}
\]

fixing the exterior.  This physical coordinate permutation preserves the
packet owner set and satisfies

\[
                         \widehat\rho\,\iota(x)=\iota(\rho x),   \tag{5.9}
\]

where `iota` is the orientation-cube embedding.  Therefore Theorems 3.1
and 5.1 lift verbatim to actual middle owners and to their actual lower
and upper Boolean targets.  Spectator coordinates simply pass unchanged
through every formula.

## 6. Sharp pair-granular no-go

The four-cycle granularity cannot be replaced by the Cartesian product of
the two elementary pair banks.

Fix one `H`-coset and use coordinates `(u,v) in F_2^2`, where adding
`delta` toggles `u` and adding `gamma` toggles `v`.  Pair constancy for
two successive elementary layers has the form

\[
 \epsilon_1(u,v)=A(v),
 \qquad
 \epsilon_2(u,v)=B(u).                              \tag{6.1}
\]

The resulting row field is

\[
                         \sigma_{u,v}
                  =\rho^{B(u)}\tau^{A(v)}.                       \tag{6.2}
\]

At the prefix phase `100` on the three selected coordinates, the exact
owner-label map is

\[
 (u,v)\longmapsto
       (u+A(v),\ v+A(v)B(u)).                         \tag{6.3}
\]

At the prefix phase `110`, it is

\[
                         (u,v)\longmapsto(u,v+B(u)).             \tag{6.4}
\]

The second map is always bijective under pair constancy.  The first is
bijective exactly when

\[
 \boxed{A(0)=A(1)\quad\hbox{or}\quad B(0)=B(1)=0.}               \tag{6.5}
\]

Indeed, if `A` is nonconstant, the line on which `A=0` is fixed; any
nonzero value of `B` sends a point of the other line onto one of these
fixed points.  If `B=0`, or if `A` is constant, (6.3) is visibly a
permutation.

There are eight legal states with `A` constant and arbitrary `B`, and two
more with `A` nonconstant and `B=0`: ten of sixteen.  A pair-granular Latin
crossing with independent controls would require all sixteen states.
Therefore it does not exist in the elementary two-layer bank.

Theorem 3.1 escapes (6.5) in exactly one way: it transports the whole
four-root cell, reindexes its roots by `rho`, and changes the outgoing
matching from `delta` to `zeta`.  It does not pretend that the vertical
cell trade is two independent fixed-root `gamma`-pair trades.

The adjacent triple is also the smallest noncommuting coordinate model.
Disjoint coordinate transpositions commute.  Two transpositions sharing
one coordinate conjugate to the third edge of the triangle, as in (0.1).

## 7. Trace compatibility is not trace invisibility

The positive theorem gives the exact equivariance (5.3).  It does not say
that the physical target itself is unchanged.

Inside one split-pair orientation packet, a lower depth-one target
determines its Johnson edge uniquely: it records the omitted active pair
and the chosen endpoint on every spectator pair.  Hence the map

\[
                         e\longmapsto L_1(e)                       \tag{7.1}
\]

is injective on all packet edges.  Consequently, if an edge-set
replacement inside one packet has exactly the same lower depth-one target
multiset, then it has exactly the same edge set.  A genuine successor
crossing cannot be shadow-invisible there.

Thus there are three different requirements:

1. **literal validity:** every output flag is the actual intersection or
   union of its output window;
2. **literal injectivity:** different selected occurrences have different
   physical targets; and
3. **literal invisibility:** the output target multiset equals the input
   target multiset.

Theorems 3.1 and 5.1 prove the first and preserve the second inside each
cell.  Equation (5.6) is the exact additional condition for arbitrary
cellwise preservation of the second.  Requirement 3 is impossible for a
nontrivial within-packet crossing already at the lower first shadow.

## 8. Composition boundary

The construction resolves the local `RSR^{-1}` gate:

* the matching genuinely changes from `(ab)` to `(ac)`;
* the coordinate generators are noncommuting;
* all middle owners are partitioned exactly;
* four-cycle cells are owner-disjoint and independently selectable;
* the entering pair bits pass through by a Latin bijection; and
* every signed trace at every depth is transported literally.

It does not yet give a full switching network.  Two consecutive adjacent
triples generally define different four-root cell partitions.  Independent
choices in both partitions overlap in owners, so another associator or a
nested saturation rule is needed before the crossings may be composed.
Moreover (5.6), or a weaker aggregate target-cover theorem, must be checked
after composition.

The precise surviving routing gate is therefore:

> Construct a sequence of overlapping four-cycle conjugated cells whose
> state-dependent owner supports admit disjoint stages (or a proved
> higher associator), and whose transported target decks satisfy the
> cross-cell collision/coverage ledger.

The old fixed-matching commutation obstruction no longer excludes this
object.  The ten-state calculation excludes only its pair-granular
refinement.  This is the sharp local boundary supplied by the present
theorem.
