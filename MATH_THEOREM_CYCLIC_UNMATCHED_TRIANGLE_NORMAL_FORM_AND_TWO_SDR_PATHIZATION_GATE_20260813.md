# Cyclic unmatched triples give a three-choice two-colour pathization gate

**Date:** 2026-08-13  
**Status:** unconditional normal form, finite two-SDR certificates through
`r=7`, and an all-`r>=14` capacity no-go for this restricted family

## 0. Outcome

Put `n=2r-1` and

\[
 \mathcal L={ [n]\choose r-1},\qquad
 \mathcal M={ [n]\choose r},\qquad
 \mathcal U={ [n]\choose r+1}.
\tag{0.1}
\]

There is a canonical three-choice family of Johnson diamonds over every
upper colour `U in \mathcal U`.  Its complete geometry has the following
normal form.

* Every candidate is an oriented edge between two canonical owners
  `tau(L)` indexed by lower colours `L in \mathcal L`.
* The three candidates over one `U` form a directed triangle on three
  lower labels.
* Selecting one side per triangle with pairwise distinct tails and
  pairwise distinct heads automatically gives every upper colour once,
  pairwise distinct lower colours, and middle degree at most two.
* If the selected directed graph has no directed cycle, the physical
  Johnson graph is a linear forest with exactly `Cat_r` components.

Thus the restricted family has a literal sparse three-choice target:

> choose one arc from every canonical directed triangle so that selected
> tails and heads are both injective and no directed cycle is selected.

This is stronger and much more structured than an arbitrary occurrence
hypergraph.  Exact SAT verifies it for `2<=r<=7`; the first SAT model is
already acyclic in every tested case.  However, the exact degree law below
implies that **no degree-two selector exists in this family for any
`r>=14`**.  The family is therefore a useful small-parameter bridge and
normal form, not an all-parameter solution.

## 1. Cyclic cancellation

Represent a set by its cyclic binary membership word, with `0` an opening
symbol and `1` a closing symbol.  Cyclically cancel noncrossing `01` pairs.
Since an upper word `U in \mathcal U` has three more ones than zeros,
exactly three ones remain unmatched.  Write them in cyclic order as

\[
 f_0,f_1,f_2.
\tag{1.1}
\]

Cutting immediately before `f_0`, the word has the unique form

\[
 U=1_{f_0}P_0\,1_{f_1}P_1\,1_{f_2}P_2,
\tag{1.2}
\]

where every `P_i` is a Dyck word (possibly empty).  Indices below are
modulo three.

For each `i`, define

\[
 L_i(U)=U-\{f_i,f_{i+1}\}\in\mathcal L,
\tag{1.3}
\]

and the oriented Johnson edge

\[
 e_i(U):
 L_i+f_i\longrightarrow L_i+f_{i+1}.
\tag{1.4}
\]

The edge has lower colour `L_i` and upper colour `U`.

## 2. The canonical lower-to-owner map

Every lower word `L in \mathcal L` has one more zero than one.  Cyclic
`01` cancellation therefore leaves a unique zero; call it `z(L)`.  Define

\[
 \tau(L)=L+z(L).
\tag{2.1}
\]

### Lemma 2.1 (well-defined canonical owner)

For every candidate presentation `L=L_i(U)`, one has `z(L)=f_i`.  The map

\[
 \tau:\mathcal L\longrightarrow\mathcal M
\tag{2.2}
\]

is injective.

#### Proof

In the cyclic factorization `(1.2)`, deleting `f_i,f_(i+1)` and cutting at
`f_i` leaves the deficit-one rooted word

\[
 0_{f_i}P_i\,0_{f_{i+1}}P_{i+1}\,1_{f_{i+2}}P_{i+2}.
\tag{2.3}
\]

All three displayed `P` blocks cancel internally, and the displayed
`0_(f_(i+1))...1_(f_(i+2))` pair cancels around `P_(i+1)`.  The only
survivor is the first zero `f_i`.  Hence `z(L_i)=f_i`.

More generally, changing the unique unmatched zero `z(L)` to one preserves
all old cyclic matched pairs and leaves `z(L)` as the unique unmatched one
of `tau(L)`.  Thus the inverse map changes the unique unmatched one of a
middle word back to zero.  This proves that `tau` is injective (indeed
bijective). \(\square\)

The image misses exactly

\[
 |\mathcal M|-|\mathcal L|=0,
\tag{2.4}
\]

because the two layers have equal cardinality on an odd ground.  Thus
`tau` is in fact a bijection.

### Lemma 2.2 (directed triangle normal form)

For every `U` and `i`,

\[
 e_i(U):\tau(L_i(U))\longrightarrow\tau(L_{i+2}(U)).
\tag{2.5}
\]

Consequently the three candidates over `U` are the sides of the directed
triangle

\[
 L_0\longrightarrow L_2\longrightarrow L_1
 \longrightarrow L_0
\tag{2.6}
\]

