# Facet derivatives, exact shadow-safe rethreading, and the first K16 orbit absorber

Date: 2026-07-29

## 0. Result and boundary

This note proves four statements.

1. If an oriented rank-\((r+1)\) Johnson factor is \(T=(T_i)\) and
   \[
   X_i=T_i\cap T_{i+1},
   \]
   then every fixed lower shadow of \(X\) is exactly a one-level shift of a
   lower shadow of \(T\).  If \(T\) has no singleton positive coordinate
   run, every arbitrary-width upper witness of \(X\) is exactly an
   interior union witness of \(T\).

2. For an arbitrary cut and rethread, all-depth preservation is equivalent
   to a finite survivor-or-absorber condition.  Every cut unique witness
   must be accounted for by a survivor or a replacement absorber, but
   unique-witness rows alone are not sufficient: a target with several old
   witnesses can lose all of them at different cuts.

3. For the frozen asymmetric \(K=16\) factor
   \[
   {\cal F}=A\sqcup(B+z),
   \]
   the initial repair demand compresses exactly to nine rotation rows:
   three lower-\(q2\) rows and six arbitrary upper rank-eleven rows.  Every
   lower repair is forced to use a \(BB\) seam.  Consequently at least
   twenty-three new physical \(BB\) seams, and at least two \(Z_{15}\)-orbits
   of \(BB\) seams in an equivariant repair, are necessary to fill the lower
   holes.  This is a capacity theorem, not an existence theorem.

4. The frozen triangle packet is a literal positive base case.  Fifteen
   directed three-cycles, forming one free \(Z_{15}\)-orbit, preserve degree,
   Johnson legality, positive residence, both \(q1\) palettes, and the entire
   lower-\(q2\) ledger, while filling exactly the upper orbit represented by
   \(39911\).  Arbitrary upper holes fall from \(78\) to \(63\), and no
   arbitrary rank-twelve hole is created.  The residual bank has eight
   quotient rows.

The note does not construct the remaining absorber.  It gives its exact
finite formulation.  The post-packet census proves only that no
fixed-\(q3\)-positive, q1- and deep-safe single reciprocal two-switch or
directed three-, four-, or five-cycle exists in the audited short-cycle
catalogue.  Its gain predicate does not detect an upper target whose first
new witness is longer than four states.  It also does not exclude a compound
packet whose individually unsafe circuits cancel one another.

## 1. Canonical shadow convention

Let \(F=(F_i)\) be an oriented cyclic factor in
\(\binom{\Omega}{r}\).  Indices are cyclic within a component.  In the
canonical graded-quotient convention define
\[
 L_q^F(i)=\bigcap_{a=0}^{q}F_{i+a}.
\]
Thus lower depth \(q\) always uses the fixed \(q\)-edge, \(q+1\)-state
window.

For upper shadows define
\[
 U_\ell^F(i)=\bigcup_{a=0}^{\ell}F_{i+a}.
\]
The rank increment of the target does not fix \(\ell\).  A proper upper
target is covered if it is the accumulated union of some nonempty
contiguous interval.  The full set is premarked in the final compiler and
does not require an internal factor interval.

This distinction matters from upper depth three onward.  A target can have
a five-state union witness although neither adjacent four-state subinterval
has the same union.  Fixed upper-\(q\) replay is therefore a useful strong
local test, but the accumulated-union automaton is authoritative.

## 2. Exact derivative identities

### Theorem 2.1: lower derivative identity

Let \(T=(T_i)\) be an oriented cyclic Johnson factor in
\(\binom{\Omega}{r+1}\), and put
\[
 X_i=T_i\cap T_{i+1}\in\binom{\Omega}{r}.
\]
Then for every \(q\geq0\),
\[
 \boxed{L_q^X(i)=L_{q+1}^T(i).}
 \tag{2.1}
\]

#### Proof

Associativity and idempotence of intersection give
\[
\begin{aligned}
L_q^X(i)
 &=\bigcap_{a=0}^{q}(T_{i+a}\cap T_{i+a+1})\\
 &=\bigcap_{a=0}^{q+1}T_{i+a}
 =L_{q+1}^T(i).
\end{aligned}
\]
No run hypothesis is used. \(\square\)

