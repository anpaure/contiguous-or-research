# The SCD phase forest has a phase-independent `z`-endpoint cut against pure Catalan concatenation

Date: 2026-08-01  
Lane: Thread D / flexible four-row SCD detachment / owner-path completion  
Status: **exact all-dimensional endpoint identity, exact phase ledger,
exact connector-palette cocycle, and a sharp Hall obstruction of deficiency
`I_m-1` to joining the retained SCD phase forest by `C-1` endpoint
connectors.  This is a no-go for pure component concatenation, not for a
simultaneous release/rethread or an enlarged ear grammar.**

## 0. Verdict

Put

\[
\begin{aligned}
 D&={2m-3\choose m-2},&
 E&={2m-3\choose m-3},&
 J&={2m-3\choose m-4},\\
 c&=D-E=\operatorname {Cat}_{m-1},&
 I_m&=E-J,&
 C&=\operatorname {Cat}_m=2c+I_m.
\end{aligned}                                                   \tag{0.1}
\]

Assume the flexible four-row SCD detachment has been selected so that its
`W-C` rooted Johnson edges form an upper-exact, lower-injective linear
forest `F` on all

\[
                         W={2m-1\choose m}
\]

owners.  It therefore has `C` directed path components.  Let `H` be its
`C` unused lower colours.

The proposed completion keeps every edge of `F` and adds `C-1` Johnson
edges between component endpoints, using `C-1` members of `H`.  This is
impossible for every `m>=4`, independently of how the flexible phases are
chosen.  The exact violated Hall row is the coordinate `z`:

\[
 \boxed{
  \#\{K\in H:z\in K\}-1
  -\#\{\text{source endpoint owners containing }z\}
  =I_m-1. }                                                   \tag{0.2}
\]

Thus the finite dimensions `m=4,...,9` have deficiencies

\[
                    3,13,47,164,571,2001.                    \tag{0.3}
\]

The upper-repeat palette is not the cause.  Its coordinate degrees obey an
exact cocycle, and after adjoining the endpoint union it is an abstract
regular Catalan multidesign.  The obstruction is the **directed physical
occurrence** row: too many unused lower tails contain `z`, while only `c`
component-source owners contain `z`.

## 1. The universal endpoint--hole identity

Let `Omega` have order `2m-1`.  More generally, let `F` be any spanning
degree-at-most-two Johnson graph on the rank-`m` owners such that

1. its upper colours are every rank-`(m+1)` set exactly once; and
2. its lower colours are distinct, with missing family `H` of order `C`.

For a coordinate `q`, put

\[
 H_q=|\{K\in H:q\in K\}|,
 \qquad
 E_q=\sum_{T\ni q}(2-d_F(T)).                              \tag{1.1}
\]

Here `E_q` counts free endpoint slots containing `q`; an isolated owner
contributes two slots.

### Theorem 1.1 (endpoint--hole cocycle)

For every coordinate `q`,

\[
                  \boxed{E_q=H_q+2c.}                       \tag{1.2}
\]

#### Proof

For a Johnson edge with owners `T,T'`, lower intersection `K` and upper
union `R`, one has coordinatewise

\[
 {f1}_T+{f1}_{T'}={\bf1}_K+{\bf1}_R.                    \tag{1.3}
\]

Summing the left side over the forest edges gives

\[
                  2{2m-2\choose m-1}-E_q.                  \tag{1.4}
\]

The exact upper palette and the used lower palette give

\[
 {2m-2\choose m}
 +{2m-2\choose m-2}-H_q.                                   \tag{1.5}
\]

Equating (1.4) and (1.5), then using

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}=c,
 \qquad
 {2m-2\choose m}={2m-2\choose m-2},                        \tag{1.6}
\]

proves (1.2).  No acyclicity or phase assumption was used.  \(\square\)

## 2. Exact lower-hole ledger of the flexible SCD ears

Let `A_C` be the number of missing `aU` targets served by the aligned
long-chain C phase.  There are `E` such targets in total, so `E-A_C` use a
D phase.  Every one of the `J` all-`G` targets uses one auxiliary `zV`
tail.  Provider, auxiliary-tail and head injectivity imply the following
exact unused-lower counts:

