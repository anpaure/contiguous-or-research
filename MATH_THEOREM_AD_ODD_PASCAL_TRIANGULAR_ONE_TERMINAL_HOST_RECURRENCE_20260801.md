# Odd Pascal triangular recurrence and the exact one-terminal-host gate

Date: 2026-08-01  
Lane: AD, same-parity lower-chain recursion / terminal compiler state  
Status: exact scalar recurrence, exact integral four-sector normal form,
exact adjacent-boundary cocycle, and a conditional one-terminal induction.
This note does **not** prove integral triangular rounding, simultaneous
two-cross-bank host embedding, or `nu(k)=B(k)+O(1)`.

## 0. Outcome

Let `k=2m-1`, `m>=3`, and put

\[
 W=\binom{2m-1}{m},\qquad \Lambda=4^{m-1}-1,
 \qquad \tau_q=\binom{q+1}{2},
\]

\[
 d=\min\{q:qW+\tau_q\ge\Lambda\},\qquad
 \sigma=dW+\tau_d-\Lambda .                         \tag{0.1}
\]

For the odd child `k'=2m+1`, use primes.  Write

\[
 c=\operatorname {Cat}_m={2W\over m+1}.
\]

The exact scalar recurrence is

\[
 W'=4W-c,\qquad \Lambda'=4\Lambda+3,
 \qquad d'\in\{d,d+1\},                              \tag{0.2}
\]

\[
 d'=d
 \quad\Longleftrightarrow\quad
 4\sigma\ge dc+3\tau_d+3,                            \tag{0.3}
\]

and

\[
 \boxed{
 \sigma'=4\sigma-dc-3\tau_d-3
       +(d'-d)(W'+d+1).}                              \tag{0.4}
\]

Four copies of the parent triangular address system have the exact raw
address contraction

