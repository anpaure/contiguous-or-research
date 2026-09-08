# The exact depth-one common refinement: GMM rigidity, Middle-Levels closure, and the Hall component ledger

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 \mathcal X=\binom{[n]}m,\quad
 \mathcal L=\binom{[n]}{m-1},\quad
 \mathcal U=\binom{[n]}{m+1},
\]

\[
 W=|\mathcal X|=|\mathcal U|,\qquad
 N=|\mathcal L|={m\over m+2}W,\qquad
 d=W-N={2W\over m+2}.
\tag{0.1}
\]

The exact spanning depth-one common-refinement problem is the following.

> Find a spanning Johnson \(2\)-factor \(C\subseteq J(n,m)\) such that
> every upper colour \(X\cup Y\in\mathcal U\) occurs exactly once, every
> lower colour \(X\cap Y\in\mathcal L\) occurs at least once, and
> \(C\) has \(o(W/H)\) components, where \(H=o(m)\).

The word ``injective'' belongs to the upper ledger in this normalization.
A spanning \(2\)-factor has \(W\) edges but \(|\mathcal L|=W-d\), so its
lower map cannot be injective.  Its total lower repeat excess is forced to
be exactly \(d\).

There are two versions which must not be conflated.

* The **coverage version** asks only \(\mu^-(R)\ge1\).  The capacitated
  Hall theorem below is necessary and sufficient for its additive
  completion.
* The **balanced version** additionally asks
  \(\mu^-(R)\in\{1,2\}\), the exact floor/ceiling quota.  This adds one
  lower-colour capacity to every completion edge.  Its exact system is
  (2.3a)--(2.3d) below and is not an ordinary network flow.

All component estimates proved here apply to both versions.  Unqualified
"common refinement" below means the coverage version stated above.

This note proves four exact conclusions.

1. **Component fusion is automatic after the correct core exists.**  If an
   exact lower core is a forest and passes the residual capacitated-Hall
   inequalities, every completion has at most

   \[
                             d={2W\over m+2}=o(W/H)                 \tag{0.2}
   \]

   components.  Thus no additional Hamiltonicity or component-fusion
   theorem is needed for the stated \(o(W/H)\) target.

2. **A projected GMM tight enumeration has a sharp rigid-occurrence
   obstruction.**  All but at most \(d\) lower colours occur on exactly
   one transition.  Their forced upper colours must already be pairwise
   distinct.  After reserving them, only a matching problem on at most
   \(d\) flexible lower colours remains.  A collision between two forced
   colours cannot be repaired while staying inside that GMM cycle.

3. **The published Middle-Levels component target is already solved.**
   The canonical \(0/1\)-lexical cycle factor has at most
   \(\operatorname {Cat}_m=W/(2m+1)=O(W/m)=o(W/H)\) components and its
   projected upper colours are already a bijection.  It is the desired
   coverage common refinement if and only if its lower colours are
   hole-free; for balance their loads must additionally be at most two.
   The same criterion holds for a joined Middle-Levels Hamilton cycle, for
   which deleting one occurrence of each lower colour makes the deleted
   edges an exact self-completion.

4. **The PBBS two-sided rainbow pseudoforest already has the required
   quantitative rate, but not exact completion.**  For
   \(H=o(m/\log ^2m)\) it has \(N-k\) edges with \(k=o(W/H)\), and
   \(O(W\log ^2m/m)=o(W/H)\) path components.  If its missing lower
   colours could be inserted while retaining the waste--slack Hall
   inequalities, the component target would follow with at most
   \(d+O(k)=o(W/H)\) cycles.  The published construction does not imply
   these exactification or Hall statements.  The more general fixed-girth
   diagonal has only the weaker unparameterized \(k=o(W)\).

Consequently the depth-one common refinement remains unproved, but its
component clause is no longer an independent gate.  The minimum remaining
hypothesis is an exact colour-compatible, Hall-admissible lower core.

## 1. Signed colours and the exact load ledger

For a Johnson edge \(e=XY\), put

\[
                         \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.
\tag{1.1}
\]

