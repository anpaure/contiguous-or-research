# K16 H1 joint13 proxy-OR-closure and safe-follower theorem

Date: 2026-07-30  
Lane: AD  
Status: **proved source-relative reductions; feasibility UNSOLVED/UNKNOWN**

## 1. Frozen scope

Let $A$ be the authenticated length-$12{,}873$ word with sole hole
$11373=\mathtt{0x2c6d}$, and freeze the editable support

\[
 [0,2)\ \dot\cup\ [4486,4490)\ \dot\cup\ [6438,6441)
 \ \dot\cup\ [12869,12873).
\]

This note starts from the independently audited canonical occupancy model:

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a

scratch/k16_reorganized_h1_exact_provider_atlas_v2.audit.json
SHA-256 b216a9da50abe571969049cc5c60b4dff534c6eebba286de1612ef9c124d3c68

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.cnf
SHA-256 251229383ec319a744fea37bd2f3f89bdf59e638727677166f0eaa7751ecd9bb

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.map.json
SHA-256 f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31
```

The base model has 55 residual targets, 13 editable cells, 1,130 variables,
17,558 clauses, and 67,482 literals.  Its 195 availability variables obey
the exact forward and reverse canonical rows

\[
 a_{i,q}=1
 \quad\Longleftrightarrow\quad
 q\in\bigcap\{T:o_{T,i}=1\}.                                      \tag{1.1}
\]

The reverse direction in (1.1) is essential below.  Forward omission rows
alone would not imply any of the closure reductions in this note.

All claims here are conditional on this frozen 13-cell support and on the
unbounded-substitution scope `budget=-1`.  There is no claim that an
arbitrary global length-$12{,}873$ solution can be moved into this support.

## 2. Exact target-intersection and width-OR closure

Let $\mathcal R$ be the 55 residual masks, and put

\[
 \mathcal F=
 \left\{\bigcap_{T\in X}T:X\subseteq\mathcal R\right\},             \tag{2.1}
\]

where the empty intersection is $\mathtt{0xffff}$.  Direct meet closure
gives

\[
 |\mathcal F|=216,\qquad
 \min\mathcal F=\mathtt{0x0040},\qquad
 \mathtt{0xffff}\in\mathcal F.                                    \tag{2.2}
\]

For $T\in\mathcal R$, define

\[
 \mathcal F_T=\{T\cap C:C\in\mathcal F\},
 \qquad
 \mathcal U_w(T)=
 \{C_1\cup\cdots\cup C_w:C_j\in\mathcal F_T\}.                    \tag{2.3}
\]

### Lemma 2.1 (selected-chart state containment)

Suppose the occupancy signature selects target $T$ on a chart
$J=[f,l]$ of width $w=l-f+1$.  Let $C_i$ be the canonical mask at a
cell $i\in J$.  Then

\[
 C_i\in\mathcal F_T,qquad
 U_J:=\bigcup_{i\in J}C_i\in\mathcal U_w(T).                        \tag{2.4}
\]

#### Proof

The selected chart makes $T$ active at every cell of $J$.  If
$\mathcal A_i$ is the set of all other selected targets active at $i$,
then exact canonicality (1.1) gives

\[
 C_i=T\cap\bigcap_{S\in\mathcal A_i}S.
\]

The second factor belongs to $\mathcal F$, including the case
$\mathcal A_i=\varnothing$, when it is the empty intersection
$\mathtt{0xffff}$.  Thus $C_i\in\mathcal F_T$, and taking the union over
the $w$ cells proves the second assertion.  Notice that the unused FULL
state is a necessary neutral element: it represents “no other active
target.”  It never makes a $T$-active cell FULL, because
$T\cap\mathtt{0xffff}=T$.  $\square$

The cells in (2.3) are allowed to choose their intersection states
independently.  Hence $\mathcal U_w(T)$ is an exact finite **overfamily**
of actual selected-chart unions.  It deliberately forgets the fact that
every other target has one contiguous occupancy run.  This loss cannot
invalidate an implication proved on all of $\mathcal U_w(T)$.

For the frozen instance, all 220 families with
$T\in\mathcal R$ and $1\le w\le4$ have at most 440 states.

## 3. Exact proxy-generator theorem

Fix a chart $(T,J,N)$, where $N$ is its residual need.  Partition
$\mathcal U_w(T)$ into

\[
 \mathsf{Good}=\{U:N\subseteq U\},
 \qquad
 \mathsf{Bad}=\mathcal U_w(T)\setminus\mathsf{Good},                \tag{3.1}
\]

and let

\[
 E=\left(\bigcap_{U\in\mathsf{Good}}U\right)\setminus\{6\}.        \tag{3.2}
\]

Here “$\setminus\{6\}$” removes the common coordinate, not the integer
mask 6.  The family $\mathsf{Good}$ is nonempty because the state
$T$ itself is available and contains every chart need.

Choose $G\subseteq E$ of minimum cardinality, breaking ties
lexicographically, subject to

\[
 \forall U\in\mathsf{Bad},\qquad G\nsubseteq U.                    \tag{3.3}
\]

### Theorem 3.1 (exact chartwise proxy equivalence)

For every $U\in\mathcal U_w(T)$,

\[
                       N\subseteq U
 \quad\Longleftrightarrow\quad
                       G\subseteq U.                               \tag{3.4}
\]

Consequently the guarded durable row for every tracked bit of $N$ may be
replaced by the guarded durable rows for the bits of $G$, without changing
the satisfying assignments of the other canonical variables.

#### Proof

If $N\subseteq U$, then $U\in\mathsf{Good}$.  Definition (3.2) gives
$G\subseteq E\subseteq U$.  Conversely, if $G\subseteq U$ and
$N\nsubseteq U$, then $U\in\mathsf{Bad}$, contradicting (3.3).
This proves (3.4).

Under a selected chart signature, Lemma 2.1 places the actual editable
union $U_J$ in $\mathcal U_w(T)$.  A guarded bit row says exactly that
the bit occurs in $U_J$.  Thus the conjunction of the $N$-rows and the
conjunction of the $G$-rows are equivalent.  Outside the signature both
sets of guarded clauses are vacuous.  $\square$

The important extra freedom is $G\nsubseteq N$: a proxy coordinate may
be absent from the formal need but forced in every good canonical state.
The old-to-new implication uses $G\subseteq\bigcap\mathsf{Good}$; the
new-to-old implication uses the bad-state hitting condition (3.3).

### Exact census

There are 1,595 charts but only 445 distinct triples $(T,w,N)$.  Exhaustive
enumeration over at most 440 union states and at most 11 tracked coordinates
per target gives

| chart width | old durable rows | retained proxy rows | removed |
|---:|---:|---:|---:|
| 1 | 4,772 | 1,962 | 2,810 |
| 2 | 3,188 | 1,976 | 1,212 |
| 3 | 1,721 | 1,112 | 609 |
| 4 | 620 | 415 | 205 |
| **total** | **10,301** | **5,465** | **4,836** |

The retained durable rows have 25,819 literals, versus 46,486 originally.

Relative to generators artificially restricted to $G\subseteq N$, four
charts change:

```text
T= 9981, J=[1,1] : (3,4,7)   -> (4,10)       [the sole 3-to-2 reduction]
T=30317, J=[5,5] : (3,10,14) -> (2,3,14)
T=48367, J=[1,1] : (1,13)    -> (1,3)
T=48367, J=[8,8] : (1,13)    -> (1,3)
```

For $T=30317,J=[5,5]$, exact enumeration finds no eligible two-bit
separator; its size remains three.  This corrects a preliminary attribution
of the unique row saving to that chart.

## 4. Optimality in the positive chartwise clause language

The unit proxy rows of Section 3 are a special case of a more general
guarded positive clause.  For a coordinate set $C$, write

\[
 \neg\sigma_{T,J}\ \vee\
 \bigvee_{q\in C}\ \bigvee_{i\in J}a_{i,q}.                        \tag{4.1}
\]

### Lemma 4.1 (prime-clause/set-cover characterization)

Clause (4.1) is valid for the old chart condition if and only if

\[
                         C\cap U\ne\varnothing
 \quad\text{for every }U\in\mathsf{Good}.                          \tag{4.2}
\]

Such a clause rejects exactly the bad states $U$ with
$C\cap U=\varnothing$.  Therefore a family of positive clauses is exactly
equivalent to the old chart condition if and only if their rejection sets
cover $\mathsf{Bad}$.  Inclusion-minimal transversals of
$\mathsf{Good}$ suffice as candidates.

#### Proof

On an active chart, (4.1) says $C\cap U_J\ne\varnothing$.  It is valid on
all old-feasible states exactly when it meets every good state, proving
(4.2).  A bad state violates it exactly when it is disjoint from $C$.
Covering every bad state is therefore necessary and sufficient for the
conjunction to imply $N\subseteq U_J$.  Removing a nonminimal transversal
can only enlarge its rejection set, so only inclusion-minimal transversals
are needed.  $\square$

The complete frozen census contains 2,336 prime candidates over the 445
distinct chart types, at most 11 for one type.  Exact set cover, minimizing
first the number of clauses and then their availability-literal count,
returns exactly the 5,465 singleton proxy clauses of Section 3.  Thus:

This candidate enumeration is complete: a coordinate outside $T$ meets
no good state and cannot help a transversal, while the common coordinate 6
belongs to every bad state and cannot reject one.  Hence it suffices to
enumerate subsets of the at most 11 noncommon coordinates of $T$.

### Corollary 4.2 (restricted optimality)

The 5,465-row durable family is clause-minimal among all chartwise guarded
positive availability-CNFs whose validity is certified solely by the
independent-cell families $\mathcal U_w(T)$.  Allowing wider positive
clauses does not save a clause and only increases the secondary literal
cost.

This is not an optimality theorem for clauses using negative availability
literals, cross-chart correlations, or the exact interval-pattern tuple
family.

## 5. One exact existential projection

After the proxy reduction, availability

\[
                    a_{2,8}
 \quad\text{(physical position 4486, old variable 973)}             \tag{5.1}
\]

occurs in no durable row.  It occurs only in the 51 forward omission rows
for targets lacking coordinate 8 and its one reverse canonical row.  Those
52 clauses, containing 154 literals, uniquely define (5.1): it is false if
an omitter is active and true otherwise.  Existentially eliminating the
variable therefore permits deletion of all 52 definition clauses.

No other availability variable is unused.  Renumbering variables above 973
gives the primary exact projection:

| model | variables | clauses | literals |
|---|---:|---:|---:|
| audited canonical base | 1,130 | 17,558 | 67,482 |
| proxy-closure projection | **1,129** | **12,670** | **46,661** |

The reduction is 1 variable, 4,888 clauses, and 20,821 literals.  The
projected formula has exactly the existential projection of the base
formula onto its retained variables.

## 6. Optional strict-containment safe-follower forest

Let $N(T,J)$ be the exact need of target $T$ on chart $J$.

### Lemma 6.1 (safe follower)

Suppose $S\subsetneq T$ and

\[
                         N(T,J)\subseteq N(S,J).                    \tag{6.1}
\]

Conditional on selecting $S$ on $J$, one may select $T$ on the same
chart $J$, preserving satisfiability.

#### Proof

The selected $S$-chart makes every canonical cell on $J$ a submask of
$S$, hence of $T$, and its union supplies $N(S,J)$, hence $N(T,J)$.
The exact fixed base for the $T$-chart therefore makes $J$ a literal
$T$-witness.

Replace the old selected $T$-chart by $J$.  Adding $T$ on $J$ does
not change a canonical cell, because $S\subsetneq T$ is already active
there.  Removing $T$ from its old cells can only enlarge their target
intersections.  Every other target still active at such a cell contains all
newly admitted coordinates, so no selected witness is contaminated, while
durable supply cannot decrease.  Thus the recanonicalized assignment is
still feasible.  $\square$

For every target having an eligible strict subtarget, choose a parent that
maximizes the number of safe charts in (6.1), breaking ties by the integer
value of the parent.  Strict containment makes the resulting directed graph
acyclic, and one parent per target makes it a forest.  Processing it from
smaller to larger targets proves simultaneous canonicalization.

The exact forest has

\[
        36\text{ edges},\qquad150\text{ chart triggers}.            \tag{6.2}
\]

If $\sigma_{S,J}$ is the exact occupancy signature, encode
$\sigma_{S,J}\Rightarrow\sigma_{T,J}$ one consequent literal at a time.
There are 92 signatures of size 2 and 58 of size 3, producing

\[
                  358\text{ clauses and }1{,}248\text{ literals}.   \tag{6.3}
\]

The optional forest model consequently has 1,129 variables, 13,028 clauses,
and 47,909 literals.

Unlike Sections 3--5, these follower clauses do not preserve every occupancy
assignment.  Lemma 6.1 proves only **equisatisfiability**, by selecting a
canonical representative.  They remain exact for support-restricted
existence and are not a global-support WLOG theorem.

## 7. Frozen artifacts and independent audit

```text
scratch/build_ad_k16_h1_joint13_orclosure_reduced_cnf_20260730.py
SHA-256 6cc6b7d58bfb9b4ab4dae7e17ccfca94bb25849a71c36b98ff21a5e824fd5f31

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.cnf
SHA-256 c59418fd0a01a9f5275c9c067c97d051b8ddc7bff02110e91b8c127cc8546683

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.safe_followers.cnf
SHA-256 4011d80e749424ac71edf02e783a1889d043d7510b9a068c719dbdf58075fe69

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.audit.json
SHA-256 e7e24b3cac5fb1820f4da3b6bd7f098f1459063ca4b1ca421f20d2b9ddbe1617
payload SHA-256 99ed0d75e80fa73b15cdd96686d482d7f372c1b24371e37c73eb667da85bcd5a

