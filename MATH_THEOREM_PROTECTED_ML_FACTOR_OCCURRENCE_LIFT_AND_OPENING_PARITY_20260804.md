# Protected Middle-Levels factors: exact occurrence lift, opening loss, and phase parity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  No finite search or
computational construction is used.  The theorem closes the support-level
occurrence-address and local containment-prefix rows after a protected
Middle Levels factor has been chosen.  It does not supply a common-cap
suffix router, a capacity-faithful compiler embedding, or a connected
upper-decorated carrier.

## 0. Main conclusion

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},
\]

and let `ML_m` be their containment graph.  Let `Phi` be a spanning
two-factor of `ML_m`, and let `P subseteq Phi` be any protected incidence
bank.

After choosing an orientation of every component of `Phi`, every incidence
edge of `Phi` has a unique physical **half-turn address**.  If the edge is
`L--U`, that address records

\[
 (\text{component},\text{turn index},\text{left/right side},
   L,U,U\setminus L).
\tag{0.1}
\]

It gives a literal one-incidence containment prefix from the occurrence of
the lower turn `L` to the adjacent owner halfport `U`.  Different incidence
edges have different halfport addresses and these one-step prefixes have no
interior.  Their only possible endpoint collisions are exact:

\[
 \begin{array}{c|c}
 \text{shared resource}&\text{multiplicity in }P\\ \hline
 \text{lower-turn occurrence }L&d_P(L)\\
 \text{owner-cell occurrence }U&d_P(U)\\
 \text{halfport occurrence}&1.
 \end{array}
\tag{0.2}
\]

Thus a protected factor does more than provide an abstract edge: it provides
an occurrence address, a singleton coordinate label, and a local prefix with
an edge-private halfport and empty (hence private) interior.  Its lower source
or owner-cell alias need not be private.  It does **not** decide whether the
actual common-cap network uses the halfport as a separate unit gate or
identifies it with the shared owner cell.  Nor does it show that the local
prefix survives the fixed compensation linkage or reaches a typed unused
sink.

The other two exact conclusions are:

1. requested predecessor/successor or phase labels are realizable exactly
   when one parity bit is consistent on each factor component; and
2. opening every factor component loses the minimum possible number

   \[
    \sum_C\min_{L\in\mathcal L(C)}d_P(L)
    \le \left\lfloor {|P|\over3}\right\rfloor
   \tag{0.3}
   \]

   of protected internal halfports.  A lossless opening exists exactly when
   every component has a lower vertex of protected degree zero.

These statements identify which rows in the preselect-then-complete theorem
are automatic from factor serialization and which remain genuinely
compiler/common-cap-specific.

## 1. Suppressing one factor component

Fix a component `C` of `Phi`.  Orient and index it as

\[
 U_0-L_0-U_1-L_1-\cdots-U_{\ell-1}-L_{\ell-1}-U_0,
\tag{1.1}
\]

where indices are modulo `ell`, the `U_j` lie in `mathcal U`, and the `L_j`
lie in `mathcal L`.

Because `L_j` is contained in the two distinct rank-`m` sets `U_j` and
`U_{j+1}`, there are distinct coordinates `a_j,b_j` such that

\[
 U_j=L_j\cup\{a_j\},\qquad
 U_{j+1}=L_j\cup\{b_j\}.
\tag{1.2}
\]

Suppressing the lower shore gives the cyclic Johnson chronology

\[
 U_0,U_1,\ldots,U_{\ell-1}.
\tag{1.3}
\]

At its `j`-th turn,

\[
 U_j\cap U_{j+1}=L_j,
 \qquad
 U_j\cup U_{j+1}=L_j\cup\{a_j,b_j\}.
\tag{1.4}
\]

Define the two half-turn occurrences

\[
 h_j^-=(C,j,-;L_j,U_j,a_j),
 \qquad
 h_j^+=(C,j,+;L_j,U_{j+1},b_j).
\tag{1.5}
\]

The minus half is the predecessor/deletion side of the turn and the plus
half is the successor/insertion side.