Let \(C\) be a spanning \(2\)-factor on \(\mathcal X\).  Then \(|E(C)|=W\).
If its upper colours are injective, they exhaust \(\mathcal U\).  If its
lower colours are hole-free and

\[
                         \mu_C(R)=|\{e\in E(C):\ell(e)=R\}|,
\]

then

\[
 \mu_C(R)\ge1\quad(R\in\mathcal L),\qquad
 \sum_{R\in\mathcal L}(\mu_C(R)-1)=W-N=d.             \tag{1.2}
\]

Thus (1.2), not lower injectivity, is the exact floor baseline.  In
particular at most \(d\) lower colours can have multiplicity greater than
one, although one colour may have multiplicity larger than two.

For the balanced version, let

\[
 \mathcal Q=\{R\in\mathcal L:\mu_C(R)=2\}.
\]

Then \(|\mathcal Q|=d\), and exact middle ownership forces a stronger
pointwise law.

### Proposition 1.1 (regular repeated-lower family)

In every balanced spanning common refinement,

\[
 d_{\mathcal Q}(x)=\kappa
 :=\frac{d(m-1)}{2m+1}
 =\frac{2(m-1)W}{(2m+1)(m+2)}
 \qquad(x\in[n]).                                               \tag{1.3}
\]

#### Proof

Count, for a fixed coordinate \(x\), incidences between factor edges and
their two middle endpoints which contain \(x\).  Every middle owner
containing \(x\) has factor degree two, so the count is

\[
 2\binom{2m}{m-1}.                                             \tag{1.4}
\]

For one Johnson edge, the number of its endpoints containing \(x\) is the
sum of the indicators that its lower and upper colours contain \(x\).
Upper exactness contributes \(\binom{2m}{m}\).  The once-covered lower
baseline contributes \(\binom{2m}{m-2}\), and the repeated family
contributes \(d_{\mathcal Q}(x)\).  Therefore

\[
 d_{\mathcal Q}(x)
 =2\binom{2m}{m-1}
  -\binom{2m}{m}
  -\binom{2m}{m-2}.
\]

Elementary binomial ratios reduce the right side to (1.3).
\(\square\)

This is necessary but not sufficient: it records the exact point-degree
shadow of middle ownership, not the pairing or component structure.

There is also a near-spanning version.  A \(2\)-factor on exactly \(N\)
owners whose two colour maps are injective uses every lower colour once and
uses \(N\) upper colours once.  Its owner and upper leaves both have size
\(d=o(W/H)\) for \(H=o(m)\).  The projected two-level GMM saturating cycle
has precisely this form on the lower side; its missing assertion is exact
injectivity of

\[
                         R_{i-1}\cup R_i\cup R_{i+1}.              \tag{1.5}
\]

The spanning and near-spanning formulations are therefore distinct.  The
rest of this note treats the spanning formulation, for which the
Middle-Levels projection is the natural one-sided starting point.

## 2. Exact lower cores and capacitated Hall completion

Call \(F\subseteq E(J(n,m))\) an **admissible exact lower core** when

1. every \(R\in\mathcal L\) is the lower colour of exactly one edge of
   \(F\);
2. the upper colours of \(F\) are pairwise distinct; and
3. \(d_F(X)\le2\) for every \(X\in\mathcal X\).

Then \(|F|=N\).  Define

\[
 \delta_F(X)=2-d_F(X),\qquad
 \mathcal U_0(F)=\mathcal U\setminus u(F).                       \tag{2.1}
\]

The two residual masses are

\[
 \sum_{X\in\mathcal X}\delta_F(X)=2(W-N)=2d,
 \qquad |\mathcal U_0(F)|=d.                                    \tag{2.2}
\]

For \(\mathcal A\subseteq\mathcal X\), write

\[
 d_{\mathcal A}(U)=|\{X\in\mathcal A:X\subset U\}|.
\]

### Theorem 2.1 (exact common-refinement Hall theorem)

The core \(F\) extends to a spanning depth-one common refinement if and
only if, for every \(\mathcal A\subseteq\mathcal X\),

\[
 \boxed{
 \sum_{X\in\mathcal A}\delta_F(X)
 \le
 \sum_{U\in\mathcal U_0(F)}\min\{2,d_{\mathcal A}(U)\}.}
\tag{2.3}
\]

