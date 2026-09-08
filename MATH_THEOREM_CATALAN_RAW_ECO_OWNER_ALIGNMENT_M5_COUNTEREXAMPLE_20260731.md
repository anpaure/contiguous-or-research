# Raw coherent ECO hypertrees fail owner alignment first at `m=5`

Date: 2026-07-31  
Status: exact finite counterexample to the **unrepaired canonical-factor**
ECO owner-alignment proposal; exact positive `m<=4` calibration; no
obstruction to preliminary rethreading, a repaired factor, or full RSB

## 0. Verdict

The explicit coherent ECO family supplies component glues, but it does not
by itself supply the joint decoration which must own their forced ports.
The first failure is already the canonical `m=5` factor.

In paper parameter `n=m-1`, the canonical `n=4` factor has three components.
Its complete physical ECO catalogue has 45 distinct atoms.  Every minimal
topology-safe ECO hypertree therefore consists of two successive
component-reducing atoms.  Exhausting every legal ordered pair gives

\[
 648\text{ ordered sequences},\qquad 324\text{ endpoint Hamilton cycles}.
\]

All 648 accepted pairs have disjoint six-port sets, and their forced
three-colour faces are disjoint on both shores.  Thus the census covers both
descriptions: every ordered topology-safe minimal sequence and every
pairwise-port-disjoint two-ECO Hamilton outcome.  It already passes the
local owner-colour collision test.  Nevertheless every endpoint has exactly
the same deficient turn palettes:

\[
 \begin{aligned}
 \mathcal R^{+}&=\{219,365,438\},\\
 \mathcal R^{-}&=\{73,146,292\}.
 \end{aligned}                                                   \tag{0.1}
\]

Thus it realizes only `81` of the required `84` colours on each shore.
There is no upper-turn transversal at all, hence no gap graph, forest
matching, or unique owner alignment containing the selected ECO ports.

This refutes the raw implication

\[
 \text{coherent ECO hypertree}
 \Longrightarrow
 \text{leaf-forest owner-aligned decoration}.                    \tag{0.2}
\]

It does **not** refute the repaired route.  The known synchronized `m=5`
repair changes the factor first and then admits a leaf-peelable decoration
which owns the two standard coherent glues.  The order of construction is
therefore load-bearing:

\[
 \boxed{\text{prepare/rethread first; then choose the coherent ECO tree and
 its owners jointly}.}                                           \tag{0.3}
\]

## 1. The explicit ECO atom

Let `D=1u0v` be a Dyck word of semilength `n-1`, and put

\[
                 h=1u000v0.                                      \tag{1.1}
\]

Let `a,b,c` be the three consecutive positions in the displayed `000`,
let `e` be the first position, let `d` be the last position, and let `H`
be the support of `h`.  The six ports are

\[
 \begin{array}{lll}
 L_a=H+a,&L_b=H+b,&L_c=H+c,\\
 U_{ab}=H+a+b,&U_{bc}=H+b+c,&U_{ca}=H+c+a.
 \end{array}                                                     \tag{1.2}
\]

In the canonical factor the old and new alternating matchings are

\[
 \begin{aligned}
 E_0&=\{L_aU_{ca},L_bU_{ab},L_cU_{bc}\},\\
 E_1&=\{L_aU_{ab},L_bU_{bc},L_cU_{ca}\}.             \tag{1.3}
 \end{aligned}
\]

At every lower port the external factor edge inserts the common coordinate
`d`, and at every upper port it deletes the common coordinate `e`.
Consequently every atom is coherent.  Its forced turn-colour faces are

\[
 \begin{aligned}
 C^+(D)&=\{H+d+a+b,H+d+b+c,H+d+c+a\},\\
 C^-(D)&=\{H-e+a,H-e+b,H-e+c\}.                     \tag{1.4}
 \end{aligned}
\]

Rotating all positions produces the full physical orbit of the atom.
Coherence proves fixed-decoration transparency **if** all six ports belong
to one decoration.  It says nothing about existence of that decoration.

## 2. Why a missing turn colour is already decisive

Write a factor component in alternating order as

\[
 A_0,B_0,A_1,B_1,\ldots,qquad A_i\subset B_i\supset A_{i+1}.
\]

Its two turn words are

\[
 u_i=B_{i-1}\cup B_i,qquad \ell_i=A_i\cap A_{i+1}.                \tag{2.1}
\]

A joint decoration first chooses one occurrence of every upper colour
`u_i`; these choices form the transversal `I`.  It then chooses one lower
occurrence in every cyclic `I`-gap, giving one occurrence of every lower
colour.  Therefore