\[
\begin{array}{c|c|c}
\text{signature in }\{a,z\}&\text{unused roots}&\text{number}\\ \hline
\varnothing&\text{short-chain }L&c\\
a&-&0\\
z&zS&c-J+A_C\\
az&azR&E-A_C.
\end{array}                                                   \tag{2.1}
\]

Indeed, all `D` roots `aS` are provider tails.  Exactly the `E` long roots
`L` are provider tails, leaving the `c` short roots `L`.  The C-phase ears
use `A_C` of the `E` roots `azR`.  Finally the D-phase ears and the `J`
all-`G` ears use `E-A_C+J` distinct members of the `D`-element `zS` bank.

The total in (2.1) is

\[
 c+(c-J+A_C)+(E-A_C)=2c+E-J=C.                    \tag{2.2}
\]

In particular the phase parameter cancels from the `z`-containing count:

\[
 \boxed{H_z=(c-J+A_C)+(E-A_C)=c+I_m=C-c.}          \tag{2.3}
\]

This is the first phase-independent selection constraint supplied by the
endpoint cocycle.

## 3. Source versus terminal endpoint slots

Every directed path component has a unique unused tail root `K in H`, and
its physical terminal owner is `M_0(K)`.  Write

\[
                         M_0(K)=K+e(K).             \tag{3.1}
\]

Let `T_q` and `S_q` count terminal and source endpoint owners containing
`q`, respectively, with both roles counted on an isolated component.  Put

\[
                 t_q=|\{K\in H:e(K)=q\}|.          \tag{3.2}
\]

Then

\[
 T_q=H_q+t_q,
 \qquad
 S_q=E_q-T_q=2c-t_q.                               \tag{3.3}
\]

For `q=z`, exactly the `c` short-chain holes `L` in the first row of
(2.1) have `M_0(L)=zL`.  Every other unused root already contains `z`, so
its added coordinate is not `z`.  Therefore

\[
                         t_z=c,
 \qquad
                         \boxed{S_z=c.}             \tag{3.4}
\]

Notice that (3.4) is independent of `A_C`.  Changing the C/D phase mixture
redistributes the `z` and `az` holes but cannot create another
`z`-containing component source.

## 4. The exact connector Hall cut

A directed connector from the terminal of component `i` to the source of
component `j` has rooted form

\[
                         K_i\longrightarrow P_j,    \tag{4.1}
\]

and physical owners `M_0(K_i),M_0(P_j)`.  Its lower colour is `K_i` exactly
when

\[
                         K_i\subset M_0(P_j).        \tag{4.2}
\]

Equivalently, writing `M_0(K_i)=K_i+x_i`, every non-diagonal legal
connector is uniquely

\[
 K_i\longrightarrow M_0^{-1}(K_i+y),
 \qquad y\notin M_0(K_i).                           \tag{4.2a}
\]

This is exactly the connector-variable catalogue in the joint model.  The
combined indegree/outdegree rows force its tail to be a phase-forest sink
and its head to be a phase-forest source; no frozen choice of the phase
forest is being assumed.

Consequently every connector using a tail `K_i` with `z in K_i` consumes a
source endpoint owner containing `z`.  Source tickets are capacity one.
A path on `C` components has `C-1` connectors and can leave only one member
of `H` unused.  Hence the `z`-row requires

\[
                         H_z-1\le S_z.              \tag{4.3}
\]

Substituting (2.3) and (3.4) gives

\[
 H_z-1-S_z=(C-c)-1-c=C-2c-1=I_m-1.                \tag{4.4}
\]

For `m=3`, `I_m=1` and this row is tight.  For every `m>=4`, `I_m>1`, so
(4.3) fails.  This proves (0.2) and the all-dimensional no-go.  It occurs
before connector cycles, component order, or upper-repeat choices.

### Corollary 4.1 (minimum escape budget)

