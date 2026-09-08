# Lane I: exact boundary indicators at the $k=15$, Hall-29 gate

Date: 2026-07-28

## 0. Result

Let $A_{29}$ be the canonical Dulmage--Mendelsohn target shore of the
current Hall-29 chronology.  It has

\[
 |A_{29}|=1524,
 \qquad |N(A_{29})|=1495.                              \tag{0.1}
\]

The blanket boundary allowance $36$ cannot separate this shore, since

\[
 1495+36=1531>1524.                                    \tag{0.2}
\]

There is, however, a compact exact replacement.

1. For compiler delay $d=3$, an interior cell of row depth
   $h\in\{0,1,2\}$ is determined by a centered window of exactly
   $5+h$ directed middle edges.  Thus the depth-adaptive exact states have
   sizes $5,6,7$, and a uniform exact state has seven edges.

2. All eighteen cells at one linear endpoint are determined by the first
   nine middle vertices, equivalently the first eight directed edges.  The
   former twelve-vertex boundary enumeration is correct but has three
   unnecessary vertices.

3. On the actual three-parent directed catalogue, the sizes $5,6,7$ are
   not merely worst-case bounds for $A_{29}$.  Centered states one edge
   shorter give false positive counts at every depth.  In particular a
   centered six-edge state leaves exactly $28$ false depth-two hits, while
   seven edges give the exact value $1495$.

4. The selected Hall-29 endpoint collars hit no $A_{29}$ cell:

\[
 B^-_{A_{29}}=B^+_{A_{29}}=0.                           \tag{0.3}
\]

Consequently the exact cut evaluates to

\[
 I_{A_{29}}+B^-_{A_{29}}+B^+_{A_{29}}
 =1495<1524,                                            \tag{0.4}
\]

and rejects the incumbent by its true deficiency $29$.

The boundary term cannot be a function of the endpoint vertex alone.  It is
a function of the endpoint and its selected eight-edge collar.  The exact
formulation below derives that collar from the directed Hamilton circuit by
order indicators; it does not enumerate all endpoint paths.

## 1. Exact compiler notation

Let

\[
 Y_0,Y_1,\ldots,Y_{W-1}\in\binom{[15]}8               \tag{1.1}
\]

be a directed Johnson path, and put $d=3$.  For every letter position $p$
define its allowed-coordinate mask

\[
 Q_p=\bigcap_{j=\max(0,p-d)}^{\min(p,W-1)}Y_j.          \tag{1.2}
\]

For an occurrence $a\in Y_t$, its carrier is

\[
 C(t,a)=\{p\in[t,t+d]:a\in Q_p\}.                      \tag{1.3}
\]

A compiler cell of row depth $h<d$, starting at $b$, uses the letter
positions

\[
 S_{b,h}=[b,b+h].                                       \tag{1.4}
\]

Its envelope and mandatory mask are

\[
 E_{b,h}=\bigcup_{p=b}^{b+h}Q_p,                        \tag{1.5}
\]

\[
 M_{b,h}=\{a:\text{some nonempty }C(t,a)
                    \text{ is contained in }S_{b,h}\}. \tag{1.6}
\]

A lower target $T$ fits this cell precisely when

\[
 M_{b,h}\subseteq T\subseteq E_{b,h},
 \qquad T\cap Q_p\ne\varnothing\quad(b\le p\le b+h).  \tag{1.7}
\]

For a fixed target shore $A$, let

\[
 c_A(b,h)=
 \mathbf 1\{\text{some }T\in A\text{ satisfies (1.7)}\}. \tag{1.8}
\]

This is exactly the adjacency predicate used by the Hall auditor.

## 2. The short-state identity

For a coordinate $a$, write $q_p(a)=\mathbf 1_{a\in Q_p}$ and

\[
 J_p=[\max(0,p-d),\min(p,W-1)].
\]

### Lemma 2.1 (local convexity)

If $q_p(a)=q_r(a)=1$ and $0\le r-p\le d$, then

\[
 q_j(a)=1\qquad(p\le j\le r).                           \tag{2.1}
\]

#### Proof

