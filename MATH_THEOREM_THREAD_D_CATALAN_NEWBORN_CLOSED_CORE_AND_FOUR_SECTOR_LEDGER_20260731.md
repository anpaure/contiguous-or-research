# Strict DERF newborn reserve: closed stopping cores and the exact four-sector credit ledger

Date: 2026-07-31  
Status: dimension-uniform compression theorem and exact finite audit.  The
remaining inequality on compressed cores is isolated.  No all-parameter
absorption theorem is claimed.

## 0. Result

Fix one shore of a strict DERF output at parameter `m`.  Retain the notation
of the absorbing-newborn theorem:

* `G=(O,X)` is the direct occurrence multigraph;
* `I` is the inherited path bank, with endpoint blocks `{a_i,b_i}`;
* `Z_B` is the selected newborn terminal bank;
* `e(H)=kappa_I(H)+|Z_B cap H|` and `rho(H)=|H|-e(H)`; and
* `Gamma(H)` is the **simple** outer neighbourhood of `H`.

Put

\[
 D(H)=N\bigl(|H|-|\Gamma(H)|\bigr)-C\rho(H)
     =R|H|+Ce(H)-N|\Gamma(H)|.                       \tag{0.1}
\]

The absorbing-newborn inequality is exactly `D(H)<=0` for every `H`.
This note proves that any counterexample compresses, without losing
counterexample status, to a set which is simultaneously

1. Galois closed;
2. an outer stopping set: every active outer row has at least two distinct
   middle neighbours in the set; and
3. connected in the simple middle--outer incidence graph.

Thus an all-`m` proof need only treat connected closed outer-2-cores.

There is also an exact edge ledger.  Let `F` be the output Catalan path
forest and define

\[
 \beta(H)=\sum_{x\in H}(2-d_F(x)),                    \tag{0.2}
\]

the forest endpoint/isolated-slot mass.  If `d_H(o)` counts occurrence
**multiplicity**, put

\[
 \lambda(H)=\sum_{o\in\Gamma(H)}(m+2-d_H(o)).        \tag{0.3}
\]

This is the number of occurrence edges entering the active outer rows from
`X\H`.  Then

\[
 (m+2)\bigl(|H|-|\Gamma(H)|\bigr)
       =4|H|-\beta(H)-\lambda(H),                    \tag{0.4}
\]

and the reserve inequality is equivalent to

\[
 \boxed{
 m\bigl(\beta(H)+\lambda(H)\bigr)+2|H|
       \ \ge\ 2(2m+1)e(H).}                          \tag{0.5}
\]

Formula (0.5) is the sharp nonlocal pooling invariant.  The four DERF
middle sectors partition both `beta` and `lambda`, so their credits add
exactly; no common-neighbour allocation to individual rows is required.

The authenticated `n=3 -> 4` counterexample leaf-peels to the literal
closed connected outer-2-core

```text
{0x55,0x5a,0x5c,0x66,0x69,0x6c,0x71,0x72,
 0x74,0x95,0xac,0xb2,0xb4,0xe4,0xe8,0xf0}.
```

Its sharp profile is

\[
 (|H|,|\Gamma H|,e,\rho,\beta,\lambda,D)
                   =(16,9,7,9,9,13,14).              \tag{0.6}
\]

The two sides of (0.5) are `120` and `126`.  This is a concrete obstruction
to proving (0.5) from closure, the 2-core condition, or ordinary Boolean
rank isoperimetry alone.

## 1. Galois closure

For `H subseteq X`, define

\[
 \operatorname{cl}(H)
   =\{x\in X:\Gamma(x)\subseteq\Gamma(H)\}.          \tag{1.1}
\]

### Lemma 1.1 (closure strictly improves a deficit)

One has

\[
 H\subseteq\operatorname{cl}(H),\qquad
 \Gamma(\operatorname{cl}(H))=\Gamma(H),             \tag{1.2}
\]

and therefore

