# Protected sequential `C6` fusion: voltage, residence, and deep-window gates

**Date:** 2026-08-02  
**Lane:** A, pure mathematics and authenticated `c68b` specialization  
**Status:** exact protected-fusion theorem and exact residence obstruction for
the frozen two-`C6` witness.  The theorem closes the owner, lower-palette,
immediate-upper, topology, and voltage rows.  It does **not** claim depth-three
residence, deeper upper coverage, source binding, or compiler feasibility.

## 1. Outcome

The independently replayed `c68b` quotient factor has three cycles

\[
                  (1362,2),\qquad(26,5),\qquad(42,0),       \tag{1.1}
\]

where each pair is `(quotient length, Z_17 voltage)`.  Two state-relative
quotient incidence `C6` rotations, both avoiding the protected rows, give
the prefix sequence

\[
 (1362,2)+(26,5)+(42,0)
 \longrightarrow (1388,14)+(42,0)
 \longrightarrow (1430,4).                                \tag{1.2}
\]

Every prefix has degree two at every owner orbit, one edge at every
rank-eight facet orbit, all `1,144` rank-ten cap orbits covered, and all 232
protected marker edge orbits fixed.  Since `gcd(17,4)=1`, the final quotient
cycle lifts to one physical cycle on all 24,310 rank-nine owners.

The reusable mechanism is a **sequential prefix-safe `C6` fusion lemma**:
cyclically transfer one moving owner endpoint among three mutable facet rows;
test cap loads and the retained-path port involution on the current prefix;
then regenerate before the next transfer.  A cap-multiset identity is a
strong sufficient condition, but literal cap survival is the exact one.

There is an essential correction.  The final connected physical cycle has

\[
             2873\text{ positive runs of length }2,
 \qquad     2499\text{ positive runs of length }3,         \tag{1.3}
\]

hence 5,372 **positive-run** depth-three residence defects.  It also has
8,976 short zero gaps, so the full signed short-run census is 14,348.
Connectivity cannot be converted to a `D^3` antecedent by choosing a cut:
one cut can clip at most one positive run per coordinate, so at least
`5372-17=5355` positive defects remain internal.  The literal all-cut replay
is stronger: its exact positive-run minimum is 5,369 (attained by 272 cuts).

This note gives the exact residence delta by a weighted port-token graph:
six ports for a phase-closed physical `C6`, and the union of all developed
ports for a quotient rotation or composite.  It also proves:

* every coordinate always has exactly `Cat_(m-1)` positive runs and average
  run length `m` in an exact rank-`(m-1)`-rainbow/rank-`m` owner cycle;
* the abstract port calculus admits odd short-run defect change, so topology
  and coordinate marginals alone impose no parity invariant; but
* any equivariant repair of the present order must touch at least 32 further
  quotient edge orbits, hence at least 11 simple `C6`s.

Thus the observed residence debt is a support/locality obstruction, not a
parity or scalar-capacity impossibility.

## 2. Quotient incidence factors and protected rows

Let `G=Z_n` act freely on the relevant lower, owner, and immediate-upper
objects; in the odd central application `n=2m-1`.  Write

\[
 \mathcal L=\binom{[2m-1]}{m-1}/G,
 \quad \mathcal O=\binom{[2m-1]}m/G,
 \quad \mathcal U=\binom{[2m-1]}{m+1}/G.                \tag{2.1}
\]

At a lower orbit `c`, an admissible option is a phase-labelled unordered
pair of owner orbits `{r,t}` whose physical developments meet in the lower
orbit `c`.  Its immediate-upper label is denoted

\[
                         u(c;r,t)\in\mathcal U.            \tag{2.2}
\]

A quotient factor chooses one option at every `c` and has weighted degree
two at every owner orbit.  Developing it gives one physical edge of every
lower colour and degree two at every owner.  A protected row has its complete
phase-labelled option fixed; a legal protected switch may not change it.

For a cap orbit `U`, let

\[
             M_F(U)=|\{c:u(c;F(c))=U\}|.                  \tag{2.3}
\]

Immediate-upper completeness is `M_F(U)>=1` for every `U`.

## 3. The elementary protected `C6`

