# One-provider collar systems: maximal intersections, sharp Helly bounds, and exact induction

Date: 2026-07-30

Status: exact abstract theorem, exact provider-choice CSP, sharp fixed-choice
Helly theorem, and two sufficient induction principles.  The S4 specialization
is literal, but no provider choice for all 69 residual S4 targets is asserted.
The K16 bracket remains

\[
12873\leq\nu(16)\leq12874.
\]

## 1. Provider model, including fixed-body contributions

Let \(\Omega\) be a finite nonempty coordinate set and let \(C\) be a finite
nonempty set of variable cells.  Cell \(p\) may receive any nonempty value

\[
\varnothing\ne A_p\subseteq D_p,
\qquad \varnothing\ne D_p\subseteq\Omega.                 \tag{1.1}
\]

There is a finite nonempty target set \({\cal T}\).  Target \(t\) has a nonempty mask
\(S_t\subseteq\Omega\) and a nonempty provider domain \({\cal P}_t\).  An
option \(e\in{\cal P}_t\) consists of

\[
e=(F_e,Q_e),\qquad F_e\subseteq\Omega,\quad Q_e\subseteq C. \tag{1.2}
\]

Here \(F_e\) is the exact OR contributed by the fixed part of the literal
interval, and \(Q_e\) is its set of variable cells.  Selecting \(e\) for
target \(t\) requires

\[
F_e\cup\bigcup_{p\in Q_e}A_p=S_t.                       \tag{1.3}
\]

A provider choice is a map \(\sigma\) with
\(\sigma(t)\in{\cal P}_t\) for every target.  It is feasible if one common
assignment \((A_p)_{p\in C}\) satisfies (1.1) and (1.3) for every selected
option.  Extra accidental witnesses are allowed: “one provider per target”
means one designated witness, not exactly one occurrence in the final word.

The downward-closed cell domain in (1.1) is essential.  Exact-rank or other
non-downward-closed cell alphabets require a different theorem.

## 2. Maximal-intersection theorem

Fix a provider choice \(\sigma\), write

\[
e_t=\sigma(t)=(F_t,Q_t),
\]

and define the maximal per-cell intersection

\[
K_p(\sigma)
=D_p\cap\bigcap_{t:\,p\in Q_t}S_t,                     \tag{2.1}
\]

where the intersection over no selected provider is \(\Omega\).

### Theorem 2.1 (maximal-intersection equivalence)

The fixed provider choice \(\sigma\) is feasible if and only if

\[
F_t\subseteq S_t\qquad(t\in{\cal T}),                  \tag{2.2}
\]

\[
K_p(\sigma)\ne\varnothing\qquad(p\in C),               \tag{2.3}
\]

and

\[
F_t\cup\bigcup_{p\in Q_t}K_p(\sigma)=S_t
\qquad(t\in{\cal T}).                                  \tag{2.4}
\]

When these conditions hold, \(A_p=K_p(\sigma)\) is feasible.  Moreover it
is the unique coordinatewise greatest feasible assignment.

#### Proof

Let \((A_p)\) be any feasible assignment.  If \(p\in Q_t\), equality (1.3)
forces \(A_p\subseteq S_t\); also \(A_p\subseteq D_p\).  Therefore

\[
A_p\subseteq K_p(\sigma)                                \tag{2.5}
\]

for every cell.  Necessity of (2.2) and (2.3) follows immediately, while

\[
S_t=F_t\cup\bigcup_{p\in Q_t}A_p
\subseteq F_t\cup\bigcup_{p\in Q_t}K_p(\sigma)
\subseteq S_t
\]

proves (2.4).  Conversely, (2.3) makes \(A_p=K_p(\sigma)\) a legal nonempty
cell value, and (2.4) gives every selected provider equality.  Inclusion
(2.5) proves coordinatewise maximality and uniqueness of the greatest
assignment. \(\square\)