Every such completion adds exactly \(d\) Johnson edges, one of each unused
upper colour.

#### Proof

Form the bipartite incidence network between \(\mathcal U_0(F)\) and
\(\mathcal X\).  Give every \(U\) demand two, every \(X\) demand
\(\delta_F(X)\), and every incidence \(X\subset U\) capacity one.  A full
integral flow chooses two distinct facets \(X_U,Y_U\) of each unused \(U\),
and hence the Johnson edge \(X_UY_U\).  Equation (2.2) says that source and
sink masses agree.  The max-flow/min-cut inequalities are exactly (2.3),
and integral capacities give an integral flow.  The added edges fill every
middle degree to two and use each missing upper colour once.  Conversely,
the added edges of any completion give this flow.  Lower coverage is already
present in \(F\). \(\square\)

The same cuts have the waste--slack form

\[
 \omega_F(\mathcal A)\le\sigma(\mathcal A),                    \tag{2.4}
\]

where, writing \(E_U\) for the two endpoints of the core edge of used
upper colour \(U\),

\[
 \sigma(\mathcal A)=
 \sum_{U\in\mathcal U}\min\{2,d_{\mathcal A}(U)\}-2|\mathcal A|,
\tag{2.5}
\]

\[
 \omega_F(\mathcal A)=
 \sum_{U\in u(F)}
 \bigl(\min\{2,d_{\mathcal A}(U)\}-|E_U\cap\mathcal A|\bigr).
\tag{2.6}
\]

This is obtained by subtracting the used-upper contribution from (2.3).
The universal slack \(\sigma\) is nonnegative because the regular
middle-to-upper incidence graph contains a spanning \(2\)-factor.  Formula
(2.4) makes clear why marginal colour balance is insufficient.

### Proposition 2.1B (exact balanced-completion system)

The same core \(F\) extends to a balanced common refinement if and only if
there are variables

\[
 z_{R,U}\in\{0,1\}
 \qquad
 (U\in\mathcal U_0(F),\ R\in\mathcal L,\ R\subset U)
 \tag{2.3a}
\]

satisfying

\[
 \sum_{\substack{R\in\mathcal L\\R\subset U}}z_{R,U}=1
 \qquad(U\in\mathcal U_0(F)),                                  \tag{2.3b}
\]

\[
 \sum_{\substack{U\in\mathcal U_0(F)\\R\subset U}}z_{R,U}\le1
 \qquad(R\in\mathcal L),                                       \tag{2.3c}
\]

\[
 \sum_{\substack{R\subset X\subset U\\U\in\mathcal U_0(F)}}
 z_{R,U}=\delta_F(X)
 \qquad(X\in\mathcal X).                                      \tag{2.3d}
\]

#### Proof

A flag \(R\subset U\), with \(|U\setminus R|=2\), determines the unique
Johnson edge joining the two intermediate \(m\)-sets.  Equation (2.3b)
chooses exactly one edge of every unused upper colour.  Equation (2.3d)
fills every middle degree deficit.  Since the core already uses every
lower colour once, (2.3c) says that no lower load exceeds two.  These
conditions are plainly also necessary for any balanced completion.
\(\square\)

Forgetting (2.3c) and remembering only the two selected facets of each
\(U\) gives the flow in Theorem 2.1.  Thus (2.3) is necessary but not
sufficient for balanced completion.  The distinction is integral, not
notational: for three facets \(X_1,X_2,X_3\) of one \(U\), the three
possible pair flags have, on the middle-capacity rows, the matrix

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.                                                \tag{2.3e}
\]

Hence the balanced residual system is a four-resource hypergraph matching,
not the bipartite flow (2.3).

### Theorem 2.2 (the component clause is automatic)

If an admissible core \(F\) satisfies (2.3), then every completion \(C\)
satisfies

\[
 c(C)\le d+c_{\rm cyc}(F),                                      \tag{2.7}
\]

where \(c_{\rm cyc}(F)\) is the number of cycle components already present
in \(F\).  In particular, if \(F\) is a forest, then

