# K16 neutral collar slides: exact P3, surplus flow, and the fusion boundary

Date: 2026-07-29  
Status: universal flow and fusion lemmas proved; the complete marked
radius-two component through the frozen `L57614` collar is audited exactly.
A two-slide macroscopic topology rethread is materialized.  No residence
descent, rebuilt overlay, or deeper-shadow preservation is claimed.

## 1. Objects and terminology

Let `F` be a simple spanning two-factor of `J(16,8)`.  For an edge `uv`, put

\[
 L(uv)=u\cap v,\qquad U(uv)=u\cup v.                       \tag{1.1}
\]

Write `m_L(R)` and `m_U(T)` for the physical lower- and upper-q1 loads.  A
factor is **q1-complete** when all 11,440 colours on each shore have positive
load.  In that case define the nonnegative surplus vectors

\[
 \lambda_R=m_L(R)-1,\qquad \mu_T=m_U(T)-1.                \tag{1.2}
\]

For a coordinate `h`, let `rho_h(F)` be the number of proper cyclic one-runs
of `h`, of all positive lengths.  Let

\[
 D_j(F)=\#\{\text{proper }h\text{-runs of length }j:
                 h\in[16]\},\qquad j=1,2,3,              \tag{1.3}
\]

and

\[
 D(F)=D_1+D_2+D_3,\qquad
 \Psi(F)=3D_1+2D_2+D_3.                                  \tag{1.4}
\]

Thus `D` is the literal short-residence objective and `Psi` is the finer
distance-to-length-four charge.

For fixed `h`, the intrinsic part of a defect is its path component in the
induced factor graph on middle sets containing `h`.  The two incident
`h=0` neighbours are its **collar ports**.  Moving a collar port need not move
the intrinsic defect.

## 2. The exact q1/run conservation identities

### Theorem 2.1 (run vector equals the q1-surplus marginal)

Every q1-complete spanning two-factor of `J(16,8)` satisfies

\[
 \sum_R\lambda_R=\sum_T\mu_T=12870-11440=1430,            \tag{2.1}
\]

and, for every coordinate `h`,

\[
 \boxed{
 \rho_h=\sum_{T\ni h}\mu_T
       =1430-\sum_{R\ni h}\lambda_R.}                    \tag{2.2}
\]

Moreover

\[
                         \boxed{\sum_{h=0}^{15}\rho_h=12870.} \tag{2.3}
\]

#### Proof

Every Johnson edge satisfies the incidence-vector identity

\[
 {\mathbf 1}_{L(uv)}+{\mathbf 1}_{U(uv)}
 ={\mathbf 1}_u+{\mathbf 1}_v.                           \tag{2.4}
\]

Summing loads gives (2.1).  Fix `h`, and let `A_h` be the number of factor
edges whose two endpoints contain `h`.  There are `binom(15,7)=6435`
middle vertices containing `h`, each of factor degree two.  The number of
factor edges crossing the `h`-cut is `2 rho_h`, so

\[
 2A_h+2\rho_h=2\binom{15}{7},\qquad A_h=6435-\rho_h.      \tag{2.5}
\]

An edge has lower colour containing `h` exactly when both endpoints contain
`h`.  Hence

\[
 \sum_{R\ni h}\lambda_R=A_h-\binom{15}{6}
 =6435-\rho_h-5005=1430-\rho_h.                           \tag{2.6}
\]

An edge has upper colour containing `h` exactly when at least one endpoint
contains `h`.  The number of these edges is

\[
 A_h+2\rho_h=6435+\rho_h.                                 \tag{2.7}
\]

There are `binom(15,8)=6435` upper baseline colours containing `h`, proving
the other equality in (2.2).

Finally, every Johnson edge crosses exactly two coordinate cuts.  Counting
crossing-edge/coordinate incidences gives

\[
 2\sum_h\rho_h=2|F|=2(12870),                             \tag{2.8}
\]

which proves (2.3).  ∎

Thus a fusion which reduces `rho_h` by one must fission a run somewhere
else.  This is a conservation law for **all** Johnson two-factors, not merely
for q1-complete ones.  It does not force the compensating new run to be
short.

## 3. Complete pure-collar slide normal form

Fix a rank-seven set `S`; choose distinct `c,alpha,beta` outside `S`.  Put

\[
 v=S+c,\qquad z=S+\alpha,\qquad a=S+\beta.                \tag{3.1}
\]

Here `v` is the final `c=1` vertex of a marked run, `z` is its old `c=0`
collar port, and `a` is the proposed new `c=0` port.  A pure collar square
deletes `zv,ab` and inserts `va,zb`, where `b` omits `c` and is Johnson
adjacent to both `z` and `a`.  The four vertices are assumed distinct and
the inserted edges unused, as required for a nontrivial simple C4 switch.

