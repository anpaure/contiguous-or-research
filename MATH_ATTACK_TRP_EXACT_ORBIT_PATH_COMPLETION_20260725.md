# TRP exact orbit path completion: desymmetrization neither gains nor loses runs

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let

\[
 n=2m,\qquad M=m+H,\qquad
 T=M\binom{2m}{M},\qquad G=S_{2m},
\tag{0.1}
\]

and let \(\mathcal B\) be an integral ambient floor/ceiling-balanced
top-rooted full-flag resolution with exactly \(M\) columns above every
rank-\(M\) top.  Resolve its columns to radius-\(Q\) rotor states.

For a fixed top \(U\), let \(S_U(\mathcal B)\) be its \(M\) selected
states.  If \(P\) is a partial matching from a source copy to a target
copy of \(S_U(\mathcal B)\), supported on legal rotor edges, let
\(c(P)\) be the number of directed cycle components of \(P\), and put

\[
 p_U(\mathcal B)
 :=\min_P\{M-|P|+c(P)\},
 \qquad
 p(\mathcal B):=\sum_U p_U(\mathcal B).
\tag{0.2}
\]

Isolated vertices count as path components.  Thus (0.2) is exactly the
minimum number of directed rotor paths and cycles which partition the
selected states over \(U\), with every directed cycle charged once.

Take the full coordinate orbit \(\bigsqcup_{g\in G}g\mathcal B\).
Among **all** legal occurrence-level successor permutations of this
orbit multiset and all typewise reassignments which leave every color
with exactly its original full-column occurrences, the least possible
total number of monochromatic cyclic runs is

\[
 \boxed{R_{\min}(\mathcal B)=|G|\,p(\mathcal B).}
\tag{0.3}
\]

The upper bound in (0.3) is constructive and integral.  Choose a
minimizing partial matching separately in every top of every color.
After taking the full orbit, the unmatched source stubs and unmatched
target stubs have exactly the same constant multiplicity at every exact
rotor state.  A perfect matching of the regular rotor state graph joins
all residual stubs.  Adding those edges never increases the number of
monochromatic runs.

There is an equally exact quota-preserving version.  Let \(\mathfrak B\)
be the finite family of all integral ambient floor/ceiling-balanced
top-rooted full-flag resolutions with the prescribed quotas, and put

\[
 p_{\mathrm{bal}}:=\min_{\mathcal B'\in\mathfrak B}p(\mathcal B').
\tag{0.4}
\]

The full coordinate orbit of **every** \(T\)-column full-flag family has
the same multiplicity on every exact full flag.  Consequently, even if
colors may be rebuilt into arbitrary ambient-balanced resolutions while
using only the available exact full-flag occurrences, the exact optimum
is

\[
 \boxed{R_{\min}^{\mathrm{quota}}=|G|\,p_{\mathrm{bal}}.}
\tag{0.5}
\]

Thus symmetrization followed by arbitrary integral flow completion is
neither a shortcut nor an additional obstruction.  It has low total run
count

\[
 R=o(|G|W/Q)
\tag{0.6}
\]

if and only if there exists one ambient-balanced resolution with

\[
 p(\mathcal B)=o(W/Q).
\tag{0.7}
\]

This is sharper than a Hall-only statement: exact successor Hall gives
cycle covers but (0.2) also charges their number.  The theorem does not
construct a balanced resolution satisfying (0.7), and hence does not by
itself prove coefficient one.

## 1. The fixed-top component functional

Fix a top \(U\).  The selected state set \(S_U=S_U(\mathcal B)\) has
size \(M\).  Distinctness follows from the calibrated middle load
\(T/W\le1\): two equal resolved states would have the same middle flag,
whereas middle flags occur at most once in \(\mathcal B\).