The two conditions say that $a$ belongs to every middle set indexed by
$J_p$ and by $J_r$.  Since $r-p\le d$, these truncated intervals overlap,
and for $p\le j\le r$ one has $J_j\subseteq J_p\cup J_r$.  Hence $a$
belongs to every middle set indexed by $J_j$, so $a\in Q_j$.
\(\square\)

### Theorem 2.2 (mandatory-mask identity)

For every legal $0\le b\le W+2-h$ and $0\le h<d=3$,

\[
 \boxed{
 M_{b,h}=
 \begin{cases}
 E_{b,h}\setminus Q_{b+h+1},&b+h<d,\\[1mm]
 E_{b,h}\setminus Q_{b-1},&b\ge W,\\[1mm]
 E_{b,h}\setminus(Q_{b-1}\cap Q_{b+h+1}),&\text{otherwise}.
 \end{cases}}
                                                               \tag{2.2}
\]

The first and second lines are respectively the left- and right-special
cases; the last line includes the cross-boundary starts $d\le b<W$.

#### Proof

Fix a coordinate $a\in E_{b,h}$, and choose $p\in S_{b,h}$ with
$q_p(a)=1$.

Suppose first that $b<W$ and $q_{b+h+1}(a)=0$.  Choose
$t=\min(p,W-1)$.  Then $t\in J_p$, so $a\in Y_t$, and
$p\in[t,t+d]$, so $p\in C(t,a)$.  Also $t\ge b$.  If a point
$r>b+h$ belonged to $C(t,a)$, then $q_p(a)=q_r(a)=1$ and
$r-p\le d$; Lemma 2.1 would force $q_{b+h+1}(a)=1$.  Hence
$C(t,a)\subseteq S_{b,h}$, and $a$ is mandatory.

Symmetrically, suppose $b+h\ge d$ and $q_{b-1}(a)=0$.  The chosen $p$
must satisfy $p\ge d$: if $p<d$, then
$J_p=[0,p]\supseteq[0,b-1]=J_{b-1}$, so
$Q_p\subseteq Q_{b-1}$, contradicting $q_p(a)=1$ and
$q_{b-1}(a)=0$.  We may therefore choose $t=p-d\ge0$.  Then
$p\in C(t,a)$, and the same convexity argument excludes every carrier point
left of $b$; no carrier point lies right of $p\le b+h$.  Thus again
$C(t,a)\subseteq S_{b,h}$.  This includes the nonvacuous crossing case
$b<d\le b+h$.

Now assume $b+h\ge d$, $b<W$, and both adjacent masks contain $a$.
If some nonempty $C(t,a)$ were contained in $S_{b,h}$, then the true left
adjacent mask could be avoided only by $t\ge b$, while the true right
adjacent mask could be avoided only by $t+d\le b+h$.  These inequalities
give $d\le h$, contrary to $h<d$.  This proves the ordinary third line.

Finally suppose $b+h<d$.  If $q_{b+h+1}(a)=1$, any nonempty carrier
$C(t,a)\subseteq S_{b,h}$ would have $0\le t\le b+h$; hence
$b+h+1\in[t,t+d]$ and the true right adjacent mask would also belong to
$C(t,a)$, a contradiction.  This proves the first line.  Reversing the
middle path proves the second line. \(\square\)

### Corollary 2.3 (smallest raw windows)

For the canonical interior realization, the cell begins at local position
$b=6$.  Equations (1.5), (1.7), and (2.2) use exactly

\[
 Q_5,Q_6,\ldots,Q_{7+h}.                                \tag{2.4}
\]

These masks are determined by

\[
 Y_2,Y_3,\ldots,Y_{7+h},                                \tag{2.5}
\]

a string of $6+h$ middle vertices or $5+h$ directed edges.  Thus the
depths $0,1,2$ require $5,6,7$ centered edges respectively.

For the eighteen left-boundary cells, $0\le b\le5$ and $0\le h\le2$.
Formula (2.2) uses no allowed mask beyond $Q_8$.  Therefore the single
prefix

\[
 Y_0,Y_1,\ldots,Y_8                                      \tag{2.6}
\]

determines the whole left boundary palette.  This is nine vertices, or eight
directed edges.  The last nine vertices in reverse order determine the right
palette.

## 3. The $A_{29}$ minimality audit

The current directed catalogue is the union of the three paths

