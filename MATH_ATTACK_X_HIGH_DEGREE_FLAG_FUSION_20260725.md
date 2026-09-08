# Lane X: integral high-degree cross-parent flags and the exact rotor gate

Date: 2026-07-25

## 0. Outcome

There is no incidence-capacity obstruction to the surface-scale,
high-degree fusion demanded by the equal-shell endpoint theorem.

Fix an even Boolean dimension \(k=2m\), a four-block product-SCD
decomposition, and

\[
H=\lceil A\sqrt m\rceil
\tag{0.1}
\]

for fixed \(A>0\).  There is an integral family of exactly

\[
W=\binom{2m}{m}
\]

two-sided saturated flags, one rooted at every middle set, such that every
target in every rank \(m-H,\ldots,m+H\) occurs at least once.  After one
coordinate relabelling, all but \(o(W)\) of these flags meet a different
four-box parent at every one of their \(2H+1\) ranks.  Thus almost every
abstract portal has cross-parent degree

\[
2H+1=\Theta(\sqrt m).
\tag{0.2}
\]

In particular the flags contain every target in the U7 certified-support
complement, simultaneously at every depth.  They absorb the complete
shoulder ledger abstractly using exactly the width number \(W\) of portal
sites.

What is not proved is physical resolvability.  The balanced flags are not
known to be the suffix-OR states of one word of length \(W+o(W)\).  The
remaining statement is an exact rotor path-cover lemma: choose the balanced
flags so their ordered-partition prefixes split into
\(o(W/H)\) one-update MTF runs.  Such a path cover has an explicit literal
word of length

\[
W+2HJ+1,
\tag{0.3}
\]

where \(J\) is the number of runs.  Therefore \(J=o(W/H)\) proves the
fixed Gaussian-window theorem and, after diagonalization in \(A\), the
constant-one upper bound.

This is the minimal surviving fusion problem in this lane.  Coverage,
integrality, nesting, common middle ownership, parent-rainbowness, and the
surface/high-degree incidence count are all solved below.  Only the common
coverage/dynamics resolution is open.

---

## 1. Integral balanced two-sided flag factor

Put

\[
N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\qquad 0\le q\le H.
\tag{1.1}
\]

### Theorem 1.1 (balanced flag factor)

There are maps

\[
L_q:\binom{[2m]}m\longrightarrow\binom{[2m]}{m-q},
\qquad 0\le q\le H,
\tag{1.2}
\]

and

\[
U_q:\binom{[2m]}m\longrightarrow\binom{[2m]}{m+q},
\qquad 0\le q\le H,
\tag{1.3}
\]

such that, for every middle owner \(X\),

\[
L_H(X)\subset L_{H-1}(X)\subset\cdots\subset L_0(X)=X
 =U_0(X)\subset\cdots\subset U_H(X),
\tag{1.4}
\]

every consecutive inclusion has difference one, and every target \(S\) at
depth \(q\) has load

\[
\#\{X:L_q(X)=S\},\quad \#\{X:U_q(X)=S\}
\in
\left\{
\left\lfloor\frac{W}{N_q}\right\rfloor,
\left\lceil\frac{W}{N_q}\right\rceil
\right\}.
\tag{1.5}
\]

Consequently every target in every displayed rank occurs in at least one
flag.

#### Proof

Use the layered inclusion network from rank \(m\) down to rank \(m-H\).
Split every depth-\(q\) set \(S\) into an in-node and out-node, and give its
internal arc capacities

\[
\left\lfloor\frac{W}{N_q}\right\rfloor
\le f(S^{\rm in},S^{\rm out})\le
\left\lceil\frac{W}{N_q}\right\rceil.
\tag{1.6}
\]

At depth zero both capacities are one.  Put an unbounded downward arc on
every facet inclusion, send one unit into every middle set, and require
total flow \(W\) at the bottom.

The symmetric fractional flow is feasible: every depth-\(q\) set has
throughput \(W/N_q\), divided equally among its facets.  Indeed a
depth-\((q+1)\) set has \(m+q+1\) parents and every depth-\(q\) parent has
\(m-q\) facets, while

\[
\frac{N_q}{N_{q+1}}=\frac{m+q+1}{m-q}.
\tag{1.7}
\]

After the standard lower-capacity reduction, the network matrix is a
directed incidence matrix.  Integral capacities and fractional feasibility
therefore give an integral flow.  Decompose it into \(W\) unit paths, one
starting at each middle set.  Their depth-\(q\) vertices define \(L_q\)
and prove (1.4)--(1.5) on the lower side.