Let `r_z` be the number of formerly required `z`-containing lower tails
which a proposed extension services outside the component-connector bank,
and let `s_z` be the number of additional pairwise-independent
`z`-containing source-owner tickets which it creates.  Every repair must
satisfy the exact cut

\[
                         \boxed{r_z+s_z\ge I_m-1.}   \tag{4.5}
\]

Thus any completion retaining this SCD forest grammar must provide at
least `I_m-1` **cut units** from the following resources:

1. extra `z`-containing source-owner tickets;
2. exemptions which service `z`-containing lower holes without a component
   connector; or
3. simultaneous release/rethread operations which change the terminal or
   unused-lower signature ledger.

Merely changing C/D phases, reordering/reversing the existing components,
or choosing a different repeated-upper multiset cannot repair the cut.

Equation (4.5), rather than an unqualified edge count, is the sharp
statement.  If a specified release actuator is proved to create at most
`b` such units, then at least

\[
                         \left\lceil{I_m-1\over b}\right\rceil \tag{4.6}
\]

actuators are necessary.  In particular a one-shore release has `b=1`,
while an actuator which can both exempt one `z`-tail and create one new
`z`-head has `b<=2`.  No bound on arbitrary compound rethreads is assumed.

## 5. Exact connector-repeat palette

The upper repeats have a separate, completely soluble coordinate ledger.
Suppose a final owner Hamilton path uses every lower colour except `K_0`,
has endpoint owners `T^-`,`T^+`, and uses every upper colour once plus a
repeat multiset `mathcal R` of order `C-1`.  The same edge-incidence sum as
in Section 1 gives

\[
 \boxed{
 d_{\mathcal R}(q)=2c+{\bf1}_{q\in K_0}
  -{\bf1}_{q\in T^-}-{\bf1}_{q\in T^+}. }          \tag{5.1}
\]

If the two endpoints are Johnson-adjacent with

\[
 K_0=T^-\cap T^+,
 \qquad
 R_0=T^-\cup T^+,                                  \tag{5.2}
\]

then

\[
 d_{\mathcal R}(q)=2c-{\bf1}_{q\in R_0},           \tag{5.3}
\]

and

\[
                 \mathcal Q=\mathcal R\mathbin{\dot\cup}\{R_0\}
\]

is a multiset of `C` rank-`(m+1)` blocks with constant coordinate degree
`2c`.

Such an abstract `mathcal Q` always exists.  Indeed,

\[
                         C(m+1)=(2m-1)2c.           \tag{5.4}
\]

Write the cyclic coordinate list `0,1,...,2m-2` exactly `2c` times and
partition the resulting word into `C` consecutive blocks of length `m+1`.
Because `m+1<2m-1`, every block has distinct entries.  Reading the blocks
as sets gives the required regular multiset.  A prescribed `R_0` can
equivalently be incorporated by the biregular degree-sequence construction
of
`MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md`.

Thus the palette cocycle has an unconditional abstract solution.  It does
not supply the occurrence-level inclusions (4.2), and therefore does not
touch the `z`-endpoint cut.

## 6. Finite evidence and exact scope

The saved flexible-detachment witnesses for `m=4,...,8` independently
replay as upper/lower-exact forests with `C` components.  Their fixed
component connector digraphs already fail at `m=4,5`.  More strongly, the
joint flexible-phase plus all-rooted-connector CP model is infeasible at
`m=4,5`.  These computations are regressions for (4.4), not the proof;
(4.4) closes `m=4,...,9` and every larger dimension at once.

The no-go is deliberately narrow.  It assumes that all `W-C` phase-forest
edges are retained and the only new physical edges are `C-1` connectors
between their exposed component endpoints.  A simultaneous alternating
release/rethread can change `H`, the endpoint roles, or both, and is not
excluded.  Nor does this note claim that the flexible phase CNF itself is
automatically acyclic: an explicit clause-satisfying `m=4` selection has a
directed five-cycle, as audited in
`MATH_THEOREM_THREAD_D_SCD_FLEXIBLE_DETACHMENT_POTENTIAL_SCOPE_20260801.md`.