\[
                         c(C)\le d=o(W/H)\qquad(H=o(m)).          \tag{2.8}
\]

#### Proof

A cycle component already contained in \(F\) is saturated and remains a
component.  Every other cycle component of \(C\) contains at least one of
the \(d\) added edges: otherwise it would be a cycle of \(F\).  Distinct
components contain distinct added edges, proving (2.7).  Finally

\[
 {d\over W/H}={2H\over m+2}\longrightarrow0
\]

when \(H=o(m)\). \(\square\)

If \(F\) is a spanning forest, it has exactly

\[
                         W-|F|=d                              \tag{2.9}
\]

path or isolated components.  Thus (2.8) is sharp at the level of this
ledger.  It closes the requested component scale without requiring the
completion to be connected.

### Theorem 2.3 (converse core extraction)

From every spanning depth-one common refinement \(C\), choose one edge of
each lower colour and call the result \(F\).  Then \(F\) is an admissible
core, \(C\setminus F\) witnesses (2.3), and

\[
                         c_{\rm cyc}(F)\le c(C).                 \tag{2.10}
\]

#### Proof

Upper injectivity and degree at most two are inherited from \(C\).  The
unselected edges use precisely the upper colours outside \(u(F)\) and fill
the degree deficits, so they are the residual flow.  A cycle contained in
\(F\) is already saturated at all its vertices and is consequently a whole
component of \(C\). \(\square\)

Hence Theorems 2.1--2.3 are an exact characterization of the coverage
version, not merely a sufficient relaxation.  For the balanced version,
replace Theorem 2.1 by Proposition 2.1B.  The same component proof applies
because either completion adds exactly \(d\) edges.

## 3. GMM tight enumeration: the rigid-occurrence theorem

Let \(P\) be the Hamilton Johnson cycle obtained by contracting a GMM tight
enumeration of levels \(m-1,m\).  Every lower colour occurs at least once.
Exactly \(N\) transitions come from the unique intervening lower vertices,
and the remaining \(d\) transitions are direct middle-to-middle steps.

Construct the occurrence graph

\[
 B_P=(\mathcal L,\mathcal U;E_P),\qquad
 E_P=\{(\ell(e),u(e)):e\in E(P)\}.                              \tag{3.1}
\]

The graph is simple because a pair \((R,U)\), \(R\subset U\), determines
the unique Johnson edge formed by the two intermediate sets.  Its lower
degrees are the lower multiplicities of \(P\), and

\[
 \sum_{R\in\mathcal L}(d_{B_P}(R)-1)=d.                         \tag{3.2}
\]

Put

\[
 \mathcal L_1=\{R:d_{B_P}(R)=1\},\qquad
 \mathcal L_+=\mathcal L\setminus\mathcal L_1.                 \tag{3.3}
\]

Then

\[
                         |\mathcal L_+|\le d.                    \tag{3.4}
\]

For \(R\in\mathcal L_1\), denote its unique upper neighbour by \(v(R)\).

### Theorem 3.1 (exact rigid/flexible transversal criterion)

The occurrence graph \(B_P\) has a matching saturating every lower colour
if and only if both of the following hold.

1. The forced upper colours \(v(R)\), \(R\in\mathcal L_1\), are pairwise
   distinct.
2. After deleting these forced upper colours, the graph

   \[
   B_P[\mathcal L_+,\ \mathcal U\setminus v(\mathcal L_1)]
   \tag{3.5}
   \]

   has a matching saturating \(\mathcal L_+\); equivalently it satisfies
   Hall's inequalities on all subsets of \(\mathcal L_+\).

#### Proof

Every matching saturating \(\mathcal L\) is forced to use the unique edge
at each \(R\in\mathcal L_1\).  These edges must be disjoint, proving the
necessity of condition 1, and their upper endpoints are unavailable to the
remaining lower vertices, proving condition 2.  Conversely, unite the
forced edges with a matching supplied by condition 2. \(\square\)

Thus the flexible Hall instance has at most \(d=O(W/m)\) left vertices,
but the rigidity condition concerns \(N-O(d)\) lower colours.  This is a
sharp obstruction, not a heuristic second-moment issue.

