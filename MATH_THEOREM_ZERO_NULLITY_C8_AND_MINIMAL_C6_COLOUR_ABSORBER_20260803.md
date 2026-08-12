# A zero-nullity protected C8 actuator and the minimal Boolean C6 colour absorber

**Date:** 2026-08-03  
**Status:** unconditional local owner/q1 theorems.  The first construction
gives a prospectively plantable odd topology actuator whose protected turns
have no repeated immediate-upper colour.  The second classifies every
simple upper-valid incidence `C6` exchange and gives an explicit Boolean
two-for-two colour absorber.  These results do not prove that the required
reserve occurrences coexist in one global upper-exact resident carrier.

## 0. Outcome

At the owner/immediate-upper layer there are two logically different local
currencies.

1. A four-cycle successor toggle changes component parity.  It can be
   housed in four private saturated `C8` components with all sixteen turn
   colours distinct.  Thus parity can be prepared with zero local Catalan
   duplicate charge.
2. A three-cycle successor toggle has even topology action but is the
   smallest possible colour-changing Boolean circuit.  Every simple
   upper-valid `C6` is controlled by three exterior labels.  It is either
   colour-neutral, changes two colours for two colours, or changes all
   three.  A one-for-one `C6` exchange is impossible.  The two-for-two case
   is an exact Boolean rectangle and repairs a missing colour whenever the
   two displaced colours have reserve occurrences.

Consequently the neutral `C8` fibre cannot itself repair colour support.
The first additional circuit needed is a `C6`, and its sharp nonzero colour
footprint is two old values versus two new values.

Throughout let the ground set have order `2m-1`.  Lower vertices have rank
`m-1`, owner vertices rank `m`, and immediate-upper colours rank `m+1`.

## 1. A zero-nullity saturated-private odd socket

Assume `m>=6`.  Choose

* a set `S` of rank `m-2`;
* distinct petals `a_0,a_1,a_2,a_3` outside `S`;
* an exterior point `e` outside `S` and the petals;
* distinct points `z_0,z_1,z_2,z_3 in S`; and
* one further point `f` outside
  `S union {a_0,a_1,a_2,a_3,e}`.

Indices are cyclic modulo four.  Define

\[
\begin{aligned}
 C_i&=S+a_i,\\
 T_i&=S+a_i+a_{i+1},\\
 R_i&=S+a_i+e,\\
 D_i&=(S-z_i)+a_i+e,\\
 Q_i&=(S-z_i)+a_i+e+f,\\
 E_i&=(S-z_i)+a_i+f,\\
 V_i&=(S-z_i)+a_i+a_{i+1}+f,\\
 A_i&=(S-z_i)+a_i+a_{i+1}.
\end{aligned}                                             \tag{1.1}
\]

The lower vertices are `C_i,D_i,E_i,A_i`; the owners are
`T_i,R_i,Q_i,V_i`.

### Lemma 1.1 (four private rainbow octagons)

For every `i`,

\[
 T_i-C_i-R_i-D_i-Q_i-E_i-V_i-A_i-T_i                 \tag{1.2}
\]

is a simple incidence `C8`.  The four cycles are pairwise vertex-disjoint.
Their sixteen immediate-upper turn colours are pairwise distinct.

#### Proof

Every consecutive pair in (1.2) is a containment by (1.1).  Within one
cycle the four owners, and separately the four lower vertices, have
different exterior or puncture data.  Across cycles, punctured vertices are
distinguished by the missing `z_i`: a punctured vertex from cycle `i`
contains `z_j` and omits `z_i`, while one from cycle `j` does the reverse.
Unpunctured vertices are distinguished by their petal sets, and a punctured
vertex cannot equal an unpunctured one because the latter contains all of
`S`.  Hence the cycles are simple and disjoint.

The four turn colours on the `i`-th cycle are

\[
\begin{aligned}
 B_i&=R_i\cup T_i=S+a_i+a_{i+1}+e,\\
 X_i&=R_i\cup Q_i=S+a_i+e+f,\\
 Y_i&=Q_i\cup V_i=(S-z_i)+a_i+a_{i+1}+e+f,\\
 Z_i&=V_i\cup T_i=S+a_i+a_{i+1}+f.
\end{aligned}                                             \tag{1.3}
\]

