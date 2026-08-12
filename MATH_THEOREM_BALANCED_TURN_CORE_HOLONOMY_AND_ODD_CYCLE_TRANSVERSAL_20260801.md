# Balanced turn cores, phase holonomy, and the exact odd-cycle-transversal bound

**Date:** 2026-08-01  
**Status:** unconditional structural theorems plus an authenticated `k=17`
counterexample to raw balancedness.  This does not construct the missing
`k=17` chronology.

## 0. Verdict

The balanced-matrix route from
`MATH_THEOREM_CHRONOLOGY_FIRST_OWNER_FLAG_HALL_AND_PROTECTED_EXCHANGE_20260801.md`
has a useful exact subclass, but balancedness is not automatic even for a
highly structured exact lower flag factor.

1. If one fixes a bijective owner attachment at the head roots and keeps
   only turns using those attachments, the turn incidence matrix is
   balanced.  A fractional perfect matching in the resulting ordinary
   predecessor graph therefore rounds exactly.  In particular, a
   biregular predecessor graph is sufficient.
2. The authenticated switched GKS `k=17` exact flag factor already contains
   the minimum forbidden balanced-matrix minor

   \[
   \begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.
   \]

   It also contains a clean strong `C5` of **zero phase holonomy**.  The
   latter lifts to 17 disjoint physical strong `C5`s.  Hence no choice of
   quotient gauge can make every odd cycle a nonzero-voltage artefact.
3. The exact connected age-type inventory deletes the raw `C3`, but retains
   a different zero-holonomy clean `C5`.  That `C5` has an authenticated
   one-row portal and two disjoint alternating cycle atoms which saturate its
   five rows exactly.  It is therefore a non-TU witness, not a local parity
   impossibility.
4. More generally, for an odd cyclic covering group, every quotient strong
   odd cycle lifts to a physical strong odd cycle.  Nonzero holonomy merely
   lengthens it by an odd factor.
5. Requiring the whole turn matrix to be balanced is much stronger than
   necessary.  If `x` is a fractional perfect matching and deleting an atom
   set `Z` leaves a balanced matrix, then the integral matching deficiency is
   at most

   \[
                      \lfloor x(Z)\rfloor .
   \]

   In particular, `x(Z)<1` already forces an exact perfect matching.

The correct weaker target is therefore a **fractionally light odd-cycle
transversal in the positive support of one correlated fractional perfect
matching**, not balancedness of the complete legal-turn catalogue.

There is a sharp warning: the unrestricted physical Boolean turn catalogue
has a uniform fractional perfect matching but every odd-cycle atom
transversal has fractional mass at least `N/25`, where `N` is the size of a
middle shore.  Thus any light-transversal theorem must use the age/flag
structure essentially; Boolean union geometry or a phase opening alone
cannot prove it.

## 1. Turn hypergraphs and strong odd cycles

Let `P,Q` be two copies of the rank-`m` roots and let `O` be the rank-`m+1`
owners.  A physical Boolean turn atom is

\[
                         e=(p,q,o),
 \qquad p\ne q,\quad p,q\subset o,
 \quad o=p\cup q.                                      \tag{1.1}
\]

A fixed age-flag table retains only those atoms satisfying the literal
survivor conditions.  Its vertex--atom incidence matrix is balanced exactly
when it has no square odd-order submatrix with two ones in every row and
column, equivalently no clean strong odd Berge cycle.

### Lemma 1.1 (physical triangles are impossible)

The physical Boolean turn hypergraph contains no strong `C3`.

#### Proof

In a strong triangle the three shared resource rows must have the three
different types `P,Q,O`.  Call them `p,q,o`.  The atom sharing `p,o` implies
`p subset o`, and the atom sharing `q,o` implies `q subset o`.  The roots
are distinct facets of `o`, so `p union q=o`.  Therefore the third atom,
which contains `p,q`, also contains the selected row `o`; its column has
three rather than two selected ones, a contradiction.  `square`

This lemma is physical.  It need not survive quotienting, because the three
uses of one root or owner orbit may have incompatible phases.

## 2. An exact balanced subclass

Fix an exact rooted flag table `F`.  Let

\[
                         \theta:Q\longrightarrow O              \tag{2.1}
\]

be a bijection such that `q subset theta(q)`.  Let `H_theta` retain all
legal turn atoms `(p,q,o)` with

\[
                              o=\theta(q).                       \tag{2.2}
\]

Parallel phase-labelled atoms are retained.

### Theorem 2.1 (functional-attachment balancedness)

The incidence matrix of `H_theta` is balanced.  Fractional perfect
matchings of `H_theta` are exactly fractional perfect matchings of the
bipartite predecessor multigraph

\[
 B_\theta=(P,Q;\{pq:(p,q,\theta(q))\in H_\theta\}).              \tag{2.3}
\]

Consequently, if `B_theta` is positive biregular, then `F` has an
owner-exact literal cycle cover.  More generally, ordinary Hall in
`B_theta` suffices.

#### Proof

For every head `q`, its row and the owner row `theta(q)` are identical on
the retained columns.  Suppress the owner rows.  The remaining matrix is
the vertex--edge incidence matrix of the bipartite multigraph `B_theta`,
and hence is balanced (indeed totally unimodular after orienting one shore).

Balancedness is preserved by duplicating a row.  To see this directly,
suppose an odd two-regular square used both copies of an identical row.  A
column meeting one copy meets both, so the two copies and their two incident
columns form an even `2 x 2` component.  Removing all such components leaves
an odd two-regular square in the unduplicated matrix, a contradiction.

The head and owner equations are identical under (2.1), so the fractional
matching systems are the same.  In the biregular case uniform edge weights
give a fractional perfect matching; balanced packing integrality rounds it.
Ordinary bipartite Hall gives the final statement directly.  `square`

