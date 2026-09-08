# The `6c98` exact-add UNSAT: a signed four-colour rainbow core

Later scope correction: both signed clauses below are valid, but
`MATH_AUDIT_AD_K16_R99_6C98_CUT_DOMINANCE_20260729.md` proves that the single
26-node endpoint-cover row strictly dominates their conjunction.  They should
not be installed alongside that row.  The exact 36-new-variable
endpoint-witness block is stronger than all three linear rows.

## 1. Scope and result

This note audits the first delete-branch cut that passed the lifted joint
lower/upper double-repair master,

\[
  \operatorname{sha}_{256}(\operatorname{sort}X)
  =\mathtt{6c98aa96b824b580be70fb9bab617e80fef233b4bf11b33a7a83adce5d9c39b4}.
\]

The frozen exact-add CNF is infeasible, but a full 99-positive-literal
no-good would throw away almost all of the available explanation.  The
conflict already occurs in four upper-`q1` rows and three quotient nodes.  It
has two useful exact projections.

1. A pair of signed cut clauses is valid for every binary source cut, at any
   radius.  One clause rejects `6c98` and all cuts with the same local
   obstruction.
2. The complete four-colour necessary recourse problem has only 199 Boolean
   variables and 37 constraints.  It can be installed directly as a lifted
   master block or used with signed assumptions to learn further clauses.

Neither statement closes the delete branch.  Neither uses the now-redundant
joint-cover row layer.

The solver-free replay is

```text
scratch/audit_ad_k16_r99_6c98_signed_rainbow_core_20260729.py
scratch/ad_k16_r99_6c98_signed_rainbow_core_20260729.audit.json
```

At the time of this audit their SHA-256 digests are, respectively,

```text
22e62a1982e5d521511b215cb0ecb7b1f2309a2496a49a9589284be4dca2f083
131315118275c20f457cfb5fdc64a1cf1bc955c8fddb955e00edc1cf8ee5e1b9
```

## 2. Exact provider data

Let `S` be the fixed loopless quotient 2-factor and let `x_e=1` mean that
the source edge `e` is deleted.  Put

\[
 d_x(v)=\sum_{e\in S:\ v\in\partial e}x_e.
\]

The following four upper colours have unique providers in `S`:

| role | upper colour | unique source provider | source endpoints |
|---|---:|---:|---:|
| `A` | `(1,1883)` | `4742` | `92,499` |
| `B` | `(1,1907)` | `22511` | `611,617` |
| `C` | `(1,3255)` | `23229` | `638,754` |
| `D` | `(1,5939)` | `24034` | `663,739` |

For each colour its complete catalogue provider graph is a `K_9`.  Exactly
one of its 36 edges is the displayed source edge, leaving 35 eligible
off-source providers.  The four nine-node sets are

\[
\begin{aligned}
V_A={}&\{92,485,499,541,576,606,615,617,619\},\\
V_B={}&\{97,490,502,546,581,611,617,620,623\},\\
V_C={}&\{208,521,576,600,638,751,754,757,758\},\\
V_D={}&\{403,611,663,667,739,759,761,832,852\}.
\end{aligned}
\]

At `6c98`, intersecting those cliques with positive cut-degree nodes leaves
the exact off-source provider lists

\[
\begin{aligned}
E_A(X)&=\{4737,4740,18552,18555,21385\},\\
E_B(X)&=\{18171,18172\},\\
E_C(X)&=\{21408,21411\},\\
E_D(X)&=\{22529,22530\}.
\end{aligned}
\]

The relevant endpoint descriptions are

\[
\begin{array}{c|l}
A&(92,576),(92,617),(499,576),(499,617),(576,617)\\
B&(490,611),(490,617)\\
C&(576,638),(576,754)\\
D&(611,663),(611,739).
\end{array}
\]

Moreover

\[
 d_X(576)=d_X(611)=d_X(617)=1.                 \tag{2.1}
\]

## 3. The fixed four-row obstruction

### Theorem 3.1 (three-hub forcing chain)

There is no exact degree-restoring addition set for `6c98` that covers the
four upper colours `A,B,C,D`.

### Proof

Because the source provider of `C` is deleted and cannot be re-added, every
available `C` provider consumes node `576`.  Similarly every available `D`
provider consumes `611`.  By (2.1), those two capacities are exhausted.

Every available `B` provider consumes either `611` or `617`.  It cannot use
the already exhausted node `611`, so it consumes `617`.  Every available `A`
provider consumes `576` or `617`, both of which are now exhausted.  This is
impossible.  ∎

This proof is independent of the SAT transcript.  The audit also checks all
`5*2*2*2=40` rainbow choices literally and finds none.  If any one of the
four colours is omitted, a local capacity-feasible rainbow exists, so this
four-colour obstruction is deletion-minimal as a local rainbow obstruction.
That does not assert minimum cardinality among every possible full-CNF core.