Choose three distinct mutable rows `c_i`, retained owners `r_i`, and moving
owners `t_i`, indexed modulo three, such that

\[
 F(c_i)=\{r_i,t_i\},\qquad
 F^Q(c_i)=\{r_i,t_{i+1}\}                                \tag{3.1}
\]

are all legal phase-labelled options.  Assume the three added incidences are
not already selected.  Call (3.1) a **state-relative simple `C6`**.

### Theorem 3.1 (protected degree and palette identity)

The switch (3.1) preserves:

1. one selected option at every lower row;
2. weighted degree two at every owner orbit;
3. every protected row; and
4. the complete physical rank-eight palette after development.

#### Proof

Each touched row loses and gains one moving incidence while retaining the
other.  Each `t_i` is removed at `c_i` and added at `c_{i-1}`, so its owner
degree is unchanged.  All other rows and owners are untouched.  Since the
three rows are mutable, no protected option is changed.  Development
commutes with this orbitwise identity.  \(\square\)

Define old and new cap labels

\[
 U_i^-=u(c_i;r_i,t_i),\qquad
 U_i^+=u(c_i;r_i,t_{i+1}).                                \tag{3.2}
\]

Let `r_Q(U)` and `a_Q(U)` be their multiplicities.

### Theorem 3.2 (exact prefix cap criterion)

For every cap orbit `U`,

\[
             M_{F^Q}(U)=M_F(U)-r_Q(U)+a_Q(U).             \tag{3.3}
\]

Consequently the switch preserves complete immediate-upper coverage iff

\[
             M_F(U)-r_Q(U)+a_Q(U)\ge1
             \quad\hbox{for every }U.                    \tag{3.4}
\]

The stronger multiset identity

\[
             \{U_i^-:i\in\mathbb Z_3\}_{\rm multi}
             =\{U_i^+:i\in\mathbb Z_3\}_{\rm multi}      \tag{3.5}
\]

preserves the complete cap multiplicity vector.

#### Proof

Only the three displayed rows change, giving (3.3).  A formerly covered cap
survives exactly when its new load is positive.  Equation (3.5) makes every
delta zero.  \(\square\)

## 4. Exact component fusion

In the suppressed owner factor, the old and new edge matchings on the six
cut ports are

\[
 \rho=\prod_{i=0}^2(r_i\ t_i),\qquad
 \beta=\prod_{i=0}^2(r_i\ t_{i+1}).                       \tag{4.1}
\]

Delete the three old edges.  The retained path fragments pair the ports;
write `alpha` for this fixed-point-free involution.  If `c(pi)` counts cycles
of a permutation, including fixed points, then

\[
 k^-(Q)=\frac{c(\alpha\rho)}2,
 \qquad
 k^+(Q)=\frac{c(\alpha\beta)}2.                           \tag{4.2}
\]

These are exactly the numbers of touched quotient components before and
after the switch.

### Corollary 4.1 (two-component `C6` merger)

Suppose the cut profile is `(2,1)` on two current components.  The `C6`
merges them precisely when `c(alpha beta)=2`.  Equivalently, after naming
the twice-cut component consistently, its two retained fragments pair the
same-role ports (`r` with `r` and `t` with `t`); the cross-role pairing does
not merge.  A `C6` cutting three distinct components once merges all three.

The port formula (4.2), rather than a component-count or parity proxy, is the
proof-safe test.

### Theorem 4.2 (sequential protected two-`C6` fusion)

Let `F_0` have three quotient components.  Suppose:

1. `Q_1` satisfies Theorems 3.1 and 3.2 in `F_0` and (4.2) shows that it
   merges two components;
2. after forming and rebuilding `F_1=F_0^{Q_1}`, `Q_2` satisfies the same
   conditions in `F_1` and merges its two remaining components; and
3. the unique cycle of `F_2=F_1^{Q_2}` has voltage generating `Z_n`.

Then `F_2` develops to one physical owner cycle, fixes the protected bank,
uses every lower colour once, and covers every immediate-upper orbit.

#### Proof

Theorems 3.1 and 3.2 apply at each prefix.  Equation (4.2) reduces the
quotient component count from three to two to one.  The lift of a quotient
cycle of voltage `v` has `gcd(n,v)` components, so the last hypothesis gives
one physical component.  \(\square\)