Define the upper side by complementation:

\[
U_q(X)=[2m]\setminus L_q([2m]\setminus X).
\tag{1.8}
\]

This is nested upward from \(X\), and complementation preserves the load
histogram.  Finally \(W/N_q\ge1\), so the lower value in (1.5) is at least
one. \(\square\)

The construction is one common integral owner table at every depth.  It is
not a collection of independently balanced rank marginals.

---

## 2. Almost every flag can be made parent-rainbow

Partition \([2m]\) into four fixed coordinate blocks and choose one SCD in
each block.  Their products partition the Boolean lattice into four-chain
parents.  Write \(P(S)\) for the parent containing a target \(S\).

### Lemma 2.1 (same-parent extension bound)

Let \(X\subset Y\) have rank gap \(g\ge1\), with both ranks in
\([m-H,m+H]\).  For a uniform coordinate permutation \(\sigma\),

\[
\Pr(P(\sigma X)=P(\sigma Y))
\le
\frac{\binom{g+3}{3}}
     {\binom{m-H}{g}}.
\tag{2.1}
\]

#### Proof

Condition on \(\sigma X\).  The set \(\sigma(Y\setminus X)\) is a uniform
\(g\)-subset of the complement, whose size is at least \(m-H\).

If \(\sigma X\) and \(\sigma Y\) lie in the same product of four chains,
then in each factor chain one advances some number \(g_i\ge0\) of ranks,
with \(g_1+\cdots+g_4=g\).  A weak composition \((g_1,\ldots,g_4)\)
determines at most one possible upper point of that product parent.  There
are \(\binom{g+3}{3}\) weak compositions, proving (2.1). \(\square\)

### Theorem 2.2 (integral high-degree parent-rainbow fusion)

For every fixed \(A>0\), some coordinate relabelling of the balanced flag
factor in Theorem 1.1 has at most

\[
O_A\left(\frac{W}{\sqrt m}\right)=o(W)
\tag{2.2}
\]

flags containing two members in the same four-chain parent.  Every other
flag visits \(2H+1\) distinct parents.

#### Proof

In one flag, group unordered pairs of members by their rank gap \(g\).  At
most \(2H+1-g\) pairs have gap \(g\).  Lemma 2.1 gives expected collision
count at most

\[
\sum_{g=1}^{2H}(2H+1-g)
\frac{\binom{g+3}{3}}{\binom{m-H}{g}}.
\tag{2.3}
\]

The \(g=1\) term is \(O_A(H/m)\).  For \(g\ge2\), use

\[
\binom{m-H}{g}\ge\left(\frac{m-H}{g}\right)^g.
\tag{2.4}
\]

Since \(g\le2H=O_A(\sqrt m)\), the resulting series is dominated by its
\(g=2\) term and contributes \(O_A(H/m^2)\).  Thus (2.3) is
\(O_A(m^{-1/2})\).

Summing over the \(W\) flags, the expected number of same-parent pairs is
\(O_A(W/\sqrt m)\).  Every non-parent-rainbow flag contains at least one
such pair.  Some relabelling therefore has at most the number in (2.2).
Relabelling preserves every load in (1.5). \(\square\)

This gives the exact kind of high-degree cross-parent object forced by the
equal-shell no-go.  It is integral, all target names are literal Boolean
sets, and almost every one of the \(W\) portal flags has degree
\(\Theta(H)=\Theta(\sqrt m)\).

Since every band target occurs at least once by Theorem 1.1, the abstract
flags contain, in particular, every target counted by every local
\(D_R(d)\) ledger after the local equal cores are embedded in the Boolean
cube.  Thus the shoulder deficit is not blocked by Hall, divisibility,
nesting, common ownership, or parent collisions.

---

## 3. A surface-size extraction corollary

The full flag factor is stronger than the endpoint-sharing toll needs.
The following formulation matches its natural scale.

Let \(\mathcal T_a\subseteq\binom{[2m]}{m+a}\), \(|a|\le H\), be
prescribed shoulder target families satisfying

\[
\sum_{a=-H}^{H}
\frac{|\mathcal T_a|}{\binom{2m}{m+a}}
\ge \rho H
\tag{3.1}
\]

for a fixed \(\rho>0\).

### Corollary 3.1 (surface number of high-degree portals)

