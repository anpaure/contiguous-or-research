# Primal--dual coatom pairing: aperture and residence no-go

Date: 2026-08-01  
Lane: A, `B(k)+O(1)` primal/dual cancellation  
Status: exact no-go for the intact or unary protected primal--dual pair;
exact coupled crossing-deck escape condition isolated.  No no-go is claimed
against a larger packet which rethreads a linear number of dual adjacencies.

## 0. Verdict

Pairing the canonical OR-transparent mixed coatom packet with its literal
complement does **not** give a constant-seam macro transparent to both upper
OR support and lower intersection support.

There are two independent invariants.

1. **Four-coordinate aperture.**  Every primal owner lies in one fixed
   `(r+4)`-set, while every dual owner contains one fixed `(r-4)`-set.
   Therefore an internal primal OR has rank at most `r+4`, and an internal
   dual intersection has rank at least `r-4`.  The canonical lower damage
   contains rank-`r-q` targets at every `2<=q<=d`; for `q>=5` no dual
   internal interval can host them.  Dually, the complement packet's lost
   OR targets have rank `r+q`, and no primal internal interval can host them.

2. **Singleton-run incidence.**  The dual has exactly `12d` internal
   `0,1,0` positive-run witnesses, one for each middle filler in each of its
   twelve atom blocks.  An intact dual fragment therefore violates even
   threshold-two positive residence.  A seam rethread retaining all dual
   owners must change at least

   \[
                            12\left\lceil\frac d2\right\rceil   \tag{0.1}
   \]

   old block adjacencies merely to hit all these witnesses.

Thus the complement is a valid gap/AND rail, but not a zero-cost physical
repair rail for the positive-resident OR packet.  The only surviving escape
is a genuinely coupled braid: it must use primal--dual crossing intervals
as named lower witnesses, change `Omega(d)` dual adjacencies, and verify the
crossing OR deck simultaneously.  This is not composition of two unary
transparent packets.

This is a **physical/cancellation** obstruction, not a new fixed-flag
lattice obstruction.  The authoritative Pluecker-lattice theorem already
proves that reversible primal packets generate the complete saturated
fixed-filler reflected flag lattice `U_d`; its depth-two projection generates
the complete coordinate-degree kernel.  Algebraically the complement
reflects rather than cancels that action:

\[
 \Delta_\vee(P_0,P_1)=0,\qquad
 \Delta_\cap(P_0,P_1)=\mathcal D,\qquad
 \Delta_\cap(D_0,D_1)=0,\qquad
 \Delta_\vee(D_0,D_1)=\mathcal C(\mathcal D).                 \tag{0.2}
\]

Here `mathcal C` complements every labelled support value in `Omega`.
Reversing the dual phase changes the sign of the last exchange, not its
shore.  Thus the remaining issue is physical realization of an
owner-disjoint inverse action (and its nonlinear compiler state), not
integer generation inside the filler flag.

## 1. Set-up

Let `d>=1`, `n=d+2`, and `r>=d+4`.  Write the canonical primal phases as
`P_0,P_1`.  Their coordinates split as

\[
 S=K\mathbin{\dot\cup}A\mathbin{\dot\cup}F,
 \qquad |K|=r-d-4,\quad |A|=6,\quad |F|=d+2,                  \tag{1.1}
\]

so `|S|=r+4`.  Embed them in

\[
 \Omega=S\mathbin{\dot\cup}G,
 \qquad |G|=r-4,qquad |\Omega|=2r,                           \tag{1.2}
\]

and let `D_epsilon=Omega-P_epsilon` cellwise.  Coordinate conjugacy of a
dual phase is allowed below; it does not alter any rank or run count.

For the canonical schedule, put

\[
 P_q^F=\{f_1,\ldots,f_{n-q-1}\},\qquad
 S_q^F=\{f_q,\ldots,f_{n-2}\}.                               \tag{1.3}
\]

The exact old-only and new-only depth-`q` lower values, for every
`2<=q<=d`, are

\[
\begin{aligned}
 \mathcal L_q^-&=\{K\cup Ibc\cup P_q^F,
                    K\cup Ica\cup S_q^F\},\\
 \mathcal L_q^+&=\{K\cup Ica\cup P_q^F,
                    K\cup Ibc\cup S_q^F\}.
\end{aligned}                                                  \tag{1.4}
\]

