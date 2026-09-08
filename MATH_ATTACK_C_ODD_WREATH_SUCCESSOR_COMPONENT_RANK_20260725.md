# Ordered-state splicing of an exact odd-graph wreath factor

Date: 2026-07-25

## 0. Scope and outcome

Let

\[
n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
B=\frac{W}{n}=\operatorname {Cat}_m,
\]

and let \(\mathcal F\) be any exact \(C_n\)-factor of the odd graph
\(KG(n,m)\).  Every member of \(\mathcal F\) is a wreath.  Choosing an
orientation of each wreath turns its \(n\) middle owners into a directed
circuit in the ordered-\((m-1)\)-tuple overlap graph.

This note proves four exact facts.

1. For fixed wreath orientations, the minimum number of directed circuits
   obtainable by legal successor switches is exactly the number of weak
   components of the fixed ordered-state multigraph.  It is attained using
   only component-merging switches.
2. If \(d(v)\) is the multiplicity of an ordered state, then the exact
   independent fusion rank is

   \[
   B-c=\sum_v(d(v)-1)-\beta,
   \]

   where \(c\) is the component count and \(\beta\) is the cycle rank of
   the circuit--state incidence graph.  Thus a state of multiplicity \(d\)
   has capacity \(d-1\), not \(\binom d2\).  No singleton-state assumption
   is made.
3. Reversal freedom is a signed incidence problem.  An orientation choice
   splits every unoriented order class into its two signs.  This gives an
   exact formula for the collision budget, including order fragmentation
   and orientation frustration.
4. The topological minimum can always be attained while preserving cyclic
   recurrence gap at least \(m+1\).  For a larger target gap \(m+H\), an
   exact triangular two-collar test is necessary and sufficient at every
   adaptive merge.  Hence the remaining mesoscopic issue is a collar-safe
   spanning-rank theorem, not ordinary circuit splicing.

The result is a theorem about the restricted singleton/ordered-word route.
It does not assert that singleton states are without loss of generality for
contiguous OR words, and it does not prove a central near-Ucycle.

Throughout the orientation discussion we assume \(m\ge3\).  The component
theorem itself holds for \(m\ge2\).

## 1. The fixed ordered-state multigraph

Choose one of the two orientations of each wreath \(C\in\mathcal F\), and
write its cyclic coordinate order as

\[
q_C=(q_{C,0},q_{C,1},\ldots,q_{C,n-1}).
\]

Here \(q_C\) is the wreath's **tight** cyclic coordinate order, in which
middle owners are consecutive \(m\)-intervals.  If one starts from the
odd-cycle omitted-label word, this is its step-two reordering.

Its middle owners are the supports of the cyclic ordered words

\[
e_{C,i}=(q_{C,i},q_{C,i+1},\ldots,q_{C,i+m-1}),
\qquad i\in\mathbb Z_n.
\tag{1.1}
\]

The exact factor hypothesis says that the \(W=nB\) supports in (1.1) are
pairwise distinct and exhaust \(\binom{[n]}m\).

Let \(\Gamma=\Gamma(\mathcal F,\varepsilon)\) be the directed graph whose
arcs are (1.1), with

\[
e_{C,i}:\quad
(q_{C,i},\ldots,q_{C,i+m-2})\longrightarrow
(q_{C,i+1},\ldots,q_{C,i+m-1}).
\tag{1.2}
\]

Its vertices are the used ordered \((m-1)\)-tuples.  Here
\(\varepsilon\in\{+,-\}^{\mathcal F}\) records the chosen wreath
orientations.  Every wreath is a directed \(n\)-circuit in \(\Gamma\).
Consequently

\[
d^+(v)=d^-(v)=:d(v)
\tag{1.3}
\]

at every used state \(v\).

No one wreath visits a state twice.  Indeed, equality of two ordered states
on the same wreath already equates their first coordinates; since \(q_C\)
is a permutation, their indices are equal modulo \(n\).