This is a genuine balanced subclass, but it moves the hard choice into the
joint construction of `F` and `theta`.  A frozen exact flag table can have
dead predecessor rows for every possible `theta`, as the current `k=17`
audits show.

### Corollary 2.2 (row-coherent cyclic/interval flags)

Suppose the root set is partitioned into directed cyclic rows and:

1. the adjacent union on the row entering `q` defines `theta(q)`;
2. these adjacent unions use every owner exactly once; and
3. the rooted interval flags literally propagate along every row edge.

Then the row edges form a perfect matching in `B_theta`; hence the
functional turn support is balanced and has an owner-exact cycle cover.

Thus cyclic/interval flags do solve the turn integrality gate whenever the
same row system is simultaneously exact on roots, owners and named lower
flags.  The unresolved part is precisely that simultaneous exactness.  A
root-only wreath factor is insufficient: its canonical lower interval
flags need not realize the required named lower palette.

## 3. Phase holonomy does not remove odd cycles at odd `k`

Suppose a free cyclic group `Z_k` acts on all resources and atoms.  For an
atom orbit `e` incident with a resource orbit `v`, let

\[
                         \alpha_e(v)\in\mathbb Z_k               \tag{3.1}
\]

be the incidence phase in a chosen gauge.  If a quotient strong cycle has
atom orbits `e_0,...,e_{ell-1}` and shared resource orbits
`v_0,...,v_{ell-1}`, where `v_i` joins `e_i` to `e_{i+1}`, define

\[
 h(C)=\sum_{i=0}^{\ell-1}
       \bigl(\alpha_{e_i}(v_i)-\alpha_{e_{i+1}}(v_i)\bigr)
       \in\mathbb Z_k.                                      \tag{3.2}
\]

Changing the gauge adds a telescoping vertex potential, so `h(C)` is gauge
invariant.

### Theorem 3.1 (odd-cover lift)

The quotient cycle lifts to cycles of length

\[
                    \ell\,{k\over\gcd(k,h(C))}.                 \tag{3.3}
\]

If `k` and `ell` are odd, every lifted cycle is odd.  If `h(C)=0`, there
are exactly `k` disjoint physical lifts, each of length `ell`.

#### Proof

Choose a phase for `e_0` and propagate the atom phase by requiring equality
at each shared resource.  After one circuit the new phase differs from the
old one by `h(C)`.  The first return occurs after the order
`k/gcd(k,h(C))` of this group element, proving (3.3).  The third incidence
of every quotient atom lies outside the selected quotient resource rows,
so it creates no chord after lifting.  When `k` is odd, the return order is
odd.  For zero holonomy every initial phase closes separately.  `square`

Thus nonzero voltage is not a parity cure at odd `k`: a quotient `C3` of
voltage six at `k=17`, for example, lifts to a physical `C51`.

## 4. Authenticated minimum obstructions in the exact GKS flag table

The input is the independently replayed switched GKS turn catalogue

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_turns_20260801.tsv
SHA256 6b417b8413afb915ad03becec0154927f2a659642d26bfdae8bdd80eb909f7b9
```

It contains the following three atom orbits:

\[
 (285,919,14821),\qquad
 (285,927,21451),\qquad
 (919,927,14821).                                  \tag{4.1}
\]

On the rows `tail 285`, `head 927`, `owner 14821`, their incidence minor is

\[
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix}.                                    \tag{4.2}
\]

The three target phases are `0,6,0` and the shared-owner phases are zero,
so the triangle has holonomy `6 mod 17`.  This is a determinant-two,
minimum-order certificate that the quotient turn matrix is not balanced.

More decisively, the same exact flag table contains the clean `C5` with
shared rows

```text
tail 10, head 60, owner 3707, tail 47, owner 3323
```

and atom orbits

```text
(10,47,3323)   head phase 0, owner phase 0
(10,60,1787)   head phase 0, owner phase 0
(1011,60,3707) head phase 3, owner phase 3
(47,198,3707)  head phase 0, owner phase 0
(47,173,3323)  head phase 0, owner phase 0.
```

Its holonomy is

\[
                         0+(0-3)+(3-0)+0+0=0.         \tag{4.3}
\]

It therefore gives 17 disjoint physical `C5`s.  This rules out the proposed
shortcut “all quotient odd cycles are nonzero-holonomy and can be removed by
choosing a gauge.”

The standalone `-O3` H100 audit and transcript are

```text
scratch/audit_k17_turn_hypergraph_balancedness_20260801.cpp
SHA256 fa6598d1b1371c874dd64067166ece708da70cc3ee38dcb34d337fda2a876651

scratch/k17_turn_hypergraph_balancedness_20260801.audit.txt
SHA256 f84e4334da87f7ed4ca9f265cfb9bb8900612a41863fda2318c7b34a17eba4dd
```

The conclusion is scoped: it kills balancedness of this exact GKS table,
not the existence of another exact table with a balanced turn core.

## 5. The exact weaker rounding theorem

Let `H` be any tripartite turn hypergraph with three shores of size `N`.
Let `x` be a fractional perfect matching, so

\[
                         A_Hx={\bf1},\qquad x\ge0.    \tag{5.1}
\]

For an atom family `Z`, write `x(Z)=sum_{e in Z}x_e`.

### Theorem 5.1 (fractionally light balanced-core rounding)

If `A_{H-Z}` is balanced, then

\[
                  \nu(H-Z)\ge N-\lfloor x(Z)\rfloor. \tag{5.2}
\]

In particular:

* `x(Z)<1` implies that `H-Z`, and hence `H`, has a perfect matching;
* `x(Z)<C+1` implies integral matching deficiency at most `C`.

#### Proof

The restriction `x'=x|_{H-Z}` is a feasible fractional packing in `H-Z`
of total weight