Every member has rank `r-q`.  Formula (1.4) is the symbolic endpoint form
of the independently audited lower-damage theorem.

## 2. Exact serial deck algebra

For a word `W`, let `P_star(W),S_star(W),I_star(W)` be its distinct prefix,
suffix and internal interval decks for `star` equal to union or
intersection.  For two nonempty words `A,B`,

\[
 \mathcal I_\star(AB)=
 \mathcal I_\star(A)\cup\mathcal I_\star(B)\cup
 \{s\star p:s\in\mathcal S_\star(A),\ p\in\mathcal P_\star(B)\}.
                                                                    \tag{2.1}
\]

For three blocks `A,C,B`, the additional crossing families are

\[
\begin{aligned}
 &\mathcal S_\star(A)\star\mathcal P_\star(C),\qquad
   \mathcal S_\star(C)\star\mathcal P_\star(B),\\
 &\{s\star T_\star(C)\star p:
       s\in\mathcal S_\star(A),\ p\in\mathcal P_\star(B)\},
\end{aligned}                                                   \tag{2.2}
\]

besides the three internal decks.  Here set products mean all pairwise
values and `T_star(C)` is the total union or intersection of `C`.

### Lemma 2.1

Equations (2.1)--(2.2) are exact.

#### Proof

An interval is internal to one block, crosses one block boundary, or crosses
both.  Its contribution from every completely traversed block is the total
semilattice value, while its two partial contributions are a suffix and a
prefix.  These cases are disjoint and exhaustive. \(\square\)

Consequently a connector can repair a loss only by literal membership in
one of (2.2); marginal equality or opposite signed counts do not suffice.

## 3. The four-coordinate aperture

Define the upper and lower apertures of a rank-`r` word `W` by

\[
 a^+(W)=\left|\bigcup W\right|-r,
 \qquad
 a^-(W)=r-\left|\bigcap W\right|.                              \tag{3.1}
\]

For the canonical primal and its dual,

\[
                 a^+(P_\epsilon)=4,
                 \qquad a^-(D_\epsilon)=4.                    \tag{3.2}
\]

### Theorem 3.1 (unary paired-macro no-go)

Assume `d>=5`.  In any protected two-slot construction in which old values
must be retained by an internal interval of either the primal slot or one
coordinate-conjugate dual slot, the dual cannot repair the canonical lower
losses at all depths.  If the dual phase is changed, the primal cannot
repair its complementary OR losses either.

#### Proof

Every internal dual intersection contains its conjugated fixed core of size
`r-4`, hence has rank at least `r-4`.  But (1.4) has rank `r-q<r-4` for
`q>=5`.  Thus no member of `L_q^-` belongs to the dual internal intersection
deck, irrespective of coordinate relabelling or phase orientation.

By De Morgan, changing the dual phase exchanges OR values complementary to
the primal lower differences.  At depth `q` these have rank `r+q`.  Every
primal internal OR lies in the fixed support `S`, of size `r+4`, and cannot
equal such a value for `q>=5`. \(\square\)

The invariant is not the number of packets.  Any bounded collection of
ordinary complement packets still has lower aperture four in each slot and
cannot internally host a rank below `r-4`.

## 4. Literal serial pairing is sector-separated

There is a still sharper statement for the natural, unconjugated
concatenation.  Assume `K` is nonempty (equivalently `r>=d+5`) and choose
`k in K`, `g in G`.  Every primal cell has marker signature

\[
                              (k,g)=(1,0),                      \tag{4.1}
\]

and every dual cell has signature `(0,1)`.  Therefore internal and crossing
intervals have the following immutable sectors:

\[
\begin{array}{c|ccc}
 &\text{primal internal}&\text{dual internal}&\text{crossing}\\ \hline
 \text{OR}&10&01&11\\
 \text{intersection}&10&01&00.
\end{array}                                                     \tag{4.2}
\]

### Theorem 4.1 (literal one-pair no-go)

For `d>=2`, in the natural serial pair, either orientation and either
same-phase or crossed-phase pairing, crossing intervals cannot repair a
primal lower loss or a dual OR loss.  Hence one primal plus one dual is not
simultaneously OR and lower-intersection transparent even if residence is
ignored.

