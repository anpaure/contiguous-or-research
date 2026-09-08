# Exact classification of the bi-flat holonomy gate

## 1. Outcome

The freedom to pair rank-\((m-1)\) occurrences does **not** cancel
holonomy already present in the rank-\(m\) occurrence graph.  It only asks
whether a flat rank-\(m\) potential can be extended across the lower
occurrences.

There is an exact classification of that extension problem.  First solve
the fixed rank-\(m\) voltage graph.  Its solutions have one additive phase
per connected component.  For any choice of those phases, a compatible
rank-\((m-1)\) pairing exists if and only if, target by target and residue
by residue, the two sides have the same number of occurrences with that
phase.  Equivalently, a short collection of group-ring translation
equations must vanish.

For a single interaction-component trade induced by a transposition, the
rank-\(m\) graph contracts to a particularly concrete gain graph on the
negative wreaths.  A loop occurs exactly when the two transposed labels
are antipodal in one of those cyclic orders, and that loop has gain
\(\pm1\).  Hence such a trade has no bi-flat pointing.  This gives a
structural counterexample, not merely a failed choice of lower-occurrence
bijections.

The practical consequence for the **translation-stable bi-flat ansatz** is
important:

> An auxiliary bi-flat construction can repair a nonzero middle holonomy only by
> rerouting or replacing a middle occurrence on every unbalanced cycle.
> Adding lower-rank edges, or adding sectors disjoint from the old middle
> occurrence graph, cannot help.

This statement is not a no-go theorem for arbitrary pointed extensions.
The coarser \(\kappa/\lambda\) criterion of Theorem 6.1 in
`HAAR_ANTIPODAL_SUSPENSION.md` can identify distinct residues and may admit
a single legal pointing even when the exact voltage is not flat.  Such a
coarse solution is not stable under all common translations, so the
averaging argument that guarantees a surviving deeper effect no longer
applies automatically.

## 2. The general extension theorem

Let \(n=2m+1\).  Let \(\mathcal N\) and \(\mathcal P\) be middle-wreath
packings with equal rank-\(m\) and rank-\((m-1)\) incidence vectors.  For
an occurrence of a target \(S\) in an oriented cyclic order \(C\), write
\(s_C(S)\in\mathbb Z_n\) for its start.

The rank-\(m\) occurrence pairing is forced, because a middle-wreath
packing contains each middle target at most once.  Let \(\Gamma_m\) be its
bipartite occurrence graph, oriented from \(\mathcal N\) to
\(\mathcal P\), with voltage

\[
 \gamma(CD)=s_D(S)-s_C(S).                          \tag{2.1}
\]

Suppose first that \(\gamma\) is exact.  Choose one base potential
\(a_v^0\) satisfying

\[
 a_D^0-a_C^0=\gamma(CD)                             \tag{2.2}
\]

on every middle edge.  Let \(\mathscr K\) be the set of connected
components of \(\Gamma_m\), and let \(\kappa(v)\) denote the component of
\(v\).  Every middle-flat potential, and no other one, has the form

\[
 a_v=a_v^0+z_{\kappa(v)},\qquad z_K\in\mathbb Z_n.  \tag{2.3}
\]

For a rank-\((m-1)\) target \(T\), define its phase at an occurrence
\((v,T)\) by

\[
 \phi_z(v,T)=a_v^0+z_{\kappa(v)}-s_v(T).            \tag{2.4}
\]

### Theorem 2.1 (phase-bucket extension criterion)

There are rank-\((m-1)\) occurrence bijections for which the combined
voltage cochain is exact if and only if:

1. the fixed rank-\(m\) voltage cochain is exact; and
2. phases \(z_K\in\mathbb Z_n\) can be chosen so that, for every lower
   target \(T\) and every \(q\in\mathbb Z_n\),

\[
 \#\{(C,T)\in\mathcal N:\phi_z(C,T)=q\}
 =
 \#\{(D,T)\in\mathcal P:\phi_z(D,T)=q\}.           \tag{2.5}
\]

When (2.5) holds, one obtains every required bijection simply by matching
the two occurrence sets independently inside each phase bucket.

#### Proof