```text
scratch/k15_doubletrans_05_213_hall29.json
scratch/k15_outer2_p1_h30_bridge.json
scratch/k15_trans1113_balanced_hall31.json
```

It has $6435$ vertices and $15890$ distinct directed edges.  Positive
centered states were enumerated against the fixed shore $A_{29}$, and then
the states active on the Hall-29 path were counted.

| centered edges | depth 0 | depth 1 | depth 2 | total |
|---:|---:|---:|---:|---:|
| 4 | 90 | 421 | 1233 | 1744 |
| 5 | **81** | 404 | 1126 | 1611 |
| 6 | **81** | **395** | 1047 | 1523 |
| 7 | **81** | **395** | **1019** | **1495** |
| exact Hall audit | 81 | 395 | 1019 | 1495 |

Hence the first exact state size is $5$ at depth zero, $6$ at depth one,
and $7$ at depth two.  In particular:

\[
 1047-1019=28                                             \tag{3.1}
\]

false depth-two hits survive a centered six-edge projection.  This proves an
$A_{29}$-specific lower bound: a uniform state of at most six edges cannot
be exact on the present catalogue.  Corollary 2.3 supplies the matching
seven-edge upper bound.

The numbers of positive catalogue states needed by a depth-adaptive exact
encoding are

\[
 29027\qquad(h=0,\ 5\text{ edges}),
\]

\[
 137426\qquad(h=1,\ 6\text{ edges}),
\]

\[
 595220\qquad(h=2,\ 7\text{ edges}),                   \tag{3.2}
\]

for a total of

\[
 761673.                                                  \tag{3.3}
\]

A uniform seven-edge table has $1108667$ states.  Thus the depth-adaptive
version saves $346994$ indicators without weakening the cut.

The incumbent boundary computation from (2.2) gives

\[
 (B^-_{A_{29},0},B^-_{A_{29},1},B^-_{A_{29},2})=(0,0,0),
\]

\[
 (B^+_{A_{29},0},B^+_{A_{29},1},B^+_{A_{29},2})=(0,0,0). \tag{3.4}
\]

Thus all $1495$ neighbours in (0.1) are interior.

## 4. Endpoint identity is not enough

The exact eight-edge collar census in the same three-parent union contains

\[
 8967022                                                   \tag{4.1}
\]

simple directed collars on each side.  Their $A_{29}$-boundary weights
range through every integer from $0$ to $18$.

Of the $6435$ possible endpoint vertices,

* $6383$ left endpoints admit two or more different boundary weights;
* $6388$ right endpoints admit two or more different boundary weights;
* $3718$ left endpoints and $3720$ right endpoints admit a zero-weight
  collar.

The actual Hall-29 start and end are

\[
 Y_0=9901,
 \qquad Y_{W-1}=7779.                                    \tag{4.2}
\]

Within the union catalogue, collars from the same start $9901$ have weights

\[
 \{0,1,3,4,6\},                                          \tag{4.3}
\]

and collars into the same end $7779$ have weights

\[
 \{0,1,2,3,6\}.                                          \tag{4.4}
\]

The selected incumbent collars choose weight zero in both sets.  Therefore a
coefficient attached only to the endpoint variable is not exact.  One must
couple the endpoint to its directed collar.

## 5. Compact exact boundary formulation

Let $G=(V,E)$ be the directed parent-union catalogue.  Let $x_{uv}$ be the
selected normal-arc variables, and let

\[
 s_v=x_{\partial v},
 \qquad t_v=x_{v\partial}                                \tag{5.1}
\]

be the dummy-to-start and end-to-dummy variables in the existing directed
circuit.  `AddCircuit` makes these arcs one Hamilton cycle through the dummy,
hence one Hamilton path on $V$.

### 5.1 Order channel

Introduce an integer order $\pi_v\in\{0,\ldots,W-1\}$ for every $v\in V$
and an inverse variable $\eta_i\in V$ for every position $i$.  Impose the
single global inverse constraint

\[
 \operatorname{AddInverse}((\pi_v)_{v\in V},(\eta_i)_{0\le i<W}),
 \qquad \eta_{\pi_v}=v.                                \tag{5.2}
\]

Couple this inverse channel to the already selected circuit by

\[
 s_v=1\Longrightarrow \pi_v=0,
 \qquad
 t_v=1\Longrightarrow \pi_v=W-1,                        \tag{5.3}
\]