Thus, after the providers have been chosen, there is no residual search over
cell values.  The canonical maximal assignment either realizes all selected
providers or proves that choice impossible.

## 3. Exact blocker form and pure provider-choice CSP

For a coordinate \(x\in\Omega\), define

\[
H_x=\{p:x\in D_p\},
\qquad
B_x(\sigma)=\bigcup_{u:\,x\notin S_u}Q_u.               \tag{3.1}
\]

Then

\[
x\in K_p(\sigma)
\quad\Longleftrightarrow\quad
p\in H_x\setminus B_x(\sigma).                         \tag{3.2}
\]

Under (2.2), condition (2.4) is equivalent to the unblocked-anchor
conditions

\[
Q_t\cap\bigl(H_x\setminus B_x(\sigma)\bigr)\ne\varnothing
\qquad(t\in{\cal T},\ x\in S_t\setminus F_t).          \tag{3.3}
\]

Condition (3.3) is the exact reproduction gate.  Failure for \((t,x)\)
means that the selected supports of targets omitting \(x\), together with
the cells whose caps omit \(x\), cover the entire selected support \(Q_t\).
For interval supports this is an ordinary interval-cover obstruction.

Theorem 2.1 eliminates the cell variables completely.  Introduce only the
provider-choice variables

\[
y_{t,e}\in\{0,1\},\qquad \sum_{e\in{\cal P}_t}y_{t,e}=1. \tag{3.4}
\]

First discard every option with \(F_e\nsubseteq S_t\), equivalently add its
one-variable forbidden clause.  There are then exactly two further kinds of
forbidden compatible partial transversals:

1. **dead-cell tuples:** selected options through one cell \(p\) whose
   target masks have empty intersection with \(D_p\);
2. **blocker-cover tuples:** a selected option \(e\in{\cal P}_t\), a bit
   \(x\in S_t\setminus F_e\), and selected options of targets omitting
   \(x\) whose supports cover \(Q_e\cap H_x\).

Forbid every inclusion-minimal tuple of these two types.  Together with
(3.4), these clauses are an exact provider-only CSP: a total choice avoids
all of them if and only if it is feasible.  This is not a relaxation; it is
just (2.3) and (3.3) with the canonical cell assignment eliminated.

## 4. Sharp fixed-choice Helly theorem and its limits

For a selected subfamily \({\cal R}\), feasibility means feasibility of
those rows alone, with the same cells and caps.  Put

\[
h=\max\left\{
1,\ \max_{p\in C}|D_p|,\ 1+\max_e|Q_e|
\right\}.                                               \tag{4.1}
\]

### Theorem 4.1 (fixed-choice \(h\)-Helly property)

If a fixed selected provider family is infeasible, some selected subfamily
of at most \(h\) providers is already infeasible.  Equivalently, a fixed
choice is feasible whenever every selected subfamily of size at most \(h\)
is feasible.

#### Proof

An invalid row with \(F_t\nsubseteq S_t\) is a one-row certificate.  If
\(K_p=\varnothing\), then for every \(x\in D_p\) choose one selected provider
through \(p\) whose target omits \(x\).  At most \(|D_p|\) chosen rows already
have empty intersection with \(D_p\).

Otherwise some selected provider \(t\) fails to reproduce a coordinate
\(x\in S_t\setminus F_t\).  For each \(p\in Q_t\cap H_x\), choose one
selected provider through \(p\) whose target omits \(x\).  Together with
provider \(t\), these at most \(1+|Q_t|\) rows still block \(x\) at every
cell of \(Q_t\), so provider \(t\) fails in the induced subsystem.
\(\square\)

Both terms in (4.1) are sharp.

* For the cell term, take \(k\ge2\), one cell with cap \([k]\), and \(k\) providers
  supported there with masks \([k]\setminus\{i\}\) and fixed contribution
  equal to their masks.  The whole intersection is empty, while deleting
  any row leaves a nonempty intersection.
