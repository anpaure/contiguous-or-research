# Independent audit: period-three Catalan filter packets and a voltage-safe port criterion

Date: 2026-07-31  
Status: exact finite physical replay through \(a=7\), exact clean-\(H\)
packet decomposition, and a sufficient socket-subdivision theorem; no
all-\(m\) physical filter construction

## 1. Verdict

The exceptional-bank bijection and its count in
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md` are correct:

\[
 {\cal N}_a=\binom{\mathbb Z_{2a+1}}a/\mathbb Z_{2a+1},
 \qquad |{\cal N}_a|=\operatorname {Cat}_a .          \tag{1.1}
\]

The upper bank is a second copy of the same necklace set under
complementation, and the two families of forced partial full-rotation edge
orbits are disjoint.  Thus every exact two-sided transversal uses at least

\[
                         2\operatorname {Cat}_a       \tag{1.2}
\]

partial \(\mathbb Z_q\)-edge orbits.

Two scope qualifications are necessary.

1. The proof establishes the lower bound (1.2), not simultaneous
   attainability of equality.  Accordingly, “exact minimum” is justified
   only after a physical construction with exactly one partial edge orbit
   per necklace is supplied.
2. When \(v_3(q)=1\), “choose one of three phases” describes the minimal
   **\(H\)-invariant** sections supported in one full edge orbit.  An
   unrestricted section can choose its sheet independently above each
   physical exceptional colour.

The second point has a precise general form recorded next.

## 2. Exact clean-\(H\) content of one Catalan filter

Put

\[
 q=6a+3,
 \quad n=q/3=2a+1,
 \quad s=3^{v_3(q)},
 \quad h=q/s,
 \quad H=\langle s\rangle\cong\mathbb Z_h,            \tag{2.1}
\]

and let \(K_3\leq\mathbb Z_q\) be the subgroup of order three.  Fix one
exceptional full-rotation colour orbit \(C\) and one incident free
full-rotation Johnson-edge orbit \(E\).  Then

\[
 C\cong\mathbb Z_q/K_3,
 \qquad E\cong\mathbb Z_q,                            \tag{2.2}
\]

and \(E\to C\) is the quotient map with fibres of size three.  Since
\(H\cap K_3=1\), restriction to \(H\) gives

\[
 \begin{array}{c|c}
 E & s\text{ free }H\text{-orbits}\cr
 C & s/3\text{ free }H\text{-orbits}.
 \end{array}                                          \tag{2.3}
\]

Each \(H\)-colour orbit in (2.3) has exactly three \(H\)-edge orbits above
it, and each of those maps bijectively to that colour orbit.  Consequently:

> **Filter-packet lemma.** A minimal \(H\)-invariant section supported in
> the fixed full edge orbit \(E\) selects exactly \(s/3\) \(H\)-edge
> orbits, one above each exceptional \(H\)-colour orbit.  There are exactly
> \(3^{s/3}\) such sections.

Indeed, after quotienting by \(H\), the map in (2.2) is

\[
 \mathbb Z_s\longrightarrow
 \mathbb Z_s/\overline K_3,                            \tag{2.4}
\]

whose fibres are the three cosets of the residual order-three subgroup.
Choices over its \(s/3\) target points are independent.

Thus the \(2\operatorname {Cat}_a\) objects are filter **packets**.  In a
minimal clean-\(H\) realization they account for

\[
                  2\operatorname {Cat}_a\,{s\over3}   \tag{2.5}
\]

selected \(H\)-edge orbits.  This is compatible with the full-rotation
floor because the \(s/3\) clean orbits in one packet together form one
partial full-rotation orbit section of \(q/3\) physical edges.

For comparison, without \(H\)-invariance a section supported in \(E\) has
\(3^{q/3}\) choices.

## 3. Small physical calibration

The independent replay constructs every necklace through \(a=7\), all of
its exceptional physical colours on both shores, and one deterministic
incident Johnson-edge orbit on each shore.  For every necklace it checks:

* the edge orbit has size \(q\);
* the exceptional colour orbit has size \(q/3\);
* every exceptional physical colour has exactly three incident edges in
  that edge orbit;
* the clean-\(H\) decompositions have respectively \(s\) and \(s/3\)
  orbits, with three edge orbits above each colour orbit; and
* a lower-exceptional edge orbit and an upper-exceptional edge orbit are
  disjoint because the former contains \(\infty\) in every union and the
  latter does not.

For \(a=0,1,2\), it also exhausts all subsets on both outer ranks
(respectively \(4,210,11440\) subsets per rank) and confirms that the
displayed banks are exactly all shortened states.

The first cases are:

\[
\begin{array}{c|c|c|c|c|c|c}
a&q&(h,s)&|{\cal N}_a|&
  H\text{-colour orbits/packet}&
  H\text{-edge orbits/packet}&
  H\text{-invariant sections}\cr\hline
0&3 &(1,3) &1  &1&1&3\cr
1&9 &(1,9) &1  &3&3&27\cr
2&15&(5,3) &2  &1&1&3\cr
3&21&(7,3) &5  &1&1&3\cr
4&27&(1,27)&14 &9&9&3^9\cr
7&45&(5,9) &429&3&3&27.
\end{array}                                           \tag{3.1}
\]

At \(a=2\), the two lower necklace representatives are

\[
                         \{0,1\},\quad\{0,2\}
                         \subset\mathbb Z_5,          \tag{3.2}
\]

with a complementary upper copy.  Hence there are exactly four packets,
each consisting of one \(H\cong\mathbb Z_5\)-edge orbit in this abstract
palette model.  This is not an identification with the four changed edge
classes of the authenticated K16 construction.  There only one changed
lower colour is shortened, no changed upper colour is shortened, all three
residual sectors interlace inside each strict spiral, and the final compiler
breaks \(H\).  The four packets here are therefore filter demands, not
literal K16 seams or compiler defects.

At \(a=1\), by contrast, \(H\) is trivial.  The unique lower necklace is
\(\{0\}\subset\mathbb Z_3\), representing the three colours

\[
 \{\infty,0,3,6\},\quad
 \{\infty,1,4,7\},\quad
 \{\infty,2,5,8\}.                                   \tag{3.3}
\]

A section contains one physical edge over each of these colours and has
\(3^3=27\) possible sheet choices inside a fixed full edge orbit.

## 4. The smallest exact port/voltage model

After the internal paths of a clean-\(H\) quotient forest have been fixed,
orient every quotient path and retain its entry and exit as distinct
occurrence ports.  A candidate connector record is

\[
                    c=(i,j;\delta_c),                 \tag{4.1}
\]

meaning a literal \(H\)-orbit of seams from the exit of quotient path
\(i\) to the entry of quotient path \(j\), of voltage
\(\delta_c\in\mathbb Z_h\).  Parallel records must be retained.
The path occurrences are free: an odd-order stabilizer of a finite path
would act through its automorphism group of order at most two and hence fix
every middle vertex.

Selecting one outgoing and one incoming record at every quotient path
produces a permutation \(\tau\) of the path occurrences.  If \(r_i\) is
the internal voltage of path \(i\), the exact closure conditions are

\[
 \tau\text{ is one cycle},
 \qquad
 \gcd\!\left(h,\sum_i(r_i+\delta_{c_i})\right)=1.     \tag{4.2}
\]

For \(h=1\) the second condition is vacuous.  Equation (4.2), plus literal
port degrees and palette/resource constraints, is the smallest directed
incidence/voltage model: its development is one physical cycle if and only
if (4.2) holds.

If orientations are not fixed, use two occurrence ports per path, the
fixed involution \(P\) pairing the ports of each path, and a connector
perfect matching \(M\).  The exact topological condition is

\[
                         P\cup M\text{ is one cycle}. \tag{4.3}
\]

Tutte's condition characterizes existence of a perfect matching \(M\), and
Hall's condition does so in a bipartite orientation, but neither condition
alone gives (4.2) or (4.3).  One-cycle subtour constraints and the voltage
condition remain independent.

## 5. A generic Hall construction which preserves unit voltage automatically

There is a clean sufficient architecture in which topology and voltage no
longer burden the filter assignment.

Let \(C_0\) be a directed clean-\(H\) quotient skeleton cycle of unit
voltage \(V_0\), and let \(S\) be a set of occurrence-labelled socket arcs
of \(C_0\).  Assume the skeleton contains every nonfilter occurrence and
that one gadget for each packet supplies all reserved occurrences exactly
once.  Let

\[
 \Phi={\cal N}_a^-\sqcup{\cal N}_a^+,
 \qquad |\Phi|=2\operatorname {Cat}_a,                \tag{5.1}
\]

be the lower and upper filter packets.  Join \(f\in\Phi\) to \(e\in S\)
in a bipartite compatibility graph \(B\) when there is a phase choice and
a literal \(H\)-equivariant path gadget \(Q(f,e)\) satisfying all of the
following.

1. For every \(g\in H\), the developed \(Q(f,e)_g\) is an oriented path
   from the exact tail of the developed socket \(e_g\) to its exact head.
2. Its selected internal edges realize one complete section of packet
   \(f\), hence \(s/3\) clean-\(H\) edge orbits.
3. Its developed internal vertices are distinct across all \(g\in H\) and
   disjoint from the developed skeleton.  Each socket has a private
   reserved vertex, colour and guard bank, so gadgets at distinct sockets
   are physically vertex-disjoint, and a saturating gadget choice uses
   exactly all vertices reserved outside the skeleton.
4. Every developed edge is literal and simple.

### Proposition 5.1 (Hall socket-subdivision criterion)

If

\[
                 |N_B(X)|\ge |X|
                 \qquad(X\subseteq\Phi),              \tag{5.2}
\]

then all \(2\operatorname {Cat}_a\) packets can be inserted simultaneously,
and the resulting physical closure is Hamiltonian.

#### Proof

Hall gives distinct sockets for all packets.  Replacing pairwise distinct
arcs of one directed cycle by directed paths leaves one directed cycle.
Because every replacement has the same ordered physical endpoints as the
removed socket lift, its quotient path voltage equals the removed arc
voltage.
Thus the total voltage remains \(V_0\), which is a unit, and the clean-\(H\)
voltage-lift criterion gives one physical cycle.  Conditions 2--4 give the
required filter sections and physical ledgers. \(\square\)

In this generic reduction, filter packets are the left vertices and
endpoint-preserving socket orbits are the right vertices.
The packet's \(s/3\) internal \(H\)-edge orbits belong inside one gadget;
treating them as unrelated Hall demands would lose the requirement that
they form one full-rotation section.

The paired-\(P_4\) construction gives a smaller specialized model: the
necklace flag matching first pairs one lower and one upper track, leaving
\((s/3)\operatorname {Cat}_a\) quotient \(P_4\) paths.  Their omitted
fourth edges are native ordered sockets, so a reduced unit-voltage cycle
which already contains those sockets needs no further filter--socket Hall
assignment; simultaneous literal square subdivisions preserve voltage.

If distinct socket gadgets can share internal resources, (5.2) is no
longer sufficient.  The exact candidate model then has one binary variable
\(x_c\) per phase-labelled gadget and the constraints

\[
 \sum_{c:f(c)=f}x_c=1,
 \quad
 \sum_{c:e(c)=e}x_c\le1,
 \quad
 \sum_{c:r\in R(c)}x_c\le1,                           \tag{5.3}
\]

for every filter, socket and physical resource.  This is a conflict
hypergraph matching problem, not ordinary Hall.

Finally, if a gadget connects the socket orbits with a different phase,
write

\[
 d(c)=\operatorname {vol}(Q(c))-\operatorname {vol}(e).          \tag{5.4}
\]

The exact additional condition on a selected conflict-free transversal is

\[
                  \gcd\!\left(h,V_0+\sum_c d(c)x_c\right)=1.     \tag{5.5}
\]

For composite \(h\), distinct possible voltages do not imply (5.5).
Endpoint-preserving physical subdivision is therefore the robust
construction: it forces every defect in (5.4) to zero and retains unit
voltage without a tuner.

## 6. Complement pairing: valid provider symmetry, invalid connector shortcut

For the \(v_3(q)=1\) provider bank in Theorem 3 of the recursion note, let
\({\cal A}_{\rm filt}\) denote the prescribed lower-filter and
upper-filter edges.  The construction has the following exact properties.

* \({\cal A}_{\rm filt}\) is closed under setwise complementation of both
  middle endpoints.
* Its lower colours and upper colours are separately injective, so it is a
  partial inclusion matching.
* Its middle endpoints are pairwise distinct.
* In the clean quotient it contains \(2\operatorname {Cat}_a\) edges on
  \(4\operatorname {Cat}_a\) middle vertices.

Complementation exchanges intersection and union colours by

\[
 \ell(e^c)=\Omega\setminus u(e),\qquad
 u(e^c)=\Omega\setminus\ell(e),                       \tag{6.1}
\]

which proves the first two statements from the displayed construction.
The complete-coset occupancy and the one extra finite point recover each
lower endpoint; upper endpoints are their distinct complements.

The exact clean-\(H\) extension target is therefore:

1. an \(H\)-invariant perfect lower--upper inclusion matching
   \(F\supseteq{\cal A}_{\rm filt}\);
2. the selected Johnson-edge lift of \(F\) is a spanning linear forest;
3. legal \(H\)-orbits of endpoint connectors use every endpoint occurrence
   once (two occurrences at an isolated one-vertex path) and form one
   occurrence-level cycle after path contraction; and
4. that quotient cycle has primitive total \(H\)-voltage.

These conditions are sufficient by the regular voltage-lift theorem and
are the right exact criterion for this prescribed bank.  The connector
orbits need not be complement-paired, and there is no filter-to-connector
bijection: prescribed filter edges may lie anywhere inside the final
paths.  Compiler, residence or cap-two equivariance is an additional
hypothesis, not a consequence of this graph criterion.

### Complement nonadjacency warning

Complementation does **not** supply a connector between paired middle
vertices.  For every \(m\)-set \(X\subset\Omega\),

\[
 |X\mathbin\triangle(\Omega\setminus X)|=2m,\qquad
 d_{J(2m,m)}(X,\Omega\setminus X)=m.                  \tag{6.2}
\]

Since \(m\ge2\), \(X\) is never Johnson adjacent to its complement.  The
smallest counterexample is

\[
 \Omega=\{\infty,0,1,2\},\quad
 X=\{\infty,0\},\quad X^c=\{1,2\};                   \tag{6.3}
\]

their symmetric difference has size four, not two.  Thus a proposed
“reverse-complement zipper” which directly joins a path endpoint to its
complement is not physical.  Reverse-complement paths do have opposite
voltage after compatible gauges, but cancellation is useful only after
literal connector edges have independently been supplied.

The native socket \(X_iY_j\) in the paired-\(P_4\) construction avoids this
error: \(X_i\) and \(Y_j\) differ by the single exchange
\(\infty\leftrightarrow c_k\), so they are genuinely Johnson adjacent.
Replacing that ordered socket by the other three sides of its literal
square preserves both endpoints and voltage exactly.

### Quotient path capacity

Write \(d=s/3\), so \(h=(2a+1)/d\), and put

\[
                         p={\operatorname {Cat}_{3a+2}\over h}.  \tag{6.4}
\]

Then \(p\) is even and

\[
                         p\ge 2d\operatorname {Cat}_a.           \tag{6.5}
\]

For parity, \(\operatorname {Cat}_r\) is odd exactly when
\(r=2^t-1\).  The identity \(3a+2=2^t-1\) would give
\(3(a+1)=2^t\), which is impossible; division by the odd number \(h\)
preserves evenness.

For (6.5), cancel \(d\) using \(h=(2a+1)/d\).  It remains to prove

\[
 \operatorname {Cat}_{3a+2}
   \ge 2(2a+1)\operatorname {Cat}_a.                  \tag{6.6}
\]

The case \(a=0\) is equality.  For \(a\ge1\), every factor in

\[
 {\operatorname {Cat}_{3a+2}\over\operatorname {Cat}_a}
 =\prod_{r=a}^{3a+1}{2(2r+1)\over r+2}
\]

is at least two, and \(2^{2a+2}\ge2(2a+1)\).

At \(v_3(q)=1\), (6.5) reads
\(p\ge2\operatorname {Cat}_a\).  For the disjoint paired-\(P_4\) normal
form, the stronger \(p\ge2d\operatorname {Cat}_a\) supplies enough scalar
bulk-component capacity to alternate every packet with a bulk path.
Neither inequality proves the required inclusion matching, endpoint
adjacencies, Hall condition or primitive voltage; a general extension may
also place several prescribed filter edges in one path, so distinct
filter-to-path assignment is not necessary.

## 7. Replay

Run

```text
python3 scratch/audit_catalan_period3_filter_sections_independent_20260731.py --max-a 7
```

The frozen output is

```text
scratch/catalan_period3_filter_sections_independent_20260731.audit.json
```

with canonical payload SHA-256

```text
06e65031416a19f95c517ad004840d7497e59b58d12df0e96d0937cdcc3a36e2
```

The replay proves no simultaneous physical socket bank.  Proposition 5.1
isolates exactly what such a bank must supply.
