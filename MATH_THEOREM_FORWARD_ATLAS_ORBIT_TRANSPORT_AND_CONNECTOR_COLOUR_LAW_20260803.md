# Exact orbit transportation for the forward atlas, and the connector-colour law

**Date:** 2026-08-03  
**Scope:** pure all-parameter mathematics for the fixed rooted Boolean occurrence
ground.  No finite candidate calculation is used.  The positive results below
do not assert that the final physical colour--tail--head matching exists.

## 0. Outcome

Fix `m>=2`, `n=2m-1`, a perfect incidence matching

\[
 M_0:{[n]\choose m-1}\longrightarrow {[n]\choose m},
\]

a protected directed pivot forest `P`, its designated root `rho`, and a strict
total order `phi` extending `P`.  For a nonmatching incidence `e=LV`, put

\[
 t(e)=L,\qquad h(e)=M_0^{-1}(V),\qquad
 u(e)=M_0(L)\cup V.
\]

The exact conclusions are as follows.

1. The stabilizer of `(M_0,phi,P,rho)` on the rooted occurrence ground is
   trivial.  Moreover, an endpoint-near-perfect selection in a fixed strict
   forward atlas is forced to be the consecutive Hamilton path in `phi`.
   Consequently that atlas has neither a nontrivial coordinate-orbit
   compression nor a positive-density path-selection problem.
2. A nontrivial group can preserve a tied potential or an orbit DAG, but an
   invariant DAG has no directed path within one vertex orbit.  In particular,
   the vertices of every protected directed path lie in distinct orbits, and
   upper-colour availability must be reproved after ties are introduced.
3. Orbit averaging is exact for the invariant *fractional* problem.  Integral
   orbit totals lift only when the corresponding literal zero-one fibre is
   integral.  Complete Cartesian fibres and the private-tail/private-head Hall
   faces give exact positive lift theorems.
4. Symmetry and biregularity alone do not give an integral lift.  There are
   loopless, diagonal-action examples for every even order in which all orbit
   totals and all literal fractional marginals are integral/feasible, while a
   modular cocycle forbids every literal matching.
5. In the actual Boolean rooted ground, every desired near-perfect path has an
   exact integer connector-colour degree vector.  If `tau` is its omitted tail,
   `rho` its omitted head, and `a(tau)` is the unique coordinate in
   `M_0(tau)-tau`, then its `Cat_m-1` repeated colours obey

   \[
    \sum_R s_R {\bf1}_R
      =2\operatorname {Cat}_{m-1}{\bf1}
       -{\bf e}_{a(\tau)}-{\bf1}_{M_0(\rho)}.       \tag{0.1}
   \]

   This colour-coordinate layer has a bounded-multiplicity multiset solution
   for every `m>=3` and every `(tau,rho)`; it fails for `m=2` exactly when
   `a(tau) in M_0(rho)`.  Physical endpoints, forward occurrence multiplicity,
   and the fixed pivot remain separate constraints.

## 1. The strict-order stabilizer is trivial

Let `G` be any group of automorphisms of the rooted occurrence ground which
preserves `M_0`, the strict order `phi`, the protected bank, and the designated
root.  Preservation of `phi` means

\[
 \phi(L)<\phi(K)\quad\Longleftrightarrow\quad
 \phi(gL)<\phi(gK).
\]

### Theorem 1.1 (strict-order collapse)

For every `m>=2`, `G` is trivial on rooted vertices and occurrences.  If `G`
comes from coordinate permutations, it is trivial on `[2m-1]` as well.

#### Proof

A finite strict linear order has no nonidentity order automorphism.  Hence every
`g in G` fixes every lower vertex `L`.  The ordered endpoint pair determines a
rooted occurrence: an arc from `L` to `H`, when present, is the unique incidence
`L M_0(H)`.  Thus every occurrence is fixed.

For a coordinate action, the action on the nontrivial layer
`{[2m-1]\choose m-1}` is faithful.  Indeed, for any two distinct coordinates
there is an `(m-1)`-set containing one and not the other.  A coordinate
permutation fixing every such set is therefore the identity.  \(\square\)

