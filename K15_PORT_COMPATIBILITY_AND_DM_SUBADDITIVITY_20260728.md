# k=15 port compatibility and DM subadditivity

## 1. Compiler-neighbourhood subadditivity

Fix any target family \(A\) in the lower compiler and write
\(h_A(P)=|N_P(A)|\) for the number of compiler cells adjacent to at least one
target in \(A\) when the middle carrier is the factorable linear path \(P\).

**Theorem.** If \(P,Q,PQ\) are factorable, then

\[
h_A(PQ)\le h_A(P)+h_A(Q).
\]

**Proof.** A depth-\(j\) cell of \(PQ\), with start \(s\), is injected into
the cell of \(P\) with the same start when \(s<|P|\), and otherwise into the
cell of \(Q\) with start \(s-|P|\). These images are disjoint. Relative to
the isolated image, gluing can only shrink every maximal erosion mask.
Consequently its envelope shrinks and every carrier set shrinks. If an
isolated carrier is contained in the cell positions, its glued carrier is
also contained there, so

\[
\operatorname{mandatory}_{\rm isolated}
 \subseteq \operatorname{mandatory}_{\rm glued}.
\]

Thus any target \(X\) accepted by the glued cell was accepted by its isolated
image: \(X\) was contained in the smaller envelope, met every smaller mask
(hence every enlarged isolated mask), and contained the larger glued
mandatory mask (hence the isolated one). The cell injection proves the
inequality. \(\square\)

Therefore every Benders seam coefficient

\[
w_A(P,Q)=h_A(PQ)-h_A(P)-h_A(Q)
\]

is non-positive by theorem, not by accident. Equality means that tightening
the two boundary collars loses no \(A\)-neighbour.

The difference is supported in a radius \(2d-1=5\) collar at depth \(d=3\).
The exact Hall30 cut ledger is frozen in
`scratch/k15_outer2_p1_h30_bridge.dm_cut_gains.json`. The source has
\(|A|=1528,h_A=1498\). Among 2697 individually upper-safe cuts, the maximum
gain is 11. Exactly three spaced cuts suffice: positions 99, 338, 747 have
gains 10, 11, 10, intrinsic total 1529, and leave every upper rank complete.
Two cuts can gain at most 21, so three is minimal. This capacity statement is
not a chronology statement: those four components admit only the original
residence-safe, upper-exact order, whose seam losses return the score to 1498.

## 2. Port-matching relaxation

Give each middle component two physical ports and let \(I\) be the fixed
perfect matching pairing the two ports of each component. Let \(G\) be the
undirected graph of residence-safe external seams. A forced seam is an edge
of \(G\); a forced endpoint reserves a port as globally unmatched.

**Theorem (necessary completion criterion).** Let \(F\) be a port-disjoint
forced-seam forest, and contract \(I\cup F\) into alternating path fragments.
Every Hamilton chronology extending \(F\) induces, on the unreserved exposed
ports, a matching of size

\[
    n-1-|F|
\]

using only edges between distinct fragments. Its fragment graph is connected.
Moreover, for every set \(S\) of fragments,

\[
    c(G-S)\le |S|+1.
\]

**Proof.** A chronology uses every component internally and exactly one
external seam at every port except its two global endpoints. Hence its
external seams are a matching of size \(n-1\). Removing the already forced
edges gives the stated completion matching. An edge within one forced
fragment would close a proper alternating cycle. Contracting the chronology
gives a spanning fragment path, proving connectivity and the cut inequality,
because deleting \(|S|\) vertices from a path creates at most \(|S|+1\)
components. \(\square\)

Maximum cardinality blossom, connectivity, and the \(|S|=1,2\) cut tests are
polynomial and are implemented in O3 in
`scratch/analyze_k15_action_compat.cpp`. Its blossom implementation agrees
with brute force on 4400 frozen random graphs. These tests are necessary, not
sufficient: the remaining connected alternating-Hamilton problem retains the
usual global difficulty.

For the former rich N64 exact-zero source `n64_s12062`, the six locally valid
compiler actions leave 59 fragments but an isolated fragment; maximum
completion matching is 56 versus 58 required. Inclusion-minimal fixed-action
cores include \(\{5801,10794,21588\}\) and \(\{10794,17738\}\). The exact
artifact is `scratch/cpp_n64_s12062.fixed_action_cores.json`.

## 3. Polynomial resource relaxations

Assign each possible completion seam its non-positive DM weight \(w_A\).
Adding the missing zero, one, or two dummy endpoint vertices reduces the best
possible DM score to a maximum-weight matching. This gives a rigorous upper
bound on \(h_A\). Giving an edge weight equal to the number of cut-out lower
or upper colours it restores gives an optimistic restoration bound; duplicate
colours are deliberately credited repeatedly, so the resulting residual-hole
lower bound remains rigorous.

This is implemented in `scratch/analyze_k15_port_resources.py`. On the former
rich N64 source it proves, before SAT, topology deficiency 2, source-DM
deficiency at least 17, and unavoidable lower holes at least 20, 14, 2 in
depths 1, 2, 3 respectively.

## 4. Joint-conditioned portfolio

The cheap native generator remains the default (~0.01 s); blossom conditioning
is opt-in so regression generation does not become exponential. Cut selection
can now use the exact local DM gains. In the first 256-member H100 portfolio,
41 candidates passed port matching/connectivity. All top 24 passed the source
DM weighted-blossom gate with bounds 1551--1574, whereas the previous best
port-conditioned sources were at most 1513. The independently audited top six
are recorded in `scratch/k15_gain_portfolio_top6.audit.json`.

Exact Benders then exposed the next fact: source-DM margin alone is not enough.
The first alternate chronologies have different Hall blocks (deficiencies
52--59 and then 74--86), and the three-witness systems are infeasible. The
next generator must therefore score a vector \((h_{A_0},h_{A_1},\ldots)\) and
maximize its minimum normalized slack, rather than optimize only the canonical
Hall30 block.
