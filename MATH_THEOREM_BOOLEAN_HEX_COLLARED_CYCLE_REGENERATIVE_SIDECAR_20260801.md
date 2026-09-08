# Regenerative composition of bounded square-collared cycle actuators

Date: 2026-08-01  
Status: exact bounded central sidecar and exact conditional
`B(k)+O(1)` implication.  The central cycle row resets to zero.  Residence,
arbitrary-width upper witnesses, and the occurrence-labelled common cap are
explicit additional hypotheses; the Pascal child is **not** proved to
export the required collars.

**Phase-decoupling update.**  The strong version above asks for more than
the bounded-spine theorem needs.  The old phase may be carried as an
auxiliary owner/q1 state while the all-new phase is physicalized and
compiled afresh.  Consequently a terminal compiler and terminal upper
witness occurrences need not survive the phase change.  The exact reduced
statement, together with a shortest resident return rail, is proved in
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`.

## 0. Outcome

One square-collared ternary-hex actuator has two six-atom phases with the
same complete four-resource signature:

\[
\begin{array}{c|c|c}
 &\text{old phase}&\text{new phase}\\ \hline
\text{physical topology}&C_4+P_1+P_1&P_5+P_1\\
\text{external tail sockets}&A,C&A,C\\
\text{external head sockets}&B,D&B,D\\
\text{socket pairing}&A\to B,\ C\to D&A\to D,\ C\to B.
\end{array}                                                   \tag{0.1}
\]

Its typed signature consists of exactly six lower colours, six upper
colours, six tail resources and six head resources.  Its physical record
uses eight middle vertices and exports four named sockets.

A private bank of `H` such actuators is therefore a literal Boolean
`H`-cube of central factors.  All `2^H` phase vectors have the same complete
four-resource support.  If the surrounding bulk is a physically disjoint
forest, setting all phase bits to new removes exactly `H` cycles and returns
a forest.  The operation is count-neutral and commuting.

This is the exact bounded cycle sidecar needed by a regenerative proof.  It
does not by itself say that an arbitrary Pascal child contains the old
phase, nor that either phase is a legal OR-word chronology.

## 1. A path-collar principle

The square in the explicit actuator is only the shortest return collar.

### Theorem 1.1 (guardable return path)

Let a ternary packet have old and new physical phases

\[
 O=\{AB,CD,EF\},\qquad N=\{AF,CB,ED\}.                 \tag{1.1}
\]

Let `R` be any directed physical path from `F` to `E` such that:

1. `O union R` is a four-resource matching;
2. every internal vertex of `R` avoids `A,B,C,D`; and
3. `R` is otherwise resource-private from the packet.

Then

\[
                         O\cup R\longrightarrow N\cup R       \tag{1.2}
\]

preserves all four typed resource multisets.  The old physical graph is one
cycle `EF union R` plus the paths `AB,CD`; the new physical graph is the two
paths

\[
                         A-F\,R\,E-D,
              \qquad     C-B.                                  \tag{1.3}
\]

#### Proof

The packet identity gives `res(O)=res(N)`, while `R` is unchanged.  Removing
`EF` opens the old cycle as the directed path `F R E`; replacing the three
packet edges joins it between `A` and `D` and cross-connects `C` to `B`.
The privacy hypotheses make both unions typed matchings.  `square`

The Johnson-square collar in
`MATH_THEOREM_BOOLEAN_HEX_SQUARE_COLLAR_CYCLE_ACTUATOR_20260801.md`
is the length-three instance

\[
                         F\to X\to Y\to E.                       \tag{1.4}
\]

Theorem 1.1 matters for guards: a future construction may replace the
three-edge square by a longer resident rail without changing the central
resource proof.

## 2. Exact bounded sidecar

Let `F_0` be a four-resource matching whose physical projection is a
linear forest.  Let

\[
                    \mathcal G=\{(G_i^-,G_i^+):1\le i\le H\}    \tag{2.1}
\]

be resource-private collared actuators, physically vertex-disjoint from
`F_0` and from one another.  For a phase vector
`epsilon in {-,+}^H`, put

\[
                    M(\epsilon)=F_0\cup\bigcup_iG_i^{\epsilon_i}.
\tag{2.2}
\]

### Theorem 2.1 (Boolean sidecar cube)

Every `M(epsilon)` is a four-resource matching and all of them have the
same complete lower, upper, tail and head signature.  Its physical cycle
count is exactly

\[
                         |\{i:\epsilon_i=-\}|.                    \tag{2.3}
\]

The reset

\[
                         \mathfrak R:M(\epsilon)\mapsto M(+,\ldots,+)
\tag{2.4}
\]

is independent of toggle order, preserves every immediate palette, and
returns a physical linear forest.

The sidecar has the following bounded arity:

\[
\begin{array}{c|c}
\text{record}&\text{per actuator}\\ \hline
\text{typed boundary resources}&6+6+6+6=24\\
\text{physical middle vertices}&8\\
\text{external sockets}&4\\
\text{phase state}&1\text{ bit}.
\end{array}                                                   \tag{2.5}
\]

Thus an `H`-actuator sidecar carries at most `24H` typed tokens, `8H`
physical vertices, `4H` sockets and `H` phase bits.  Labels depend on the
dimension, but the number of records is bounded.

#### Proof

One actuator has equal phase signatures by the square-collar theorem.
Privacy makes signatures add disjointly over the bank and with `F_0`, so
every phase vector is a matching with the same support.  Its old phase has
one cycle and its new phase has none.  Physical vertex-disjointness makes
the component counts additive and the toggles commute.  This proves
(2.3)--(2.5).  `square`

### Corollary 2.2 (cycle defect is a reset row)

For a carried defect vector

\[
        x=(x_{\rm cyc},x_{\rm run},x_{\rm up},x_{\rm cap},\ldots),
\tag{2.6}
\]

an exported private collared bank of order at most `H` gives the exact
central transition

\[
                              x_{\rm cyc}\le H\longmapsto0.       \tag{2.7}
\]

No fresh graphic sink is consumed: each balanced toggle returns two path
components.  Equations for the other rows do not follow from (2.7).

## 3. What is automatic and what is not

The reset automatically preserves precisely the following data.

1. The selected atom count.
2. The complete immediate lower palette.
3. The complete immediate upper palette.
4. Every typed tail capacity and head capacity.
5. The four named external socket sets; only their pairing changes as in
   (0.1).
6. Physical maximum indegree/outdegree one, and—after reset—acyclicity.

The following OR-word guards are **not** automatic.

### 3.1 Residence and erosion envelopes

The four-resource identity sees only which middle vertices occur as tails
and heads, not their positions in one linear owner chronology.  A square
collar may create coordinate runs shorter than the required `d+1`, and an
external splice may do the same.  A guarded record must therefore contain
either

* one literal chronology in which both packet phases satisfy every declared
  run lower bound; or
* a longer return path from Theorem 1.1 with a proved resident-rail
  schedule and phase-compatible endpoint ages.

The certificate must be checked after the actuator paths are ordered with
the bulk; componentwise residence is insufficient.

### 3.2 Arbitrary-width upper witnesses

Equality of the six immediate upper colours proves only the `q=1` row.
Every interval crossing an edited collar can change at widths `q>=2`.
For every protected upper target, the record must name either

* an old witness interval disjoint from all collar cuts in both phases; or
* a phase-specific recreated ladder.

Equivalently, the exact cut-transversal criterion must certify that no
target loses all of its witnesses.  Marginal upper coverage in the two
phases is not enough because the physical occurrence labels must coexist in
one chronology.

### 3.3 Common cap and the one-cell star

The lower compiler is occurrence-labelled.  Palette equality does not
preserve its SDR or alternating linkage.  Each guarded record must carry

* the changed cap halo;
* source entrances for every displaced lower obligation;
* vertex-disjoint (or otherwise jointly Rado-certified) paths to the free
  sink bank; and
* all protected compiler resources consumed by those paths.

If a collar is realized through an inserted source cell, the fan and the
destroyed crossing values obey the star-hidden identity

\[
                    Z\cup C_i=L_{i+1}\cup R_{d-i+1}.              \tag{3.1}
\]

Only star coordinates with interval-zero crossing traces are programmable.
Thus a free fan target and a free crossing repair cannot be specified
independently.

These three guard rows are logically independent of the central reset.  A
claim that the square collar proves `B(k)+O(1)` without them would be false.

## 4. Guarded regenerative state

An **`(H,s,h)` guarded collared state** consists of:

1. a central decomposition (2.2) with at most `H` actuators;
2. a literal physicalization of the all-new reset state of length at most
   `B(k)+s`;
3. joint residence, arbitrary-width upper-witness, and common-cap
   certificates on that same chronology; and
4. a terminal family of at most `h` uncovered literal masks.

For an auxiliary state intended for the next Pascal step, the exported
record additionally names at most `H` old-phase collars in the child and
their four socket labels.  Exportability means that the three guard
certificates are regenerated in the child; terminal appending does not
count as regeneration.

### Theorem 4.1 (exact composition)

Suppose one compatible infinite odd spine has guarded collared odd states
and guarded collared even terminal children with uniform parameters
`(H,s,h)`.  Then

\[
                             \nu(k)\le B(k)+s+h                 \tag{4.1}
\]

for every sufficiently large `k`.

More generally, if the terminal hole family `\mathcal H_k` has uniformly
bounded repair complexity `R(\mathcal H_k)<=r`, then

\[
                             \nu(k)\le B(k)+s+r.                 \tag{4.2}
\]

#### Proof

Apply the central reset (2.4).  It changes neither physical length nor any
immediate resource and yields the certified all-new forest chronology.
Items 2--3 in the state definition make this a legitimate defective
terminal physical word of length at most `B(k)+s`, rather than merely a
central factor.  Append the at most `h` missing masks literally, or append a
shortest repair word of length `r`.  The bounded-defect odd-spine theorem
then applies independently in each dimension; terminal repairs are not
carried to the next auxiliary state.  `square`

### Corollary 4.2 (explicit per-actuator ledger)

Suppose the non-actuator construction contributes length excess `s_0` and
at most `h_0` terminal holes.  Suppose every one of at most `H` guarded
actuators can be realized with at most `s_1` extra source positions and at
most `h_1` additional terminal casualties, jointly without overlap.  If the
child exports another bank of order at most `H`, then

\[
              \boxed{\nu(k)\le B(k)+C},\qquad
              C=s_0+Hs_1+h_0+Hh_1.                            \tag{4.3}
\]

Replacing literal listing by a joint repair word replaces the last two
terms by its uniform repair complexity.

This is an implication, not a construction of the hypotheses.

## 5. The exact remaining theorem

The central cycle sidecar is now finished.  The unproved all-dimensional
statement has the following narrow form.

> **Guarded collar export.**  The same-parity Pascal child can be chosen so
> that every bounded physical cycle debt is already presented as a private
> old square-collared ternary-hex state, and the all-new reset phase admits
> one joint residence/upper/common-cap certificate while exporting at most
> the same bounded number of guarded collars to the next child.

Neither the Delcourt--Postle theorem nor the ordinary Pascal scalar/palette
recurrences prove this export statement.  The hex-free-cycle theorem shows
that collars cannot be recovered from an arbitrary near-perfect body after
the fact.  They must be part of the occurrence-labelled child state from the
start.