They are distinct: `Y_i` is the only one missing `z_i`, and the other
three are distinguished by which one of `a_(i+1),e,f` is absent.  Across
indices, the punctured colours `Y_i` are distinguished by their missing
`z_i`.  Among the full-`S` colours, the exterior triples have the forms

\[
 \{a_i,a_{i+1},e\},\qquad
 \{a_i,e,f\},\qquad
 \{a_i,a_{i+1},f\}.                                  \tag{1.3a}
\]

The three families are separated by the presence of `e,f`, and within a
family their singleton or cyclic petal pair distinguishes the index.  Thus
all sixteen colours are distinct.
\(\square\)

At `C_i`, take `C_iT_i` as the old successor incidence and
`C_iT_(i-1)` as the new one.  Phase all four private cycles coherently so
that

\[
 \begin{aligned}
 M_0&:\ C_iR_i,\ D_iQ_i,\ E_iV_i,\ A_iT_i,\\
 M_1&:\ C_iT_i,\ D_iR_i,\ E_iQ_i,\ A_iV_i.
 \end{aligned}                                           \tag{1.3b}
\]

Thus the toggle changes only the four displayed `C_i` edges of `M_1`.

### Theorem 1.2 (zero-nullity odd actuator)

Toggling

\[
                 \{C_iT_i:0\le i<4\}
       \longleftrightarrow
                 \{C_iT_{i-1}:0\le i<4\}              \tag{1.4}
\]

has the following properties.

1. It merges the four private cycles (1.2) into one cycle.
2. It preserves every lower and owner degree.
3. Relative to a fixed predecessor matching, it changes the successor
   permutation by a four-cycle and hence flips component parity.
4. It preserves the complete immediate-upper multiplicity vector.
5. Both phases have sixteen distinct protected turn colours, so the socket
   has zero immediate-upper repeat excess.

#### Proof

Deleting `C_iT_i` opens the `i`-th private cycle into a path from `C_i` to
`T_i`.  The new edge joins its `C_i` end to the `T_(i-1)` end of the
preceding path.  The index map is one four-cycle, so the four paths close
into one cycle.  Endpoint degrees and the two matching shores are
unchanged.

Only the turn at `C_i` changes.  Its old colour is `B_i`; its new colour is

\[
 R_i\cup T_{i-1}=S+e+a_{i-1}+a_i=B_{i-1}.             \tag{1.5}
\]

Thus the four `B` colours are permuted, while the twelve `X,Y,Z` colours
are fixed.  Lemma 1.1 proves zero repeat excess in both phases. \(\square\)

### Proposition 1.3 (sharpness of the off-phase saturated support)

Among odd sockets in which the four old toggle incidences lie in four
vertex-disjoint saturated protected components and all protected turn
colours are distinct, the `32` planted off-phase incidences in (1.2) are
minimum.  This is a statement about the saturated off-phase host: the
union of both toggle phases also contains the four new cross incidences in
(1.4), for `36` distinct incidences in total.

#### Proof

The middle-levels incidence graph has no simple `C4`.  Hence every
saturated component has length at least six.  An incidence `C6` is the
boundary of one Boolean rank-two interval: its three lower turns all have
the same rank-`(m+1)` union.  Such a component has repeat excess two and is
forbidden by zero nullity.  Therefore every one of the four private
components has length at least eight.  The construction uses exactly four
`C8` components and attains `4*8=32`. \(\square\)

### Corollary 1.4 (protected planting)

Let `P` be a 2-bounded protected incidence bank with `p` edges, occupying
`b_-` lower and `b_0` owner vertices.  If

\[
                 16(b_-+b_0)<W,
        \qquad p+32\le m-2,                            \tag{1.6}
\]

then a relabelled copy of the off socket is disjoint from `P`, and
`P` together with that complete socket extends to a spanning two-factor.
Both socket phases preserve `P` and have the same immediate-upper palette.

#### Proof

A random coordinate relabelling makes each of the sixteen socket lower
vertices uniform on the lower shore and each of its sixteen owners uniform
on the owner shore.  Hence the expected number of vertex collisions with
`P` is

\[
             {16b_-\over W}+{16b_0\over W}
             ={16(b_-+b_0)\over W}<1.
\]

Thus a disjoint copy exists.  Its union with `P` is
2-bounded and has at most `m-2` protected incidences.  Apply the protected
middle-levels two-factor extension theorem.  Every private socket vertex is
already saturated, so the four cycles remain separate before the toggle.
Theorem 1.2 applies afterward. \(\square\)