after transporting owners through `tau`.

#### Proof

The tail identity is `(2.1)`.  Also

\[
 L_{i+2}=U-\{f_{i+2},f_i\},
\]

whose distinguished surviving zero is `f_(i+2)`.  Hence

\[
 \tau(L_{i+2})=L_{i+2}+f_{i+2}=U-f_i
 =L_i+f_{i+1},
\]

which is the head in `(1.4)`. \(\square\)

## 3. Exact selector theorem

Let `\mathcal T_r` be the directed graph on vertex set `\mathcal L` whose
arcs are the three arcs `(2.6)` for every `U in \mathcal U`, with each arc
remembering its upper label `U`.

### Theorem 3.1 (two-SDR selector implies a Catalan linear forest)

Suppose one arc `a(U)->b(U)` is selected from the triangle belonging to
each `U`, and suppose

\[
 U\mapsto a(U)\quad\hbox{and}\quad U\mapsto b(U)
\tag{3.1}
\]

are both injective.  Then the corresponding physical edges

\[
 \tau(a(U))\tau(b(U))
\tag{3.2}
\]

have all of the following properties.

1. Every upper colour occurs exactly once.
2. The lower colours `a(U)` are pairwise distinct.
3. Every middle owner has degree at most two.
4. Every component is a path or a cycle.

If the selected directed arcs contain no directed cycle, the physical
graph is a linear forest.  It then has exactly

\[
 |\mathcal M|-|\mathcal U|=\operatorname {Cat}_r
\tag{3.3}
\]

components, counting isolated owners.

#### Proof

The upper and lower claims follow from construction.  Injectivity of
`tau`, together with the two injections in `(3.1)`, gives indegree and
outdegree at most one at every physical owner, hence total degree at most
two.

In a finite directed graph with indegree and outdegree at most one, an
undirected cycle is necessarily a directed cycle: every vertex on the
cycle must use one incoming and one outgoing cycle edge.  Thus absence of
directed cycles is equivalent to the physical graph being a linear
forest.  It has `|\mathcal M|` vertices and `|\mathcal U|` edges, so Euler's
forest identity gives `(3.3)`. \(\square\)

This theorem deliberately uses the stronger two-SDR condition.  Middle
degree at most two alone can allow two heads at an owner which is not a
tail; that weaker condition does not give the clean permutation model.

## 4. Exact candidate-degree law

The sparse system has an exact plane-tree degree interpretation.

### Theorem 4.1 (root-degree law)

For `L in \mathcal L`, cut its cyclic word at its unique unmatched zero
`z(L)` and delete that zero.  The remaining word `D(L)` is a Dyck word of
semilength `r-1`.  The number `d(L)` of upper triangles containing `L` is
the number of top-level primitive components of `D(L)`, equivalently the
root degree of its rooted plane tree.

Consequently, for `1<=j<=r-1`,

\[
 \boxed{
 |\{L:d(L)=j\}|=(2r-1){j\over 2r-2-j}
 {2r-2-j\choose r-1}.}
\tag{4.1}
\]

#### Proof

Write the rooted lower word as

\[
 0_{z(L)}D.
\tag{4.2}
\]

An upper candidate containing `L` must change `z(L)` and one further zero
to ones.  It is a candidate of Section 1 exactly when that further zero is
the opening `0_y` of one top-level primitive component

\[
 D=A\,(0_yQ1_x)\,B,
\tag{4.3}
\]

where `A,B,Q` are Dyck words (with `A,B` allowed to have several primitive
components).  Indeed the resulting upper word is

\[
 1_{z(L)}A\,1_yQ\,1_xB,
\]

so its three cyclic unmatched ones are precisely `z(L),y,x`, and deleting
the first two recovers `L`.  Conversely the normal form `(1.2)--(2.3)`
identifies such a primitive component for every incident upper triangle.
This proves the degree interpretation.

There are `2r-1` choices of the unmatched-zero position for every Dyck
word `D`, and this gives every lower word exactly once.  If `m=r-1`, the
generating function for Dyck words with exactly `j` primitive components
is

\[
 (zC(z))^j,
\]

where `C(z)=1+zC(z)^2`.  Lagrange inversion gives

\[
 [z^m](zC(z))^j
 ={j\over2m-j}{2m-j\choose m}.
\]

Multiplication by `2r-1` proves `(4.1)`. \(\square\)

In particular, every lower label occurs in at least one candidate and the
degree-one population is

\[
 (2r-1)\operatorname {Cat}_{r-2}.
\tag{4.4}
\]

This large leaf bank explains the finite positive behavior, but the high
root-degree tail eventually overwhelms the one-omission-per-triangle
budget.

### Theorem 4.2 (capacity no-go from `r=14` onward)

No choice of one candidate edge from every upper triangle can have middle
degree at most two when `r>=14`.  This remains true without orientation,
tail injection, head injection, or acyclicity.

#### Proof