There are

\[
P=O(W/H)
\tag{3.2}

\]

pairwise target-disjoint saturated flags and one coordinate relabelling
such that:

1. all but \(o(P)\) flags are parent-rainbow;
2. every retained flag has degree \(2H+1=\Theta(H)\); and
3. the retained flags contain \(\Omega(W)\) incidences with the prescribed
   families \(\mathcal T_a\).

#### Proof

Fix any SCD of \(B_{2m}\).  The number of its chains meeting every rank in
the displayed band is exactly \(\binom{2m}{m-H}=\Theta_A(W)\), whereas
\(W/H=o(W)\).  Select \(P=\lceil cW/H\rceil\) of these long chains.

Under a uniform coordinate relabelling, the member at rank \(m+a\) of
each fixed chain is uniform in that rank.  Hence the expected number of
prescribed incidences is at least \(\rho PH=\Theta(W)\).  The proof of
Theorem 2.2 gives only \(O_A(P/\sqrt m)=o(P)\) bad flags in expectation.
Deleting every bad flag loses at most \((2H+1)o(P)=o(PH)=o(W)\)
incidences.  Taking expectation of “prescribed incidences minus the loss
bound” yields one relabelling satisfying all three conclusions. \(\square\)

This closes the pure incidence count behind the surface/high-degree portal
requirement.  It does not yet make the flags physical endpoints of one
word.

---

## 4. Exact ordered-state form of one flag

For one middle owner \(X\), write the combined flag from (1.4) as

\[
F_{X,-H}\subset F_{X,-H+1}\subset\cdots\subset F_{X,H}.
\tag{4.1}
\]

Define disjoint nonempty blocks

\[
B_{X,0}=F_{X,-H},
\qquad
B_{X,i}=F_{X,-H+i}\setminus F_{X,-H+i-1}
\quad(1\le i\le2H).
\tag{4.2}
\]

The blocks after \(B_{X,0}\) are singletons, and their union is
\(F_{X,H}\), a proper subset because \(H<m\).  Put

\[
\Lambda_X=(B_{X,0},B_{X,1},\ldots,B_{X,2H}).
\tag{4.3}
\]

Every ordered partition beginning with \(\Lambda_X\) exposes the entire
flag as its first \(2H+1\) prefix unions.  Equivalently, at the
corresponding word endpoint, the suffix ORs beginning at the last
occurrence of \(B_{X,i}\) represent all the targets (4.1).

Call a sequence \(X_1,\ldots,X_s\) a **one-update flag run** if there are
full ordered states \(\Sigma_i\), each beginning with \(\Lambda_{X_i}\),
and nonempty masks \(A_i\) such that

\[
\Sigma_{i+1}=M_{A_i}(\Sigma_i)
\qquad(1\le i<s).
\tag{4.4}
\]

The masks need not be prescribed lower cores; allowing arbitrary legal MTF
updates makes the remaining lemma weaker.

### Lemma 4.1 (exact run realization)

If the \(W\) owners split into \(J\) one-update flag runs, then one
nonzero literal OR word covers every member of every flag and has length

\[
\boxed{W+2HJ+1.}
\tag{4.5}
\]

#### Proof

For the first run, emit the nonempty complement of
\(F_{X_1,H}\), followed by

\[
B_{X_1,2H},B_{X_1,2H-1},\ldots,B_{X_1,0}.
\tag{4.6}
\]

This initializes a full state beginning with \(\Lambda_{X_1}\).  Emit the
\(s-1\) one-update masks along the run.

At every later run, reverse-write only its \(2H+1\) useful prefix blocks.
They are disjoint and their union is proper, so the old residual tail is
inherited behind the desired prefix.  Then emit that run's one-update
masks.

The first run costs \(1+(2H+1)+(s_1-1)=s_1+2H+1\).  Every later run costs
\((2H+1)+(s_j-1)=s_j+2H\).  Summing \(\sum_js_j=W\) proves (4.5).  The
prefix-union observation before the lemma proves every literal witness.
\(\square\)

---

## 5. Minimal open design lemma

> **Balanced high-degree flag rotor lemma \(\mathrm{BFR}_A\) — OPEN.**  For
> every fixed \(A>0\), with \(H=\lceil A\sqrt m\rceil\), choose one
> integral balanced two-sided flag factor as in Theorem 1.1 whose \(W\)
> ordered prefixes split into
> \[
> J=o(W/H)
> \]
> one-update flag runs.