\[
 \boxed{4(W+d)-(W'+d')=c+4d-d'.}                     \tag{0.5}
\]

This is an address count, not a join count and not a recurrence for the
de-Bruijn serialization charge `chi`.

There is also an exact integral normal form.  Any integral parent
triangular factor yields `W'` already top-anchored child chains and an
endpoint-labelled residual bank of `c+4d` chain pieces, plus the three
newborn singleton targets.  Its total residual mass is at most

\[
                         d(c+4d)+3=O(W/\sqrt m).       \tag{0.6}
\]

The child has exactly enough scalar capacity for this bank, with surplus
`sigma'`.  Completing it is an integral comparability/path-forest problem;
the scalar identities do not solve that problem.

For the proposed old C8 terminal sidecar, the two ray chains have lengths
`d-1,d-1`.  They fit the two largest relevant triangular boundary
capacities `d-1,d`, leaving one scalar cell (three on a deadline jump if the
two largest child capacities are used).  But literal absorption into two
adjacent suffix tables is much stricter.  With a fresh terminal singleton
letter `Z`, it is possible exactly when, after swapping the two shores if
necessary,

\[
                         P_t=Z\cup R_t
                         \qquad(1\le t<d).             \tag{0.7}
\]

The canonical opposite prefix/suffix C8 flags violate all `d-1` equations
in both orientations.  Thus the old host is absorbed **scalarly** but not
by the canonical literal boundary cocycle.

A whole-host filler reflection turns one suffix flag into a prefix flag and
does satisfy (0.7), subject to one exact base equation.  This proves a
positive suffix-table interface, not its physical owner/residence/upper/
common-cap embedding.

Finally, define `C_m` to be an honest uncontracted terminal source-position
charge above the declared stage-`m` baseline.  Under the explicit prepared
lift hypotheses in Theorem 7.1 below,

\[
 \boxed{
 C_{m+1}\le \max(C_m,1)+\rho_m+\beta_m+u_m.}          \tag{0.8}
\]

Here `rho_m` is the literal trace/reset packing defect,
`beta_m=beta_m^bg+beta_m^res` counts both background targets whose selected
cells fail admissible full-block transport and residual targets displaced
by the prescribed boundary host, and `u_m` is the remaining upper-target
defect.  The
zero-block theorem removes any additional *abstract* positive-threshold
sorting charge only after both physical cross matchings exist in one
cap/guard state.

The current folded-C8 physical catalogue does not satisfy that antecedent:
the common-endpoint replay has `exact_one_ray_comparators=0` and upper
support `15`.  What is presently proved is one full nested suffix-ray
rethread with injective old-background transport, phasewise, inside an
upper-support-safe resident two-path owner forest.  Simultaneous realization
of both cross matchings remains open.  Therefore (0.8) is a precise
conditional induction, not a claimed all-`m` recurrence.

## 1. Exact odd-to-odd scalar recurrence

### Theorem 1.1

Equations (0.2)--(0.4) hold for every `m>=3`.

#### Proof

The binomial ratio gives

\[
 {W'\over W}
 = {\binom{2m+1}{m+1}\over\binom{2m-1}{m}}
 =4-{2\over m+1},
\]

which is `W'=4W-c`.  The lower half has size
`Lambda=4^(m-1)-1`, hence `Lambda'=4Lambda+3`.

For arbitrary trial depth `q`, put

\[
 F_m(q)=qW+\tau_q-\Lambda.
\]

Then

\[
 \begin{aligned}
 F_{m+1}(q)
 &=q(4W-c)+\tau_q-(4\Lambda+3)\\
 &=4F_m(q)-qc-3\tau_q-3.                  \tag{1.1}
 \end{aligned}
\]

Since `d` is minimal, `F_m(d-1)<0`.  Equation (1.1) gives
`F_(m+1)(d-1)<0`, so `d'>=d`.  At `q=d`, (1.1) becomes

\[
 F_{m+1}(d)=4\sigma-dc-3\tau_d-3.          \tag{1.2}
\]

This proves the plateau criterion (0.3).

It remains to rule out a jump larger than one.  We have `d<=m-1`, because
the old strict lower ideal has `m-1` ranks and each has size at most `W`.
Also `c=2W/(m+1)`.  Hence

\[
 W'+d+1>dc+3\tau_d+3                         \tag{1.3}
\]

for `m>=3`.  Indeed,

\[
 W'-dc=4W-(d+1)c
 \ge\left(2+{2\over m+1}\right)W.                    \tag{1.3a}
\]

Now `d<=m-1` and `W>=binom(2m-1,2)` make the right side of
(1.3a) larger than `3tau_d+2-d`; adding `d+1` gives (1.3).  Since
`sigma>=0`, equations (1.2)--(1.3) give

\[
 F_{m+1}(d+1)=F_{m+1}(d)+W'+d+1>0.
\]

Thus `d'` is `d` or `d+1`.  If it jumps, raising the depth adds exactly one
cell at each of the `W'` owners and a new boundary row of size `d+1`.
Equation (0.4) follows. \(\square\)

### Corollary 1.2 (raw address contraction)

Equation (0.5) holds.

#### Proof

Subtract `W'+d'` from `4(W+d)` and use `4W-W'=c`. \(\square\)

The word "raw" is load-bearing.  Empty chain atoms can make some address
contractions vacuous.  Conversely, one address contraction may require a
nontrivial source reset.  Neither the number of physical components nor
`chi` follows from (0.5).

## 2. Exact four-sector packetization of an integral parent

Assume now that an exact integral triangular parent is given: `W` anchored
chain addresses of capacity `d` and boundary addresses of capacities
`1,...,d`, whose selected chains partition the old nonempty strict lower
ideal.  The theorem is conditional on this integral parent; the fractional
triangular theorem does not supply it.

There are `W` old rank-`(m-1)` targets.  An inclusion chain contains at most
one of them.  Hence exactly `W` of the `W+d` selected parent chains contain
a rank-`(m-1)` target, and exactly `d` are top-free.

Choose a perfect matching

\[
 \mu:\binom{\Omega}{m-1}\longrightarrow\binom{\Omega}{m},
 \qquad A\subset\mu(A).                                \tag{2.1}
\]

It exists because the consecutive-level containment graph is balanced and
regular.

For a top-containing chain

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell=A),
 \qquad |A|=m-1,
\]

introduce new coordinates `x,y` and form