### Theorem 1.1 (exact cyclic occurrence lift)

The map

\[
 U_jL_j\longmapsto h_j^- ,\qquad
 L_jU_{j+1}\longmapsto h_j^+
\tag{1.6}
\]

is a bijection from the incidence edges of `C` to its half-turn
occurrences.  Under this bijection:

1. the lower claim value is exactly `L_j`;
2. the adjacent owner/port value is exactly the displayed `U`;
3. the literal coordinate carried by the incidence is the singleton
   `U-L_j`; and
4. the complete lower and upper turn values are the two sets in (1.4).

#### Proof

Every edge of the alternating cycle (1.1) is uniquely either `U_jL_j` or
`L_jU_{j+1}`.  Equation (1.2) gives its unique singleton difference.
Conversely, every address in (1.5) names the corresponding edge in (1.1).
Equations (1.2)--(1.4) prove all value statements.  \(\square\)

The containment graph has no four-cycle.  Indeed, two distinct rank-`m-1`
sets with a common rank-`m` upper neighbour have a unique possible common
upper neighbour, namely their union.  Hence every component has

\[
                              \ell\ge3.
\tag{1.7}
\]

## 2. What the factor gives as a literal prefix

For each turn occurrence introduce a claim node `s_(C,j)`, and for each
incidence edge introduce its halfport node `p_e`.  The occurrence lift has
the canonical directed local arc

\[
             s_{(C,j)}\longrightarrow p_e
             \qquad(e\text{ incident with }L_j),
\tag{2.1}
\]

labelled by the literal containment `L_j subset U` and by the singleton
`U-L_j`.  Call this the **incidence-skeleton prefix**.

### Theorem 2.1 (exact local privacy and collision ledger)

For any `H subseteq Phi`, the incidence-skeleton prefixes belonging to `H`
have pairwise disjoint interiors.  More precisely:

1. distinct edges of `H` have distinct halfport nodes;
2. precisely `d_H(L)` prefixes start at the turn occurrence `L`;
3. after halfports with the same owner occurrence are identified with that
   owner cell, precisely `d_H(U)` prefixes end at the owner occurrence `U`;
4. there are no other occurrence collisions forced by the factor.

In particular, if physical capacity is assigned to incidence halfports,
the terminal ports are automatically distinct.  If capacity is assigned to
owner cells, right degree two is a real capacity collision rather than two
independent ports.

Repeated singleton labels `U-L` and repeated upper-turn values
`U_j union U_(j+1)` are possible.  They are values carried by the skeleton,
not additional occurrence nodes.  Any capacity quotient which identifies
equal labels or equal upper-turn values therefore requires a separate load
calculation; it is not covered by the three occurrence multiplicities above.

#### Proof

The arcs (2.1) have empty interiors.  Theorem 1.1 makes their halfport
terminals edge-labelled and therefore distinct.  Two factor edges have the
same lower endpoint exactly when their prefixes share a turn source, and
they have the same upper endpoint exactly when their halfports alias the
same owner cell.  These multiplicities are the two degrees in the table.
No further vertex occurs in a one-arc prefix.  \(\square\)

### Scope of the word “literal”

Theorem 2.1 is a literal statement in the serialized owner/q1 incidence
skeleton: both endpoint occurrences and the singleton containment label are
specified.  To regard (2.1) as a path in a residual common-cap network
`D'`, one still needs an occurrence-faithful embedding of these nodes and
arcs into `D'`.  That embedding must show that:

* the relevant turn source and port capacity were not deleted by the fixed
  compensation linkage;
* aliases use the correct common capacity gate;
* the phase, role, flags, and terminal type are legal in one materialized
  state; and
* later suffix paths meet a prefix only at its declared port.

These are compiler/common-cap premises.  They do not follow from the
existence of `Phi`.

## 3. Exact phase and role compatibility

Fix a reference orientation of every component.  For an incidence edge
`e` put