scratch/audit_ad_k16_h1_joint13_proxyclosure_reduced_cnf_20260730.py
SHA-256 d256c9eb82a70df7a22712f74e29b0ad448309bf2f5d54744d59a4f0ebf24d58

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.independent_audit.json
SHA-256 d8c7d189daf2bd705c07873f40cd0c197e3a674f3159842d0c732b17f7e145f8
payload SHA-256 704166a9517cc6ddc6244c93123f9d7ec90899520a86a01596d511092c4e3dae
```

The independent audit constructs the 216-state meet closure by pairwise
fixed point rather than the builder's incremental subset-intersection
method.  It independently recomputes every $\mathcal U_w(T)$, all 445
minimum generators, all 2,336 prime-clause candidates and exact covers, the
single dead availability variable, the reduced ordered clause stream, and
all 36 follower edges.  It reports `PASS_SOLVER_FREE`.

## 8. Exact remaining boundary

No SAT solver was run locally or remotely for either reduced CNF.  The raw
unbounded model already running elsewhere was not duplicated or touched.
The feasibility status of the 13-cell support remains
**UNSOLVED/UNKNOWN**.

An exact interval-pattern refinement was tested only under a hard
100,000-tuple cap and was abandoned without an artifact: for the hardest
target $T=48367$, width 2 closes at 19,881 tuples, while widths 3 and 4
cross the cap before completion.  Therefore no correlated-tuple reduction,
SAT claim, UNSAT claim, or global $K=16$ conclusion is made here.  The
authenticated bracket remains

\[
                         12873\le \nu(16)\le12874.
\]