\[
 \begin{aligned}
 Q_C^0&=(S_2,\ldots,S_\ell,\mu(A)),\\
 Q_C^x&=(S_1+x,\ldots,S_\ell+x),\\
 Q_C^y&=(S_1+y,\ldots,S_\ell+y),\\
 R_C&=(S_1,S_1+xy,\ldots,S_{\ell-1}+xy).
                                                        \tag{2.2}
 \end{aligned}
\]

Every displayed chain has exactly `ell` members.  For a top-free parent
chain retain its four vertical tagged copies.  All pieces have length at
most `d`.  Sectorwise they cover the untagged old ranks at most `m-1`
together with the matched rank-`m` tops, the `x`- and `y`-tagged copies of
old ranks at most `m-1`, and the `xy`-tagged copies only through old rank
`m-2`.  The only omitted child targets at this stage are the three singleton
births `{x},{y},{x,y}`.

Classify the parent addresses:

* `A`: contains ranks `m-1` and `m-2`;
* `B`: contains rank `m-1` but not rank `m-2`;
* `C`: is top-free and contains rank `m-2`;
* `D`: contains neither.

Then

\[
 |A|+|B|=W,\qquad |A|+|C|=W-c,\qquad |C|+|D|=d.       \tag{2.3}
\]

The second identity uses

\[
 \binom{2m-1}{m-2}=W-c.                               \tag{2.4}
\]

### Theorem 2.1 (child top bank and residual bank)

The number of pieces containing a child rank-`m` target is

\[
 4|A|+3|B|+|C|=4W-c=W'.                              \tag{2.5}
\]

They cover every child rank-`m` target exactly once and therefore anchor to
distinct rank-`(m+1)` child owners.  The inherited non-top bank has exactly

\[
 |B|+3|C|+4|D|=c+4d                               \tag{2.6}
\]

labelled chain pieces.  Retaining `d'` pieces as child boundary roots leaves
exactly `c+4d-d'` inherited address contractions.  The three newborn
singletons are separate insertion obligations.

#### Proof

For class `A`, all four chains in (2.2) contain a rank-`m` target; for class
`B`, the first three do; class `C` contributes its `xy` copy; class `D`
contributes none.  This proves (2.5).  The four child sectors show directly
that all rank-`m` targets occur, and the count makes them unique.  The
rank-`m`/rank-`(m+1)` containment graph is balanced regular, so a perfect
owner matching exists.

Subtract the top-piece count from the four pieces at every one of the
`W+d` parent addresses, or use (2.3), to obtain (2.6). \(\square\)

### Corollary 2.2 (residual mass)

If `ell_P` is the length at parent address `P`, the exact residual mass is

\[
 R=
 \sum_{P\in B}\ell_P
 +3\sum_{P\in C}\ell_P
 +4\sum_{P\in D}\ell_P+3,                            \tag{2.7}
\]

and hence the finite inequality in (0.6) holds.  The standard central
binomial estimate gives `Lambda/W=Theta(sqrt(m))`.  The integer
`ceil(Lambda/W)` is feasible in the definition of `d`, so
`d=O(sqrt(m))`; then `tau_d/W=o(1)`, and the minimality inequality forces
`d=Omega(sqrt(m))`.  Thus `d=Theta(sqrt(m))`.  Since `c=Theta(W/m)`, it
follows that

\[
 d(c+4d)+3=O(W/\sqrt m)+O(m)=O(W/\sqrt m),
\]

which proves the asymptotic part of (0.6).

The `+3` is precisely the newborn singleton bank.  This is a sublinear
leave, not an `O(1)` leave.

## 3. The exact residual completion gate

Let `M` be the mass already placed in the `W'` top-containing child chains.
Then the unplaced mass is

\[
                         R=\Lambda'-M.                 \tag{3.1}
\]

The unused capacity in those owner chains together with the complete child
boundary triangle is