Define the forced collision mass

\[
 \rho(P)=
 \sum_{U\in\mathcal U}
 \bigl(|\{R\in\mathcal L_1:v(R)=U\}|-1\bigr)_+.                 \tag{3.6}
\]

### Corollary 3.2 (sparse-edit lower bound)

No lower-saturating upper-injective core contained in \(P\) exists when
\(\rho(P)>0\).  More generally, any upper-injective choice of one edge for
every lower colour, allowed to use edges outside \(P\), must replace at
least \(\rho(P)\) of the forced \(P\)-occurrences.

#### Proof

At most one forced occurrence with upper colour \(U\) can remain in an
upper-injective family.  Summing the compulsory deletions over (U) gives
(3.6). \(\square\)

Suppose the two conditions of Theorem 3.1 hold, and let \(F\subset P\) be
the corresponding \(N\)-edge transversal.  It is automatically a forest:
it is a proper edge subset of the simple cycle \(P\), since \(N<W\).  It is
therefore an admissible exact lower core.  Combining Theorems 2.1 and 2.2
gives the exact GMM specialization.

### Corollary 3.3 (GMM-to-common-refinement gate)

The GMM tight cycle \(P\) yields a spanning common refinement with at most
\(d=o(W/H)\) components provided

1. its occurrence graph satisfies Theorem 3.1; and
2. the selected transversal core satisfies the capacitated-Hall cuts
   (2.3), equivalently the waste--slack cuts (2.4).

Neither assertion follows from the published tight-enumeration theorem.
In particular, (3.2) says that only \(d\) lower colours are flexible; it
does not bound collisions among the forced upper colours.

For the balanced common refinement, condition 2 must be replaced by the
integral residual system (2.3a)--(2.3d).  The rigid/flexible transversal
still supplies the forest core, and the same \(d\)-component conclusion
then follows.

The rigid-collision obstruction is realized at linear scale by the
published GJM four-central-level lexical forest.  That forest has exactly
one edge of every lower colour, so every lower occurrence is rigid.  The
audited first-global-minimum collision injection gives duplicate upper
excess

\[
 \delta_m\ge\binom{2m-1}{m-2}
 =\left(\frac14-o(1)\right)W.                                  \tag{3.7}
\]

Thus its forced collision mass is \(\rho=\delta_m\).  Corollary 3.2 implies
that every upper-injective exact lower core must replace at least
\((1/4-o(1))W\) of those published lexical edges.  The six-cycle joins in
the published construction leave this lower forest unchanged.  Hence that
specific central-level backbone cannot be upgraded by a Catalan-scale or
\(o(W)\) fusion.  This is a no-go for the published lexical backbone, not
for a new GMM tight enumeration or a new Middle-Levels cycle.

## 4. Middle Levels: exact closure of Hall and components

The published Middle-Levels construction begins with the union of the
\(0\)- and \(1\)-lexical perfect matchings between ranks \(m\) and \(m+1\).
This is a spanning cycle factor of the middle-levels graph.  Suppress every
rank-\((m+1)\) vertex and call the resulting Johnson \(2\)-factor
\(Q_{\rm lex}\).

### Theorem 4.0 (published lexical factor already has the target component scale)

The upper colours of \(Q_{\rm lex}\) exhaust \(\mathcal U\) exactly once,
and

\[
 c(Q_{\rm lex})
 \le \operatorname {Cat}_m
 =\frac{W}{2m+1}
 =o(W/H)
 \qquad(H=o(m)).                                             \tag{4.0}
\]

Consequently \(Q_{\rm lex}\) is a coverage common refinement if and only
if

\[
                         \ell(Q_{\rm lex})=\mathcal L,          \tag{4.0a}
\]

and it is balanced if and only if (4.0a) holds and

\[
                         \mu_{Q_{\rm lex}}(R)\le2
                         \quad(R\in\mathcal L).                  \tag{4.0b}
\]

#### Proof

Every upper vertex occurs in exactly one bipartite factor cycle and its two
neighbouring middle facets have union equal to that vertex.  Suppression
therefore gives every upper colour exactly once.