By Lemma 4.1, \(\mathrm{BFR}_A\) gives a word of length \(W+o(W)\)
covering every target in the fixed Gaussian band.  Proving it for every
fixed \(A\) and diagonalizing gives a band
\(H=\sqrt m\,\omega(m)\), after which the established tail word completes
the constant-one theorem.

The lemma asks for one common resolution of two exact structures already
available separately:

1. **Coverage resolution.**  Theorem 1.1 gives balanced integral flags,
   complete band coverage, and after relabelling parent-rainbow degree
   \(\Theta(H)\).
2. **Dynamics resolution.**  An exact wreath factor splits the middle
   owners into \(W/(2m+1)\) cyclic one-update runs.  Its reset cost is
   \(O(HW/m)=o(W)\), but its nonmiddle interval loads need not cover the
   ranks.

The missing mathematics is to make these resolutions coincide.  It is not
a remaining fractional matching, shell-cap, width-accounting, or portal-
capacity issue.  It is a single integral rotor/path-cover problem in the
exact middle-owner fibre.

---

## 6. Consequence for Lane X

The surface-scale high-degree fusion demanded by the Lane H no-go is
therefore feasible at the set-incidence level, and much more is true:
almost all \(W\) abstract portals can have degree \(\Theta(\sqrt m)\) while
covering the entire band with balanced multiplicity.

However, this does not yet upgrade the U7 word.  A physical word must
realize those abstract flags as suffix chains at the same endpoints while
moving between their ordered states at average cost \(1+o(1)\).  The exact
quantitative gate is \(\mathrm{BFR}_A\).  No proof of that rotor path cover
is currently available.

---

## 7. Exact compatibility graph and why parent-rainbow is orthogonal

Write one flag state as

\[
\gamma_X=(L;z_1,\ldots,z_{2H};R),
\tag{7.1}
\]

where

\[
L=F_{X,-H},\qquad
F_{X,-H+t}=L\cup\{z_1,\ldots,z_t\},qquad
R=[2m]\setminus F_{X,H}.
\tag{7.2}
\]

Thus \(|L|=|R|=m-H\).  The canonical tail-entering rotor update chooses
\(x\in L\), \(y\in R\), and produces a state beginning with

\[
\mathcal R_{x,y}(\gamma_X)
=
(L-x+y;x,z_1,\ldots,z_{2H-1};R-y+z_{2H}).
\tag{7.3}
\]

The final displayed component records only the remaining coordinate set;
its physical tail may have several blocks.  This useful prefix is exactly
what the move-to-front update by the new lower core \(L-x+y\) produces.
Its middle owner is

\[
X-z_H+y,
\tag{7.4}
\]

so it is a Johnson neighbour of \(X\).

There are additional legal owner-changing one-update transitions.  If
\(y=z_j\) for \(H<j\le2H\), updating by \(L-x+y\) produces a state
beginning with

\[
(L-x+y;x,z_1,\ldots,z_{j-1},z_{j+1},\ldots,z_{2H}).
\tag{7.4a}
\]

Its owner is again \(X-z_H+y\).  Choosing \(y=z_j\) with \(j\le H\)
leaves the middle owner unchanged, so those transitions are irrelevant to
a path on the distinct owner vertices.

Let \(\Gamma=\{\gamma_X:X\in\binom{[2m]}m\}\) be any one-state-per-owner
flag table, and define its **rotor compatibility digraph**
\(\mathfrak R(\Gamma)\) by

\[
X\longrightarrow Y
\quad\Longleftrightarrow\quad
\text{one update by }L_Y\text{ sends a state beginning with }
\gamma_X\text{ to one beginning with }\gamma_Y.
\tag{7.5}
\]

### Proposition 7.1 (flag-language compatibility test)

An edge \(X\to Y\) exists if and only if there are
\(x\in F_{X,-H}\), \(y\notin X\), and an index
\(j\in\{H+1,\ldots,2H+1\}\) satisfying the following conditions.

If \(j\le2H\), then

\[
y=F_{X,-H+j}\setminus F_{X,-H+j-1};
\tag{7.5a}
\]

if \(j=2H+1\), then \(y\notin F_{X,H}\).  In both cases

\[
F_{Y,-H}=F_{X,-H}-x+y
\tag{7.6}
\]

and, simultaneously for every \(1\le t\le2H\),

