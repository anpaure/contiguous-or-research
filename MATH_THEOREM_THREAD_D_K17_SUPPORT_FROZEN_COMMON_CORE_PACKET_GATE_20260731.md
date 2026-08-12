# Thread D: support-frozen common-core gate for long trace packets

Date: 2026-07-31  
Status: exact packet normal form, exact local turn-support ledger, and exact
pre-solve common-core Hall/linkage certificate; the companion K17 audit now
supplies improving packets; no all-dimension existence theorem

## 1. Scope

Let

\[
 {\cal A}=\binom{[2m-1]}{m-1},\qquad
 {\cal B}=\binom{[2m-1]}m
\]

be the two shores of the middle-levels graph, and let \(C\) be a literal
spanning two-factor. Hamiltonicity is not assumed. For \(A\in{\cal A}\)
and \(B\in{\cal B}\), write

\[
 u_C(A)=B^-(A)\cup B^+(A),\qquad
 \ell_C(B)=A^-(B)\cap A^+(B).
\tag{1.1}
\]

The results below apply to one-retained-edge long or compound packets: at
every affected physical vertex exactly one factor edge is retained and one
is replaced. This includes a disjoint union of ordinary alternating
circuits of arbitrary length. A more general packet in which both factor
edges at one vertex change still has the common-core Hall certificate in
Section 4, but not the three-edge-column normal form in Section 2.

The note certifies only the fixed-middle-levels-support decoration gate. A
partial old-rail atom ledger is not a full ordered four-transversal, and no
such promotion is made here.

## 2. The exact joint-service column normal form

Let \(Z_A\subseteq{\cal A}\), \(Z_B\subseteq{\cal B}\), with

\[
 |Z_A|=|Z_B|=t.
\]

On the affected vertices, let \(p_0\) be the old internal perfect matching
of \(C\), and let \(e(v)\) be the other, retained, factor neighbour of \(v\).
Choose a new perfect matching \(p_1\) from \(Z_A\) to \(Z_B\), using only
middle-levels edges outside \(C\). Then

\[
 C'=C-p_0+p_1                                             \tag{2.1}
\]