\[
 D(\operatorname{cl}(H))-D(H)
 =R\,|\operatorname{cl}(H)\setminus H|
  +C\bigl(e(\operatorname{cl}(H))-e(H)\bigr).        \tag{1.3}
\]

In particular, if closure adds a vertex then the deficit increases
strictly.

#### Proof

Every neighbour of a newly added vertex already lies in `Gamma(H)`, so
closure adds no outer vertex.  Conversely it contains `H`, giving equality
of the two boundaries.  The function `e` is monotone.  Equation (1.3)
now follows from (0.1), and `R>0` at every parameter in scope. \(\square\)

Thus every global maximum of `D` may be taken closed.  Closed sets are
exactly complements of outer neighbourhoods:

\[
 H=X\setminus\Gamma(U),\qquad U=O\setminus\Gamma(H). \tag{1.4}
\]

This is the precise closed-set compression; no coordinate order or SCD is
used.

## 2. Leaf peeling and the stopping core

For `x in H`, let

\[
 p_H(x)=|\{o\in\Gamma(H):N_G(o)\cap H=\{x\}\}|      \tag{2.1}
\]

count active outer rows for which `x` is the unique **distinct** middle
neighbour.  Let

\[
 \epsilon_H(x)=e(H)-e(H\setminus\{x\})\in\{0,1\}.   \tag{2.2}
\]

The value is one exactly when removing `x` loses a touched inherited block
or a selected newborn singleton resource.

### Lemma 2.1 (exact leaf deletion)

\[
 D(H\setminus\{x\})-D(H)
       =-R-C\epsilon_H(x)+Np_H(x).                   \tag{2.3}
\]

Hence if `p_H(x)>=1`, deleting `x` never decreases `D`.  Equality is
possible only when `p_H(x)=epsilon_H(x)=1`.

#### Proof

Deletion removes one middle vertex, `epsilon_H(x)` endpoint resources, and
exactly `p_H(x)` outer neighbours.  Substitute these three changes into
(0.1).  Since `N=R+C`, the minimum of the right side for `p_H(x)>=1` is
zero. \(\square\)

Iteratively delete a vertex lying alone in an active row.  A positive
deficit survives every deletion, and the process cannot reach the empty
set because `D(empty)=0`.  It stops at a nonempty set in which every active
outer row has at least two distinct middle neighbours.  Closing that set
adds no active row, can only increase row occupancies, and strictly improves
the deficit if it adds anything.

### Corollary 2.2 (closed outer-2-core reduction)

If any `H` has `D(H)>0`, then some nonempty closed outer-2-core `H_0` has

\[
                         D(H_0)\ge D(H)>0.            \tag{2.4}
\]

Equivalently, a positive maximizer of minimum cardinality is already closed
and has no private outer neighbour.

The same calculation gives a useful packet-peeling rule.  For
`S subseteq H`, let `b_H(S)` count active rows all of whose `H`-neighbours
lie in `S`, and let `s_H(S)=e(H)-e(H\setminus S)`.  Then

\[
 D(H\setminus S)-D(H)=-R|S|-Cs_H(S)+Nb_H(S).         \tag{2.5}
\]

Thus any packet satisfying `Nb_H(S)>=R|S|+Cs_H(S)` may be peeled without
weakening a counterexample.

## 3. Connected reduction

Let `H_1,...,H_t` be the middle shores of the connected components of the
simple incidence graph induced by `H union Gamma(H)`.  Let `s` be the
number of nontrivial inherited endpoint blocks whose two endpoints lie in
different components.  Boundary and vertex cardinalities add, while such
a split block is counted twice in `sum e(H_j)` and once in `e(H)`.  Hence

\[
                         D(H)=\sum_j D(H_j)-Cs.        \tag{3.1}
\]

If `D(H)>0`, at least one component has positive deficit.  If `H` was
closed, each `H_j` is closed: a vertex all of whose neighbours lie in that
component's outer shore belongs to `H` by closure and then belongs to the
same incidence component.  The outer-2-core property also passes to every
component.

### Theorem 3.1 (exact counterexample normal form)

