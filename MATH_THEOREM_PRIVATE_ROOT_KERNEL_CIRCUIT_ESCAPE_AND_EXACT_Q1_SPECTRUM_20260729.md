# Private-root kernels, circuit escape, and the exact middle/q1 spectrum

Date: 2026-07-29

Status: proved an exact private-root reduction of weighted Hall, classified
the surviving minimal circuit types, gave three finite sufficient
root-expansion criteria, and derived a new exact-factor run-spectrum
fingerprint for the critical \(E_5\) circuit. Exact middle/\(q=1\)
injectivity is not yet proved to force compiler readiness, and no strict
\(k=15\) counterexample is constructed.

This note starts from
MATH_THEOREM_COMPILER_READY_DECORATED_PAIR_ROOT_ARC_CEGAR_20260729.md and
uses the audited minimal-circuit and \(E_5\) facts in
MATH_ATTACK_L_GRADED_HALL_AFTER_Q3_MINIMAL_CIRCUIT_20260729.md and
MATH_ATTACK_L_E5_CHRONOLOGY_AND_LAZY_HALL_CUT_20260729.md. Coordination
with the compact quotient implementation is through
THREAD_D_CLAUDE_COMPACT_QUOTIENT_EXACT_CORE_HALL_BENDERS_20260729.md only.

## 1. Normalize the composite weighted problem

Fix one legal equivariant omission-state cycle \(Z\), hence one core
\(C=P\setminus Z\). Let \(\mathcal F\) be the \(329\) full target orbits
of weight \(15\), and let \(e_3,e_5\) be the exceptional target orbits of
weights \(5,3\), respectively. All right quotient blocks have capacity
\(15\).

For a shore containing \(f\) full orbits, its integer block demand is

\[
 b(X)=
 \left\lceil {15f+5{\bf1}_{e_3\in X}
                    +3{\bf1}_{e_5\in X}\over15}\right\rceil
 =
 \begin{cases}
 f,&X\cap\{e_3,e_5\}=\varnothing,\\
 f+1,&X\cap\{e_3,e_5\}\ne\varnothing.
 \end{cases}
\tag{1.1}
\]

Let \(G_3\) be the ordinary unit-capacity quotient graph induced by
\(\mathcal F\cup\{e_3\}\), and define \(G_5\) analogously.

### Lemma 1.1 (two ordinary Hall tests)

The weighted \(k=15\) quotient graph passes Hall if and only if both
\(G_3\) and \(G_5\) pass ordinary Hall.

#### Proof

Weighted Hall restricted to full orbits is ordinary Hall. A shore of full
orbits together with one exceptional orbit needs one additional block by
(1.1), exactly the corresponding ordinary Hall inequality in \(G_3\) or
\(G_5\). A shore containing both exceptional orbits has the same threshold
\(f+1\), and its neighborhood contains the neighborhood obtained after
deleting either exceptional orbit. Thus either one-exception inequality
implies the two-exception inequality. The converse is immediate. \(\square\)

This normalization is a decision equivalence. It does not produce two
simultaneous physical matchings.

## 2. Exact private-root kernel

The following theorem is stated for the weighted graph because it is useful
beyond \(k=15\).

Let \(G=(L,R;E)\) have left demands \(0<w(\ell)\le k\), uniform right
capacity \(k\), and unbounded edge capacity. For \(X\subseteq L\), call a
right vertex \(r\) **private in \(X\)** when

\[
 |N(r)\cap X|=1.
\tag{2.1}
\]

Call \(K\subseteq L\) a **right-two-core** when every
\(r\in N(K)\) has at least two neighbors in \(K\). A zero-degree left
vertex is therefore itself a right-two-core.

Starting from \(L_0=L\), repeatedly choose a private right vertex in the
current shore, record its unique neighbor \(\ell_t\), and delete
\(\ell_t\). Stop when there is no private right vertex.

### Theorem 2.1 (unique private-root kernel and exact Hall reduction)

The terminal target set \(K_\infty\) is independent of all peeling choices
and is the unique greatest right-two-core. Moreover,

\[
 G\text{ saturates every left demand}
 \quad\Longleftrightarrow\quad
 G[K_\infty,N(K_\infty)]
 \text{ saturates every demand in }K_\infty.
\tag{2.2}
\]

