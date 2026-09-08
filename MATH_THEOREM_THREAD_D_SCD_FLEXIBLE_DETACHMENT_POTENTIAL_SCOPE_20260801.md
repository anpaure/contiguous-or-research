# Flexible SCD detachment needs a graphic row: the exact monotone subcatalogue and an `m=4` potential no-go

Date: 2026-08-01  
Lane: Thread D, flexible four-row SCD detachment  
Status: exact all-dimensional local potential criterion, exact `m=4`
counterexample to automatic acyclicity, and exact `m=4` no-go for any one
selection-independent strict potential.  No all-dimensional detachment rule
is claimed.

## 0. Outcome

The standard Greene--Kleitman coordinate-sum potential

\[
                         \Phi(X)=\sum_{i\in X}i                 \tag{0.1}
\]

proves acyclicity of the aligned four-row long-ear construction, but it does
**not** prove acyclicity of the flexible phase CNF.

There is an exact positive replacement.  Every flexible option has one of
the coordinate increments listed in Theorem 2.1 below.  If the selected
options use only positive rows from that table, then head injectivity and the
already exact lower-tail row imply a physical linear forest.  In particular,
an all-`m` construction may make topology automatic by staying in this
monotone subcatalogue.

The restriction is genuine.

1. The authenticated `m=4` SAT witness is already an exact upper/lower,
   maximum-in/outdegree-one forest, but it contains two strictly
   `Phi`-decreasing physical arrows.
2. The complete `m=4` phase-CNF census has `2252` capacity-feasible
   selections, of which `7` contain a directed (and undirected) cycle.  Thus
   capacity feasibility does not imply topology even for the standard SCD.
3. More strongly, three complete acyclic `m=4` selections contain,
   respectively, the physical arrows

   \[
      a123\longrightarrow a124,
      \qquad a124\longrightarrow a134,
      \qquad a134\longrightarrow a123.                       \tag{0.2}
   \]

   Hence no single vertex potential, not merely (0.1), can increase on every
   edge of every feasible detachment forest.

Consequently the decoded acyclicity at `m=4,...,8` is a property of those
particular witnesses.  It is not a consequence of the phase CNF or of the
standard SCD order.  An all-dimensional rule must either stay inside the
monotone subcatalogue or retain a selection-dependent graphic/cycle row.

## 1. Fixed matching and notation

Put

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad
 G=[2m-3],\qquad a=2m-2,quad z=2m-1.                \tag{1.1}
\]

On a long Greene--Kleitman chain write

\[
 R\subset S=R+\rho\subset L=S+x\subset U_0=L+y,    \tag{1.2}
\]

where

\[
                         \rho<x<y.                   \tag{1.3}
\]

For a short chain only `S<L=S+x` is present.  The fixed four-row matching is

\[
\begin{array}{c|cc}
\text{root}&\text{long}&\text{short}\\ \hline
azR&azS&-\\
zS&zL&azS\\
aS&aL&aL\\
L&U_0&zL.
\end{array}                                          \tag{1.4}
\]

Orient every physical edge from the owner matched to its selected lower
root.  This is the orientation used by the flexible CNF and by the
outdegree-one forest proof.

## 2. Exact potential increments

### Theorem 2.1 (complete local increment table)

For an `a`-target `aU`, choose a provider facet

\[
                      U=L+q.                         \tag{2.1}
\]

The primary arrow is

\[
                    aL\longrightarrow a(S+q),
                    \qquad \Delta\Phi=q-x.           \tag{2.2}
\]

Its auxiliary arrow is exactly one of

\[
\begin{array}{c|c|c}
\text{provider/phase}&\text{physical arrow}&\Delta\Phi\\ \hline
\text{long, aligned C}&azS\to az(R+x)&x-\rho>0\\
\text{long, reversed D}&zL\to azS&a-x>0\\
\text{short, D}&azS\to zL&x-a<0.
\end{array}                                          \tag{2.3}
\]

For an all-`G` target `W`, choose a long provider `U_0=L+y` and write

\[
                         W=U_0+v.                     \tag{2.4}
\]

The primary arrow is

\[
                     U_0\longrightarrow L+v,
                     \qquad \Delta\Phi=v-y.          \tag{2.5}
\]

Choose the auxiliary deletion `t in L`, put `V=L-t`, and set

\[
                         C=zL,qquad D=z(V+y).         \tag{2.6}
\]

The fixed matching decides the orientation:

\[
\begin{array}{c|c|c}
M_0(zV)&\text{physical arrow}&\Delta\Phi\\ \hline
C&C\to D&y-t\\
D&D\to C&t-y.
\end{array}                                          \tag{2.7}
\]

Every retained seed/provider arrow has positive increment: `z-x` for an
`azL` provider and `z-y` for a `zU_0` provider.

#### Proof

The physical endpoints are read directly from (1.4).  Every row in
(2.2)--(2.7) replaces exactly one coordinate by another.  Subtracting the
coordinate sums gives the displayed increments.  The strict inequalities
in (2.3) use (1.3) and the fact that `a` is larger than every coordinate of
`G`.  The retained-row increments are equally immediate.  \(\square\)

### Corollary 2.2 (monotone flexible-detachment forest)

Suppose a flexible selection has exact lower tails and injective heads, and
also satisfies

