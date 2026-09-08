# Independent audit: socketed counterflow and complement rotation

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_ODD_SOCKETED_COUNTERFLOW_CYCLE_CRITERION_20260806.md`  
**Method:** direct source/terminal accounting, cycle decomposition, and
odd-order orbit lifting; no computation or search  
**Verdict:** PASS, with one harmless simple-graph wording qualification in
Corollary 3.2.

## 1. Deterministic socket accounting

For a selected sink set \(I\), the suffix ending at \(b_i\) starts on
source path \(P_{\pi(i)}\).  Retaining the paths to \(a_i\) for
\(i\in I\cup S\) and redirecting the paths with source indices
\(\pi(I)\) is source-disjoint exactly when

\[
                  \pi(I)=[\delta]\setminus(I\cup S).
\tag{1.1}
\]

The terminal count is then

\[
                  2|I|+|S|=\delta.
\tag{1.2}
\]

On one \(\pi\)-cycle, (1.1) alternates selected-pair and redirected-source
indices.  An even cycle needs no socket; an odd cycle needs and accepts
exactly one.  Hence the minimum socket number is precisely the number of
odd cycles.  The direction convention in the source is consistent: sink
\(b_i\) uses source \(\pi(i)\), not \(\pi^{-1}(i)\).

## 2. Matching-faithful support formula

For an oriented support edge represented by a suffix

\[
                         P_j\leadsto b_i,
\tag{2.1}
\]

the construction retains \(P_i\leadsto a_i\) and redirects source
\(P_j\).  A graph matching makes the source indices \(i,j\) disjoint
between chosen edges.  Matching-faithfulness supplies the remaining
physical vertex-disjointness.  Every matched graph edge therefore pays
two sources and produces the two endpoints of one physical boundary edge;
every unmatched graph vertex contributes one retained aperture terminal.
The exact socket count is

\[
                         \delta-2|M|,
\]

and maximizing \(|M|\) proves \(\delta-2\nu(G_\partial)\).  No hidden
orientation, terminal-duplication, or colour assumption is missing:
the aperture theorem already makes the boundary edges a matching with
private hubs.

The only wording qualification is that, for a permutation \(\pi\), the
underlying **simple** support graph is not literally a union of ordinary
cycles in the degenerate lengths one and two.  A fixed point becomes an
isolated vertex and a two-cycle becomes one \(K_2\) edge.  Its maximum-
matching deficiency is nevertheless one for the former and zero for the
latter, exactly the odd-cycle formula.  The theorem and corollary are
unchanged after stating these degeneracies explicitly.

## 3. Complement-rotation orbit parity

Write \(m=2^a\ell\), \(\ell\) odd, and put

\[
                         J=CR^{2^a}.
\tag{3.1}
\]

The rotation factor has odd order \(\ell\), and it commutes with digit
complement.  If a state belongs to an odd \(J\)-orbit of length \(t\),
then

\[
                         u=CR^{2^a t}u.
\tag{3.2}
\]

Every coordinate cycle of \(R^{2^a t}\) has odd length.  Iterating (3.2)
around such a cycle alternates \(x\) and \(2-x\); odd closure forces
\(x=1\).  Thus the only odd orbit is the fixed all-one state.  This also
covers \(\ell=1\), when \(J=C\).

Complement reverses a directed unit transfer and rotation preserves it,
so \(J\) is indeed an automorphism of the undirected cyclic capacity-two
token graph.

## 4. Odd quotient descent

Suppose an odd-order group \(H\) commutes with \(J\), and an orbit
\([x]\) has odd period \(t\) under the induced permutation.  Then

\[
                         J^t x=h x
\]

for some \(h\in H\).  If \(h\) has odd order \(r\), commutation gives

\[
                         J^{tr}x=x.
\]

Thus the ordinary \(J\)-orbit of \(x\) has odd length and hence is the
all-one fixed point.  If that point is \(H\)-fixed, its quotient orbit is
the unique odd orbit downstairs.  The source theorem uses this only for
odd rotation subgroups, where all hypotheses hold.

## 5. Scope check

The audited theorem proves an exact **criterion** and a source-level
parity-perfect target.  It does not prove:

1. that the complement-rotation is realized by physical counterflow
   suffixes in the fixed contracted digraph;
2. matching-faithfulness of any macroscopic support graph;
3. hub-orbit injectivity after a nontrivial stabilizer quotient; or
4. compatibility with the complementary nonwrap receiver bank.

No sentence in the audited result should be read as closing those physical
rows.

