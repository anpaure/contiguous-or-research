# The partial-annulus SCD scaffold and its sharp top-tag rotor cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and fix

\[
 0<a<b,\qquad q_0=\lceil a\sqrt m\rceil,
 \qquad H=\lfloor b\sqrt m\rfloor.
\]

The corrected annulus problem only needs \(N_{q_0}+o(W)\) paid middle
occurrences.  This slack interacts particularly cleanly with one symmetric
chain decomposition.

For an arbitrary full SCD \(\mathcal D\) of \(B_{2m}\), retain precisely
the central chains of full radius at least \(q_0\).  There are exactly
\(N_{q_0}\) of them.  Their middle owners are distinct.  More importantly,
at every \(q_0\le q\le H\), the subfamily of retained chains having radius
at least \(q\) contains every rank-
\((m-q)\) mask and every rank-\((m+q)\) mask exactly once.

Consequently the owner and all-depth target equations are already solved
integrally before any rotor edges are selected.  Shorter retained chains
may be extended arbitrarily to radius \(H\); their extra flags can only add
duplicate witnesses.  There is substantially more central freedom.  If
\(D=C_{-q_0}\) and \(E=C_{q_0}\), the middle owner may be reassigned to
any \(m\)-set \(X\) with \(D\subset X\subset E\); then the \(q_0\) labels
in \(X\setminus D\) and the \(q_0\) labels in \(E\setminus X\) may be
ordered independently.  All controlled flags begin at radius \(q_0\), so
these \((2q_0)!\) corner/port choices do not alter one required target.
The choices across chains must retain distinct middle owners.  The
original SCD corners show that this owner transversal is nonempty.  The
sole remaining joint gate is chronological:

\[
 \boxed{\text{put these }N_{q_0}\text{ decorated states into a
 radius-}H\text{ rotor path forest with }o(W/H)\text{ paths}.}
\]

Such a forest gives an exact annulus compiler of length \(W+o(W)\).
Equivalently, if all but the remainder

\[
 \rho=N_{q_0}-2m\left\lfloor{N_{q_0}\over2m}\right\rfloor<2m
\]

can be put into radius-\(H\), length-\(2m\) rotor cycles, then the omitted
providers create at most

\[
 2\rho(H-q_0+1)=o(W)
\]

signed annular holes.  This is the exact cycle-form sufficient target in
the corrected ledger; proving that the cycles exist remains the
chronological gate.  The \(W-N_{q_0}\) other middle owners are appended as
singletons.

Literal cycle closure is stronger than the compiler needs.  If the
chronological cover has \(p\) paths, split every path after each block of
\(2m\) states.  The number \(B\) of resulting path packets obeys

\[
 B\le {N_{q_0}\over2m}+p,
\]

and hard-starting them gives the sharper no-hole ledger

\[
 L\le W+2HB
 \le W+{H\over m}N_{q_0}+2Hp.
\]

Thus \(p=o(W/H)\) already gives length-at-most-\(2m\) literal path
packets at total length \(W+o(W)\).  The cycle statement above remains an
exact sufficient form, but constructing antipodally closed cycles is an
additional monodromy demand.

There is also a sharp inherited obstruction.  After fixing one annular
port assignment \(\sigma\), let \(\lambda_H(\mathcal D,\sigma)\)
be the maximum number of arcs in a vertex-disjoint directed linear forest
of genuine rotor arcs induced by the chains of full radius at least \(H\),
that is, the tag-\(H\) class after clipping to the radius-\(H\) band.
Every rotor path
cover of the retained tag-\(\ge q_0\) states with \(p\) paths obeys

\[
 \boxed{
 p\ge
 \bigl(2N_H-N_{q_0}-\lambda_H(\mathcal D,\sigma)\bigr)_+.}
\]

Since

\[
 {N_{q_0}\over W}=e^{-a^2+o(1)},\qquad
 {N_H\over W}=e^{-b^2+o(1)},
\]

the narrow-annulus threshold is

\[
 \boxed{b^2-a^2<\log2.}
\]

Below this threshold, a successful SCD must contain at least

\[
 \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W
\]