Even for disjoint row supports, the second topology test is state-relative:
the first switch changes the retained-path pairing.  For lower-disjoint
switches the final cap delta is additive, but prefix survival can be
order-sensitive.  Condition (3.5) is a strong sufficient reason that no
cap-load regeneration is needed; it is not necessary.

## 5. Voltage is a fragment ledger

Give every directed quotient edge an antisymmetric voltage `delta(e)` in
`Z_n`.  Delete the three old edges of a `C6`.  Orient each retained fragment
`P` as it appears in an output cycle `K`.  Then

\[
 V_{F^Q}(K)=
 \sum_{P\subset K}\delta(P)+
 \sum_{f\in Q^+\cap K}\delta(f)\pmod n.                  \tag{5.1}
\]

### Proposition 5.1 (why component voltages do not merely add)

Formula (5.1) is exact for overlapping and sequential switches.  When every
input component is cut once, it compresses to a signed sum of old component
voltages plus the new-minus-old seam displacement.  In a `(2,1)` cut, one
component is split into two fragments; its total voltage does not determine
their two individual voltages.  Thus the fragment ledger, not the old cycle
totals alone, is necessary.

For a quotient factor with cycles `K`, the physical lift has exactly

\[
                         \sum_K\gcd(n,V(K))                \tag{5.2}
\]

components.  Nonzero voltage is sufficient only when `n` is prime; the
dimension-uniform condition is `gcd(n,V)=1`.

## 6. The authenticated `c68b` two-stage witness

The exact option rows are as follows.  Every row is mutable.

\[
\begin{array}{c|r|r|r|r|r|r}
 &c&r&t^-&t^+&U^-&U^+\\ \hline
Q_1&255&1279&2041&511&10233&1535\\
   &495&3961&511&1981&4089&3963\\
   &1977&3955&1981&2041&3963&4083\\ \hline
Q_2&1271&5085&9463&10169&20341&10171\\
   &9145&9147&10169&15257&10171&15289\\
   &9335&15273&15257&9463&15289&20341
\end{array}                                                \tag{6.1}
\]

The primary-variable replacements are

\[
\begin{aligned}
 Q_1:&\quad 19\to2,\quad150\to178,\quad2935\to2941,\\
 Q_2:&\quad1267\to1269,\quad19509\to19510,
                    \quad19825\to19816.                  \tag{6.2}
\end{aligned}
\]

Before `Q_1`, cap loads at `10233,4089,3963` are respectively `2,2,1`.
The unique occurrence of `3963` is removed and recreated within the switch;
the first two retain a backup.  Hence (3.4) holds.  The new caps `1535` and
`4083` were already covered, so `Q_1` changes multiplicities but not support.

For `Q_2`, the cap multiset is literally rotated:

\[
       (20341,10171,15289)\longmapsto(10171,15289,20341),  \tag{6.3}
\]

so (3.5) holds.

The independently replayed prefix topology is exactly (1.2).  An explicit
voltage check for `Q_1` uses retained path lengths `25,653,707` and

\[
              0+9+16+11+1+11=48\equiv14\pmod {17}.       \tag{6.4}
\]

For `Q_2`, the retained path lengths are `1310,41,76` and

\[
              10+0+16+0+13+16=55\equiv4\pmod {17}.       \tag{6.5}
\]

The displayed oriented entries (including the `16`s) use the declared
traversal orientations; reversing the full output cycle negates the total
and changes no conclusion.
Since `4` is a unit modulo `17`, the physical lift is one cycle.

These are quotient endpoint-incidence `C6`s.  The first exchange has phase
`16 mod 17` and develops to one 102-edge alternating circuit (51 old and 51
new physical adjacencies), not to 17 disjoint physical hexagons.  The second
has phase zero and does develop to 17 physical hexagons.  This distinction
does not affect the cap, component, or voltage identities, but it is
essential for residence accounting.

This proves exactly: owner degree two, all rank-eight colours, all rank-ten
caps, all protected marker paths, quotient connectivity, and physical
connectivity.  It proves nothing yet about the chronological run state.

## 7. Exact residence delta of a circuit