The absorbing-newborn inequality fails if and only if it fails on a
connected, Galois-closed outer-2-core.

This is a genuine reduction of the quantifier family, not a new hypothesis.

## 4. Exact endpoint/cross-boundary ledger

The direct occurrence multigraph has the dimension-uniform degree laws

\[
 d_G(x)=m-d_F(x),\qquad d_G(o)=m+2.                  \tag{4.1}
\]

Consequently the number of occurrence edges from `H` into its boundary is

\[
 E(H,\Gamma H)=m|H|-\sum_{x\in H}d_F(x)
               =(m-2)|H|+\beta(H).                  \tag{4.2}
\]

On the other hand it is `(m+2)|Gamma(H)|-lambda(H)`.  Equating these
expressions proves (0.4).

The Catalan parameters satisfy

\[
                         {N\over C}={m(m+2)\over2(2m+1)}. \tag{4.3}
\]

Substitute (0.4) into `C rho >= N defect`, use `rho=|H|-e`, and multiply by
`2(2m+1)`.  This gives (0.5).  More precisely,

\[
 m(\beta+\lambda)+2|H|-2(2m+1)e
      =-{2(2m+1)\over C}D(H).                        \tag{4.4}
\]

Thus the ledger records the exact deficit, not only its sign.

Every positive-defect set satisfies

\[
                         \beta(H)+\lambda(H)<4|H|,    \tag{4.5}
\]

so a counterexample is necessarily a near-full-row cluster.  This explains
why a row-atomic allocation is too rigid: the useful quantity is the total
cross-boundary occurrence credit `lambda`, pooled across the entire active
cluster.

### Four-sector form

Partition the middle layer by the two newborn-coordinate tags
`ab in {00,01,10,11}`.  Let `h_ab`, `beta_ab` be the corresponding parts.
Let `lambda_ab` count occurrence edges from tag-`ab` vertices outside `H`
into active outer rows.  Charge every inherited touched block to sector
`10`, and charge a newborn terminal hit to its own sector; call the result
`e_ab`.  Then

\[
 \sum_{ab}\left[m(\beta_{ab}+\lambda_{ab})+2h_{ab}
                 -2(2m+1)e_{ab}\right]
 =-{2(2m+1)\over C}D(H).                             \tag{4.6}
\]

This is the exact four-sector overlap accounting requested by the
recursive problem.  Individual sector summands need not be nonnegative;
the theorem requires nonlocal pooling of their credits.

There is a complementary simple-neighbourhood form which isolates the
overlap loss explicitly.  Write `H_s` for the part of `H` in middle sector
`s`, and for an outer sector `o` put

\[
 T_{o,s}=\Gamma_o(H_s),\qquad
 a_s=\sum_o|T_{o,s}|-|H_s|,                         \tag{4.7}
\]

\[
 \ell_o=\sum_s|T_{o,s}|-
          \left|\bigcup_sT_{o,s}\right|.            \tag{4.8}
\]

Direct inclusion--exclusion, with no inequality, gives

\[
 |H|-|\Gamma(H)|=\sum_o\ell_o-\sum_s a_s            \tag{4.9}
\]

and therefore

\[
 C\rho(H)-N\bigl(|H|-|\Gamma(H)|\bigr)
   =C\rho(H)+N\sum_s a_s-N\sum_o\ell_o.             \tag{4.10}
\]

Indeed, `sum_s a_s=sum_(o,s)|T_(o,s)|-|H|`, whereas
`sum_o ell_o=sum_(o,s)|T_(o,s)|-|Gamma(H)|`; subtracting proves
(4.9).

In the strict four-sector lift the allowed middle-to-outer incidences are

\[
\begin{array}{c|cccc}
 &00&01&10&11\\ \hline
\text{upper}&00,01&01,11&10,11&11\\
\text{lower}&00&00,01&00,10&01,11
\end{array}                                         \tag{4.11}
\]

(the entries in a column are the possible outer sectors for that middle
sector).  Hence only `ell_01,ell_11` can be nonzero above, and only
`ell_00,ell_01` below.  The surviving all-parameter assertion can thus also
be written as the exact closed-core overlap bound

