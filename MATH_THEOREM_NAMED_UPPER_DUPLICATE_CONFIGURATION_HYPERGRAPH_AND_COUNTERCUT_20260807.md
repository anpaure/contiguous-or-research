# Named upper-safe fusion is a configuration-hypergraph problem, not a rank-count problem

**Date:** 2026-08-07  
**Status:** exact formulation, exact fractional countercut, and explicit
integral obstructions.  Central binomial slack pays the total common-state
fusion current rank by rank, but neither total slack nor nesting inside
individual crossing ladders implies a simultaneous named selection.  A
palette-neutral pentagonal (3\leftrightarrow3) packet is the correct
immediate-palette type, but its higher-window current needs its own named
configuration matching.

## 1. Named duplicate capacities

Fix an upper-complete pre-fusion chronology.  For every upper offset (s)
and every named rank-(R+s) target (T), let

\[
 \mu_s(T)=\#\{\text{current occurrences of }T\},
 \qquad
 b_s(T)=\mu_s(T)-1.
\tag{1.1}
\]

The number (b_s(T)) is the exact number of old occurrences of (T)
which may be deleted while retaining a protected old witness.  Since the
row is complete,

\[
 \sum_T b_s(T)=W-\binom{k}{R+s}=S_s.
\tag{1.2}
\]

Thus the central-slack theorem is the full-shore identity and lower bound

\[
 \sum_T b_s(T)=S_s\ge cs.
\tag{1.3}
\]

It contains no information about which (T)'s occur at candidate fusion
interfaces.

## 2. Candidate packets and the strong protected-deletion problem

First prescribe a finite set (mathcal I) of fusion tasks.  This may be a
fixed list of component interfaces, or the arcs of a preselected rooted
fusion schedule.  For task (i), let (mathcal P_i) be its admissible
literal packet options.

Every (P\in\mathcal P_i) must already include:

1. its literal owner rethread;
2. residence-compatible collars;
3. its physical ports and topology action;
4. exact equality of its old and new lower-(q1) palettes;
5. preferably exact equality of its old and new upper-(q1) palettes;
6. a complete old/new occurrence ledger at every higher offset.

Let

\[
 d_{iP}(s,T)
\tag{2.1}
\]

be the multiplicity of old crossing occurrences of named target (T)
which packet (P) deletes.  Internal old/new equality cancellations may
be made before (2.1), but creations by other packets are deliberately not
credited.  The strong protected-deletion problem is to choose one option
(P_i\in\mathcal P_i) for every task so that

\[
 \boxed{
 \sum_{i\in\mathcal I}d_{iP_i}(s,T)\le b_s(T)
 \quad\text{for every }(s,T).}
\tag{2.2}
\]

When packet collars are physically disjoint, (2.2) guarantees that every
old named upper target retains a witness.  New crossings can only add
witnesses.  Therefore (2.2), together with the packet's local owner,
palette, residence and topology guarantees, is a sufficient literal
upper-safe fusion criterion.

The exact net condition can be weaker.  If (a_{iP}(s,T)) is the number
of new occurrences, it is

\[
 \mu_s(T)+\sum_i
 \bigl(a_{iP_i}(s,T)-d_{iP_i}(s,T)\bigr)\ge1.
\tag{2.3}
\]

Equation (2.2) is preferable for an absorber theorem because it is
monotone, packet-local, and does not rely on cancellation between distant
interfaces.

## 3. Exact configuration-hypergraph formulation

Expand every capacity into labelled unit tokens

\[
 mathcal R={(s,T,u):1\le u\le b_s(T)\}.
\tag{3.1}
\]

For every packet (P\in\mathcal P_i), and every injection of its
(d_{iP}(s,T)) deletion claims into the corresponding tokens (3.1), form
a hyperedge containing:

* the task vertex (i);
* all assigned duplicate tokens;
* every exclusive physical port or guard resource consumed by (P).

Call the resulting configuration hypergraph (mathcal K).

### Theorem 3.1 (exact protected-deletion matching)

Assume the topology schedule is already prescribed and every packet option
has the advertised local literal properties.  There is a simultaneous
upper-safe, resource-disjoint choice of one packet per task if and only if
(mathcal K) has a matching covering every task vertex.

#### Proof

A covering matching selects one edge incident with each task and no two
selected edges share a capacity or physical-resource token.  Forgetting
the capacity-token labels gives (2.2) and physical disjointness.
Conversely, any packet selection satisfying (2.2) can inject the claims
for each ((s,T)) into its (b_s(T)) labelled tokens; physical
disjointness then gives a matching of the associated configuration edges.
(square)

If topology is not prescribed, each packet also has an edge or hyperedge
on the component quotient.  One must then impose a spanning-tree,
arborescence, or graphic-rank condition on the selected packet set.  This
is a configuration matching coupled to a graphic constraint, not an
ordinary bipartite matching.  Rank-wise upper slack says nothing about
that extra condition.

## 4. Exact fractional Hall countercut

Ignore physical resources and topology for the moment.  Let (V) be the
set of all relevant named pairs ((s,T)), including pairs of zero
capacity.  An option deleting a zero-capacity name is thereby forbidden
unless its old/new ledger cancels that deletion before (2.1) is formed.

and regard (d_{iP}\in\mathbb Z_{ge0}^V) as the packet's named demand
vector.  The fractional relaxation is

\[
 \sum_{P\in\mathcal P_i}x_{iP}=1,
 \qquad
 \sum_{i,P}d_{iP}(v)x_{iP}\le b(v),
 \qquad x_{iP}\ge0.
\tag{4.1}
\]

### Theorem 4.1 (weighted named countercut)

The fractional system (4.1) is feasible if and only if, for every
nonnegative price vector (lambda\in\mathbb R_{ge0}^{V}),