The identity is a statement about the indexed sequence.  It does not by
itself say that \(X\) is a spanning factor: distinct edges of \(T\) may have
the same intersection.  Spanning ownership of \(X\) requires the separate
exact intersection-deck hypothesis.

### Theorem 2.2: arbitrary-width upper derivative identity

Assume that no coordinate trace of \(T\) has a singleton positive run.
Then, for every \(\ell\geq1\),
\[
 \boxed{U_\ell^X(i)=\bigcup_{a=1}^{\ell}T_{i+a}.}
 \tag{2.2}
\]

#### Proof

Fix a coordinate \(x\) and let \(t_j=1_{\{x\in T_j\}}\).
The left side contains \(x\) precisely when some adjacent pair
\((t_{i+a},t_{i+a+1})\), \(0\leq a\leq\ell\), equals \(11\).
Such a pair contains an index from \(i+1,\ldots,i+\ell\), so the right side
contains \(x\).

Conversely suppose \(t_{i+b}=1\) for some \(1\leq b\leq\ell\).  Since this
one is not an isolated positive run, at least one of its cyclic neighbours
is also one.  Hence either
\((t_{i+b-1},t_{i+b})=11\) or
\((t_{i+b},t_{i+b+1})=11\).  The corresponding intersection is one of
\(X_i,\ldots,X_{i+\ell}\).  Thus the left side contains \(x\).  The
coordinatewise equivalence proves (2.2). \(\square\)

### Corollary 2.3: shifted all-depth inheritance

A \(T\)-interval
\[
 T_a,T_{a+1},\ldots,T_b
\]
and the \(X\)-interval
\[
 X_{a-1},X_a,\ldots,X_b
\]
have the same union.  Consequently
\[
\begin{array}{c|c}
\text{\(X\) witness}&\text{\(T\) witness}\\ \hline
\text{lower depth \(q\), rank \(r-q\)}
  &\text{lower depth \(q+1\)}\\
\text{upper rank \(r+q\)}
  &\text{upper rank \(r+q\) with one fewer interior level}.
\end{array}
\]
Thus an all-depth \(T\) factor transfers its shifted tower to \(X\), subject
only to the stated no-singleton hypothesis for upper witnesses.

### Proposition 2.4: converse antiderivative

