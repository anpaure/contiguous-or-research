# Exact lifetime/prefix compiler-Hall Benders cuts

Date: 2026-07-29

Status: the carrier-only union-Hall cut, its primitive lifetime explanation,
and the lower-`q2`/all-width-upper prefix cuts are proved.  A deterministic
replay on the frozen `k=11` and `k=15` carriers passes.  The result does **not**
project a Hall shore of one arbitrarily sampled core to the carrier: that
projection is false, and an exact decorated-state replacement is stated
below.

## 1. Strict-spiral run coordinates

Let `T=(T_j)_(j in Z_W)` be a cyclic rank-`r` Johnson carrier with

\[
 T_{j+N}=\rho^vT_j,
 \qquad W=kN,
 \qquad (v,k)=1,
 \tag{1.1}
\]

where `rho` adds one to every coordinate modulo `k`.  Write

\[
 T_{j+1}=T_j-\{\alpha_j\}+\{\beta_j\}.
 \tag{1.2}
\]

Let `b_u=1[0 in T_u]`.  On a cyclic lift to the integers, write the positive
runs of `b` as

\[
 (p_t,e_t]\cap\mathbb Z,
 \qquad e_t=p_t+\ell_t,
 \qquad p_{t+1}=p_t+\ell_t+g_t,
 \tag{1.3}
\]

where `ell_t` is the positive lifetime and `g_t` the following zero gap.
Put

\[
 u_{j,x}=\langle j-Nv^{-1}x\rangle_W.
 \tag{1.4}
\]

All endpoint comparisons below are cyclic: equivalently, choose the unique
integer lift of `u_(j,x)` in one fixed period and include the corresponding
periodic lifts of the `p_t,e_t`.

### Lemma 1.1 (exact run reification)

For every physical position `j` and coordinate `x`,

\[
 x\in T_j
 \iff
 \bigvee_t[p_t<u_{j,x}\le e_t],                         \tag{1.5}
\]

\[
 \beta_j=x
 \iff
 \bigvee_t[p_t=u_{j,x}],                                \tag{1.6}
\]

and

\[
 \alpha_j=x
 \iff
 \bigvee_t[e_t=u_{j,x}].                                \tag{1.7}
\]

If the carrier is depth-`d` resident and

\[
 P_j=\bigcap_{a=0}^{d}T_{j-a},                          \tag{1.8}
\]

then

\[
 x\in P_j
 \iff
 E_{j,x}:=\bigvee_t[p_t+d<u_{j,x}\le e_t].              \tag{1.9}
\]

#### Proof

Equation (1.1) says that translating physical position by `N` translates
the coordinate label by `v`.  Hence membership of `x` at `j` is membership
of coordinate zero at the scalar position (1.4), proving (1.5).  A scalar
zero-to-one edge is exactly a run start `p_t`, and a one-to-zero edge is
exactly a run end `e_t`; this proves (1.6)--(1.7).  Finally, the `d+1`
scalar positions corresponding to (1.8) are

\[
 u_{j,x}-d,\ldots,u_{j,x}.
\]

They all lie in `(p_t,e_t]` exactly when
`p_t+d<u_(j,x)<=e_t`, proving (1.9).  \(\square\)

Thus every atom used below is a disjunction of exact linear endpoint
relations in the prefix variables `p_t`, lifetimes `ell_t`, and gaps `g_t`.

## 2. The union of all one-core incidences

A one-core of `P` is a cyclic sequence `C` satisfying

\[
 C_j\subseteq P_j,
 \qquad C_j\cup C_{j+1}=P_j\cup P_{j+1}.                \tag{2.1}
\]

For each position define its forced port set

\[
 F_j=\{\alpha_j,\beta_{j-d-1}\}.                        \tag{2.2}
\]

The set may be a singleton when the two coordinates coincide.

### Lemma 2.1 (forced endpoints)

For every one-core `C`,

\[
 F_j\subseteq C_j.                                      \tag{2.3}
\]