Make a bipartite graph with a source and a target copy of \(S_U\), and
join \(s_{\mathrm{out}}\) to \(t_{\mathrm{in}}\) precisely when
\(s\to t\) is a legal rotor update.  A partial matching \(P\) in this
graph becomes a directed graph on the common vertex set \(S_U\), with
indegree and outdegree at most one.  Every component is one of:

* an isolated vertex;
* a nontrivial directed path; or
* a directed cycle.

Let \(a(P)\) be the number of path components, including isolated
vertices, and \(c(P)\) the number of cycle components.

### Lemma 1.1 (exact component count)

\[
 \boxed{a(P)+c(P)=M-|P|+c(P).}
\tag{1.1}
\]

#### Proof

A path component on \(v\) vertices has \(v-1\) edges; a cycle component
on \(v\) vertices has \(v\) edges.  Summing \(v-e\) over all components
gives \(M-|P|=a(P)\).  Adding \(c(P)\) proves (1.1). \(\square\)

It follows that \(p_U(\mathcal B)\) in (0.2) is exactly the minimum
number of legal directed path/cycle pieces covering all selected states.
In particular, merely maximizing \(|P|\) need not minimize the charged
component count: closing a path into a cycle raises both \(|P|\) and
\(c(P)\) by one and leaves (1.1) unchanged.

## 2. Every colored cycle factor has at least the local optimum

Take the occurrence multiset

\[
 \widehat{\mathcal B}=\bigsqcup_{g\in G}g\mathcal B,
\tag{2.1}
\]

and suppose its occurrences have been given an arbitrary legal successor
permutation.  Assume first that each occurrence keeps the indexed color
\(g\) and full column supplied by (2.1).  Split every directed successor
cycle into its maximal constant-color runs; an entirely monochromatic
cycle counts as one run.  Let the total be \(R\).

Fix a color \(g\) and a top \(U\).  Retain only those successor edges for
which both endpoints have color \(g\).  They form a legal partial
matching \(P_{g,U}\) on the \(M\) selected states of \(g\mathcal B\)
over \(U\).  Its path components are exactly the noncyclic runs of this
color and top, and its cycle components are exactly the wholly
monochromatic successor cycles of this color and top.  Hence its number
of runs is

\[
 M-|P_{g,U}|+c(P_{g,U}).
\tag{2.2}
\]

Relabelling by \(g^{-1}\) identifies this table with the table of
\(\mathcal B\) over \(g^{-1}U\).  Therefore (2.2) is at least
\(p_{g^{-1}U}(\mathcal B)\).  As \(U\) runs over all tops, so does
\(g^{-1}U\).  Summing first over tops and then over all indexed colors
gives

\[
 \boxed{R\ge |G|p(\mathcal B).}
\tag{2.3}
\]

This lower bound permits arbitrary legal successor cycles; it is not
restricted to copied cycles of a fixed state permutation.

## 3. Orbit residuals are exactly uniform

For every top \(U\), choose a partial matching \(P_U^*\) attaining
\(p_U(\mathcal B)\).  Put

\[
 r_U=M-|P_U^*|,
 \qquad
 r=\sum_U r_U.
\tag{3.1}
\]

The matching \(P_U^*\) leaves exactly \(r_U\) unmatched source vertices
and exactly \(r_U\) unmatched target vertices.  Let \(A^+\) be the
indexed set of all unmatched source columns of \(\mathcal B\), and
\(A^-\) the indexed set of all unmatched target columns.  Then

\[
 |A^+|=|A^-|=r.
\tag{3.2}
\]

Relabel these chosen matchings in every color \(g\mathcal B\).  These
monochromatic edges form exactly

\[
 |G|\sum_U\bigl(M-|P_U^*|+c(P_U^*)\bigr)
 =|G|p(\mathcal B)
\tag{3.3}
\]

monochromatic path/cycle pieces.

Let \(\mathscr S\) be the global exact radius-\(Q\) state space.  The
action of \(G\) on \(\mathscr S\) is transitive, and one state has
stabilizer order