\[
 \boxed{
 \sum_{i\in\mathcal I}
 \min_{P\in\mathcal P_i}
 \langle\lambda,d_{iP}\rangle
 \le \langle\lambda,b\rangle.}
\tag{4.2}
\]

#### Proof

Necessity follows by pricing the resource inequalities in (4.1): the
expected price paid by task (i) is at least the cheapest option price.

For sufficiency, the set

\[
 \sum_i\operatorname{conv}{d_{iP}:P\in\mathcal P_i}
 +\mathbb R_{ge0}^{V}
\]

is a closed convex upper set.  If it contains no vector coordinatewise at
most (b), a separating hyperplane may be chosen with nonnegative normal
(lambda).  Separation gives the strict reverse of (4.2), a
contradiction.  \(\square\)

For a resource subset (Q\subseteq V), taking
(lambda=mathbf1_Q) gives the concrete necessary cut

\[
 \boxed{
 \sum_i\min_{P\in\mathcal P_i}d_{iP}(Q)\le b(Q).}
\tag{4.3}
\]

The central-slack row (1.3) is only the special choice where (Q) is an
entire rank shore and the task demand is known to equal (s).  It checks
none of the proper named subsets (Q), and it does not correlate different
ranks.

## 5. Two sharp counterexamples

### 5.1 Total rank slack can fail even fractionally

Take two tasks and one rank at which each packet deletes two occurrences.
Let the duplicate capacities be one on each of

\[
 A,B_1,B_2,C.
\]

Task 1 has the sole demand ({A,B_1}), and task 2 has the sole demand
({A,B_2}).  Total capacity is four and total demand is four, so the
rank-wise scalar inequality is tight.  Nevertheless the named cut
(Q={A}) has

\[
 1+1> b(A)=1.
\]

No fractional or integral selection exists.  The unused duplicate at
(C) is irrelevant.

The same example can be extended through arbitrarily many upper widths by
placing the forced targets (A_s) on one nested crossing ray and giving
all other claims private capacity.  Thus nesting along the forced ray does
not repair the named cut.

### 5.2 Nested packet chains do not imply integral rounding

Let the unit-capacity Boolean targets be

\[
 a=\{1\},\quad b=\{2\},
\]

\[
 z_{ax}=\{1,3\},\quad z_{bx}=\{2,3\},\quad
 z_{ay}=\{1,4\},\quad z_{by}=\{2,4\},
\]

and

\[
 x=\{1,2,3\},\qquad y=\{1,2,4\}.
\]

Task 1 has two options

\[
 a\subset z_{ax}\subset x,
 \qquad
 b\subset z_{by}\subset y,
\tag{5.1}
\]

while task 2 has

\[
 a\subset z_{ay}\subset y,
 \qquad
 b\subset z_{bx}\subset x.
\tag{5.2}

Every option is a nested Boolean chain.  Every rank has at least as much
total capacity as demand.  The half-half fractional choice uses (a,b,x,y)
exactly once and every middle target with load (1/2), so (4.1), and hence
all weighted cuts (4.2), pass.

There is no integral choice.  If task 1 chooses its (a\)-to-(x) chain,
the two options of task 2 collide respectively at (a) and (x).  If
task 1 chooses its (b\)-to-(y) chain, they collide respectively at
(y) and (b).

Thus even nested multi-rank packet options can have a genuine integral
configuration obstruction after all fractional Hall cuts pass.

## 6. Why a pentagonal packet is the right palette type—and why slack still does not finish it

A bare common-state splice has two immediate defects:

1. all selected seams use the same lower-(q1) colour; and
2. its upper-(q1) values undergo the nonzero (2\times2) rectangle
   exchange.

It therefore cannot be inserted post hoc into an already simple two-sided
immediate palette.

A prepared pentagonal alternating (3\leftrightarrow3) exchange instead
preserves the complete selected lower and upper immediate palettes.  Such
packets are the correct candidates for the families (mathcal P_i): their
(s=1) named current is zero, and topology can change without spending an
immediate-palette duplicate.

However, a pentagonal packet changes three owner transitions.  With
separated collars, its raw old crossing count at upper offset (s) is at
most (3s), before named old/new cancellations.  A bank of (t) packets
therefore has raw demand up to (3ts).  The scalar theorem
(S_s\ge cs), proved for (c) changed common-state seams, does not by
itself dominate this different ledger.  One must compute each packet's
exact higher-window vector (d_{iP}(s,T)), exploit its internal
cancellations, and solve Theorem 3.1.

There is a second independent gate: the existing pentagonal theory proves
that an aligned packet preserves both outer palettes, but not that every
current component configuration contains a prepared packet with the
required topological action.  Candidate supply and the named duplicate
matching must be selected jointly.

## 7. Exact remaining theorem

A proof-safe upper-fusion theorem would establish all of the following.

1. **Prepared supply.**  There is a topology-spanning family of
   residence-safe pentagonal packet options preserving both (q1)
   palettes.
2. **Named expansion.**  Their configuration hypergraph satisfies a
   covering-matching criterion, or has an absorber which rounds the
   fractional cuts (4.2).
3. **Terminal widths.**  Full-period and multi-seam paths have a separate
   protected reserve.
4. **Regeneration.**  The selected packet/duplicate state is exported with
   bounded complexity.

Rank-wise binomial slack proves the full-shore scalar row needed by Item 2.
It does not prove the proper named cuts, integrality, topology, or
regeneration.  The exact first countercut to test in any proposed bank is

\[
 \sum_i\min_{P\in\mathcal P_i}d_{iP}(Q)>b(Q)
\]

for a small family (Q) of seam-accessible named targets.  If every such
fractional countercut passes, the remaining obstruction is the integral
configuration matching illustrated by Section 5.2.