* For the reproduction term, take \(q\ge1\) cells with caps \(\{x,y\}\).  A root
  provider has support all \(q\) cells, mask \(\{x,y\}\), and fixed part
  \(\{y\}\).  At cell \(i\), a singleton blocker has mask and fixed part
  \(\{y\}\).  All \(q+1\) rows are needed to erase \(x\) from the root.

For \(q\ge2\), the second example uses a laminar interval family: one root
interval and singleton children.  Hence laminarity alone supplies neither
reproduction nor a Helly number independent of maximum provider length.

For arbitrary subsets of a \(k\)-coordinate universe, the nonempty-
intersection Helly number is exactly \(k\).  Pairwise nonempty intersections
do not suffice: \(\{1,2\},\{2,3\},\{1,3\}\) intersect pairwise but have empty
total intersection.  If the caps and target masks belong to a genuinely
2-Helly set family, pairwise overlap does settle only the dead-cell gate;
the reproduction clauses (3.3) remain necessary.

Finally, this fixed-choice Helly theorem does not commute with the existential
provider choices.  Take two singleton cells and three targets with distinct
singleton masks.  Give each target the two singleton cells as options, with
fixed contribution equal to its target mask.  Every two-target subsystem is
feasible by using different cells, but the three-target system is infeasible.
Thus pairwise target-subsystem feasibility does not guarantee a common
choice, even for interval providers.

## 5. Exact laminar leaf induction

An empty selected support is feasible exactly when its fixed contribution is
the whole target; it then imposes no cell restriction and may be deleted.
After making this deletion, fix a provider choice whose distinct nonempty
supports form a laminar family
\({\cal L}\).  Providers with the same support are grouped at one node.  For
\(Q\in{\cal L}\), let

\[
G(Q)=\{t:Q_t=Q\},
\]

and define the cumulative mask

\[
M_Q=\bigcap_{R\in{\cal L}:\,Q\subseteq R}
       \ \bigcap_{t\in G(R)}S_t.                       \tag{5.1}
\]

Let \({\rm ch}(Q)\) be the maximal proper selected supports inside \(Q\),
and put

\[
R_Q=Q\setminus\bigcup_{R\in\operatorname{ch}(Q)}R.      \tag{5.2}
\]

For a used cell \(p\), the selected supports containing \(p\) form a chain;
write \(d(p)\) for the smallest one.  Define leaf-to-root variable unions

\[
V_Q=\left(\bigcup_{p\in R_Q}(D_p\cap M_Q)\right)
     \cup\left(\bigcup_{R\in\operatorname{ch}(Q)}V_R\right). \tag{5.3}
\]

### Theorem 5.1 (exact laminar characterization)

The selected laminar provider family is feasible if and only if

\[
D_p\cap M_{d(p)}\ne\varnothing                         \tag{5.4}
\]

for every used cell \(p\), and

\[
F_t\cup V_Q=S_t
\qquad(Q\in{\cal L},\ t\in G(Q)).                     \tag{5.5}
\]

#### Proof

The selected target masks constraining a cell \(p\) are precisely the masks
on the ancestor chain of \(d(p)\).  Therefore

\[
K_p=D_p\cap M_{d(p)}.                                  \tag{5.6}
\]

This proves the equivalence of (2.3) and (5.4).  The cells of \(Q\) are the
disjoint union of \(R_Q\) and its child supports.  Induction from the leaves
using (5.6) gives

\[
V_Q=\bigcup_{p\in Q}K_p.                               \tag{5.7}
\]

Now (5.5) is exactly (2.4) for every provider at node \(Q\).  Apply Theorem
2.1. \(\square\)

Theorem 5.1 handles equal supports and nonzero fixed contributions; neither
may be discarded in the S4 collar.

There is also a simpler structural sufficient condition.

### Corollary 5.2 (laminar private-anchor choice)

Suppose one can choose one provider per target so that:

1. \(F_t\subseteq S_t\) for every selected provider;
2. the selected supports are distinct and laminar;
3. \(Q_u\subsetneq Q_t\) implies \(S_u\subseteq S_t\);
4. \(D_p\cap S_{d(p)}\ne\varnothing\) at every used cell;
5. for every \(t\) and every \(x\in S_t\setminus F_t\), there is a residual
   cell \(p\in R_{Q_t}\) with \(x\in D_p\).

Then the provider choice is feasible.

#### Proof

Nested masks make \(M_{Q_t}=S_t\).  At the residual anchor supplied by (5),
equation (5.6) contains \(x\).  Thus every required coordinate of every
provider is reproduced; condition (4) gives nonempty cells.  Theorem 2.1
applies. \(\square\)

The private-anchor clause is essential, as the root-plus-singleton blocker
example after Theorem 4.1 shows.  For the S4 system, a distinct-support
certificate alone cannot cover 69 targets.  Every support lies inside one of
the three disjoint blocks of sizes \(4,9,5\), and a laminar family on an
\(n\)-point block has at most \(2n-1\) distinct nonempty members: after
adjoining the block and all singletons, its inclusion tree has \(n\) leaves
and every internal node has at least two children.  Hence S4 has at most

\[
(2\cdot4-1)+(2\cdot9-1)+(2\cdot5-1)=33                \tag{5.8}
\]

distinct laminar supports.  A laminar S4 proof must therefore use the grouped
equal-support identities (5.5), not merely Corollary 5.2.

## 6. Running-intersection induction for provider choices

The exact provider-only CSP of Section 3 has one variable
\(X_t\in{\cal P}_t\) per target.  Assign every minimal forbidden tuple to a
scope \(W_a\subseteq{\cal T}\) containing all its variables, and let \(R_a\)
be the relation of assignments on \(W_a\) extending none of the tuples
assigned there.  Require every target variable to occur in some scope,
adding an unconstrained unary scope when necessary.  Then satisfying all
\(R_a\) is exactly avoiding every forbidden tuple of Section 3.

### Theorem 6.1 (join-tree extension)

Assume the scopes admit a tree \({\cal T}_0\) with the running-intersection
property: for every target variable \(X_t\), the nodes \(a\) with
\(t\in W_a\) form a connected subtree.  Perform exact semijoin pruning along
the tree.  If the root relation remains nonempty and every retained parent
tuple has a compatible retained tuple in each child relation, then a global
provider choice exists.  In particular, the projection equalities

\[
\pi_{W_a\cap W_b}(R_a)=
\pi_{W_a\cap W_b}(R_b)                                 \tag{6.1}
\]

on every tree edge, together with nonemptiness of the pruned relations, are
sufficient.  If pruning empties a relation, no global choice exists.

#### Proof

Choose a retained root tuple.  Extend it to a compatible retained tuple at
each child and recurse.  If a variable occurs in two chosen bags, the
running-intersection property places it in every separator along their path,
so the values agree.  The resulting total choice satisfies every relation
and therefore avoids every forbidden tuple from Section 3.  Theorem 2.1
gives the canonical cell assignment.  Conversely, the restriction of a
global solution supports itself across every separator and cannot be removed
by an exact semijoin. \(\square\)

This is the precise Helly-like choice theorem.  Acyclicity plus separator
consistency supports induction; pairwise provider or target feasibility does
not.  Whether the S4 conflict scopes admit a useful join tree is a separate,
currently unproved structural gate.

## 7. Exact S4 specialization

In the frozen S4 \(4/9/5\) collar,

\[
\Omega=[16],\qquad |C|=18,\qquad D_p=\Omega
\]

for every free cell.  The two fixed bodies leave exactly 69 residual targets.
The authenticated complete semantic catalogue has 5,867 provider rows in 389
shapes.  A row is precisely

\[
(S_t,F_e,Q_e),
\]