### Lemma 3.1 (two and only two collar geometries)

Exactly one of the following holds:

* **T type:** `b=S+gamma`, with `gamma` outside
  `S union {c,alpha,beta}`;
* **D type:** `b=(S-s)+alpha+beta` for a unique `s in S`.

#### Proof

Let `t=|b intersect S|`.  Adjacency to `S+alpha` and `S+beta` gives

\[
 t+1[\alpha\in b]=t+1[\beta\in b]=7.                    \tag{3.2}
\]

Thus either both indicators vanish and `t=7`, giving T type, or both equal
one and `t=6`, giving D type.  The condition `c notin b` excludes `gamma=c`.
There are no other cases.  ∎

### Theorem 3.2 (exact D-slide ledger)

For a D slide `alpha -> beta`, the four q1 labels are

\[
\begin{array}{c|cc}
 &L&U\\ \hline
zv&S&S+c+\alpha\\
ab&(S-s)+\beta&S+\alpha+\beta\\
va&S&S+c+\beta\\
zb&(S-s)+\alpha&S+\alpha+\beta.
\end{array}                                               \tag{3.3}
\]

Consequently the load vector transports one upper occurrence

\[
 S+c+\alpha\longrightarrow S+c+\beta                     \tag{3.4}
\]

and one lower occurrence in the opposite direction

\[
 (S-s)+\beta\longrightarrow(S-s)+\alpha.                 \tag{3.5}
\]

If the pre-slide factor is q1-complete, then the new factor remains
q1-complete precisely when the post-move loads in (3.3) remain positive;
equivalently, the two distinct donor loads in (3.4)--(3.5) are at least two.
Under this condition, the two transported occurrences are surplus tokens.
Its exact run-vector derivative is

\[
                         \boxed{\Delta\rho=e_\beta-e_\alpha.} \tag{3.6}
\]

For a T slide all lower labels are unchanged and the two upper transfers
cancel coordinatewise, so `Delta rho=0`.

Every pure `c`-collar slide fixes the induced internal edge set `F[V_c]`
pointwise.  Hence every intrinsic `c`-run, including its vertex set and
length, is invariant under an arbitrary sequence of pure `c` slides.  Such
a sequence cannot fuse, shorten, or cancel two `c`-defects.

#### Proof

The table follows by intersection and union.  Equation (3.6) follows either
from (2.2), or directly from the edge-flip labels: the old D edges cross
coordinate pairs `{c,alpha}` and `{s,alpha}`, while the new edges cross
`{c,beta}` and `{s,beta}`.  Thus the number of `alpha`-crossings drops by two
and the number of `beta`-crossings rises by two.  The T labels are
`{c,alpha},{beta,gamma}` before and
`{c,beta},{alpha,gamma}` after, giving zero coordinatewise change.

The only affected edge incident with a `c=1` vertex is a crossing edge;
all other affected endpoints omit `c`.  Therefore no edge with two
`c=1` endpoints changes, proving the last assertion.  ∎

## 4. The frozen marked defect and its exact three-state component

Put

\[
 S=64008=\{3,9,11,12,13,14,15\},\qquad c=5,              \tag{4.1}
\]

and let

\[
 v=64040=S+5,\qquad w=64036.                              \tag{4.2}
\]

The marked intrinsic defect is the coordinate-five length-two path
`{w,v}` with internal edge `(64036,64040)` and fixed left collar edge
`(64036,65028)`.  Its mobile right seam is

\[
                         (v,x_j),\qquad x_j=S+j.           \tag{4.3}
\]

In all three audited states `(v,x_j)` is the unique provider of lower colour
`S`; its load is exactly one.

At `S_8` this is precisely the three-edge closure occurring in the frozen
19-row signed Hall--Farkas obstruction.  The move `S_8 -> S_4` breaks that
fixed row.  From `S_4` onward the assertions below use fresh literal
degree/q1/run audits; the old Farkas row is not assumed to remain valid or to
certify the successor states.

The complete marked radius-two graph is

\[
                         \boxed{S_8\;--\;S_4\;--\;S_{10}}. \tag{4.4}
\]

The exact state data are

\[
\begin{array}{c|c|c|c|c|c}
\text{state}&x_j&\text{components}&(D_1,D_2,D_3)&D&\Psi\\ \hline
S_8&64264&(13,12857)&(131,902,1189)&2222&3386\\
S_4&64024&(13,2270,10587)&(131,902,1189)&2222&3386\\
S_{10}&65032&(13,967,2270,9620)&(130,902,1190)&2222&3384.
\end{array}                                               \tag{4.5}
\]