In particular, \(K_\infty=\varnothing\) is a sufficient Hall certificate.

#### Proof

Let \(K\) be any right-two-core. Suppose inductively that \(K\) is contained
in the current target set. If the algorithm deletes \(\ell\) using a right
vertex \(r\) private to \(\ell\), then \(\ell\notin K\): otherwise
\(r\in N(K)\) would have at most one neighbor in \(K\), contrary to the
core property. Thus every right-two-core survives every peeling order.

At termination, every right vertex meeting the remaining target set has
degree at least two there, so the remainder is itself a right-two-core.
It contains every other such core and is therefore the unique greatest
one. This also proves independence of the choices.

If the full graph is feasible, Hall holds on every target subfamily and in
particular on \(K_\infty\). Conversely, suppose the kernel is feasible.
Read the peeling order backwards. When \(\ell_t\) was deleted, its recorded
block \(r_t\) had no neighbor among the targets surviving that deletion.
The recorded blocks are distinct, and none is used by the kernel flow.
Assign all \(w(\ell_t)\le k\) units of \(\ell_t\) to \(r_t\). Reversing all
deletions extends the kernel flow to every target. \(\square\)

For an omission-state core, each edge \(\ell r\) is a local root predicate
\(g_r^{\{\ell\}}(Z_r)=1\). Hence private-root peeling is a finite
root-motif reduction before any max-flow separator is called.

### Corollary 2.2 (peelable state-cycle criterion)

If a legal \(8/16\)-state cyclic omission path at \(k=15\) has empty
private-root kernels in both \(G_3\) and \(G_5\), then its weighted quotient
Hall graph passes and the decorated pair is compiler-ready.

More generally, every generated Hall row may be restricted to the two
terminal kernels.

This is the first useful sufficient carrier condition: find one legal
omission cycle whose root graph is private-peelable. It is stronger than
Hall but replaces exponentially many shores by a linear local certificate.

## 3. The exact residual motifs are unary zeros or transversal circuits

If an inclusion-minimal failed shore \(X\) contains a zero-degree target,
then that singleton is already failed, so minimality forces \(X\) to be
that unary target. Assume henceforth that all targets in \(X\) have
positive degree.

### Theorem 3.1 (complete minimal-shore classification and rooted escape)

If Hall fails in one terminal kernel and \(X\) is an inclusion-minimal
positive failed shore, then in \(G_3\) or \(G_5\), \(X\) is a
transversal-matroid circuit:

\[
 |N(X)|=|X|-1,
\tag{3.1}
\]

every proper subset of \(X\) is matchable, its incidence graph is
connected, and it has no private right block.

For every chosen root \(r\in X\), there is a bijection

\[
 M:X\setminus\{r\}\longrightarrow N(X).
\tag{3.2}
\]

Direct an arc \(u\to v\) when \(u\) is adjacent to \(M(v)\). Then every
vertex of \(X\) is reachable from \(r\). Conversely, (3.1), a bijection
(3.2), and this reachability imply that \(X\) is a circuit.

In physical weighted units, exactly one of the following occurs:

\[
\begin{array}{c|c|c}
\text{type}&\text{exceptional orbit in }X&\text{physical defect}\\ \hline
F&\text{none}&15\\
E_3&e_3&5\\
E_5&e_5&3.
\end{array}
\tag{3.3}
\]

The two exceptional orbits cannot both occur in a minimal weighted shore.

#### Proof

Ordinary Hall minimality in \(G_3,G_5\) gives (3.1) and matchability of
every proper subset. Disconnected target components have disjoint right
neighborhoods, so one component would already be deficient. A private
right block would let its unique target be deleted without reducing the
remaining neighborhood enough to remove the defect. Hence the incidence
is connected and has no private block.

Fix \(r\). A matching of \(X\setminus\{r\}\) has size \(|X|-1\), hence is
a bijection onto \(N(X)\). Run alternating reachability from the unmatched
root. If the reached target set \(A\) were proper, its reached right set
would be exactly \(M(A\setminus\{r\})\), so
\(|N(A)|=|A|-1\), contradicting matchability of proper subsets.

Conversely, flip \(M\) along a directed alternating path from \(r\) to
any \(x\). This matches \(X\setminus\{x\}\). Thus every one-vertex deletion,
and hence every proper subset, is matchable while (3.1) makes \(X\)
dependent.