## 4. A signed cut projection

Define the 23 outside provider nodes

\[
\begin{split}
O=\{&97,208,403,485,502,521,541,546,581,600,606,615,619,\\
    &620,623,667,751,757,758,759,761,832,852\}.
\end{split}
\]

The two source edges at node `576` are

\[
 f=18158,\qquad g=21391.                         \tag{4.1}
\]

The second source incidences at `611` and `617`, besides the common source
provider `22511`, are `22520` and `22692`.  Let

\[
 N_0=\{e\in S:\partial e\cap O\ne\varnothing\}
       \mathbin{\cup}\{22520,22692\}.             \tag{4.2}
\]

The replay verifies

\[
 |\{e\in S:\partial e\cap O\ne\varnothing\}|=44,
 \qquad |N_0|=46,                                \tag{4.3}
\]

and that `N_0`, `{f,g}`, and the four source providers have the required
disjointness.  The exact list of all 46 edges is stored in the audit JSON.

### Theorem 4.1 (signed rainbow-core clauses)

Every binary source cut that has a degree-restoring both-`q1` completion
satisfies both inequalities

\[
\begin{aligned}
x_{4742}+x_{22511}+x_{23229}+x_{24034}
 -\sum_{e\in N_0}x_e-x_f&\le 3,                 \tag{4.4}\
x_{4742}+x_{22511}+x_{23229}+x_{24034}
 -\sum_{e\in N_0}x_e-x_g&\le 3.                 \tag{4.5}
\end{aligned}
\]

### Proof

It is enough to consider the case in which all four positive terms equal
one and every member of `N_0` is zero; otherwise each inequality is
automatic.

All nodes of `O` then have cut degree zero.  Since `22511` is cut and the
other source incidences `22520,22692` are not, nodes `611,617` each have cut
degree exactly one.  Therefore the provider graphs reduce to the forcing
pattern in Theorem 3.1 unless node `576` has cut degree two.  The source is a
loopless 2-factor and its two incidences at `576` are exactly `f,g`, so cut
degree two is equivalent to `x_f=x_g=1`.  Thus feasibility forces both
negative literals in (4.4)--(4.5), proving the two clauses.  ∎

For `6c98`, the four positive literals and `f` equal one, while `g` and all
of `N_0` equal zero.  Hence (4.4) is tight and (4.5) has left side four,
violating its right side three.

The useful learned row is therefore a signed 51-literal clause, not a
99-positive-literal assignment no-good.  It rejects every cut that loses the
same four colours while omitting all 47 certified escape incidences in
`N_0 union {g}`.  No claim is made that this clause is globally prime: some
individual escape literals may still fail to repair the complete problem.

## 5. Exact compact four-colour recourse blocks

The clauses above retain only the visible forcing-chain consequence.  The
strongest exact projection of this *four-colour node-capacity relaxation* is
obtained from the following small lifted system.

For every off-source provider edge `a` of one of `A,B,C,D`, introduce a
binary witness `z_a`.  For each colour `c`, let `s_c` be its unique source
provider and `E_c` its 35 off-source provider edges.  Impose

\[
 \sum_{a\in E_c}z_a=x_{s_c}
       \quad(c=A,B,C,D),                          \tag{5.1}
\]

and, for every node in `V_A union V_B union V_C union V_D`,

\[
 \sum_{a:\ v\in\partial a}z_a
 \le d_x(v).                                     \tag{5.2}
\]

This edge-witness form has exactly

```text
59 relevant source-cut variables
140 provider-witness variables
4 colour equalities
33 node-capacity inequalities
199 variables and 37 constraints in total.
```

### Theorem 5.1 (necessity and exact local semantics)

Every full exact degree-restoring both-`q1` completion projects to a feasible
solution of (5.1)--(5.2).  Conversely, (5.1)--(5.2) is exactly the existence
condition for one node-capacity-feasible provider witness for each lost
colour among these four.  It makes no assertion about the other 1,524
quotient `q1` rows.

### Proof

If `x_{s_c}=0`, set all witnesses of colour `c` to zero.  If `x_{s_c}=1`,
the unique source provider is absent, so full upper-`q1` coverage supplies at
least one selected off-source provider; choose one and set its witness to
one.  Different upper colours have disjoint provider-edge sets.  The chosen
witness incidence at every node is no greater than the incidence of all
added edges there, which exact degree restoration makes equal to `d_x(v)`.
This proves necessity.  The reverse statement is simply the literal meaning
of the binary variables and (5.1)--(5.2).  ∎

### 5.1 Endpoint compression using the four `K_9` identities

