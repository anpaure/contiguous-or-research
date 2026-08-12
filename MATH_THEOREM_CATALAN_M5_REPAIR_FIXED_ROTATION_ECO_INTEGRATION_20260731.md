# The repaired `m=5` endpoint contains a private fixed-rotation ECO hypertree

Date: 2026-07-31  
Status: exact finite positive theorem at project `m=5`; no all-`m` supply or
occurrence-channel theorem

## 0. Verdict

The first raw ECO obstruction is completely removed by the synchronized
three-`C10` preparation, on the exact fixed-rotation ECO face.

Let `F_0` be the canonical middle-levels factor on ground set size `9`, and
let `C_1,C_2,C_3` be the three `C10` circuits of the repaired fixture.  Put

\[
                    F_* = F_0\mathbin\triangle C_1
                              \mathbin\triangle C_2
                              \mathbin\triangle C_3 .             \tag{0.1}
\]

This is the repaired **pre-glue** endpoint.  It has two components, of
orders `120` and `132`, and the decoration exported by the repair has a
forest gap graph with one unique perfect matching.

There are five fixed-rotation coherent ECO atoms, indexed by the five Dyck
words of semilength three.  At `F_*`:

1. every atom's three old factor edges are still present;
2. every atom is physically vertex-disjoint from all three `C10` supports;
3. every atom meets both components and its toggle produces one Hamilton
   cycle; and
4. exactly four atoms have all six ports selected by the repair decoration
   and are pointwise owner-aligned in its unique gap matching:

\[
               110100,qquad110010,qquad101100,qquad101010.       \tag{0.2}
\]

The atom `D=101100` is moreover isolated in the complete fixed-rotation
physical-support conflict graph.  It is exactly the second old standard
label, so its endpoint is the already audited standard-cube state `(0,1)`.
There is also a genuinely new witness: `D=110100` is not one of the three
standard labels and its Hamilton endpoint is outside the entire four-state
two-standard-glue cube.  Its singleton selection has no internal collision.
For either witness, the incidence graph with the two factor components is a
three-vertex tree.  Hence the repaired endpoint admits a literal
collision-free, component-faithful, one-atom ECO hypertree which may be
installed without touching the repair packet.

This is the exact finite compatibility statement missing from the raw
`m=5` counterexample:

\[
 \boxed{\text{three-`C10` preparation}
        \longrightarrow
        \text{unique owner forest + private coherent ECO hypertree}.} \tag{0.3}
\]

It proves no uniform repair packet and no occurrence-router local-channel
lemma.

## 1. The repaired state and its fixed decoration

The synchronized repair theorem starts from the standard Hamilton output,
applies the three displayed `C10` circuits, and then transports one forced
decoration backwards through the two standard glues.  Removing those two
glues gives (0.1).  Direct reconstruction gives

\[
              |Q_1|=120,\qquad |Q_2|=132.                         \tag{1.1}
\]

For the transported occurrence marks `(I,J)`, the factorwise gap graph
`Gamma_I` satisfies

\[
 \Gamma_I\text{ is a forest},\qquad
 \#\operatorname {PM}(\Gamma_I)=1,\qquad
 \text{the binary mark trace is a forest}.                        \tag{1.2}
\]

Write `M` for the unique matching.  Thus the forced-port theorem on this
state is the pointwise owner test: a lower-shore occurrence is admissible if
and only if its gap--colour edge lies in `M`.

## 2. Complete fixed-rotation audit

Use paper parameter `n=4`.  For

\[
                         D=1u0v\in\mathcal D_3,
\]

the fixed-rotation ECO atom has support word `1u000v0`, external labels
`(d,e)=(8,0)`, and the six standard incidence ports.  The exhaustive result
is:

\[
\begin{array}{c|c|c|c|c}
D&\text{all six marked}&\text{owner-aligned}&
  \text{repair-port intersection}&\text{endpoint components}\\ \hline
111000&\text{no (one port missing)}&\text{no}&0&252\\
110100&\text{yes}&\text{yes}&0&252\\
110010&\text{yes}&\text{yes}&0&252\\
101100&\text{yes}&\text{yes}&0&252\\
101010&\text{yes}&\text{yes}&0&252
\end{array}                                                       \tag{2.1}
\]

All five atoms also have zero edge intersection with the thirty edges of
the three `C10` circuits.  The stronger vertex-disjointness in (2.1) makes
the two operations commute as physical symmetric differences.

The two owner-aligned atoms at the bottom of the table recover exactly the
private triples already visible in the standard-glue fixture:

\[
 \begin{array}{c|c}
 D&\text{lower owner triple}\\ \hline
 101100&\{50,52,56\},\\
 101010&\{82,84,88\}.
 \end{array}                                                       \tag{2.2}
\]

For the selected witness `D=101100`, the ports are

\[
       \{51,53,55,57,59,61\};                                     \tag{2.3}
\]

the three upper-transversal positions are `51,53,57`, and the three selected
lower occurrences are `55,59,61`.  The pointwise owner map is

\[
                    55\mapsto52,\qquad59\mapsto50,
                    \qquad61\mapsto56.                            \tag{2.4}
\]

In the notation `Z=(H;a,b,c;d,e)`, (2.4) is exactly

\[
\begin{aligned}
 \operatorname {owner}_M(g(H+a+b))&=H-e+b,\\
 \operatorname {owner}_M(g(H+b+c))&=H-e+c,\\
 \operatorname {owner}_M(g(H+c+a))&=H-e+a.
\end{aligned}                                                     \tag{2.5}
\]

So this is pointwise forest rigidity, not merely equality of the two
three-colour sets.