Finally, write \(f\) for the number of full orbits and \(b=|N(X)|\).
The physical defect is
\[
 15(f-b)+5{\bf1}_{e_3\in X}+3{\bf1}_{e_5\in X}.
\]
Minimality bounds the positive defect by every member weight. Reduction
modulo \(15\) gives precisely (3.3), and simultaneous membership of
\(e_3,e_5\) would require a positive integer at most three congruent to
eight modulo fifteen. \(\square\)

Thus a minimal failed shore is a rooted alternating skeleton with no escape
block. For an incumbent circuit \(B=N(X)\), its valid necessary
one-new-block escape row is

\[
 \boxed{\quad
 \sum_{j\notin B}g_j^X(Z_j)\ge1.
 \quad}
\tag{3.4}
\]

This novelty row alone does not preserve old neighbors. The complete exact
Hall row is

\[
 \sum_jg_j^X(Z_j)\ge |X|.
\tag{3.5}
\]

Every summand is a local omission-state/root-collar motif. The skeleton
itself can be global.

## 4. Finite sufficient root-expansion criteria

### 4.1 Ordered private ears

For a fixed state cycle, put

\[
 a_{Oj}=g_j^{\{O\}}(Z_j),\qquad
 d_O=\sum_ja_{Oj},\qquad
 c_{OR}=\sum_ja_{Oj}a_{Rj}.
\tag{4.1}
\]

### Proposition 4.1 (ordered private-ear expansion)

Suppose the target orbits admit an order \(O_1,\ldots,O_s\) such that

\[
 \sum_j a_{O_tj}\prod_{u>t}(1-a_{O_uj})\ge1
 \qquad(1\le t\le s).
\tag{4.2}
\]

Then weighted Hall passes. The stronger pairwise condition

\[
 d_{O_t}>\sum_{u>t}c_{O_tO_u}
\tag{4.3}
\]

implies (4.2).

#### Proof

Equation (4.2) supplies a block adjacent to \(O_t\) and to no later target.
These blocks are automatically distinct, and reversing the order assigns
the entire demand \(w(O_t)\le15\) to its block. This is exactly a complete
private-root peeling certificate.

For (4.3), the union bound says that the number of neighbors of \(O_t\)
shared with at least one later orbit is at most the displayed codegree sum.
At least one unshared neighbor remains. \(\square\)

Conditions (4.2) are finite local root/state motifs once the order is
given. A carrier/core master may seek the omission cycle and the order
together.

### 4.2 Reciprocal local load

### Proposition 4.2 (uniform reciprocal-load expansion)

If every \(d_O>0\) and

\[
 L_j:=
 \sum_{O:a_{Oj}=1}{w(O)\over15d_O}\le1
 \qquad\text{for every block }j,
\tag{4.4}
\]

then weighted Hall passes.

#### Proof

Spread the normalized demand \(w(O)/15\) uniformly over the \(d_O\)
neighbors of \(O\). Equation (4.4) is exactly the statement that no
unit-capacity quotient block is overloaded. This is a feasible fractional
flow; integral network capacities then give a saturating integral flow.
\(\square\)

A master-friendly sufficient version chooses integers \(\ell_O\ge1\),
imposes \(d_O\ge\ell_O\), and permits only local states satisfying

\[
 \sum_{O:a_{Oj}=1}{w(O)\over15\ell_O}\le1.
\tag{4.5}
\]

It replaces all Hall shores by \(331\) additive degree rows and at most
sixteen local load tests per layer. Private ears may be removed first and
(4.5) applied only to the residual kernel.

### 4.3 A condition genuinely using exact q1 injectivity

Assume now that the physical rank-seven row

\[
 B_i=D^2P_i
\tag{4.6}
\]

enumerates every rank-seven set exactly once. For physical targets \(S,R\),
let \(d(S)\) and \(c(S,R)\) denote their degree and codegree in the physical
containment graph of the chosen core.

### Proposition 4.3 (exact-q1 codegree bound)

\[
 c(S,R)\le
 \begin{cases}
 \displaystyle {15-|S\cup R|\choose7-|S\cup R|},
       &|S\cup R|\le5,\\[2mm]
 0,&|S\cup R|>5.
 \end{cases}
\tag{4.7}
\]