The published component description identifies the cycles of the
\(0/1\)-lexical factor with plane trees having \(m\) edges.  Rooting a plane
tree at a corner gives a rooted ordered tree, so the number of plane trees
is at most the number \(\operatorname {Cat}_m\) of rooted ordered trees.
Moreover

\[
 W=\binom{2m+1}{m}
   =\frac{2m+1}{m+1}\binom{2m}{m}
   =(2m+1)\operatorname {Cat}_m.
\]

This proves the component bound and its \(o(W/H)\) consequence.  The last
two equivalences are exactly the definitions of lower coverage and the
floor/ceiling cap, since the upper and owner ledgers are already exact.
\(\square\)

Thus the canonical factor does not need to be fused before addressing
depth one.  The sole missing published-factor statistic is (4.0a), or
(4.0a)--(4.0b) in the balanced version.  The cited component theorem does
not assert either lower-colour property.

Let \(Q\) be a Hamilton cycle in the middle-levels inclusion graph between
ranks \(m,m+1\), and suppress its upper vertices.  The result is a Hamilton
cycle on \(\mathcal X\) whose upper colours exhaust \(\mathcal U\) exactly
once.

### Theorem 4.1 (Middle-Levels common-refinement criterion)

The projected cycle \(Q\) is a spanning depth-one common refinement if and
only if

\[
                         \ell(Q)=\mathcal L.                    \tag{4.1}
\]

When (4.1) holds, choose one edge \(e_R\) of each lower colour and put
\(F=\{e_R:R\in\mathcal L\}\).  Then

1. \(F\) is an admissible exact lower core and a forest;
2. \(Q\setminus F\), consisting of exactly \(d\) edges, is an integral
   residual Hall completion of \(F\); and
3. the completed factor is the one-component cycle \(Q\).

#### Proof

The forward equivalence is the definition of lower hole-freeness, since
upper exactness and Hamiltonicity are already present.  Under (4.1), the
selected edges have distinct lower colours; their upper colours are
distinct because all upper colours on \(Q\) are distinct.  Degrees are at
most two.  Since \(F\) is a proper subset of a simple cycle, it is a forest.

Every deleted edge has an upper colour not used by \(F\), and upper
injectivity of \(Q\) shows that these are exactly the \(d\) unused upper
colours.  At each owner, the deleted incidences equal its degree deficit in
\(F\).  Thus \(Q\setminus F\) is precisely the integral flow of Theorem
2.1. \(\square\)

This theorem identifies the cleanest published-construction gate:

> For a GMM Middle-Levels Hamilton cycle, prove that every
> \((m-1)\)-set occurs as the intersection of two consecutive middle
> owners.

There is no further Hall, exactification, or component-fusion problem once
this statement is known.  The published Middle-Levels theorem does not
assert (4.1).

For the balanced version there is one additional, exact condition:

\[
 \ell(Q)=\mathcal L
 \quad\text{and}\quad
 \mu_Q(R)\le2\quad(R\in\mathcal L).                              \tag{4.2}
\]

Necessity is immediate.  Under (4.2), the \(d\) deleted edges in the proof
of Theorem 4.1 have pairwise distinct lower colours, namely the colours of
multiplicity two.  Hence they witness not only the incidence flow but the
balanced system (2.3a)--(2.3d).  Thus (4.2) is necessary and sufficient for
a projected Middle-Levels Hamilton cycle to be the balanced common
refinement.

## 5. Relation to the two-sided rainbow pseudoforest

Let \(P_0\) be a spanning Johnson linear forest whose lower and upper colours
are both injective.  Since \(|\mathcal L|=N\), write

\[
                         |E(P_0)|=N-k.                            \tag{5.1}
\]

Then \(P_0\) has exactly

\[
                         W-|E(P_0)|=d+k                           \tag{5.2}
\]

path or isolated components and misses \(k\) lower colours.  It also has
\(d+k\) unused upper colours and total middle degree deficit \(2(d+k)\).

Suppose one can add the \(k\) missing lower colours using distinct unused
upper colours and available middle degree slots, obtaining an admissible
core \(F\).  This is the exact four-resource system