\[
 x_{uv}=1\Longrightarrow \pi_v=\pi_u+1
 \qquad(uv\in E).                                       \tag{5.4}
\]

Only the first and last nine inverse positions are decomposed into coordinate
bits.  If $\mu(v)$ is the 15-bit mask of $v$, set

\[
 m^-_i=\mu(\eta_i),
 \qquad m^+_i=\mu(\eta_{W-1-i})
 \quad(0\le i\le8),                                   \tag{5.5}
\]

using `Element` constraints.  Equivalently one may write
$\ell_{i,v}=\mathbf1_{\eta_i=v}$ and
$r_{i,v}=\mathbf1_{\eta_{W-1-i}=v}$, but the implementation does not create
the resulting $18W$ Boolean table.  No collar enumeration and no second
order channel is present.

For a coordinate $a\in[15]$, define the selected middle-membership bits

\[
 y^-_{i,a}=\mathbf1_{a\in m^-_i},
 \qquad
 y^+_{i,a}=\mathbf1_{a\in m^+_i}.                       \tag{5.6}
\]

The left allowed masks are encoded bitwise by

\[
 q^-_{p,a}=\bigwedge_{j=\max(0,p-3)}^p y^-_{j,a}
 \qquad(0\le p\le8),                                   \tag{5.7}
\]

and $q^+_{p,a}$ is defined analogously on the reversed suffix.

### 5.2 Boundary-cell indicators

For every side, $0\le b\le5$, and $0\le h\le2$, compute $E_{b,h}$ by
(1.5) and $M_{b,h}$ by (2.2).  For each $T\in A_{29}$, introduce a fit
indicator $f^{\pm}_{b,h,T}$ for the conjunction, where
$e^{\pm}_{b,h,a}=\mathbf1_{a\in E^{\pm}_{b,h}}$ and
$m^{\pm}_{b,h,a}=\mathbf1_{a\in M^{\pm}_{b,h}}$:

\[
 \bigwedge_{a\notin T}\neg m^{\pm}_{b,h,a}
 \quad\wedge\quad
 \bigwedge_{a\in T}e^{\pm}_{b,h,a}
 \quad\wedge\quad
 \bigwedge_{p=b}^{b+h}\bigvee_{a\in T}q^{\pm}_{p,a}.    \tag{5.8}
\]

Finally put

\[
 c^{\pm}_{b,h}=\bigvee_{T\in A_{29}}f^{\pm}_{b,h,T},
 \qquad
 B^{\pm}_{A_{29}}=\sum_{b=0}^5\sum_{h=0}^2c^{\pm}_{b,h}. \tag{5.9}
\]

Equations (5.2)--(5.9) give the exact boundary score of the selected circuit.
The direct disjunction would use $18|A_{29}|=27432$ fit indicators per side,
still far fewer than one indicator for each of the $8967022$ possible
collars.  The implemented existential compression in §5.3 is smaller again.

For the current $W=6435$, $|E|=15890$ catalogue, the boundary channel has

* $6435$ order integers and $6435$ inverse-position integers;
* eighteen endpoint `Element` masks and 270 selected coordinate bits;
* $15890$ reified successor equalities;
* per shore, 36 claim bits, 36 target indices, 540 selected-target bits, and
  at most 1080 target/allowed meet bits;
* fewer than $2000$ shared allowed-mask, envelope, mandatory, and blocker
  indicators.

This is a compact exact endpoint formulation.  The already-required directed
circuit variables are not duplicated.

### 5.3 Existential target compression used by the consumer

For feasibility, the full family of fit variables in (5.8) can be replaced
by one claim bit $c^{\pm}_{b,h}$ and one selected target
$\tau^{\pm}_{b,h}\in A_{29}$ for each of the 36 cells.  Impose only

\[
 c^{\pm}_{b,h}=1\Longrightarrow
 \tau^{\pm}_{b,h}\text{ satisfies all three conditions in (5.8)}. \tag{5.10}
\]

No reverse implication is needed.  Since every cell contributes at most one
unit to the Hall row, the system

\[
 \sum_\gamma z_\gamma+\sum_{\pm,b,h}c^{\pm}_{b,h}\ge |A_{29}| \tag{5.11}
\]