\[
                         |x'|=N-x(Z),                \tag{5.3}
\]

because summing (5.1) over one shore gives `|x|=N`.  Balancedness makes the
packing polytope of `H-Z` integral.  Hence its integral matching number is
at least the value of this feasible fractional packing and, being an
integer, satisfies

\[
 \nu(H-Z)\ge\lceil N-x(Z)\rceil
           =N-\lfloor x(Z)\rfloor.                  \tag{5.4}
\]

This proves every assertion.  `square`

It is enough that `Z` meet every strong odd Berge cycle in the **positive
support of `x`**.  Zero-weight legal atoms may simply be discarded first.
This is strictly weaker than making the full legal-turn catalogue balanced.

## 6. A growing obstruction to every phase-only balanced-core theorem

The preceding weaker theorem is useful only if the age/flag construction
produces a sparse special support.  It is false for the unrestricted Boolean
turn catalogue by a large margin.

Let `n=2m+1` and let `U_m` contain every physical turn (1.1).  Put

\[
 N={2m+1\choose m},\qquad D=m(m+1),\qquad |E(U_m)|=ND. \tag{6.1}
\]

Every tail, head and owner has degree `D`; therefore

\[
                             x_e={1\over D}           \tag{6.2}
\]

is a fractional perfect matching.

### Theorem 6.1 (linear-density clean `C5` packing)

`U_m` contains at least `|E(U_m)|/25` pairwise atom-disjoint clean strong
`C5`s.  Consequently every atom set `Z` whose deletion makes `U_m-Z`
balanced satisfies

\[
                |Z|\ge {|E(U_m)|\over25},\qquad
                x(Z)\ge {N\over25}.                 \tag{6.3}
\]

#### Proof

Choose an `(m-2)`-set `K` and four ordered distinct labels `a,b,c,d` outside
`K`.  Define selected root rows

\[
\begin{aligned}
 p_0&=K+\{a,b\},&p_1&=K+\{c,d\},\\
 q_0&=K+\{d,a\},&q_1&=K+\{b,c\},
\end{aligned}                                                    \tag{6.4}
\]

and the selected owner row

\[
                             o=K+\{a,c,d\}.           \tag{6.5}
\]

With `s=K+{a,c}`, take the five atoms