The audited clique structure gives a smaller exact formulation.  Introduce
`u_(c,v)` for `c in {A,B,C,D}` and `v in V_c`; it means that `v` is one
endpoint of the chosen provider for colour `c`.  If the source provider
`s_c` has endpoints `a_c,b_c`, impose

\[
\begin{aligned}
 \sum_{v\in V_c}u_{c,v}&=2x_{s_c},              &&(c=A,B,C,D),\tag{5.3}\\
 u_{c,a_c}+u_{c,b_c}&\le x_{s_c},               &&(c=A,B,C,D),\tag{5.4}\\
 \sum_{c:\ v\in V_c}u_{c,v}&\le d_x(v),        &&(v\in\bigcup_cV_c).\tag{5.5}
\end{aligned}
\]

When `x_(s_c)=1`, (5.3) chooses two distinct nodes of `V_c`; (5.4) forbids
the one pair equal to the deleted source edge.  Every other pair is the
endpoint pair of exactly one eligible off-source provider because the
provider graph is `K_9`.  Thus (5.3)--(5.5) is equivalent to
(5.1)--(5.2), not a relaxation of it.

Its exact census is

```text
59 relevant source-cut variables
36 colour-endpoint witness variables
4 colour-cardinality equalities
4 deleted-source-pair inequalities
33 node-capacity inequalities
95 variables and 41 constraints in total.
```

Only the 36 witness variables are new when the block is placed in the
existing cut master.

This block is not implied by the current double-repair matching master.  The
double-repair variables certify only enough seams that simultaneously repair
one lower and one upper unique colour; they do not assign a provider to each
of these four upper colours.  Thus this is a genuine next recourse layer,
whereas re-adding joint-cover inequalities already implied by the lifted
double-repair master is not.

## 6. Exact implementation choices

### 6.1 Recommended eager block

Add the 36 `u_(c,v)` variables and the 41 rows (5.3)--(5.5) directly to the
cut master.  This is smaller and stronger than adding only (4.4)--(4.5), and
it requires no auxiliary solve.  It preserves every cut having a full exact
add completion by Theorem 5.1 and the exact endpoint compression above.

An edge-witness implementation must use all 35 off-source provider edges per
colour, not only the 11 providers usable at `6c98`.  The endpoint form must
likewise use all nine nodes in every displayed `V_c`.  Restricting either
form to the frozen positive-degree support would be an unsound
generalization.

### 6.2 Signed-assumption local Benders

If keeping the master smaller is preferred, build the uniform 95-variable
endpoint model once.  For a candidate cut, guard each of its 59 relevant cut
variables by its actual signed literal:

```text
x_e     when e is cut,
not x_e when e is retained.
```

On infeasibility, replay and shrink the returned sufficient assumption core.
If the replayed core has positive set `P` and negative set `N`, learn

\[
  \sum_{e\in P}x_e-\sum_{e\in N}x_e\le |P|-1.    \tag{6.1}
\]

Indeed, (6.1) is just the clause saying that at least one core literal must
change.  A negative OR-Tools Boolean literal with internal reference `j` is
encoded by the negated reference `-j-1`; the assumption registry must map
both signs explicitly.  Every learned core must be exported and replayed
with exactly its signed assumptions before (6.1) is admitted.

The current positive-only assumption scheme cannot expose this local core
compactly.  With the radius equation, 99 positive assumptions fix the entire
candidate, but after shrinking a small positive subset the 47 escape edges
are free to turn on.  Signed assumptions are what retain the meaningful
absence conditions.

### 6.3 Full-subproblem signed cores

The same signed-core translation is sound for the complete add subproblem:
guard every source cut bit by its candidate value, extract a sufficient
signed core, replay it, and add (6.1).  That may discover conflicts beyond
the four-colour block.  The compact block is preferable as the first
regression because its semantics and universal necessity have a direct
proof, and because a failure is expected to presolve without materializing
all 26,570 add variables.

An empty replayed assumption core would mean the unguarded branch subproblem
itself is infeasible and would close the branch.  It must not be serialized
as an ordinary row with right side `-1` without an explicit branch-closure
status.

## 7. Exact proved boundary

Proved here:

1. the four fixed upper rows plus degree capacity already contradict `6c98`;
2. the contradiction has the explicit forcing chain of Theorem 3.1;
3. the two signed inequalities (4.4)--(4.5) are valid for every binary source
   cut in the off-source replacement model;
4. (4.5) rejects `6c98`;
5. the 199-variable system (5.1)--(5.2) is an exact four-colour provider-
   witness model, its 95-variable endpoint compression (5.3)--(5.5) is
   exact, and both are necessary projections of every full completion.

Not proved here:

1. infeasibility of every radius-99 delete-branch cut;
2. sufficiency of the four-colour local model for either palette;
3. primeness or minimum support of the signed clauses;
4. connectivity, voltage one, dynamic residence, or any deeper shadow gate.