is feasible for a fixed circuit if and only if its exact neighborhood has
size at least $|A_{29}|$: a feasible assignment certifies a distinct compiler
cell for every asserted claim, while a circuit with enough fitting cells can
choose an arbitrary fitting target independently in each such cell.  Thus
(5.10) is an equisatisfiable existential compression, not an upper allowance.
It uses exactly 36 claim bits and 36 target-index variables per shore.  In
particular, it neither grants a blanket boundary credit nor assumes that one
target works in different cells.

## 6. Exact interior coupling and the Hall cut

For depth $h$, enumerate only the positive centered $(5+h)$-edge states
from Corollary 2.3.  Write $g_L(v)=\mathbf 1_{\pi_v\ge2}$ and
$g_R(v)=\mathbf 1_{\pi_v\le W-3}$.  If $v_0,v_*$ are the first and last
vertices of a centered state, define its indicator by the **single guarded
conjunction**

\[
 z_\gamma=
 \left(\bigwedge_{e\in\gamma}x_e\right)
 \wedge g_L(v_0)\wedge g_R(v_*).                       \tag{6.1}
\]

Equivalently, the CNF/PB encoding includes the upper inequalities for every
arc and both guards and the lower inequality

\[
 z_\gamma\ge
 \sum_{e\in\gamma}x_e+g_L(v_0)+g_R(v_*)-(|\gamma|+1). \tag{6.2}
\]

The guards are part of the lower bound; merely adding guard upper bounds to
an unguarded conjunction lower bound would be inconsistent on a selected
boundary occurrence.  Because the centered state discards two irrelevant
vertices from each side of the historical full context, (6.1) removes
exactly the two endpoint layers:

\[
 z_\gamma\le1-\ell_{0,v_0}-\ell_{1,v_0},
 \qquad
 z_\gamma\le1-r_{0,v_*}-r_{1,v_*}.                      \tag{6.3}
\]

Thus $z_\gamma$ is the exact indicator of one interior compiler cell.

Indeed, a centered $(5+h)$-edge chain beginning at middle position $i$
represents compiler start $b=i+4$.  The two guards say

\[
 i\ge2,\qquad i+5+h\le W-3,
\]

or equivalently $6\le b\le W-4-h$.  Row $h$ has all starts
$0\le b\le W+2-h$; its complement is exactly the six left starts
$0,\ldots,5$ and the six right starts
$W-3-h,\ldots,W+2-h$.  Hence the partition has twelve boundary cells per
depth and 36 in total, with neither a gap nor an overlap.

Put

\[
 I_{A_{29}}=\sum_{\gamma}z_\gamma.                       \tag{6.4}
\]

The exact Benders row is then

\[
 \boxed{
 I_{A_{29}}+B^-_{A_{29}}+B^+_{A_{29}}\ge1524.
 }                                                        \tag{6.5}
\]

### Theorem 6.1 (exactness)

For every Hamilton path selected by the directed circuit, the left side of
(6.5) is exactly the number of compiler cells in
$N(A_{29})$.  Hence (6.5)
is equivalent to the Hall inequality for the fixed shore $A_{29}$.

#### Proof

The full compiler cell set is the disjoint union of the bounded interior
cells and the eighteen cells at each endpoint.  Corollary 2.3 and the guards
(6.1) give one exact indicator for every interior cell and none for a boundary
cell.  More explicitly, every active guarded centered chain has the two
predecessor and two successor vertices needed for a simple full
$(10+h)$-vertex extension; the exhaustive catalogue DFS enumerates that
extension, while Corollary 2.3 says that hit versus non-hit depends only on
the centered chain.  Thus the serialized positive centered palette is an
if-and-only-if catalogue for an arbitrary mixed selected path, not merely for
the parent chronologies used in regression.  Equations (5.2)--(5.9)
reconstruct the selected endpoint collars and,
by Theorem 2.2 and (1.7), give one exact indicator for each boundary cell.
Therefore (6.4) and (5.9) count the two parts of $N(A_{29})$ without overlap.
\(\square\)

On the incumbent, (6.5) reads $1495+0+0\ge1524$, which is false.  The
blanket $+36$ has been eliminated, and the original Hall-29 defect is
recovered exactly.