top-tag rotor edges in one vertex-disjoint linear forest.  Therefore an
SCD is excluded in this range only if even the maximum over all its
annular port assignments is \(o(W)\).  No such conclusion is
currently available for clipped BTK: its
tag-\(H\) graph has explicit rotor edges, contrary to an earlier claim.
The result does not construct the required noncanonical SCD; it
reduces the corrected partial annulus to that single path-forest gate and
identifies its exact hard cut.

There is a stronger cut which does not require a narrow annulus.  If
\(r_{\rm full}\) is the number of genuine full-radius-\(H\) rotor arcs in
the path cover, then

\[
 \boxed{p+r_{\rm full}\ge N_H.}
\]

Thus every successful fixed annulus requires
\((e^{-b^2}-o(1))W\) genuine full rotors.  The narrow cut above remains
useful because it localizes a positive fraction of them specifically
between two clipped top-tag states.

## 1. SCD notation and radius extensions

A symmetric chain of radius (or tag) \(d\) has the form

\[
 C_{-d}\subset C_{-d+1}\subset\cdots\subset C_0
 \subset\cdots\subset C_d,
 \qquad |C_i|=m+i.
\]

Let \(\mathcal D_d\) be the full-radius-\(d\) chains of a full SCD
\(\mathcal D\).  Write

\[
 \mathcal D_{\ge q}=\bigcup_{d\ge q}\mathcal D_d.
\]

Every chain in \(\mathcal D_{\ge q}\) contains one rank-
\((m-q)\) member and one rank-\((m+q)\) member.  Conversely every set in
either of these ranks lies on a unique chain, necessarily of tag at least
\(q\).  Therefore

\[
 |\mathcal D_{\ge q}|=N_q.                                      \tag{1.1}
\]

Fix \(H<m\).  A full-radius-\(d\) chain with \(d<H\) can be extended to a complete
radius-\(H\) useful state by choosing an ordered \((H-d)\)-tuple in
\(C_{-d}\) below the chain and an ordered \((H-d)\)-tuple outside
\(C_d\) above it.  Thus the number of extensions is

\[
 ((m-d)_{H-d})^2>0.                                             \tag{1.2}
\]

For a chain of full radius \(d\ge H\), its restriction to the radius-
\(H\) band is the unique complete state.  In every extension or
restriction, the displayed signed flag agrees with the original SCD chain
through every depth \(q\le\min(d,H)\).

That chain-faithful state is not the only state relevant to the corrected
annulus.  Put

\[
 D(C)=C_{-q_0},\qquad E(C)=C_{q_0}.                            \tag{1.3}
\]

Choose any middle corner

\[
 D(C)\subset X(C)\subset E(C),\qquad |X(C)|=m.                 \tag{1.4}
\]

Order the \(q_0\) labels of \(X(C)\setminus D(C)\) arbitrarily in state
positions \(H-q_0+1,\ldots,H\), and order the \(q_0\) labels of
\(E(C)\setminus X(C)\) arbitrarily in positions
\(H+1,\ldots,H+q_0\).  Every lower and upper flag at a controlled depth
\(q\ge q_0\) remains unchanged.  Conversely, the depth-\(q_0\) endpoints
of any compatible state force (1.4), and its two ordered central blocks
are exactly these two orders.  This is the exact annular-corner normal
form.

Thus each retained chain has exactly

\[
 (2q_0)!\bigl((m-d)_{H-d}\bigr)^2                              \tag{1.5}
\]

annular port states when \(q_0\le d<H\), and \((2q_0)!\) when
\(d\ge H\).  Indeed,
\(\binom{2q_0}{q_0}(q_0!)^2=(2q_0)!\).

Across different chains the corners \(X(C)\) must be distinct.  Let
\(\Sigma_{q_0,H}(\mathcal D)\) be the set of simultaneous owner-simple
choices of one such annular port state for every chain in
\(\mathcal D_{\ge q_0}\).  This set is nonempty: take the original middle
member \(C_0\) of every SCD chain and its original central orders.
Equivalently, before chronology is imposed, corner choice is the
bipartite matching problem

\[
 C\sim X\quad\Longleftrightarrow\quad
 D(C)\subset X\subset E(C),\quad |X|=m,                        \tag{1.6}
\]