If the rank-\(m\) cochain is not exact, its nonzero-voltage cycle remains
a cycle after any lower edges are added.  Thus exactness there is
necessary.  If it is exact, (2.3) is the standard description of all
solutions of a graph coboundary equation.

For fixed \(z\), a negative lower occurrence \((C,T)\) and a positive
lower occurrence \((D,T)\) may be paired flatly exactly when

\[
 a_C-s_C(T)=a_D-s_D(T),
\]

that is, exactly when their phases in (2.4) agree.  The allowable
matching graph for \(T\) is therefore the disjoint union, over
\(q\in\mathbb Z_n\), of complete bipartite graphs between its two phase
buckets.  It has a perfect matching exactly when the two bucket sizes
agree for every \(q\).  This is (2.5), and the choices for different
targets are independent.  \(\square\)

This is a Hall theorem in a degenerate but useful form: all nontrivial
Hall inequalities collapse to equality of the phase-bucket cardinalities.
In particular, choosing a clever lower-occurrence bijection cannot change
whether (2.5) holds.

### Group-ring form

Let \(R_n=\mathbb Z[X]/(X^n-1)\).  For a lower target \(T\) and a middle
component \(K\), put

\[
 f_{T,K}(X)=
 \sum_{\substack{(C,T)\in\mathcal N\\\kappa(C)=K}}
 X^{a_C^0-s_C(T)}
 -
 \sum_{\substack{(D,T)\in\mathcal P\\\kappa(D)=K}}
 X^{a_D^0-s_D(T)}.                                 \tag{2.6}
\]

Then (2.5) is equivalent to the simultaneous translation equations

\[
 \boxed{\quad
 \sum_{K\in\mathscr K}X^{z_K}f_{T,K}(X)=0
 \quad\text{in }R_n\quad\text{for every }T.
 \quad}                                             \tag{2.7}
\]

Thus the only global freedom left after middle flatness is one cyclic
translation per middle component.  If \(\Gamma_m\) is connected, there
is only a common translation, which cancels from (2.7); lower extension
is then a deterministic yes/no property.

## 3. Cyclic Latin-column formulation

For a family of pointed orders \((C,a_C)\), define the rank-\(r\) column
at phase \(q\) by

\[
 \Lambda_r(q)=
 \multiset{I^{(r)}_{a_C-q}(C):C\in\mathcal N}.      \tag{3.1}
\]

Here \(I^{(r)}_i(C)\) is the rank-\(r\) cyclic interval starting at
\(i\).  Each order is a row, and choosing \(a_C\) cyclically shifts that
row.  The phase buckets are precisely the columns of this array.

For a transposition trade \(\mathcal P=\tau\mathcal N\), with the same
point attached to \(C\) and \(\tau C\), Theorem 2.1 becomes

\[
 \boxed{\qquad
 \tau\Lambda_m(q)=\Lambda_m(q),\qquad
 \tau\Lambda_{m-1}(q)=\Lambda_{m-1}(q)
 \quad(q\in\mathbb Z_n).
 \qquad}                                            \tag{3.2}
\]

So bi-flatness means that the middle and first-lower cyclic interval
tables can be row-rotated until every column is invariant under \(\tau\).
This is the promised cyclic-Latin-square interpretation.

## 4. The owner-transfer gain graph for a transposition

Now let \(\tau=(x\ y)\), let \(\mathcal K\) be the negative side of one
legal interaction-component trade, and let the positive side be
\(\tau\mathcal K\).  Identify the positive vertex \(\tau C\) with its
negative progenitor \(C\).

### Lemma 4.1 (a zero vertical edge at every wreath)

Every cyclic order \(C\) has a rank-\(m\) interval fixed by \(\tau\).
Consequently the middle occurrence graph contains a voltage-zero edge
from \(C\) to \(\tau C\).

#### Proof

Each coordinate belongs to exactly \(m\) of the \(n=2m+1\) cyclic
rank-\(m\) intervals.  Hence the total number of incidences of \(x\) and
\(y\) with those intervals is \(2m=n-1\).  If every interval contained
exactly one of \(x,y\), this total would instead be \(n\).  Some interval
therefore contains both or neither and is fixed by \(\tau\).  It occurs
at the same start in \(C\) and \(\tau C\), giving voltage zero. \(\square\)