Conjugating `phi` by a coordinate permutation produces an isomorphic but
different forward instance.  It does not produce a quotient symmetry of the
fixed instance.

There is also no fully symmetric choice of the root matching.

### Proposition 1.2 (no full-coordinate equivariant root matching)

For `m>=2`, no incidence matching `M_0` is equivariant under all of
`S_{2m-1}`.

#### Proof

Write `M_0(L)=L union {a(L)}`.  The stabilizer of one fixed `(m-1)`-set `L`
contains the full symmetric group on its `m`-element complement.  Equivariance
would force `a(L)` to be fixed by this transitive action, which is impossible.
\(\square\)

Thus even before imposing `phi`, a chosen `M_0` breaks full coordinate
symmetry; the strict order removes every surviving vertex symmetry.

## 2. What a symmetry-preserving DAG would require

### Lemma 2.1 (no invariant reachability inside an orbit)

Let a finite group `G` act on a finite directed acyclic graph `D`.  If `x` and
`y` lie in one `G`-orbit, there is no directed path from `x` to `y` unless
`x=y`.

#### Proof

Suppose that a directed path joins `x` to `gx`.  Translate it successively by
`g`.  Since `g` has finite order on `x`, concatenating the translated paths
gives a directed closed walk, and hence a directed cycle.  The same argument
applies when `y=gx`.  \(\square\)

Consequently a `G`-invariant DAG has no arc inside a vertex orbit and descends
to a DAG on vertex orbits.  Every directed protected path has all its vertices
in distinct orbits.  Its designated first vertex makes that path pointwise
fixed under every bank automorphism.

A `G`-invariant weak potential is constant on each vertex orbit.  Keeping only
strictly increasing arcs is therefore possible, but Theorem 3.1 of the forward
atlas note no longer proves upper-colour surjectivity: the functional cycle of
one colour may be contained entirely in tied levels.  Exact availability must
be established for every colour orbit in the new orbit DAG.

## 3. Exact fractional quotient and the literal integral fibre

After fixing `P`, delete its occupied tail and head resources and give every
remaining literal occurrence a variable `x_e`.  The residual system consists
of tail capacities, exact residual head demands, lower bounds for colours not
already covered by `P`, and the exact cardinality `W-1-|P|`.

Suppose for this section that a finite group `G` preserves all of these data.
Let `Omega` be an edge orbit and `A` a tail, head, or colour orbit.  For a
representative `v in A`, define

\[
 d^s_{A,\Omega}=
 |\{e\in\Omega:s(e)=v\}|,
 \qquad s\in\{t,h,u\}.                              \tag{3.1}
\]

This is independent of the representative.

### Theorem 3.1 (exact invariant fractional quotient)

The residual literal LP is feasible if and only if it has a `G`-invariant
feasible point.  Such a point is exactly described by values
`z_Omega in [0,1]`, one per edge orbit, with literal-orbit loads

\[
 \sum_\Omega d^s_{A,\Omega}z_\Omega               \tag{3.2}
\]

and total size `sum_Omega |Omega|z_Omega`.

#### Proof

Average an arbitrary feasible point over `G`.  All right-hand sides and all
resource families are invariant, so feasibility is preserved.  The average is
constant on every edge orbit.  Conversely, assigning `x_e=z_Omega` for
`e in Omega` gives the stated literal loads.  \(\square\)

An integer aggregate `n_Omega=|Omega|z_Omega` is not an invariant integral
selection unless `n_Omega` is either zero or `|Omega|`.  It records only how
many orbit members should be used.

Let `A` be the complete literal resource-incidence matrix, with slack variables
inserted for inequalities, and let `B` be the edge-orbit sum matrix.  For fixed
integer orbit totals `n`, the exact lift question is

\[
 \{x\in\{0,1\}^{E}: Ax=b,\ Bx=n\}\ne\varnothing.   \tag{3.3}
\]

Thus an orbit flow lifts precisely when its zero-one fibre (3.3) is nonempty.
Biregularity proves the fractional spreading in Theorem 3.1; it does not prove
(3.3).  Total unimodularity of the augmented equality/slack matrix is a clean
sufficient condition for every integral feasible right-hand side to lift.  In
the standard all-right-hand-sides formulation it is exactly the usual
Hoffman--Kruskal integrality gate.