Let \(Y=(Y_i)\) be a rank-\(r\) Johnson two-factor whose upper-\(q1\)
edge colours form a perfect palette.  Put
\[
 T'_i=Y_{i-1}\cup Y_i.
\]
Then the \(T'_i\) enumerate the rank-\((r+1)\) states exactly once and
\[
 \boxed{Y_i=T'_i\cap T'_{i+1}.}
 \tag{2.3}
\]

Indeed both adjacent upper colours contain \(Y_i\).  They are distinct,
because an exact palette cannot use one colour twice.  Two distinct
rank-\((r+1)\) supersets of the same rank-\(r\) set intersect exactly in
that set.

Moreover the trace of \(T'\) is the adjacent-OR dilation of the trace of
\(Y\):
\[
 1_{\{x\in T'_i\}}
 =1_{\{x\in Y_{i-1}\}}\vee1_{\{x\in Y_i\}}.
\]
A nonconstant positive \(Y\)-run of length \(a\) becomes a positive
\(T'\)-run of length \(a+1\).  In particular positive residence four for
\(Y\) supplies the hypothesis of Theorem 2.2.

This proves that an upper-perfect rethread remains a literal turn
derivative.  It does not prove that the reconstructed antiderivative has
the old shadow support.

## 3. The exact cut-kernel

Let \(F_0\) be an all-depth factor.  Delete a set \(H\) of old edges, retain
the resulting oriented segment interiors, and join exposed ports with a set
\(M\) of new seams.  Segment reversal is allowed.

For a fixed lower or fixed upper depth \(q\), and an occurrence-labelled
target \(Z\), write

- \(\lambda_q(Z)\) for its old witness-window count;
- \(d_q(Z)\) for the number of old \(Z\)-windows whose internal edge set
  meets \(H\);
- \(a_q(Z)\) for the number of final \(Z\)-windows whose internal edge set
  meets \(M\).

Each window is counted once even if it crosses several deleted or new seam
edges.

### Theorem 3.1: exact fixed-window load identity

\[
 \boxed{\lambda'_q(Z)=\lambda_q(Z)-d_q(Z)+a_q(Z).}
 \tag{3.1}
\]

Hence fixed-depth coverage is equivalent to
\[
 \boxed{a_q(Z)\geq d_q(Z)-\lambda_q(Z)+1.}
 \tag{3.2}
\]

#### Proof

A final window avoiding \(M\) lies wholly in a retained old segment.
Reading the segment in either orientation gives the same intersection or
union.  Thus seam-free final witnesses are in bijection with old witnesses
avoiding \(H\).  All remaining final witnesses meet \(M\).  The two classes
are disjoint and yield (3.1); positivity gives (3.2). \(\square\)

An interval may cross several seams.  This causes no defect in (3.1),
because it is one occurrence in \(a_q(Z)\), not one occurrence per seam.
The familiar estimates
\[
 \sum_Zd_q(Z)\leq q|H|,
 \qquad
 \sum_Za_q(Z)\leq q|M|
\]
hold for fixed \(q\), with equality when the corresponding
\(q\)-neighbourhoods are disjoint.

## 4. Arbitrary upper shadows: survivor or accepting path

For each fixed lower target \(S\), let \({\cal W}_S^-\) be its old fixed
window witnesses.  For each proper upper target \(U\), let
\({\cal W}_U^+\) be all of its old contiguous union witnesses, of arbitrary
width.  Define
\[
 {\rm Crit}(H)
 =\{Z:\hbox{ every old required witness of \(Z\) meets \(H\)}\}.
 \tag{4.1}
\]

### Theorem 4.1: finite shadow-safe seam criterion

The rethreaded factor is shadow-complete in the canonical graded convention
if and only if every \(Z\in{\rm Crit}(H)\) has a new accepting path.

For a lower target \(S\) at depth \(q\), an accepting path is a selected
\(q\)-edge Johnson path
\[
 V_0,\ldots,V_q
\]
with \(\bigcap_jV_j=S\).

For a proper upper target \(U\), use the finite state graph
\[
 (\hbox{accumulated union},\hbox{ current middle state contained in \(U\)}).
\]
A selected Johnson transition updates the accumulated union, and a state is
accepting when that union is \(U\).

#### Proof

If an old witness avoids every cut, it survives inside one retained segment,
possibly reversed.  If no old witness survives, coverage is exactly the
existence of a new contiguous witness, which is exactly a lower state path
or an accepting accumulated-union path.  The factor is finite, so both path
families are finite. \(\square\)

Equivalently, with seam variables \(y_s\), every critical target has a
finite monotone disjunction
\[
 \bigvee_{\alpha\in{\cal P}_Z}
       \bigwedge_{s\in J(\alpha)}y_s.
 \tag{4.2}
\]
Path variables \(w_\alpha\) linearize (4.2) by
\[
 w_\alpha\leq y_s\quad(s\in J(\alpha)),
 \qquad
 \sum_{\alpha\in{\cal P}_Z}w_\alpha\geq1.
\]

### Corollary 4.2: what unique-witness guards do and do not prove

If \(Z\) has a unique old witness, cutting an internal edge of that witness
forces an absorber path.  These survivor-or-absorber rows are mandatory.
Protecting one chosen old witness for every target is a sufficient cut-only
condition.

Protecting the old witness in either of the preceding ways is not necessary
for a successful rethread, because a new path may replace it.  The
survivor-or-absorber row itself is necessary.  Unique-witness rows alone are
not sufficient: a target with two old witnesses can lose one at each of two
cuts.  The exact minimal bank is the critical-target bank (4.1), recomputed
for the proposed cut set.

This is the missing qualification behind any claim that q1 and residence
alone preserve the PBBS tower.

For the frozen canonical \(B_0\) all-depth audit, the complete nonzero
load-one census is
\[
\begin{array}{c|rrrrrrrr}
\text{rank}&4&5&6&7&8&9&10&11\\ \hline
\text{load-one targets}
 &90&900&3630&6435&6435&3675&1095&30.
\end{array}
\tag{4.3}
\]
Ranks six and eight are the two q1 palettes and rank seven is the owner
deck.  Away from those baseline rows, (4.3) gives \(90,900,3675,1095,30\)
literal mandatory last-witness guards.  Ranks with no load-one targets
still require (4.2), because several positive-load witnesses can all be
cut.

## 5. Four-separated local signatures

Suppose a seam joins ports \(p\) and \(p'\).  Write their inward states as
\[
 V^p_0,V^p_1,V^p_2,\ldots,
 \qquad
 V^{p'}_0,V^{p'}_1,V^{p'}_2,\ldots,
\]
where the two zero-index states are the seam endpoints.  The final local
order is
\[
 \ldots,V^p_2,V^p_1,V^p_0,V^{p'}_0,V^{p'}_1,V^{p'}_2,\ldots.
\]

The two lower-\(q2\) signatures are
\[
 V^p_1\cap V^p_0\cap V^{p'}_0,
 \qquad
 V^p_0\cap V^{p'}_0\cap V^{p'}_1.
 \tag{5.1}
\]
The three fixed upper-\(q3\) signatures are
\[
\begin{split}
 &V^p_2\cup V^p_1\cup V^p_0\cup V^{p'}_0,\\
 &V^p_1\cup V^p_0\cup V^{p'}_0\cup V^{p'}_1,\\
 &V^p_0\cup V^{p'}_0\cup V^{p'}_1\cup V^{p'}_2.
\end{split}
\tag{5.2}
\]

If all retained fragments have at least four states, every window of depth
at most three crosses at most one seam, so (5.1) and (5.2), together with
the old survivors, give exact fixed-depth ledgers.  Equation (5.2) is only a
sufficient local library for arbitrary upper rank eleven.  The exact upper
test remains Theorem 4.1.

### Proposition 5.1: exact positive-residence seam test

Assume that every prospective positive run of length below the required
threshold \(d\) meets at most one new seam.  It is enough, for example, that
every retained fragment between consecutive new seams contain at least
\(d\) states.

For a coordinate \(x\), let \(s_x(p)\) be the length of the trailing
positive run at \(V^p_0\), and let \(t_x(p')\) be the length of the leading
positive run at \(V^{p'}_0\), with value zero when the endpoint bit is zero.
Lengths may be truncated at the required residence threshold \(d\).  The
new seam creates a short positive run in coordinate \(x\) exactly when
\[
 0<s_x(p)+t_x(p')<d.
\tag{5.3}
\]
Thus (5.3) failing for every coordinate is the exact local port
compatibility row under the one-seam-run hypothesis.  A cut-halo separation
of at least \(2d-1\), preserved by the final fragment assembly, supplies
that hypothesis.  The triangle packet has \(d=4\) and old cut gap at least
seven; its simultaneous physical replay, rather than old spacing alone,
checks the final collars directly.

## 6. The frozen asymmetric K16 endpoint

The source is the literal rank-eight factor
\[
 {\cal F}=A\sqcup(B+z),
\]
where \(A\) is all-depth complete and \(B\) is the complement of the
documented seed7 factor.  The frozen source factor and audit hashes are
\[
\begin{split}
{\rm factor}:&\quad
4f5368d063bcfddfe5c2be6d7f68d5ebc38327ee3c4f40d6b00d9d05c1ace139,\\
{\rm audit}:&\quad
d7aa0e13f0e30d0d814187d6892662cc4234d7f81e901c70bac4559fe3377e23.
\end{split}
\]

The factor is Johnson-legal, has positive residence four, and covers both
\(q1\) palettes.  Its only fixed lower holes are \(45\) rank-six targets at
depth two.  Its only arbitrary upper holes are \(78\) rank-eleven targets.

Under \(Z_{15}\), the lower holes are three free orbits represented by
\[
 \boxed{33337,\quad33609,\quad34069.}
 \tag{6.1}
\]
The upper holes are five free orbits represented by
\[
 \boxed{36343,\quad36599,\quad39791,\quad39911,\quad40623}
 \tag{6.2}
\]
and one orbit of size three represented by
\[
 \boxed{46811.}
 \tag{6.3}
\]
Thus
\[
45=3\cdot15,\qquad78=5\cdot15+3.
\]
The initial deficit is exactly nine quotient rows, but the physical row
weights must be retained.

### Proposition 6.1: the lower holes force BB service

Every target in (6.1) contains \(z\).  Any intersection window containing an
\(A\)-state omits \(z\).  Hence every new witness of a lower hole is a
\(BBB\) triple, and it contains at least one new \(BB\) seam.

### Proposition 6.2: sharp lower-q2 seam capacity

Let \(h\) be the number of new physical \(BB\) seams.  The number of
two-edge windows meeting at least one such seam is at most \(2h\).  Therefore
\[
 \boxed{h\geq\lceil45/2\rceil=23.}
 \tag{6.4}
\]

More sharply, if the seam edges form \(\kappa\) cyclic clusters and are not
all edges of the component, the number of changed two-edge windows is
\[
 h+\kappa.
 \tag{6.5}
\]
At \(h=23\), filling \(45\) distinct holes forces \(\kappa\geq22\).  Thus
all seams are isolated except possibly one adjacent pair.  If the cuts also
destroy all old witnesses of \(c_2\) previously covered lower targets, then
\[
 45+c_2\leq46,
\]
so \(c_2\leq1\).

For a \(Z_{15}\)-equivariant braid, one seam orbit supplies at most two
lower-\(q2\) signature orbits.  Three free deficit orbits therefore force
\[
 \boxed{\text{at least two \(BB\) seam orbits, hence at least 30 seams}.}
 \tag{6.6}
\]

These bounds do not use upper repair, endpoint matching, or topology.  They
are necessary and may be unattainable.

### Proposition 6.3: cross-shore parity

If \(b_A,b_B\) are the numbers of opened \(A\)- and \(B\)-segments, and
\(r_{AA},r_{BB},c_{AB}\) are the new seam counts by shore type, then
\[
 2b_A=2r_{AA}+c_{AB},
 \qquad
 2b_B=2r_{BB}+c_{AB}.
 \tag{6.7}
\]
Thus \(c_{AB}\) is even.  In an equivariant construction a genuine
cross-shore braid uses at least two \(AB\) seam orbits.  If it also repairs
the lower holes directly, (6.6) gives a four-orbit capacity floor: two
\(BB\) and two \(AB\) orbits.  A pure \(B\)-shore repair is not subject to
the \(AB\) part of this floor.

No analogous bound of \(26\) seams follows from arbitrary upper coverage.
The estimate \(\lceil78/3\rceil=26\) applies only to the stronger demand
that the three fixed signatures (5.2) themselves cover all upper holes.
Longer accumulated-union paths can do more.

## 7. Exact nine-row provider and absorber system

Fix a physical cut set, oriented retained segments, and a finite legal seam
catalogue.  A selection is a valid shadow-safe repair if and only if all of
the following hold.

1. Every exposed port is used exactly once.

2. Every selected join is a Johnson edge and the resulting middle deck has
   degree two.

3. The signed lower and upper \(q1\) loads remain at least one:
   \[
   \lambda'_1(C)=\lambda_1(C)-d_1(C)+a_1(C)\geq1.
   \tag{7.1}
   \]

4. Every selected port collar is positive-residence compatible.

5. Each of the three lower rows (6.1) has a selected lower accepting path.
   For four-separated seams these are exactly the signatures (5.1).

6. Each of the six upper rows (6.2)--(6.3) has an accepting
   accumulated-union path.

7. Every previously covered target made critical by the cuts has a
   replacement accepting path.

Conditions 5 and 6 are the initial nine-row service demand.  Condition 7 is
the dynamic casualty bank.  It is the reason that filling the 123 named
physical holes alone is not a certificate.

Only after every non-port shadow and colour obligation has already been
discharged or fixed does the residual endpoint feasibility become an
ordinary capacitated matching problem admitting Hall inequalities.  Before
that point the full problem is not an ordinary Hall instance: one seam
simultaneously consumes two ports, chooses two \(q1\) colours, creates two
lower-\(q2\) signatures, changes several upper automaton paths, and changes
residence collars.

A proof-safe sufficient decomposition is:

1. choose pairwise port-disjoint service configurations for the quotient
   deficit rows and for every induced casualty;
2. verify and discharge all of their signed \(q1\), residence, colour-quota,
   and shadow ledgers physically;
3. complete the remaining exposed ports by an endpoint matching with no
   further non-port quota.

The size-three orbit (6.3) has physical weight three.  If a free seam orbit
creates one provider signature for it, the fifteen rotated occurrences hit
each of its three physical targets five times.  Treating it as a unit-weight
quotient row gives false capacity.

More generally, if one seed atom has signed provider count \(a_O\) into a
target orbit \(O\), its generic fifteen-translate closure changes every
physical target in \(O\) by
\[
 \delta_O=\frac{15a_O}{|O|}.
\tag{7.2}
\]
Thus a free row changes by \(a_O\), while the exceptional row represented by
\(46811\) changes by \(5a_O\).  Exact one-per-target service of that row
would require compatible stabilizer structure; mere quotient incidence
cannot express it.

## 8. The triangle-orbit absorber

The file

    scratch/k16_asymmetric_triangle_orbit_repair_20260729.json

materializes fifteen directed three-cycles.  They form one free
\(Z_{15}\)-orbit.  Each cycle cuts three old transitions and cyclically
permutes their heads.  Across the orbit there are \(45\) distinct cuts and
\(45\) new edges.  All cuts lie in one source component and their old cyclic
separation is at least seven.

The materialized factor hash is
\[
6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc,
\]
and its independent replay audit hash is
\[
3519ff2a8e08d48a7e58513a3b631f82b2d7229f2cfef3ab1ecd102ab2ef9f73.
\]

One representative triangle is the literal replacement
\[
\begin{split}
 &(35062,35302),\ (33015,33270),\ (35047,33255)\\
\longmapsto\;&
 (35062,33270),\ (33015,33255),\ (35047,35302).
\end{split}
\tag{8.1}
\]
It supplies upper target \(39911\).  Its fourteen rotations supply the
other members of that free target orbit.

### Theorem 8.1: verified one-orbit upper repair

The simultaneous fifteen-triangle packet has:

- zero non-Johnson edges;
- positive minimum run four and zero positive-residence violations;
- both \(q1\) palettes still complete;
- exactly the same \(45\) lower-\(q2\) holes as the source;
- arbitrary rank-eleven upper holes reduced from \(78\) to \(63\);
- no arbitrary upper hole at rank twelve or any other higher rank.

The fifteen gained upper labels are exactly the \(Z_{15}\)-orbit of
\(39911\).  Hence the packet discharges that quotient row and no other
initial row.

#### Proof

The head permutation preserves indegree and outdegree one at every state.
The frozen materializer checks every new edge by symmetric difference two,
checks that all \(45\) cuts are distinct, and reconstructs all successor
orbits.  It then replays the coordinate run audit, every fixed lower and
upper window, and the independent arbitrary-width accumulated-union audit.
The output values are the assertions above.

The orbit claim is also explicit in the short-cycle census: its fifteen
maximum examples are precisely the rotations of the seed triangle whose
gained label is \(39911\).  Simultaneous replay deletes those fifteen and no
other arbitrary upper holes. \(\square\)

### Important fixed-window nuance

After the packet, fixed four-edge upper replay reports one new free orbit,
namely fifteen rank-twelve fixed-window holes.  The arbitrary-upper audit
reports no rank-twelve hole.  Each such target therefore has a longer
contiguous union witness.

This is a concrete instance in which fixed upper-\(q4\) preservation is
strictly stronger than the compiler's actual arbitrary-width upper
condition.  It validates the accumulated-union formulation in Theorem 4.1.

## 9. The residual eight-row gate

After Theorem 8.1 the unresolved lower rows remain
\[
33337,\quad33609,\quad34069,
\tag{9.1}
\]
and the unresolved arbitrary upper rows are
\[
36343,\quad36599,\quad39791,\quad40623,\quad46811.
\tag{9.2}
\]
Their physical mass is
\[
3\cdot15+(4\cdot15+3)=108.
\]

The lower capacity floor (6.4)--(6.6) is unchanged.  The triangle packet
does not spend a lower provider slot because it creates no gained lower
target.

## 10. Exact next-packet formulation

Let \(s\) be the current successor permutation.  Select distinct old
transitions
\[
 e_j=(u_j,s(u_j)),\qquad 0\leq j<\ell,
\]
and let \(\pi\) be a permutation of their heads.  Replacing them by
\[
 (u_j,s(u_{\pi(j)}))
\tag{10.1}
\]
always preserves middle ownership and degree.  If \(\pi\) is one
\(\ell\)-cycle, call (10.1) a single alternating \(\ell\)-circuit.  A
compound packet is a disjoint union of such head-permutation circuits,
audited only after their signed ledgers are summed.

On a genuinely changed support of size five, the only derangement types are
\[
 (5)\qquad\hbox{and}\qquad(3+2).
\tag{10.2}
\]
Thus the first support-five compound class omitted by a single-cycle census
is exactly one directed triangle plus one reciprocal switch.  Its two atoms
need not be safe separately; their signed q1 and shadow debts may cancel.

### Proposition 10.1: necessary upper-provider eligibility

Let \(U\) be a currently missing rank-eleven target which becomes covered
after a packet.  Every new \(U\)-witness crosses at least one new seam
\(a\to b\), and at every such crossed seam
\[
 a\cup b\subseteq U.
\tag{10.3}
\]
Indeed every middle state on an interval whose union is \(U\) is contained
in \(U\).  A rank-nine seam colour \(a\cup b\) is contained in exactly
\[
 \binom{16-9}{11-9}=\binom72=21
\tag{10.4}
\]
rank-eleven targets.  Hence the next packet must hit the finite eligibility
hypergraph
\[
 {\cal E}(U)=
 \{a\to b:a\cup b\subseteq U
 \text{ and the seam lies on an accepting \(U\)-path}\}.
\tag{10.5}
\]
The containment in (10.3) is necessary but not sufficient: the adjacent
retained fragments must remain inside \(U\) and collectively introduce all
coordinates of \(U\).

### Theorem 10.2: finite admissibility criterion

A proposed packet is a legal improving packet for the residual factor if
and only if:

1. every edge in (10.1) is a Johnson edge, the undirected edge set is
   squarefree, and no directed two-cycle is created;
2. every lower and upper \(q1\) load after the whole packet is positive;
3. every changed coordinate collar has positive runs of length at least
   four;
4. every previously covered required fixed lower target at every depth
   retains a survivor or receives a new fixed-length intersection path;
5. every previously covered proper upper target retains a survivor or
   receives an accumulated-union accepting path;
6. at least one residual row in (9.1)--(9.2) becomes covered, so the
   residual bank strictly decreases, and no dynamic casualty remains
   uncovered.

For a \(Z_{15}\)-equivariant packet, it is enough to impose these conditions
on quotient representatives with physical orbit weights, then replay the
literal lift.  The proof is Theorems 3.1 and 4.1 applied to the aggregate
head permutation; testing the constituent circuits separately is neither
necessary nor sufficient.

### Corollary 10.3: what the short-cycle no-go proves

The post-packet frozen census has factor hash
\[
6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc
\]
and audit hash
\[
e006b295151fdf34aef2ac651d8faf1567fdf433e8baa760f7d538f902b6474e.
\]
Within its complete audited fixed-\(q3\) provider catalogue:

- all \(60\) q1- and deep-safe reciprocal two-switches have zero gain;
- none of the \(529\) directed provider three-cycles is both q1-safe and
  deep-safe;
- none of the \(3142\) directed provider four-cycles is both q1-safe and
  deep-safe.

The separate five-cycle audit has hash
\[
fb0e888e186e3e4d9ba00f00174acbd2b8f82548d309e6ad06d895964e5689fc.
\]
All \(988\) deep-safe members among its \(29521\) directed fixed-\(q3\)
provider five-cycles are q1-unsafe.  Therefore any improving single
head-permutation circuit detected by this separated-cut, fixed-collar
provider model has length at least six.

This does not rule out a compound of short circuits.  Two individually
unsafe circuits may exchange q1 donor tokens or replace one another's
destroyed shadow witnesses.  In particular a \(C_2+C_2\) compound can have
total support four, so the result is not a universal support-five lower
bound.

There is a second, independent scope gap.  The census defines positive gain
using a new lower fixed-\(q2\) or upper fixed-\(q3\) signature.  It does not
run the accumulated-union automaton on every candidate.  A two- through
five-cycle with no fixed four-state provider may still create a longer
rank-eleven witness.  The correct next search object for the canonical
compiler is therefore one of:

- a two- through five-cycle rescored by arbitrary upper reachability;
- one directed fixed-collar circuit of length at least six; or
- an aggregate packet of shorter circuits satisfying Theorem 10.2 only
  after their signed ledgers are summed.

For a full \(Z_{15}\)-orbit of an \(\ell\)-circuit, the nominal support is
\(15\ell\) old and \(15\ell\) new edges, unless the seed has a nontrivial
stabilizer.  Edge-disjointness and the actual stabilizer must be checked
before quotient counts are interpreted physically.

## 11. Smallest live absorber lemma

The carrier-shadow part of the asymmetric \(K=16\) construction would close
if one proves the following finite statement.

### Residual orbit-absorber lemma

There is a physical or \(Z_{15}\)-equivariant aggregate head-permutation
packet on the triangle-repaired factor such that:

1. the three lower rows (9.1) receive triple-intersection providers;
2. the five upper rows (9.2) receive accumulated-union providers;
3. every target made critical by its cut set receives a replacement;
4. degree, Johnson legality, both \(q1\) palettes, and positive residence
   survive.

In an equivariant solution, at least two \(BB\) seam orbits are forced by
the lower rows.  If the packet uses both shores, cross-shore endpoint parity
forces at least two \(AB\) seam orbits as well.  These are necessary
capacities, not a proof that four orbits suffice.

Even this lemma closes only the shadow-safe carrier repair.  Connectivity,
the common-owner graded Hall compiler, and the final upper-safe opening
remain separate gates.

## 12. Audit scope

All identities in Sections 2--7 and 10 are mathematical and do not depend
on a search.  The numerical source and triangle statements are frozen
certificate claims supported by:

- scratch/k16_asymmetric_two_rail_factor_20260729.audit.json;
- scratch/k16_asymmetric_short_rethread_cycles_20260729.audit.json;
- scratch/k16_asymmetric_triangle_orbit_repair_20260729.json;
- scratch/k16_asymmetric_triangle_orbit_repair_20260729.audit.json;
- scratch/k16_asymmetric_short_rethread_cycles_round1_20260729.audit.json;
- scratch/k16_asymmetric_short_rethread_cycles_round1_len5_20260729.audit.json;
- scratch/materialize_k16_asymmetric_triangle_orbit_repair_20260729.py.

The short-cycle files certify only their explicit catalogue and ledger
scope.  They do not certify all higher-support switches or compositions.
The arbitrary-upper replay, rather than the fixed-\(q3\) or fixed-\(q4\)
tables, is authoritative for the graded compiler.

There is one byte-provenance defect.  The materialized triangle factor
records the census digest
\[
da6692cdb2547ac708e69d7c780511f33247101c112483cc825875f0234dad33,
\]
whereas the present extended census file has digest
\[
f859249dc382b80875f438696951c5c32f79709c39d5042b85934df52ce0ca90.
\]
The current census contains the same fifteen explicit triangle orders and
the same frozen source hash, and the materialized factor is self-contained
and independently replayed.  Thus the theorem-level certificate is intact,
but the census dependency is not byte-for-byte closed until that source
file is refrozen.

No solver, web access, remote job, or sustained local computation was used
in preparing this theorem note.