## 7. Consequence for Lane I

The boundary issue is now an encoding problem, not an unresolved projection
estimate:

* four-edge and six-edge projections are provably too coarse for the actual
  $A_{29}$ shore;
* the exact interior state is depth-adaptive (5/6/7);
* the exact endpoint state is an eight-edge collar generated by the circuit's
  first/last nine order positions;
* endpoint identity alone is invalid, but no explicit collar catalogue is
  required;
* the incumbent violates the resulting exact row by $29$.

The next finite search should therefore replace every `B 36` record by the
order-channel construction (5.2)--(5.11), and replace the present projected
interior motifs by the centered (5/6/7) tables with the two-layer guards
(6.1).  Any surviving circuit then genuinely crosses $A_{29}$; it cannot be
an artefact of boundary credit or a short-state collision.

## 8. Reproducibility ledger

The certified integration uses the self-contained
`K15_DIRECTED_MULTI_DM_CENTERED_EXACT_V2` format generated by
`--adaptive-exact`, not the legacy projected format.  The consumer parses the
complete edge table, targets, depth-adaptive positive palettes, declared
counts, and locality metadata; it rejects a catalogue edge-set mismatch.  It
then builds the shared `AddInverse` channel and the literal endpoint formulas
above.  The older `--boundary-summary` census remains an independent audit,
not the consumer interface.

The H100 execution environment was `arboghast:/dev/shm/k15_rotation`, with
OR-Tools `9.15.6755`.  Executed/core SHA-256 values are:

```text
7f53e515cf68a7f6dbd8b043c0831517c942e749e19ed5056d12844d9284c1ca  fast_k15_directed_multi_dm_projection_v2.cpp
5fa26f41e640b2c05b242040edf894e86cb6e066638d203bcf419f9de6e0e63d  fast_k15_directed_multi_dm_projection_v2 (H100 binary)
28c4fb46b271cbc5cc1d4bdf18a96ee65cd8bc81fa86e94f93072a516d1178a1  search_k15_directed_parent_union_cpsat_v2.py
3fd3281844ff86fd908a46c59ed5a0c583a1869702c3f73fbacc2f49be4f82ad  regress_k15_centered_exact_v2.py
5e8bb4b437aa374abd0de21736842bfdff00b9f773b1c6c444daeaf21c619ff9  fast_k15_hall_dm (H100 binary)
```

The five adjacent-pair V2 tables have hashes

```text
f925190c26b928c7e3032268981ab044ea0bc6b1337281f3c3315b61ac2f5fcb  pair01.centered_exact_v2.tsv
b9dbd2e1e98c0a207123429babc78288fef2026c33b6e649ad25f0635a704ced  pair12.centered_exact_v2.tsv
de2c9f2e8937ed702273971aa637920026553289fc142ca922d3fa44084a7492  pair23.centered_exact_v2.tsv
c0a078a885fee8839619b2dc6b8910ce5b138ee4f7aa6d2016d522c1eb211298  pair34.centered_exact_v2.tsv
acf749ad63761331cfc7b84a3df98da469f0b27a0de33f92b229419321bf9600  pair40.centered_exact_v2.tsv
```

All ten parent/table regressions return
`K15_CENTERED_EXACT_V2_REGRESSION_PASS`; their individual hashes, together
with the five parent and five target-shore hashes, are frozen in
`scratch/k15_centered_exact_v2_20260728/k15_five_pair_centered_exact_v2.sha256`.
The complete 79-file local provenance bundle contains the original 55-file
H100 export (five tables, generation commands/stdout/stderr, all ten
regressions, executed sources and binaries, and the pair-01 integration
records) plus the five fixed-parent command/log/stderr/summary quartets, their
runner, checksum file, manifest, and verifier.

The final-consumer fixed-parent calibration has summary hash

```text
6e896baada98cbb096323986079ec7a8b48f2ff7d740b618651a66ee019be414  pair01.fixed_h29.centered_exact_v2.summary.json
```

and reports `CERTIFIED_INFEASIBLE`, terminal CP-SAT status `INFEASIBLE`,
`fix_parent=0`, no upper or dynamic cuts, residence enabled, and only the two
V2 exact rows at thresholds 1524 and 1528.  This is a channel regression, not
a two-parent no-go.  An earlier unrestricted pair-01 attempt used consumer
hash `438832862c07...`, reached CP-SAT `UNKNOWN` after 900 solver seconds, and
is retained only as a memory/scalability record; it is not an UNSAT
certificate and is not attributed to the final consumer.

