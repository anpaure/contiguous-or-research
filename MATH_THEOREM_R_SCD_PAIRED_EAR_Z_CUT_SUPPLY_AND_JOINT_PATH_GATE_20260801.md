# The short paired-ear bank supplies only one `z`-cut unit per short chain in the exact phase-plus-connector model

Date: 2026-08-01  
Lane: R / four-row SCD phase detachment / paired-ear repair  
Status: **exact all-dimensional cut calculation and exact final-state
0--1 formulation.  The anonymous capacity-two boundary projection does not
repair the joint rooted `z` cut: after exact upper-palette accounting, a
short chain supplies at most one new cut unit.  Consequently this enlarged
grammar is still impossible for every `m>=6`.  Dimensions `m=4,5` pass this
one scalar row but retain the typed head, target, and graphic gates.**

## 1. Notation and the old cut

Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I=I_m=\operatorname {Cat}_m-2\operatorname {Cat}_{m-1},\qquad
 C=\operatorname {Cat}_m=2c+I.
\]

For the standard four-row matching `M_0`, the flexible detachment grammar
has an exact upper palette, an injective lower palette of order `W-C`, and

\[
 H_z=c+I,qquad t_z=c,qquad S_z=2c-t_z=c.          \tag{1.1}
\]

Here `H_z` is the number of unused lower roots containing `z`, `t_z` is
the number of unused roots `K` for which `M_0(K)=K+z`, and `S_z` is the
number of directed source owners containing `z`.  The equality

\[
                         S_z=2c-t_z                 \tag{1.2}
\]

is the endpoint--hole cocycle in directed form.  Since a Hamilton path may
leave only one lower root unused, the rooted connector row has deficiency

\[
                         H_z-1-S_z=I-1.             \tag{1.3}
\]

## 2. Literal paired states in the joint grammar

For a short central chain `S<L=S+x`, write

\[
 A=aS,\qquad B=zS,\qquad C_S=L.
\]

Choose independently `U_0=L+b_0` and `U_1=L+b_1`, with
`b_0,b_1\notin L`, and put

\[
 P_0=M_0^{-1}(U_0),\qquad
 V_1=S+b_1=U_1-x,\qquad
 Q_1=M_0^{-1}(aV_1).
\]

The genuinely new first-stage choice in the long-ear model is the
alternative realization

\[
 \boxed{h_{S,U_0}:\quad C_S\longrightarrow P_0}    \tag{2.1}
\]

of the already required provider colour `zU_0`.  It replaces the native
`zU_0` edge of the long chain containing `U_0`.  The short `azL` provider
may remain `A->B`.

The second stage is already present in the ordinary flexible-detachment
catalogue: its short D option for target `aU_1` is

\[
 \boxed{d_{S,U_1}:\quad B\longrightarrow C_S,
        \qquad A\longrightarrow Q_1.}              \tag{2.2}
\]

Selecting both gives the final paired bundle

\[
 \boxed{B\longrightarrow C_S\longrightarrow P_0,
        \qquad A\longrightarrow Q_1.}              \tag{2.3}
\]

It has upper colours `azL,zU_0,aU_1` and lower tails `B,C_S,A`.
In an exact upper-palette construction it has the following typed meaning.

* The first stage (2.1) replaces the unique native `zU_0` provider;
  `zU_0` is retained, not an additional missing target.
* The second stage (2.2) replaces the short `azL` provider while retaining
  `azL`, and services the one missing target `aU_1`.

Thus (2.3) uses two provider rows and one target row and contributes three
edges.  This is edge-neutral relative to the standard provider-plus-target
ledger: `3-2=1`, the same one-edge excess supplied by one ordinary target
option.

The exact joint model need not force the two choices to occur together.
The first-stage `h` choice by itself is a legal provider rethread; the
second-stage `d` choice by itself is an ordinary short D target option.
The cut calculation below counts first-stage `h` choices.  Requiring a
literal serial paired ear may add `d<=h` (with the natural sum over
labels), but this only shrinks the feasible set and is not needed for the
no-go.

The serial capacity-two projection which treats the two stages as two
anonymous services forgets this distinction.  In the exact palette, the
first displayed `zU_0` is a provider-colour substitution, while only
`aU_1` occupies a missing-target row.

## 3. Exact cut contribution

Let `r` be the number of short chains on which a first-stage alternative
`h_{S,U_0}` is selected in a simultaneous exact phase selection.  All
tail/head rows are occurrence-labelled, and every such alternative uses
the tail `C_S`, so no two can use the same short chain.  Hence

\[
                              0\le r\le c.          \tag{3.1}
\]

### Theorem 3.1 (one cut unit, not two)

For every exact-upper, lower-injective degree-at-most-two selection in the
enlarged ordinary-option plus first-stage/paired-bundle grammar,

\[
 \boxed{H_z=c+I,\qquad t_z=c-r,\qquad S_z=c+r.}     \tag{3.2}
\]

Consequently the exact `z` connector cut is

\[
 \boxed{r\ge I-1.}                                 \tag{3.3}
\]

In particular, the paired bank supplies exactly one unit of the old
deficiency per active short chain.

Equivalently, after restoring the displaced ordinary target service, the
two typed operations have the exact net ledger

\[
\begin{array}{c|rrr|r}
\text{operation}&\Delta H_z&\Delta t_z&\Delta S_z&
 \text{cut gain}\\ \hline
h_{S,U_0}\text{ (provider rethread)}&0&-1&+1&1\\
d_{S,U_1}\text{ (ordinary target relocation)}&0&0&0&0.
\end{array}                                             \tag{3.3a}
\]

The second row is the unit which the anonymous capacity-two projection
incorrectly counts a second time.