\[
F_{Y,-H+t}
=
\begin{cases}
F_{X,-H+t-1}\cup\{y\},&t<j,\\
F_{X,-H+t},&j\le t\le2H.
\end{cases}
\tag{7.7}
\]

When \(j=2H+1\), only the first line occurs.

#### Proof

If \(y\) lies in the tail, the prefix union at depth \(t\ge1\) after the
update is

\[
(L-x+y)\cup\{x,z_1,\ldots,z_{t-1}\}
=F_{X,-H+t-1}\cup\{y\}.
\]

If \(y=z_j\), then before the deleted old singleton position the same
formula holds.  At and after that position the skipped singleton already
belongs to the new lower core, so the prefix union is the old
\(F_{X,-H+t}\).  The depth-zero prefix is always \(L-x+y\).

Conversely, after updating by a distinct lower core \(L_Y\), the first
residual old block must be a singleton.  Since \(|L_Y|=|L|\), this forces
\(L_Y=L-x+y\).  To change the owner, \(y\notin X\); hence \(y\) is either
one of \(z_{H+1},\ldots,z_{2H}\) or lies in the tail.  Reading the old
blocks in order gives exactly (7.7). \(\square\)

Thus one compatibility edge is not a marginal inclusion condition.  It is a system
of \(2H+1\) coherent equalities between two complete flags.

Moreover, for every coordinate permutation \(\sigma\),

\[
X\to Y\text{ in }\mathfrak R(\Gamma)
\quad\Longleftrightarrow\quad
\sigma X\to\sigma Y\text{ in }\mathfrak R(\sigma\Gamma).
\tag{7.8}
\]

Hence the relabelling that makes the flags parent-rainbow leaves the entire
compatibility digraph unchanged.  Parent-rainbow extraction can be applied
after a rotor-coherent table is found, but it cannot create rotor edges.

---

## 8. Quantitative sparsity of an uncorrelated transversal

The full radius-\(H\) flag-prefix state space has

\[
|\Omega_H|=\frac{(2m)!}{(m-H)!^2}
\tag{8.1}
\]

states.  Every middle owner has exactly

\[
K_H=(m)_H^2
=\left(\frac{m!}{(m-H)!}\right)^2
\tag{8.2}
\]

states above it.  Every state has exactly

\[
(m-H)m
\tag{8.2a}
\]

owner-changing one-update successors: choose \(x\in L\), and then choose
\(y\in[2m]\setminus X\).  The latter set consists of the \(H\) active
upper singletons and the \(m-H\) tail coordinates.

### Proposition 8.1 (random transversals have essentially no rotor edges)

Choose independently and uniformly one state above every middle owner.
Then the expected number of edges in the induced compatibility digraph is

\[
\boxed{
\mathbb E e(\mathfrak R(\Gamma))
=W\frac{(m-H)m}{K_H}.}
\tag{8.3}
\]

For \(H\ge2\), this is \(O(Wm^{2-2H})\); for
\(H=\lceil A\sqrt m\rceil\) it is superpolynomially smaller than \(W\).

#### Proof

The full compatibility digraph has \(WK_H(m-H)m\) directed edges.  Its endpoints
have different middle owners.  A fixed full edge survives the independent
owner-transversal selection with probability \(K_H^{-2}\).  Linearity of
expectation gives (8.3). \(\square\)

Choose a transversal with at most the expectation in (8.3), and then apply
the relabelling argument from the proof of Theorem 2.2 (that argument uses
only saturated flags, not balanced loads).  By (7.8), the rotor edge count does not
change, while all but \(o(W)\) flags become parent-rainbow.  Therefore
parent-rainbow degree \(\Theta(H)\) across four-box labels does not imply
positive rotor min-degree, expansion, or even \(\Omega(W)\) total rotor
edges.  The two notions of degree are genuinely different.

The random transversal need not have balanced rank loads; Proposition 8.1
is not a counterexample to \(\mathrm{BFR}_A\).  It proves exactly that the
parent-rainbow theorem cannot be the missing argument.  Balance and rotor
coherence must be imposed jointly.

---

## 9. The exact missing compatibility statistic

For a flag table \(\Gamma\), define

\[
\ell_{\rm rot}(\Gamma)
=\max\{|E(\mathcal P)|:\mathcal P
\text{ is a spanning directed linear forest in }
\mathfrak R(\Gamma)\}.
\tag{9.1}
\]