For an algebraic exact test, adjoin complement variables
`x_e+bar x_e=1`.  The lift is membership of the augmented right-hand side in
the affine semigroup generated by the resulting columns.  If that semigroup is
normal, cone feasibility plus its Smith-lattice congruences is sufficient.  In
the absence of normality, even those two tests may leave semigroup holes.

## 4. Two exact positive lift faces

### Theorem 4.1 (Cartesian-fibre lift)

Partition literal colours, tails, and heads into blocks `C_a,T_i,H_j`.
Suppose every allowed quotient cell is the complete Cartesian product

\[
                         C_a\times T_i\times H_j.    \tag{4.1}
\]

Let nonnegative integer cell counts `q_aij` satisfy all tail and head block
capacities.  Suppose also that

\[
                  \sum_{i,j}q_{aij}\ge r_a|C_a|,   \tag{4.2}
\]

where every literal colour in `C_a` is required at least `r_a` times.  Then
the cell counts have a literal lift.

#### Proof

For each tail block, partition the required number of distinct literal tails
among its incident cells.  Do the same independently in every head block.
Within each cell, biject the assigned tail set to the assigned head set.  For
fixed `a`, label at least `r_a|C_a|` of the resulting endpoint pairs so that
each colour of `C_a` occurs at least `r_a` times; label any surplus pairs
arbitrarily.  Completeness of (4.1) makes every labelled triple legal.  All
literal endpoint capacities hold by construction.  \(\square\)

The Boolean occurrence ground is not Cartesian: for an allowed ordered
endpoint pair `(L,H)`, its colour is the single value
`M_0(L) union M_0(H)`.  Theorem 4.1 therefore cannot be invoked without an
additional fibre-completeness argument.

### Theorem 4.2 (private-resource orbit Hall theorem)

Let `K` be a set of required colour tasks, each owning a distinct private tail,
and let `H` be the available literal heads.  Suppose `K` and `H` are partitioned
into orbits `K_i,H_j`, and every allowed orbit block is either empty or the
complete bipartite graph `K_i times H_j`.  Then a literal matching of all tasks
to distinct heads exists if and only if

\[
 \sum_{i\in I}|K_i|
   \le \sum_{j\in N(I)}|H_j|
 \qquad\hbox{for every set of task orbits }I.       \tag{4.3}
\]

Every integral quotient transportation satisfying the corresponding block
margins lifts.

#### Proof

For a literal task subset `S`, its neighbourhood is the union of the complete
head blocks adjacent to the task orbits met by `S`.  The worst subset meeting
a fixed collection `I` is therefore `union_{i in I}K_i`.  Literal Hall reduces
exactly to (4.3).

Equivalently, an integral quotient max flow gives block counts `f_ij`.  Partition
each `K_i` and `H_j` according to these counts and pair the assigned atoms
inside each complete block.  \(\square\)

The head-private statement is symmetric.  This is the exact network/min-cut
regime.  Without private resources or Cartesian fibres, the problem remains a
three-index correlation rather than a flow.

## 5. Exact obstruction outside the flow regime

The smallest obstruction has colours, tails, and heads indexed by `F_2`, with
four triples satisfying `c=t+h`:

\[
 000,\quad 011,\quad 101,\quad 110.                 \tag{5.1}
\]

Putting weight `1/2` on every triple gives load one on every literal resource.
There is no integral pair covering both colours and both endpoint shores: the
two same-colour pairs are the two endpoint-perfect matchings, while every
mixed-colour pair shares a tail or a head.

With columns ordered as in (5.1), the rows `(c_0,t_0,h_0,total)` form

\[
 \begin{pmatrix}
  1&1&0&0\\
  1&0&1&0\\
  1&0&0&1\\
  1&1&1&1
 \end{pmatrix},                                     \tag{5.2}
\]

whose determinant has absolute value two.  For right-hand side `(1,1,1,2)`,
the unique fractional solution is `(1/2,1/2,1/2,1/2)`.  Modulo two, every
allowed triple obeys `c+t+h=0`; the requested marginals violate the summed
identity.  Notice that for each single colour the available endpoint graph has
matching rank two, and the union of both colours also has rank two.  Hence all
natural colour-subset matching-rank inequalities pass.