More strongly, no one wreath visits the same *unordered* state support
twice.  The position sets of two length-\((m-1)\) cyclic intervals in
\(\mathbb Z_n\) are equal only when their starting positions are equal:
a nonempty proper cyclic interval has a unique entry boundary.  Since
\(q_C\) is bijective, equality of the coordinate supports is equality of
those position intervals.

A **successor system** is a bijection

\[
\theta_v:E^-(v)\longrightarrow E^+(v)
\tag{1.4}
\]

for every state \(v\).  Its orbits on the arc set are directed circuits.
A **legal successor switch** transposes the two values of \(\theta_v\) on
two incoming arcs at the same state.  This is exactly the full-word overlap
condition: the last \(m-1\) letters of one word equal the first \(m-1\)
letters of its successor.

### Lemma 1.1 (successor switches generate every local system)

Starting from any successor system, legal successor switches generate every
other successor system on the fixed directed arc set.

#### Proof

Fix \(v\), and let \(\theta_v,\theta'_v:E^-(v)\to E^+(v)\) be the old and
desired bijections.  Then

\[
\theta'_v\theta_v^{-1}
\]

is a permutation of \(E^+(v)\).  Every finite permutation is a product of
transpositions, and transposing two values of \(\theta_v\) is exactly one
legal successor switch at \(v\).  Perform such factorizations independently
at all states.  \(\square\)

## 2. Exact minimum component theorem

### Theorem 2.1 (weak components are the exact optimum)

Fix the orientation choice \(\varepsilon\), and let
\(c(\Gamma)\) be the number of weak components of \(\Gamma\) containing
arcs.  Among all successor systems on the fixed arcs (1.1), the minimum
number of directed circuits is exactly

\[
\boxed{c(\Gamma).}
\tag{2.1}
\]

Starting from the \(B\) wreath circuits, this minimum is attained by
exactly

\[
\boxed{B-c(\Gamma)}
\tag{2.2}
\]

legal switches, every one of which joins two currently distinct circuits.
No sequence can use fewer switches to attain (2.1).

#### Proof

A successor circuit cannot leave a weak component of the fixed graph, so
at least one circuit is required in every weak component.

Conversely, consider any current circuit decomposition of the arcs.  If a
weak component contains at least two current circuits, then two of those
circuits share a state.  Otherwise their state sets would be pairwise
disjoint, separating the weak component.  At a shared state, transpose the
successors of one incoming arc from each circuit.  The standard cut-and-join
identity for two permutation cycles shows that the two circuits become one.
Repeat.  This stops with one directed circuit in every weak component and
uses exactly one switch for each unit decrease, namely \(B-c(\Gamma)\).

A transposition in a successor permutation changes its orbit count by
exactly one in absolute value.  Reducing \(B\) orbits to \(c(\Gamma)\)
therefore needs at least \(B-c(\Gamma)\) switches.  This proves all claims.
\(\square\)

The theorem permits arbitrary state multiplicities.  In particular, a
single state shared by \(r\) wreaths can join those \(r\) wreaths using
\(r-1\) switches; replacing this state by \(\binom r2\) independent
pairwise resources is an incorrect collision ledger.

## 3. The exact incidence-rank ledger

Form the bipartite incidence graph \(\mathcal I_\varepsilon\).  Its left
vertices are the \(B\) original wreath circuits, its right vertices are the
used directed ordered states, and \(C\) is joined to \(v\) when \(C\)
visits \(v\).  The observation following (1.3) makes this a simple
bipartite graph.  It has

\[
|E(\mathcal I_\varepsilon)|=nB=W.
\tag{3.1}
\]

Its connected components are exactly the weak components of \(\Gamma\).
Put

\[
V_\varepsilon=|V_R(\mathcal I_\varepsilon)|,
\qquad
\Xi_\varepsilon=W-V_\varepsilon
                 =\sum_v(d(v)-1),
\tag{3.2}
\]

and let \(\beta_\varepsilon\) be the ordinary cycle rank of the incidence
graph.  Thus

\[
\beta_\varepsilon
=W-(B+V_\varepsilon)+c(\Gamma).
\tag{3.3}
\]

### Theorem 3.1 (collision excess minus incidence redundancy)

For every exact wreath factor and every orientation choice,

\[
\boxed{
B-c(\Gamma)=\Xi_\varepsilon-\beta_\varepsilon.
}
\tag{3.4}
\]

Consequently, a necessary and sufficient condition for legal successor
switches to leave \(o(B)\) circuits is

\[
\Xi_\varepsilon-\beta_\varepsilon=B-o(B).
\tag{3.5}
\]

#### Proof

Equation (3.4) is a rearrangement of (3.3) and (3.2).  Theorem 2.1 then
turns (3.4) into (3.5).  \(\square\)

Two useful sharp consequences are as follows.  If

\[
R=|\{v:d(v)\ge2\}|,
\qquad D=\max_v d(v),
\]

then

\[
B-c(\Gamma)\le\Xi_\varepsilon\le(D-1)R.
\tag{3.6}
\]

Thus \(R\ge(B-c)/(D-1)\), not necessarily \(R\ge B-c\).  On the other
hand, the raw number of pairwise switch incidences

\[
P=\sum_v\binom{d(v)}2
\]

satisfies only

\[
\Xi_\varepsilon\le P\le\frac D2\Xi_\varepsilon.
\tag{3.7}
\]

Hence a lower bound on \(P\) can overcount independent fusion rank by a
factor of order \(D\), and even \(\Xi\) still overcounts it by the exact
incidence-cycle term \(\beta\).  Both inequalities in (3.6)--(3.7) are
attained by elementary stars or one-state hyperedges, so their dependence
on multiplicity cannot be improved without additional wreath structure.

## 4. Unordered shadows and the local matching cap

For an unordered \((m-1)\)-set \(S\), let \(\mu(S)\) be the number of
state occurrences whose support is \(S\).  Such an occurrence lies between
the two consecutive middle owners

\[
S\cup\{x\},\qquad S\cup\{y\},qquad x\ne y,
\tag{4.1}
\]

on its wreath.

### Lemma 4.1 (complement matching)

For fixed \(S\), the pairs \(\{x,y\}\) from (4.1) form a matching on
\([n]\setminus S\).  In particular,

\[
\boxed{
\mu(S)\le\left\lfloor\frac{m+2}{2}\right\rfloor,
\qquad
d(v)\le\left\lfloor\frac{m+2}{2}\right\rfloor.
}
\tag{4.2}
\]

Equivalently, every directed ordered-state multiplicity \(r=d(v)\)
satisfies the exact incidence constraint

\[
\boxed{2r\le m+2.}
\tag{4.2a}
\]

#### Proof

If two occurrences used the same endpoint \(x\), then the middle owner
\(S\cup\{x\}\) would occur twice in the exact factor.  All endpoints are
therefore distinct.  Since \(|[n]\setminus S|=m+2\), (4.2) follows.
\(\square\)

Let

\[
N=\binom{n}{m-1}=\frac{m}{m+2}W
\tag{4.3}
\]

be the number of unordered lower depth-one shadows, and let \(M\) of them
be missing from the wreath factor's tight-window shadow multiset.  If
\(o_\varepsilon(S)\) denotes the number of distinct directed orderings used
over \(S\), then

\[
\Xi_\varepsilon
=\sum_S\bigl(\mu(S)-o_\varepsilon(S)\bigr)
\le W-(N-M).
\]

Therefore

\[
\boxed{
\Xi_\varepsilon
\le \frac{2W}{m+2}+M
=\left(4-\frac6{m+2}\right)B+M.
}
\tag{4.4}
\]

Equality holds precisely when all occurrences over every covered \(S\)
use one directed ordering.  In particular, if every lower depth-one shadow
is covered and \(c=o(B)\), then at least

\[
\frac{B-o(B)}{(4-6/(m+2))B}
=\frac14-o(1)
\tag{4.5}
\]

of the entire forced unordered collision excess must survive both order
fragmentation and incidence-cycle redundancy.  This is only a necessary
budget condition, not a connectivity theorem.

Combining (3.6) and (4.2), an \(o(B)\)-component construction needs at least

\[
R\ge
\frac{B-o(B)}{\lfloor(m+2)/2\rfloor-1}
=\Omega(B/m)
\tag{4.6}
\]

distinct repeated directed states.  The weaker scale \(B/m\), rather than
\(B\), is the correct universal statement when high state multiplicity is
allowed.

## 5. Reversal is a signed global constraint

For each covered \(S\), identify an ordered tuple with its reversal.  Let
\(\mathcal R(S)\) be the set of reversal classes which occur over \(S\),
and write

\[
a(S)=|\mathcal R(S)|,
\qquad
\Phi=\sum_{S:\mu(S)>0}(a(S)-1).
\tag{5.1}
\]

Choose one representative in each reversal class \(r\).  An incidence of
a wreath \(C\) with \(r\) has a sign \(\sigma(C,r)\in\{+1,-1\}\), according
as the order induced by a reference orientation of \(C\) is the chosen
representative or its reversal.  Reorienting \(C\) multiplies all signs on
that wreath by one common \(\varepsilon_C\in\{+1,-1\}\).

Let \(b_\varepsilon\) be the number of reversal classes \(r\) for which
the values \(\varepsilon_C\sigma(C,r)\), over all incident wreaths, contain
both signs.  Such a class splits into two directed states; a monochromatic
class gives one.

### Proposition 5.1 (exact signed-orientation ledger)

For every orientation choice \(\varepsilon\),

\[
V_\varepsilon=N-M+\Phi+b_\varepsilon
\tag{5.2}
\]

and hence

\[
\boxed{
\Xi_\varepsilon
=\frac{2W}{m+2}+M-\Phi-b_\varepsilon.
}
\tag{5.3}
\]

Moreover, some orientation has \(b_\varepsilon=0\) if and only if the
signed bipartite incidence graph on wreaths and reversal classes is
balanced: the product of its incidence signs around every cycle is \(+1\).

#### Proof

There are \(N-M\) covered supports.  Their first reversal classes contribute
\(N-M\) vertices, their additional reversal classes contribute \(\Phi\),
and precisely the bichromatic classes contribute one further directed-state
vertex.  This proves (5.2), and (5.3) follows from \(\Xi=W-V\) and (4.3).

If all classes are to be monochromatic, there must be signs \(\delta_r\)
such that

\[
\varepsilon_C\sigma(C,r)=\delta_r
\tag{5.4}
\]

on every incidence.  Multiplying (5.4) around a bipartite cycle gives the
stated necessary cycle condition.  Conversely, under that condition fix
one vertex sign in each connected component and propagate (5.4) along a
spanning tree.  The cycle condition makes the propagated signs independent
of path.  Thus (5.4) has a solution.  \(\square\)

Equations (3.4) and (5.3) give the complete collision ledger

\[
\boxed{
B-c(\Gamma)
=\frac{2W}{m+2}+M-\Phi-b_\varepsilon-\beta_\varepsilon.
}
\tag{5.5}
\]

The optimum permitted by independently orienting whole wreaths is therefore

\[
\boxed{
c_{\min}(\mathcal F)
=\min_{\varepsilon\in\{+,-\}^{\mathcal F}}
 c(\Gamma(\mathcal F,\varepsilon)).
}
\tag{5.6}
\]

Equivalently, by (3.4),

\[
\boxed{
c_{\min}(\mathcal F)
=B-\max_{\varepsilon\in\{+,-\}^{\mathcal F}}
 \bigl(\Xi_\varepsilon-\beta_\varepsilon\bigr).
}
\tag{5.7}
\]

Indeed, cyclic rotation of a wreath changes neither its directed arc set nor
its state incidences, while reversal is exactly the sign choice
\(\varepsilon_C\).  These are all choices of orientation of a fixed wreath.
Theorem 2.1 gives the optimum after each such choice, and minimizing over
the choices proves (5.6)--(5.7).

This is not an independent-orientation choice at every port: one
\(\varepsilon_C\) controls all \(n\) incidences of \(C\).  The signed-cycle
condition is the exact obstruction to treating those choices locally.

## 6. Exact recurrence-gap seam test

For a cyclic spelling \(z\), say that it has gap \(L\) if every cyclic
block of \(L\) letters has distinct entries.  Each original wreath spelling
is a permutation of \([n]\), hence has gap \(L\) for every \(L\le n\).

Suppose two current directed circuits share an ordered state

\[
s=(s_1,\ldots,s_{m-1}).
\]

At the chosen occurrence on circuit \(A\), write the local spelling as

\[
\cdots,p^A_2,p^A_1,s_1,\ldots,s_{m-1},q^A_1,q^A_2,\cdots,
\tag{6.1}
\]

and define \(p_i^B,q_j^B\) similarly.  Here \(p_1\) and \(q_1\) are the
letters immediately before and after the common state block.

### Theorem 6.1 (adaptive triangular collar criterion)

Let \(1\le H\le m+1\).  Assume the two input circuits have gap at least
\(m+H\).  Swap their successors at the displayed occurrences of \(s\).
The merged circuit has gap at least \(m+H\) if and only if

\[
\boxed{
\begin{aligned}
p_i^A&\ne q_j^B,\\
p_i^B&\ne q_j^A
\end{aligned}
\qquad(i,j\ge1,\ i+j\le H+1).
}
\tag{6.2}
\]

The collars in (6.2) are the actual collars at the time of the switch;
after earlier splices they need not be collars from one original wreath.

#### Proof

The switch creates the two cross seams \(A^-B^+\) and \(B^-A^+\).  The two
new seams are separated in either direction by the length of one input
circuit.  The assumed gap \(m+H\) itself forces each cyclic input word to
have length at least \(m+H\).  A bad block of length \(m+H\) consequently
crosses at most one new seam.

All repetitions wholly on one retained side are excluded by the hypotheses.
The common state itself is safe with each retained side.  Thus at seam
\(A^-B^+\) the only possible new repetition is
\(p_i^A=q_j^B\).  In (6.1), the forward distance from \(p_i^A\) to
\(q_j^B\) is

\[
m-2+i+j.
\]

It is smaller than \(m+H\) exactly when \(i+j\le H+1\).  This gives the
first line of (6.2); the other seam gives the second.  Necessity and
sufficiency follow.  \(\square\)

### Corollary 6.2 (the exact topological optimum is depth-one gap-safe)

For \(H=1\), every switch between two distinct current components at a
shared ordered state satisfies (6.2).  Hence the minimum
\(c(\Gamma)\) from Theorem 2.1 can always be attained with final recurrence
gap at least \(m+1\).

#### Proof

For \(H=1\), (6.2) asks only

\[
p_1^A\ne q_1^B,\qquad p_1^B\ne q_1^A.
\]

If, for example, \(p_1^A=q_1^B=x\), then the incoming edge on \(A\) and
the outgoing edge on \(B\) both have support \(S\cup\{x\}\), where
\(S=\{s_1,\ldots,s_{m-1}\}\).  The fixed edge set contains every middle
owner exactly once, so those two edges are identical and cannot lie in
distinct current components.  Thus both inequalities hold.  Apply the
component-merging sequence from Theorem 2.1 and use Theorem 6.1
inductively.  \(\square\)

Successor switches never change the ordered \(m\)-words (1.1).  Therefore
the multiset of every lower word of length at most \(m\), obtained as the
corresponding suffix of an arc, is invariant under all switches.  In
particular, all lower shallow-shadow colors supplied by the chosen ordered
wreath factor are retained exactly.  A gap \(m+H\) additionally guarantees
that every upper word of length \(m+h\), \(1\le h\le H\), has the correct
rank \(m+h\).  It does not by itself prove global coverage or injectivity of
those upper colors.  Lower invariance is likewise not a coverage theorem:
every lower hole in the initial ordered factor remains a hole after every
successor recombination.

### Corollary 6.3 (precise mesoscopic conditional theorem)

Fix \(H\le m+1\) and an orientation choice \(\varepsilon\).  Suppose that
inside every weak component of \(\Gamma(\mathcal F,\varepsilon)\) one can
order a sequence of joins between distinct current circuits such that every
join passes the actual-collar test (6.2).  Then the exact factor can be
recombined into \(c(\Gamma)\) Euler circuits with gap at least \(m+H\),
while retaining every lower shadow multiset through depth \(m-1\).

In particular, if

\[
c(\Gamma)=o(B)
\tag{6.3}
\]

and such a collar-safe joining sequence exists for
\(H=H(m)\), the restricted construction gives \(o(\operatorname{Cat}_m)\)
singleton Eulerian components with correct recurrence ranks through upper
depth \(H\).

#### Proof

There are \(B-c(\Gamma)\) joins in the sequence.  Theorem 6.1 preserves the
gap inductively, Theorem 2.1 gives the final component count, and the fixed
arc observation gives lower-shadow invariance.  \(\square\)

## 7. Exact surviving gate and obstruction criteria

For this restricted route, ordinary de Bruijn circuit splicing is now
fully resolved.  A proof of \(o(B)\) components must establish, for some
single orientation choice of the whole wreaths,

\[
\Xi_\varepsilon-\beta_\varepsilon=B-o(B),
\tag{7.1}
\]

and then find \(B-o(B)\) adaptive joins satisfying (6.2) at the desired
mesoscopic \(H\).  Pairwise overlap counts, unordered shadow collisions,
or independently chosen port orientations do not establish (7.1).

The following are rigorous obstruction certificates.

1. **Rank obstruction.**  If for every \(\varepsilon\),

   \[
   \Xi_\varepsilon-\beta_\varepsilon\le(1-\delta)B,
   \]

   then every successor recombination has at least \(\delta B\) Euler
   circuits.
2. **Multiplicity-corrected state obstruction.**  For a fixed orientation,
   if the number \(R_\varepsilon\) of repeated directed states satisfies

   \[
   R_\varepsilon=o(B/m),
   \]

   then (4.2) and (3.6) give \(B-c=o(B)\), so
   \(c=(1-o(1))B\).  If this bound holds for every \(\varepsilon\), it
   obstructs the orientation-optimized route as well.
3. **Order-fragmentation obstruction.**  Formula (5.5) exactly subtracts
   every extra reversal class, every orientation-frustrated split, and
   every redundant incidence cycle from the unordered collision budget.
4. **Mesoscopic collar obstruction.**  Even when (7.1) holds, failure of
   (6.2) can prevent a gap-safe spanning rank.  For \(H=1\) this obstruction
   vanishes identically; for growing \(H\) it is the sole additional
   recurrence obstruction within the fixed ordered-edge architecture.

No claim is made that an arbitrary exact odd-graph factor satisfies (7.1),
nor that the MSW factor has a collar-safe spanning rank for
\(H\asymp\sqrt m\).  Those are the two exact statements still needed by
the restricted central near-Ucycle/cycle-splicing lane.

## 8. Audit against the earlier local-Hall and near-Ucycle reductions

The full-word local Hall equations are automatic here: (1.3) gives equal
head and tail multiplicity at every ordered state.  What Hall does not
decide is the orbit count of the chosen local bijections.  Theorem 2.1 and
(3.4) are the exact missing subtour calculation.

The closed singleton-state obstruction from the deletion-word audit is the
special case \(d(v)=1\) for every used state.  Then
\(\Xi=\beta=0\), so (3.4) gives \(c=B\): no successor switch exists.  This
special case is not a normal form.  At the opposite extreme, one state of
multiplicity \(r\) supplies \(r-1\) independent joins, subject to the exact
cap \(2r\le m+2\).  Thus neither counting repeated states without
multiplicity nor counting all \(\binom r2\) pairs gives the correct rank.

Finally, the exact odd-graph factor supplies the \(W\) middle owners, but
the elementary ownership count alone gives no lower bound on ordered-state
fusion rank.  Equality of unordered depth-one shadows does not by itself
align their linear orders up to a globally consistent choice of wreath
reversals.  Equations (5.3)--(5.7) quantify that loss exactly.  This respects
the prior audit warning: a singleton near-Ucycle is a restricted sufficient
architecture, not a necessary form of a general contiguous-OR word.