#### Proof

Every primal lower loss in (1.4) has sector `10`.  By (4.2), only a primal
internal intersection can have that sector; it is absent after the primal
move.  Every dual OR loss has sector `01`, and only a dual internal OR can
have that sector; it is absent after the dual move.  Reversal changes no
deck, and reversing the phase direction merely exchanges old-only with
new-only values. \(\square\)

At the boundary case `K=empty`, Theorem 4.1's two-marker proof is not
available.  The aperture theorem still applies for `d>=5`, and the residence
obstruction below applies for every `d>=1`.

Two sharper serial statements remove most of that boundary qualification.

### Lemma 4.2 (middle-filler ray obstruction)

Let `F^o={f_1,...,f_d}`.  Every literal dual owner contains at most one
member of `F^o`, whereas for `2<=q<=d-1` every value in (1.4) contains
exactly `d+1-q>=2` members of `F^o`.  Hence no intersection interval which
touches a literal dual owner can repair any of those lower losses.

#### Proof

A dual block cell contains its single displayed filler, and a dual screen
contains no middle filler.  An intersection is a subset of every owner it
touches.  Formula (1.3) gives the ray size. \(\square\)

Dually, no OR interval touching a primal owner can equal the complementary
dual loss at these depths: that primal owner contributes all but at most one
middle filler, while the complementary loss forbids at least two.  Thus the
natural complement contributes no cancellation for `q<=d-1`, even through
a crossing interval.  A connector-only interval could provide the target,
but then the connector, not the dual, is the repair.

### Theorem 4.3 (arbitrary conjugate direct-pair no-go)

Let one coordinate-conjugate dual packet be concatenated directly before or
after the primal packet.  For every `d>=3`, no choice of conjugacy,
orientation or phase direction repairs all canonical lower losses.

#### Proof

Every value in (1.4) contains the active coordinate `c`, while both primal
packet endpoints omit `c`.  A crossing intersection contains the adjacent
primal endpoint and therefore omits `c`; it cannot be a ladder value.

Every internal intersection of a conjugated dual contains the same fixed
core `pi(G)`, of size

\[
                    |G|=r-4=|K|+d.                             \tag{4.3}
\]

If the dual internal deck covered all old-only values in (1.4), then this
core would be contained in their total intersection.  For `d>=2`, that
intersection is exactly

\[
                         K\cup\{c,\mathord\infty\},             \tag{4.4}
\]

of size `|K|+2`, contradicting (4.3) when `d>=3`.  The new primal
internal deck itself omits the old-only values, exhausting (2.1). \(\square\)

At `d=2` the core-size comparison is tight, but positive residence still
rules out the requested pair.

### Lemma 4.4 (boundary chains cannot be repaired from behind)

The total intersection of either primal phase is `K`.  Its old-only
prefix-AND values are `K+{b}` and `K+{b,infinity}`, while its old-only
suffix-AND value is `K+{e,b}` (with `a` replacing `b` in the other phase).
If the primal packet is the first block of a serial macro, no later block
can repair its missing prefix values; if it is the last block, no earlier
block can repair its missing suffix value.

#### Proof

After a prefix has traversed the whole primal block, its intersection is
contained in the primal total intersection `K`, so it cannot equal an
old-only prefix value strictly containing `K`.  The suffix statement is the
same argument in reverse. \(\square\)

This is a context-independent boundary-deck obstruction.  It remains at
`d=1`, where the internal ladder (1.4) is empty.

## 5. Positive-residence obstruction

Inside a dual atom block the owners have the form

\[
             G\cup(A\setminus V)\cup\{f_0\},\ldots,
             G\cup(A\setminus V)\cup\{f_{n-1}\}.              \tag{5.1}
\]

No dual screen contains a middle filler `f_i`, `1<=i<=n-2`.  Thus, for
each of twelve blocks and each of the `d` middle fillers, the corresponding
cell is the centre of a strict internal `0,1,0` occurrence pattern.

### Theorem 5.1 (residence and edit floor)