\[
\begin{aligned}
 e_1&=(p_0,q_0,p_0\cup q_0),\\
 e_2&=(p_0,q_1,p_0\cup q_1),\\
 e_3&=(p_1,q_1,p_1\cup q_1),\\
 e_4&=(p_1,s,o),\\
 e_5&=(s,q_0,o).
\end{aligned}                                                    \tag{6.6}

On the rows `q_0,p_0,q_1,p_1,o` these columns form a clean `C5`.

There are

\[
 T={2m+1\choose m-2}(m+3)(m+2)(m+1)m              \tag{6.7}
\]

ordered constructions.  A fixed atom belongs to at most
`5m(m-1)` of them: choose its one of five roles, choose `K` by deleting one
of the `m-1` elements of the intersection of its two roots, and choose the
one remaining free label in at most `m` ways.

Greedily selecting a construction removes at most `5 * 5m(m-1)` remaining
constructions (five atoms, each with the preceding load).  Hence there are
at least

\[
 {T\over25m(m-1)}
 ={1\over25}{2m+1\choose m}m(m+1)
 ={|E(U_m)|\over25}                                  \tag{6.8}
\]

pairwise atom-disjoint `C5`s.  Every balanced-core deletion meets each one,
giving the first inequality in (6.3); (6.2) gives the second.  `square`

The cycles in (6.6) are physical and therefore zero-holonomy.  Thus neither
a cyclic gauge nor one opening changes this obstruction.  The theorem does
not rule out a light balanced core for a carefully engineered depth-`d(k)`
exact flag table; it proves that such a result must exploit the survivor-age
restrictions and cannot follow from the Boolean union colouring alone.

## 7. Revised proof target

The balanced route should now be stated as follows.

> **Light supported odd-cycle transversal lemma.**  Construct one exact
> lower flag table `F` and one fractional perfect turn matching `x` such
> that the positive-support turn matrix has an atom set `Z` meeting every
> strong odd Berge cycle and `x(Z)<1`.

By Theorem 5.1 this already produces an exact owner/flag cycle cover.  For a
bounded-defect theorem it is enough to have `x(Z)=O(1)`.

Two concrete sufficient subtargets are now visible:

1. construct a functional attachment `theta` for which `B_theta` is
   fractionally perfect (Theorem 2.1, with `Z` empty); or
2. construct a correlated age circulation whose basic positive support is
   balanced except for a fractionally light cactus of odd blocks.

The authenticated zero-holonomy `C5` shows that phase coherence alone is
not the missing hypothesis.  The exact lower palette factor and the
chronology must be selected so that their **positive fractional support**,
not their complete legal catalogue, has the required near-balanced
structure.

## 8. The `k=17` type gate already has a one-regular solution

There is no aggregate age-type obstruction to the functional-attachment
subclass.  Write the nine full age types as

```text
A=(1,5,2,1)  B=(1,6,1,1)  C=(2,5,1,1)
D=(3,3,2,1)  E=(3,4,1,1)  F=(4,3,1,1)
G=(5,1,2,1)  H=(5,2,1,1)  I=(6,1,1,1)
```

with multiplicities

```text
(139,297,8,20,20,140,127,237,442).
```

A source type `s` can precede a head type `t` exactly when

\[
                         t_1\le s_0,\qquad t_2\le s_1,             \tag{8.1}
\]

because the oldest head class and every source `C2` are nonempty
singletons in this table.  The following directed type cycles partition all
1,430 occurrences exactly:

```text
127 copies  A -> G -> H -> A
  4 copies  A -> I -> H -> A
  8 copies  A -> I -> C -> H -> A
297 copies  B -> I -> B
 20 copies  D -> D
 20 copies  E -> F -> E
120 copies  F -> F
 98 copies  H -> H
133 copies  I -> I.
```

Every displayed arrow satisfies (8.1), and direct row/column summation gives
the required multiplicity of every type on both shores.  Equivalently, the
type compatibility graph has an integral perfect matching, indeed a cycle
cover with components of length at most four.

This removes type Hall and type divisibility from the functional-owner
programme.  The first unsolved positive statement is genuinely labelled:
realize these small type-cycle packets while using every rooted named lower
flag and every owner once.  The current frozen GKS factor fails precisely at
this labelled step (it has dead predecessor roots despite satisfying the
same type census).

The same conclusion holds asymptotically for the canonical Ferrers demand.
The exact aggregate semigroup theorem in
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`
decomposes the demand, for every `k>=31`, into uniform short, long and mixed
rotor packages.  Forgetting labels, every such package is a directed cycle
of compatible age compositions.  Their disjoint union is therefore a
one-in/one-out cycle cover on exactly `W` anonymous type occurrences.

This does **not** contradict the primitive labelled-lift obstruction in that
theorem: an anonymous two-state type cycle need not lift on one copy of its
coordinate labels.  It proves only that the functional-owner programme has
no aggregate type or divisibility obstruction for all sufficiently large
dimensions.  Named-target/owner colouring is the first possible
obstruction.

For computation this gives a smaller exact search face than a free
1,430-state cycle cover: prescribe the nine aggregate cycle-package counts
above and search only their literal labelings, with palette-neutral flag
switches supplying the named suffix resources.  A success is automatically
in the one-regular functional-attachment balanced subclass of Theorem 2.1.

### 8.1 Minimal connected repair of the short-cycle inventory

The preceding inventory has three weak type components: `{D}`, `{E,F}` and
the main component.  It is therefore suitable for the owner/flag
**cycle-cover** gate but cannot itself support one Hamilton chronology.
Two legal transportation switches, the minimum possible number for three
components, repair this without changing any type margin:

\[
\begin{aligned}
 (D,D)+(H,H)&\longmapsto(D,H)+(H,D),\\
 (E,F)+(H,H)&\longmapsto(E,H)+(H,F).                \tag{8.2}
\end{aligned}
\]

All four new arcs satisfy the survivor inequalities (8.1).  The changed
rows of the connected pair-count matrix are

```text
D: D19, H1
E: F19, H1
H: A139, D1, F1, H96
```

and every other row remains as in the displayed short-cycle inventory.
Column sums are still the nine certified masses.  The support is now
strongly connected: `D<->H`, while `H->F->E->H` joins the second old
component to the main one.  Hence the repaired abstract type multigraph has
an Euler circuit of length 1,430.

The optional exact SAT face

```text
scratch/build_k17_incidence_bimatching_age_skeleton_20260801.cpp
  --type-cycle-connected
```

encodes precisely this connected inventory, while `--type-cycle` retains
the original three-component calibration.  The independent decoder
`scratch/verify_k17_incidence_bimatching_age_model_20260801.cpp` recomputes
the selected source/head type census from the literal `D,H` incidences.
Neither mode includes upper-shadow rows.

### 8.2 Corrected fixed-inventory audit: the triangle dies, a clean `C5`
survives

The raw determinant-two triangle (4.1) does **not** lie in the connected
fixed inventory.  The authenticated flag file uses one-based types
`A=1,...,I=9`; packets `285,919,927` have types `H,G,G`.  Hence the three
triangle atoms have type pairs

\[
                         H\to G,\quad H\to G,\quad G\to G.       \tag{8.3}
\]

All three corresponding entries of the connected pair-count matrix are
zero.  An exhaustive support audit finds no strong `C3` after imposing that
inventory.  This correction is important: the raw triangle proves the full
flag matrix nonbalanced, but it is not an obstruction on the fixed-inventory
face.

The connected face is nevertheless nonbalanced.  It contains the following
zero-holonomy clean `C5`:

```text
rows:
  tail49, head182, owner7485, tail1407, head109

atoms:
  (49,109,5621)    G->H
  (49,182,3453)    G->H
  (483,182,7485)   H->H
  (1407,139,7485)  C->H
  (1407,109,21749) C->H
```

Every displayed type arc has positive connected-inventory capacity.  The
five-by-five incidence minor is the odd cycle matrix, so its determinant has
absolute value two.  Its holonomy is zero, hence it lifts to 17 disjoint
physical `C5`s.  Thus fixing all 81 aggregate pair counts still does not make
the named-label master TU or balanced.

This is the first exact named obstruction on the connected face.  The
compact model correctly keeps the `D,H`, age, suffix and pair variables
integral; a linear transportation relaxation cannot be promoted to a proof.

## 9. The connected inventory has a complete symmetric fractional lift

The determinant-two obstruction is integral only.  The connected inventory
of Section 8.1 has a fractional realization satisfying owners, roots,
literal age recurrence and every named lower marginal simultaneously.

### Theorem 9.1 (fixed-inventory fractional realization)

On the full physical `k=17` layer, there is a fractional circulation with
the connected type-pair counts of Section 8.1 such that:

1. every rank-nine owner has source and head load one;
2. every rank-eight root has load one;
3. every required suffix target of ranks two through seven has load one;
4. every positive transition satisfies literal depth-three age recurrence.

It descends equivariantly to the `Z_17` quotient.

#### Proof

Fix an oriented Johnson owner edge

\[
 T\longrightarrow U,qquad
 T-U=\{\alpha\},\quad U-T=\{\beta\}.                \tag{9.1}
\]

For a permitted source/head type pair `s->t`, fix `C3={alpha}`.  Partition
the common eight-set into source classes `C0,C1,C2` of sizes
`s0,s1,s2`.  Choose

\[
 D_1\subseteq C_0,\ |D_1|=t_1,\qquad
 D_2\subseteq C_1,\ |D_2|=t_2,\qquad
 D_3\subseteq C_2,\ |D_3|=1,                       \tag{9.2}
\]

and put

\[
 D_0=\{\beta\}\ \dot\cup\
      (C_0-D_1)\ \dot\cup\ (C_1-D_2)\ \dot\cup\ (C_2-D_3). \tag{9.3}
\]

The survivor inequalities guarantee that (9.2) is possible.  Since both
types sum to nine,

\[
 |D_0|=1+(s_0-t_1)+(s_1-t_2)+(s_2-1)=t_0.          \tag{9.4}
\]

Thus (9.2)--(9.3) is exactly one literal age transition.

For a fixed oriented edge and type pair, the symmetric group on the common
eight coordinates acts transitively on the source partitions and on the
head partitions (with `alpha,beta` fixed), and preserves compatibility.
The compatibility bipartite graph is therefore biregular.  Put its uniform
edge measure on that edge; after normalization it couples the uniform
probability measures on the two (not necessarily equally sized) partition
shores.

Now use every oriented Johnson owner edge uniformly and give type pair
`s->t` total quotient mass equal to its integer count `a_st`.  There are
`72=9*8` outgoing and incoming owner edges at every physical owner, while

\[
                     \sum_t a_{st}=b_s=\sum_t a_{ts}. \tag{9.5}
\]

Hence every owner has the required unit source/head load and type marginal.
Uniformity in the deleted coordinate gives every rank-eight root unit load.

Finally average over all coordinate permutations.  The number of suffix
slots at every rank `2,...,8` equals the number of physical targets at that
rank by the certified type census.  Transitivity of the symmetric group on
each rank therefore makes the load of every named target exactly one.  All
steps commute with cyclic rotation, so the construction descends to the
free `Z_17` quotient.  `square`

Theorem 9.1 proves that the compact connected-inventory master has no
fractional Hall or chronology separator.  Together with the clean `C5` in
Section 8.2, it locates the first possible failure exactly: one-copy
integral colouring of the owner/root/suffix resources.  A SAT `UNSAT` result
for the audited compact model would therefore be a genuine nonnormality
theorem for this fixed inventory, not a rank-count or fractional-flow
obstruction.

## 10. Exact odd-cycle parity and a one-portal absorber

The surviving determinant-two `C5` is not itself an exact parity
obstruction.  The right invariant and its minimal escape are elementary.

### Lemma 10.1 (odd-row portal necessity)

Let `R` be the resource-row set of a clean odd cycle in a hypergraph
incidence matrix.  If a matching `M` saturates every row of `R`, then `M`
contains an atom `e` for which

\[
                              |e\cap R|\quad\hbox{is odd}.       \tag{10.1}
\]

#### Proof

Since `M` is a matching saturating `R`, every row of `R` occurs in exactly
one selected atom.  Therefore

\[
                         \sum_{e\in M}|e\cap R|=|R|.             \tag{10.2}
\]

The right side is odd.  Hence not every summand on the left can be even.
`square`

The cycle atoms themselves meet `R` in exactly two rows.  Thus a matching
confined to them cannot saturate an odd `R`; some **odd portal** is necessary.

### Lemma 10.2 (one-portal absorption of a clean odd cycle)

Let `R` be the rows of a clean `C_{2l+1}`.  Suppose there is an atom `g`
meeting `R` in exactly one row `r`, and suppose `g` is resource-disjoint from
the `l` alternating cycle atoms which cover the path `R-r`.  Then these
`l+1` atoms are a matching saturating `R`.

#### Proof

Deleting `r` from the row cycle leaves an even path.  Its alternating cycle
atoms are pairwise resource-disjoint and cover every remaining cycle row
once.  By hypothesis `g` is disjoint from them and covers the one omitted
row.  `square`

The authenticated connected-inventory `C5` has exactly such a portal:

```text
portal row: head109

selected matching atoms:
  (57,109,5621)    H->H   [one-row portal]
  (49,182,3453)    G->H   [cycle atom]
  (1407,139,7485)  C->H   [cycle atom]
```

The three atoms are fully resource-disjoint and cover the five displayed
cycle rows exactly once.  All three type arcs have positive capacity in the
connected inventory.  Consequently the `C5` is a genuine non-TU witness but
not a local exact-matching obstruction: one permitted portal kills its
parity defect.

### Lemma 10.3 (orbitwise portal lift)

Let a free cyclic quotient contain a zero-holonomy clean odd cycle and a
one-portal absorber as in Lemma 10.2.  If the absorber atoms use distinct
quotient resource orbits, then all cyclic translates of the absorber form a
physical matching saturating every row in the complete lifted cycle orbit.

#### Proof

Zero holonomy makes the lift a disjoint union of one cycle for each initial
phase.  Rotating one absorber through every phase uses every physical vertex
of each quotient resource orbit exactly once.  Distinct quotient resource
orbits never collide.  Hence the translated absorbers are mutually
resource-disjoint and saturate all lifted cycle rows.  `square`

The authenticated three-atom absorber satisfies the hypothesis.  Its
physical phase incidences are

```text
(57,109,5621):    tail 0, head 0, owner 0
(49,182,3453):    tail 0, head 0, owner 0
(1407,139,7485):  tail 0, head 8, owner 8
```

and its nine quotient resource orbits are distinct.  Therefore its 17
rotates are 51 pairwise resource-disjoint physical atoms saturating all 85
rows of the 17 lifted `C5`s.  The entire authenticated odd-cycle orbit, not
just one representative, is exactly absorbable.

### Theorem 10.4 (prepared portal-core rounding)

Let `H` be a three-partite three-uniform turn hypergraph with equal shore
sizes.  Suppose `P` is a matching of prepared portal atoms.  Delete the
three vertices of every atom of `P` and all incident atoms, obtaining `H'`.
If

1. the incidence matrix of `H'` is balanced, and
2. `H'` has a fractional perfect matching,

then `H` has a perfect matching containing `P`.

#### Proof

The packing polytope of a balanced incidence matrix is integral.  A
fractional perfect matching of `H'` has objective value `|V(H')|/3`, the
largest possible value of a matching in a three-uniform hypergraph.  Hence
an integral optimum has that same cardinality and saturates every residual
vertex.  Its union with `P` is a perfect matching of `H`.  `square`

This is the exact portal analogue of Theorem 5.1.  Theorem 5.1 deletes a
fractionally light bad-atom transversal and rounds what remains; Theorem
10.4 first commits to a resource-disjoint odd portal system and rounds the
residual balanced core.  Either route is sufficient.  For the chronology
problem the latter may be more natural, because the authenticated `C5`
absorber already consumes allowed type arcs rather than forbidding them.

### Theorem 10.5 (short Boolean odd cycles always have a portal)

Work in the unrestricted physical Boolean turn hypergraph on rank-`m` roots
and rank-`m+1` owners.  Let `R` be a clean `C_{2l+1}` and choose a row `r`
such that the `l` alternating cycle atoms covering `R-r` are already a
matching.  If

\[
                                  3l\le m,                         \tag{10.3}
\]

then this alternating path has a one-row portal and hence an exact absorber.

#### Proof

Every resource row has exactly `m(m+1)` incident Boolean turn atoms.  Fixing
the row `r`, any one foreign resource row forbids at most `m` of them:

* a foreign row on the same shore forbids none;
* a foreign root on the opposite shore fixes at most one neighbour;
* a foreign owner (or, with `r` an owner, a foreign root) leaves at most `m`
  choices.

The `l` alternating atoms are resource-disjoint and avoid `r`, so their
resource union has size `3l`.  By the union bound it forbids at most
`3lm\le m^2` atoms incident to `r`, strictly fewer than `m(m+1)`.  Choose an
incident atom outside that union.  It meets `R` only in `r` and is disjoint
from all alternating path atoms.  Lemma 10.2 applies.  `square`

Thus every fixed-length linear odd cycle is locally absorbable for all
sufficiently large ranks in the full Boolean catalogue.  A genuine
obstruction must come from one of three global effects: flag restrictions
delete the portals, many cycles compete for the same portal resources, or
the aggregate type quotas cannot accommodate all selected portals.  This
is exactly why the remaining statement is a *simultaneous prepared portal*
theorem rather than another parity lemma.

The proof also gives a flag-restricted criterion.  If a retained turn
support has row degree `delta` and inherits the Boolean pair-codegree bound
`m`, then the same cycle is absorbable whenever

\[
                                  \delta>3lm.                     \tag{10.4}
\]

In particular, every positive-density flag support absorbs every bounded
odd cycle once `m` is large.  Therefore a failure of portal absorption must
be caused by sparse/fibre-rigid flags or by global competition, not by a
bounded cycle in a dense retained core.

### Theorem 10.6 (global portal-Hall sufficient condition)

Let `S` be a set of resource rows meeting every strong odd cycle of a
three-partite turn hypergraph `H`.  For each `s in S`, let `L_s` be a list of
prepared absorber packets.  A packet is itself a matching of turn atoms, it
saturates `s`, and it uses at most `p` resource vertices.  Suppose that for
every `J subseteq S`,

\[
 \nu\!\left(\bigcup_{s\in J}L_s\right)>
                            p(|J|-1),                             \tag{10.5}
\]

where the matching number is taken in the resource hypergraph whose edges
are whole packets.  Then there are pairwise resource-disjoint packets
`P_s in L_s`, one for every `s in S`.

Let `P` be their union and delete all resources used by `P`, obtaining
`H_P`.  If the fractional matching number of `H_P` is at least

\[
                         n_P-C,                                  \tag{10.6}
\]

where `n_P` is one residual shore size, then `H` has a matching of
deficiency at most `C`.  In particular, `C=0` gives a perfect matching.

#### Proof

Pad packets by private dummy vertices to make the packet hypergraph
`p`-uniform.  Condition (10.5) is the Aharoni--Haxell rainbow-matching
criterion, so it selects one disjoint packet from every colour `s`.  Since
every odd cycle meets `S` and every row of `S` is deleted, the incidence
matrix of `H_P` is balanced.  Its packing polytope is integral, so its
integral matching number equals its fractional matching number and is at
least `n_P-C`.  Add the fixed packet matching `P`.  `square`

For the natural anchored portal lists, (10.5) is usually **impossible**.
Every packet in `L_s` contains the same designated row `s`, so a matching in
their union uses at most one packet from each list and therefore

\[
                 \nu\!\left(\bigcup_{s\in J}L_s\right)\le |J|. \tag{10.6a}
\]

For packet rank `p>=3` and `|J|>=2`, this cannot exceed the
Aharoni--Haxell threshold `p(|J|-1)`.  That theorem is a correct sufficient
condition only after a different, unanchored packet encoding; it cannot
certify the canonical anchored portal lists.  The list-versus-conflict
criterion below is the relevant one here.

There is also a simple list-versus-conflict sufficient condition for the
rainbow step.  If every list has size at least `L`, every packet conflicts
with at most `Delta` packets in all other lists, and

\[
                         e(2L\Delta+1)<L^2,                       \tag{10.7}
\]

then the Lovasz local lemma selects one conflict-free packet from every
list.  Indeed a conflicting-pair event has probability `L^{-2}` and depends
on at most `2L Delta` other such events.  Thus either (10.5) or (10.7), plus
the residual fractional bound (10.6), is a concrete global theorem turning
the local portal construction into exact or constant-defect rounding.

For comparison, the deletion route of Theorem 5.1 is even shorter: an atom
set `Z` meeting every odd cycle and satisfying `x(Z)<C+1` under one
fractional perfect matching already gives deficiency at most `C`.  The two
sharp global targets are therefore

\[
\boxed{\text{light odd-cycle deletion transversal}}
\quad\text{or}\quad
\boxed{\text{portal-packet rainbow matching + residual fractional Hall}}.
\tag{10.8}
\]

This result is deliberately local.  It does not prove that portals for all
odd cycles can be chosen simultaneously, nor that their use respects every
global type quota.  It sharpens the remaining theorem to the following.

> **Prepared odd-cycle portal theorem.**  Starting from the symmetric
> fractional lift of Theorem 9.1, choose a bounded-mass set of permitted odd
> portals whose deletion/activation meets every strong odd cycle and whose
> alternating cycle-path completions are mutually resource-compatible.

Equivalently, the needed theorem is not “the connected support is balanced”
(it is not), and it is not a raw parity impossibility (the authenticated
`C5` is portal-absorbable).  It is a simultaneous integral portal-packing
theorem.  Combined with Theorem 5.1, any construction placing all residual
odd-cycle mass below one would already force a perfect flag matching.

## 11. Audit artifacts and hashes

The bounded support audit was compiled with `g++ -std=c++20 -O3` and run on
the H100 CPU against the authenticated switched-GKS turn and flag tables.
It independently checks the raw `C3`, the raw and connected zero-holonomy
`C5`s, the connected-inventory type filter, and the exact one-portal cover.

```text
scratch/audit_k17_turn_hypergraph_balancedness_20260801.cpp
scratch/k17_turn_hypergraph_balancedness_20260801.audit.txt
```

```text
fa6598d1b1371c874dd64067166ece708da70cc3ee38dcb34d337fda2a876651  audit source
f84e4334da87f7ed4ca9f265cfb9bb8900612a41863fda2318c7b34a17eba4dd  audit transcript
6b417b8413afb915ad03becec0154927f2a659642d26bfdae8bdd80eb909f7b9  turn TSV input
908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451  flag TSV input
```

## 12. Quantitative portal lists: what closes and the first flag-rigidity term

Write the odd dimension as `k=2m+1`; roots have rank `m` and owners rank
`m+1`.  Suppose there are `h` portal tasks.  Task `i` is based on a clean
`C_(2l_i+1)`, with `l_i<=l`, and its alternating path atoms have already
been fixed.  Assume all these path matchings and all designated portal rows
are mutually resource-disjoint.  Put

\[
                              b_h:=h(3l+1).                       \tag{12.0}
\]

For the list at one designated row, the other fixed resources to avoid are
contained in a bank of size at most `b_h`.  One completed absorber uses

\[
                         p_i=3(l_i+1)\le p:=3(l+1)               \tag{12.1}
\]

resource vertices.

### 12.1 Full Boolean catalogue

Every resource row has degree

\[
                              D_{\rm raw}=m(m+1),                \tag{12.2}
\]

and every pair of resource rows has codegree at most `m`.  The union of the
fixed alternating paths and designated rows has size at most `b_h`.
Therefore the portal list at any designated row, after avoiding the whole
fixed bank, has size

\[
                         L_{\rm raw}\ge m(m+1-b_h).              \tag{12.3}
\]

Because all lists have already avoided the fixed bank, two completed
packets can now conflict only through their variable one-atom portals.  A
portal has three resources, each contained in at most `m` candidates of
another list.  Hence

\[
                         \Delta_{\rm raw}\le3m(h-1).             \tag{12.4}
\]

For fixed `h` and `l=O(d)=O(sqrt(m))`, (12.3)--(12.4) give

\[
 {L_{\rm raw}\over\Delta_{\rm raw}}=\Omega(m/h)\longrightarrow\infty.
                                                                    \tag{12.5}
\]

In particular the local-lemma inequality (10.7) holds for all sufficiently
large `m`.  Thus **portal competition itself closes asymptotically in the
full Boolean catalogue** for a bounded task bank, even when each local odd
cycle has length `O(d)`.

The Aharoni--Haxell union condition does not close: every anchored list has
a common row, so (10.6a) gives union matching number at most `|J|`.  This is
an exact structural failure of that sufficient theorem, not a shortage of
raw portal atoms.

### 12.2 Conditional resource-separated singleton-terminal star

The canonical all-high rotor and the connected `k=17` inventory use
singleton oldest classes on the relevant turns.  The following count is for
the **complete prospective resource-separated star**: all indicated
successor flags are retained as alternative columns and different
`(beta,gamma)` pairs are treated as different turn resources.  This is a
local design hypothesis, not a property proved after one named flag per
owner has been frozen.

Fix a source labelled state

\[
       X=(C_0,\ldots,C_d),\qquad |C_d|=1,\quad a:=|C_{d-1}|,    \tag{12.6}
\]

and a legal successor type whose oldest class is also a singleton.  Put
`T=union C_i`, let `alpha` be the unique member of `C_d`, and use the tail
root `p=T-{alpha}`.

In the complete prospective labelled catalogue a distinct turn support is
specified by

* `beta notin p`, giving next owner `U=p+{beta}` (`m+1` choices), and
* `gamma in C_(d-1)`, giving head root `q=U-{gamma}` (`a` choices).

The other survivor classes can be filled because the type transition is
legal.  Under the resource-separation hypothesis, different pairs
`(beta,gamma)` give different resource triples.  Consequently the distinct
prospective turn degree and its pair-codegree are

\[
                       D_{\rm star}=a(m+1),\qquad
                       \gamma_{\rm star}\le a.                  \tag{12.7}
\]

If quotient owner self-loops are forbidden, the choice `beta=alpha` is
removed and `a(m+1)` is replaced by `am`; every asymptotic conclusion below
is unchanged.

After avoiding the same `b_h`-resource fixed bank,

\[
 L_{\rm star}\ge a(m+1-b_h),\qquad
 \Delta_{\rm star}\le3a(h-1).                                  \tag{12.8}
\]

Therefore a complete resource-separated singleton-terminal star also
satisfies (10.7) for fixed `h` and `l=O(d)`.  The missing factor `m` relative
to the raw Boolean degree is **not** fatal: it cancels from the codegree as
well.  What remains open is precisely whether the named lower-exact flag
selection can retain such a separated star.

### 12.3 The first unproved density is after named flags are frozen

Let `F` be a one-copy owner/target flag selection and let
`P_F(r)` be the set of resource-distinct prospective turns retained at a
root row `r`.  Define its robust portal degree

\[
\delta_F(b)=
   \min_{r}\ \min_{B\subseteq V-\{r\}:\ |B|\le b}
       |\{e\in P_F(r):e\cap B=\varnothing\}|,                    \tag{12.9}
\]

and let `gamma_F` be the maximum pair-codegree in this retained support.
The preceding list calculation gives the exact sufficient inequality

\[
 e\bigl(2L\,[3\gamma_F(h-1)]+1\bigr)<L^2,qquad
 L:=\delta_F(b_h).                                                \tag{12.10}
\]

For example, the robust flag theorem

\[
        \delta_F(b_h)\ge\alpha m,\qquad \gamma_F\le K           \tag{12.11}
\]

with absolute `alpha,K>0`, bounded `h`, and `l=O(d)`, would make portal
selection automatic for large `m`.

No current theorem proves (12.11).  The symmetric fractional lift of
Theorem 9.1 averages over many labelled partitions and may use a different
partition for every outgoing arc; it does not furnish one named flag per
owner with linear robust degree.  Freezing exact suffix targets can collapse
the prospective `(beta,gamma)` rectangle to a singleton or to the empty set.

The authenticated switched-GKS `k=17` table shows that this is a real
phenomenon, although only for that finite frozen table.  After imposing the
connected type inventory, its audited support has

```text
connected atoms                         1932
tail degrees: zero/min/max/sum          801 / 0 / 9 / 1932
head degrees: zero/min/max/sum          704 / 0 / 7 / 1932
maximum resource-pair codegree          6
```

Thus even positive retained degree fails on hundreds of rows.  This audit
does **not** constrain the separate owner-only SAT master, which selects new
flags from the full incidence atlas.

### Corollary 12.1 (exact conditional additive-constant implication)

Fix constants `h_0,A,alpha,K,C`.  Suppose that for every sufficiently large
odd dimension the already upper-safe/resident chronology construction
exports a turn hypergraph and at most `h<=h_0` odd-cycle tasks with the
following properties.

1. Each task has `l_i<=A d` and a fixed alternating path matching; all path
   resources and designated portal rows are mutually disjoint.
2. For `b_h=h(3 max_i l_i+1)`, its frozen named flags satisfy

   \[
             \delta_F(b_h)\ge\alpha m,qquad \gamma_F\le K.      \tag{12.12}
   \]

3. Deleting the resources of any conflict-free complete packet choice
   removes every strong odd cycle, and the residual fractional matching
   number is at least `n_P-C`.

Then, for all sufficiently large `m`, the terminal turn matching has
deficiency at most `C`.  If `C=0`, it is exact.  If the exported upper and
residence gates are the ones in the serial terminal theorem, the resulting
word has length at most `B(k)+C` (plus any separately declared fixed physical
charge).

#### Proof

Truncate every portal list to

\[
                               L=\lfloor\alpha m\rfloor.
\]

After the fixed resource bank has been excluded, a packet conflicts with at
most three portal resources, and each has codegree at most `K` in each of
the other `h-1` lists.  Thus

\[
                              \Delta\le3K(h_0-1).                 \tag{12.13}
\]

Since `L` tends to infinity while `Delta` is constant,
`e(2L Delta+1)<L^2` for all sufficiently large `m`.  The local lemma selects
one resource-disjoint packet per task.  Hypothesis 3 leaves a balanced
residual support with fractional deficiency at most `C`; balanced-matrix
integrality gives an integral residual matching with the same bound.
Theorem 10.4 and the established terminal-deficiency conversion finish the
claim.  `square`

This is the exact `O(1)` bridge furnished by the portal method.  It is
conditional only on bounded task birth, the robust frozen-flag estimate
(12.12), and residual fractional Hall.  Aharoni--Haxell is not the engine:
common anchors force its union matching number below its hypothesis by
(10.6a).  The LLL works because it uses large *coloured lists* directly.

### 12.4 Quantitative verdict

The desired `L=Omega(m^2), Delta=O(md)` estimate is true in the full Boolean
catalogue, and the weaker conditional resource-separated
`L=Omega(m), Delta=O(d)` singleton-terminal estimate already suffices for
bounded tasks.  The additive-constant implication still
does not close, because two independent global statements remain unproved:

1. **bounded task birth:** only `h=O(1)` odd-cycle/portal tasks with
   `l=O(d)` must survive the recursive construction; and
2. **robust named-flag degree:** the selected one-copy lower-exact flags must
   satisfy a bound such as (12.11), while leaving residual fractional
   deficiency `O(1)` after the chosen packets are fixed.

The first flag-rigidity term is therefore exactly `delta_F(b_h)`.  Aggregate
age circulation, owner symmetry, and raw terminal-star degree do not lower-
bound it.  Proving (12.11), or replacing it by a direct robust common-cap
Hall theorem, is the first missing quantitative step.