\[
 \sigma_C(e)=
 \begin{cases}
 0,&e\text{ is a minus/predecessor half in the reference orientation},\\
 1,&e\text{ is a plus/successor half in the reference orientation}.
 \end{cases}
\tag{3.1}
\]

Suppose a protected edge set `H` is assigned requested binary roles

\[
                         q:H\longrightarrow\{0,1\}.
\tag{3.2}
\]

The labels may mean predecessor/successor, alternating factor phase, or any
other role which is swapped by reversing a component.

This hypothesis on the role action is essential.  A phase datum which also
depends on an absolute root index or on an external chronology is not covered
unless its change under every allowed rerooting has first been reduced to the
same one-bit component action.

### Theorem 3.1 (one-bit-per-component criterion)

There are orientations of the components for which every protected edge
has its requested role if and only if, for every component `C`, the value

\[
                         q(e)\mathbin\oplus\sigma_C(e)
\tag{3.3}
\]

is constant over `e in H cap E(C)`.

In particular, the two incidences at one complete lower turn always receive
opposite roles.  Prescribing the same role to both is impossible.  Rooting
or cyclically shifting a component does not change this criterion.

#### Proof

Keeping the reference orientation leaves every `sigma_C(e)` unchanged;
reversing the component toggles every one of them.  Thus the only choice on
`C` is one bit `eta_C`, and the required equations are

\[
                         q(e)=\sigma_C(e)\oplus\eta_C.
\]

They have a solution precisely when (3.3) is constant.  The two edges at a
turn belong to opposite alternating classes, proving the special case.
\(\square\)

Thus an uncoloured protected-factor theorem does not automatically preserve
arbitrary phase labels.  It reduces their realization to the exact parity
test (3.3).

## 4. Linear opening: an exact formula and a sharp universal bound

To open component `C`, choose one lower turn `K_C in mathcal L(C)` and
delete the cyclic transition through it.  The two factor incidences at
`K_C` cease to be internal half-turn occurrences.  All other addresses and
roles remain unchanged in the resulting linear owner path.

Endpoint remnants of the two deleted incidences may be useful to a separate
boundary theorem, but they are not the same internal q1 occurrence and are
not counted as retained here.

### Theorem 4.1 (exact protected opening loss)

For a choice of one cut in every component, the number of protected
incidence occurrences lost from the internal chronology is exactly

\[
                         \sum_C d_P(K_C).
\tag{4.1}
\]

Consequently:

1. all protected incidences survive if and only if every component `C` has
   some lower vertex `L` with `d_P(L)=0`;
2. the minimum possible loss is

   \[
                         \sum_C\min_{L\in\mathcal L(C)}d_P(L);
   \tag{4.2}
   \]

3. for every protected bank,

   \[
    \sum_C\min_{L\in\mathcal L(C)}d_P(L)
       \le \left\lfloor {|P|\over3}\right\rfloor.
   \tag{4.3}
   \]

If `Phi` is one component, a lossless opening is automatic whenever the
lower support of `P` is a proper subset of `mathcal L`; in particular it is
automatic when `|P|<|mathcal L|`.

#### Proof

Opening at `K_C` deletes exactly the two factor edges incident with that
lower vertex, so its intersection with `P` has size `d_P(K_C)`.  This proves
(4.1) and the first two conclusions.

Let `ell_C=|mathcal L(C)|` and `b_C=|P cap E(C)|`.  Every protected edge has
one lower endpoint in `C`, hence

\[
 \sum_{L\in\mathcal L(C)}d_P(L)=b_C.
\]

Therefore

\[
 \min_L d_P(L)\le {b_C\over\ell_C}\le {b_C\over3}
\]

by (1.7).  Sum over components and use integrality to obtain (4.3).  In one
component, protected degree at least one at every lower vertex would force
`|P|>=|mathcal L|`, proving the stated scalar corollary.  More directly, a
proper lower support contains a degree-zero cut, proving the stronger support
formulation.  \(\square\)