#### Proof

Fix a coordinate `x`.  Its support in `P` is a disjoint union of positive
paths.  Equation (2.1) says that the selected `C`-positions form a vertex
cover of every edge on which `P` is nonzero.  If `a` is the initial endpoint
of a positive support path, then `P_(a-1)=0` and `P_a=1`; equality in (2.1)
on the boundary edge `(a-1,a)` forces `C_a=1`.  The terminal boundary edge
forces the other endpoint in the same way.  By (1.6)--(1.9), the terminal
endpoint at `j` is `alpha_j` and the initial endpoint at `j` is
`beta_(j-d-1)`.  \(\square\)

### Theorem 2.2 (exact incidence union over all cores)

For every nonempty target `S` and position `j`,

\[
 \exists\hbox{ a one-core }C:
 C_j\subseteq S\subseteq P_j
 \quad\Longleftrightarrow\quad
 F_j\subseteq S\subseteq P_j.                           \tag{2.4}
\]

#### Proof

Necessity is Lemma 2.1.  Conversely assume the right side.  For each
coordinate `x` in `P_j\S`, position `j` is not an endpoint of its `P`-support
path, because \(F_j\subseteq S\); omit `j` from the coordinate-`x` cover and
select every other position in that support.  The omitted vertex is internal
and its two neighbours are selected, so all support edges remain covered.
For every other coordinate select its full `P`-support.  The constraints are
coordinatewise independent, and the resulting one-core has `C_j=S`.
\(\square\)

The theorem is incidencewise.  Cores witnessing two different pairs
`(S,j)` need not be the same; this noncoexistence is the residual common-core
gate.

## 3. A proof-safe carrier-only Hall cut

Let `S_h` be the target family used by the graded compiler, and let `O` run
over its `C_k` coordinate-rotation orbits.  Give `O` its physical weight

\[
 w(O)=|O|.                                               \tag{3.1}
\]

For a set `X` of target orbits and a position block `J in Z_N`, define

\[
 z_J^X=
 \bigvee_{O\in X}\ \bigvee_{R\in O}
 [F_J\subseteq R\subseteq P_J].                         \tag{3.2}
\]

Using all phases `R in O` makes (3.2) independent of the chosen physical
representative of the right orbit.  Short orbits must occur once per
distinct phase, not `k` times.

### Theorem 3.1 (union-Hall Benders row)

If there exists any one-core whose physical compiler graph has a matching
saturating all targets, then, for every `X`,

\[
 \boxed{
 \sum_{J=0}^{N-1}z_J^X
 \ge b_X:=
 \left\lceil{\sum_{O\in X}w(O)\over k}\right\rceil .}
 \tag{3.3}
\]

Suppose an incumbent carrier has

\[
 B=\{J:z_J^X=1\},\qquad |B|<b_X.                        \tag{3.4}
\]

Then the incumbent-separating relative cut

\[
 \boxed{
 \sum_{J\notin B}z_J^X\ge b_X-|B|}
 \tag{3.5}
\]

is globally valid.

#### Proof

Form the union graph `U` containing an edge `S--j` exactly when some
one-core can realize that incidence.  By Theorem 2.2 this is precisely the
graph (3.2), and every fixed-core graph is a subgraph of `U`.  Hence a
successful fixed core implies that `U` has a saturating matching.

The graph `U` is `C_k`-equivariant.  Hall deficiency is supermodular, so the
union of all rotations of a maximum-deficiency shore is again a
maximum-deficiency shore.  It therefore suffices to test unions `X` of full
target orbits.  Their right neighbourhood is a union of `N` free physical
position orbits, each of capacity `k`, while their demand is
`sum_(O in X)w(O)`.  This gives (3.3).  Finally

\[
 \sum_{J\in B}z_J^X\le |B|,
\]

so (3.5) is a consequence of (3.3).  It is violated by (3.4).  \(\square\)