\[
 N\sum_o\ell_o\le C\rho+N\sum_s a_s.                \tag{4.12}
\]

The dual source-side identity shows where genuinely nonlocal reserve enters.
For an outer family split into sectors `U_o`, set `W_o=Gamma(U_o)` and

\[
 f(W)=R|W|+C\bigl(p_I(W)+t_B(W)\bigr).              \tag{4.13}
\]

The possible overlaps form the path

\[
 00-01-11-10\quad\text{above},\qquad
 10-00-01-11\quad\text{below}.                      \tag{4.14}
\]

The family has the running-intersection property on this path.  If `s_I`
counts inherited endpoint blocks split between the two exclusive parts of
the feeders of middle sector `10`, then

\[
 f\!\left(\bigcup_oW_o\right)
  =\sum_o f(W_o)-\sum_{uv\in E(4.14)}f(W_u\cap W_v)+Cs_I. \tag{4.15}
\]

This is exact, not a relaxation.  The final positive term is the reserve
which the row-atomic common-neighbour model discards.  Formula (4.15) is
asserted for the strict four-sector running-intersection family, not for an
arbitrary collection of sets.  To prove it, apply tree inclusion--exclusion
to vertex cardinality and newborn-terminal singletons.  Every inherited
endpoint lies in middle sector `10`, so only the two `10` feeders can
contain one; their complete-pair indicator obeys ordinary two-set
inclusion--exclusion plus exactly the split-pair term `s_I`.

## 5. Why generic uncrossing and Kruskal--Katona do not close the gate

For two middle sets `A,B`, define

* `omega_I(A,B)` as the number of inherited endpoint pairs split between
  `A\B` and `B\A`; and
* `omega_G(A,B)=|Gamma(A) cap Gamma(B)|-|Gamma(A cap B)|`.

Direct inclusion--exclusion gives

\[
 D(A)+D(B)-D(A\cup B)-D(A\cap B)
             =C\omega_I(A,B)-N\omega_G(A,B).         \tag{5.1}
\]

Accordingly uncrossing works for a pair only when
`N omega_G >= C omega_I`.  It is not automatic.  The authenticated outputs
contain inherited endpoint pairs with no common outer neighbour (already
`8,8` on the two parameter-five shores).  Taking the two singleton endpoint
sets gives `omega_I=1` and `omega_G=0`, the exact wrong-sign term `C`.
Hence generic submodular or laminar-family arguments are invalid.

On the upper occurrence shore every selected occurrence is a containment
from rank `m` to rank `m+2`, but `Gamma_G(H)` is only a sparse,
multiplicity-bearing subgraph of the full two-step upper shadow.  Thus

\[
                         \Gamma_G(H)\subseteq\partial^{+2}H,        \tag{5.2}
\]

and ordinary Kruskal--Katona lower bounds the larger set on the right, not
the occurrence neighbourhood needed on the left.  A valid isoperimetric
proof must use the actual recursive occurrence maps or prove (0.5) directly
on the closed stopping cores.  The lower shore has the complement-dual
statement with the full two-step lower shadow.

These are sharp method obstructions, not counterexamples at parameters
five through seven.

## 6. Authenticated finite replay

The solver-free audit reconstructs occurrence multiplicities and simple
neighbourhoods independently from the retained strict chain.

For the parameter-four upper counterexample, deleting the sole leaf
`0xc5` leaves the core (0.6).  Its nine active rows have simple occupancies

\[
                         2^3,\ 3^3,\ 4^3,             \tag{6.1}
\]

and multiplicity occupancies

\[
                         3^2,\ 4^1,\ 5^5,\ 6^1.      \tag{6.2}
\]

So the counterexample survives all three structural compressions.

For every authenticated output parameter `m=4,5,6,7` and both shores:

* the full middle set is equality in both reserve and edge ledgers;
* all multidegrees in (4.1) replay exactly; and
* the protected endpoint support itself leaf-peels to a zero-deficit
  stopping core: three middle/three outer vertices on the upper shore and
  the empty set on the lower shore.

The simple-edge and parallel-excess counts are

\[
\begin{array}{c|rr|rr}
m&\text{upper simple}&\text{upper parallel}&
   \text{lower simple}&\text{lower parallel}\\ \hline
4&132&36&131&37\\
5&633&207&628&212\\
6&2878&1082&2854&1106\\
7&12920&5098&12903&5115.
\end{array}                                           \tag{6.3}
\]

This also audits why multiplicity must be retained in `lambda` even though
closure and Hall boundary use the simple graph.

The independent four-sector replay gives two further finite facts.

* The peeled parameter-four obstruction has sector profile
  `01^4 10^9 11^3`; its only simple overlap loss is `ell_11=8`, while
  `a_11=1`.  Equation (4.10) replays the margin `-14` exactly.
* At each authenticated output parameter `m=5,6,7`, every nonempty proper
  union of whole middle sectors satisfies the reserve inequality on both
  shores.  The sharp proper-sector margins are respectively

  \[
                         1428,\qquad14454,\qquad155727. \tag{6.4}
  \]

  In all three cases the sharp union is `00 union 01 union 11`, excluding
  the inherited sector `10`.  Consequently any counterexample in these
  three outputs must split at least one sector internally.

For one outer row from each inherited feeder, the numbers of row pairs with
positive split credit `s_I=1` are, upper/lower,

\[
                  14/8,\qquad49/39,\qquad147/126    \tag{6.5}
\]

at `m=5,6,7`; no such row pair has credit above one.  These counts verify
that the nonlocal term in (4.15) is genuinely present.  They are finite
support evidence, not an all-parameter lower bound.

An exact CP separator implements the complete closed-2-core reduction with
literal boundary ORs, touched-block ORs, closure rows and outer-2-core rows.
The bounded authenticated `m=6` upper-shore run ended `UNKNOWN` after
`180.002` seconds, `3,929,579` branches and `1,725,642` conflicts, using one
worker and `143,704` KiB peak RSS.  It found no witness, but a satisfaction
run's displayed bound has no proof meaning.  No result for the lower shore
or `m=7` is inferred from this resource-limited run.

## 7. Exact surviving induction gate

The all-parameter absorbing-newborn theorem is now reduced to the following
statement and no further:

> For the actual recursive newborn bank, every connected closed outer-2-core
> obeys (0.5), simultaneously on the two complementary shores.

The finite `n=4 -> 5` robust theorem proves this in that output.  Universal
absorption at `n=5 -> 6` and `n=6 -> 7` is not inferred here from stored
orientations and remains subject to exact separation.  The parameter-four
core (0.6), the split-pair term in (5.1), and the sparse-shadow direction in
(5.2) show that closure, stopping-set structure, generic uncrossing, and
ordinary rank isoperimetry alone cannot prove the surviving statement.

No claim about common `Q`, rooted graphic support, residence, deeper
shadows, a compiler, or `nu(k)=B(k)` follows.

## 8. Audit artifacts

```text
scratch/audit_threadD_catalan_newborn_closed_core_ledger_20260731.py
scratch/threadD_catalan_newborn_closed_core_ledger_20260731.audit.json
scratch/audit_threadD_catalan_newborn_four_sector_pooling_20260731.py
scratch/threadD_catalan_newborn_four_sector_pooling_20260731.audit.json
scratch/search_threadD_newborn_closed_2core_cpsat_20260731.py
scratch/threadD_newborn_closed_2core_n6_upper_20260731.unknown.audit.json
scratch/threadD_newborn_closed_2core_n6_upper_20260731.resource.log
```

The two files named `audit_...closed_core` and `audit_...four_sector` import
no optimizer and perform no search.  The separately named `search_...`
file is the exact bounded CP separator; its retained result is explicitly
`UNKNOWN_RESOURCE_LIMIT`.  All three authenticate

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

before reconstructing every displayed quantity.