At each state, every current marked-closure edge was paired with every
vertex-disjoint factor edge and both cross matchings were considered: 77,202
four-vertex raw pairings per state.  After Johnson legality and
deduplication, the geometric counts are

\[
                         29,\quad26,\quad22,               \tag{4.6}
\]

and the numbers preserving both complete q1 palettes are

\[
                         1,\quad2,\quad1.                  \tag{4.7}
\]

They are exactly the two edges in (4.4), with their inverses.  Literal cycle
replay proves that all four directed moves have `Delta D=0`.

### 4.1 First edge: `8 -> 4`

This is the previously frozen direct slide

\[
\begin{array}{ll}
\mathrm{delete}&(56088,64024),(64040,64264),\\
\mathrm{insert}&(56088,64264),(64024,64040).
\end{array}                                               \tag{4.8}
\]

Its complete nonzero q1 ledger is

\[
 L_{55832}:2\to1,\quad L_{56072}:1\to2,\quad
 U_{64296}:2\to1,\quad U_{64056}:1\to2.                  \tag{4.9}
\]

It changes no intrinsic short defect.  It only replaces the marked right
collar `x_8` by `x_4`, and

\[
                         \Delta\rho=e_4-e_8.              \tag{4.10}
\]

### 4.2 Second edge: `4 -> 10`

The new forward slide is

\[
\begin{array}{ll}
\mathrm{delete}&(64024,64040),(65032,65040),\\
\mathrm{insert}&(64024,65040),(64040,65032).
\end{array}                                               \tag{4.11}
\]

It is D type with `alpha=4,beta=10,s=3`.  Its complete q1 ledger is

\[
 L_{65024}:3\to2,\quad L_{64016}:1\to2,\quad
 U_{64056}:2\to1,\quad U_{65064}:1\to2,                  \tag{4.12}
\]

and

\[
                         \Delta\rho=e_{10}-e_4.           \tag{4.13}
\]

It removes

* the coordinate-four length-one closure
  `{(65025,65040),(65032,65040)}`; and
* the marked coordinate-five length-two closure at `x_4`;

and creates

* the same intrinsic coordinate-five length-two defect with collar `x_10`;
  and
* the coordinate-ten length-three closure
  `{(47713,48705),(48705,65025),(65025,65040),
     (64024,65040)}`.

Thus it replaces two closure signatures by two closure signatures, but at
the intrinsic-charge level it is one-for-one scattering
`(4,length 1) -> (10,length 3)` plus transport of the unchanged marked
coordinate-five collar.  It is not a cancellation.  It preserves `D=2222`
but strictly improves the finer charge by two.

The chain is genuinely stateful: (4.9) creates the second copy of
`U_64056`, and (4.12) immediately spends that copy.  At `S_8` this upper
colour has load one, so the `4 -> 10` donor inequality is unavailable before
the first slide.  The two squares are therefore an adaptive surplus route,
not two independently executable edits.

### Corollary 4.3 (exact local no-cycle theorem)

Within the graph of q1-complete radius-two switches deleting an edge of the
three-edge marked closure at one of the states (4.4), every closed walk is
inverse backtracking.
There is no nonbacktracking cycle, no collar holonomy, and no coalescence or
cancellation of the marked defect.  Any continuation beyond `S_10` requires
a move disjoint from the marked closure, a remote slack-changing preparatory
move, or a compound exchange.

The conclusion is local to the marked component.  It is not a no-go for the
full q1-complete factor fibre.

## 5. A genuine two-step macroscopic rethread

Although (4.4) has no cycle, it already gives a nonlocal topology effect:

\[
 (13,12857)\longrightarrow(13,2270,10587)
 \longrightarrow(13,967,2270,9620).                      \tag{5.1}
\]

Both radius-two steps preserve q1 completeness and `D=2222`.  Thus local
collar squares can assemble a literal macroscopic cycle rethread.  The
second step also improves `(D,Psi)` lexicographically from `(2222,3386)` to
`(2222,3384)`.  What fails is continuation: `S_10` has only the inverse
marked-closure move.  This particular rethread splits rather than merges
physical cycles; reversing it merges them only by returning through the
already known states.  It is therefore not a connectivity improvement.

### Theorem 5.1 (conditional same-witness diamond holonomy)

Fix `S,c,s`.  Suppose a literally legal sequence of D slides has labels

\[
 \alpha_0\to\alpha_1\to\cdots\to\alpha_t=\alpha_0.       \tag{5.2}
\]