\[
 K=(m-H)!(m-Q)!(H-Q)!.
\tag{3.4}
\]

### Lemma 3.1 (uniform residual multiplicities)

Every exact state \(s\in\mathscr S\) occurs exactly \(rK\) times among
the relabelled unmatched source occurrences, and exactly \(rK\) times
among the relabelled unmatched target occurrences.

#### Proof

Fix one indexed column \(c\).  Exactly \(K\) permutations send its
resolved state to a prescribed \(s\).  Sum this count first over the
\(r\) columns in \(A^+\), and then over the \(r\) columns in \(A^-\).
The answers are both \(rK\). \(\square\)

No relation between the actual sets \(A^+\) and \(A^-\) is needed.  Only
their equal cardinalities matter after full coordinate symmetrization.

## 4. Integral residual completion without additional runs

For a state

\[
 (U;L;z_1,\ldots,z_{2Q};R),
\]

a legal rotor edge is specified by \((x,y)\in L\times R\).  Hence the
bipartite legal state graph is

\[
 D\text{-regular},\qquad D=(m-Q)(H-Q),
\tag{4.1}
\]

on both sides.  It has a perfect matching \(\psi:\mathscr S\to
\mathscr S\) by Hall's theorem.

For each state \(s\), take the \(rK\) residual source occurrences of
type \(s\), and biject them to the \(rK\) residual target occurrences of
type \(\psi(s)\).  Lemma 3.1 makes this possible.  Add the resulting
legal rotor edges.  Every occurrence now has indegree and outdegree one,
so all occurrences form directed cycles.

Before completion, every monochromatic cycle component has no residual
stub and remains unchanged.  Every other monochromatic component is a
path.  Adding an edge between two residual endpoints has one of three
effects:

1. if its endpoint colors differ, it leaves the two monochromatic runs
   distinct;
2. if the colors agree and the paths are distinct, it merges two runs;
3. if the colors agree and it closes one path, it turns that run into one
   monochromatic cycle.

In no case does the number of monochromatic runs increase.  Thus the
completed successor permutation has

\[
 R\le |G|p(\mathcal B).
\tag{4.2}
\]

Together with (2.3), this proves the exact identity (0.3).

The proof is an integral path factorization, not a fractional averaging
argument.  Its only matching step is in a regular bipartite graph.

## 5. The full-flag orbit is independent of the starting resolution

An exact full top-rooted flag is a chain

\[
 F_{m-H}\subset F_{m-H+1}\subset\cdots\subset F_M,
 \qquad |F_j|=j.
\tag{5.1}
\]

The group \(G\) acts transitively on these flags.  Its stabilizer may
permute independently the bottom set \(F_{m-H}\) and the ambient
complement \([2m]\setminus F_M\), both of size \(m-H\); every one-point
increment in the chain is fixed.  Therefore the stabilizer order is

\[
 K_{\mathrm{full}}=((m-H)!)^2.
\tag{5.2}
\]

### Lemma 5.1 (universal full-flag orbit multicover)

Let \(\mathcal A\) be any indexed family of exactly \(T\) full flags,
with repetitions allowed.  In

\[
 \bigsqcup_{g\in G}g\mathcal A,
\]

every exact full flag occurs exactly

\[
 \boxed{T((m-H)!)^2}
\tag{5.3}
\]

times.

#### Proof

For each indexed flag of \(\mathcal A\), the permutations sending it to
a prescribed exact flag form a coset of the stabilizer (5.2).  Sum over
the \(T\) indexed flags. \(\square\)

In particular, the full coordinate orbits of any two \(T\)-column
families are isomorphic by a full-flag-type-preserving bijection of their
occurrences.

## 6. Exact quota-preserving recoloring optimum

Let \(\mathfrak B\) be the family of all integral top-rooted resolutions
with:

* exactly \(M\) columns at every top; and
* the prescribed ambient floor/ceiling target loads at every rank.