Consequently, an ordering \(S_1,\ldots,S_{4943}\) of the physical flexible
targets satisfying

\[
 d(S_t)>
 \sum_{\substack{u>t\\|S_t\cup S_u|\le5}}
 {15-|S_t\cup S_u|\choose7-|S_t\cup S_u|}
\tag{4.8}
\]

is a private-ear compiler certificate.

#### Proof

If \(S,R\) share position \(i\), then
\[
 S\cup R\subseteq P_i\subseteq B_i.
\]
The first containment is impossible when \(|S\cup R|>5\). Otherwise the
injective rank-seven label \(B_i\) is one of exactly the number of
rank-seven supersets displayed in (4.7). This proves the bound. Equation
(4.8) and the union bound leave a neighbor of \(S_t\) unused by every later
target, so Proposition 4.1 applies physically. \(\square\)

This is a strong sufficient condition, not a claim that exact q1
injectivity automatically makes (4.8) true.

## 5. A terminal-rank reserve

Exact lower-q3 support says every rank-five target orbit occurs among the
envelopes \(P_j\). There are \(201\) such orbits.

### Theorem 5.1 (rank-five private reserve)

Choose one quotient block \(J_O\) with \(P_{J_O}\in O\) for each rank-five
orbit \(O\), and impose

\[
 Z_{J_O}=\varnothing.
\tag{5.1}
\]

The \(201\) blocks are automatically distinct. Assign every full rank-five
orbit phasewise inside its block, and assign the three physical members of
\(e_5\) to three positions of its block.

If the remaining legal omission cycle on the other \(228\) blocks passes
weighted Hall for the \(130\) target orbits of ranks at most four, then the
whole compiler exists. The residual minimal circuits have only types
\(F\) and \(E_3\).

#### Proof

A quotient block has one rank-five envelope orbit, so blocks chosen for
different \(O\) are distinct. Empty omission makes \(C=P\) throughout each
selected physical block. For a full orbit the fifteen phases of \(P\) are
its fifteen targets; for \(e_5\), the three targets each occur five times,
so three distinct positions suffice.

Empty omission states conflict with no adjacent state. Reserve these
positions and targets. A residual matching on the other blocks is disjoint,
and adjoining the rank-five assignments gives a physical saturating
matching. No rank-five exceptional orbit remains in a residual shore.
\(\square\)

This theorem does not hide the critical \(E_5\) circuit. If its sole
\(e_5\) block is also the singleton orbit's sole root block, reserving that
block makes the singleton unary-zero in the residual problem.

## 6. Calibrations

### 6.1 The exact \(k=11\) pass is private-peelable

For the audited strict \(k=11\) carrier and its canonical equivariant core,
all \(21\) target orbits have full weight eleven. A tiny solver-free
extension of the existing quotient-graph audit gives the following
private-peeling certificate, written as

\[
 \text{target-orbit representative}:\text{private quotient block}:
\]

    7:2 13:37 5:3 11:41 3:18 1:16 19:0
    9:23 17:40 21:9 25:1 35:11 33:8 37:6
    41:5 49:14 67:31 69:10 73:17 81:30 137:4

Each displayed block is private relative to that target and the suffix of
the list. Thus Theorem 2.1 certifies Hall without a min-cut row.

The source selector has SHA-256

    05832de6a2aa7191dc99dc7133b67b852539278a930cf717bb12ed9a301616e7

and the existing audit is
scratch/audit_k11_equivariant_graded_quotient_hall.py, SHA-256

    d168e12e993a61ea772e829e5d46de8bf9e456aede494a2913e0cbd852ca0c30.

The reciprocal-load condition is not necessary: its largest normalized
block load on this same graph is \(97/60>1\), while private peeling
succeeds.

### 6.2 The \(E_5\) circuit is a two-vertex kernel component

In the critical defect-three configuration, the singleton orbit \(U\) and
\(e_5\) have the same unique block \(J_*\). In the graph induced by these
two targets and their neighborhood,

\[
 N(U)=N(e_5)=\{J_*\}.
\tag{6.1}
\]