Then the complete lower and upper q1 load changes telescope to zero, as does
the run-vector change.  If every step is scalar-residence-neutral, the final
factor has the same q1 load vectors, the same `rho`, the same marked
`c`-internal factor, and the same `D` as the initial factor.  If its physical
edge set is different, the sequence is a genuine macroscopic neutral
rethread/holonomy.

#### Proof

At step `i`, (3.4)--(3.5) give

\[
 U_{\alpha_i}\to U_{\alpha_{i+1}},\qquad
 L^{s}_{\alpha_{i+1}}\to L^{s}_{\alpha_i},                \tag{5.3}
\]

where `U_alpha=S+c+alpha` and `L^s_alpha=(S-s)+alpha`; the
other lower and upper labels cancel inside that step.  Both sums telescope
around (5.2), and (3.6) telescopes `Delta rho`.  The marked internal factor
is fixed by Theorem 3.2.  Scalar neutrality gives the last assertion.  ∎

The audited path (4.4) has no such cycle.  A same-witness diamond cycle is
therefore an exact constructive target for a remote router; it is not
present in the frozen local catalogue.

## 6. The exact escape from pure transport: a fusion square

Let `P,Q` be two distinct intrinsic `h`-run paths of orders `a,b<=3`, with
boundary edges `pz,qy`, where `p,q` contain `h` and `z,y` omit it.  If `pq`
and `zy` are unused Johnson edges, then

\[
 F'=F-\{pz,qy\}+\{pq,zy\}                                \tag{6.1}
\]

is the unique radius-two geometry which joins `P,Q` while deleting no
`h`-internal edge.  Its exact `h`-defect derivative is

\[
                         \Delta_hD=1[a+b\le3]-2.          \tag{6.2}
\]

It coalesces two defects into one when `a+b<=3` and annihilates both when
`a+b>=4`.  It also has `Delta rho_h=-1`, so (2.3) forces

\[
                         \sum_{g\ne h}\Delta\rho_g=1.     \tag{6.3}
\]

The move is q1-complete exactly when all lower and upper loads after its
four-label delta remain positive.  Its global residence derivative is

\[
 \Delta D=1[a+b\le3]-2+\sum_{g\ne h}\Delta_gD.           \tag{6.4}
\]

In particular an annihilating fusion is a strict descent whenever the net
short-defect change at the other coordinates is at most one.

Therefore there is no universal law saying every radius-two C4 can only move
defects.  The sharp law is:

* pure collar squares conserve the marked intrinsic defect;
* scalar-neutral chains conserve only the number `D` and may scatter named
  defects; annihilating two named defects along an all-neutral chain must
  create two elsewhere, while coalescing two into one must create one
  elsewhere;
* a strict improvement must contain some nonneutral C4 or compound exchange
  with negative total short-run ledger; the fusion square (6.1) is one exact
  sufficient class, not the only possible negative C4 geometry.

## 7. Square-class invariant and exact scope

Let `B` be the unsigned vertex-edge incidence matrix of the Johnson graph.
The signed column of every C4 slide lies in `ker_Z B`.  Hence every slide
chain `F -> F'` satisfies

\[
 {\mathbf 1}_{F'}-{\mathbf 1}_F=\sum_i\delta_i,
 \qquad B\delta_i=0.                                      \tag{7.1}
\]

and modulo two, `F` and `F'` have the same class in the Johnson cycle space
quotiented by legal four-cycles.  Equivalently, every mod-two edge weighting
whose sum on every legal Johnson square is zero has invariant pairing with
the factor.  No claim is made that this computes the whole quotient or that
it obstructs the present P3.

The permanent bounded replays are

```text
scratch/audit_k16_l57614_neutral_collar_slide_graph_20260729.py
scratch/k16_l57614_neutral_collar_slide_graph_20260729.audit.json

scratch/audit_k16_l57614_neutral_collar_p3_20260729.py
scratch/k16_l57614_neutral_collar_p3_20260729.audit.json
scratch/k16_l57614_neutral_collar_state_s10_20260729.json
```

The first is the canonical fail-closed three-state census; the second
independently materializes `S_10` and replays the full q1, run-vector,
short-charge, motif, and component ledgers at all three states.  Both are
bounded `O(|F|)`/constant-state audits, not SAT, CP, LP, or a fibre search.

Not proved:

* preservation of q2/deeper decks by either neutral slide;
* feasibility of the rebuilt resident/q1 overlay after `S_10`;
* existence of a remote preparatory move reopening the marked collar graph;
* a legal same-witness holonomy cycle; or
* any factor with `D<2222`.