This is a prospective q1 statement.  The arbitrary exterior completion
need not be upper-surjective, resident, or compatible with deeper shadows.
The extension theorem is unphased: if `P` carries named predecessor/
successor pins, their ordinary component-parity consistency must still be
checked.  The four private socket cycles themselves have the coherent
phasing (1.3b).

## 2. Classification of the simple Boolean C6 exchange

Assume `m>=3`.
Let a simple incidence `C6` toggle one successor matching into another.
Write its three successor owners as `B_0,B_1,B_2` and its lower vertices as

\[
                         L_i=B_i\cap B_{i-1}.           \tag{2.1}
\]

Suppose a fixed predecessor owner `A_i` contains `L_i`, and require both
the old and new turns at `L_i` to have rank `m+1`; thus neither predecessor
edge coincides with a successor edge.

### Lemma 2.1 (top-and-exterior normal form)

There are a rank-`(m+1)` set `R`, distinct holes
`b_0,b_1,b_2 in R`, and exterior points `e_i notin R` such that

\[
 B_i=R-b_i,qquad
 L_i=R-\{b_i,b_{i-1}\},qquad
 A_i=L_i+e_i.                                          \tag{2.2}
\]

The old and new colours are

\[
 O_i=(R-b_i)+e_i,qquad
 N_i=(R-b_{i-1})+e_i.                                  \tag{2.3}
\]

#### Proof

The three `B_i` form a triangle of the Johnson graph.  A Johnson triangle
is either a star with one common rank-`(m-1)` core or the three facets of
one rank-`(m+1)` top.  In the star case all three intersections in (2.1)
are the same lower vertex, contradicting simplicity.  Hence the triangle
is the top form in (2.2).

The only points of `R` outside `L_i` are `b_i,b_(i-1)`.  Choosing either as
the extra point of `A_i` would make `A_i` equal one of the two successor
owners and would give a non-upper turn.  Therefore the extra point `e_i`
lies outside `R`.  Equation (2.3) follows by taking unions. \(\square\)

### Theorem 2.2 (sharp C6 palette trichotomy)

For a simple upper-valid `C6` exchange, the number of colours common to the
old and new three-element palettes is `0`, `1`, or `3`, never `2`.
Consequently the exchange is exactly one of:

* a neutral permutation of all three colours;
* a two-old-for-two-new exchange; or
* a three-old-for-three-new exchange.

In particular, a nonneutral `C6` changes at least two old and two new
colours, and this lower bound is sharp.

#### Proof

By (2.3),

\[
                         O_i=N_j
\]

holds exactly when `e_i=e_j` and `b_i=b_(j-1)`, hence exactly when
`j=i+1` and `e_i=e_(i+1)`.  The number of common colours is therefore the
number of equal adjacent pairs in the cyclic word
`(e_0,e_1,e_2)`.  It is zero when all labels are distinct, one when exactly
two are equal, and three when all are equal.  Two equal adjacencies force
the third by transitivity.  Within either phase the three colours are
pairwise distinct, because equality would require both the exterior label
and the omitted hole to agree. \(\square\)

There is no smaller simple endpoint-preserving Boolean circuit: a matching
exchange lives on an even incidence cycle, and the middle-levels graph has
no `C4`.  Thus `C6` is the first possible colour actuator, while Theorem
2.2 gives its sharp nonzero colour footprint.

## 3. The explicit two-for-two colour rectangle

Assume `m>=4`.  Choose `R`, `b_0,b_1,b_2` as above and two distinct
exterior points `e,f notin R`.  Set

\[
                         e_0=e_1=e,qquad e_2=f.        \tag{3.1}
\]

Then the old colours are

\[
 (R-b_0)+e,quad (R-b_1)+e,quad (R-b_2)+f,            \tag{3.2}
\]

and the new colours are

\[
 (R-b_2)+e,quad (R-b_0)+e,quad (R-b_1)+f.            \tag{3.3}
\]

After cancelling the common first colour, the exact palette exchange is

\[
 \boxed{
 \{(R-b_1)+e, (R-b_2)+f\}
 \longleftrightarrow
 \{(R-b_2)+e, (R-b_1)+f\}.}                          \tag{3.4}
\]

It is the Boolean rectangle obtained by swapping the two exterior labels
across the two holes `b_1,b_2`.