Let `W` be a physical owner cycle.  For a coordinate `x`, its positive trace
is the cyclic binary word `1_(x in W_i)`.  Let

\[
 \Phi_d(W,x)=\#\{\text{positive }x\text{-runs of length at most }d\}.
                                                                  \tag{7.1}
\]

For the present `D^3` gate, `d=3`.  Singleton positive runs cannot occur in
an exact lower-rainbow factor: if an owner `T` containing `x` were isolated
between two owners omitting `x`, both incident lower colours would equal
`T-x`, contradicting lower-colour injectivity.  Thus the length-two and
length-three census is the complete positive `D^3` defect.

Delete a finite set of old physical adjacencies and expose their ports.  Let
`rho` be the old port matching and `beta` the final new port matching.  For
fixed `x`, take every positive component `B` of the retained fragments which
meets a cut port.  Give it weight

\[
                         w(B)=|B|.                          \tag{7.2}
\]

For `mu` equal to the old or new port matching, form `H_x(mu)` by joining
`B(p)` and `B(q)` whenever `pq` is a seam of `mu` and both endpoint owners
contain `x`.  A retained fragment which is entirely positive contributes
one component meeting both of its ports, so chains through several seams
are handled without exception.

### Theorem 7.1 (finite-port residence identity)

The affected positive runs under matching `mu` are exactly the connected
components `A` of `H_x(mu)`, and their lengths are

\[
                         w(A)=\sum_{B\subseteq A}w(B).      \tag{7.3}
\]

Consequently

\[
 \Delta_x(Q)=
 \sum_{A\in\pi_0H_x(\beta)}{\bf1}_{1\le w(A)\le d}
 -\sum_{A\in\pi_0H_x(\rho)}{\bf1}_{1\le w(A)\le d}       \tag{7.4}
\]

is the exact coordinate residence-defect change.  All fragment-internal runs
cancel.  Weights may be truncated at `d+1`.

#### Proof

Every changed run meets a cut port.  Within a retained fragment, its positive
terminal pieces are precisely the `B`.  A seam merges two such pieces iff
both endpoint bits are one.  Transitive seam merging is exactly graph
connectivity in `H_x(mu)`, and lengths add.  No other run changes.  \(\square\)

Thus a `C6` is globally positive-run-defect-monotone iff

\[
                         \sum_x\Delta_x(Q)\le0,            \tag{7.5}
\]

coordinatewise monotone iff every `\Delta_x\le0`, and strictly improving iff
the corresponding inequality is strict.  For an exact lower-rainbow prefix,
the singleton-run lemma makes the `w=1` term zero; this is why the present
census can use only lengths two and three.  A literal physical `C6` has six
ports.  A free `Z_n` quotient `C6` must be developed first and in general has
`6n` ports; its phase may join the translates into longer alternating
circuits, as in `Q_1`.

For a composite, apply the same construction to the union of all cut ports
and the final matching.  Deltas may be added circuit by circuit only after
state regeneration, or when, for every coordinate, the two boundary-
component systems `H_x` are vertex-disjoint (no retained positive component
or seam component participates in both).  Disjoint cyclic neighborhoods
alone are not enough.

The equivalent implementation state is: endpoint bits, prefix/suffix
constant-run ages truncated at `d+1`, an all-constant flag, and internal
short-run count.  Its concatenation rule is associative.

Applying the same construction to zero components gives the exact gap delta
`\Delta_x^-`; write the displayed positive-run delta as `\Delta_x^+` when
the distinction matters.  The signed residence gate is exactly the pair of
conditions on `\Delta_x^+` and `\Delta_x^-`.  The support lower bound below
uses only positive runs, which already suffice to rule out the frozen order.

## 8. Run-count invariant, absence of a parity obstruction, and locality

### Theorem 8.1 (exact run count)

In every connected exact rank-`(m-1)`-rainbow/rank-`m` owner factor on
`[2m-1]`, every coordinate `x` has

\[
 R_x=\binom{2m-2}{m-1}-\binom{2m-2}{m-2}
    =\operatorname{Cat}_{m-1}                              \tag{8.1}
\]

positive runs, and their average length is exactly `m`.

#### Proof

