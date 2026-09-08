# Exact root-motif exchange closure at \(k=15\)

This note extracts the mathematical content of the five-parent root-motif
census.  Its most important qualification is stated first:

> The native enumeration is exact for the **cycle-free forced exchange-path
> closure**.  It is not an enumeration of all successor permutations at the
> same support, because an arbitrary completion may also contain disjoint
> alternating cycles.

Accordingly, nothing below proves that every support-\(\le 34\) five-parent
move leaves the seven Hall-29 zero targets unchanged.  What is proved is a
local dependency theorem, exact matching-support floors for the retained
motifs, and an exhaustive residence obstruction inside the stated
cycle-free closure.

## 1. Compiler cells have a finite dependency window

Let

\[
T=(T_0,\ldots,T_{W-1})
\]

be a rank-eight middle chronology and let \(d=3\).  Its maximal linear
erosion is

\[
P_p=\bigcap_{j=\max(0,p-3)}^{\min(p,W-1)}T_j,
\qquad 0\le p<W+3.
\tag{1.1}
\]

For an occurrence \((i,x)\), where \(x\in T_i\), define its carrier set

\[
K(i,x)=\{p\in[i,i+3]:x\in P_p\}.
\tag{1.2}
\]

An interior compiler cell of row-depth \(\ell\in\{0,1,2\}\), starting at
erosion position \(s\), uses the interval

\[
J=[s,s+\ell].
\tag{1.3}
\]

Its envelope is \(\bigcup_{p\in J}P_p\), and its mandatory coordinates are
determined by those occurrences for which \(K(i,x)\subseteq J\).  These are
exactly the data used by the literal compiler eligibility test.

### Lemma 1.1 (dependency-window closure)

The eligibility neighbourhood of the cell \((s,\ell)\) is determined by the
consecutive middle word

\[
T_{s-6},T_{s-5},\ldots,T_{s+\ell+3},
\tag{1.4}
\]

with out-of-range indices omitted.  In the interior this word has exactly
\(\ell+10\) vertices.

#### Proof

The envelope uses \(P_s,\ldots,P_{s+\ell}\).  By (1.1), these depend only on
middle indices from \(s-3\) through \(s+\ell\).

For the mandatory condition, an occurrence can matter only when its nonempty
carrier lies inside \(J\).  Since \(K(i,x)\subseteq[i,i+3]\), this forces

\[
s-3\le i\le s+\ell.
\]

To determine all of \(K(i,x)\), one must inspect
\(P_i,\ldots,P_{i+3}\).  Equation (1.1) shows that these depend only on
\(T_{i-3},\ldots,T_{i+3}\).  Taking the union over
\(i\in[s-3,s+\ell]\) gives exactly the interval
\([s-6,s+\ell+3]\).  Its cardinality is \(\ell+10\).  Boundary truncation
only shortens it.  \(\square\)

### Corollary 1.2 (a repaired zero has a local witness)

If a target has no eligible compiler cell in a chronology \(T\), but gains
one in a chronology \(T'\), then some cell of \(T'\) has a dependency word
from (1.4) different from the corresponding word of \(T\).  In particular,
at least one successor arc in that local word changes.

This is the rigorous basis for enumerating local target motifs before running
a global chronology solver.  It does not say that motifs from different
parents compose independently.

## 2. Forced successor motifs reduce to paths plus optional cycles

Close a Hamilton path with a dummy vertex, so its successor map \(f_0\) is a
permutation of a finite set \(V\).  Let \(f\) be another successor
permutation whose arcs lie in the permitted parent atlas.  Put

\[
\pi=f_0^{-1}\circ f.
\tag{2.1}
\]

Thus \(f(x)=f_0(\pi(x))\), and changed successor tails are precisely the
non-fixed points of \(\pi\).

Suppose a local motif prescribes changed arcs \(f(u)=g(u)\) for
\(u\in U\).  Let

