# `k=17`: the static necklace age-flag factor, the direct-SCD obstruction, and an exact quotient model

Date: 2026-08-01

Status: unconditional finite static-factor theorem and scoped obstruction.
The direct use of one necklace symmetric-chain decomposition is ruled out;
an exact cross-chain factor has been found and independently replayed.  No
changing-owner chronology, strict-upper target, or upper-safe physical
opening is supplied, so this note does not prove `nu(17)=24313`.

## 1. The static object

Write

\[
 \mathcal N_s=\binom{\mathbb Z_{17}}s/\mathbb Z_{17}.
\]

For `1<=s<=16` the rotation action is free, and hence

\[
 |\mathcal N_s|={1\over17}\binom{17}s.
\]

In particular

\[
 (|\mathcal N_s|)_{s=1}^9
 =(1,8,40,140,364,728,1144,1430,1430).
 \tag{1.1}
\]

The nine certified age types and their multiplicities are

\[
\begin{array}{c|c|c}
\text{name}&(c_0,c_1,c_2,c_3)&\text{mass}\\ \hline
A&(1,5,2,1)&139\\
B&(1,6,1,1)&297\\
C&(2,5,1,1)&8\\
D&(3,3,2,1)&20\\
E&(3,4,1,1)&20\\
F&(4,3,1,1)&140\\
G&(5,1,2,1)&127\\
H&(5,2,1,1)&237\\
I&(6,1,1,1)&442.
\end{array}
\tag{1.2}
\]

An age flag of type `c` over a rank-nine owner `T` is a disjoint
partition

\[
 T=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2
      \mathbin{\dot\cup}C_3,
 \qquad |C_i|=c_i,
\]

and emits the nested necklace classes

\[
 [C_0]\subset[C_0\cup C_1]\subset
 [C_0\cup C_1\cup C_2]\subset[T].
 \tag{1.3}
\]

At ranks two through nine the desired static object is exactly a partition
of all necklace elements into 1430 flags of the nine types and masses in
(1.2).  Types `A,B` contribute three elements of the truncated poset
(their rank-one suffix is slack), and the other 994 flags contribute four.
Indeed

\[
 436\cdot3+994\cdot4=5284
 =\sum_{s=2}^9|\mathcal N_s|.
 \tag{1.4}
\]

This is the precise static `Cat_8` necklace-poset chain factor induced by
the age certificate.

## 2. One fixed necklace SCD does not directly realize the factor

Let an arbitrary symmetric-chain decomposition of the necklace poset be
fixed.  The number of its central chains born at rank `b` is the adjacent
rank difference.  For `b=0,2,...,8` these numbers are

\[
\begin{array}{c|rrrrrrrr}
b&0&2&3&4&5&6&7&8\\ \hline
\#\text{ chains}&1&7&32&100&224&364&416&286.
\end{array}
\tag{2.1}
\]

(There is no new chain at rank one.)  After restriction to ranks `2,...,9`,
a chain born at `b` contains respectively

\[
 8,8,7,6,5,4,3,2
 \tag{2.2}
\]

elements.

### Proposition 2.1 (direct-SCD obstruction)

It is impossible to obtain the required static age factor while requiring
every output flag to lie inside one fixed SCD chain.

### Proof

Every central SCD chain contains exactly one rank-nine element, and every
age flag contains exactly one rank-nine owner.  Since both families have
1430 members, an SCD-contained factor would assign exactly one output flag
to each central SCD chain.

But an age flag contains at most four elements at ranks `2,...,9`, whereas
every SCD chain born at rank at most five contains at least five such
elements by (2.2).  Those extra elements cannot be assigned to another
SCD-contained flag: their SCD chain has already supplied its unique
rank-nine endpoint, and distinct SCD chains are disjoint.  Contradiction.
\(\square\)

Thus an SCD can only be a reservoir.  Any successful use must split long
chains and reconnect their fragments across distinct SCD chains.  The
existence of an SCD, by itself, supplies neither those cross-chain
containments nor the changing-owner chronology.

This is a scoped obstruction.  It does not rule out a GKS chain-cover
recombination using non-SCD containment edges.