\[
\begin{aligned}
 \sum_{U\supset R}z_{R,U}&=1 &&(R\text{ missing}),\\
 \sum_{R\subset U}z_{R,U}&\le1 &&(U\text{ unused}),\\
 \sum_{R\subset X\subset U}z_{R,U}&\le\delta_{P_0}(X)
     &&(X\in\mathcal X),
\end{aligned}                                                   \tag{5.3}
\]

with \(z_{R,U}\in\{0,1\}\).  It is not an ordinary network matrix: fixing
three facets of one \(U\) gives the determinant-two triangle

\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}.              \tag{5.4}
\]

If \(F\) then satisfies (2.3), Theorem 2.1 completes it.  Moreover every
cycle of \(F\) contains an edge added to the forest \(P_0\), so

\[
                         c_{\rm cyc}(F)\le k.                      \tag{5.5}
\]

Theorem 2.2 yields

\[
                         c(C)\le d+k.                              \tag{5.6}
\]

Consequently the following quantitative statement is sufficient:

\[
 \boxed{
 k=o(W/H),\quad (5.3)\text{ has an integral solution, and the resulting
 core satisfies }(2.3).}                                         \tag{5.7}
\]

For \(H=o(m)\), equations (0.2) and (5.6) then give
\(c(C)=o(W/H)\).

For floor/ceiling balance, the final \(d\) completion edges must in
addition have distinct lower colours.  Equivalently the resulting exact
core must satisfy (2.3a)--(2.3d), not merely (2.3).  The component estimate
(5.6) is unchanged.

The generic audited conflict-free matching construction proves only
\(k=o(W)\) after a fixed-girth diagonal.  It gives neither the rate in
(5.7), nor the determinant-two exactification, nor the waste--slack cuts.
Indeed that construction can be prescribed to output a
two-sided-rainbow near-forest which isolates one middle owner while using
all its upper cofacets.  For that near-forest, even the uncoloured
extension singleton cut reads \(2\le0\).  This does not assert the
existence of a poisoned exact lower core; it shows that the qualitative
pseudoforest conclusion alone cannot be fed into Theorem 2.1.

There is, however, an explicit quantitative input.  The audited PBBS
first-avoided-pair construction gives, whenever

\[
                         H=o(m/\log ^2m),                         \tag{5.8}
\]

a two-sided-rainbow Johnson linear forest with

\[
 |E(P_0)|=N-o(W/H),\qquad
 c(P_0)=O(W\log ^2m/m)=o(W/H).                                  \tag{5.9}
\]

After unused owners are added as isolated vertices, this is exactly the
normalization (5.1) with \(k=o(W/H)\).  Thus PBBS supplies the quantitative
part of (5.7), including every fixed Gaussian window.  What remains is
precisely:

1. solve the determinant-two exactification (5.3) for its actual leave;
2. make the resulting core satisfy (2.3), or (2.3a)--(2.3d) in the
   balanced version.

Potential reachability or the PBBS marginal multiplicity theorem does not
supply either integral statement.

There is a stronger quantitative near-core from the independent PBBS
pair-omission construction
`PBBS_PAIR_OMISSION_TWO_SIDED_Q1_COLOR_THEOREM_20260725.md`.  Its two signed
colour leave is

\[
 k=O\!\left({W\log m\over m}\right),
\tag{5.8}
\]

and its nontrivial path fragmentation is

\[
 O\!\left({W\log ^2m\over m}\right).
\tag{5.9}
\]

After adjoining unused owners as isolated vertices, (5.8)--(5.9) are still
\(o(W/H)\) whenever \(H=o(m/\log ^2m)\), in particular on the fixed
Gaussian window.  Thus that construction supplies the quantitative leave
and component rates absent from the fixed-girth diagonal.  It still does
not supply the integral exactification (5.3) or the final residual system
(2.3), respectively (2.3a)--(2.3d) in the balanced version.  The exact
common refinement remains the same Hall-aware absorption gate.

## 6. Sparse fusion of two published one-sided cycles is circular

The following elementary inequality records the limit of retention-based
fusion.

### Proposition 6.1 (two-backbone retention bound)