Choosing one side of a triangle is equivalent to omitting one of its three
lower-label vertices.  If a lower label `L` lies in `d(L)` triangles, then
middle degree at most two forces it to be omitted in at least

\[
 (d(L)-2)_+
\tag{4.5}
\]

of them.  Since every upper triangle omits exactly one label, a necessary
condition is

\[
 R_r:=\sum_{L\in\mathcal L}(d(L)-2)_+\le |\mathcal U|.
\tag{4.6}
\]

Every triangle contributes three incidences, so

\[
 \sum_Ld(L)=3|\mathcal U|,
 \qquad \sum_L1=|\mathcal L|=:W.
\]

Only the `d=1` term differs between `(d-2)_+` and `d-2`; by `(4.4)` its
population is `(2r-1)Cat_(r-2)`.  Therefore

\[
 R_r=3|\mathcal U|-2W+(2r-1)\operatorname {Cat}_{r-2}.
\tag{4.7}
\]

Using

\[
 {|\mathcal U|\over W}={r-1\over r+1},
 \qquad
 {(2r-1)\operatorname {Cat}_{r-2}\over W}
 ={r\over4r-6},
\tag{4.8}
\]

the slack in `(4.6)` is exactly

\[
 {|\mathcal U|-R_r\over W}
 =2-2{r-1\over r+1}-{r\over4r-6}
 ={ -r^2+15r-24\over 2(r+1)(2r-3)}.
\tag{4.9}
\]

The numerator is negative for every integer `r>=14`: at `r=14` it is
`-10`, and its difference on increasing `r` is `14-2r<0`.  Thus
`R_r>|\mathcal U|`, contradicting `(4.6)`. \(\square\)

At the first impossible value the deficit is already

\[
 R_{14}-|\mathcal U|=267444.
\tag{4.10}
\]

The obstruction is purely local owner capacity.  It says nothing negative
about the full diamond catalogue, where an upper set has many more than
the three cyclic-unmatched choices.

## 5. Exact finite evidence and reproducibility

The deterministic generator and SAT audit are

`scratch/audit_cyclic_unmatched_triangle_selector_20260813.py`.

For `2<=r<=7`, it encodes:

* exactly one of the three arcs for every upper label;
* at most one selected arc with any given tail;
* at most one selected arc with any given head.

For every tested `r`, Kissat returns SAT, and direct replay finds no
directed cycle in the first model:

\[
\begin{array}{c|r|r|c|c}
r&|\mathcal U|&\text{variables}&
\text{selected rules }(0,1,2)&\text{directed cycles}\\ \hline
2&1&3&(0,0,1)&0\\
3&5&15&(0,1,4)&0\\
4&21&63&(1,5,15)&0\\
5&84&252&(9,21,54)&0\\
6&330&990&(35,101,194)&0\\
7&1287&3861&(143,516,628)&0
\end{array}
\tag{5.1}
\]

The checker independently verifies the requested number of distinct
lower labels, tails, and heads.  These are finite certificates only; no
pattern inferred from solver variable order is used as a theorem.

Formula `(4.1)` gives, for illustration, the distributions

\[
\begin{array}{c|l}
r&\#\{L:d(L)=j\}_{j\ge1}\\ \hline
3&5,5\\
4&14,14,7\\
5&45,45,27,9\\
6&154,154,99,44,11\\
7&546,546,364,182,65,13
\end{array}
\tag{5.2}
\]

and the full candidate digraph is strongly connected through `r=9`.
Neither observation is currently promoted to an all-`r` theorem.

## 6. The exact restricted-family conclusion

The remaining statement is now concise.

### Finite-range question 6.1 (cyclic triangle selector)

For which `2<=r<=13` do the labelled directed triangles of `\mathcal T_r`
admit one selected side per triangle such that tails and heads are both
injective and the selected digraph is acyclic?

The non-topological part is a three-choice two-SDR problem.  Equivalently,
one seeks a matching of the upper labels into directed arcs with capacity
one on each tail and each head.  Hall on only one projection is not
sufficient; the two shores are coupled by the choice of a side of the
same triangle.

The all-parameter pathization problem must enlarge the catalogue.  Two
plausible routes are:

1. add non-unmatched diamonds to the three local sides and prove a
   bounded-capacity matching theorem for the enlarged plane-tree complex;
2. use the full incidence catalogue `L subset U`, whose average lower
   degree is large, while retaining a potential that makes the selected
   owner graph acyclic.

The finite selector through `r=7` still supplies a different two-colour
owner forest at those parameters.  It cannot be extrapolated through this
three-choice family.

## 7. Scope

This note does not prove the full protected rail theorem.  It proves both
the exact appeal and the exact limitation of cyclic unmatched triples:
they reduce the second-shadow problem to a concrete Catalan selector and
solve it computationally at the first parameters, but their high-degree
plane-tree tail creates a rigorous linear-capacity obstruction from
`r=14` onward.  Any all-parameter proof must use additional diamonds.