### Corollary 3.2 (primitive lifetime explanation)

For each \(J\notin B\) and phased target
\(R\in\bigcup_{O\in X}O\), choose one of the
following atoms which is false at the incumbent:

\[
 a_{R,J}=E_{J,x}
 \quad\hbox{for some }x\in R\setminus P_J,              \tag{3.6a}
\]

or, when \(R\subseteq P_J\),

\[
 a_{R,J}=\bigvee_{x\in R}[\alpha_J=x]
 \quad\hbox{if }\alpha_J\notin R,                       \tag{3.6b}
\]

or

\[
 a_{R,J}=\bigvee_{x\in R}[\beta_{J-d-1}=x]
 \quad\hbox{if }\beta_{J-d-1}\notin R.                 \tag{3.6c}
\]

At least one case exists because `J notin B`.  Put

\[
 r_J=\bigvee_{O\in X}\ \bigvee_{R\in O}a_{R,J}.        \tag{3.7}
\]

Then

\[
 \boxed{
 \sum_{J\notin B}r_J\ge b_X-|B|}
 \tag{3.8}
\]

is valid and incumbent-false.  In defect one it is the single requested
disjunction

\[
 \bigvee_{J\notin B}\ \bigvee_{O\in X,R\in O}a_{R,J}.
 \tag{3.9}
\]

#### Proof

Each conjunction \([F_J\subseteq R\subseteq P_J]\) implies the selected atom
\(a_{R,J}\).  Hence \(z_J^X\) implies \(r_J\).  Equation (3.8) follows from
(3.5), while every selected atom is false at the incumbent.  Lemma 1.1
expresses (3.6) exactly in run endpoints and lifetimes.  \(\square\)

Unlike a full no-good, this cut excludes every schedule which leaves all
selected failed endpoint/prefix relations unchanged, regardless of all
unrelated choices.  Hence it dominates the full no-good whenever at least
one unrelated assignment can vary without repairing a selected atom.

### The sampled-core obstruction

A Hall shore of one sampled core is not enough to obtain an
incumbent-violated carrier-only row.  On the independently verified carrier
`scratch/fixtures/k11_equivariant_carrier_repo_v1.json`, the choice `C=P`
has no rank-one or rank-two incidences and therefore fails Hall, while the
canonical coordinatewise one-core on that same carrier passes physical and
weighted Hall `231/231`; see
`scratch/k11_graded_pipeline_repo.audit.json`.  Thus any carrier-only cut
claimed merely from the `C=P` shore would delete a valid carrier.

If omission/core states are retained, the exact replacement is the decorated
row

\[
 \sum_{J,\mathcal C,Z}g_J^X(\mathcal C,Z)
 y_{J,\mathcal C,Z}\ge b_X,                            \tag{3.10}
\]

where \(\mathcal C\) is the complete directed carrier/collar state, `Z` is
the omission state, `y` is the exact combined-state literal, and `g` says
that this state has an incidence to `X`.  Equation (3.10), together with
one-hot, legal-transition, and twisted-seam constraints, is exact for a
fixed-core shore.  A bare local `Z` variable without its carrier/collar
state is not sufficient.  Without these states, (3.3) is a necessary
carrier relaxation and can miss a purely noncoexistence obstruction.

## 4. Exact alpha/beta prefix identities

Write

\[
 X_{j,x}=\mathbf1[x\in T_j],
 \quad
 A_{j,q}(x)=\sum_{a=0}^{q-1}\mathbf1[\alpha_{j+a}=x],
 \quad
 B_{j,\ell}(x)=\sum_{a=0}^{\ell-1}\mathbf1[\beta_{j+a}=x].
 \tag{4.1}
\]

### Lemma 4.1 (intersection and union prefixes)

For every cyclic Johnson chronology,

\[
 x\in\bigcap_{a=0}^{q}T_{j+a}
 \iff X_{j,x}=1\ \hbox{ and }\ A_{j,q}(x)=0,            \tag{4.2}
\]