There is an infinite loopless version respecting one diagonal action on the
tail/head vertex set.

### Theorem 5.1 (loopless diagonal cocycle obstruction)

For every even `n>=4`, let the common endpoint set be `Z_n`.  Keep only arcs

\[
                         t\longrightarrow t+1,
 \qquad                   t\longrightarrow t+2,    \tag{5.3}
\]

and colour an arc `t->h` by `c=t+h mod n`.  Diagonal translation by `a`
sends endpoints to `+a` and colours to `c+2a`, so it preserves the ground.

The two edge-orbit totals `n/2,n/2` satisfy every orbit margin.  Their uniform
literal expansion, weight `1/2` on every arc, gives tail and head load one and
colour load one.  Nevertheless no integral endpoint-perfect selection uses
every colour once.

#### Proof

Every colour has exactly two arcs in (5.3), in the difference class having the
same parity as the colour, so the half-weight assertion follows.  An integral
selection would be a permutation `pi` of `Z_n`, and colour exactness would give

\[
 \sum_{t\in Z_n}(t+\pi(t))=\sum_{c\in Z_n}c.        \tag{5.4}
\]

The left side is twice `sum Z_n`, hence zero modulo `n`.  For even `n`, the
right side is `n/2`, a contradiction.  \(\square\)

Thus no theorem based only on orbit balance, transitivity, biregularity, or
ordinary Hall cuts can supply a literal lift.  The missing datum is a lattice
character (and, in general, possibly a semigroup hole).

## 6. The exact Boolean connector-colour degree law

For a lower vertex `L`, write

\[
                         M_0(L)=L\cup\{a(L)\}.       \tag{6.1}
\]

Let `Q` be any rooted occurrence set with `W-1` distinct tails and heads,
omitting tail `tau` and head `rho`, and covering every upper colour.  Write its
colour multiplicities as

\[
                         q_R=1+s_R,
 \qquad s_R\ge0,
 \qquad \sum_Rs_R=\operatorname {Cat}_m-1.          \tag{6.2}
\]

No acyclicity or forward-order assumption is needed for the next identity.

### Theorem 6.1 (connector-colour law)

The extra colour multiset in (6.2) satisfies (0.1):

\[
 \boxed{
 \sum_Rs_R{\bf1}_R
   =2\operatorname {Cat}_{m-1}{\bf1}
      -{\bf e}_{a(\tau)}-{\bf1}_{M_0(\rho)}.}
                                                               \tag{6.3}
\]

#### Proof

For one occurrence `e`, put `L=t(e)`, `H=h(e)`, `T=M_0(L)`, and
`V=M_0(H)`.  Since `L subset T cap V`, both `T,V` have size `m`, and the
occurrence is not a matching edge, `T cap V=L`.  Therefore, over the integers,

\[
 {\bf1}_{u(e)}={\bf1}_T+{\bf1}_V-{\bf1}_L.          \tag{6.4}
\]

Let

\[
 A={2m-2\choose m-1},\qquad B={2m-2\choose m-2}.
\]

Across all owners, every coordinate occurs `A` times; across all lower
vertices, every coordinate occurs `B` times.  Summing (6.4) over `Q`, whose
used tails are all vertices except `tau` and whose used heads are all vertices
except `rho`, gives

\[
 \sum_{e\in Q}{\bf1}_{u(e)}
   =(2A-B){\bf1}
       -{\bf1}_{M_0(\tau)}-{\bf1}_{M_0(\rho)}
       +{\bf1}_\tau
   =(2A-B){\bf1}-{\bf e}_{a(\tau)}
       -{\bf1}_{M_0(\rho)}.                         \tag{6.5}
\]

One copy of every upper colour has coordinate degree `B`, because
`{2m-2\choose m}=B`.  Subtract this mandatory layer from (6.5).  Finally,

\[
 A-B={1\over m}{2m-2\choose m-1}
     =\operatorname {Cat}_{m-1},                    \tag{6.6}
\]

which proves (6.3).  \(\square\)

Modulo two, (6.3) becomes the exact residue