For a fixed SCD, the exact recombination question is obtained without any
new variables.  Give a flag `f` the cost

\[
 \rho(f)=\#\{\text{successive inclusions in }f
                 \text{ whose endpoints lie in different SCD chains}\}.
 \tag{2.3}
\]

Minimize `sum_f rho(f) z_f` subject to (3.1)--(3.3) below.  Optimum zero is
ruled out by Proposition 2.1.  Any finite optimum is literally a split of
the original SCD into singleton/interval fragments followed by that many
cross-chain recombination links.  Thus this weighted exact cover is the
precise finite GKS split/recombine formulation; no informal preorder or
planarity claim is needed.

## 3. Exact static cross-chain formulation

For every owner necklace `U in N_9`, every type `t`, and every literal
aligned age partition `f` of a representative owner of type `t`, introduce
a binary variable `z_f`.  Let `ell_s(f)` be the emitted target necklace at
rank `s`, whenever `s` is one of the three proper suffix ranks of `t`.

The static factor exists if and only if

\[
 \sum_{f:\operatorname{owner}(f)=U}z_f=1
 \qquad(U\in\mathcal N_9),                              \tag{3.1}
\]

\[
 \sum_{f:\operatorname{type}(f)=t}z_f=m_t
 \qquad(t=A,\ldots,I),                               \tag{3.2}
\]

and

\[
 \sum_{f:\ell_s(f)=O}z_f=1
 \qquad(2\le s\le8,\ O\in\mathcal N_s).              \tag{3.3}
\]

Necessity is immediate.  Conversely, (3.1) selects one nested flag at
every owner, (3.2) gives the certified type masses, and (3.3) partitions
every tight lower necklace rank.  This is an exact finite hypergraph
perfect-matching formulation, not a marginal relaxation.

This system is satisfiable.  A compact 1430-row certificate is

```text
scratch/k17_static_necklace_age_flag_factor_20260801.certificate.tsv
SHA256 fa34a07bd1f5feb84b79567fd92ceec4e4ec00394963c8e5837cdc6d2046f578
```

and the independent verifier

```text
scratch/verify_k17_static_necklace_age_flag_certificate_20260801.cpp
```

reports

```text
PASS_K17_STATIC_NECKLACE_AGE_FLAG_CERTIFICATE
owners=1430 target_orbits_rank2_to8=3854
```

Thus the static cross-chain recombination exists.  What remains is to make
one such factor compatible with a changing-owner quotient cycle.

For the displayed certificate this compatibility is not a small repair.
After freezing its owner attachment, the literal changing-owner graph has
only 93 non-self arcs; 1,338 owners have zero outdegree, 1,340 have zero
indegree, and its maximum bipartite matching has size 89.  The independent
audit is

```text
scratch/audit_k17_static_flag_changing_owner_matching_20260801.cpp
```

Thus the static factor proves integrality of the flag marginal, but the
owner attachment and transition system must be chosen jointly.

The raw formulation has 17,136 possible labelled partitions per owner,
or 24,504,480 variables before obvious quotient factoring.  More exactly,
the per-type menu sizes are

\[
 (1512,504,1512,5040,2520,2520,1512,1512,504),
 \tag{3.4}
\]

whose sum is 17,136 and whose product with 1430 is 24,504,480.  The
factorized encoding below avoids this raw menu.

## 4. Exact changing-owner extension

The static factor does not yet label a chronology.  Let `f` be a flag on
owner representative `T`, and let `g` be a flag on `T'` aligned through a
quotient Johnson edge

\[
 T'=T-\{\alpha\}+\{\beta\}.
\]

Declare `f -> g` compatible precisely when

* `C_3(f)={alpha}`;
* the inserted physical coordinate `beta` lies in `C_0(g)`; and
* after undoing the quotient rotation on `g`,

  \[
        C_{j+1}(g)\subseteq C_j(f)\qquad(0\le j<3).
        \tag{4.1}
  \]

The inclusion is exactly the survivor choice in the changing-owner age
lemma; old coordinates not selected as survivors are refreshed into age
zero.