Thus \(\{U,e_5\}\) is a two-vertex transversal circuit, and it is contained
in the terminal private-root kernel of the full graph.  The present audit
does not show that no other nonpeelable targets also survive.  This
circuit's physical demand is \(15+3\) against capacity \(15\). Its
normalized reciprocal load at \(J_*\) is

\[
 1+{3\over15}={6\over5}.
\tag{6.2}
\]

For this fixed core, a second block adjacent to either \(U\) or \(e_5\)
creates the required escape and settles the induced two-orbit compiler.
Equivalently, this local circuit disappears when
\(|N(U)\cup N(e_5)|\ge2\).  This statement concerns the fixed-core
neighborhoods: an adaptive forced-port set defined before choosing the
omission cycle is not interchangeable with \(N_C(U)\).

## 7. What exact middle/q1 injectivity really adds

The private-root automaton alone does not use exact-once middle and q1
labels. The following identity records their complete one-set trace
consequence.

Assume \(T=(T_i)\) enumerates all rank-eight subsets of \([15]\) exactly
once and the edge colors \(T_i\cap T_{i+1}\) enumerate all rank-seven
subsets exactly once. For \(A\subseteq[15]\), \(1\le|A|=s\le7\), put

\[
 \chi_A(i)={\bf1}_{A\subseteq T_i}.
\tag{7.1}
\]

### Theorem 7.1 (exact subset-run census)

The cyclic trace \(\chi_A\) has

\[
 M_s={15-s\choose8-s}
\tag{7.2}
\]

positive positions,

\[
 E_s={15-s\choose7-s}
\tag{7.3}
\]

positive-positive edges, and therefore

\[
 R_s=M_s-E_s
\tag{7.4}
\]

positive runs. Explicitly,

\[
\begin{array}{c|rrrrrrr}
s&1&2&3&4&5&6&7\\ \hline
M_s&3432&1716&792&330&120&36&8\\
E_s&3003&1287&495&165&45&9&1\\
R_s&429&429&297&165&75&27&7.
\end{array}
\tag{7.5}
\]

#### Proof

Exact middle-deck injectivity gives (7.2), because that is the number of
rank-eight supersets of \(A\). Exact q1 injectivity gives (7.3), because
the positive-positive carrier edges are precisely the rank-seven edge
colors containing \(A\). In a nonconstant cyclic binary trace, the number
of positive runs equals the number of positive vertices minus the number
of positive-positive edges. This proves (7.4)--(7.5). \(\square\)

### Corollary 7.2 (finite spectrum of a genuine critical \(E_5\) circuit)

Assume additionally three-residence and strict unit-voltage equivariance

\[
 T_{i+N}=\rho^vT_i,\qquad \gcd(v,15)=1,
\]

where \(N=W/15=429\),
and let

\[
 P_i=T_i\cap T_{i-1}\cap T_{i-2}\cap T_{i-3},
\]

and suppose the critical circuit has

\[
 \mathcal E=\mathcal L=\{J_*\}.
\tag{7.6}
\]

For each of the three exceptional rank-five sets \(Q\in e_5\), its trace
\(\chi_Q\) has exactly five runs of length four, no run of length at least
five, and

\[
 (n_1,n_2,n_3,n_4)
 =(40+t,\ 30-2t,\ t,\ 5)
\tag{7.7}
\]

for

\[
 t\in\{0,5,10,15\}.
\]

Equivariance forces the same \(t\) for all three exceptional sets.

#### Proof

Because \(P_i\) has rank five,

\[
 P_i=Q
 \quad\Longleftrightarrow\quad
 \chi_Q(i-3)=\chi_Q(i-2)=\chi_Q(i-1)=\chi_Q(i)=1.
\tag{7.8}
\]

Consequently, if the positive \(Q\)-runs have lengths \(\ell\), then

\[
 \#\{i:P_i=Q\}=\sum_{\text{\(Q\)-runs}}(\ell-3)_+.
\tag{7.9}
\]

One exceptional quotient block has fifteen physical positions and contains
each of the three members of \(e_5\) five times. Thus \(Q\) has exactly five
\(P\)-occurrences.

At those five positions the common singleton-port block rotates through
the five coordinates of \(Q\). If its port is \(\{x\}\), the exact
four-step return identity says that \(x\) occupies precisely the four
middle states in (7.8). Therefore the containing \(Q\)-run has length
exactly four. The five \(P\)-occurrences give five distinct length-four
runs. Any further run of length at least four would create another
\(P_i=Q\), so none exists.