\[
 \sum_R(s_R\bmod2){\bf1}_R
   ={\bf e}_{a(\tau)}+{\bf1}_{M_0(\rho)}.           \tag{6.7}
\]

Thus an endpoint-neutral absorber cannot change this residue.  Moving the
terminal from `tau` to `tau'` changes it by
`e_{a(tau)}+e_{a(tau')}`.

The protected bank does not alter (6.3).  For a residual construction after
fixing `P`, simply subtract `sum_{e in P}{\bf1}_{u(e)}` from (6.5).

There is a useful matrix form of the same conservation law.  Let
`mathsf T,mathsf H` be the literal tail and head incidence matrices.  Let
`mathsf O` be the matrix whose column at `L` is `1_{M_0(L)}`, let `mathsf L`
have column `1_L`, and let `mathsf U` have occurrence column `1_{u(e)}`.
Equation (6.4) is the exact factorization

\[
 \mathsf U=(\mathsf O-\mathsf L)\mathsf T
              +\mathsf O\mathsf H.                 \tag{6.8}
\]

### Corollary 6.2 (endpoint-neutral trades are coordinate-neutral)

For every signed literal trade `z`,

\[
 \mathsf Tz=\mathsf Hz=0\quad\Longrightarrow\quad
 \mathsf Uz=0.                                      \tag{6.9}
\]

More generally its colour-coordinate boundary is exactly

\[
 \mathsf Uz=(\mathsf O-\mathsf L)(\mathsf Tz)
                 +\mathsf O(\mathsf Hz).            \tag{6.10}
\]

Thus an endpoint-neutral pull absorber may redistribute colour identities only
inside the kernel of the upper-colour coordinate-incidence map.  It cannot
repair a coordinate-degree defect.  Any such repair must be paid for by an
explicit tail or head boundary change; moving the terminal in (6.3) is the
global example.

### Corollary 6.3 (the Hamilton-cycle deletion law)

If an upper-surjective rooted Hamilton cycle has colour multiplicities
`1+s_R^circ`, then its `Cat_m` extra colours are exactly coordinate-regular:

\[
             \sum_Rs_R^{\rm circ}{\bf1}_R
                =2\operatorname {Cat}_{m-1}{\bf1}. \tag{6.11}
\]

Delete a nonrepresentative cycle arc `e_*:tau->rho`.  The remaining directed
Hamilton path still covers every colour, and its connector-colour vector is

\[
 2\operatorname {Cat}_{m-1}{\bf1}-{\bf1}_{u(e_*)}
 =2\operatorname {Cat}_{m-1}{\bf1}
      -{\bf e}_{a(\tau)}-{\bf1}_{M_0(\rho)}.        \tag{6.12}
\]

Thus the safe-duplicate edge in the Hamilton-cycle route pays exactly the two
boundary deficits in (6.3), with no hidden colour-coordinate discrepancy.

## 7. Exact feasibility of the unrestricted colour layer

Equation (6.3) prescribes a multiset of `b=Cat_m-1` blocks of size
`k=m+1` on `v=2m-1` coordinates.  Put

\[
 D=2\operatorname {Cat}_{m-1}.
\]

The desired degrees are `D`, except for a deficit on every coordinate of
`M_0(rho)` and one more deficit at `a(tau)`.  The double deficit occurs when
`a(tau) in M_0(rho)`.

### Theorem 7.1 (bounded-multiplicity colour-layer realization)

For every `m>=3` and every `(tau,rho)`, the degree vector in (6.3) is realized
by a multiset of `(m+1)`-subsets in which no block has multiplicity greater
than two.  If `a(tau) notin M_0(rho)`, the realization may be chosen simple.

For `m=2`, it is realizable if and only if
`a(tau) notin M_0(rho)`.

#### Proof

First observe

\[
                         bk=vD-k,                   \tag{7.1}
\]

which is the sum of the degrees in (6.3).  For `m>=3`, one also has

\[
 b\le {v\choose k},\qquad D\le b,                  \tag{7.2}
\]

with equality in the second inequality at `m=3` and strict inequality
afterward.