The separately certified ten two-parent exclusions use the proof-safe
endpoint-conditioned boundary *upper relaxation*.  Their exact scope and all
§335 hashes are preserved in
`scratch/k15_exact_pair_nogos_20260728/MANIFEST.json`; the verifier rejects
any `allow6` artifact.  Since an exact-boundary feasible path would also be
feasible under that upper relaxation, those ten UNSAT results remain valid
pair no-gos without rerunning the much larger literal inverse-order model.

## 9. Lane-I status after integration

The V2 generator and independent native scorer were applied to every parent
chronology in each of the five adjacent unions.  The following table records
the literal total; a parenthetical `L=(a,b,c)` is the nonzero left-endpoint
contribution by depth, so it cannot be hidden in an interior count.

| union | chronology | own-shore literal total | other-shore literal total |
|---|---:|---:|---:|
| 01 | $P_0$ | $B_0:1495$ | $B_1:1800$ |
| 01 | $P_1$ | $B_1:1498$ | $B_0:1794$ |
| 12 | $P_1$ | $B_1:1498$ | $B_2:1613$ |
| 12 | $P_2$ | $B_2:1498$, $L=(1,1,0)$ | $B_1:1612$ |
| 23 | $P_2$ | $B_2:1498$, $L=(1,1,0)$ | $B_3:1903$ |
| 23 | $P_3$ | $B_3:1495$ | $B_2:1891$, $L=(0,0,1)$ |
| 34 | $P_3$ | $B_3:1495$ | $B_4:1800$, $L=(0,0,1)$ |
| 34 | $P_4$ | $B_4:1495$ | $B_3:1800$, $L=(0,0,1)$ |
| 40 | $P_4$ | $B_4:1495$ | $B_0:1739$ |
| 40 | $P_0$ | $B_0:1495$ | $B_4:1739$ |

Every displayed number agrees exactly with the native complete-carrier
neighborhood scorer.  In particular the nonzero $P_2$ endpoint cells show
that the integration is not silently replacing all boundaries by zero.
Moreover one deficient chronology in each union was fixed inside the actual
CP-SAT circuit and solved through the literal V2 rows.  All five returned
top-level `CERTIFIED_INFEASIBLE` with terminal solver status `INFEASIBLE`, no
upper or dynamic cuts, residence enabled, and the intended local
`fix_parent` value.  The 20 command/log/stderr/summary hashes are frozen in
`k15_five_pair_fixed_parent_centered_exact_v2.sha256`.  These remain scoped
channel calibrations because each model fixes its chronology.

The logical conclusions are now sharply separated.

1. The fixed $P_0$ regression reproduces
   $(81,395,1019)+0+0=1495$, hence the Hall-29 failure, through the actual
   shared inverse-order CP-SAT channel; the other four fixed calibrations
   exercise the same channel on every adjacent pair, including the nonzero
   $P_2$ boundary palette.
2. Each of the ten two-parent directed unions is excluded by the already
   certified conditional-boundary-upper model.  This implication is
   proof-safe because the conditional maximum dominates the literal boundary
   contribution statewise.
3. The unrestricted literal pair-01 solve is `UNKNOWN`, not a second proof of
   item 2.  It consumed about 130.7 GB peak RSS.  Consequently launching a
   literal three-parent or five-parent inverse-order solve on the same H100
   would not be a responsible finite test; none was launched.
4. Thus the surviving finite gate is genuinely at least three parents.  The
   old five-parent boundary-upper search remains `UNKNOWN`; no exact or
   relaxed five-face UNSAT is claimed here.

For every future certificate, `status=CERTIFIED_INFEASIBLE` is necessary but
not sufficient as a citation: one must also quote the serialized
`certified_infeasible_scope`.  In particular a summary with `fix_parent=0`
is only a regression, whereas a pair-union no-go requires `fix_parent=null`,
no force tuple/endpoints, no legacy interior-only mode, the stated residence
setting, and the exact list of upper/dynamic/preloaded cuts.