## 3. Proof of the finite theorem

### 3.1 Physical survival and component faithfulness

The audit reconstructs `F_*` literally from the canonical factor and the
thirty displayed `C10` edges.  For every one of the five ECO atoms, its old
matching is a subset of `F_*`.  Its six ports avoid the union of the three
repair supports.  Toggling the atom therefore changes no repaired edge and
preserves degree two.

Every atom has ports in both components of (1.1).  Exhaustive traversal of
the toggled factor gives one component of order `252`.  Thus each atom is a
component-faithful hypermerge.  With two initial components, one such atom
is already an incidence hypertree.

### 3.2 Owner alignment

For each atom the three lower physical ports are tested against `I`, and
the three upper physical ports against the selected lower occurrence set
`J`.  Four atoms pass all six tests.  For each passing atom, the audit then
finds the unique `I`-gap containing each selected lower port and compares
its selected matching colour with the forced formula (2.5).  All twelve
pointwise equations hold.

Because `Gamma_I` is a forest, its perfect matching is unique.  The
leaf-forest owner theorem therefore implies that every passing atom's three
forced gap--colour edges extend, with no residual Hall search.

### 3.3 Preservation of the repaired state

For each of the four passing atoms, the same occurrence marks are replayed
on the toggled Hamilton cycle.  Both selected turn palettes are unchanged.
The resulting gap graph is again a forest with exactly one perfect matching,
and its binary trace is a forest.  Thus the ECO move does not merely coexist
with the repair support: it preserves the accepting repaired decoration.

### 3.4 Collision-free witnesses

The fixed-rotation ECO support-overlap theorem says that atom conflicts form
a path forest.  Direct intersection of all five literal supports shows that
`D=101100` has degree zero in this forest.  It is also disjoint from every
repair circuit.  Selecting it therefore has no atom--atom or atom--repair
physical conflict.  Literal comparison identifies its six-edge circuit with
standard label index `1`, so this Hamilton endpoint is the known repair-cube
state `(0,1)`.

For separation from the old standard construction, select `D=110100`
instead.  It is not a standard label; its endpoint edge set equals none of
the four standard-cube endpoints.  It has one conflict neighbour in the
unselected catalogue (`D=110010`), but a one-atom selected family has no
internal conflict, and its ports are still disjoint from all three `C10`s.
This gives a genuinely new fixed-rotation ECO Hamilton endpoint and proves
(0.3) independently of merely renaming the standard glue.

## 4. Exact router scope

The finite `m=5` central gluing result above is **unconditional**.  The audit
directly applies the physical atom, obtains one Hamilton cycle, and replays
the same literal decoration, unique gap matching, gap forest and trace
forest.  No router certificate is needed to establish this known finite
operation.

The router formalism is needed only when this certificate is promoted to an
all-`m` catalogue/order theorem without explicitly executing each move.  For
a one-atom tree there is no cross-atom route-packing problem.  Once one local
occurrence path from the atom source to its sink is supplied, router
resilience is automatic: a deletion set which kills the only bridge is
nonempty, so the surviving component count is at most

\[
                              2\le |Y|+1.             \tag{4.1}
\]

The present audit does **not** construct that local occurrence path in a
uniform prepared router.  Physical support isolation proves that any channel
confined to this atom bank would be private; it does not prove such a
channel exists for the recursive catalogue.  This is the sole unproved
central row when the finite witness is abstracted into the all-`m`
router-private theorem, not a caveat on the finite toggle itself.

## 5. The all-`m` invariant suggested by the fixture

The finite theorem points to a more precise recursive state than either
"repairable palette" or "connected ECO supply" alone.

Given a repair macro `P`, its endpoint factor `F_P`, and a leaf-peelable
decoration `(I,M)`, define the **repair-exported ECO bank**

\[
 \mathcal E(P,I,M)=\{Z:\
 \begin{array}{l}
 E_0(Z)\subseteq F_P,\quad V(Z)\cap V(P)=\varnothing,\\
 Z\text{ is component-faithful and coherent},\\
 P_A(Z)\subseteq I,\quad F_B(Z)\subseteq M
 \end{array}\}.                                                   \tag{5.1}
\]

The exact proposed invariant is:

> **Repair-exported private-ECO invariant.**  At every recursive boundary,
> the prepared state exports `(F_P,I,M)` such that the component hypergraph
> of `E(P,I,M)` contains an incidence hypertree; selected atoms have
> conflict-independent physical supports (or one certified commuting cube),
> zero-flux/owner-aligned matching blocks, and node-private or laminar
> occurrence channels.

Project `m=5` satisfies the incidence, physical, and owner rows with either
`D=101100` or the nonstandard `D=110100`.  Both literally preserve the
same unique leaf-forest matching and trace-forest guard.  The uniform
occurrence-channel row remains conditional as explained in Section 4.  No
claim is made here that (5.1) is nonempty, much less hypertree-spanning, for
arbitrary `m`.

This invariant captures the lesson of the raw counterexample and its repair:
the ECO tree must be selected **after** the repair and filtered by the same
unique owner matching.  Static ECO connectivity before preparation is the
wrong quantifier order.

## 6. Audit

Run

```text
python3 scratch/audit_catalan_m5_repair_fixed_rotation_eco_integration_20260731.py
```

It writes

```text
scratch/catalan_m5_repair_fixed_rotation_eco_integration_20260731.audit.json
```

and reports

```text
PASS_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION
```

The script is finite and solver-free.  It reconstructs the repair, the
unique decoration, all five fixed-rotation atoms, every pointwise owner
equation, every endpoint factor, and the complete physical conflict row.
