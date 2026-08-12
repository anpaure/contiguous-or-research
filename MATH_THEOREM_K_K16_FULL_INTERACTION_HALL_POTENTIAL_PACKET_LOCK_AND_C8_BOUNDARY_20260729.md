# K16 full-interaction Hall potential, packet locks, and the C8 boundary

Date: 2026-07-29  
Lane: K  
Status: exact potential, certified deficiency 15, frozen detector descent through 73, and a finite local-minimum criterion  
Scope: the fixed `resume1` resident endpoint and the named physical q1 factors

## 1. Verdict

There is a canonical integer potential for the fixed-overlay residence problem.
It is not the number of raw motifs, static blockers, saturation cores, or cores
returned by one propagation order.  If \(\mathscr C_R(Q)\) is the hypergraph
of inclusion-minimal motif sets that are jointly incompatible with degree and
both q1 palettes, then the exact number of unavoidable inherited-motif holes is

\[
\boxed{\Delta_R(Q)=\tau(\mathscr C_R(Q)).}
\]

Every family of pairwise motif-disjoint Hall cores gives a lower bound on this
potential.  A feasible overlay assignment gives the complementary upper bound.
Strict descent is proved only when the two bounds cross; lowering the size of
one greedily peeled core packing does not prove that \(\Delta_R\) decreased.
For a fixed reverse-closed wrapper class, the lexicographic refinement
\(\Psi=(\Theta,\text{minimum wrapper radius})\) is nonincreasing under an
exact lex-minimizing rethread and equals \((0,0)\) exactly at a resident
factor.  It need not decrease strictly inside a neutral packet class.

This distinction changes the interpretation of the corrected portal beam.
The saved, q1-complete physical chain has peeled-core counts

\[
27,21,18,16,14,12,11,9,8,7,6,5,4,3,2,1.
\]

These are sixteen separate certified lower bounds, not values of
\(\Delta_R\).  At the last score-one state, all connected q1-support-preserving
alternating \(C_4/C_6\) moves through the displayed packet support were
enumerated: exactly two exist and neither clears the detector.  A radius-four
alternating \(C_8\) does clear every peeled unit core, producing score
\((0,0,0,2250,4)\).  It uses q1 duplicate slack.  The zero score means only
that this unit-propagation procedure found no core; it is not a feasible
overlay witness and does not prove \(\Delta_R=0\).

In fact all three score-zero endpoints are infeasible for an exact,
solver-free reason.  They share one inherited occurrence whose motif row and
eight palette/degree rows sum to the real Farkas contradiction
\(0\le-1\).  Exact branch replay strengthens this to fourteen distinct
singleton motif circuits at every endpoint; a motif-disjoint two-occurrence
serial packet supplies one further unit.  Consequently

\[
\boxed{\Delta_R(Q_i)\ge15\qquad(i=0,1,2).}
\]

The complete two-choice failed-literal banks have
sizes

\[
95,93,93.
\]

This stronger score is actionable.  At candidate 1 an explicit
q1-cover-preserving \(C_6\) deletes the common affine occurrence and four
successive \(C_8\)'s attack successive branch cores.  The frozen displayed
chain is

\[
\boxed{93\longrightarrow86\longrightarrow81\longrightarrow78
\longrightarrow76\longrightarrow73.}
\]

Separately, a three-step sequence of pairwise vertex-disjoint
q1-cover-preserving \(C_6\)'s kills the two serial-packet motifs and changes a
support row of the common affine packet, giving

\[
\boxed{93\longrightarrow87\longrightarrow84\longrightarrow82.}
\]

Every prefix in both paths remains a simple spanning degree-two factor with
zero lower- or upper-q1 holes.  Neither final state is claimed feasible: the
displayed last state still has 73 two-branch refutations.  Thus the full failed-literal
bank, rather than the unit-core count, is the correct current proof-directed
descent potential.

For any fixed finite trade library, orienting only strict
\(\Phi_{\rm FL}\)-decreases gives a path of length at most its initial score
and terminates at a library-local minimum.  A proof/eligibility-halo census is
an exact finite certificate for such a minimum.  No complete outgoing census
is frozen for \(Q_{73}\), so the displayed chain is not a convergence claim.

There is also a genuine packet lock.  In the strict-load-neutral,
core-directed connected \(C_4/C_6\) library, the two saved factors
\(F_1,F_2\) form a closed two-state class.  Each carries a Hall core tied to
the same locked endpoint socket, and the unique strict \(C_6\) that hits the
current packet is the inverse of the preceding one.  Thus a universal strict
descent theorem is false for that architecture.  The no-go does not cover
q1-slack moves, remote neutral routers, disconnected exchanges, larger
circuits, or a moving resident endpoint.

No H100 job was launched for this report.  All new work below is proof or
lightweight replay of already saved artifacts.

## 2. The exact fixed-overlay system

Fix a resident spanning two-factor \(R\) and a q1-complete spanning
two-factor \(Q\) of the physical Johnson graph.  Put

\[
B=Q\setminus R,\qquad A=R\setminus Q.
\]

For \(e\in B\), let \(b_e=1\) mean that \(e\) is removed from \(Q\).  For
\(f\in A\), let \(a_f=1\) mean that \(f\) is inserted.  The base system
\(\mathcal B_R(Q)\) consists of the binary bounds

\[
a_f,b_e\in\{0,1\},
\tag{2.1}
\]

the exact endpoint balances

\[
\sum_{f\in A(v)}a_f=\sum_{e\in B(v)}b_e
\quad\text{for every middle vertex }v,
\tag{2.2}
\]

and, for every lower or upper q1 colour \(c\),

\[
\sum_{e\in B_c}b_e-\sum_{f\in A_c}a_f
\le \mu_Q(c)-1.
\tag{2.3}
\]

The zero vector belongs to \(\mathcal B_R(Q)\).  If \(M\) is a current
short-run occurrence and \(C_M\) is its complete entering/internal/exiting
cut collar, then that inherited occurrence is destroyed if and only if

\[
\sum_{e\in C_M\cap B}b_e\ge1.
\tag{2.4}
\]

Here \(\mathcal M(Q)\) is occurrence-labelled: distinct short-run occurrences
remain distinct vertices even if they induce identical inequalities or edge
closures.  For
\(x=(a,b)\in\mathcal B_R(Q)\), write

\[
H_Q(x)=\{M\in\mathcal M(Q):x\text{ violates (2.4) for }M\}.
\]

The exact inherited-motif deficiency is

\[
\Delta_R(Q)=\min_{x\in\mathcal B_R(Q)}|H_Q(x)|.
\tag{2.5}
\]

Indeed, the complete collar survives in
\(G=(Q\setminus D_b)\cup A_a\) exactly when every one of its old edges
survives.  Moreover \(\mathcal B_R(Q)\) is exactly the family of factors
\(G\) satisfying