Theorem 7.1 gives \(75\) runs and \(120\) positive positions. Hence
\[
 n_1+n_2+n_3=70,\qquad
 n_1+2n_2+3n_3=100,
\]
which is equivalent to (7.7). Unit-voltage time translation realizes
coordinate rotation, so the three exceptional traces have the same run
spectrum. Moreover,

\[
 \chi_Q(i+3N)=\chi_Q(i),
\]

because \(\rho^{3v}\) stabilizes every member \(Q\) of \(e_5\). The
nonconstant cyclic trace is therefore five repetitions of a length-\(3N\)
cyclic trace, so every run multiplicity is divisible by five. In particular
\(5\mid t=n_3\), giving the four displayed values. \(\square\)

This reduces the exact-factor \(E_5\) obstruction to four synchronized
run spectra. It does not contradict any of them. For comparison, the
per-coordinate exact census is arithmetically compatible with one
length-four run, \(427\) length-eight runs, and one length-twelve run.
Thus middle/q1 moment identities alone do not force a second root block.

## 8. Why no bounded local motif theorem follows yet

Finite omission-state size does not bound circuit support. Abstractly, for
any tree \(H\), take its vertices as targets and one right block for each
tree edge, adjacent to its two endpoints. The whole target shore has
\(|X|-1\) blocks. Every proper target shore \(Y\) has at least \(|Y|\)
incident tree edges: each component of \(H[Y]\) has one fewer internal edge
than vertices and at least one boundary edge. Hence the whole shore is a
transversal circuit of arbitrary size, although every right motif has
degree two.

This graph-theoretic family proves that finite state count and bounded
right-motif degree, by themselves, cannot bound circuit support. It does
not prove that the family is realizable by the omission automaton of an
exact carrier. What is not known is whether one can embed such a kernel
into one exact rank-eight/rank-seven Hamilton factor while retaining
residence and all shadows. No strict exact-factor counterexample is
presently available.

The sharp remaining positive lemma must retain the common-state quantifier:

> **Exact-factor circuit escape lemma.** Every resident, shadow-complete,
> exact middle/q1 \(k=15\) carrier admits one legal common omission-state
> cycle \(Z\) with the following property. For every tuple
> \((X,r,M,B)\) in either normalized graph \(G_3(Z)\) or \(G_5(Z)\), where
> \(r\in X\), \(B\subseteq N_Z(X)\),
> \(M:X\setminus\{r\}\to B\) is a bijective matching, and the associated
> alternating orientation makes every member of \(X\) reachable from
> \(r\), one has \(N_Z(X)\setminus B\ne\varnothing\).

For the two-vertex \(E_5\) skeleton, this requires ruling out all four
spectra (7.7) under \(\mathcal E=\mathcal L=\{J_*\}\). Equivalently, one
must prove that exact chronology forces
\(|\mathcal L\cup\mathcal E|\ge2\): a second singleton-port or
exceptional-envelope block.

## 9. Proved boundary

The omission automaton plus exact middle/q1 injectivity has not been shown
to force all Hall shores. What is now proved is:

1. Hall reduces exactly to the unique private-root kernels;
2. empty kernels give a finite local root-expansion certificate;
3. every minimal residual is either a unary zero or one of the three
   positive circuit types \(F,E_3,E_5\); retaining a circuit's incumbent
   \(|X|-1\) blocks reduces repair to one escape block, while an
   unrestricted state change still requires the complete row (3.5);
4. private-ear, reciprocal-load, and exact-q1 codegree inequalities are
   sufficient expansion theorems;
5. the audited \(k=11\) pass is completely private-peelable;
6. reserving all terminal-rank blocks removes \(E_5\) from the residual
   problem without pretending to repair the critical singleton conflict;
7. a genuine critical \(E_5\) carrier must realize one of the four exact
   run spectra (7.7); and
8. finite state count and bounded local incidence degree alone do not
   bound circuit size; realizability inside the exact carrier automaton
   remains open.

The next proof must use global exact-factor chronology to establish circuit
escape, not another unweighted positive-degree or local-collar screen.