\[
O=f_0^{-1}(g(U)),\qquad D=O\setminus U,
\qquad K=U\setminus O.
\tag{2.2}
\]

The elements of \(D\) are unforced old owners displaced by forced heads;
the elements of \(K\) are forced tails whose old heads become available.
An exchange arc \(x\to y\) means that the candidate is allowed to assign

\[
f(x)=f_0(y).
\tag{2.3}
\]

### Theorem 2.1 (path-and-cycle closure)

After the forced arcs are fixed, every successor-permutation completion is
equivalent to

1. a family of mutually vertex-disjoint exchange paths pairing \(D\) with
   \(K\), together with
2. an arbitrary family of mutually vertex-disjoint exchange cycles disjoint
   from the forced path closure.

Conversely, every such path-and-cycle family gives a successor-permutation
completion.  If all changed tails have unit cost, then

\[
|\operatorname{supp}(f-f_0)|
=|U|+\sum_{P}|E(P)|+\sum_C|E(C)|.
\tag{2.4}
\]

Consequently every minimum-support completion contains no optional exchange
cycle, and its support is obtained exactly by a unit-capacity, node-split
minimum-cost flow from \(D\) to \(K\).

#### Proof

The directed graph of the non-fixed arcs \(x\mapsto\pi(x)\) is a disjoint
union of directed cycles, because \(\pi\) is a permutation.  Delete the
prescribed arcs with tails in \(U\).  In every component meeting a prescribed
arc, each remaining nonempty segment starts at a vertex in \(O\setminus U=D\)
and ends at a vertex in \(U\setminus O=K\).  Vertex-disjointness follows from
the bijectivity of \(\pi\).  A component that meets no prescribed arc remains
an optional directed exchange cycle.  This proves the forward decomposition.

Conversely, inserting vertex-disjoint \(D\)-to-\(K\) paths repairs exactly the
heads displaced and released by the forced arcs; inserting disjoint cycles
preserves both indegree and outdegree.  Hence the resulting map is a
permutation.  Formula (2.4) just counts its non-fixed tails.  Every optional
cycle has positive length, so a minimum-support completion omits all of them.
The standard node-splitting construction enforces vertex-disjointness and
therefore gives the claimed exact min-cost-flow formulation.  \(\square\)

## 3. Exact matching-support floors for the retained motifs

The file `scratch/t1_12_h29zero7.interior.tsv` contains 16 retained interior
motifs from the transposition parent.  Each was imposed relative to the
Hall-29 base path `P0`, with exchange arcs drawn from the union of the five
frozen parents `P0,...,P4`.  Theorem 2.1 gives the following exact minimum
fixed-endpoint successor-support floors, minimized over retained motifs for
each target:

\[
\begin{array}{c|rrrrrrr}
\text{target}&17738&21641&5801&13620&2575&13616&29776\\ \hline
\text{support floor}&19&21&30&30&35&36&38.
\end{array}
\tag{3.1}
\]

These are matching floors.  They do not assert Hamiltonicity, residence, or
compiler feasibility.

For the best target-17738 motif the five forced changed tails are

\[
U=\{23691,23693,25942,25946,25972\},
\]

the five initially displaced tails are

\[
D=\{7821,20909,25934,25948,30040\},
\]

and \(K=U\).  The unique cycle-free minimum uses 14 exchange arcs, hence has
support \(5+14=19\).  Its dummy-closed successor permutation has component
sizes

\[
6048,\quad 304,\quad 84,
\tag{3.2}
\]

so it is not a Hamilton path.

## 4. Exact cycle-free residence census

The native `-O3` enumerator exhausts every cycle-free exchange-path closure
through a declared support cap.  In augmented-endpoint mode, the cumulative
target-17738 census is:

\[
\begin{array}{r|r|r|r|r}
\text{cap}&\text{systems}&\text{Hamilton}&\min\text{ residence defects}
&\text{resident}\\ \hline
19&1&0&-&0\\
20&4&0&-&0\\
21&7&0&-&0\\
22&17&0&-&0\\
23&63&10&15&0\\
24&173&10&15&0\\
25&427&28&15&0\\
26&1115&28&15&0\\
27&3102&162&15&0\\
28&8621&165&15&0\\
29&24397&1023&13&0\\
30&69728&1046&13&0\\
31&200502&6844&13&0\\
32&578793&7110&13&0\\
33&1676638&46895&13&0\\
34&4872036&49431&13&0\\
35&14190482&331145&13&0.
\end{array}
\tag{4.1}
\]

Thus, in this exact scoped class, the first Hamilton completions occur at
support 23, but no completion through support 35 is depth-three resident.
The independently replayed support-23 witness has 15 residence defects and
upper-hole vector

\[
(7,4,1,0,0,0,0),
\]

while the best support-29 witness has 13 residence defects and upper-hole
vector

\[
(6,6,1,0,0,0,0).
\]

The other audited augmented-endpoint motif families also contain no resident
completion through support 35:

\[
\begin{array}{c|r|r|r}
\text{target}&\text{systems at cap 35}&\text{Hamilton}&
\min\text{ residence defects}\\ \hline
21641&2761981&64694&19\\
5801&814&13&20\\
13620&2174&0&-.
\end{array}
\tag{4.2}
\]

This proves a genuine residence obstruction for the retained motifs inside
the cycle-free closure.  It does **not** prove a global support-35 residence
obstruction.

## 5. Minimal scope counterexample

The path-only qualification cannot be dropped.  Starting from the unique
support-19 target-17738 minimum closure, add the disjoint atlas exchange cycle

\[
(3036,6620,7128).
\tag{5.1}
\]

The result is a valid successor matching of support 22, omitted by the native
path-only enumeration.  It is still non-Hamilton and has seven residence
defects; its purpose is solely to disprove the statement that the native
enumeration covers arbitrary completions of the same support.

The exact frontier is therefore:

1. globally, intrinsic single transfers are closed through support 9 and
   parent-pure transfers through support 7;
2. for the retained target motifs, the matching floors (3.1) are exact;
3. for the enumerated cycle-free forced closures, the residence no-go through
   support 35 is exact;
4. optional disjoint cycles, compositions of transfers, mixed-parent motifs
   outside the retained list, and parent-pure supports 8 and 9 remain open.

## 6. Reproducibility

Primary source and audit artifacts:

```text
scratch/search_k15_root_motif_exchange.cpp
SHA-256 43ec49e87e76086f87d2cc2da377053292d9de01a0c9bf959ab2847dec330873

scratch/k15_h29zero7_retained_motif_exchange_floors.json
SHA-256 dd51d735c4f16c9753c688f95f52ec38f29602bf5b30b67172380c4cefe7e407

scratch/k15_root17738_motif_mincost_full.json
SHA-256 de0bf5d75ea844c022a2413e6d8605728078359270244a15386665cbd9780e13

scratch/k15_root_motif_exchange_candidate_audit.json
SHA-256 744c3401937aa7329693e32048821d49fd43d556b69d29623fcf86de908f2aae
```

Frozen parents:

```text
P0 scratch/k15_doubletrans_05_213_hall29.json
   5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c
P1 scratch/k15_outer2_p1_h30_bridge.json
   6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
P2 scratch/k15_trans1113_balanced_hall31.json
   6d7cee2418f10dbd02076971fdd119d7bc7c35d154430522a70c06f953687ea7
P3 scratch/k15_transposition_parent_winner.json
   8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd
P4 scratch/k15_accumulated_zero_parent_winner.json
   2b25279185b50a9485c65cbc727a08d95b71a1d310332cbdcb23dd6b0b3d2cb7
```

The force motif used in the detailed target-17738 census is
`scratch/k15_force_root17738_motif_novel5.json`, SHA-256
`557509c895a251c32905512daa0c3e05c5f939fa835c51e870c64ce63f469c40`.