\[
Q\cap R\subseteq G\subseteq Q\cup R
\]

and preserving both q1 supports: (2.2) is precisely degree two, while (2.3)
is \(\mu_G(c)\ge1\); the converse is immediate by reading off the removed and
inserted shores.

This is a fixed-overlay quantity.  Even \(\Delta_R(Q)=0\) would not by
itself exclude new motifs created at added seams; a materialized endpoint
must be re-audited and, if necessary, re-centred.

## 3. Hall-core transversal theorem

Define the **full interaction circuit hypergraph**
\(\mathscr C_R(Q)\) on vertex set \(\mathcal M(Q)\).  Its hyperedges are the
inclusion-minimal sets \(S\subseteq\mathcal M(Q)\) for which

\[
\mathcal B_R(Q)+\{\text{row (2.4) for every }M\in S\}
\]

is infeasible over the binary variables.

### Theorem 3.1 (exact potential)

For every fixed pair \((R,Q)\),

\[
\boxed{\Delta_R(Q)=\tau(\mathscr C_R(Q)).}
\tag{3.1}
\]

Equivalently,

\[
|\mathcal M(Q)|-\Delta_R(Q)
\]

is the maximum number of inherited motif rows that can be hit
simultaneously while preserving degree and both q1 palettes.

#### Proof

For \(x\in\mathcal B_R(Q)\), the hole set \(H_Q(x)\) meets every circuit.
Otherwise \(x\) would satisfy all rows of an infeasible circuit.  Hence
\(|H_Q(x)|\ge\tau(\mathscr C_R(Q))\), and minimization gives
\(\Delta_R(Q)\ge\tau\).

Conversely, let \(H\) be a minimum transversal.  If the base system together
with all motif rows in \(\mathcal M(Q)\setminus H\) were infeasible, finiteness
would supply an inclusion-minimal infeasible subset disjoint from \(H\).  That
subset would be a circuit missed by the transversal.  Thus the rows outside
\(H\) are jointly feasible, so \(\Delta_R(Q)\le|H|=\tau\).  This proves
(3.1). \(\square\)

### Corollary 3.2 (core packing)

If \(P_1,\ldots,P_p\) are infeasible motif packets with pairwise disjoint
motif-row sets, then

\[
p\le\nu(\mathscr C_R(Q))\le\tau(\mathscr C_R(Q))=\Delta_R(Q).
\tag{3.2}
\]

Indeed, shrink each packet to a minimal circuit.  Their motif sets remain
disjoint.

### Corollary 3.3 (proof-safe strict descent certificate)

Fix the same resident \(R\), and suppose \(p\ge1\).  If \(Q\) has \(p\)
pairwise motif-disjoint infeasible packets, while a displayed
\(x'\in\mathcal B_R(Q')\) satisfies

\[
|H_{Q'}(x')|\le p-1,
\]

then