Opening all components gives a family of linear owner paths.  Concatenating
their lists does **not** make the seams Johnson-adjacent and does not preserve
upper witnesses or residence across the seams.  A connector or pull theorem
is still required to obtain one global carrier.

## 5. Consequences for preselect-then-complete

Apply the preselection theorem with an injection

\[
                         \iota:I\hookrightarrow\mathcal L.
\]

### One occurrence coordinate

For the protected matching

\[
 M_0=\{\iota(i)\mu_0(i):i\in I\},
\]

factor serialization automatically gives:

1. a distinct lower-turn occurrence for every gain;
2. a distinct incidence halfport for every selected edge;
3. a distinct owner **value** for every selected edge, because `mu_0` is a
   matching;
4. the literal singleton label `mu_0(i)-iota(i)`; and
5. edge-private incidence-skeleton prefix interiors.

Thus the occurrence-address and local-prefix part of the former open row is
automatic, subject only to choosing cuts which retain the edge.

### Two occurrence coordinates

For

\[
 M_{01}=M_0\cup M_1,
\]

the two selected incidences at `iota(i)` exhaust the degree of that lower
turn in the completed factor.  Hence they become exactly the two opposite
halfports of one prescribed turn.  In addition:

1. the `2|I|` halfport addresses are distinct;
2. owner values are distinct inside each coordinate and have multiplicity
   at most two in the union;
3. the two coordinate roles at one gain are necessarily opposite;
4. all requested global phase labels are realizable exactly when Theorem
   3.1 holds; and
5. if the same owner value is used once in each coordinate, the two
   halfports are distinct but alias one owner-cell occurrence.  Those two
   incidences also have opposite factor-side roles, because they exhaust the
   two incidences at that owner.

If the completed factor is Hamiltonian and `|I|<|mathcal L|`, the whole
two-coordinate bank has a lossless opening: its lower support is exactly
`iota(I)`, even when its edge count `2|I|` is at least `|mathcal L|`.

Therefore a halfport-capacity model sees two distinct ports in item 5,
whereas an owner-cell-capacity model sees one shared unit gate.  The latter
cannot be replaced by the abstract right-degree-two statement.

## 6. Revised status of the physical rows

The factor theorem and serialization now prove unconditionally:

* the cyclic occurrence address of every selected incidence;
* its lower turn, owner value, singleton coordinate, and predecessor or
  successor side after an orientation is chosen;
* a one-step containment prefix with edge-private halfport and empty interior
  in the incidence skeleton;
* the exact endpoint collision ledger (0.2);
* the exact componentwise phase criterion (3.3); and
* the exact opening-loss formula (4.1), including the universal bound
  (4.3).

The following remain genuine external premises:

1. **cap activation:** embedding the skeleton prefix in the same residual
   cap/guard/occurrence state after the compensation linkage;
2. **capacity identity:** deciding whether two halfports alias one physical
   cell and pricing that shared gate correctly;
3. **source multiplicity:** supplying two independent source units when two
   coordinate tickets, rather than one factor claim choosing one port, must
   route simultaneously;
4. **typed suffix router:** simultaneous disjoint suffixes to distinct legal
   unused sinks, or the equivalent strict-gammoid/full-cut certificate;
5. **product closure:** compatibility of the two occurrence coordinates in
   one common state, including structural zeros and transported phase 1;
6. **global carrier:** bounded-component joining, upper palettes,
   arbitrary-width witnesses, residence, and safe seams.

In particular, the suffix-router rank

\[
                 r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|
\]

does not follow from occurrence serialization.  The factor now supplies a
canonical local prefix candidate; the common-cap theorem must still supply
the suffix expansion and capacity-faithful activation.

## 7. Dependencies

* `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
  supplies the protected spanning two-factor.
* `MATH_THEOREM_PRESELECT_THEN_COMPLETE_MIDDLE_LEVELS_BOOLEAN_ROUTER_20260804.md`
  supplies the selected one- or two-coordinate incidence bank.
* `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`
  states the exact suffix-router premise after a literal prefix bank is
  active.