Here every vertex has indegree and outdegree at most one in \(\mathcal P\),
and directed cycles are forbidden.  Put

\[
\boxed{
\delta_{\rm rot}(\Gamma)=W-\ell_{\rm rot}(\Gamma).}
\tag{9.2}
\]

A spanning directed linear forest with \(e\) edges has exactly \(W-e\)
path components.  Consequently

\[
\boxed{
\delta_{\rm rot}(\Gamma)
=\text{the minimum number of one-update rotor runs covering }
\Gamma.}
\tag{9.3}
\]

Thus the minimal open lemma can be written without chronology prose:

> **Balanced rotor-forest lemma — OPEN.**  For every fixed \(A>0\), some
> balanced two-sided flag factor \(\Gamma_m\) at
> \(H=\lceil A\sqrt m\rceil\) satisfies
> \[
> \delta_{\rm rot}(\Gamma_m)=o(W/H).
> \tag{9.4}
> \]

This is equivalent to \(\mathrm{BFR}_A\) for the full one-update
compatibility relation (7.5)--(7.7), and it is sufficient for the literal word bound by
Lemma 4.1.

There is a useful two-part relaxation.  Let \(B_\Gamma\) be the bipartite
graph with a left and right copy of the owner set and edge \(X_LY_R\) for
every rotor edge \(X\to Y\).  Its maximum matching deficiency is exactly

\[
\Delta_H(\Gamma)
=\max_{S\subseteq V}(|S|-|N^+(S)|)
=W-\nu(B_\Gamma).
\tag{9.5}
\]

A matching gives a disjoint union of directed paths and cycles.  Hence
(9.4) follows if

1. \(\Delta_H(\Gamma)=o(W/H)\); and
2. a maximum or near-maximum matching can be chosen with
   \(o(W/H)\) directed cycles.

The second clause cannot be discarded: the full rotor graph contains the
short slot-rotation cycles of length \(2H+2\), so a cycle factor may have
\(\Theta(W/H)\) components.  What is needed is either average cycle length
\(\omega(H)\), or enough extra rotor edges to splice those cycles.

Equations (7.6)--(7.7), together with the Hall profile (9.5) and the cycle
count, are the exact missing local compatibility statistics.  Balanced
rank histograms control none of them directly.

---

## 10. A first local obstruction: deletion-word flow imbalance

The lower half of a flag has a unique ordered deletion word

\[
d(X)=(d_1(X),\ldots,d_H(X)),
\qquad
d_q(X)=L_{q-1}(X)\setminus L_q(X).
\tag{10.1}
\]

In the state notation (7.1),

\[
(z_1,\ldots,z_H)=(d_H,\ldots,d_1).
\tag{10.2}
\]

### Proposition 10.1 (de Bruijn overlap condition)

Every owner-changing compatibility edge \(X\to Y\) satisfies

\[
\boxed{
d(Y)=(d_2(X),d_3(X),\ldots,d_H(X),x)}
\tag{10.3}
\]

for the unique coordinate \(x\in L_H(X)\setminus L_H(Y)\).

#### Proof

For every legal owner-changing update in Proposition 7.1, the entering
coordinate \(y\) occurs strictly after the first \(H\) active singleton
blocks, or in the tail.  Hence the first \(H\) residual singletons after
the new lower core are always

\[
(x,z_1,z_2,\ldots,z_{H-1}).
\]

Reverse this list using (10.2). \(\square\)

For an ordered \((H-1)\)-tuple \(\theta\), define

\[
a_\theta
=\#\{X:(d_2(X),\ldots,d_H(X))=\theta\},
\tag{10.4}
\]

\[
b_\theta
=\#\{X:(d_1(X),\ldots,d_{H-1}(X))=\theta\}.
\tag{10.5}
\]

Both families have total mass \(W\).  Every directed linear-forest edge
uses one outgoing suffix and one equal incoming prefix.  Therefore

\[
\ell_{\rm rot}(\Gamma)
\le\sum_\theta\min(a_\theta,b_\theta)
=W-\frac12\sum_\theta|a_\theta-b_\theta|.
\tag{10.6}
\]

Consequently

\[
\boxed{
\delta_{\rm rot}(\Gamma)
\ge
\Delta_{\rm seq}(\Gamma)
:=
\frac12\sum_\theta|a_\theta-b_\theta|.}
\tag{10.7}
\]