Contract one such zero edge for every \(C\).  The resulting
**owner-transfer gain graph** \(Q_\tau\) is described without reference
to the bipartite double cover:

* its vertices are the orders \(C\in\mathcal K\);
* for every moved middle-target orbit \(\{S,\tau S\}\), let \(C_S\) and
  \(C_{\tau S}\) be its two owners in \(\mathcal K\);
* orient an edge \(C_S\to C_{\tau S}\) and give it gain

\[
 \delta(S)=s_{C_{\tau S}}(\tau S)-s_{C_S}(S).       \tag{4.1}
\]

Choosing the other member of the orbit reverses both the edge and its
gain, so this is a well-defined gain graph.

### Theorem 4.2 (exact transposition criterion)

The rank-\(m\) occurrence voltage is exact if and only if
\(Q_\tau\) is balanced:

\[
 \sum_{e\in W}\epsilon_e\delta(e)=0\pmod n         \tag{4.2}
\]

for every closed walk \(W\) in \(Q_\tau\).  If the original trade is one
interaction component, then \(Q_\tau\) is connected and a potential
\(a_C\) is unique up to one common additive constant.

#### Proof

For a moved target \(S\), its forced occurrence edge goes from its owner
\(C_S\) on the negative side to \(\tau C_{\tau S}\) on the positive
side and has voltage (4.1).  The occurrence edge for \(\tau S\) gives the
same gain relation with the reverse orientation.  The fixed targets give
only zero vertical edges.  Contracting those vertical edges therefore
turns the middle coboundary equations exactly into

\[
 a_{C_{\tau S}}-a_{C_S}=\delta(S).
\]

Such equations have a solution exactly when all closed-walk gains vanish.
Connectivity is preserved by the zero-edge contraction. \(\square\)

Once this graph is balanced, the complete bi-flat criterion for the
single component is the phase-refined identity

\[
 \#\{C:T=I_i^{(m-1)}(C),\ a_C-i=q\}
 =
 \#\{C:\tau T=I_i^{(m-1)}(C),\ a_C-i=q\}           \tag{4.3}
\]

for every lower target \(T\) and residue \(q\).  Ordinary equality of
the \(B_{m-1}\) shadows gives only the sum of (4.3) over \(q\).

## 5. The antipodal-loop obstruction

### Theorem 5.1

If one order \(C\in\mathcal K\) owns both members of a moved middle
orbit \(\{S,\tau S\}\), then no bi-flat pointing exists.  Equivalently,
if the transposed labels occur at cyclic distance \(m\) in one of the
orders of the trade, the owner-transfer graph has a nonzero loop.

#### Proof

Two distinct rank-\(m\) intervals on a \((2m+1)\)-cycle whose sets differ
by one deletion and one insertion have intersection size \(m-1\).
For two length-\(m\) cyclic arcs this happens only when their starts differ
by \(\pm1\).  In that step the leaving and entering positions are at
cyclic distance \(m\).  Hence

\[
 C_S=C_{\tau S}=C
 \quad\Longleftrightarrow\quad
 \operatorname{dist}_C(x,y)=m,
\]

and the corresponding loop gain is \(\delta(S)=\pm1\), which is nonzero
in \(\mathbb Z_{2m+1}\).  Theorem 4.2 rules out a potential. \(\square\)

For the certified \(m=4\) Haar edge, take

\[
 C=(1,6,4,3,2,8,7,5,9),\qquad \tau=(1\ 2).
\]

The labels \(1,2\) are at positions \(0,4\).  The consecutive middle
windows

\[
 \{1,6,4,3\},\qquad \{2,6,4,3\}
\]

are exchanged by \(\tau\), so the owner-transfer graph has a gain-one
loop.  Moreover \(\{8,7,5,9\}\) is a fixed middle interval and supplies
the zero vertical edge.  Thus the obstruction can already be seen as a
two-edge cycle of voltages \(1\) and \(0\), sharper than the previously
recorded \(+1,-1\) digon.

This answers the automatic-existence question negatively: even a legal,
first-shadow-invisible, exact-factor component trade need not admit any
bi-flat pointing.