\[
\Delta_R(Q')\le p-1<p\le\Delta_R(Q).
\tag{3.3}
\]

Thus strict descent requires an upper witness at the new state, not merely a
smaller core packing.

### Theorem 3.4 (global wrapper potential)

Let \(\mathfrak W\) be any fixed finite class of q1-complete spanning
two-factors on the same finite graph, for example a reverse-closed
AA-square/BB-cycle/C6 trade orbit.  Regard every motif as
occurrence-labelled.  For
\(F,G\in\mathfrak W\), put

\[
u_F(G)=\#\{M\in\mathcal M(F):C_F(M)\subseteq G\}.
\tag{3.4}
\]

Thus \(u_F(G)\) counts old occurrences of \(F\) whose complete collars remain
unhit in \(G\).  Define

\[
\Theta_{\mathfrak W}(F)=\min_{G\in\mathfrak W}u_F(G)
\tag{3.5}
\]

and

\[
R_{\mathfrak W}(F)=
\min\{|F\setminus G|:G\in\mathfrak W,
                     u_F(G)=\Theta_{\mathfrak W}(F)\}.
\tag{3.6}
\]

Then

\[
\Psi_{\mathfrak W}(F)=
(\Theta_{\mathfrak W}(F),R_{\mathfrak W}(F))
\tag{3.7}
\]

is a global lexicographic potential in the following exact sense.  If \(G\)
attains both minima (3.5)--(3.6), then

\[
\Psi_{\mathfrak W}(G)
\le_{\rm lex}\Psi_{\mathfrak W}(F).
\tag{3.8}
\]

Moreover,

\[
\Psi_{\mathfrak W}(F)=(0,0)
\quad\Longleftrightarrow\quad
F\text{ has no short motif.}
\tag{3.9}
\]

#### Proof

The complete entering/internal/exiting collar determines the same
coordinate-labelled local occurrence in any two degree-two factors containing
it, up to reversal.  Thus common-collar occurrences of \(F\) and \(G\) are in
a multiplicity-preserving involutive bijection, and

\[
u_G(F)=u_F(G)=\Theta_{\mathfrak W}(F).
\]

Using \(F\) as a candidate wrapper for \(G\) gives

\[
\Theta_{\mathfrak W}(G)\le u_G(F)=\Theta_{\mathfrak W}(F).
\]

If this inequality is strict, (3.8) follows.  If equality holds, \(F\) is
itself a \(\Theta\)-optimal wrapper for \(G\), so

\[
R_{\mathfrak W}(G)\le|G\setminus F|
=|F\setminus G|=R_{\mathfrak W}(F),
\]

where the middle equality uses the common edge cardinality of spanning
two-factors.  This proves (3.8).

If \(\Psi(F)=(0,0)\), a radius-zero minimizing witness must be \(G=F\), and
then \(u_F(F)=|\mathcal M(F)|=0\).  The converse is immediate. \(\square\)

Define a new wrapper hypergraph \(\mathscr C_{\mathfrak W}(F)\) on
\(\mathcal M(F)\): its hyperedges are the inclusion-minimal
\(S\subseteq\mathcal M(F)\) for which no \(G\in\mathfrak W\) destroys every
collar in \(S\).  The proof of Theorem 3.1 gives

\[
\Theta_{\mathfrak W}(F)=\tau(\mathscr C_{\mathfrak W}(F)).
\]

This wrapper hypergraph agrees with \(\mathscr C_R(F)\) only when
\(\mathfrak W\) is exactly the family represented by \(\mathcal B_R(F)\) and
collar survival is encoded by (2.4).  The result gives a nonincreasing
**doubly minimizing** rethread, but not a bounded-radius implementation and
not strict descent at every nonterminal state.  Equality can persist around
a neutral class; Section 5 gives the corresponding packet-lock obstruction.

## 4. Why no unoriented local statistic can be a Lyapunov function

A physical alternating circuit is invertible.  Hence the following argument
applies to a state-valid exchange relation declared reverse-closed; it does
not apply automatically to a source-filtered/core-directed generator or an
oriented controller.  If a statistic \(P\) were nonincreasing along every
edge of such a relation, then for
each edge \(Q\leftrightarrow Q'\) one would have both

\[
P(Q')\le P(Q),\qquad P(Q)\le P(Q'),
\]

so \(P\) would be constant on every connected component of the trade graph.
The displayed peeled-core statistic is not constant: the saved moves include
\(30\to29\) and \(29\to27\), and their inverses give increases.  Therefore
this peeled statistic is not an unoriented Lyapunov function.  More generally,
any named statistic can be nonincreasing on a reverse-closed component only
if it is constant there.  The saved counts do not show that either the exact
maximum packing or \(\Delta_R\) is nonconstant.

The exact termination formulation is oriented.  For a finite legal-move
graph \(\Gamma\) and an exact success set \(Z\), put

\[
d_\Gamma(Q,Z)=\min\{\text{length of a directed path from }Q\text{ to }Z\},
\]

with value \(\infty\) if no such path exists.  If
\(0<d_\Gamma(Q,Z)<\infty\), the first edge of a shortest path decreases the
distance by one.  If \(d_\Gamma(Q,Z)=\infty\), the finite reachable subgraph
contains a terminal strongly connected class disjoint from \(Z\).  Such a
class is a graph-theoretic terminal lock; it becomes a Hall packet lock only
after Theorem 5.1's transport hypotheses are verified.  For a fixed-overlay
stage one may take \(Z=\{Q:\Delta_R(Q)=0\}\); for the full CEGAR one must take
\(Z\) to be the literally re-audited residence-clean endpoints.

## 5. Transported-packet obstruction

### Theorem 5.1 (packet-lock certificate)

Fix \(Q_0\) and suppose it has \(p\) infeasible packets

\[
P_1(Q_0),\ldots,P_p(Q_0)
\]

with pairwise disjoint motif sets.  Suppose every allowed transition
\(Q\to Q'\) maps every certified family of \(p\) pairwise motif-disjoint
\(\mathcal B_R(Q)\)-infeasible packets to a family of \(p\) pairwise
motif-disjoint \(\mathcal B_R(Q')\)-infeasible packets.  Then every state
\(Q\) reachable from \(Q_0\) satisfies

\[
\Delta_R(Q)\ge p.
\tag{5.1}
\]

In particular, the reachable class contains no state of exact deficiency
zero.

#### Proof

Induct on path length from \(Q_0\).  The transport hypothesis preserves a
family of \(p\) disjoint infeasible packets at every step, and Corollary 3.2
then gives \(\Delta_R(Q)\ge p\). \(\square\)

The hypothesis is deliberately stronger than “the current motif was moved.”
A trade must annihilate or merge a full interaction packet; translating its
motif row while preserving its palette/endpoint halo does not count as
descent.

## 6. The exact strict-token two-state lock

Let \(F_1\) be the factor after the first strict-token portal and \(F_2\) the
factor after the second.  In \(F_1\), the translated motif closure is

\[
\{(37531,37785),(37531,41627),(41627,41657)\}.
\tag{6.1}
\]

The conditional closure edge \((37531,41627)\) has sole resident replacement
\((33467,49819)\).  The two selected source edges at socket \(49819\),

\[
(49819,49881),\qquad(49819,53787),
\]

are locked by unique q1 rows.  Degree balance therefore forbids the sole
replacement, while unique rows lock the other closure edges.  This is an
exact Hall packet.

The unique strict-token connected \(C_6\) through its decorated blue halo is

\[
\begin{aligned}
D_2={}&\{(41147,57499),(41627,41657),(57529,58009)\},\\
A_2={}&\{(41147,41627),(41657,58009),(57499,57529)\}.
\end{aligned}
\tag{6.2}
\]

Both lower-token multisets are \(\{41115,41625,57497\}\), and both upper-token
multisets are \(\{41659,57531,58041\}\).  It maps \(F_1\) to \(F_2\).  The
new motif closure is

\[
\{(37051,41147),(37531,41627),(41147,41627)\},
\tag{6.3}
\]

and it is tied to the same locked socket.

The complete core-directed census gives:

- at \(F_1\), 48 raw alternating \(C_4\) incidences through the five
  decorated blue edges and no strict-token \(C_4\);
- at \(F_2\), 53 such incidences and no strict-token \(C_4\);
- at each state, exactly one strict-token \(C_6\) hitting the current
  decorated packet; the two witnesses are inverse.

Hence the strict-load-neutral, connected, radius-at-most-three,
core-directed state graph is exactly

\[
F_1\longleftrightarrow F_2,
\tag{6.4}
\]

and Theorem 5.1 applies with \(p=1\).  This is the promised precise packet
lock.  It is architecture-specific: a move not initially touching the packet
may act as a neutral router, and support-preserving q1-slack moves are not in
this strict fibre.

## 7. The corrected 27-core census

Replaying the old three-move beam with the corrected full interaction
analyser gives

\[
(30,554)\to(29,548)\to(27,461)\to(27,501),
\tag{7.1}
\]

where each pair is

\[
(\text{peeled unit-core packets},\text{union of proof-row tags}).
\]

The last move clears the old scalar saturation score but leaves the full
peeled count unchanged.  The current final packing consists of 27 independently
unit-refuted packets on 39 pairwise distinct motif rows.  Therefore

\[
\boxed{27\le\nu(\mathscr C_R(Q))\le\Delta_R(Q).}
\tag{7.2}
\]

No base-feasible assignment with at most 27 holes has been exhibited, so
equality is not proved.  The
frozen report's row-union value 517 is stale: the current source replays the
same factor with row union 501.  The count 27 is stable across that source
drift, but row-union size is neither canonical nor safe as a theorem
invariant.

The interaction is genuinely nonlocal.  Joining the 27 packets by shared
nonmotif q1/endpoint rows gives component sizes

\[
17,4,2,1,1,1,1,
\]

whereas joining them only by shared physical closure edges gives two
two-packet components and 23 singletons.  This is why a raw-motif or
pointwise-blocker potential misses the obstruction.

## 8. Corrected protected-token chain and the last C4/C6 gate

The linked portal24 artifacts give the exact saved sequence

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
\widehat\nu_{\mathrm{peel}}&27&21&18&16&14&12&11&9&8&7&6&5&4&3&2&1\\
\text{row union}&501&390&301&249&226&213&166&150&110&86&64&49&42&18&12&7.
\end{array}
\tag{8.1}
\]

Every displayed endpoint is a literal degree-two Johnson factor with zero
lower and upper q1 holes.  The chain uses six \(C_4\)'s and nine \(C_6\)'s.
Only the \(8\to7\) move preserves both lower and upper token multisets
exactly.  One other move is lower-strict only, one is upper-strict only, and
the remaining twelve spend or transport duplicate q1 tokens.  Thus this is a
protected-token-flow chain, not a strict-token chain.

At the score-\((1,7,0,2248,3)\) state the sole displayed unit core uses motif
565 and five blue proof edges.  The complete core-focused radius-\(\{2,3\}\)
generator produces exactly two q1-support-preserving connected exchanges.
Neither reaches zero.  Its lexicographically best endpoint has score

\[
(1,3,1,2248,3)
\]

and contains the literal static packet motif 1839 with closure

\[
\{(33715,41395),(34233,41401),(41395,41401)\}.
\tag{8.2}
\]

The common edge is \((33715,41395)\).  Upper row \(U42425\) locks
\((34233,41401)\), and lower row \(L41393\) locks
\((41395,41401)\).  Hence the two removable variables satisfy

\[
x=0,\qquad y=0,qquad x+y\ge1,
\]

an exact one-motif circuit.  This proves \(\Delta_R\ge1\) there.  It does not
prove \(\Delta_R=1\).

The radius-\(\{2,3\}\) failure is exhaustive only for connected moves through
the current peeled-core blue support.  It does not exclude a remote neutral
router followed by a splitter.

## 9. The support-neutral C8 escape and its exact meaning

Widening the last score-one scan to radius four produces 17 connected
q1-support-preserving candidates.  Exactly three have zero peeled unit cores.
The saved best \(C_8\) is

\[
\begin{aligned}
D_8={}&\{(34233,34281),(37305,37337),
          (38345,42441),(41401,42409)\},\\
A_8={}&\{(34233,42409),(34281,42441),
          (37305,41401),(37337,38345)\}.
\end{aligned}
\tag{9.1}
\]

It yields physical-edge digest

```text
432839c8e7c28cf6862b7d69a97ad6126968c73c4453bcaf600931fcfe3fd749
```

and exact saved score

\[
(0,0,0,2250,4).
\tag{9.2}
\]

It is not strict-token.  Its lower ledgers change from

\[
\{34217,34249,37273,41385\}
\quad\text{to}\quad
\{33209,34217,34249,37321\},
\]

and its upper ledgers change from

\[
\{34297,37369,42425,46537\}
\quad\text{to}\quad
\{38361,42425,42473,45497\}.
\]

All q1 colours remain present because duplicate slack carries this drift.
All three score-zero \(C_8\)'s change the upper-token multiset; one is
lower-strict and the other two also change the lower multiset.  Hence upper-q1
duplicate slack is necessary within this complete connected core-focused
radius-at-most-four bank.

The endpoint still has 2,250 short residence motifs and four physical
components.  More importantly, a zero **peeled unit-core** count supplies no
base-feasible assignment satisfying every motif row.  Unit propagation is not
a complete feasibility algorithm for this binary system.  Consequently the
only proof-safe statement is

\[
\widehat\nu_{\mathrm{peel}}=0;
\]

neither \(\nu(\mathscr C_R(Q))=0\), \(\Delta_R=0\), nor a resident carrier
follows from the zero detector alone.

For calibration, a direct audit at the optional score-one motif-1839 plateau
enumerates 25,668, 23,715, and 24,025 alternating closed radius-four exchanges
through its three closure edges.  Of these, 24,946, 23,146, and 23,533 are
simple physical \(C_8\)'s.  Neither class contains a strict-token witness.
This confirms that the successful escape leaves the strict-load fibre; it is
not a global C8 no-go.

## 10. Exact higher-order obstruction after unit-core zero

The full fixed-overlay model for candidate 0 has 24,958 literal decision
variables and 37,997 rows:

\[
12,867\text{ degree}+11,440\text{ lower q1}
+11,440\text{ upper q1}+2,250\text{ motifs}.
\]

Its frozen H100 transcript reports `INFEASIBLE` at round zero, before any
dynamic CEGAR row.  More importantly, the infeasibility now has a completely
solver-free real-linear certificate.

### Theorem 10.1 (common one-motif nine-row Farkas packet)

All three score-zero radius-four endpoints contain the same physical
coordinate-11 length-two occurrence with closure

\[
C=\{(62050,64034),(62514,63538),(63538,64034)\}.
\tag{10.1}
\]

Its occurrence indices are respectively 1607, 1852, and 1331 in candidates
0, 1, and 2.  Put

\[
\begin{array}{lll}
x=b_{(63538,64034)},&y=b_{(62050,64034)},
&z=b_{(62514,63538)},\\
a=a_{(63526,64546)},&b=b_{(63526,63750)},
&c=a_{(61486,63526)},\\
d=b_{(59438,63526)},&p=a_{(61554,63538)},
&q=a_{(48178,63538)}.
\end{array}
\tag{10.2}
\]

In every one of the three fixed \(Q/R\) overlays, the complete named rows are

\[
\begin{array}{c|c}
\text{row}&\text{inequality}\\ \hline
L63522&x-a\le0\\
U63782&b\le0\\
V63526&a+c-b-d\le0\\
U63534&d-c\le0\\ \hline
M_C&-x-y-z\le-1\\
L61986&y\le0\\
L61490&z-p\le0\\
U64562&z-q\le0\\
V63538&p+q-x-z\le0.
\end{array}
\tag{10.3}
\]

The first four rows sum to

\[
x\le0.
\tag{10.4}
\]

The last five sum to

\[
-2x\le-1.
\tag{10.5}
\]

Twice (10.4) plus (10.5) is the literal Farkas contradiction

\[
0\le-1.
\tag{10.6}
\]

Hence \(\{C\}\) is a singleton hyperedge of
\(\mathscr C_R(Q_i)\) for each zero-detector endpoint \(Q_i\), and

\[
\Delta_R(Q_i)\ge1\qquad(i=0,1,2).
\tag{10.7}
\]

The proof holds over the reals.  It is a palette/endpoint Hall deficiency,
not an odd-cycle, parity, blossom, or integrality obstruction.  The exact
nine-row subsystem is inclusion-minimal: a Boolean witness is frozen after
deleting any one of its nine rows.  Since the base system is feasible at the
zero switch, the singleton motif set is automatically a minimal motif
circuit. \(\square\)

The mechanism is transparent.  The left packet forces \(x=0\).  On the right,
\(y=0\), while deleting \(z\) requires both providers \(p,q\), and the socket
at 63538 has capacity \(p+q\le x+z\).  Thus the motif can only be hit through
\(x\), which the remote packet has already forbidden.

### Theorem 10.2 (common serial two-motif packet)

There is a second, motif-disjoint obstruction shared by all three endpoints.
Let

\[
\begin{aligned}
A={}&\{(7526,7782),(7526,15714),(15466,15714)\},\\
B={}&\{(47458,63810),(48210,63570),(63570,63810)\}.
\end{aligned}
\tag{10.8}
\]

These are inherited coordinate-8 and coordinate-14 length-two occurrences.
Write

\[
H_1=b_{(15466,15714)}+b_{(7526,15714)},qquad
H_2=b_{(47458,63810)}+b_{(63570,63810)},
\]

and

\[
s=a_{(48450,63810)},qquad
h=b_{(15686,15698)},qquad
e=a_{(57678,61766)}.
\]

Exact sums of nine palette/degree rows on the first side and six on the
second give

\[
H_1+s\le h,qquad H_2+e\le s.
\tag{10.9}
\]

For avoidance of any hidden-provider ambiguity, the first sum uses exactly

\[
U15467,V15459,L15458,U15718,L7494,V15686,
U48454,V48450,U48482,
\]

where \(V\) denotes the displayed red/blue endpoint-balance orientation.
The second uses exactly

\[
U58702,V57678,U61774,U62278,V61766,V63810.
\]

Literal reconstruction in every endpoint verifies that all unlisted
coefficients cancel and that these sums are precisely (10.9).

The two motif rows require \(H_1,H_2\ge1\); the bounds give
\(e\ge0\) and \(h\le1\).  Adding all seventeen model rows and those two
bounds yields

\[
H_1+H_2+e\le h\le1,qquad H_1+H_2\ge2,
\]

again a real-linear contradiction.  This packet is disjoint in motif rows
from (10.1).  Therefore

\[
\boxed{\Delta_R(Q_i)\ge2\quad(i=0,1,2).}
\tag{10.10}
\]

Candidate 0 additionally has the newly created motif-82 nine-row packet, so
its three displayed packets give \(\Delta_R(Q_0)\ge3\).  No equality is
claimed.

### Theorem 10.3 (fourteen singleton packets plus one serial surcharge)

For candidates 1 and 2, there are fourteen distinct inherited motif
occurrences \(M_1,\ldots,M_{14}\) such that

\[
\mathcal B_R(Q_i)\cup\{M_j\text{ is hit}\}
\quad\text{is infeasible}
\qquad(1\le j\le14).
\tag{10.10a}
\]

The fourteen physical \((\text{coordinate},\text{length},\text{closure})\)
keys agree between the two candidates, although their occurrence indices can
differ.  Candidate 0 retains thirteen of these keys.  The missing key is the
coordinate-3 length-two closure

\[
\{(41395,41401),(41401,42409),(42409,46497)\},
\]

and candidate 0 replaces it, for purposes of the packing bound, by its
independently locked motif 82.  Thus every candidate has fourteen distinct
singleton circuits.

The replay is purely solver-free.  It rebuilds the exact degree and both-q1
hard rows.  For each occurrence it chooses a live closure variable and
propagates each of its two Boolean values from scratch.  Both branches end in
a signed-cardinality contradiction, and the frozen branch proofs contain no
motif row other than the named occurrence.  Since the hard base has the zero
assignment as a witness, each named occurrence is a genuine singleton
hyperedge of \(\mathscr C_R(Q_i)\), not merely a failed branch in a larger
packet.

The motifs \(A,B\) in Theorem 10.2 are disjoint from all fourteen singleton
rows.  Their serial packet forces at least one additional unhit occurrence.
Therefore

\[
\boxed{\Delta_R(Q_0),\Delta_R(Q_1),\Delta_R(Q_2)\ge15.}
\tag{10.10b}
\]

This is a lower bound on inherited-motif deficiency for the fixed resident
endpoint.  It is not equality and does not persist automatically after moving
the resident factor. \(\square\)

### Corollary 10.4 (packet-halo necessity)

Let

\[
\Lambda_C^- =\{63522,61986,61490\},\qquad
\Lambda_C^+ =\{63782,63534,64562\},
\]

and let \(V_C=\{63526,63538\}\).  If a q1-preserving trade leaves the motif
\(C\), the complete provider lists and loads of all colours in
\(\Lambda_C^-\cup\Lambda_C^+\), and the two symmetric-difference stars at
\(V_C\) unchanged, then all nine rows (10.3) survive verbatim and the new
fixed overlay is infeasible.

Consequently every viable q1 trade must do at least one of the following:

1. remove an edge of the closure \(C\) so that the occurrence disappears;
2. change a provider list or load in one of the six named q1 rows;
3. change the red/blue endpoint incidence at 63526 or 63538; or
4. move the resident endpoint so that one of the four red providers
   \(a,c,p,q\) or the two degree stars changes shore.

This is the exact support target for the next portal search.  The three
radius-four moves that cleared unit cores do none of these things to the
inherited packet, which explains their common failure.

### The failed-literal working potential

After the complete full-row unit fixpoint, let \(L_2(Q)\) be the variables occurring
in a still-unhit two-choice motif row.  Define

\[
\Phi_{\rm FL}(Q)=
\#\{v\in L_2(Q):\text{both assumptions }v=0,\ v=1
                 \text{ unit-refute the full row system}\}.
\tag{10.11}
\]

Complete solver-free banks give

\[
\Phi_{\rm FL}(Q_0)=95,qquad
\Phi_{\rm FL}(Q_1)=\Phi_{\rm FL}(Q_2)=93.
\tag{10.12}
\]

Unlike the zero peeled-core statistic, every counted failed literal is an
actual two-branch infeasibility certificate.  The count is still not
\(\Delta_R\), a core packing, or an unoriented Lyapunov function: different
literals can share the same packet, and inverse moves can increase it.  It is
the correct proof-directed **working score** after enforcing Corollary 10.4.
The next safe lexicographic screen is therefore

\[
(\mathbf1_{\text{common packet survives}},
  \Phi_{\rm FL},
  \text{total failed-branch proof size},
  \text{motifs},
  \text{components}),
\tag{10.13}
\]

with no return to unit-core count as a stopping condition.

### Theorem 10.5 (an explicit q1-cover-preserving failed-literal descent)

For candidate 1, the complete connected alternating-circuit census through
the closures of \(A\) and \(B\) has the following exact sizes:

\[
\begin{array}{c|cc|cc}
&A,C_4&A,C_6&B,C_4&B,C_6\\ \hline
\text{raw circuits}&33&1134&33&1131\\
\text{both-q1-cover preserving}&0&4&1&7.
\end{array}
\tag{10.14}
\]

After deduplication these are twelve physical trades.  The best single trade
in the complete bank is

\[
\begin{aligned}
D_B={}&\{(47395,55587),(47458,63810),(55619,63747)\},\\
A_B={}&\{(47395,47458),(55587,55619),(63747,63810)\}.
\end{aligned}
\tag{10.15}
\]

It destroys \(B\), preserves both q1 covers, and changes
\(\Phi_{\rm FL}:93\to87\).  Next apply the disjoint support trade

\[
\begin{aligned}
D_C={}&\{(63526,63750),(63622,63650),(63778,63874)\},\\
A_C={}&\{(63526,63622),(63650,63874),(63750,63778)\}.
\end{aligned}
\tag{10.16}
\]

This changes the exact \(U63782\) support row in (10.3), keeps the occurrence
\(C\) itself, preserves both q1 covers, and changes
\(\Phi_{\rm FL}:87\to84\).  Finally apply

\[
\begin{aligned}
D_A={}&\{(7478,23846),(7526,15714),(15654,32034)\},\\
A_A={}&\{(7478,7526),(15654,15714),(23846,32034)\}.
\end{aligned}
\tag{10.17}
\]

It destroys \(A\), preserves both q1 covers, and changes
\(\Phi_{\rm FL}:84\to82\).  The three alternating \(C_6\)'s are pairwise
vertex-disjoint, so every prefix and their union is automatically
degree-preserving.  Writing \(C_B,C_C,C_A\) for the three exchanges in that
order, literal replay gives

\[
\begin{array}{c|cccc}
&Q_1&Q_1\triangle C_B&\triangle C_C&\triangle C_A\\ \hline
\Phi_{\rm FL}&93&87&84&82\\
\#\text{physical components}&4&4&3&3\\
\#\text{short occurrences}&2250&2251&2252&2253\\
(A,B,C)&(1,1,1)&(1,0,1)&(1,0,1)&(0,0,1).
\end{array}
\tag{10.18}
\]

Every displayed state has zero lower- and upper-q1 holes.  This proves that
the new potential admits a genuine local descent and that hitting the common
packet support can be combined with killing \(A,B\).  It does **not** prove
descent of \(\Delta_R\), because no matching feasible hole assignment has
been produced, and it does not prove the final overlay feasible: 82 complete
failed-literal certificates remain.  In particular the remaining obstruction
is distributed beyond the three named packets. \(\square\)

### Theorem 10.6 (direct affine-packet deletion and the prefix through 81)

There is a sharper two-step path from candidate 1.  First use the physical
alternating \(C_6\)

\[
\begin{aligned}
D_1={}&\{(53986,62114),(55843,55970),(62050,64034)\},\\
A_1={}&\{(53986,55970),(55843,64034),(62050,62114)\}.
\end{aligned}
\tag{10.19}
\]

It deletes the common closure edge \((62050,64034)\), hence destroys the
affine occurrence (10.1) rather than merely changing one support row.  The
result is a simple two-component factor with both q1 covers complete,
2,248 short occurrences, and

\[
\Phi_{\rm FL}:93\longrightarrow86.
\]

From that endpoint use the alternating \(C_8\)

\[
\begin{aligned}
D_2={}&\{(50804,52788),(50808,52848),
          (52824,56912),(54868,54896)\},\\
A_2={}&\{(50804,54896),(50808,52824),
          (52788,52848),(54868,56912)\}.
\end{aligned}
\tag{10.20}
\]

It targets the smallest surviving failed-literal packet.  The result is a
simple three-component factor with both q1 covers complete, 2,244 short
occurrences, and

\[
\boxed{\Phi_{\rm FL}:86\longrightarrow81.}
\tag{10.21}
\]

The two materialized endpoints and their complete 979- and 975-variable
probe banks are frozen.  The final bank contains 81 double failures, so this
is a strict descent of the detector, not a feasible overlay.  No global
completeness claim is made for the targeted radius-\(2,3,4\) trade generator,
and neither \(\Delta_R\) nor the fourteen-packet packing has been recomputed
for the two new factors. \(\square\)

### Theorem 10.7 (the frozen C8 tail through score 73)

Starting at the score-81 endpoint of Theorem 10.6, apply the following three
physical alternating \(C_8\)'s in order:

\[
\begin{aligned}
D_{81}={}&\{(9327,9339),(9575,9831),
             (11367,11847),(11371,11374)\},\\
A_{81}={}&\{(9327,9575),(9339,11371),
             (9831,11847),(11367,11374)\};
\end{aligned}
\tag{10.22}
\]

\[
\begin{aligned}
D_{78}={}&\{(25011,26019),(25059,26081),
             (26033,30113),(50657,58785)\},\\
A_{78}={}&\{(25011,26033),(25059,26019),
             (26081,50657),(30113,58785)\};
\end{aligned}
\tag{10.23}
\]

\[
\begin{aligned}
D_{76}={}&\{(25269,25493),(41653,41877),
             (41905,58033),(58005,58257)\},\\
A_{76}={}&\{(25269,58005),(25493,41877),
             (41653,41905),(58033,58257)\}.
\end{aligned}
\tag{10.24}
\]

Each symmetric difference is one simple alternating eight-cycle.  Independent
replay obtains exact equality with the three frozen endpoint edge sets and

\[
\begin{array}{c|rrrr}
&Q_{81}&Q_{78}&Q_{76}&Q_{73}\\ \hline
\Phi_{\rm FL}&81&78&76&73\\
\text{complete probe bank}&975&975&974&970\\
\#\text{components}&3&2&3&4\\
\#\text{short occurrences}&2244&2243&2241&2240\\
\text{lower q1 holes}&0&0&0&0\\
\text{upper q1 holes}&0&0&0&0.
\end{array}
\tag{10.25}
\]

Thus the full frozen chain is

\[
93\to86\to81\to78\to76\to73.
\]

Every arrow is an exact finite certificate.  The statement is deliberately
not a convergence claim: \(Q_{73}\) remains solver-free infeasible, its
\(\Delta_R\) has not been computed, and no complete outgoing local atlas at
\(Q_{73}\) is asserted here. \(\square\)

## 11. Failed-literal descent and finite local-minimum certificates

**Successor audit notice (2026-07-29).**  The integer-decrease statement in
Theorem 11.1 remains valid, but Proposition 11.2's old five-item halo is not a
theorem-safe eligibility transport certificate: preserving only rows used by
the old propagation does not prove that a token stays unassigned in the new
complete fixpoint.  The corrected theorem requires a derivation of every
fixed literal plus a residual nonforcing check over every target row, and a
coefficient/RHS-preserving full-support isomorphism for every replayed proof
row together with exact replay of every ordered branch-unit-propagation
forcing step.  The successor report
`MATH_THEOREM_K_WEIGHTED_FAILED_LITERAL_HALO_ALTERNATIVE_AT_FL30_20260729.md`
also freezes the exact chain

\[
73\to69\to56\to48\to39\to34\to30
\]

and the outgoing \(30\to27\) packet, proves the killed-minus-born identity,
and refutes monotonicity of the old proof-incidence weight.  Use its Theorem
7.1, not the unqualified halo-localization paragraph below, for any future
local-minimum certificate.  No convergence claim is added here.

Fix a finite state class \(\mathfrak F\) of spanning degree-two factors on the
same physical vertex set, all complete in both q1 supports, and fix a finite
legal alternating-trade library \(\mathcal L\).  Restrict to states at which
the exact full-row unit propagation (degree, both q1 palettes, and every
current motif row) reaches a noncontradictory fixpoint, so that the complete
two-choice score \(\Phi_{\rm FL}\) is defined by (10.11).

### Theorem 11.1 (integer descent theorem)

Orient a legal edge \(Q\to Q'\) precisely when

\[
\Phi_{\rm FL}(Q')<\Phi_{\rm FL}(Q).
\tag{11.1}
\]

Every directed path is simple and has length at most
\(\Phi_{\rm FL}(Q_0)\).  Every maximal directed path ends at a state with no
strictly lower \(\mathcal L\)-neighbour.

#### Proof

The score is a nonnegative integer and decreases by at least one at every
arrow.  Hence a path starting at \(Q_0\) has at most
\(\Phi_{\rm FL}(Q_0)\) arrows and cannot repeat a state.  If the path is
maximal, its terminal state has no lower legal neighbour. \(\square\)

This proves finite **descent**, not convergence to an overlay solution.  A
terminal score can be positive; even score zero only clears this detector and
does not imply \(\Delta_R=0\), absence of new seam motifs, or residence.

### Superseded five-item halo heuristic

The earlier version of this section claimed that preserving the decision
edges, used q1 provider lists, used endpoint stars, used motif collars, and
the incidences appearing in one old eligibility provenance was enough to
transport a failed literal.  That locality claim is withdrawn.  It replays
the two branch contradictions only after eligibility is known, but does not
prove the global negative fact that the token remains unassigned in the new
complete fixpoint.

The corrected certificate is Theorem 7.1 of the successor report cited
above.  In addition to coefficient/RHS-preserving full-support isomorphisms
for every replayed proof row, it requires a derivation of every target
fixpoint literal, a residual nonforcing check of every target row, and exact
replay of both ordered branch-UP contradiction transcripts.  A derived
Farkas infeasibility combination alone is insufficient to prove membership
in the algorithmic bank.  Only that complete certificate, or a fresh
full-bank audit, may be used to declare an omitted packet inert.  The result
remains library-local and says nothing about larger packets or a moving
resident.

### Exact-potential CEGAR controller

The preceding results support the following proof-safe controller.

1. At the current factor, use the **exact** base system and all current motif
   rows.  A base-feasible assignment with \(h\) violated motif rows proves
   \(\Delta_R\le h\); one satisfying all rows proves \(\Delta_R=0\).  An
   infeasible subsystem is an infeasible packet and becomes a circuit only
   after inclusion-minimization.
2. Maintain the circuit hypergraph, not a raw motif count.  Disjoint circuits
   give lower bounds and feasible hole sets give upper bounds on
   \(\Delta_R\).
3. Claim strict descent only through Corollary 3.3 or an equivalent matched
   lower/upper certificate.
4. If \(d_\Gamma(Q,Z)<\infty\), prescribe a shortest-path edge and reach
   \(Z\) in exactly \(d_\Gamma(Q,Z)\) steps.  If the distance is infinite, a
   reachable bottom strongly connected class disjoint from \(Z\) exists; stop
   there with a graph lock.  It is a Hall packet lock only after Theorem 5.1's
   transport hypotheses are proved.
5. After every materialized switch, recompute the motif atlas.  Hitting all
   inherited rows is not enough because new seam motifs may appear.

This is an exact termination dichotomy, not a claim that the present local
library always terminates.  The strict \(F_1\leftrightarrow F_2\) packet proves
that a core-directed strict-token \(C_4/C_6\) controller can fail.  The long
protected-token chain and its final C8 show how duplicate palette slack can
leave that architecture.  Theorems 10.1--10.3 prove that all three
zero-detector branches remain Hall-infeasible, while Theorems 10.5--10.7
prove strict descents of the complete failed-literal working score after
deliberately hitting the common packet halo.

## 12. Frozen evidence and hashes

Independent corrected 27-core replay:

```text
scratch/audit_k16_27core_beam_hall_rank_20260729.py
SHA-256 2ccd1a103b872307021783bf19c1c246fa65a5a0f260d801c99bb99cd33c2bed

scratch/k16_27core_beam_hall_rank_20260729.audit.json
SHA-256 c32261739d55c7be4022ad6cc10733d818d2200ee89082724ae5d6244dd1f9b4
```

Linked protected-token chain audit through the score-one state:

```text
scratch/audit_k16_portal24_chain_metadata_20260729.py
SHA-256 fa54c3b6ccfd82633d1bdabbb0c12a23c3134ae11e9b5bde8df1dc7516764e72

scratch/k16_portal24_chain_metadata_20260729.audit.json
SHA-256 7870c58f79c8618e323a25ecb2e282f70e897ae4b599ffc96f68c5a9799cd2e2
```

Radius-four zero-unit-core report and materialized endpoint:

```text
scratch/k16_resume1_core1_hitting_portal_r234_24_20260729.json
SHA-256 67050aa1b6da6d9de4cf5456b533e6d0848ac86767549e12b7c18211b5b0331f

scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_20260729.json
SHA-256 6f614ae41d1264121acc7cfb1b3303f3bb93532d57aeac1d0153e3f344a73f53
```

Strict C6 packet-lock audit:

```text
scratch/k16_strict_token_c6_chain_trap_20260729.audit.json
SHA-256 b947955bda222b856c006779feb38c3db735bd7143a104eb20488a85b8494007
```

Strict C8 audit at the live motif-1839 plateau:

```text
scratch/audit_k16_live_core_strict_token_c8_direct_20260729.py
SHA-256 a921191b2412599efcdea8b19ed6a65ae8c5773e84a1dcc74b32b9b2bb0a1258

scratch/k16_live_core_strict_token_c8_direct_20260729.audit.json
SHA-256 92de53ce10aa60b9507daf2a31b0372aeb9ffbd8d2338c69eb3c1e11f2c4e006
```

The three materialized zero-unit-core endpoints:

```text
scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_20260729.json
SHA-256 6f614ae41d1264121acc7cfb1b3303f3bb93532d57aeac1d0153e3f344a73f53

scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_candidate1_20260729.json
SHA-256 7435b0f27e035e2eec87ec5afe47130fd2d08da3bcee70669a4189f4bb7d6dff

scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_candidate2_20260729.json
SHA-256 ce17d15a6474cf20108412a6b255a91b8bab7566a27bbedf75dad8eb1002d738
```

Common singleton affine/Farkas packet:

```text
scratch/audit_k16_three_zero_unit_candidates_common_affine_core_20260729.py
SHA-256 97082108f7ee0f47fa0dc7d01ca9f92aeaddbedeb2af4c44978cf75168fbfb59

scratch/k16_three_zero_unit_candidates_common_affine_core_20260729.audit.json
SHA-256 ed29297b30542d4c6311748bc9692e8ff1eebb8a91034244bdaafe4882317a8c
```

Common serial two-motif packet:

```text
scratch/audit_k16_three_zero_endpoints_common_two_motif_packet_20260729.py
SHA-256 8596ab770ac8283fa93724d817e5534897f518143ecbb53edb0dbc6c0a244b9d

scratch/k16_three_zero_endpoints_common_two_motif_packet_20260729.audit.json
SHA-256 7b064e048c7a2594ce661e15dc73fc1a1216a9aed909bac9466d8e635cac893b
```

Fourteen singleton packets plus the disjoint serial surcharge:

```text
scratch/audit_k16_three_zero_endpoints_singleton_packet_packing_20260729.py
SHA-256 d6d41f761c413bea4fb5a5a76e203fe9e79bb5dc22e8216f3bbe9c2fc1fe4345

scratch/k16_three_zero_endpoints_singleton_packet_packing_20260729.audit.json
SHA-256 a13baa6ca351861959264381eb6a286fb58d9bf79cadeabd00b738ec144db70c

MATH_AUDIT_K_K16_SINGLETON_PACKET_PACKING_AND_SMALL_TRADE_SCOPE_20260729.md
SHA-256 8256e5aa7b908071dffe5d906a0b3b27a90bdd105e8488f797bd418110bd98e3
```

Complete failed-literal banks for candidates 0, 1, and 2:

```text
scratch/k16_zero_unit_failed_literal_core_fullbank_20260729.audit.json
SHA-256 3b77d3b217922038ee5ce835d35c2d52ec5536007d91bab556d4115c83537e3b

scratch/k16_zero_unit_failed_literal_core_candidate1_fullbank_20260729.audit.json
SHA-256 c77cdb309c47ba3ee14120004c4a6e9ec4b684b4e6bb87dea0a6dfddc9d0821f

scratch/k16_zero_unit_failed_literal_core_candidate2_fullbank_20260729.audit.json
SHA-256 625b56c114c2c98d30bd7ea4dc882bc53abba62e609065e87793c6cd070c669f
```

Complete bounded \(A/B\) trade census and the exact three-step descent:

```text
scratch/audit_k16_candidate1_ab_trade_failed_literal_potential_20260729.py
SHA-256 98ae7ff92419a019fa79e2652720b856764a25e5f0469656d27768ae4c7f6fc9

scratch/k16_candidate1_ab_trade_failed_literal_potential_20260729.audit.json
SHA-256 439d387c189b15bb0a3e99090bb9a4de4e74b6ca3e2d53b487b8185a54c32d3c

scratch/audit_k16_candidate1_abc_failed_literal_descent_20260729.py
SHA-256 7ddb8f9de2f6fd1da0382adebd6c0a7a6c0d8ead8f8ecc7312651a10a527fbe3

scratch/k16_candidate1_abc_failed_literal_descent_20260729.audit.json
SHA-256 3293274746b449986d16c7034841bac390796db905c2dfb99d3bb48e55128d03
```

Direct common-packet deletion and the frozen chain through score 73:

```text
scratch/k16_candidate1_common_affine_targeted_packets_20260729.json
SHA-256 420fc430564d92a0f8f46dc83d01532fc6a4c88b33fdd97f8a44ad1c872580a1

scratch/k16_q1_endpoint_resume1_failedlit86_20260729.json
SHA-256 3a0603fcd435c747dfe1fbc5c4d0c90b1c43f791135302987b726d0d65441f05

scratch/k16_failedlit86_fullbank_20260729.audit.json
SHA-256 bcccce1cced15edf0c8c8832ce615d3f0a6cc61a369c0333d3cd9ed5b4e3ff85

scratch/k16_q1_endpoint_resume1_failedlit81_20260729.json
SHA-256 2ed874f24813039258f0562c5e2c9b307e8a3ce7a5552c326a0cc68f24f9b2db

scratch/k16_failedlit81_fullbank_20260729.audit.json
SHA-256 31b3bf28428ba2f45ad1648fb4755e7077c555ecab71ab15ca3b2021ca5e8f1d

scratch/audit_k16_candidate1_affine_to_failedlit81_chain_20260729.py
SHA-256 db71b3c95373b7b79fadc86adf4e350b769c85ee8c558f9e1524910bec93f99d

scratch/k16_candidate1_affine_to_failedlit81_chain_20260729.audit.json
SHA-256 6a1442ccb502d1d57aacce4031f292a7e99f16ef3f96208eb5fa3245e54d26c5

scratch/k16_q1_endpoint_resume1_failedlit78_20260729.json
SHA-256 6f08c934ae7dc7f6d92c2dcd32954805b62c18eb7f9083e6124b3799b51beba9

scratch/k16_failedlit78_fullbank_20260729.audit.json
SHA-256 5233a0ab41962a31588cfc22c7a35a6925e839b650a93d703afbe4daa2ec5ada

scratch/k16_q1_endpoint_resume1_failedlit76_20260729.json
SHA-256 181dd18b0f45982b9929dc7f78b8e87fbd5eb3e6b16f1e045a06b5c9a88aa1a9

scratch/k16_failedlit76_fullbank_20260729.audit.json
SHA-256 f2dd6e4637cac725a66e8d6cbcf46fdc5404e1414bb1fc0999d2c9d84db68280

scratch/k16_q1_endpoint_resume1_failedlit73_20260729.json
SHA-256 fa7d6edce1a71012d317220a97e0cf8900dd14d385087ea3a6d920a64d16e513

scratch/k16_failedlit73_fullbank_20260729.audit.json
SHA-256 d03193607795d42865e16277888c4ea0c3c025499fcd78c966077a131cde7c47

scratch/audit_k16_failedlit81_to73_chain_20260729.py
SHA-256 aa5f2ffa25c663a22004e09a4a2e86c2efc10ff443f1ab0b25645beb22d012e5

scratch/k16_failedlit81_to73_chain_20260729.audit.json
SHA-256 d0e68f183828697216ba4627afdc42ca579f0f630c27a59ef695175d78182241
```

The old corrected 27-core replay records the then-current analyser hash in
its payload, but the analyser file has since changed.  Its frozen JSON remains
the cited evidence; rerunning the top-level script today is not a
dependency-hash-closed reproduction unless the recorded dependency is first
restored.

The sharp boundary is therefore:

> The exact fixed-overlay potential is the transversal number of the full
> interaction-circuit hypergraph.  A strict-load-neutral, core-directed
> \(C_4/C_6\) library has a proved two-state packet lock.  Protected-token
> \(C_4/C_6\) flow reduces the displayed packing certificate to one, and a
> non-strict \(C_8\) clears the unit-propagation detector.  All three such
> endpoints nevertheless have certified fixed-overlay deficiency at least
> fifteen.  A
> q1-cover-preserving \(C_6\)-then-four-\(C_8\) path hits successive proof
> halos and gives the frozen exact chain
> \(93\to86\to81\to78\to76\to73\); an independent
> three-\(C_6\) path killing \(A,B\) gives \(93\to82\).  No exact all-motif
> circulation or new resident endpoint has yet been proved, and no convergence
> claim is made.