There are `M_x=binom(2m-2,m-1)` owners containing `x`.  An adjacency is
`11` in the `x`-trace exactly when its lower colour contains `x`; exact lower
ownership gives `I_x=binom(2m-2,m-2)` such adjacencies.  A positive run of
length `ell` contains `ell-1` such adjacencies, hence `I_x=M_x-R_x`.
Pascal's ratio gives (8.1), and `M_x/R_x=m`.  \(\square\)

At `m=9`,

\[
 M_x=12870,\qquad I_x=11440,\qquad R_x=1430,
 \qquad M_x-4R_x=7150.                                    \tag{8.2}
\]

There is abundant scalar mass for all runs to have length at least four.
The circuit must redistribute it.

There is no mod-two obstruction in the abstract port calculus.  At the
six-port level, take six unlinked positive terminal fragments of weights

\[
                         (1,1,3,1,3,3).                    \tag{8.3}
\]

The old matching `(01)(23)(45)` produces run lengths `(2,4,6)`, while the
alternating matching `(12)(34)(50)` produces `(4,4,4)`.  The defect drops by
one, while total mass, run count, and endpoint membership are unchanged.
Reversal increases it by one.  This is not asserted to be a Boolean-legal,
cap-safe, protected `C6`; it proves only that no parity invariant follows
from retained-fragment topology and coordinate marginals.  A Boolean-
catalogue parity or supply obstruction remains possible.

### Theorem 8.2 (equivariant support lower bound for the frozen chronology)

The final equivariant cycle has, for each coordinate, exactly

\[
                 169+147=316                              \tag{8.4}
\]

short positive runs.  In a `Z_17`-equivariant repair, one removed original
quotient edge orbit can meet at most `m+1=10` of these runs for a fixed
coordinate: among its 17 developed old
edges, exactly ten have a cap containing that coordinate, and every such
edge meets at most one positive run.  Every initial short run must have at
least one adjacency in its closure removed.  Therefore every equivariant
residence repair sequence from this fixed chronology must remove at least

\[
                         \left\lceil316/10\right\rceil=32  \tag{8.5}
\]

distinct original quotient edge orbits.  Since a simple quotient `C6`
touches three rows, at least 11 further simple quotient `C6`s are necessary.
This is a lower bound on equivariant support, not a claim that 11 suffice and
not a bound in the right units for arbitrary non-equivariant physical edits.

Finally, cutting a cyclic word can clip at most one positive run per
coordinate.  Hence no opening of the final cycle leaves fewer than

\[
                         5372-17=5355                      \tag{8.6}
\]

internal positive residence defects.

The authenticated all-cut census sharpens (8.6): the exact minimum is 5,369,
attained by 272 of the 24,310 cuts.  Equation (8.6) is the dimension-free
argument; 5,369 is the factor-specific replay value.

## 9. Deeper upper witnesses

For `h>=1`, let `D_h(F)` be the multiset of ORs of all cyclic windows of
`h+1` consecutive owner states; `h=1` is the immediate cap deck.  For a
switch `Q`, let `r_{Q,h}(X)` and `a_{Q,h}(X)` count removed and added
occurrences of target `X`.  Exactly as in (3.3),

\[
 M_{F^Q,h}(X)=M_{F,h}(X)-r_{Q,h}(X)+a_{Q,h}(X).            \tag{9.1}
\]

Only windows crossing an old or new seam change.  One `C6` exposes at most
`3h` old quotient-window starts at depth `h`; the two authenticated switches
expose at most `6h`, and through depth `d` at most

\[
                         3d(d+1).                          \tag{9.2}
\]

Development multiplies this occurrence bound by `n`.

### Corollary 9.1 (exact fixed-width deep-extension condition)

A prefix-safe `C6` fusion preserves every fixed-width tight deck through
depth `d` iff

\[
 M_{F,h}(X)-r_{Q,h}(X)+a_{Q,h}(X)\ge1
 \quad(1\le h\le d,\ X\text{ previously covered}).       \tag{9.3}
\]

It suffices that every lost crossing-window OR has an unaffected duplicate
witness, or that the new crossing OR deck contains the old crossing deck.
A unique old deep witness crossing a removed seam, with no equal new
crossing witness, is the minimal obstruction.