is again a spanning two-factor. The union \(p_0\cup p_1\) is a disjoint
union of alternating circuits. Whether \(C'\) is Hamiltonian is a separate
literal component test.

Every allowed new edge \(a=AB\), \(A\in Z_A,B\in Z_B\), is a
**joint-service column** with labels

\[
 U(a)=e(A)\cup B,\qquad L(a)=e(B)\cap A.               \tag{2.2}
\]

They are exactly the new turn colours at \(A\) and \(B\). Thus one selected
column simultaneously chooses one physical incidence edge, one upper-turn
occurrence and one lower-turn occurrence. Treating these three choices as
independent is an invalid relaxation.

### Lemma 2.1 (exact palette delta)

For every upper colour \(U\) and lower colour \(L\),

\[
 n_U(C')=n_U(C)-|\{A\in Z_A:u_C(A)=U\}|
                 +|\{a\in p_1:U(a)=U\}|,             \tag{2.3}
\]

\[
 n_L(C')=n_L(C)-|\{B\in Z_B:\ell_C(B)=L\}|
                 +|\{a\in p_1:L(a)=L\}|.             \tag{2.4}
\]

#### Proof

Every turn outside \(Z_A\sqcup Z_B\) is unchanged. At an affected vertex,
substituting \(p_1(v)\) for \(p_0(v)\) in (1.1) gives (2.2), so subtracting
the old affected occurrences and adding the new ones proves the formulas.
\(\square\)

Assume the upper word of \(C\) is surjective. Define the endangered upper
and lower palettes

\[
 {\mathfrak U}_Z=
 \{U:\{A:u_C(A)=U\}\subseteq Z_A\},                  \tag{2.5}
\]

\[
 {\mathfrak L}_Z=
 \{L:n_L(C)>0,\ \{B:\ell_C(B)=L\}\subseteq Z_B\}.    \tag{2.6}
\]

If \(D\) is a set of currently missing lower colours which the packet is
required to install, Lemma 2.1 gives the exact local rows

\[
 {\mathfrak U}_Z\subseteq\{U(a):a\in p_1\},           \tag{2.7}
\]

\[
 {\mathfrak L}_Z\sqcup D\subseteq\{L(a):a\in p_1\}.  \tag{2.8}
\]

Equation (2.7) is necessary and sufficient for preserving upper-turn
surjectivity. Equation (2.8) is necessary and sufficient for retaining all
old lower-turn support and installing every colour in \(D\). In particular,

\[
 t\ge |{\mathfrak U}_Z|,\qquad
 t\ge |{\mathfrak L}_Z|+|D|.                          \tag{2.9}
\]

Because the middle-levels graph has no four-cycle, every nontrivial
alternating component of \(p_0\cup p_1\) has at least three columns. Hence
a nonempty packet also satisfies

\[
 t\ge3.                                               \tag{2.10}
\]

These are genuine support lower bounds. They do not assert that the
remaining labelled perfect-matching problem is feasible.

Two cheap marginal Hall prefilters are also valid. For an endangered upper
colour \(U\), let \(P_U(U)\) be the affected \(A\)-positions which occur in
some allowed column of upper label \(U\). For an obligation
\(L\in{\mathfrak L}_Z\sqcup D\), define \(P_L(L)\subseteq Z_B\) analogously.
Any packet satisfying (2.7)--(2.8) must obey

\[
 \left|\bigcup_{U\in S}P_U(U)\right|\ge |S|,
 \qquad S\subseteq{\mathfrak U}_Z,                    \tag{2.11}
\]

\[
 \left|\bigcup_{L\in T}P_L(L)\right|\ge |T|,
 \qquad T\subseteq{\mathfrak L}_Z\sqcup D.            \tag{2.12}
\]

They are only marginal necessary conditions: the same column must satisfy
the \(A\)-position, \(B\)-position, upper-label and lower-label ledgers.

## 3. One fixed augmented core for the whole support fibre

Let \({\cal G}_C\) be the augmented trace graph. Its edges consist of the
two physical incidence edges at every position, the edge from every
\(A\)-position to its upper turn colour, and the edge from every lower turn
colour to each corresponding \(B\)-position.

For every old internal pair \(AB\in p_0\), remove the three-edge bundle

\[
 \{AB,\ A u_C(A),\ \ell_C(B)B\}.                      \tag{3.1}
\]

Call the resulting graph \(H_Z\). It depends only on the support and the
old internal matching, not on the reconnection. For an allowed new column
\(a=AB\), put

\[
 \beta(a)=\{AB,\ A U(a),\ L(a)B\}.                   \tag{3.2}
\]

### Lemma 3.1 (support-frozen core identity)

For every new internal perfect matching \(p_1\),

\[
 {\cal G}_{C'}=H_Z\cup\bigcup_{a\in p_1}\beta(a).     \tag{3.3}
\]

#### Proof

At an affected \(A\), the external incidence edge is retained, while the
old internal incidence edge and the old upper-turn edge are precisely the
first two affected edges in (3.1). The new internal incidence and upper
turn are the first two corresponding edges in (3.2). The same statement
at an affected \(B\) gives the lower-turn edge. Nothing outside the support
changes. \(\square\)

Thus a support-frozen packet is exactly a perfect matching of bundled
three-edge columns over one fixed augmented core. This is the smallest
literal normal form needed by the turn-support and common-core ledgers:
\((Z,p_0,p_1)\) reconstructs the physical factor, both turn words and the
entire augmented graph.

If the old augmented deficiency is \(d\), then a maximum old matching loses
at most one edge for each member of the \(3t\)-edge deletion bank (3.1).
Consequently

\[
 r_Z\le d+3t.                                          \tag{3.4}
\]

This recovers the bounded-width estimate of items 2168--2169 in the
support-frozen coordinates. It is only a width bound: the restoring
augmenting paths may traverse the whole retained core.

The packet adds at most \(3t\) augmented edges. Adding one edge raises
matching rank by at most one, while deletions cannot help, so

\[
 \nu({\cal G}_{C'})-\nu({\cal G}_C)\le3t.             \tag{3.5}
\]

Therefore any target deficiency \(q<d\) also requires

\[
 t\ge\left\lceil\frac{d-q}{3}\right\rceil.            \tag{3.6}
\]

Together, (2.9), (2.10), and (3.6) are the immediate cardinality lower
bounds used by this normal form.

## 4. Exact rank-preserving and rank-improving Hall rows

Write the two augmented shore sizes as \(N\). Let \(M_Z\) be a maximum
matching of \(H_Z\), of size \(N-r_Z\). Orient nonmatching edges
left-to-right and matching edges right-to-left. For a selected \(p_1\), let
\(\lambda_Z(p_1)\) be the maximum number of pairwise vertex-disjoint
directed paths from the left vertices exposed by \(M_Z\) to the exposed
right vertices in

\[
 H_Z\cup\bigcup_{a\in p_1}\beta(a).                  \tag{4.1}
\]

### Theorem 4.1 (exact packet rank certificate)

The augmented deficiency after the packet is

\[
 \boxed{\quad
 \operatorname{def}({\cal G}_{C'})=r_Z-\lambda_Z(p_1).
 \quad}                                               \tag{4.2}
\]

Consequently, for any target deficiency \(q\ge0\), the following are
equivalent:

1. \(\operatorname{def}({\cal G}_{C'})\le q\);
2. \(\lambda_Z(p_1)\ge r_Z-q\);
3. for every set \(X\) on the left augmented shore,
   \[
   \left|N_{A(p_1)}(X)\setminus N_{H_Z}(X)\right|
   \ge |X|-|N_{H_Z}(X)|-q,                            \tag{4.3}
   \]
   where \(A(p_1)=\bigcup_{a\in p_1}\beta(a)\), and a negative right side
   is read as zero.

#### Proof

The matching-gain/linkage theorem applied to \(M_Z\) and (4.1) gives

\[
 \nu({\cal G}_{C'})=N-r_Z+\lambda_Z(p_1),
\]

which is (4.2) and proves the equivalence of 1 and 2. Also

\[
 |N_{{\cal G}_{C'}}(X)|
 =|N_{H_Z}(X)|+
   |N_{A(p_1)}(X)\setminus N_{H_Z}(X)|.
\]

Substitution in the deficiency form of Hall's theorem proves the
equivalence with (4.3). \(\square\)

This simultaneously gives four useful exact settings.

* \(q=0\): complete common-core repair and a decoration.
* If the baseline augmented deficiency is \(d\), \(q=d\): no rank
  regression despite the packet deletions.
* \(q=d-g\): at least \(g\) units of genuine matching-rank improvement.
* If upper turns remain surjective and \(h'\) lower colours remain missing,
  \(q=h'\): the only augmented deficiency is the unavoidable isolated
  lower-colour floor. Indeed those \(h'\) isolated colour vertices imply
  deficiency at least \(h'\), so (4.2) then forces equality. This is the
  sharp **shell-tight** row.

The last row is stronger than merely increasing lower-turn support. It
rules out a packet which fills named colours while creating an unrelated
component-Hall obstruction.

There is a useful intermediate target. When the upper word is surjective,
put

\[
 h(C)=|\{L:n_L(C)=0\}|,\qquad
 \epsilon(C)=\operatorname{def}({\cal G}_C)-h(C)\ge0. \tag{4.4}
\]

If a packet preserves old lower support and leaves \(h'\) missing colours,
then

\[
 q=h'+\epsilon(C)                                    \tag{4.5}
\]

is exactly the **excess-nonincreasing** row
\(\epsilon(C')\le\epsilon(C)\). It is the weakest target which forces every
unit of marginal lower-hole improvement to be accompanied by a unit of
actual matching-rank improvement. The choices \(q=\operatorname{def}
({\cal G}_C)\), (4.5), and \(q=h'\) should therefore be reported
separately as raw rank preservation, excess preservation, and shell
tightness.

If \(C'\) is additionally one lower-rainbow Hamilton trace and both turn
maps are surjective, the case \(q=0\) is exactly the simultaneous occurrence
flow gate: a perfect augmented matching leaves

\[
 Q-P=\operatorname {Cat}_m
\]

residual cross edges, and orienting them from the \(A\)-positions to the
\(B\)-positions gives the full layered flow witness. Conversely that flow
plus its chosen outer-colour occurrence edges reconstructs the perfect augmented
matching. Thus the common-core linkage is a pre-solve way to certify the
same joint alternating SDR, not a weaker marginal surrogate. When lower
colours are still missing, the occurrence flow is correctly marked
NOT_APPLICABLE; the \(q>0\) shell rows are only controlled intermediate
states.

## 5. A complete pre-solve no-go and exact separated rows

Let \(E_Z^{\rm allow}\) be the full allowed new-column catalogue and define

\[
 G_Z^{\max}=H_Z\cup
     \bigcup_{a\in E_Z^{\rm allow}}\beta(a).          \tag{5.1}
\]

### Corollary 5.1 (support-envelope no-go)

If

\[
 \nu(G_Z^{\max})<N-q,                                \tag{5.2}
\]

then no reconnection on the support \(Z\) can have augmented deficiency at
most \(q\). A Hall set \(X\) with

\[
 |X|-|N_{G_Z^{\max}}(X)|>q                           \tag{5.3}
\]

is a solver-independent certificate for the entire support fibre.

The converse is deliberately not asserted: (5.1) simultaneously uses
columns which may be incompatible in one physical perfect matching.

For an exact column master, let \(x_a\) select columns, with the ordinary
perfect-matching equations on \(Z_A,Z_B\). After a candidate violates
(4.3), retain its minimizing Hall set \(X\). For every right augmented
vertex \(v\notin N_{H_Z}(X)\), introduce the exact OR

\[
 y_{X,v}=\bigvee_{\substack{a:\ \beta(a)\text{ has an edge }xv\\
                             x\in X}} x_a.            \tag{5.4}
\]

Then the exact separated common-core row is

\[
 \boxed{\qquad
 \sum_{v\notin N_{H_Z}(X)}y_{X,v}
 \ge |X|-|N_{H_Z}(X)|-q.
 \qquad}                                              \tag{5.5}
\]

Right vertices, not column edges, are counted in (5.5); otherwise several
columns entering the same neighbour would be overcounted. Over all
separated \(X\), (5.5) is necessary and sufficient by Theorem 4.1.

## 6. Boundary-signature implementation

For a fixed support \(Z\), the recommended proof-safe order is:

1. Construct the joint columns \(a=(A,B;U(a),L(a))\).
2. Reject the cardinality and marginal Hall obstructions
   (2.9)--(2.12).
3. Construct \(H_Z\), one maximum matching \(M_Z\), and the union envelope
   (5.1). Reject (5.2) before enumerating physical reconnections.
4. Enumerate or optimize perfect matchings \(p_1\), enforcing (2.7)--(2.8)
   and the desired physical component condition.
5. For each survivor, run the vertex-capacitated augmenting flow of
   Theorem 4.1. If it fails, add (5.5); if it passes, retain the literal
   pairwise vertex-disjoint augmenting paths.

When many supports share a bounded adhesion, precompute the strict-gammoid
signature of \(H_Z\) on the exposed vertices and on all endpoints of column
bundles. Compose a candidate's three-edge bundles with that signature.
This is exactly the finite-boundary state of item 2169; replacing it by
independent reachability pairs is unsound because different augmenting paths
may compete for an internal vertex.

The signature must name the literal maximum matching \(M_Z\). Maximum
matchings of the same core can expose different vertex types even though
they give the same matching rank. Hence an exposed-\(U\), exposed-\(B\), or
other type histogram is not an invariant linkage state. One may either
retain \(M_Z\) with the path certificate or avoid this choice entirely by
exporting the Hall rows (4.3).

An independently replayable positive certificate consists of

* the source factor hash and the literal support \(Z\);
* \(p_0,p_1\) and the resulting physical component ledger;
* the old/new upper and lower multiplicity ledgers;
* \(H_Z\), \(M_Z\), \(q\), and \(r_Z-q\) vertex-disjoint alternating paths.

A fibre no-go consists of the same source/support provenance and the Hall
witness (5.3) in the union envelope. Resource exhaustion is neither kind
of certificate.

## 7. Consequence for the current K17 search

The independent six-bank shell audit gives a literal persistent core

\[
 {\cal C}_*=\bigcap_{i=1}^6
 \{\hbox{rank-seven colours missing in bank }i\},
 \qquad |{\cal C}_*|=1297.                            \tag{7.1}
\]

Across the union of 9,002 missing colours, the bank-frequency histogram is

\[
 1^{3303}2^{1342}3^{774}4^{860}5^{1426}6^{1297}.     \tag{7.2}
\]

The distance-one Johnson graph induced by \({\cal C}_*\) has component
orders

\[
 1285,\ 3,\ 1^9,                                     \tag{7.3}
\]

whereas its distance-at-most-two graph is connected. Each member of
\({\cal C}_*\) has exactly twenty elementary service half-ports in the
source factor and 160 raw one-arc records. Every half-port has at least one
upper-surjection-safe replacement: eight when the removed upper colour has
another occurrence, and the unique same-union replacement when it does not.
The minimum numbers of isolated upper-safe records over shell targets in
the source, hard361, hard323, quick650, soft437 and active2649 banks are
respectively

\[
 27,\ 16,\ 16,\ 16,\ 21,\ 21.                        \tag{7.4}
\]

These are prospective provider-record counts, not yet joint columns and not
switch certificates. After a literal support is frozen, each record must be
embedded into a column (2.2). The raw counts do not impose degree, topology,
collateral lower-turn conservation or the common-core row.

The complete source factor has the exact componentwise augmented rank

\[
 \nu({\cal G}_{\rm source})=39624/43758,\qquad
 d=4134=3826+308.                                    \tag{7.5}
\]

Thus its marginal lower-hole floor is 3,826 and its correlation excess
(4.4) is 308. The excess has a literal Hall witness:

\[
\begin{array}{c|cc|c}
 &\text{rank-eight positions}&\text{supported rank-seven colours}
 &|X|\\ \hline
 X_{\rm corr}&823&1261&2084
\end{array}
\]

\[
\begin{array}{c|cc|c}
 &\text{rank-nine positions}&\text{rank-ten colours}
 &|N(X_{\rm corr})|\\ \hline
 N(X_{\rm corr})&1380&396&1776 .
\end{array}
\]

Hence

\[
 |X_{\rm corr}|-|N(X_{\rm corr})|=308.               \tag{7.6}
\]

This is a reusable Hall row given by its literal vertex sets, not by the
types of vertices exposed by one maximum matching.

If a source packet installs exactly \(s\) previously missing
lower colours without losing an old one, then its excess-nonincreasing row
is

\[
 q=4134-s,                                           \tag{7.7}
\]

whereas its shell-tight row is

\[
 q=3826-s.                                           \tag{7.8}
\]

By (3.6), a shell-tight packet must satisfy

\[
 t\ge
 \max\left\{3,\ s,\ |{\mathfrak L}_Z|+s,\
       \left\lceil\frac{308+s}{3}\right\rceil\right\}.\tag{7.9}
\]

In particular, even a shell-tight packet serving one new colour has
\(t\ge103\), hence physical alternating support at least 206. This does
not rule out a shorter excess-nonincreasing packet: (7.7), not (7.8), is
the correct target for incremental descent.

A candidate service set \(D\subseteq{\cal C}_*\) should therefore be
installed in the column obligations (2.8), not scored after a free switch.
Supports with

\[
 |{\mathfrak L}_Z|+|D|>t
\]

are immediately impossible, even if every target separately has a local
provider. Among the remaining supports, (5.2) is the first correlation
test. A candidate which merely preserves all rank-ten colours and adds
members of \(D\) is not acceptable unless it also passes the chosen
rank-preserving, rank-improving, or shell-tight instance of Theorem 4.1.

This supplies an exact mathematical filter for long/compound K17 packet
generation. By itself the theorem does not construct a support or
reconnection, does not turn a non-Hamilton path bank into a middle-levels
decoration, and does not certify a full ordered four-transversal.  The
companion common-exterior census subsequently supplies exact `C10` examples
which pass the excess-nonincreasing row, without changing those latter scope
limitations.

The shell data and its complete target list are frozen in
scratch/threadD_k17_shared_lower_turn_shell_20260731.audit.json, SHA-256
054151fad4b4f02cfe7e6985256e5800f115404c19ad50c18e2a4b1bd0128e03.
The independent source-rank audit is
scratch/threadD_k17_lower_turn_shell_20260731.audit.json, SHA-256
5157fe9ef84e3790df0f708c1e694755b9f3842a402ed109b46176e0772478f0.
Only its matching rank, missing floor and excess are used here; its
matching-dependent exposed-vertex type profile is not used.
The literal 308-row is independently frozen in
scratch/threadD_k17_source_active_hall_witness_independent_20260731.audit.json,
SHA-256
226ef2c9bd9f18c05de4b9b8b48d14688936186d47df8d43ee6595676aec6cbf.