This family is nonempty by the integral balanced-flow theorem.  Define
\(p_{\mathrm{bal}}\) by (0.4).

Consider the full orbit occurrence pool of any one member of
\(\mathfrak B\).  A quota-preserving recoloring may repartition this pool
into \(|G|\) indexed colors, each of which is a member of
\(\mathfrak B\), provided every physical occurrence keeps its exact full
flag type.

### Theorem 6.1 (universal desymmetrization identity)

The least total run count over all such recolorings and all legal
occurrence-level successor permutations is

\[
 \boxed{R_{\min}^{\mathrm{quota}}=|G|p_{\mathrm{bal}}.}
\tag{6.1}
\]

#### Proof

For the lower bound, apply the argument of Section 2 separately to each
balanced color \(\mathcal B_g\).  Its contribution is at least
\(p(\mathcal B_g)\ge p_{\mathrm{bal}}\).  Summing over \(|G|\) colors
gives \(R\ge|G|p_{\mathrm{bal}}\).

For the upper bound, choose a minimizer
\(\mathcal B^*\in\mathfrak B\).  By Lemma 5.1, repartition the available
full-flag occurrences into the full coordinate orbit
\(\bigsqcup_{g\in G}g\mathcal B^*\), matching only identical exact full
flags.  Apply the integral completion of Sections 3--4 to this orbit.
It has exactly \(|G|p(\mathcal B^*)=|G|p_{\mathrm{bal}}\) runs. \(\square\)

Thus arbitrary orbit flows, exact multiplicity, and quota-preserving
color reassignment cannot lower the normalized run cost below that of
the best single balanced resolution.

## 7. Relation to Hall and the literal ledger

For one top, a perfect legal successor matching exists precisely when
successor Hall holds.  If it exists, every minimizing cover may still
contain several directed cycles, each charged once by \(p_U\).  If Hall
fails, (0.2) also charges the unmatched path endpoints.  Thus
\(p(\mathcal B)\) simultaneously records:

* Hall deficiency; and
* the number of stationary cycle components which must be cut for a
  literal word.

For a radius-\(Q\) compilation, every run has exact initialization toll
\(2Q+1\).  A color with \(T\) endpoints and \(p(\mathcal B)\) pieces has
literal length

\[
 T+(2Q+1)p(\mathcal B).
\tag{7.1}
\]

At the calibrated crossing \(T=(1-o(1))W\).  Therefore

\[
 p(\mathcal B)=o(W/Q)
\tag{7.2}
\]

is sufficient for the required \(W+o(W)\) ledger, and Theorem 6.1 says
that (7.2) is also exactly what a successful quota-preserving orbit
recoloring must discover.

## 8. Proved boundary

The desymmetrization alternatives are now separated exactly.

1. **Recoloring a fixed copied state-cycle factor.**  The adjacent-color
   overlap identity in
   `MATH_ATTACK_TRP_ORBIT_COLOR_REASSIGNMENT_NO_GO_20260725.md` forces
   \((1-o(1))|G|W\) runs.  That particular route is closed.

2. **Choosing an arbitrary integral rotor factor while retaining each
   color's exact state set.**  The exact optimum is
   \(|G|p(\mathcal B)\), by (0.3).

3. **Rebuilding colors subject only to exact full-flag availability and
   ambient floor/ceiling quotas.**  The exact optimum is
   \(|G|p_{\mathrm{bal}}\), by (0.5).

Hence full symmetrization removes denominator and residual-completion
problems, but it gives no run-count discount.  The surviving
coefficient-one gate is the following finite integral statement with its
quantifier now exact:

> Construct one ambient floor/ceiling-balanced top-rooted resolution
> \(\mathcal B\) for which the sum over tops of the minimum legal
> path/cycle cover numbers is \(o(W/Q)\).

No such construction, and no lower bound excluding it, is proved here.