This is a genuinely local necessary statistic.  The balanced constraints
(1.5) specify the multiplicities of the unordered prefix-deletion sets
\(\{d_1,\ldots,d_q\}\).  They impose no equality between the ordered
suffix histogram (10.4) and ordered prefix histogram (10.5).

Even \(\Delta_{\rm seq}=0\) is not sufficient.  Write

\[
a_q(X)=U_q(X)\setminus U_{q-1}(X)
\tag{10.8}
\]

for the upper addition word.  If the entering coordinate in an edge is
\(y=a_s(X)\), \(1\le s\le H\), then compatibility further forces

\[
a(Y)=
(d_1(X),a_1(X),\ldots,a_{s-1}(X),a_{s+1}(X),\ldots,a_H(X)).
\tag{10.9}
\]

If \(y\notin U_H(X)\) comes from the tail, it forces

\[
a(Y)=(d_1(X),a_1(X),\ldots,a_{H-1}(X)).
\tag{10.10}
\]

Thus a proof of the balanced rotor-forest lemma must first make the
deletion-word flow nearly Eulerian,

\[
\Delta_{\rm seq}=o(W/H),
\tag{10.11}
\]

and then satisfy the coupled upper-word constraints (10.9)--(10.10), the
Hall cuts (9.5), and the long-cycle/splicing condition.  This is the exact
local compatibility information absent from parent-rainbow and rankwise
balance.

---

## 11. Exact Eulerian multicover and the single-copy resolution gap

The sequence defect in Section 10 has no fractional or multiplicity-level
obstruction.

For every middle owner \(X\), take all

\[
K_H^-=(m)_H
\tag{11.1}
\]

ordered deletion words of length \(H\) with distinct entries in \(X\).
Regard a word \((d_1,\ldots,d_H)\) as a directed de Bruijn edge

\[
(d_1,\ldots,d_{H-1})
\longrightarrow
(d_2,\ldots,d_H).
\tag{11.2}
\]

### Proposition 11.1 (exact balanced Eulerian deletion multicover)

The resulting labelled directed multigraph is Eulerian.  Every middle
owner label occurs exactly \((m)_H\) times.  At depth \(q\), every
\((m-q)\)-set occurs exactly

\[
\boxed{
(m+q)_q\,(m-q)_{H-q}
=\frac{W(m)_H}{N_q}}
\tag{11.3}
\]

times as the target obtained after the first \(q\) deletions.

#### Proof

Fix an ordered \((H-1)\)-tuple \(\theta\).  The number of deletion words
with prefix \(\theta\) is

\[
(2m-H+1)\binom{2m-H}{m-H}.
\tag{11.4}
\]

Indeed, choose the last deleted coordinate outside \(\theta\), then choose
the other \(m-H\) owner coordinates outside the resulting \(H\)-word.
The same count holds for words with suffix \(\theta\), proving Eulerian
balance.

Fix \(S\) of size \(m-q\).  Choose and order the first \(q\) deleted
coordinates from the \(m+q\) coordinates outside \(S\), then choose and
order the remaining \(H-q\) deleted coordinates inside \(S\).  This gives
the first expression in (11.3); elementary factorial cancellation gives
the second. \(\square\)

Taking independently every ordered upper addition word in the complement
of each owner produces the full state multiplicity

\[
K_H=(m)_H^2.
\tag{11.5}
\]

The canonical tail-entering rotor subgraph on these states is regular and
admits Euler circuits componentwise (indeed it is strongly connected for
\(H\le m-2\)).  Coordinate transitivity gives exactly uniform target
multiplicity at every signed depth.  Thus the complete state multicover
simultaneously has perfect dynamics and perfect coverage.

The remaining operation is an exact resolution of this multicover into
single-owner transversals.  In deletion-word language, one needs to color
the labelled Eulerian edges with \((m)_H\) colors so that

1. every color uses each middle owner exactly once;
2. every color has floor/ceiling depth loads; and
3. at least one color has rotor-forest deficiency \(o(W/H)\).

Equivalently, in the full two-sided state system one asks for a low-switch
resolution of the Euler circulation into \((m)_H^2\) balanced owner
transversals.  Random colorings fail badly: they preserve owner counts but
retain only the negligible compatibility scale in (8.3).  Long interval
colorings preserve dynamics but do not preserve one occurrence of every
owner.

This is the precise single-copy integrality gap left after Proposition
11.1.  It is the rotor analogue of combining the coverage and dynamics
resolutions of the exact multicover theorem.