Among all simple `k`-uniform hypergraphs on `v` vertices with `b` edges,
choose one minimizing the sum of squared degrees.  If `d_x>=d_y+2`, then
there is an edge `E` containing `x` and not `y` for which
`E-x+y` is absent.  Otherwise the switch map would inject all selected
`x`-not-`y` edges into selected `y`-not-`x` edges, contradicting
`d_x>d_y`.  Performing the switch lowers the squared-degree sum.  Hence all
degrees differ by at most one.

By (7.1), this almost-regular hypergraph has degree `D-1` on exactly `k`
vertices and degree `D` on the other `v-k` vertices.  Relabel its low vertices
as `M_0(rho) union {a(tau)}` when `a(tau)` is outside the root owner.  This is
the required simple realization.

Now suppose `a=a(tau) in M_0(rho)`, and choose a coordinate
`z notin M_0(rho)`.  Start with an almost-regular hypergraph whose low set is
`M_0(rho) union {z}`.  There are two non-twin low vertices: if all `k` low
vertices were twins, every `k`-edge would contain all of them, because only
`v-k=m-2<k` high vertices exist, forcing `b<=1`; but `b>=4` for `m>=3`.
Relabel a non-twin pair as `a,z`.  Their degrees are equal, so some selected
edge contains `a` and not `z`.  Replace it by `E-a+z`.  If the new block was
already present, retain it with multiplicity two.  The degrees become `D-2`
at `a`, `D-1` at the other root-owner coordinates, and `D` elsewhere, exactly
as required.

For `m=2`, there is one repeated block, namely the full three-set.  In the
outside case (6.3) is `(1,1,1)` and is realized.  In the inside case one
coordinate has required degree two although only one block is available, so
it is impossible.  \(\square\)

Each literal upper colour has exactly `m+1` rooted occurrences.  Theorem 7.1
keeps the mandatory-plus-extra colour multiplicity at most three for `m>=3`,
so raw colour-family cardinality is not the obstruction.  It does **not** show
that the required copies have enough forward occurrences, nor that their tails
and heads can be packed with the pivot.

## 8. The exact absorber lattice gate

Fix the omitted endpoints and let `D` be the tail/head incidence matrix and
`C` the colour-count matrix.  Differences of two endpoint-feasible selections
lie in `ker_Z D`; their colour-profile differences lie in

\[
                         \mathcal L=C(\ker_{\mathbb Z}D).       \tag{8.1}
\]

Every endpoint-neutral pull absorber contributes one vector of this lattice.
An absorber bank can repair all quotient residues only if the lattice generated
by its trades contains every required class in the relevant cokernel.  Smith
normal form detects the finite character obstructions.  Graphic rank alone
does not address (8.1).

For the four-edge parity tensor, `ker_Z D` is generated by
`(1,1,-1,-1)`, whose colour change is `(2,-2)`.  Thus endpoint-neutral
absorbers change the two colour counts only by an even amount, exactly the
mod-two obstruction in Section 5.

For the Boolean atlas, (6.3) gives the corresponding global residue before any
local absorber grammar is chosen.  A proof-safe absorber theorem must preserve
that identity for fixed terminal, or explicitly transport the terminal and the
resulting `a(tau)` term.

## 9. Exact boundary of the progress

The following rows are closed uniformly in `m`:

* the fixed strict-order stabilizer and the impossibility of a nontrivial
  orbit quotient of that exact forward instance;
* invariant fractional quotienting and the literal zero-one fibre that an
  integral orbit flow must solve;
* exact integral lifting on Cartesian and private-resource network faces;
* an infinite loopless diagonal cocycle obstruction outside those faces;
* the integer connector-colour degree law and its bounded-multiplicity abstract
  colour-layer realization.

The remaining theorem is still physical.  One must find a Hamilton order in
the full rooted atlas whose consecutive literal occurrences realize the
prescribed colour copies, simultaneously respect all protected tails and
heads, obtain the unique root and some legal terminal, and satisfy the literal
endpoint fibre.  Equivalently, one may first solve the full-atlas partial
permutation and then remove its cycles.  Neither orbit balance,
graphic-matroid rank, the colour multiset of Theorem 7.1, nor an unverified
absorber grammar proves that final step.