1. every `a`-primary choice has `q>x`;
2. no short-chain D provider is used;
3. every all-`G` primary choice has `v>y`; and
4. every auxiliary row (2.7) is oriented from the smaller of `t,y` to the
   larger.

Then its physical support is a linear forest.

#### Proof

Theorem 2.1 makes `Phi` strictly increase along every oriented physical
edge.  Exact lower tails give outdegree at most one and head injectivity
gives indegree at most one.  If an undirected cycle existed, a vertex of
minimum `Phi` on it would have both incident cycle edges directed outward,
contradicting outdegree at most one.  \(\square\)

For the `a` sector, there are exactly

\[
 E={2m-3\choose m-3}                                \tag{2.8}
\]

targets and exactly `E` long providers.  Therefore any monotone solution
uses every long provider once and no short provider.  This turns the first
part of an all-`m` rule into the sharp bipartite problem

\[
 a(L+q)\longleftrightarrow L
 \quad\text{with}\quad q>x(L),                       \tag{2.9}
\]

together with the two head-injection rows.  Corollary 2.2 proves topology
after that matching; it does not prove (2.9) has a solution.

## 3. The authenticated witness already leaves the standard potential

The remote artifact

`/home/amodo/or15/work/root_scd_detachment_20260801/phase_m4.out`

has SHA-256

`182bf5e4690f0c8b625992bbcb98fe01b96edca24cc719ccee4c3c301fe54aff`.

Its positive variables are

\[
                         8,12,20,23,30,37.           \tag{3.1}
\]

Independent reconstruction gives `21` distinct lower and upper colours,
maximum rooted indegree/outdegree one, maximum physical degree two, and no
directed or undirected cycle.  Nevertheless it contains

\[
\begin{aligned}
 \{3,5,a,z\}&\longrightarrow\{1,3,5,z\},
      &\Delta\Phi&=-5,\\
 \{1,3,4,z\}&\longrightarrow\{1,2,3,z\},
      &\Delta\Phi&=-2.                               \tag{3.2}
\end{aligned}
\]

The first is a short D row of (2.3); the second is a reverse-oriented row
of (2.7).  Hence the standard potential is sufficient but not necessary
for an acyclic flexible witness.

## 4. Capacity feasibility does not imply acyclicity

### Theorem 4.1 (literal `m=4` phase-CNF cycle)

The option variables

\[
                         \{2,14,18,22,26,32\}        \tag{4.1}
\]

satisfy every row of the flexible phase CNF: exactly one option per target,
provider capacity one, new-head capacity one, second-tail capacity one, and
every occupied old head is released.  Their completed rooted graph contains
the directed cycle

\[
 38\to35\to49\to56\to44\to38,                       \tag{4.2}
\]

or, on physical owners,

\[
 a234\to a123\to a125\to a145\to a345\to a234.      \tag{4.3}
\]

Thus the phase CNF alone is not a forest formulation.

#### Proof

Substitution of (4.1) into the exact option table checks all capacity and
release rows.  Applying the fixed matching (1.4) to (4.2) gives (4.3).
The cycle is then literal.  \(\square\)

The complete solver-free enumeration of this `m=4` CNF has

\[
             2252\text{ capacity-feasible selections},
             \qquad 7\text{ cyclic selections}.             \tag{4.4}
\]

No claim about the number of cycles for larger `m` is made.

## 5. No common strict potential exists across all feasible forests

### Theorem 5.1 (selection-independent potential obstruction)

There is no function `Psi` on the physical owner vertices which strictly
increases along every edge of every complete acyclic `m=4` flexible
detachment.

#### Proof

The following three complete selections all satisfy the capacity rows and
have no directed or undirected cycle:

\[
\begin{array}{c|c}
\text{selected variables}&\text{distinguished physical arrow}\\ \hline
\{3,9,16,21,27,32\}&a134\to a123\\
\{5,9,15,22,26,32\}&a124\to a134\\
\{7,9,16,24,26,32\}&a123\to a124.
\end{array}                                          \tag{5.1}
\]

If one `Psi` increased along every edge in all three forests, (5.1) would
force

\[
 \Psi(a123)<\Psi(a124)<\Psi(a134)<\Psi(a123),        \tag{5.2}
\]

which is impossible.  \(\square\)

This theorem does not prevent each selected forest from having its own
topological-order potential.  It says precisely that SCD order cannot make
the graphic row disappear uniformly over the flexible menus.

## 6. Audit and remaining gate

The lightweight independent audit is

`scratch/audit_threadD_scd_flexible_detachment_potential_20260801.py`.

It reconstructs the standard `m=4` SCD and fixed matching, recreates all
`38` options, replays the authenticated model, enumerates the complete
capacity CNF without a SAT solver, and emits

`scratch/threadD_scd_flexible_detachment_potential_20260801.audit.json`.

The remote generator source has SHA-256

`16faf809cdb88942df4702874165d9f276e0e6ca182ceada33009ff229931911`.

The proved all-dimensional statement is Corollary 2.2.  The exact remaining
choice is one of:

1. prove the target/provider/head Hall systems inside the monotone
   inequalities (2.9), thereby making topology automatic; or
2. use the full flexible menus and add an explicit graphic-matroid/cycle
   separator.

The finite acyclic witnesses through `m=8` support existence, but they do
not choose between these two routes and are not an all-`m` rule.