and

\[
 x\in\bigcup_{a=0}^{\ell}T_{j+a}
 \iff X_{j,x}+B_{j,\ell}(x)\ge1.                       \tag{4.3}
\]

#### Proof

A coordinate belongs to all states precisely when it is present initially
and is never deleted in the intervening transitions.  It belongs to at
least one state precisely when it is present initially or is inserted in
an intervening transition.  These are (4.2)--(4.3).  \(\square\)

## 5. Missing lower-`q2` orbit cuts

Assume depth-two residence, so every triple intersection has rank `r-2`.
Then

\[
 I_j^{(2)}:=T_j\cap T_{j+1}\cap T_{j+2}
 =T_j\setminus\{\alpha_j,\alpha_{j+1}\}.               \tag{5.1}
\]

For every required rank-`r-2` target orbit `O`, the exact coverage row is

\[
 \boxed{
 \bigvee_{J=0}^{N-1}\ \bigvee_{R\in O}
 [I_J^{(2)}=R].}
 \tag{5.2}
\]

Because both sides have certified rank `r-2`, equality in (5.2) is
equivalent to the inside conditions

\[
 X_{J,x}=1,\qquad A_{J,2}(x)=0\qquad(x\in R).          \tag{5.3}
\]

Without the rank certificate, retain also

\[
 X_{J,y}=0\ \vee\ A_{J,2}(y)\ge1\qquad(y\notin R).     \tag{5.4}
\]

For a missing incumbent orbit, choose one false atom of (5.3)--(5.4) for
each candidate `(J,R)` and disjoin the choices.  If a future carrier
satisfies (5.2), all atoms of one candidate are true, so the chosen atom for
that candidate is true.  The resulting disjunction is therefore globally
valid and excludes the incumbent.

## 6. Missing upper-orbit cuts

For each starting position and coordinate define its first-arrival time

\[
 \delta_j(x)=
 \begin{cases}
 0,&x\in T_j,\\
 1+\min\{a\ge0:\beta_{j+a}=x\},&x\notin T_j.
 \end{cases}                                             \tag{6.1}
\]

### Theorem 6.1 (exact all-width upper criterion)

For every proper target `S`,

\[
 \exists\ell\ge0:\ \bigcup_{a=0}^{\ell}T_{j+a}=S
 \quad\Longleftrightarrow\quad
 \max_{x\in S}\delta_j(x)
 <\min_{y\notin S}\delta_j(y).                         \tag{6.2}
\]

Consequently a required upper target orbit `O` has the exact row

\[
 \boxed{
 \bigvee_{J=0}^{N-1}\ \bigvee_{R\in O}
 \left[
 \max_{x\in R}\delta_J(x)
 <\min_{y\notin R}\delta_J(y)
 \right].}
 \tag{6.3}
\]

#### Proof

By Lemma 4.1, coordinate `x` lies in the union ending at offset `ell` exactly
when `delta_j(x)<=ell`.  Such a threshold selects exactly `S` if and only if
every arrival in `S` precedes every arrival outside `S`, which is (6.2).
Quotienting physical starts and target phases gives (6.3).  \(\square\)

If (6.3) fails at the incumbent, then for every `(J,R)` choose a pair
`x in R`, `y notin R` with

\[
 \delta_J(y)\le\delta_J(x).
\]

The disjunction of the currently false atoms

\[
 [\delta_J(x)<\delta_J(y)]                               \tag{6.4}
\]

over all `(J,R)` is a proof-safe incumbent explanation.

The arrival function is itself a lifetime/gap formula.  With cyclic integer
lifts,

\[
 \delta(u)=0\quad\hbox{for }p_t<u\le e_t,               \tag{6.5a}
\]

and

\[
 \delta(u)=p_{t+1}+1-u
 \quad\hbox{for }e_t<u\le p_{t+1}.                      \tag{6.5b}
\]