\[
 \bigl|\{u_i\}\bigr|=\binom{2m-1}{m+1},\qquad
 \bigl|\{\ell_i\}\bigr|=\binom{2m-1}{m-2}                       \tag{2.2}
\]

is necessary before forced ports, forest structure, or owner alignment can
even be discussed.  Equation (0.1) violates both equalities.  In
particular, allowing a nonforest gap graph would not help this raw endpoint.

## 3. Exact `m=5` census

The independent audit reconstructs the canonical factor directly from the
MMM Dyck rotation map `f`; it does not import the existing gluing-family
audit.  For `n=4` it then constructs every pair `(E_0,E_1)` from
(1.1)--(1.3), deduplicates physical rotations, and obtains:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{value}\\ \hline
 \text{factor components}&3\\
 \text{distinct ECO atoms}&45\\
 \text{single-atom component effect}&36(-1)+9(0)\\
\text{legal ordered two-atom Hamilton sequences}&648\\
\text{distinct Hamilton endpoints}&324.
 \end{array}                                                     \tag{3.1}
\]

For every sequential pair the audit checks that the intermediate and final
graphs are literal degree-two spanning factors, that the first atom reduces
the component count from three to two, and that the second reduces it to
one.  It also checks that the two physical six-port sets and their two
forced owner faces are disjoint.  It recomputes both turn palettes from the
two neighbours of every physical middle-level vertex.  All 648 rows give
exactly (0.1).

The missing triples are complementary and are the period-three rotation
orbits:

\[
     73=001001001_2,qquad 219=011011011_2,                         \tag{3.2}
\]

up to the bit-order convention of the audit.  This agrees with, and
strictly localizes, the previously observed period-three palette obstruction:
it persists across the **entire minimal raw ECO hypertree catalogue**, not
only one canonical choice of two glues.

## 4. Minimality of the counterexample

For `n=1,2` (project `m=2,3`) the canonical factor already has one
component and complete turn palettes, so no component glue is required.
For `n=3` (project `m=4`) the raw factor has two components and all 14 ECO
atoms are one-step Hamilton merges retaining both complete 21-colour turn
palettes.  The frozen literal atom

\[
 (L_a,L_b,L_c;U_{ab},U_{bc},U_{ca})
   =(19,21,25;23,29,27)                                           \tag{4.1}
\]

has a common leaf-peelable decoration whose unique gap matching owns the
forced lower triple `18,20,24`.  Hence `m=4` is genuinely positive on the
strong forest-owner face.

Project `m=5` is therefore the smallest raw canonical ECO obstruction.

This distinction matters for the general ECO collision law.  At a fixed
rotation the lower- and upper-owner collision graphs of the whole ECO
catalogue are identical path forests, so a collision-independent atom
selection makes both forced palettes injective.  Every minimal `m=5`
selection in this census is already collision-independent.  The failure is
therefore one level later: injective forced faces do not manufacture the
three globally absent turn colours, and hence do not manufacture the
transversal `I`.

## 5. Exact scope and surviving target

The census excludes only:

* the canonical MMM factor at project `m=5`;
* a minimal leaf-ordered/topology-safe ECO hypertree, hence two genuine
  component reductions and no preliminary neutral packet; and
* any attempt to obtain its owners from the endpoint factor without first
  changing that factor.

It does not exclude:

1. a preliminary transparent rethread or synchronized repair;
2. a longer sequence containing a component-neutral preparation packet;
3. a different middle-levels factor;
4. a non-ECO coherent merge catalogue;
5. the exact nonforest alternating-cycle owner exchange; or
6. any downstream residence, deeper-shadow, socket, voltage, or compiler
   construction.

The correct all-`m` owner-alignment target is consequently conditional on a
prepared endpoint:

> construct a prepared factor `F'_m`, a leaf-peelable decoration `D_m`, and
> a topology-safe coherent ECO hypertree selected **after** preparation,
> such that every forced lower-port edge belongs to the unique matching of
> the `D_m` gap forest.

The owner-masked chart theorem then makes forced Hall automatic.  The
separate private occurrence-router row is still required.

## 6. Audit

Run:

```bash
python3 scratch/audit_catalan_raw_eco_owner_alignment_counterexample_20260731.py
```

The script writes
`scratch/catalan_raw_eco_owner_alignment_counterexample_20260731.audit.json`
and reports

```text
PASS_RAW_ECO_M5_OWNER_ALIGNMENT_COUNTEREXAMPLE
```

Authoritative companion results:

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_K_GAP_HALL_PASCAL_DECORATION_RECURSION_20260731.md`;
* `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`.