#### Proof

Every ordinary missing-target bundle has one auxiliary tail containing
`z`.  The second-stage bundle (2.2) likewise has exactly one such
auxiliary tail, namely `B=zS`; indeed it is already one of the ordinary
options.  Provider tails do not contain `z`; replacing a native
`zU_0` provider by the `C_S->P_0` edge exchanges two non-`z` tails.
Since the number of target rows is fixed, the number of used `z`-tails is
unchanged.  Therefore `H_z=c+I` remains exact.

For this `M_0`, the roots satisfying `z\notin K` and
`M_0(K)=K+z` are exactly the `c` short-chain roots `C_S=L_S`:

\[
                         M_0(C_S)=zL_S.
\]

No ordinary detachment option uses a short `C_S` as a tail.  Choice (2.1)
uses precisely its own `C_S`, and short-chain tail capacity makes these
roots distinct.  Thus exactly `r` of the `c` such roots cease to be holes,
which proves `t_z=c-r`.  Equation (1.2) now gives `S_z=c+r`.

A Hamilton path uses `C-1` of the `C` missing lower roots as connector
tails.  At most `S_z` of the required tails containing `z` can enter
distinct source owners containing `z`, so `H_z-1<=S_z`.  Substitution of
(3.2) gives (3.3).  \(\square\)

### Corollary 3.2 (all-dimensional residual obstruction)

Because `r<=c`, this grammar can pass the `z` row only if

\[
                              I-1\le c.             \tag{3.4}
\]

It fails for every `m>=6`.  The exact residual deficiency after activating
all `c` short chains is

\[
 I-1-c={m-5\over m+1}c-1,                          \tag{3.5}
\]

with values

\[
\begin{array}{c|rrrrrr}
m&4&5&6&7&8&9\\ \hline
c&5&14&42&132&429&1430\\
I-1&3&13&47&164&571&2001\\
I-1-c&-2&-1&5&32&142&571.
\end{array}
\]

Thus the anonymous inequality `I<=2c` is not the relevant physical cut.
Its second unit is lost when the retained `zU` provider and the displaced
ordinary `aU` service are restored to the ledger.  Equivalently, both
serial stages share the one short root `C_S` which changes `t_z`.

Dimensions `m=4,5` are not proved positive: they merely survive this one
necessary row.

## 4. Exact additions to the joint Hamilton-path model

The smallest clean final-state extension uses one Boolean variable

\[
                         h_{S,U_0}                  \tag{4.1}
\]

for every first-stage alternative (2.1).  The second stages (2.2) are the
existing short D ordinary options.  It is unnecessary, and potentially
unsound, to serialize intermediate rotations.  Add the following rows to
the ordinary detachment-plus-connector model.

1. **Existing target rows.**  For every missing target `aU` or all-`G`
   target, exactly one ordinary option is selected.  No `h` variable is a
   new target: it realizes a provider colour.
2. **Provider row.**  For every native `zU_0` provider, retained plus all
   ordinary all-`G` options using that provider plus all `h_{S,U_0}` equals
   one.  The existing short-provider row independently controls a retained
   `A->B` edge or a short D option (2.2).
3. **Final rooted arc.**  A selected `h_{S,U_0}` inserts exactly the arc
   `C_S->P(U_0)`.  Insert its tail and head in the same combined in/outdegree
   rows as retained providers, ordinary ears, and connectors.
4. **Exact path degree.**  On every root `q`, impose

   \[
   d^+_{\rm base}(q)+d^+_{\rm conn}(q)+e_q=1,
   \qquad
   d^-_{\rm base}(q)+d^-_{\rm conn}(q)+s_q=1,
   \]

   with exactly one start and one end.
5. **Topology.**  Add a strict order on every active base and connector
   arc, or add valid lazy cuts for every directed cycle.  Degree rows alone
   permit disjoint directed cycles.
6. **Optional explicit cut.**  Add the solver-free valid inequality
   `sum h >= I-1`.  Together with the `C_S` tail rows it proves
   presolve infeasibility for every `m>=6`.

The combined provider equations make separate release-at-head implications
redundant if every retained and generated arc is included literally in the
degree rows.  They also enforce the closure condition when `Q_1` lands at
the head of another short provider.  A model which keeps only target and
anonymous capacity-two rows is not a physical lift.

The edge count remains exact.  Every `h` variable replaces one provider
edge by one provider edge, while every ordinary target option replaces one
provider edge by two.  Thus, if `T` is the fixed number of target rows,

\[
                    (P-T-r)+2T+r=P+T=W-C.          \tag{4.2}
\]

Adding exactly `C-1` connector arcs therefore gives `W-1` total arcs;
the degree and acyclicity rows make one spanning Hamilton path.

## 5. What remains after the cut

For `m=4,5`, or after adding some other actuator which supplies the
residual units in (3.5), the following gates remain independent:

* the occurrence-labelled `U_0` provider and `U_1` target rows;
* injectivity of the `Q(U_1-x_S)` heads, already represented by combined
  indegree;
* connector occurrence availability;
* graphic independence / Hamilton-path acyclicity; and
* any protected shadow, residence, or common-cap rows.

The connector upper-repeat cocycle remains automatic once a literal
Hamilton path is obtained.  Its abstract regular multidesign does not
repair (3.3), because (3.3) is an occurrence-level lower-tail/source cut.

The sharp surviving all-dimensional conclusion is therefore negative but
scoped: **the short paired-ear layer, by itself, cannot repair the
phase-forest `z` cut for `m>=6`; at least `I-1-c` further cut units from a
different owner rethread or lower-tail release mechanism are necessary.**