whose Hall inequalities hold because the distinct original corners
\(C_0\) give an explicit saturating matching.

Only agreement with the SCD at controlled depths \(q\ge q_0\) is used
below.  No assertion is made that the arbitrary part of a short-chain
extension or the reassigned central corner is owned by the SCD at omitted
depths \(q<q_0\).

## 2. Exact owner and target equations

Retain the state set

\[
 \Omega=\mathcal D_{\ge q_0}                                   \tag{2.1}
\]

and choose any annular port assignment
\(\sigma\in\Sigma_{q_0,H}(\mathcal D)\).  Denote its
middle owner by \(X(\omega)\), and its lower and upper depth-\(q\) flags by
\(L_q(\omega)\) and \(U_q(\omega)\).

### Theorem 2.1 (exact partial-annulus SCD scaffold)

The following equations hold integrally.

1.  Owner simplicity:

    \[
    \sum_{\omega\in\Omega}\mathbf 1_{\{X(\omega)=X\}}\le1
    \quad\left(X\in\binom{[2m]}m\right),                       \tag{2.2}
    \]

    and the total selected owner mass is

    \[
    |\Omega|=N_{q_0}.                                           \tag{2.3}
    \]

2.  For every \(q_0\le q\le H\), the maps

    \[
    \omega\mapsto L_q(\omega),\qquad
    \omega\mapsto U_q(\omega)                                 \tag{2.4}
    \]

    restricted to \(\mathcal D_{\ge q}\) are bijections onto

    \[
    \binom{[2m]}{m-q},\qquad
    \binom{[2m]}{m+q},                                         \tag{2.5}
    \]

    respectively.  Equivalently, for every target on either signed rank,

    \[
    \sum_{\omega\in\mathcal D_{\ge q}}
      \mathbf 1_{\{L_q(\omega)=T\}}=1,
    \qquad
    \sum_{\omega\in\mathcal D_{\ge q}}
      \mathbf 1_{\{U_q(\omega)=T'\}}=1.                       \tag{2.6}
    \]

3.  Hence the full selected family \(\Omega\) covers every signed target
    at every depth \(q_0\le q\le H\).  States of tag below \(q\) may
    create overload, but never a hole.

#### Proof

Owner simplicity is part of the definition of
\(\Sigma_{q_0,H}(\mathcal D)\), which proves (2.2); the original SCD
corners certify that this requirement is feasible.
Equation (2.3) is (1.1) at \(q=q_0\).

Fix \(q\ge q_0\).  The SCD partitions rank \(m-q\).  A chain meets that
rank if and only if its tag is at least \(q\), and then it meets it once.
The chosen annular port state agrees with the SCD at depth \(q\) on every
such chain.  This proves the lower bijection.  The same argument at rank
\(m+q\) proves the upper bijection.  Since
\(\mathcal D_{\ge q}\subseteq\Omega\), the final assertion follows.
\(\square\)

This is the feature unavailable to an arbitrary rank-\(q_0\) packet
matching.  In a common SCD the designated provider sets are nested by tag,
and all deeper target support is exact without a discrepancy estimate.

## 3. From a rotor path cover to a literal word

A genuine radius-\(H\) rotor arc is the one-letter common-arrival move
between complete useful states.  A directed rotor path with \(s\) states
has a literal hard-started realization of length exactly

\[
 s+2H.                                                          \tag{3.1}
\]

The initial \(2H\)-letter collar realizes the first state, and every rotor
successor costs one new nonempty letter.  Every displayed lower and upper
flag of every state remains a literal contiguous OR.

### Theorem 3.1 (partial-SCD path-forest compiler)

Suppose the decorated digraph on \(\Omega\) has a vertex-disjoint directed
rotor path cover with \(p\) paths.  Then the middle layer and every signed
annular rank \(q_0\le q\le H\) have a literal word of length at most

\[
 \boxed{W+2Hp.}                                                 \tag{3.2}
\]

In particular, \(p=o(W/H)\) proves a coefficient-one compiler for the
fixed annulus.

#### Proof

Realize the \(p\) paths separately.  By (3.1), their total length is

\[
 |\Omega|+2Hp=N_{q_0}+2Hp.                                     \tag{3.3}
\]

Append once each of the \(W-N_{q_0}\) unselected middle masks.  The sum is
\(W+2Hp\).  Theorem 2.1 says that the path states already include a
witness for every signed annular target.  Concatenating the path words and
singletons cannot destroy an internal witness. \(\square\)

The same theorem holds with the audited bridge-one arcs in place of
genuine rotor arcs, provided their one-letter common-arrival realizations
are used.  The genuine-rotor statement is sufficient here and avoids any
extra promotion convention.

### Corollary 3.2 (floor-corrected \(2m\)-cycle form)

More generally, let \(R\subseteq\Omega\), put \(r=|R|\), and suppose
\(\Omega\setminus R\) has a directed rotor path cover with \(p\) paths.
The same proof gives the exact near-cover ledger

\[
 \boxed{
 L_{\rm ann}\le
 W+2Hp+2r(H-q_0+1).}                                         \tag{3.4}
\]

Indeed the omitted middle owners are included among the singleton middle
repairs, and at each signed depth only an omitted designated SCD provider
can create a new hole.  Thus \(p=o(W/H)\) and \(r=o(W/H)\) are sufficient.

Put

\[
 K=\left\lfloor{N_{q_0}\over2m}\right\rfloor,
 \qquad \rho=N_{q_0}-2mK.                                     \tag{3.5}
\]

Suppose \(2mK\) states of \(\Omega\) are partitioned into \(K\) directed
radius-\(H\) rotor cycles of length \(2m\).  Then the fixed annulus has a
literal word of length at most

\[
 \boxed{
 W+2HK+2\rho(H-q_0+1).}                                       \tag{3.6}
\]

Consequently this cycle factor is sufficient for \(W+o(W)\).

#### Proof

Cut and hard-start each cycle.  Its cost is \(2m+2H\).  Append all
unselected middle masks; the middle-layer total becomes exactly
\(W+2HK\).

In the full scaffold, every target has a unique designated provider at
depth \(q\), namely its chain in \(\mathcal D_{\ge q}\).  Omitting
\(\rho\) states can therefore remove at most \(\rho\) designated lower
providers and at most \(\rho\) designated upper providers at each depth.
Append each resulting hole as one literal singleton.  Summing over
\(H-q_0+1\) depths proves (3.6).

Finally, \(2HK=O(W/\sqrt m)\), while
\(2\rho(H-q_0+1)=O(m^{3/2})=o(W)\). \(\square\)

No divisibility assumption on \(N_{q_0}\) is hidden in this statement.

## 4. Exact ordered-Hall form of the surviving gate

Fix \(\mathcal D\), an annular port assignment
\(\sigma\in\Sigma_{q_0,H}(\mathcal D)\), and a total order
\(\prec\) on \(\Omega\).  Let
\(G_\prec\) be the bipartite graph with a left and a right copy of
\(\Omega\), and put an edge \(v_Lw_R\) exactly when

\[
 v\prec w\quad\hbox{and}\quad v\longrightarrow w
 \text{ is a genuine radius-}H\text{ rotor arc}.                \tag{4.1}
\]

Define the Hall deficiency

\[
 \operatorname{def}(G_\prec)
 =\max_{S\subseteq\Omega}
   \bigl(|S|-|N_{G_\prec}(S)|\bigr).                            \tag{4.2}
\]

### Theorem 4.1 (ordered-Hall path-cover equivalence)

The minimum number of components in a forward directed rotor path cover
of \(\Omega\) is exactly

\[
 \boxed{\operatorname{def}(G_\prec).}                           \tag{4.3}
\]

Consequently the corrected partial-annulus SCD theorem is proved if one
can choose \(\mathcal D\), one simultaneous annular port assignment
\(\sigma\) (including the short-chain outer extensions), and
\(\prec\) so that

\[
 \max_{S\subseteq\Omega}
 \bigl(|S|-|N_{G_\prec}(S)|\bigr)
 =o(W/H).                                                       \tag{4.4}
\]

#### Proof

A matching of size \(r\) in \(G_\prec\) chooses \(r\) rotor arcs with
indegree and outdegree at most one.  Strict increase under \(\prec\)
precludes directed cycles, so the chosen arcs form a spanning linear
forest with \(|\Omega|-r\) components.  Conversely every forward path
forest is such a matching.  The bipartite deficiency form of Hall's
theorem gives

\[
 \nu(G_\prec)=|\Omega|-\operatorname{def}(G_\prec),
\]

which proves (4.3).  Theorem 3.1 gives (4.4). \(\square\)

This is an exact integral Hall statement.  It contains no fractional
packet averaging and no histogram-cancellation sufficiency claim.

Optimizing the choices gives a compact exact form of the correlated gate.
Define

\[
 p_{\rm ann}(\mathcal D)
 =\min_{\sigma\in\Sigma_{q_0,H}(\mathcal D)}
   \min_{\prec}
   \max_{S\subseteq\Omega}
   \bigl(|S|-|N_{G_{\sigma,\prec}}(S)|\bigr).                  \tag{4.5}
\]

Here \(\sigma\) simultaneously chooses the owner-disjoint middle corners,
the two inner port orders, and every short-chain outer extension.
Then \(p_{\rm ann}(\mathcal D)\) is exactly the least number of components
in a genuine-rotor path cover obtainable from this SCD under the minimal
annular interface.  Thus the full surviving assertion is

\[
 \boxed{\min_{\mathcal D\ {\rm an\ SCD}}p_{\rm ann}(\mathcal D)
        =o(W/H).}                                               \tag{4.6}
\]

The inner minimization is ordinary bipartite Hall.  The outer choice of
\(\sigma\) is a correlated owner/port transversal and is not asserted to
be totally unimodular.  The explicit original-corner matching in (1.6)
only proves that its feasible set is nonempty; it does not prove (4.6).

## 5. The inherited top-tag obstruction

Fix an annular port assignment \(\sigma\) for this section, and let

\[
 \Omega_H=\mathcal D_{\ge H}\subseteq\Omega,
 \qquad |\Omega_H|=N_H.                                       \tag{5.1}
\]

Their top endpoint sets are forced, although their middle corners and two
inner \(q_0\)-port orders were freely chosen in \(\sigma\).  On two distinct
chains of full radius at least \(H\) in one SCD, bridge one is
equivalent to a genuine radius-\(H\)
rotor arc: identity would repeat the state, and promotion would preserve
the rank-\((m+H)\) endpoint, contradicting uniqueness in the SCD.

Let \(\lambda_H(\mathcal D,\sigma)\) be the maximum number of edges in a directed
vertex-disjoint linear forest in the rotor graph induced by this clipped
top class \(\Omega_H\).

### Theorem 5.1 (partial-annulus top-tag run bound)

Every bridge-one, and hence every genuine-rotor, path cover of \(\Omega\)
with \(p\) paths satisfies

\[
 \boxed{
 \lambda_H(\mathcal D,\sigma)\ge 2N_H-N_{q_0}-p,}             \tag{5.2}
\]

or equivalently

\[
 \boxed{
 p\ge
 \bigl(2N_H-N_{q_0}-\lambda_H(\mathcal D,\sigma)\bigr)_+.}    \tag{5.3}
\]

#### Proof

Read every path as a word over \(\{\mathsf H,\mathsf O\}\), according
as its full SCD tag is at least \(H\) or lies in \([q_0,H-1]\).
If \(r_H\) is the
total number of nonempty \(\mathsf H\)-runs, then path by path

\[
 \#\{\mathsf H\text{-runs}\}
 \le \#\{\mathsf O\text{-vertices}\}+1.
\]

Therefore

\[
 r_H\le (N_{q_0}-N_H)+p.                                      \tag{5.4}
\]

The number of selected path arcs having both ends in \(\Omega_H\) is

\[
 e_{HH}=N_H-r_H
 \ge2N_H-N_{q_0}-p.                                           \tag{5.5}
\]

These arcs form a vertex-disjoint directed linear forest.  Top-tag bridge
rigidity makes every one a genuine rotor arc, so
\(e_{HH}\le\lambda_H(\mathcal D,\sigma)\).  This proves (5.2). \(\square\)

### Corollary 5.2 (sharp Gaussian threshold)

If \(p=o(W/H)\), then necessarily

\[
 \lambda_H(\mathcal D,\sigma)
 \ge
 \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W.                         \tag{5.6}
\]

In particular, if

\[
 b^2-a^2<\log2,                                                \tag{5.7}
\]

then the right side of (5.6) is a positive linear fraction of \(W\).
Define the annular-port envelope

\[
 \Lambda_H^{\rm ann}(\mathcal D)
 =\max_{\sigma\in\Sigma_{q_0,H}(\mathcal D)}
   \lambda_H(\mathcal D,\sigma).                              \tag{5.6a}
\]

Every SCD with \(\Lambda_H^{\rm ann}=o(W)\) fails the partial-annulus
ordered-Hall gate in this range.  This conditional sentence must not be
applied to BTK: the clipped BTK graph has explicit tag-\(H\) rotor edges
for every \(1\le H<m\), and its annular-port envelope is not known here.

#### Proof

Uniformly for fixed \(c\),

\[
 {\binom{2m}{m-\lfloor c\sqrt m\rfloor}\over W}
 =e^{-c^2+o(1)}.                                               \tag{5.8}
\]

Substitute \(c=a,b\) into (5.2).  Since
\(p=o(W/H)=o(W)\), equation (5.6) follows.  Its coefficient is positive
exactly when

\[
 2e^{-b^2}>e^{-a^2},
\]

which is (5.7).  No assertion about the value of
\(\Lambda_H^{\rm ann}\) for BTK is used. \(\square\)

For a factor by \(K\) length-\(2m\) cycles with \(\rho\) omitted states,
the identical argument after cutting one edge per cycle gives the exact
weakened necessary inequality

\[
 \lambda_H(\mathcal D,\sigma)
 \ge 2N_H-N_{q_0}-\rho-K.                                     \tag{5.9}
\]

Indeed at most \(\rho\) omitted states can have tag \(H\), and cutting
the cycles loses at most \(K\) top--top arcs.  Both corrections are
\(o(W)\), so the threshold (5.7) is unchanged.

### Theorem 5.3 (all-threshold protected-promotion hierarchy)

The top tag is the endpoint of a more general exact filtration.  Fix
\(q_0\le q\le H\), and consider two distinct decorated states whose SCD
tags are both at least \(q\).  In the bridge-one classification, an
identity arc is impossible.  A promotion arc

\[
 L'=L-x+z_j,\qquad
 (z'_1,\ldots,z'_{2H})
 =(x,z_1,\ldots,\widehat z_j,\ldots,z_{2H})                  \tag{5.10}
\]

is possible between them only if

\[
 \boxed{j>H+q.}                                                \tag{5.11}
\]

Thus every bridge-one arc induced by \(\mathcal D_{\ge q}\) is either a
genuine rotor arc or one of the \(H-q\) late-promotion types in (5.11).

Let \(\lambda_q^{\rm late}(\mathcal D,\sigma)\) be the maximum number of arcs in a
vertex-disjoint directed linear forest in this induced rotor-plus-late-
promotion graph.  Every bridge-one path cover of \(\Omega\) with \(p\)
paths satisfies

\[
 \boxed{
 \lambda_q^{\rm late}(\mathcal D,\sigma)
 \ge2N_q-N_{q_0}-p.}                                          \tag{5.12}
\]

#### Proof

The rank-\((m+q)\) flag of a complete state is

\[
 C_q=L+\{z_1,\ldots,z_{H+q}\}.                                \tag{5.13}
\]

If \(j\le H+q\), direct substitution of (5.10) gives

\[
 C'_q
 =L-x+z_j+x+
   (\{z_1,\ldots,z_{H+q}\}\setminus\{z_j\})
 =C_q.                                                         \tag{5.14}
\]

But for tags at least \(q\), these are actual rank-\((m+q)\) members of
the common SCD.  Two distinct chains cannot share one such member.  Hence
\(j\le H+q\) is forbidden.  If \(j>H+q\), equation (5.14) no longer
holds; these are exactly the promotion types not excluded by this rank-
\(q\) uniqueness argument.  The bridge classification leaves only rotor,
promotion, and identity, proving the structural claim.

Now mark the vertices of \(\mathcal D_{\ge q}\) by \(\mathsf A\) and the
other vertices of \(\Omega\) by \(\mathsf B\).  The same run count as in
Theorem 5.1 forces at least

\[
 2|\mathcal D_{\ge q}|-|\Omega|-p=2N_q-N_{q_0}-p
\]

selected path arcs with both endpoints marked \(\mathsf A\).  They form a
linear forest and, by the first part, belong to the rotor-plus-late-
promotion graph.  This proves (5.12). \(\square\)

This statement has an equivalent selector-independent projected form.
For \(q\le H\), absorb the first and last \(H-q\) collar coordinates and
write \(\tau_q\omega\) for the resulting radius-\(q\) state of a
chain in \(\mathcal D_{\ge q}\).  Once the annular port assignment
\(\sigma\) is fixed, the truncation is independent of collar coordinates
strictly outside radius \(q\); it can depend on the allowed inner
\(q_0\)-port orders.  A full rotor truncates to
a radius-\(q\) rotor.  A promotion has the three exact regimes

\[
\begin{array}{c|c}
1\le j\le H-q&\text{identity after }\tau_q,\\
H-q<j\le H+q&\text{radius-\(q\) promotion},\\
H+q<j\le2H&\text{radius-\(q\) rotor}.
\end{array}                                                     \tag{5.12a}
\]

The first regime repeats the lower rank-\((m-q)\) SCD mask and the second
repeats the upper rank-\((m+q)\) SCD mask, so neither can join two distinct
chains of \(\mathcal D_{\ge q}\).  Hence every induced full bridge arc,
including every allowed late promotion, projects to a genuine
radius-\(q\) rotor arc.

Let \(\lambda_q^{\rm proj}(\mathcal D,\sigma)\) be the maximum size of a directed
linear forest in this forced projected rotor graph on
\(\mathcal D_{\ge q}\).  Projection preserves the chain vertices and
therefore preserves a selected linear forest.  Thus (5.12) also gives,
for the fixed annular port assignment, the cut

\[
 \boxed{
 \lambda_q^{\rm proj}(\mathcal D,\sigma)
 \ge2N_q-N_{q_0}-p.}                                          \tag{5.12b}
\]

In particular, with

\[
 \Lambda_q^{\rm ann}(\mathcal D)
 =\max_{\sigma\in\Sigma_{q_0,H}(\mathcal D)}
   \lambda_q^{\rm proj}(\mathcal D,\sigma),
\]

existence of any annular-port choice with a \(p\)-path cover forces the
same lower bound on \(\Lambda_q^{\rm ann}(\mathcal D)\).

For \(q=\lfloor c\sqrt m\rfloor\), (5.12) demands a positive-density
protected forest whenever

\[
 c^2-a^2<\log2.                                                \tag{5.15}
\]

At \(q=H\) there are no late promotions and Theorem 5.3 reduces exactly
to the genuine-rotor cut in Theorem 5.1.  At lower thresholds it records
the only available escape explicitly: density must be supplied either by
true rotor transport or by promotions drawing from the still-unowned
upper tail \(z_{H+q+1},\ldots,z_{2H}\).  Ordinary rank marginals do not
see this filtration.

### Theorem 5.4 (full-top fibre cut for the partial scaffold)

Let a bridge-one path cover of \(\Omega=\mathcal D_{\ge q_0}\) have
\(p\) paths, and let \(r_{\rm full}\) be the number of its genuine
full-radius-\(H\) rotor arcs.  Then

\[
 \boxed{p+r_{\rm full}\ge N_H.}                               \tag{5.16}
\]

Consequently, if \(p=o(W/H)\),

\[
 \boxed{
 r_{\rm full}\ge
 \bigl(e^{-b^2}-o(1)\bigr)W.}                                 \tag{5.17}
\]

This holds for every fixed \(0<a<b\); unlike the induced top--top run
bound, it has no \(b^2-a^2<\log2\) restriction.

#### Proof

For a complete state put

\[
 U_H(\omega)=L+\{z_1,\ldots,z_{2H}\}.                          \tag{5.18}
\]

Call this its full top fibre.  A promotion preserves \(U_H\), whereas a
genuine full rotor changes it.  The selected set \(\Omega\) contains all
chains of full radius at least \(H\).  Their forced clipped states give
exactly one anchor in each of the \(N_H\) distinct rank-\((m+H)\) fibres.

Delete all \(r_{\rm full}\) genuine full-rotor arcs from the path forest.
The number of components becomes exactly \(p+r_{\rm full}\).  Every
remaining nontrivial arc is a promotion and stays inside one fibre.
The anchors occupy \(N_H\) distinct fibres, so they lie in at least
\(N_H\) different remaining components.  This proves (5.16).  Equation
(5.17) follows from \(N_H/W=e^{-b^2+o(1)}\). \(\square\)

If \(K\) length-\(2m\) cycles cover all but \(\rho\) states of \(\Omega\),
then, with \(r_{\rm full}^{\rm cyc}\) the number of their full-rotor arcs,

\[
 \boxed{
 r_{\rm full}^{\rm cyc}\ge N_H-\rho-K.}                        \tag{5.19}
\]

Indeed, cut one edge in every cycle.  At most \(K\) full-rotor arcs and
at most \(\rho\) top-fibre anchors are lost, and then apply (5.16).
Since \(K=o(W)\) and \(\rho<2m\), the same asymptotic lower bound
(5.17) holds.  Averaged over the \(K\) packets, a fraction at least

\[
 e^{-(b^2-a^2)}-o(1)                                          \tag{5.20}
\]

of all packet arcs must be genuine full rotors.  The narrower run cut
additionally forces the fraction
\(2e^{-(b^2-a^2)}-1-o(1)\) to be full rotors whose two endpoints are
both clipped top-tag states.

## 6. Exact proved and conditional boundary

Proved here:

1. one arbitrary full SCD gives an exact owner-simple set of
   \(N_{q_0}\) paid middle occurrences;
2. its nested tag classes give exact one-copy lower and upper provider
   equations at every depth \(q_0\le q\le H\);
3. a radius-\(H\) rotor path cover with \(p\) components compiles these
   providers at exact length \(W+2Hp\);
4. a floor-corrected length-\(2m\) cycle factor has only
   \(O(m^{3/2})=o(W)\) possible provider holes;
5. the remaining owner/port/path problem has the exact optimized
   ordered-Hall form (4.5)--(4.6); and
6. the full-top fibre cut (5.16) forces
   \((e^{-b^2}-o(1))W\) genuine full rotors for every fixed annulus; the
   induced top-tag cut (5.3) further forces a positive-density genuine
   top--top rotor forest
   precisely on the narrow-annulus range \(b^2-a^2<\log2\), and the
   all-threshold hierarchy (5.12) identifies the only permitted promotion
   escape below the top tag.

Two companion notes sharpen the chronological boundary.  The exact
diagonal-port equations and the inner-reordering-invariant outer-tail cut
are in
`MATH_THEOREM_S_PARTIAL_ANNULUS_DIAGONAL_PORT_AND_TAIL_HALL_20260726.md`.
The endpoint-antipode law and native-radius cross-grading cut are in
`MATH_THEOREM_S_PARTIAL_ANNULUS_ANTIPODE_AND_RADIUS_CUT_20260726.md`.
In particular, an actual \(2m\)-cycle factor requires almost every
depth-\(q_0\) endpoint orbit to be a two-cycle and requires
\(\Theta(H)\) nondecreasing native-radius arcs per packet.

Not proved here:

1. an SCD satisfying the optimized gate (4.6);
2. a factor of its tag-\(\ge q_0\) states into length-\(2m\) rotor cycles;
3. the required positive-density top-tag rotor forest for a noncanonical
   SCD below the threshold; or
4. coefficient one outside this conditional annulus compiler.

The corrected slack eliminates the all-depth incidence/discrepancy gate
inside the SCD model: target support is already exact.  It does not
eliminate chronology.  The surviving task is now genuinely one-dimensional
and integral: construct one noncanonical SCD whose tag-\(\ge q_0\)
decorated rotor graph has ordered-Hall deficiency \(o(W/H)\), while its
chosen tag-\(H\) port graph supplies the linear forest forced by (5.6)
and the whole route supplies the full rotors forced by (5.17).