Add one directed edge variable for every compatible pair and impose one
selected edge into and out of each owner.  This gives an exact decorated
cycle-cover formulation.  Lazy subtour cuts make the quotient cover one
cycle, and nonzero total voltage modulo 17 makes its physical lift one
24310-owner cycle.

Neither SCD containment nor the static equations (3.1)--(3.3) imply (4.1).
The chronology problem is a second correlated gate.

### 4.1 The published MMM quotient cycle is an exact negative calibration

The materialized unit-voltage MMM quotient cycle

```text
scratch/k17_mmm_quotient_cycle.tsv
```

is owner- and lower-rainbow, but its 24310-owner physical lift has cyclic
owner-run minimum two.  More precisely, it has 5,695 coordinate runs of
length two and 1,598 of length three.  A depth-three age lift requires every
positive owner run to have length at least four.  Therefore this fixed cycle
admits no changing-owner age decoration of the required kind.

This is independently replayed by

```text
scratch/audit_k17_mmm_cycle_depth3_age_nogo_20260801.cpp
```

with result

```text
PASS_K17_MMM_CYCLE_DEPTH3_AGE_NOGO
voltage=1 owners=24310 min_run=2 length2=5695 length3=1598
```

Thus “take the published MMM cycle, then label it” is false.  The owner
cycle and the age flags must be selected jointly.  The fixed-cycle mode of
the generator is retained only as a certified negative calibration; it is
not a live solver lane.

## 5. Factorized `-O3` CNF generator

The executable

```text
scratch/build_k17_catalan_orbit_age_lower_skeleton_20260801.cpp
```

uses age-membership bits rather than the 23.9-million raw flag variables.
It encodes:

1. one directed non-self quotient Johnson edge into/out of every owner;
2. exact type masses;
3. one literal age partition per owner;
4. all survivor implications (4.1);
5. an exact rank-eight lower-q1 orbit rainbow; and
6. exact suffix-orbit coverage at ranks two through seven.

The exact 16 arc multiplicities of the fractional certificate are not
imposed.  They are one sufficient stationary circulation; any Hamilton
decorated cycle with the exact node masses induces its own balanced type
flow and is sufficient.

The generator was compiled and run on the H100 CPU with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic
```

and produced

```text
owner orbits                 1,430
directed non-self arcs      102,944
suffix choices             836,550
rank-2..7 target groups      2,424
rank-8 target groups         1,430
variables                 5,068,292
clauses                  25,215,929
CNF size                       561 MB
generator wall time             3.53 s
generator max RSS                30 MB
```

The skeleton omits, explicitly:

* Hamilton subtour cuts;
* nonzero-voltage enforcement;
* every strict-upper target and arbitrary-width upper witness; and
* the physical upper-safe opening required to linearize at length `W+3`.

Consequently a SAT result would settle the owner/lower decorated-cycle
gate only.  It would not be a `k=17` optimal-word certificate.

The same executable has a `--static` mode which omits all Johnson arcs and
encodes precisely (3.1)--(3.3).  Its H100 materialization has

```text
variables                 4,672,246
clauses                  21,660,079
CNF size                       487 MB
generator wall time             2.93 s
generator max RSS                30 MB
```

The direct arithmetic and SCD-birth ledger is independently checked by

```text
scratch/audit_k17_static_necklace_age_flag_counts_20260801.cpp
```

which reports

```text
PASS_K17_STATIC_NECKLACE_AGE_FLAG_COUNTS
owner_orbits=1430 truncated_elements=5284
raw_flags_per_owner=17136 raw_flag_variables=24504480
```

## 6. Exact frontier

The necklace SCD resolves the existence of nested central chains but fails
as a direct allocation of the age flags.  Cross-chain recombination is
unavoidable.  The exact finite frontier is therefore

\[
 \boxed{
 \text{static necklace flag exact cover}
 +\text{ changing-owner compatible quotient cycle}
 +\text{ upper-safe physical opening}.}
\]

The first two rows are represented without relaxation by the factorized
CNF skeleton.  The last row remains deliberately outside it.
