# Newborn pooling versus the fixed-four absorber: the exact projection gate

Date: 2026-07-31  
Status: exact dimension-uniform nonimplication and solver-free finite audit.
The fixed-four `C6` gives a linear planted absorber supply, but the closed-core
newborn reserve inequalities do **not** imply that an arbitrary residual can
be routed to that bank by sparse-cycle kernel switches.

## 0. Verdict

There are two independent statements.

1. The newborn inequalities

   \[
      C\rho(H)\ge N\bigl(|H|-|\Gamma(H)|\bigr)                 \tag{0.1}
   \]

   certify robust endpoint orientation on the actual occurrence graph.  It
   is enough to test connected, Galois-closed outer-2-cores.
2. A planted fixed-four absorber bank can finish a residual only when the
   literal lower and upper outer leave is a `0/1` subset sum of its designated
   target boundaries.

Every proved sparse `2 ell`-cycle switch has zero displacement under the
literal outer-palette projection `Pi`.  Thus no composition of such switches can create the missing
target-subset condition.  Equation (0.1) contains no variable recording that
condition.  The desired implication is therefore false without an additional
atlas-alignment hypothesis.

This is not an objection to choosing the bulk and absorber bank jointly.  If
the off phases are literally installed, their target boundaries are already
part of the leave and palette routing is unnecessary.  The theorem rules out
using the closed-core inequalities plus count-neutral switches to obtain that
alignment after the fact.

## 1. The literal outer projection

Let `A` be the fixed-four atom set and let `mathcal D,mathcal V` be the two
declared active outer palettes.  Their orders need not agree in the
unpunctured host; after a fixed common-basis puncture both have order `P`.
For an atom

\[
       a=(D,V;(X,i),(Y,j)),
\]

let

\[
 \Pi(a)=\mathbf e_D^-+\mathbf e_V^+
        \in\mathbb Z^{\mathcal D\sqcup\mathcal V}.              \tag{1.1}
\]

This projection remembers the identities of the two outer colours and
forgets owner slots.  Relative to the declared active palettes, the outer
leave of a matching `M` is

\[
 r(M)=\mathbf1_{\mathcal D\sqcup\mathcal V}-\Pi(M).             \tag{1.2}
\]

The full two phases of a suspended fixed-four hex use the same three lower
and the same three upper colours.  If `k` is their signed difference, then

\[
                              \Pi(k)=0.                          \tag{1.3}
\]

The same is true of a sparse `2 ell`-cycle: its phases are

\[
 \{(D_i,V_i):i\in\mathbb Z_\ell\},\qquad
 \{(D_{i+1},V_i):i\in\mathbb Z_\ell\},                         \tag{1.4}
\]

so every literal `D_i` and `V_i` occurs once on both sides.  Consequently

### Theorem 1.1 (kernel projection invariant)

For every legal composition of sparse-cycle kernel switches,