### A stronger three-target obstruction for the \(m=4\) seed

The exact coarse criterion of Theorem 6.1 in
`HAAR_ANTIPODAL_SUSPENSION.md` does not rescue the known seed.  In fact,
three middle targets occurring in one negative/positive order pair already
rule out **every** choice of antipodal pointings, before the lower row is
examined.

In ordinary interval order take

\[
\begin{aligned}
 C&=(1,3,4,8,6,7,9,5,2),\\
 D&=(1,5,9,7,6,8,4,3,2).
\end{aligned}                                       \tag{5.1}
\]

These are the fourth negative and fourth positive orders of the certified
trade.  The following three common middle targets have the indicated
starts:

\[
\begin{array}{c|cc}
S&s_C(S)&s_D(S)\\ \hline
\{1,2,3,4\}&8&6\\
\{1,2,3,5\}&7&7\\
\{3,4,6,8\}&1&4.
\end{array}                                         \tag{5.2}
\]

For \(m=4\), the five fibres of the coarse middle signature \(\kappa\)
are

\[
 \{0,1,2\},\quad\{3\},\quad\{4\},\quad
 \{5,6,7\},\quad\{8\}.                            \tag{5.3}
\]

Let \(a,b\in\mathbb Z_9\) be arbitrary pointings of \(C,D\), and put
\(x=a-8\), \(d=b-a\).  Equality of the three lifted middle incidences
would require

\[
\begin{aligned}
 \kappa(x)&=\kappa(x+d+2),\\
 \kappa(x+1)&=\kappa(x+d+1),\\
 \kappa(x+7)&=\kappa(x+d+4).                       \tag{5.4}
\end{aligned}
\]

For completeness, the allowed values of \(d\) in the three equations are
listed below.  Concatenated digits denote subsets of \(\mathbb Z_9\).

\[
\begin{array}{c|ccc}
x&D_1(x)&D_2(x)&D_3(x)\\ \hline
0&078&018&123\\
1&678&078&3\\
2&567&0&345\\
3&7&0&234\\
4&7&012&123\\
5&078&018&3\\
6&678&078&3\\
7&567&0&345\\
8&7&012&234
\end{array}                                         \tag{5.5}
\]

Every row has empty three-way intersection.  Hence (5.4) has no solution.
This proves:

> No one-point-per-old-wreath antipodal extension of the certified
> \(m=4\) trade preserves even the new middle incidence, whether or not
> exact voltage flatness or translation stability is required.

The complete \(9^8\) side-signature enumeration was also run remotely as
an independent audit and found zero equal middle signatures.  The
three-target table (5.5), however, is already a self-contained finite
proof.  The audit programs are
`find_haar_m4_coarse_pointing.cpp` and
`analyze_haar_m4_coarse_core.cpp`.

## 6. What an auxiliary bi-flat suspension must actually change

Exactness of a cochain restricts to every subgraph.  Therefore no choice
of rank-\((m-1)\) bijections can repair an unbalanced cycle in
\(Q_\tau\), and adjoining occurrence components disjoint from that cycle
cannot repair it either.

For the antipodal loop, a bi-flat suspension must reroute at least one of:

1. the moved target occurrence producing the gain-\(\pm1\) loop; or
2. the fixed target occurrence producing the zero vertical identification.

More generally, the set of middle occurrences changed by an auxiliary
Dyck completion must hit every nonzero-gain cycle of \(Q_\tau\).  After
that middle rerouting makes the new gain graph balanced, Theorem 2.1 gives
the exact remaining lower-rank test.  This separates the integral gate
into two noninterchangeable problems:

\[
 \text{middle cycle rerouting}
 \quad\longrightarrow\quad
 \text{phase-bucket balance at rank }m-1.
\]

Within the translation-stable ansatz, it is therefore not enough to seek
additional lower-shadow sectors whose
signed voltages numerically cancel the old defect.  The auxiliary orders
must alter the ownership topology of the new middle targets.

Alternatively one may abandon exact phase flatness and solve the coarse
\(\kappa/\lambda\) equations directly; then preservation of a nonzero
deeper effect becomes a separate condition rather than a consequence of
translate averaging.