An intact dual fragment fails positive-run residence for every threshold at
least two, in every exterior context and under every reversal or coordinate
permutation.  If all dual owners are retained and only old block
adjacencies are cut/rethreaded, at least

\[
                             12\left\lceil d/2\right\rceil      \tag{5.2}
\]

old adjacencies must change before all strict singleton witnesses can even
be destroyed.

#### Proof

The two neighbours of the `f_i` cell in (5.1) omit `f_i`; the resulting
run of length one is internal to the block, so exterior cells cannot extend
it.  Reversal and relabelling preserve this fact.

Within one length-`n` block, the `d=n-2` singleton centres are the internal
vertices of a path.  Changing an old adjacency can hit at most its two
incident centres.  A minimum edge set incident with every internal vertex
has size `ceil(d/2)`.  The twelve block paths are edge-disjoint, giving
(5.2).  Destroying these witnesses is only necessary, not sufficient, for
the stronger run floor `d+1`. \(\square\)

There is also no bounded literal Johnson seam between the two packets.  Any
primal owner `x` and literal dual owner `Omega-z` satisfy

\[
 |x\cap(\Omega-z)|=|x-z|\le4,\qquad
 d_J(x,\Omega-z)\ge r-4\ge d,                                 \tag{5.3}
\]

because the rank-`r` primal owners `x,z` both lie in one `(r+4)`-set.
Coordinate conjugacy can remove this particular distance bound, but not the
singleton-run invariant.

## 6. The formal inverse and the exact surviving gate

The fixed-flag algebra already contains the inverse action.  The coordinate
transposition `a<->b` sends the entire old primal phase to the new primal
phase, including its mixed screens.  A second primal copy run in the
opposite direction therefore cancels every lower flag signature while
retaining OR transparency and positive residence.  This is also a special
case of the saturated Pluecker-lattice theorem.

This cancellation is an identity of signed occurrence/flag vectors.  It
does not by itself imply Boolean support or hole cancellation without the
corresponding multiplicity and surviving-donor hypotheses.

It is not a physical solution: the inverse copy repeats the entire owner
set.  Adding a fixed private tag makes the owner sets disjoint but tags the
lower values as well, so their signatures no longer cancel.  The exact
construction target is therefore an **owner-disjoint physical inverse
packet whose tag disappears on both critical rays**, together with terminal
compiler feasibility.  The complement packet is not such an inverse.

The proposed intact primal--dual cancellation is therefore closed.  A
larger construction is not ruled out, but it must leave the unary packet
interface in three explicit ways:

1. it must use the crossing families in (2.2) as named witnesses for every
   deep lower loss `q>=5`;
2. it must change at least the adjacency floor (5.2), or replace the atom
   blocks by a positive-resident dual thickening; and
3. it must simultaneously cover the dual's complementary OR losses, rather
   than counting signed lower and upper defects separately.

Equivalently, the missing object is a coupled cross-deck braid with aperture
greater than four and a joint run transducer.  Pairing the two existing
packets without such a braid cannot prove `B(k)+O(1)` or exact equality.

Nothing here contradicts the flag-lattice theorem: that theorem supplies
every correction inside `U_d` (and every fixed-degree correction at depth
two).  The obstruction isolated here is precisely physical reachability,
owner separation, residence, cancellation beyond one fixed filler flag, and
the nonlinear terminal compiler state.

## 7. Exact replay and scope

Run

```bash
python3 scratch/audit_a_primal_dual_coatom_pair_nogo_20260801.py
```

The dependency-free replay checks `1<=d<=12` with `|K|=3`.  It verifies the
exact labelled rays (1.4), the prefix/suffix boundary differences, apertures
four, all `12d` strict dual singleton witnesses, the transposition
`a<->b`, the owner-distance bound, and all four natural same/crossed and
primal-first/dual-first deck pairings.  For every `d>=2`, each pairing has
exactly `2(d-1)` old-only and `2(d-1)` new-only values on each of the OR and
AND decks.

The all-`d`, arbitrary-`r` results are the symbolic proofs above.  The replay
does not independently prove the arbitrary-conjugacy argument, optimize the
edit floor, or reaudit the Pluecker lattice.  The concatenated natural pair
is a deck diagnostic, not a Johnson carrier; (5.3) explains why.  No K17
search is used.