### Theorem 3.1 (reserve-witness colour absorption)

Let a spanning two-factor contain the old phase of the `C6` in Section 3,
with the predecessor incidences `L_iA_i` fixed.  Suppose

* both old-only colours in the left side of (3.4) have occurrences outside
  the six toggled incidences; and
* at least one new-only colour on the right side of (3.4) is missing from
  the factor.

Then toggling the `C6` preserves all endpoint capacities and loses no
previously covered upper colour.  It decreases the number of missing upper
colours by the number of new-only colours that were previously missing.

#### Proof

The two successor phases are perfect matchings on the same three lower and
three owner vertices, so every incidence degree and every tail/head
capacity is unchanged.  All turns outside the circuit are fixed.  The
common colour in (3.2)--(3.3) remains on the circuit.  Each displaced
old-only colour survives at its stipulated reserve occurrence, while each
previously missing new-only colour is created by (3.3). \(\square\)

The theorem is an all-`m` local absorber, but its host hypotheses are real:
the old `C6`, its predecessor phase, and the two reserve witnesses must
coexist.  Aggregate duplicate count alone does not plant this rectangle.

### Proposition 3.2 (raw prospective supply through every target)

Fix a rank-`(m+1)` colour `Y`, and designate it as the new colour
`(R-b_2)+e` in (3.3).  The number of labelled parameter tuples

\[
                         (R,b_0,b_1,b_2,e,f)
\]

realizing that designation is exactly

\[
 (m+1)(m-2)m(m-1)(m-3).                              \tag{3.5}
\]

#### Proof

Choose `e in Y` in `m+1` ways and `b_2 notin Y` in `m-2` ways; then

\[
                         R=(Y-e)+b_2
\]

is forced.  Choose the ordered pair `(b_1,b_0)` from
`R-\{b_2\}=Y-\{e\}` in `m(m-1)` ways.  Finally, `R` has `m-2` exterior
points, one of which is `e`, so the distinct second exterior `f` has
`m-3` choices.  Every construction step is reversible from the labelled
tuple and designated target slot. \(\square\)

This is raw prospective supply, not a neighbourhood count after `M_0` and
the old factor are frozen.  The predecessor incidences `L_iA_i`, both old
successor reserve colours, and the topology placement still have to be
selected jointly.

## 4. The exact coordinate-current invariant

The two-for-two form is not an accident.  Every closed successor-circuit
toggle preserves the coordinate-degree vector of its upper-colour
multiset.

### Theorem 4.1 (circuit current conservation)

Let a simple incidence `C_(2s)` have successor owners `B_i`, lower vertices

\[
                         L_i=B_i\cap B_{i-1},
\]

and fixed predecessor owners `A_i` containing `L_i`.  Assume both turns at
every `L_i` have rank `m+1`.  If `O_i=A_i union B_i` and
`N_i=A_i union B_(i-1)`, then, as coordinate-incidence vectors,

\[
                         \sum_i 1_{O_i}=\sum_i1_{N_i}. \tag{4.1}
\]

#### Proof

Write

\[
 B_i=L_i+p_i,
 \qquad
 B_{i-1}=L_i+q_i.
\]

Upper validity forces the one point of `A_i-L_i` to differ from both
`p_i,q_i`.  Hence

\[
 1_{N_i}-1_{O_i}=1_{q_i}-1_{p_i}.                    \tag{4.2}
\]

Traversing the closed Johnson walk `B_0,B_1,...,B_(s-1),B_0`, the labels
`q_i` are exactly the coordinate departures and the labels `p_i` exactly
the coordinate arrivals.  Every coordinate has equally many arrivals and
departures on a closed walk.  Summing (4.2) proves (4.1). \(\square\)

There is also a global form which does not mention a chosen circuit.

### Theorem 4.2 (uniform turn current of two perfect matchings)

Let `M_0,M_1` be edge-disjoint perfect matchings of the middle-levels
incidence graph on `[2m-1]`.  For each lower vertex `L`, put

\[
                         U_L=M_0(L)\cup M_1(L).
\]

Then every ground coordinate occurs in exactly

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}                \tag{4.3}
\]

members of the turn multiset `(U_L:L in mathcal L)`.

#### Proof

Fix a coordinate `x`.  It belongs to

\[
                         B={2m-2\choose m-2}
\]

lower vertices.  For either perfect matching `M`, exactly