\[
                         r(M')=r(M)                              \tag{1.5}
\]

on both literal outer shores.  In particular the complete four-sector-
resolved leave is invariant, not merely its cardinality.

The assertion is independent of whether intermediate physical states are
forests.  Slot, graphic, root and compiler guards can only shrink the set of
legal compositions.

## 2. Exact target-semigroup condition

Let a resource-disjoint planted bank have designated target atoms

\[
                       t_j=(D_j,V_j;X_j,Y_j),\qquad j\in J.      \tag{2.1}
\]

The corresponding gain-one identity is

\[
                   B_j^+-B_j^-=t_j                              \tag{2.2}
\]

in the free abelian group on all four resource classes.  Suppose one first
applies any sparse-cycle kernel switches and then activates a subbank `S`.
Outer saturation forces

\[
 \boxed{
       r(M)=\sum_{j\in S}
             \bigl(\mathbf e_{D_j}^-+\mathbf e_{V_j}^+\bigr).}  \tag{2.3}
\]

Because bank supports are resource-disjoint, the right side is a binary
subset sum.  Formula (2.3) is necessary, not sufficient: the off atoms must
also occur in the incumbent, the owner slots must be available, and the
physical and compiler rows must pass.

This obstruction survives arbitrary interleaving.  Put

\[
 b_j=\mathbf e_{D_j}^-+\mathbf e_{V_j}^+,
 \qquad
 \Lambda_{\mathcal B}=\langle b_j:j\in J\rangle_{\mathbb Z}. \tag{2.3a}
\]

Kernel switches change the outer vector by zero, while toggling packet `j`
changes it by `plus or minus b_j`.  Hence the class of the leave in

\[
 \mathbb Z^{\mathcal D\sqcup\mathcal V}/\Lambda_{\mathcal B} \tag{2.3b}
\]

is invariant under every mixed kernel/absorber sequence.  The target
vectors have disjoint supports and are linearly independent.  In general
the quotient rank is
`|mathcal D|+|mathcal V|-T`: completion imposes
`|mathcal D|+|mathcal V|-2T` outside-target zero rows and `T` target-pair
coupling rows.  On the normalized punctured side host this specializes to
`2P-T`.  Resource privacy reduces a final binary state to the
subset equation (2.3), so there is no sequential shuttle loophole.

Coarsening (2.3) by the two newborn tags gives eight marginal equations,
one redundant after total equality.  The literal equations are stronger.
Hence a sector-count match cannot silently replace target identity.

The coarse sector condition itself has an exact capacitated-flow form.  Let
`b_st` count planted targets with lower tag `s` and upper tag `t`, and let
`r_s^-`, `r_t^+` be the residual sector counts.  There must be integers
`0<=y_st<=b_st` with

\[
 \sum_t y_{st}=r_s^-,\qquad \sum_s y_{st}=r_t^+.       \tag{2.3c}
\]

By integral bipartite flow, this holds if and only if the two totals agree
and, for every `A,B subseteq {00,01,10,11}`,

\[
 \sum_{s\in A}r_s^- -\sum_{t\in B}r_t^+
   \le \sum_{\substack{s\in A\\t\notin B}}b_{st}.     \tag{2.3d}
\]

These are the exact target-profile Hall cuts.  At literal-label resolution
the planted target graph is already a matching, so its singleton cuts force

\[
 \mathbf1[D_j\text{ is a hole}]=
 \mathbf1[V_j\text{ is a hole}],                     \tag{2.3e}
\]

and every non-target outer label must have hole indicator zero.

Equivalently, form the exact routing graph whose left vertices are feasible
residual states and whose right vertices are target subbanks, joining two
vertices when a legal sparse-kernel sequence followed by those activations
closes the residual.  The graph is a disjoint union of fibres indexed by the
ordered pair of literal unmatched palette sets

\[
                           (L^-,L^+).                         \tag{2.4}
\]

At residual size one, a planted target can lie in the fibre of `(D,V)` only
if its own outer pair is exactly `(D,V)`.  Thus an empty target fibre is an
exact one-vertex Hall cut in the routing graph.  This is the smallest
possible obstruction; no statistical density estimate can cross it.

### Corollary 2.1 (sharp quantifier dichotomy)

* If every `B_j^-` is literally planted **and the exterior avoids the rest
  of its full packet support**, its target boundary is already in the
  residual and (2.3) is automatic for that bank.
* If only packet supports or target names are reserved, (2.3) is an extra
  alignment theorem.  Count-neutral kernel switches cannot prove it.

There is a second exact obstruction even after (2.3).  For a target
`(D,V;...)`, every canonical suspended-hex option meets the owner transversal

\[
                         \mathcal W_{D,V}=\{V-b:b\in D\},        \tag{2.5}
\]

of order `n`.  Protecting the residual slots of `mathcal W_(D,V)` blocks the
entire `2n(n-2)` formal catalogue.  Thus target alignment does not imply
slot availability.

## 3. Why the closed-core theorem does not supply (2.3)

The data in (0.1) are the occurrence graph, inherited endpoint blocks and
selected newborn terminals.  Neither `r(M)` nor the target vectors in (2.3)
occur.  Closure, leaf peeling and the outer-2-core reduction preserve this
fact: they compress the quantifier over `H`; they do not add a side-matching
leave equation.

This also shows what a positive pooling theorem would have to add, but one
must not identify the old reserve units with packet options.  The quantity
`rho(H)` counts endpoint-capacity witnesses; it has no canonical injection
into literal target fibres.  A possible coupled proof would first define an
explicit joint incidence system linking reserve tokens to reachable packet
options.  If its Rado rank is `r_B(H)`, the desired *sufficient* payment row
would be

\[
 C r_{\mathcal B}(H)
   \ge N\bigl(|H|-|\Gamma(H)|\bigr).                 \tag{3.0}
\]

No such canonical incidence system or cut theorem is proved here, so (3.0)
is an open strengthening, not a necessary consequence of the existing
ledger.  The proved necessary conditions remain separate: the final reserve
rows, the exact target-subset equation (2.3), and the host/graphic guards.
An outside-target literal hole or saturation of the owner transversal (2.5)
can destroy every packet option while leaving `G,I,Z_B,rho(H)` and all old
closed-core margins unchanged.  In particular, no comparison
`r_B(H)\asymp rho(H)` follows from the old data alone.

This logical separation is already sharp in the authenticated output at
parameter five, where (0.1) is proved for every inherited orientation.  Let
`T` be the order of any resource-disjoint fixed-four packet bank.  Each
packet support uses three distinct upper colours, so

\[
                               T\le\lfloor P/3\rfloor.           \tag{3.1}
\]

After one target is designated in every packet, at most `T` upper colours
are target colours.  Therefore at least

\[
                               P-T\ge P-\lfloor P/3\rfloor       \tag{3.2}
\]

upper colours are outside the target projection of the fixed bank.  Any
residual containing one of them violates (2.3), and (1.5) prevents every
sparse-cycle repair.  This counting argument uses the actual Boolean outer
shore, not an abstract colour statistic.

If an exact outer-perfect side matching is available before imposing the
bank, deleting its atom at such an upper colour produces a literal one-atom
leave with this obstruction.  This observation shows exactly what is absent
from the reserve theorem; it is not a claim that a separately fixed bulk and
packet bank are automatically compatible.

## 4. Actual four-sector finite ledger

For the authenticated output parameters `m=5,6,7`, the upper rank-`m+2`
shore has the following exact split by the two newest coordinates:

\[
\begin{array}{c|r|rrrr|r|r|r}
m&P&00&01&10&11&\lfloor P/54\rfloor+1&\lfloor P/3\rfloor&P-\lfloor P/3\rfloor\\ \hline
5&120 &8&28&28&56 &3 &40 &80\\
6&495 &45&120&120&210 &10&165&330\\
7&2002&220&495&495&792&38&667&1335
\end{array}                                                     \tag{4.1}
\]

The penultimate columns compare the guaranteed supply `T>P/54` with the
universal resource ceiling.  Linear supply is real, but it is not universal
target coverage.

There is also an exact finite dimensional separation.  The proved sparse
family requires

\[
                         \ell\ge5,\qquad m\ge2\ell-2.            \tag{4.2}
\]

Thus no member of that family exists at `m=5,6,7`; `m=8` is the first
`ell=5` row.  Literal replay at `m=8,9,10` verifies zero outer-mask and zero
four-sector-count displacement.  The kernel invariant persists when the
family first becomes available.

A canonical fixed-four packet using the two newest coordinates has phase
sector histograms

\[
 \mathcal D:00^2,10^1,\qquad
 \mathcal V:01^1,11^2,                                  \tag{4.3}
\]

and its displayed target lies in `(D,V)=(00,11)`.  OFF plus this literal
target equals ON.  Coordinate relabelling gives other embeddings, but no
embedding changes the projection theorem.

The full `P/54` packing used the untagged symmetric orbit, so by itself it
gave no fixed-sector quota.  Linear **unpunctured** supply nevertheless
survives after the newborn coordinates are fixed.  Fix their ordered roles
as `(a,s)` and take the orbit only under permutations of the other `2n-2`
coordinates.  Put

\[
 A=\binom{2n-2}{n},\qquad
 B=\binom{2n-2}{n-1},\qquad
 E=\binom{2n-2}{n+1}.                               \tag{4.4}
\]

One aligned packet uses category multiplicities

\[
\begin{array}{c|cccccccc}
&D_{00}&D_{10}&V_{01}&V_{11}&S_{00}&S_{01}&S_{10}&S_{11}\\\hline
\text{multiplicity}&2&1&1&2&1&2&2&1,
\end{array}                                         \tag{4.5}
\]

whose category sizes are respectively `A,B,E,A,E,A,A,B`.  Transitive
double counting gives resource degree `q|O|/S` in a category of size `S`
used `q` times per packet.  Summing the twelve resource degrees of a fixed
packet counts that packet twelve times, so its closed conflict neighbourhood
has the eleven repeated self-counts removed.  Hence the packet-intersection
graph obeys strictly

\[
 \Delta+1\le
 |\mathcal O|\left({16\over A}+{2\over B}+{2\over E}\right)-11
 <|\mathcal O|\left({16\over A}+{2\over B}+{2\over E}\right).
\]

Greedy packing therefore gives a pairwise-resource-private aligned bank of
order

\[
 T_{00\to11}>
 \left({16\over A}+{2\over B}+{2\over E}\right)^{-1}
 >{P\over80}.                                       \tag{4.6}
\]

For the last inequality, clear denominators using

\[
 {A\over P}={(n+1)(n+2)\over2n(2n-1)},\quad
 {B\over A}={n\over n-1},\quad
 {E\over A}={n-2\over n+1};                        \tag{4.7}
\]

equivalently,

\[
 80-P\left({16\over A}+{2\over B}+{2\over E}\right)
 =\frac{24(11n^2-17n-13)}{(n-2)(n+1)(n+2)}>0.       \tag{4.8}
\]

Thus the remaining polynomial is positive for every `n>=3`.  This
strengthens the actual-sector supply
statement: even a fixed `00->11` bank is linear.  It does not weaken the
projection obstruction, because it still designates only `T_(00->11)`
literal target pairs and its sector matrix has only the cell `b_(00,11)`.

## 5. Occurrence-state warning

Sparse-cycle switches are not automatically transparent to the newborn
ledger.  They preserve outer palettes, but replace the owner bank
`{H_i,P_i}` by `{H_i,Q_i}` and can change the physical components and path
endpoints.  The fixed-four hex keeps the same six owners but re-pairs them,
which can also change components and terminal choices.  Therefore the
closed-core inequalities of the pre-switch state cannot simply be carried
through a routing sequence.

More exactly, let `e_G(H)` denote the endpoint/terminal charge occurring in
the state-`G` definition of `rho_G(H)` (so changing this charge changes
`rho` with the opposite sign).  For the reserve margin

\[
 \mathfrak M_G(H)=C\rho_G(H)-N\bigl(|H|-|\Gamma_G(H)|\bigr),
\]

a switch producing occurrence state `G'` changes a fixed row by

\[
 \mathfrak M_{G'}(H)-\mathfrak M_G(H)
   =N\bigl(|\Gamma_{G'}(H)|-|\Gamma_G(H)|\bigr)
    -C\bigl(e_{G'}(H)-e_G(H)\bigr).                 \tag{5.1}
\]

Thus there is a strict dichotomy.  If the kernels are occurrence-
transparent, the old closed-core rows survive but do no palette routing by
Theorem 1.1.  If they are not transparent, the old rows are not stable and
the final state needs a fresh separator.  In neither case do the initial
closed-core inequalities imply routing.

A valid positive routing theorem must add all four conditions:

1. **target-semigroup alignment:** (2.3);
2. **fixed-palette fibre reachability:** a legal kernel-switch sequence which
   installs the required off phases;
3. **occurrence acceptance:** either switchwise occurrence transparency or
   a fresh two-shore closed-core/cumulative-sector audit of the final exported
   state; and
4. **physical guards:** slot, contracted-graphic/root and downstream common-
   cap/compiler compatibility.

The closed-core inequalities address only item 3.  The `P/54` theorem proves
raw packet supply, not items 1, 2 or 4.

## 6. Exact surviving target

### Lemma 6.1 (conditional planted-bank completion)

Let `S` be a target subbank satisfying (2.3), with pairwise resource-disjoint
full packet supports.  Suppose a legal fixed-palette kernel sequence produces
a host matching `M` containing every off phase `B_j^-`, `j in S`, and put

\[
                 E=M\setminus\bigcup_{j\in S} B_j^- .          \tag{6.1}
\]

Require `res(E)` to be disjoint from the union of the full packet supports
(equivalently, `M` restricted to each support is exactly its OFF phase).
Let `F_ext=phi(E)` and require `F_ext` to be a forest.  After contracting
`F_ext`, require `phi(\bigcup_{j\in S}B_j^+)` to be graphic-independent.
Finally require the **activated** state

\[
             E\cup\bigcup_{j\in S}B_j^+                         \tag{6.2}
\]

to pass the two-shore closed-core test and the declared root/common-cap
guards.  Then (6.2) is an outer-perfect guarded physical forest.  If safe
intermediate prefixes are required, append the existing graphic
circuit-deadline rows; they are not implied here.

#### Proof

Each activation deletes its two off atoms and adds its three on atoms.  The
literal identity (2.2) fills exactly target `t_j`.  Packet privacy separates
different activations, while the exterior-clean hypothesis prevents an
unrecorded exterior atom from occupying any packet resource.  Thus (6.2) is
a host matching.  Contracted independence makes its image a forest, (2.3)
fills every outer hole, and the final-state hypotheses are precisely the
remaining occurrence, root and common-cap guards. `square`

The weakest useful replacement for the proposed implication is an
**aligned fixed-palette fibre theorem**:

> Jointly choose the bulk and an `o(P)` subbank of the linear packet atlas so
> that the off phases are installed and their target boundary is exactly the
> bulk leave; then prove that any remaining slot/graphic mismatch can be
> corrected inside the same literal outer-palette fibre while preserving or
> regenerating the newborn closed-core inequalities.

Equivalently, if the bank is chosen after seeing the residual, one needs a
resource-private matching in the target-specific packet-choice hypergraph,
including the owner transversals (2.5).  Neither assertion follows from
newborn reserve isoperimetry.

No all-parameter cover-down, common basis, residence, deeper-shadow or word
compiler conclusion is made here.

## 7. Audit

The dependency-free audit is

```text
scratch/audit_threadD_newborn_c6_kernel_projection_gate_20260731.py
scratch/threadD_newborn_c6_kernel_projection_gate_20260731.audit.json
```

It authenticates the retained strict-DERF chain and the previous four-sector
and finite-status payloads.  It reconstructs the fixed-four packets at
`n=4,...,7`, the first sparse `ell=5` switches at `n=8,9,10`, and every row
of (4.1).  Its scope is solver-free projection arithmetic; it does not
materialize a common basis, planted bank, side matching or compiler.