Let \(P,Q,C\) be spanning Johnson \(2\)-factors on the same \(W\) owners.
If

\[
 |E(C)\cap E(P)|\ge W-a,
 \qquad |E(C)\cap E(Q)|\ge W-b,
\]

then

\[
                         |E(P)\cap E(Q)|\ge W-a-b.                \tag{6.1}
\]

If \(F\subseteq P\) has \(N\) edges and

\[
 |E(C)\cap F|\ge N-a,
 \qquad |E(C)\cap E(Q)|\ge W-b,
\]

then

\[
                         |F\cap E(Q)|\ge N-a-b.                   \tag{6.2}
\]

#### Proof

Apply inclusion--exclusion inside the \(W\)-edge set \(E(C)\). \(\square\)

Thus a construction retaining all but \(o(W)\) edges of both a lower-perfect
GMM backbone and an upper-perfect Middle-Levels backbone requires those
backbones already to share \(W-o(W)\) edges.  This does not obstruct a new
factor using many new edges, but it shows that sparse splicing does not
create the missing common ledger.

## 7. Exact proved/open boundary

The following assertions are proved.

1. An admissible exact lower core plus (2.3) is equivalent to a spanning
   coverage common refinement.  For exact floor/ceiling balance, the
   necessary-and-sufficient residual condition is (2.3a)--(2.3d).
2. A forest core automatically gives at most \(d=O(W/m)=o(W/H)\)
   components for every \(H=o(m)\).
3. In a GMM tight Hamilton cycle, all but \(d\) lower colours are rigid;
   Theorem 3.1 is the exact upper-transversal criterion, and forced
   collision mass is an exact edit lower bound.
4. In a projected Middle-Levels Hamilton cycle, lower hole-freeness alone
   is necessary and sufficient for the coverage version; the balanced
   version is characterized by (4.2).  Hall and connectedness then come
   for free.
5. PBBS supplies the quantitative pseudoforest rate in (5.7) on
   \(H=o(m/\log ^2m)\), but neither its determinant-two exactification nor
   its residual Hall/balanced completion is proved.

Two clean sufficient construction lanes remain.  They are not asserted to
be equivalent to one another: the Middle-Levels lane asks for a Hamilton
refinement, while the forest-core lane allows a many-component intermediate
object whose component count is already small enough.

* **Middle-Levels lane:** construct an upper-perfect Middle-Levels
  Hamilton cycle satisfying (4.1), or (4.2) for floor/ceiling balance.
* **Core lane:** construct a forest exact lower core with pairwise distinct
  upper colours satisfying every cut (2.3); in the balanced version solve
  the stronger integral system (2.3a)--(2.3d).

For the particular GMM tight-enumeration lane, the minimum hypotheses are
the rigid/flexible transversal of Theorem 3.1 and then the residual cuts
(2.3), or the balanced system (2.3a)--(2.3d).  No separate
\(o(W/H)\)-component hypothesis remains.

This note does not prove any of these colour/Hall construction statements
and therefore does not claim the constant-one theorem.

## 8. Adversarial audit

* A spanning \(2\)-factor cannot have an injective lower map on odd ground;
  the exact lower condition is coverage with forced excess \(d\).
  Coverage does not itself impose the floor/ceiling cap two; the balanced
  version is strictly stronger.
* The component estimate uses \(H=o(m)\).  It would not imply
  \(o(W/H)\) at linear depth.
* A proper edge subset of one Hamilton cycle is a forest, but an arbitrary
  \(N\)-edge core need not be; this is why \(c_{\rm cyc}(F)\) appears in
  (2.7).
* The occurrence matching in Theorem 3.1 gives upper injectivity only.  It
  does not imply the residual Hall cuts (2.3), much less the balanced
  system (2.3a)--(2.3d).
* Middle-Levels lower coverage makes its own deleted edges a completion;
  this argument cannot be transferred to a GMM tight cycle whose upper
  colours may repeat.
* The pseudoforest theorem has no audited \(o(W/H)\) leave rate.  The
  diagonal \(o(W)\) must not be strengthened silently.
* Proposition 6.1 concerns sparse retention only and is not a no-go for a
  genuinely new common-refinement construction.