\[
                         A={2m-2\choose m-1}
\]

matched owners contain `x`, because every owner occurs once.  The `B`
lower vertices already containing `x` account for `B` of these incidences;
therefore `x` is the added matching label at exactly `A-B` lower vertices.
The two matchings are edge-disjoint, so their two added labels at one lower
vertex are distinct.  Hence the turn count is

\[
                         B+2(A-B)=2A-B.
\]

This is independent of `x`. \(\square\)

### Corollary 4.3 (Catalan duplicates form a one-design)

Suppose the turn multiset of Theorem 4.2 covers every rank-`(m+1)` upper
colour.  Subtract one copy of every upper colour, leaving its Catalan
duplicate multiset.  Then

* it has exactly `Cat_m` blocks; and
* every coordinate occurs in exactly

\[
                         2\operatorname{Cat}_{m-1}    \tag{4.4}
\]

duplicate blocks.

#### Proof

Every coordinate belongs to

\[
 {2m-2\choose m}={2m-2\choose m-2}=B
\]

members of the complete upper layer.  Subtracting this from (4.3) leaves

\[
 2(A-B)={2\over m}{2m-2\choose m-1}
       =2\operatorname{Cat}_{m-1}.                   \tag{4.5}
\]

The block count is `W-|mathcal U|=Cat_m`. \(\square\)

### Corollary 4.4 (rooted opening gives a punctured one-design)

Open such a cycle factor by deleting the successor incidence at one lower
vertex `o`, and suppose its turn colour

\[
                         U_o=M_0(o)\cup M_1(o)
\]

still occurs elsewhere, so the resulting `W-1` turns remain
upper-surjective.  Their duplicate multiset has `Cat_m-1` blocks, and the
replication number of coordinate `x` is exactly

\[
              2\operatorname{Cat}_{m-1}-1_{\{x\in U_o\}}.    \tag{4.6}
\]

#### Proof

Opening removes exactly the one turn block `U_o` from the cyclic multiset.
Apply Corollary 4.3 coordinatewise. \(\square\)

Thus even the duplicate current of a rooted upper-exact Hamilton path is
not free: it is a one-design punctured by its lost opening colour.

Thus no closed local circuit can change the coordinate current.  The `C6`
rectangle is the smallest nontrivial **balanced** repair.  A proposed
isolated missing-colour correction whose multiplicity change has nonzero
coordinate current is impossible without changing endpoints, opening the
factor, or coupling it to further colour changes.  The reserve hypotheses
in Theorem 3.1 must ultimately be supplied in a way consistent with the
one-design law (4.4).

## 5. Separation of colour and topology controls

An alternating `C_(2s)` successor toggle changes component parity by
`s-1 mod 2`.  Hence:

* the `C6` absorber has even topology action and cannot correct the final
  parity obstruction by itself;
* the `C8` socket has odd topology action and cannot repair a missing
  colour because its full colour multiplicity vector is identical in both
  phases.

Together they provide independent local generators:

\[
 \boxed{
 \text{C6: nontrivial colour rectangle, even topology action};
 \qquad
 \text{C8: neutral colour action, odd topology action}.}
                                                               \tag{5.1}
\]

In circuit length, this is the smallest possible circuit pair in the
Boolean incidence host.
The no-`C4` lemma excludes any smaller matching exchange; Theorem 2.2
excludes a one-for-one simple `C6` repair; and a neutral circuit cannot
alter colour support by definition.

## 6. Exact remaining global lemma

At the owner/q1 layer, a sufficient absorber theorem can now be stated
without ambiguity.

> **Prepared rectangle-and-parity host.**  Starting from an exact
> fractional colour--tail--head cycle selector, round to a spanning
> two-factor which contains:
>
> 1. for every missing upper colour, a sequence of `C6` rectangles whose
>    displaced colours have protected reserve occurrences and whose new
>    sides introduce that colour; and
> 2. one protected zero-nullity `C8` socket disjoint from those rectangles.
>
> After the colour rectangles make the factor upper-surjective, use even
> component joins and the `C8` parity phase to obtain the required topology.

The local algebra, endpoint conservation, minimal circuit sizes, and
palette accounting are proved above.  What remains open is the correlated
Boolean rounding/planting theorem supplying the reserve witnesses and the
required component placement simultaneously.  Neither the exact
fractional selector nor the local sockets alone imply that host.