\[
                         (d'W'-M)+\tau_{d'}.           \tag{3.2}
\]

Subtracting (3.1) from (3.2) gives exactly

\[
                         \sigma'.                      \tag{3.3}
\]

Thus no additional *scalar* defect is hidden in the `A/B/C/D`
correlations.

Delete empty pieces before forming an exact sufficient integral certificate;
retain their labels only in the raw address ledger.  On the nonempty
residual pieces take an endpoint-labelled path forest whose terminal
sink-roots are the `W'` top pieces and `d'` chosen boundary pieces.  Arcs
point toward those sinks, and an arc `P->Q` is legal when

\[
                         \max P\subseteq\min Q,        \tag{3.4}
\]

and every root path obeys its owner/boundary capacity.  The three newborn
singletons must insert into compatible gaps.  Such a forest gives the child
triangular factor.  At the labelled-address level it accounts for the
contractions in (0.5); the number of nonempty physical joins can be smaller.

No theorem here guarantees this forest.  In particular, `(d,sigma)` is not
a complete recursive state; the endpoint-containment graph of the residual
bank is necessary data.

## 4. Scalar absorption of one old two-ray host

Suppose the inherited terminal sidecar asks for two strict chains

\[
 P_1\subsetneq\cdots\subsetneq P_{d-1},\qquad
 R_1\subsetneq\cdots\subsetneq R_{d-1}.               \tag{4.1}
\]

Their total mass is `2d-2`.  The child boundary bank contains addresses of
capacities `d-1` and `d`, because `d'>=d`.  Their combined capacity is
`2d-1`, so there is one spare cell.  If `d'=d+1` and the two largest child
addresses are used instead, the spare is three.

Therefore one additional typed target fits at the scalar level.  Equally,
if one auxiliary host cell is charged against every parent and child
triangular capacity, `bar_sigma=sigma-1` obeys, on a plateau,

\[
 \bar\sigma'=4\bar\sigma-(dc+3\tau_d+3)+3.             \tag{4.2}
\]

The final `+3` is exactly the contraction of four scalar reservations to
one.  Equation (4.2) is inapplicable if the host is an owner/top state
outside strict-lower capacity, or is already one of the targets counted in
`Lambda`.

This proves only a capacity statement.  Designating (4.1) as the two child
boundary chains constrains the residual forest in Section 3, and one common
source prefix imposes the next theorem.

## 5. Exact adjacent-boundary cocycle

Let

\[
 A_1\subsetneq\cdots\subsetneq A_{d-1}                \tag{5.1}
\]

be the complete suffix table at one boundary endpoint.  Append one nonempty
source letter `X`.  The next endpoint has forced suffix table

\[
 D_1=X,\qquad D_{j+1}=X\cup A_j\quad(1\le j<d).        \tag{5.2}
\]

Let a second `(d-1)`-chain

\[
 B_1\subsetneq\cdots\subsetneq B_{d-1}                \tag{5.3}
\]

occupy all rows except row `h` of (5.2), in order.  Put

\[
 r_i=\begin{cases}i,&i<h,\\ i+1,&i\ge h.\end{cases}  \tag{5.4}
\]

### Theorem 5.1 (necessary and sufficient cocycle)

The two chains and the omitted target `H` arise from two adjacent literal
boundary endpoints if and only if there is `X!=emptyset` such that

\[
 B_i=
 \begin{cases}
 X,&r_i=1,\\
 X\cup A_{r_i-1},&r_i\ge2,
 \end{cases}                                           \tag{5.5}
\]

and necessarily

\[
 H=\begin{cases}
 X,&h=1,\\
 X\cup A_{h-1},&h\ge2.
 \end{cases}                                           \tag{5.6}
\]

The same criterion with `A,B` exchanged covers the other orientation.
For a strict target-chain realization, additionally require the complete
row list `D_1,...,D_d` in (5.2) to be pairwise distinct; equivalently,
`X union A_1,...,X union A_(d-1)` must grow strictly and `H` must differ
from every retained `B_i`.  Without this nondegeneracy clause,
(5.5)--(5.6) characterize a suffix table with multiplicity only.

#### Proof

Equation (5.2) is the definition of suffix unions after appending `X`.
Deleting its `h`th row gives (5.4)--(5.5), and the deleted row is (5.6).
This proves necessity.  Conversely, realize the strict chain (5.1) by its
successive difference letters in reverse order and append `X`.  Equations
(5.2), (5.5), and (5.6) give the required two endpoints. \(\square\)

For a typed terminal singleton socket, `H=X`, so `h=1` and the criterion is

\[
                         B_i=X\cup A_i
                         \qquad(1\le i<d).             \tag{5.7}
\]

### Corollary 5.2 (canonical opposite flags fail sharply)

Let fillers be disjoint from the fixed bases and put

\[
 P_t=B_P\cup\{f_1,\ldots,f_t\},\qquad
 R_t=B_R\cup\{f_{d-t+1},\ldots,f_d\}.                 \tag{5.8}
\]

For the terminal socket (5.7), the cocycle defect is exactly `d-1` in both
orientations.  Indeed, every `X union R_t` contains `f_d`, while every
`P_t`, `t<d`, omits it.  In the reverse orientation use `f_1`.

Even when the extra target may occupy an arbitrary row, (5.5) fails for
every `d>=3`: its `i=2` instance forces `A_1 subseteq B_2`; the two
orientations of (5.8) violate this respectively at `f_1` and `f_d`.
At `d=2` only, the nonterminal placement `h=2` has the degenerate solution
whose extra target is `P_1 union R_1`.  This does not repair the typed
terminal-singleton face `h=1`.

Thus the scalar spare in Section 4 does not absorb the canonical old host
literally.

### Corollary 5.3 (whole-host reflection is a suffix-table escape)

Let `sigma(f_i)=f_(d+1-i)` on one entire inherited filler rail.  Then

\[
 \sigma(R_t)=\sigma(B_R)\cup\{f_1,\ldots,f_t\}.        \tag{5.9}
\]

If a nonempty terminal letter `Z` satisfies

\[
                         B_P=Z\cup\sigma(B_R),         \tag{5.10}
\]

then `P_t=Z union sigma(R_t)` for every `t`, so (5.7) holds.  A literal
source tableau, earliest to latest, is

\[
 \{f_{d-1}\},\ldots,\{f_2\},
 \ \sigma(B_R)\cup\{f_1\},\ Z.                       \tag{5.11}
\]

Before `Z` its suffix rows are `sigma(R_1),...,sigma(R_(d-1))`; after `Z`
they are `Z,P_1,...,P_(d-1)`.

The reflection must act on the whole inherited host.  Relabelling only the
ray values is not a physical construction.  Equations (5.9)--(5.11) do not
prove owner injectivity, residence, upper palettes, the two simultaneous
zero-block cross matchings, or a common cap across the outside joins.

## 6. Full-block transport and its deadline qualification

Fix one linear opening of the source word.  Replace one old source position
`Q` by a consecutive nonempty block

\[
                         Q_1,\ldots,Q_s,qquad
                         \bigcup_jQ_j=Q.               \tag{6.1}
\]

Map an old interval not meeting `Q` by the order-preserving shift of its
endpoints.  Map an old interval meeting `Q` to the interval containing the
whole block (6.1).  This map is injective and preserves every interval OR.
Every genuinely new side interval is outside its image.

Therefore a previously selected target-to-cell matching transports
injectively under a full-block refinement.  This removes a separate
background Hall problem only for cells that remain admissible after the
refinement.

If `s=2`, every crossing interval gains one source position.  A crossing
old cell of width `d` becomes width `d+1`.  On a plateau `d'=d`, it leaves
the deadline band and must be rehosted; on a jump it may remain admissible.
Owner windows, maximal erosion, residence and pointwise caps can impose
further restrictions.  Let `beta_m^bg` denote the number of selected
background targets left without an admissible transported cell after all
these checks.  Together with the displaced-residual count `beta_m^res` from
the prescribed boundary packing, this gives
`beta_m=beta_m^bg+beta_m^res` in (0.8).  OR equality alone does not prove
`beta_m^bg=0`.

## 7. Conditional one-terminal-host induction

Fix the baseline numerically in advance as the declared
`B(k)=W_k+d_k` profile; it may not be redefined after seeing the lift.  Let
`C_m` be a proved upper bound on the number of uncontracted terminal source
positions above that baseline.  Call an odd Pascal lift
**one-terminal prepared** if all of the following hold.

1. **Literal baseline carrier.**  Outside the named terminal bank, one
   declared child chronology of baseline length `B(k')` is already
   owner-legal, resident and nonzero, and covers every middle/upper/lower
   target except the defects named below.  In particular, this clause is
   not inferred from an abstract chain factor.
2. **Integral triangular completion and trace realization.**  The packet
   bank of Sections 2--3 has a capacity-respecting residual forest and
   yields an exact child triangular chain factor.  One selected literal
   trace for every resulting chain places all its uncharged targets in the
   baseline chronology.
3. **Designated boundary absorption.**  The two inherited ray chains and
   the one fresh typed target occupy declared child boundary rows satisfying
   Theorem 5.1.  Any displaced residual targets are included in `beta_m`.
4. **One physical two-cross-bank split.**  One actual source split exposes
   occurrence-labelled left and right ray banks in the same endpoint,
   cap, deadline, residence and guard state.  Both cross graphs in the
   zero-block theorem have perfect matchings, and the union of those two
   matchings is cell-injective and disjoint from the full-block image and
   every already fixed triangular assignment.  A phasewise one-ray rethread
   is not enough.
5. **Admissible full-block background transport.**  All but `beta_m`
   selected background cells lift as in Section 6 and remain within every
   declared deadline/cap/guard row.
6. **Explicit overlay map.**  The materialized child word comes with a
   disjoint position partition `I_base dotcup I_term dotcup I_reset` and an
   order-preserving map of every inherited charged position into
   `I_base union I_term`.  Here `|I_base|=B(k')`,
   `|I_term|<=max(C_m,1)`, and `|I_reset|<=rho_m`.  Every inherited sidecar
   image in `I_base` is an ordinary full block; if `C_m>0`, the fresh split
   is assigned inside `I_term`, while for `C_m=0` that set has one new
   position.  `I_reset` contains all unresolved trace-imbalance,
   component-join and boundary-reset positions.
7. **Upper residue.**  At most `u_m` upper targets remain uncovered.

### Theorem 7.1 (one-terminal recurrence)

Every one-terminal-prepared lift satisfies

\[
 C_{m+1}\le\max(C_m,1)+\rho_m+\beta_m+u_m.             \tag{7.1}
\]

In particular, if `rho_m=beta_m=u_m=0` for every sufficiently large `m`,
then one initial stage with `C<=1` propagates `C<=1` under all later
same-parity steps.

#### Proof

Clauses 1--2 supply the literal child baseline and every lower target except
the explicitly charged defects.  Clause 3 puts the old ray tasks and the
fresh typed target inside the child triangular baseline.  Clause 4 and the
zero-block cross-matching theorem
give the entire terminal fan assignment with no positive-threshold matching
defect.  Clause 5 injects the old background matching into cells disjoint
from the new side cells.  Clause 6 charges exactly `max(C_m,1)+rho_m`
uncontracted positions.  Append one literal source cell for each of the
`beta_m` charged lower/residual casualties and each of the `u_m` upper
casualties from Clause 7.
Appending cannot destroy an existing contiguous-OR witness.  This proves
(7.1). \(\square\)

This is a bookkeeping implication with an independently fixed baseline and
an index-level overlay certificate.  Clause 6 is itself the unproved
packing/length antecedent; the theorem does not derive it from the scalar
recurrence.  In particular, the scalar fit in Section 4
proves neither Clause 1 nor Clause 2, and one abstract host proves neither
Clause 4 nor Clause 5.

## 8. What the ordinary trace charge actually satisfies

Let `chi(z)` be the exact minimum bridge-edge count making a selected
order-`d` de-Bruijn edge multiset `z` one Euler trail.  On a deadline plateau
`d'=d`, suppose, without the overlay hypothesis of Theorem 7.1, that the
child uses four independently lifted parent trace systems.  If all claimed
packet contractions identify trace endpoints at zero cost and the sole
remaining terminal join has endpoint states `v,u`, put

\[
                         q=d-\operatorname{ov}(v,u).   \tag{8.1}
\]

Lifting a minimum parent bridge multiset in all four copies and then adding
a shortest `v`-to-`u` walk gives only

\[
                         \chi_{m+1}\le4\chi_m+q,       \tag{8.2}
\]

On a deadline jump, lifting from order `d` to order `d+1` needs a separately
declared padding/reset construction; (8.2) is not asserted without it.  On
the plateau, `q=0` for a recycled state,
`q=1` for one actual de-Bruijn edge, and `q` can equal `d` for one abstract
host with no overlap theorem.

Thus `chi` does not obey (7.1) from scalar Pascal identities.  Replacing
`4chi_m` by `max(chi_m,1)` is exactly the content of the full-block overlay
and shared-terminal hypotheses, not algebraic cancellation.  Equivalently,
one terminal edge gives `chi<=1` only when adjoining that edge makes the
selected child trace multiset Euler-compatible and connected.

For the two independent canonical opposite flags, the directed source-word
overlap is zero in either direction: the last letter forced by a prefix flag
contains `f_1`, while every possible first letter of the suffix-flag word
omits `f_1`; reverse the argument with `f_d`.  An isolated reset can
therefore cost `d`.  A nonlocal ambient rethread may evade this local bound,
but it must be proved explicitly.

## 9. Current physical C8 verdict

The abstract zero-block theorem requires two cross perfect matchings.  The
current common-endpoint physical replay does **not** realize them together:

* `exact_one_ray_comparators=0` for every audited `2<=d<=12`;
* the relevant endpoint face has upper support `15`, not `16`;
* restoring the missing upper value can move the transported prefix
  coordinate to the other component.

The proved positive physical scope is narrower:

1. an all-`d` active endpoint rethread transports one full nested suffix
   ray and injectively transports the old background; and
2. an upper-support-safe resident two-path owner forest admits this
   rethread phasewise.

This does not establish Clause 4 of Theorem 7.1.  Likewise, the reflected
tableau in Corollary 5.3 establishes only the suffix/capacity interface.

Accordingly the exact remaining one-terminal lemma is:

> Starting from the endpoint-labelled residual forest of Theorem 2.1,
> embed a whole-host reflected (or otherwise cocycle-valid) terminal split
> whose two occurrence-labelled zero-block cross graphs both have perfect
> matchings in one owner-legal, resident, upper-complete, common-cap guard
> state; simultaneously preserve the admissible full-block image of the
> old background and make the child trace multiset connected with
> `rho_m=O(1)` (ideally zero).

Only this lemma, together with integral triangular completion, turns the
strategic `max(C_m,1)` recurrence into an all-`m` construction.

## 10. Independent audit

The light replay

```text
python3 scratch/audit_ad_odd_pascal_triangular_one_terminal_host_20260801.py --write
```

checks the integer recurrence for `2<=m<=65`, the exact address contraction,
the scalar two-ray fit, terminal cocycle defect `d-1` in both canonical
orientations, and the reflected positive suffix tableau.  It performs no
search and does not assert integral residual completion or physical host
embedding.

Frozen hashes at the time of this note:

```text
scratch/audit_ad_odd_pascal_triangular_one_terminal_host_20260801.py
  SHA-256 25d7acf5c7e9310fdb04b3e35cad1142f4bc12fa1ea2db1b465b9fcfe716855d
scratch/ad_odd_pascal_triangular_one_terminal_host_20260801.audit.json
  SHA-256 3076d5afd2532e2eba655a3779fcf7fe4904d702b49ab8b0c9541f4efa72c04b
  payload 33cbc1712ea934b63d3ae1609fe69a924f2ba27ae789bbc7979b64c1436dcd6e
scratch/audit_c8_common_endpoint_one_ray_comparator_20260801.py
  SHA-256 c1ce4aa7e8116417826f27527ddbe987d07f23d9c06f5b52c1d378ad6ede898c
scratch/c8_common_endpoint_one_ray_comparator_20260801.audit.json
  SHA-256 9244f1144d89bae78e68f1abc6c3180e4268f6464a99577311e5288dd55ba6cc
  payload 9376d5e8c4b5b91e2609f7e440cb8096f66543804cb1da11018b276f00fdd49d
```

The dependencies are
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`,
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`,
and
`MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md`.