If the target notion allows an upper set to be witnessed by intervals of
different lengths, (9.3) is sufficient but not necessary: a target lost at
one width can survive at another.  The exact arbitrary-interval criterion is
the same load identity after aggregating `r` and `a` over all admissible
interval lengths.  The local bound (9.2) applies to the fixed-width tight
decks; it must not be quoted for unrestricted long intervals without a
separate stopping or OR-growth argument.

Immediate cap neutrality does not imply (9.3): longer windows also contain
retained-path prefixes and suffixes, whose pairing changes under fusion.
Thus deep preservation needs an explicit backup bank or a prefix/suffix
OR-deck transparency theorem.

For the authenticated connected factor, literal fixed-order replay misses
exactly 1,972, 510, and 51 upper targets at ranks 11, 12, and 13,
respectively, and none at ranks 14--17.  These counts are not attributed
solely to the two `C6`s (the input chronology was not deep-complete); they
show concretely that the closed immediate-cap row does not close the deep
row.

## 10. Dimension-uniform scope and remaining theorem

The algebra above is uniform in `m` and in every free cyclic quotient.
More generally, if a protected quotient factor with `c` components admits
`c-1` regenerated quotient `C6` rotations satisfying:

1. legal mutable rows and protected avoidance;
2. prefix cap survival (3.4);
3. one component reduction by (4.2) at every prefix; and
4. unit final voltage,

then it has a connected physical completion with exact lower and immediate
upper palettes and the named protected bank.  The support is at most
`3(c-1)` quotient rows.  Therefore this mechanism is compatible with an
all-`k` additive-constant construction **conditionally** when the quotient
component count and a protected fusion supply are controlled.

There is an exact residence/deep strengthening, with no probabilistic
qualification.  If the input is depth-`d` resident, every prefix creates no
positive or zero run of length at most `d` (equivalently the two token
deltas stay zero from the zero-defect state), and every prefix satisfies
(9.3), then the output is a connected depth-`d` resident factor with every
fixed-width tight upper deck through depth `d`.  For a nonresident input,
replace the prefix condition by the union-cut token calculation of Theorem
7.1 on both bit values and require its final signed short-run count to be
zero.  For arbitrary-interval upper coverage, also replace (9.3) by its
all-length aggregate version.  These conditions are necessary and
sufficient for the chronological rows of the stated circuit family; they
are not an existence theorem for such a family.

What is not dimension-uniformly proved is the supply.  Neither regular
degree, immediate cap coverage, nor component size guarantees a protected
cap-safe `C6`, and none guarantees the residence inequalities (7.5) or deep
rows (9.3).  The exact next positive theorem would be a protected fusion
hypergraph containing a component-spanning sequence whose boundary states
are residence-monotone and whose deep-window debts lie in a reserved backup
bank.  The present `c68b` witness proves that topology and voltage can close
while residence remains macroscopically nonzero.

## 11. Frozen provenance and exclusions

The exact theorem ledger is recorded in

```text
scratch/threadA_k17_c68b_two_c6_fusion_residence_20260802.audit.json
```

The authenticated final artifacts are:

```text
70f48c248ab7e8fb7d08895048fcf7d5b27fca5ff6f389832e5c4f35cf25adb6
  c68b.double_fusion.model
7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c
  c68b.double_fusion.factor.tsv
85ae3d42671eea04fb016988b9095cb79fd20217ea6eec02d480910403bfe31b
  scratch/ad_k17_marker58_upper_q1_quotient_independent_20260802/
    c68b.double_fusion.audit.json (frozen copy)
33731d36f4d2df10106fbe8f7c006b6d0718fc5902a22206d82f694d9241b645
  independent double-fusion audit
```

The live canonical audit later changed only its auxiliary-replay status field
and now hashes `2a78b0bfd8645dd05e7d6955ced8ee79088be1944788164393f6a860a7f09f85`;
the frozen `85ae3d...` copy above is the provenance target used here.

The result does not certify source/buffer occurrence binding, zero-gap
residence, ranks above the stated checked window deck, the lower compiler,
or a universal word.  No duplicate fusion search or SAT solve was run in
this lane.