where \(F_e\) is the exact fixed-body OR and \(Q_e\) lies wholly inside one
of the three free blocks of lengths \(4,9,5\).  Hence \(|Q_e|\le9\).

For one selected row per residual target,

\[
K_p=\bigcap_{t:\,p\in Q_t}S_t                         \tag{7.1}
\]

with the empty intersection interpreted as \([16]\).  The collar is feasible
if and only if every \(K_p\) is nonempty and

\[
F_t\cup\bigcup_{p\in Q_t}K_p=S_t                     \tag{7.2}
\]

for all 69 selected rows.  The assignment \(A_p=K_p\) then gives a literal
collar assignment covering all 69 residual targets.  Thus the frozen S4
residual-coverage cell-bit model is exactly a pure one-provider-per-target
CSP; this alone does not produce an equality-valid or repeat-free K16 word.

Theorem 4.1 gives a concrete S4 consequence: every infeasible fixed provider
choice has a bad selected subfamily of at most

\[
\max\{16,1+9\}=16                                      \tag{7.3}
\]

rows.  More specifically, a dead cell has a certificate of at most 16 rows,
and a failed provider-bit has a certificate of at most 10 rows.  This bound
does not prove that some total provider choice exists; the existential
choice can still contain a cyclic Hall-type obstruction.

The protected facets

\[
0x4c71,\qquad0x4879,\qquad0x4c39
\]

have unique pairwise-disjoint literal hosts in the assembled incumbent,
wholly in the fixed lower body.  They impose no constraint on the 18
free-cell choices: collar changes cannot destroy those fixed witnesses,
although they may create additional witnesses.  Their coexistence explains
why the state2 facet trilemma cannot be globalized, but it does not solve the
69-target provider CSP.

## 8. Scope and remaining gate

The maximal-intersection theorem is unconditional under (1.1), exact fixed
ORs \(F_e\), and a complete provider catalogue.  It does not preserve omitted
middle, residence, or chronology rows unless those restrictions have already
been incorporated into the cell caps or provider constraints.

For S4, the frozen atlas supplies the required complete catalogue.  The
remaining mathematical question is now exact and smaller than the cell-bit
formulation:

> choose one of the 5,867 semantic rows for each of the 69 targets so that no
> dead-cell or blocker-cover tuple occurs.

A proof of existence may come from a grouped laminar choice satisfying
Theorem 5.1 or a separator-consistent join tree satisfying Theorem 6.1.
Neither property has yet been proved for the S4 atlas.  Pairwise Helly tests
cannot close the gate.

An independent adversarial proof audit verified Theorems 2.1, 4.1, 5.1 and
6.1 after explicitly retaining the fixed contribution `F`, filtering
fixed-overflow options, handling empty and equal supports, and requiring
nonempty separator-consistent join-tree relations.  It also verified the
sharp counterexamples and the blockwise 33-support bound.  No finite search
or solver claim enters these abstract theorems.

Frozen S4 inputs:

* `MATH_THEOREM_R_K16_S4_FIXED_FACET_RESIDUAL_HOST_CHOICE_FRONTIER_20260730.md`,
  SHA `709ce06335b82dd2cb58c8d56f35e52986cf6d8376f07b42ff232b656d541587`;
* `MATH_AUDIT_R_K16_S4_FROZEN_HOST_CHOICE_FRONTIER_20260730.md`,
  SHA `4e5cd804035434e64145418fa146c4ef7e5bbf694786e4d152badabc2200bd4a`;
* `scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/host_atlas.audit.json`,
  SHA `9304c90e9196d06f2eaad195f090b8f30d708ec7acc426d0edaab6b2cda24718`;
* `scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/model.map.json`,
  SHA `fc2c4f185e294b963c391af56379e4dfbfbf9655a2b7457aa798a7d854ff73f2`;
* `scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/residual_witness_incidence.tsv`,
  SHA `5df821abdd06e74a7aa1f8206aa0bc483d55afb0afaaf8c7cd042fd52def8cd5`.