Thus every comparison (6.4) is a finite disjunction of linear relations in
run endpoints/lifetimes.  A fixed physical width `q` must **not** replace
(6.3) for a rank-`r+q` target when `q>=3`: a coordinate may be recycled, so
an exact witness can be longer than `q` transitions.

## 7. Solver-free audit

The executable audit is

`scratch/audit_lifetime_prefix_benders_cuts_20260729.py`.

It reconstructs the runs, checks (1.5)--(1.9), constructs the union graph of
Theorem 2.2, runs the exact weighted Hall flow, checks (5.1)--(5.2) against
literal intersections, and checks (6.2)--(6.3) against literal all-width
upper unions.  It also emits hashes of primitive incumbent-false explanation
atoms for one actual missing `q2` and upper orbit.  It performs no search.

The exact results are:

| fixture | lifetimes `(min,max,sum)` | gaps `(min,max,sum)` | union Hall | lower `q2` holes | upper holes by rank |
|---|---:|---:|---:|---:|---:|
| `k11_positive` | `(4,13,252)` | `(1,14,210)` | `231/231` | `0` | `0` |
| `k11_corefail` | `(4,16,252)` | `(1,19,210)` | `220/231` | `0` | `0` |
| `k15_resident_seed` | `(4,32,3432)` | `(1,44,3003)` | `4778/4943` | `47` | `67,27,1` at ranks `9,10,11` |

For the failing `k11` fixture, the union-Hall shore is the single physical
orbit represented by `25`, of weight `11`, with no active block.  Its
primitive endpoint cut has 462 incumbent-false envelope atoms and requires
one repaired block.

For `k=15`, the union-Hall shore consists exactly of the eleven rank-five
orbits

\[
157,285,651,661,665,837,1187,1233,1349,1585,2329.
\tag{7.1}
\]

All have weight `15`, all have zero active blocks, and (3.5) requires eleven
new blocks.  Hence this Hall cut is exactly the known 165 zero-degree
terminal-target defect; it reveals no additional hidden Hall shore on this
seed.

The 47 missing `q2` quotient orbits have physical weight

\[
 45\cdot15+2\cdot5=685,                                 \tag{7.2}
\]

so stabilizer-aware phases are essential.  For representative `317`, the
primitive prefix cut contains 6435 atoms: 4931 initial-membership repairs and
1504 alpha-prefix repairs.  Its atom-list SHA-256 is

`128e3cec1e3f20a084901646514fbd8f8de76d5547029f2cb696c8f100c97845`.

For the first missing upper orbit, representative `1519`, the primitive
strict-order cut contains 6435 atoms and has SHA-256

`8d8956c5b70709344c7e843b405cb519044cab8fa3afeb5b158101f493eb2210`.

Input SHA-256 values are:

- `k11_positive`: `e02936935a4ac2f460a0a8ac8ca1cc494ea9127485f78b609cb389bebdc0714e`;
- `k11_corefail`: `388dd6e004367f3d52f5e5a5c01cdac0e64521bedc6edd7c878cd5b59ab5112b`;
- `k15_resident_seed`: `4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10`.

## 8. Exact proved/implementation boundary

The current live `c`-space loop already has exact eager lower rows and exact
upper reachability/blocker logic, but an exact compiler failure still falls
back to a complete `c`-assignment no-good.  Theorems 3.1 and Corollary 3.2
give the missing stronger carrier separator whenever the **all-core union**
graph has a deficient shore.  Equation (3.10) is required when the failure
is only for a chosen core.

Passing all union-Hall, lower-`q2`, and upper rows is not sufficient for a
compiler.  The smallest remaining gate is either:

1. install legal omission-state variables and the exact decorated shore row
   (3.10); or
2. derive an all-core dynamic-programming infeasibility certificate whose
   projection supplies a carrier cut.

No carrier-only projection of an arbitrary sampled-core shore has been
proved, and the frozen passing `k11` carrier rules out such a theorem without
additional state.
