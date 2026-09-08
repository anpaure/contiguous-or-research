# Truncated carrier-rotor paths: independent audit and integral attack

Date: 2026-07-25

Pure mathematics only.  No web search, computation, random experiment, or
solver is used.

This note audits
`TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_20260725.md` line by line and then
attacks its open statement \((\mathrm{TRP})\) through the induced regular
rotor graph.

## 0. Verdict

The truncated-carrier reduction is valid after four explicit corrections.

1. Line 31 has the harmless TeX typo `quad` in place of `\quad`.
2. Lines 105--116 state the correct strong-connectivity conclusion, but the
   displayed slot-generation argument is compressed past a proof.  A full
   Schreier-group proof is given in Theorem 2.2 below.
3. Lines 215--239 construct a stationary random **walk**.  If `path` is
   required to mean vertex-simple, that fractional measure is not yet shown
   to be a convex combination of simple length-\(M\) paths.  The literal
   compiler and the sufficient theorem need only directed walks.  Thus the
   clean exact formulation permits repeated states.  The stronger
   simple-path version remains sufficient and is nonempty because the
   truncated cyclic packets are simple examples.
4. Lines 256--263 use the probability \(M/N_q\) at both ranks
   \(m-q\) and \(m+q\).  This is correct for \(q<H\), and at the lower
   endpoint \(m-H\), but not at the upper endpoint \(m+H=M\): a packet
   contains one top, so the probability there is \(1/N_H\).  This does not
   damage the reduction, because the entire top layer has
   \(N_H=(1+o(1))W/m=o(W)\) masks and can be appended literally.  The
   corrected reservoir estimate is Proposition 5.1.

There are two additional notation/wording corrections.

- In line 231, the denominator denoted \(N_r\) is
  \(\binom{2m}{r}\); the file initially defined only the distance notation
  \(N_q=\binom{2m}{m-q}\).
- The two tails in line 282 formally include the empty lower mask at the
  last rank.  It is omitted, since the word is nonzero.  Removing it only
  decreases the displayed bound.

With these changes, the implication

\[
 (\mathrm{TRP})\quad\Longrightarrow\quad \nu(2m)\le W+o(W)
\tag{0.1}
\]

is rigorous.

The graph attack produces five further exact conclusions.

1. The carrier rotor is a regular directed lift of the Johnson graph
   \(J(U,m)\).  Every owner fiber has the same size, and every oriented
   Johnson edge has the same number of state-edge lifts.
2. Carrier walks are exactly radius-\(Q\) resident Johnson walks with a
   future-departure FIFO and a past-departure cache.  Their flags satisfy
   the path-hitting identities
   \[
     L_q(\omega_t)=\bigcap_{i=0}^qX_{t+i},\qquad
     U_q(\omega_t)=\bigcup_{i=0}^qX_{t-i}
   \tag{0.2}
   \]
   after the natural \(Q\)-step boundary padding.
3. A time-expanded unit-flow network has precisely the length-\(M\) rotor
   walks as its extreme points.  Its uniform Markov flow gives the exact
   symmetric fractional point used in the reduction.
4. The determinant-\(2\) cyclic-packet minor remains present, because every
   cyclic packet truncates to a carrier-rotor walk.  Hence the natural
   walk-versus-target output matrix is not TU.
5. Unlike the cyclic catalog, the rotor-walk catalog has exact one-owner
   exchanges.  A two-step arrival diamond changes only one intermediate
   state.  Walk-column differences therefore generate
   \[
      \left\{v\in\mathbb Z^{\binom Um}:\sum_Xv_X=0\right\}
   \tag{0.3}
   \]
   on the owner layer of every carrier.  Thus the determinant-\(2\) minor
   is not a parity or lattice obstruction here.  Its exact full-flag
   counterterm is a vertical string of \(2Q+1\) adjacent target differences,
   one at every controlled rank.

The remaining issue is positivity and simultaneous vertical absorption:
choose applicable diamonds, or longer arrival-permutation blocks, so that
their vertical strings reduce the aggregate target-hole count to \(o(W)\)
without leaving the one-walk-per-carrier polytope.

## 1. Calibration and scale audit: lines 8--41

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
 \qquad \lambda_q={W\over N_q},
\]

and let

\[
 H=\min\{h:\lambda_h\ge m+h\},\qquad M=m+H.
\tag{1.1}
\]

The exact ratio

\[
 {\lambda_{h+1}\over\lambda_h}={m+h+1\over m-h}
\tag{1.2}
\]

and the expansion

\[
 \log\lambda_h={h^2\over m}
 +O\!\left({h\over m}+{h^3\over m^2}\right)
\tag{1.3}
\]

give

\[
 H=(1+o(1))\sqrt{m\log m}.
\tag{1.4}
\]

Writing \(c=\lambda_H/M\), minimality gives \(c=1+O(H/m)\).  Hence

\[
 MN_H={W\over c}=W-o(W),\qquad HN_H=o(W).
\tag{1.5}
\]

Now take

\[
 Q=\left\lceil
 \sqrt{m(\log\log m+\gamma(m))}
 \right\rceil,
 \qquad
 \gamma\to\infty,\quad \gamma=o(\log\log m).
\tag{1.6}
\]

Then

\[
 {Q^2\over H^2}
 =(1+o(1)){\log\log m+\gamma\over\log m}=o(1),
\tag{1.7}
\]

so \(Q=o(H)\).  Also (1.3) applies to \(Q\) and yields

\[
 \lambda_Q
 =\exp(\log\log m+\gamma+o(1))
 =\log m\,e^{\gamma+o(1)}.
\tag{1.8}
\]

Thus lines 8--41 are correct, apart from the TeX typo on line 31.  The
claim that depths beyond \(Q\) are cheap is proved only after the corrected
reservoir calculation in Section 5 below.

## 2. The carrier rotor: lines 43--117

Fix \(U\in\binom{[2m]}M\), and abbreviate

\[
 a=m-Q,\qquad b=H-Q,
\tag{2.1}
\]

so \(a,b\ge2\) for all sufficiently large \(m\).  A state is

\[
 \omega=(L;z_1,\ldots,z_{2Q};R_U),
 \qquad |L|=a,\quad |R_U|=b,
\tag{2.2}
\]

with the displayed blocks partitioning \(U\).  The residual block in the
full state on \([2m]\) is

\[
 R=R_U\cup([2m]\setminus U).
\tag{2.3}
\]

For \(x\in L\) and \(y\in R_U\), the rotor successor is

\[
 \mathcal R_{x,y}(\omega)
 =(L-x+y;x,z_1,\ldots,z_{2Q-1};R_U-y+z_{2Q}).
\tag{2.4}
\]

This is the exact MTF rotor recurrence.  In particular it never moves a
coordinate across the carrier boundary.

### Proposition 2.1 (count and regularity)

The state count and in/outdegree are

\[
 |\Omega_Q(U)|={M!\over a!b!},
 \qquad d=ab=(m-Q)(H-Q).
\tag{2.5}
\]

#### Proof

Choose the unordered \(a\)-set \(L\), then the ordered \(2Q\) singleton
labels; the remaining \(b\) labels form \(R_U\).  This gives (2.5).

There are \(a\) choices for \(x\) and \(b\) for \(y\), and distinct pairs
give distinct successors.  Conversely, from a target
\((L';w_1,\ldots,w_{2Q};R')\), choose the old arrival \(y\in L'\) and the
old tail \(z_{2Q}\in R'\).  Then

\[
 L=L'-y+w_1,\qquad
 R_U=R'-z_{2Q}+y,
\]

and the remaining old queue is forced.  This gives exactly \(ab\)
predecessors. \(\square\)

### Theorem 2.2 (strong connectivity)

The carrier rotor is strongly connected.

#### Proof

Temporarily distinguish the \(a\) slots in \(L\) and the \(b\) slots in
\(R_U\).  Let them be

\[
 A_1,\ldots,A_a,\quad q_1,\ldots,q_{2Q},\quad
 B_1,\ldots,B_b.
\]

A move using \(A_i,B_j\) acts on slot labels by the cycle

\[
 c_{ij}=(A_i,q_1,q_2,\ldots,q_{2Q},B_j).
\tag{2.6}
\]

The actual state space is the Schreier quotient by

\[
 K=S_{\{A_1,\ldots,A_a\}}\times
   S_{\{B_1,\ldots,B_b\}},
\]

because the two end blocks are unordered.

Choose distinct \(A_i,A_{i'}\).  The stabilizer contains
\(\tau=(A_i,A_{i'})\).  Since \(c_{ij}\) fixes \(A_{i'}\),

\[
 c_{ij}\tau c_{ij}^{-1}=(q_1,A_{i'}).
\tag{2.7}
\]

Conjugating (2.7) by powers of \(c_{ij}\) connects \(A_{i'}\) by a
transposition to every queue slot, to \(A_i\), and to \(B_j\).  The two
internal symmetric groups then connect all remaining \(A\)- and \(B\)-slots.
Hence

\[
 \langle K,c_{ij}:i,j\rangle=S_M.
\tag{2.8}
\]

The underlying undirected Schreier graph is therefore connected.  Now use
Proposition 2.1: a finite weakly connected digraph with equal indegree and
outdegree at every vertex has only one strongly connected component.
Indeed, a source component in the condensation has no incoming edges;
degree balance then gives no outgoing edges either, contradicting weak
connectivity unless it is the whole graph.  Thus the directed carrier rotor
is strongly connected. \(\square\)

This supplies the missing detail in lines 105--116.  The conclusion there
is correct.

## 3. Flags, the Johnson quotient, and residence: lines 118--170

The state exposes the chain

\[
 L\subset L+z_1\subset\cdots\subset L+z_1+\cdots+z_{2Q}.
\tag{3.1}
\]

Its owner and radius-\(Q\) flags are

\[
 X(\omega)=L+z_1+\cdots+z_Q,
\tag{3.2}
\]

\[
 L_q(\omega)=L+z_1+\cdots+z_{Q-q},
 \qquad
 U_q(\omega)=L+z_1+\cdots+z_{Q+q}.
\tag{3.3}
\]

They have ranks \(m-q\) and \(m+q\).  Under (2.4),

\[
 X(\mathcal R_{x,y}\omega)=X(\omega)-z_Q+y.
\tag{3.4}
\]

All of lines 118--149 are therefore exact.

### Proposition 3.1 (regular Johnson lift)

Every owner fiber has size

\[
 F=(m)_Q(H)_Q
 ={m!H!\over(m-Q)!(H-Q)!}.
\tag{3.5}
\]

Every oriented Johnson edge

\[
 X\longrightarrow X-a+b,\qquad a\in X,\quad b\in U-X,
\]

has exactly

\[
 {Fd\over mH}
 ={(m-1)!(H-1)!\over
   (m-Q-1)!(H-Q-1)!}
\tag{3.6}
\]

state-edge lifts.

#### Proof

Conditional on the owner \(X\), choose the ordered \(Q\)-tuple
\((z_1,\ldots,z_Q)\) from \(X\), and independently choose the ordered
\(Q\)-tuple \((z_{Q+1},\ldots,z_{2Q})\) from \(U-X\).  This proves
(3.5).

In a uniform state over this fiber, \(z_Q\) is uniform in \(X\).  Averaging
a uniform choice of \(y\in R_U\) over the uniform upper flag makes \(y\)
uniform in \(U-X\).  The choice of \(x\in L\) does not change the next
owner.  Hence every one of the \(mH\) oriented Johnson neighbours receives
the same fraction \(1/(mH)\) of the \(Fd\) outgoing state edges.  The
simplification gives (3.6). \(\square\)

This proves lines 150--167, including the factor \(1/(mH)\).  It also
shows precisely in what sense the carrier rotor is a regular lift rather
than a pointwise graph covering: a single state has only \(H-Q\) possible
next owners, but the whole owner fiber distributes uniformly over all
\(mH\) Johnson arcs.

### Theorem 3.2 (resident Johnson normal form)

Let \((\omega_t)\) be a carrier-rotor walk and write

\[
 X_{t+1}=X_t-d_t+c_t.
\tag{3.7}
\]

At every index with the indicated history present,

\[
 z_i(t)=d_{t+Q-i}\quad(1\le i\le Q),
 \qquad
 z_{Q+j}(t)=d_{t-j}\quad(1\le j\le Q).
\tag{3.8}
\]

Moreover the next injected lower-base element is \(d_{t+Q}\), and

\[
 c_t\notin\{d_{t-1},\ldots,d_{t-Q}\}.
\tag{3.9}
\]

Conversely, a Johnson walk supplied with \(Q\)-step boundary histories and
satisfying

\[
 \begin{array}{ll}
 \mathrm{(F)}&d_t,\ldots,d_{t+Q}\text{ are distinct and lie in }X_t,\\
 \mathrm{(B)}&d_{t-1},\ldots,d_{t-Q}\text{ are distinct and lie outside }X_t,\\
 \mathrm{(R)}&c_t\notin\{d_{t-1},\ldots,d_{t-Q}\}
 \end{array}
\tag{3.10}
\]

lifts uniquely to carrier states once its boundary queues are fixed.
For every \(q\le Q\), its flags obey (0.2).

#### Proof

The target queue in (2.4) is

\[
 (x_t,z_1(t),\ldots,z_{2Q-1}(t)).
\]

Since the owner departure is \(d_t=z_Q(t)\), repeated shifting gives
(3.8), and the new first singleton \(x_t\) becomes the departure
\(d_{t+Q}\).  The membership conditions follow from
\(x_t\in L_t\), while (3.9) is exactly \(c_t=y_t\in R_{U,t}\).

For the converse define

\[
 L_t=X_t-\{d_t,\ldots,d_{t+Q-1}\},
\]

use (3.8) for the ordered singleton queue, and put

\[
 R_{U,t}=U-\left(X_t\cup\{d_{t-1},\ldots,d_{t-Q}\}\right).
\]

Conditions (3.10) make these a valid state partition and make (2.4) hold
with \(x_t=d_{t+Q}\), \(y_t=c_t\).

Finally, intersecting successive owners deletes the distinct future
departures, while taking backward unions adjoins the distinct past
departures.  Thus

\[
 \bigcap_{i=0}^qX_{t+i}
 =X_t-\{d_t,\ldots,d_{t+q-1}\}=L_q(\omega_t),
\]

and the upper identity is dual. \(\square\)

This is the exact up-set path-hitting formulation of the truncated atom.

### Corollary 3.3 (cyclic packets really are rotor walks)

Let \(u_0,\ldots,u_{M-1}\) be a cyclic order of \(U\), and let
\(X_t=I(t,m)\) be its sliding \(m\)-windows.  Then its radius-\(Q\)
truncation is a carrier-rotor cycle.

#### Proof

Put \(d_t=u_t\).  The arrival at step \(t\) is

\[
 c_t=u_{t+m}=d_{t-H}.
\]

Since \(Q<H\), this arrival is outside the last \(Q\) departures, and the
future and past residence conditions (3.10) hold.  Theorem 3.2 supplies the
carrier states and rotor edges. \(\square\)

Thus line 325 is correct, not merely heuristic.

## 4. Literal compilation and fractional loads: lines 172--239

Writing the initial blocks in reverse state order costs \(2Q+2\) nonempty
letters.  Each of the next \(s-1\) rotor edges costs one new nonempty core
letter, so a walk of \(s\) states has literal length

\[
 s+2Q+1.
\tag{4.1}
\]

The MTF recurrence preserves all internal flag witnesses.  With \(s=M\)
and one walk per carrier, the primary length is

\[
 MN_H+(2Q+1)N_H
 =W-o(W)+O(QW/m)=W+o(W).
\tag{4.2}
\]

Thus lines 172--211 are correct for directed walks as well as paths.

Choose the initial state uniformly and each rotor successor uniformly.
Proposition 2.1 makes the transition matrix doubly stochastic, so every
time marginal is uniform.  A uniform state in a fixed carrier has a
uniform rank-\(r\) flag target in \(\binom Ur\).  Therefore a fixed global
rank-\(r\) target has expected primary multiplicity

\[
 \binom{2m-r}{M-r}{M\over\binom Mr}
 ={MN_H\over\binom{2m}{r}}.
\tag{4.3}
\]

This verifies lines 213--235, with the notation correction stated in
Section 0.  Notice that (4.3) is an occurrence-multiplicity identity.  It
does not assert that the \(M\) states of one random walk are distinct.

### Proposition 4.1 (independent walks retain linear owner holes)

If the stationary walk in each carrier is chosen independently, the
expected number of uncovered middle owners is at least

\[
 (e^{-1}-o(1))W.
\tag{4.4}
\]

#### Proof

Let \(C=\binom Mm\).  By coordinate symmetry inside a carrier, the
probability \(p\) that a fixed contained owner is visited at least once is
the same for every owner.  Since one walk visits at most \(M\) distinct
owners,

\[
 Cp\le M.
\tag{4.5}
\]

A fixed global owner belongs to \(K=\binom mH\) carriers.  Independent
carrier choices leave it uncovered with probability

\[
 (1-p)^K\ge\left(1-{M\over C}\right)^K.
\]

The containment identity gives

\[
 K{M\over C}={MN_H\over W}=1-o(1),
\]

while \(M/C=o(1)\).  The right side therefore tends to \(e^{-1}\).
Linearity of expectation proves (4.4). \(\square\)

Thus line 328 is correct as a Poisson-scale lower bound.  Exact Poisson
convergence for rotor walks is neither needed nor proved.

## 5. Corrected reservoir: lines 241--283

Put

\[
 \varepsilon=e^{-\gamma/2},\qquad
 R_{\rm res}=\left\lceil{\varepsilon W\over M}\right\rceil.
\tag{5.1}
\]

Choose these full cyclic packets independently and uniformly from all tops
and cyclic orders.

### Proposition 5.1 (outer-band reservoir)

There is a deterministic reservoir of \(R_{\rm res}\) packets whose total
number of missed masks at distances \(Q<q\le H\) is \(o(W)\), after the
upper top layer is charged separately.  Its literal cost is \(o(W)\).

#### Proof

For \(Q<q<H\), a random full packet contains \(M\) distinct intervals at
each of ranks \(m-q\) and \(m+q\).  At the lower endpoint \(m-H\), it also
contains \(M\) distinct intervals.  Hence the expected misses away from the
upper top endpoint are at most

\[
 2\sum_{q=Q+1}^{H-1}
 N_q\left(1-{M\over N_q}\right)^{R_{\rm res}}
 +N_H\left(1-{M\over N_H}\right)^{R_{\rm res}}.
\tag{5.2}
\]

For every term,

\[
 {R_{\rm res}M\over N_q}
 \ge\varepsilon{W\over N_q}
 \ge\varepsilon\lambda_Q
 =\log m\,e^{\gamma/2+o(1)}.
\tag{5.3}
\]

Using \(1-u\le e^{-u}\), (5.2) is \(o(W)\).

At rank \(m+H=M\), a packet hits only its one top, not \(M\) tops.  We do
not need a probabilistic estimate there: all missed tops together number at
most

\[
 N_H=(1+o(1)){W\over m}=o(W).
\tag{5.4}
\]

The expectation of the total missed outer-band masks is therefore \(o(W)\),
so some deterministic reservoir has that property.

One full packet has literal length \(M+O(H)\).  Consequently

\[
 R_{\rm res}(M+O(H))
 =O(\varepsilon W)+O(M)=o(W).
\tag{5.5}
\]

This proves the proposition. \(\square\)

Finally,

\[
 2\sum_{q>H}N_q=O(W/H)=o(W).
\tag{5.6}
\]

The empty lower mask, if reached by the notation, is simply omitted.  Thus
the conclusion of lines 241--283 is correct after replacing their endpoint
calculation by Proposition 5.1.

## 6. Audit of the sufficient theorem: lines 285--332

Permit a directed walk of \(M\) states in every carrier.  Suppose the
aggregate number of missing targets over the two radius-\(Q\) flag bands is
\(o(W)\), with the middle rank counted once.  Compile the walks using
(4.2), append the deterministic reservoir from Proposition 5.1, append its
remaining missed masks and the corrected tails literally, and concatenate.
Every old contiguous witness remains internal to its component.  Every
letter is nonempty.  Equations (4.2), (5.5), (5.6), and the assumed hole
bound give total length \(W+o(W)\).

Therefore the theorem on lines 285--315 is valid, with `path` interpreted
as `directed walk` or with simple paths retained as a stronger hypothesis.
The one-bit odd-dimensional lift on line 317 is an independent standard
reduction and is not used in the even-dimensional audit.

The claims on lines 321--326 also survive: Corollary 3.3 embeds every
cyclic packet into the truncated catalog, and the converse fails because a
state has \((m-Q)(H-Q)>1\) rotor continuations.  Hence \((\mathrm{TRP})\)
is genuinely weaker than selecting one cyclic order per carrier.

## 7. Exact time-expanded formulation of \((\mathrm{TRP})\)

For each carrier \(U\), form the layered DAG

\[
 \mathcal T_U=\{0,1,\ldots,M-1\}\times\Omega_Q(U),
\tag{7.1}
\]

with an arc

\[
 (t,\omega)\longrightarrow(t+1,\omega')
\]

exactly when \(\omega\to\omega'\) is a rotor edge.  Join a source to every
layer-zero state and every last-layer state to a sink.

### Proposition 7.1 (local path-flow integrality)

The unit-flow polytope \(P(\mathcal T_U)\) is integral, and its extreme
points are precisely the length-\(M\) directed carrier walks.

This is immediate from total unimodularity of a directed incidence matrix.
The product

\[
 \prod_{U\in\binom{[2m]}M}P(\mathcal T_U)
\tag{7.2}
\]

therefore has one walk per carrier at every integral extreme point.

The uniform source distribution and transition probability \(1/d\) give a
feasible fractional unit flow in every \(\mathcal T_U\).  Its target output
is exactly (4.3).

There is also an integral zero-hole point after temporal rotor coupling is
removed.  Apply the lower-bounded Boolean flag flow to send \(M\) paths
from every top through the central band, with every target load equal to
the floor or ceiling of its symmetric load.  Assign the \(M\) resulting
central flag states at each top to the \(M\) time slots arbitrarily.  Thus:

- nested flag balance is integrally feasible;
- length-\(M\) rotor chronology is locally integral;
- their common target-output section is the only unresolved intersection.

To make that last statement exact, for an integral walk family \(\mathcal P\)
define

\[
 \begin{aligned}
 \delta_Q(\mathcal P)
 ={}&\sum_{q=0}^Q
 \left[
  \min\{N_q,S\}-|\{L_q(\omega):\omega\in\mathcal P\}|
 \right]\\
 &+\sum_{q=1}^Q
 \left[
  \min\{N_q,S\}-|\{U_q(\omega):\omega\in\mathcal P\}|
 \right],
 \qquad S=MN_H.
\end{aligned}
\tag{7.3}
\]

The scalar unavoidable hole term is

\[
 B_Q=\sum_{q=0}^Q (N_q-S)_+
     +\sum_{q=1}^Q (N_q-S)_+=o(W).
\tag{7.4}
\]

Indeed \(N_q\ge S\) only for \(q=O(\sqrt H)\), there are
\(O(\sqrt H)\) such ranks, and each deficit is at most
\(W-S=O(WH/m)\).  Hence the exact hard-band hole count is

\[
 B_Q+\delta_Q(\mathcal P).
\tag{7.5}
\]

The uniform fractional time-expanded flow has the zero optimum in the
standard linearized hit-variable relaxation, while an integral point has
objective exactly \(\delta_Q\).  Thus

\[
 (\mathrm{TRP})\quad\Longleftrightarrow\quad
 \min_{\mathcal P\text{ one walk/top}}\delta_Q(\mathcal P)=o(W).
\tag{7.6}
\]

## 8. The determinant-two packet minor persists

The time-expanded network block in Section 7 is TU.  Adjoining its target
output rows destroys that conclusion.

### Theorem 8.1 (inherited non-TU minor)

The walk-versus-owner incidence matrix contains

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad\det=-2.
\tag{8.1}
\]

#### Proof

Choose a common \((m-1)\)-set \(C\), three points \(a,b,c\), and an
\((H-2)\)-set \(F\), giving the top

\[
 U=C\cup F\cup\{a,b,c\}.
\]

There are cyclic orders \(P_{ab},P_{ac},P_{bc}\) for which the corresponding
middle-window packets contain respectively exactly the indicated two of

\[
 X_a=C+a,qquad X_b=C+b,qquad X_c=C+c.
\]

Explicitly, split \(F=F^-\sqcup F^+\) with both parts nonempty.  For a pair
\(\{i,j\}\), put the third point \(k\) in the cyclic order

\[
 i,F^-,k,F^+,j,C.
\]

The complements of \(X_i,X_j\) are cyclic \(H\)-intervals, while the
complement of \(X_k\) is split by \(k\) and by \(C\), hence is not an
interval.

By Corollary 3.3, truncate each cyclic packet to radius \(Q\), cut one edge,
and regard its \(M\) states as a column of the time-expanded walk catalog.
Its middle owner support is unchanged.  The three stated rows and columns
therefore give (8.1). \(\square\)

This proves that ordinary TU still cannot round the common target-output
section.  It does **not** prove an integral obstruction: the enlarged rotor
catalog contains additional columns, and the next section shows that they
destroy the cyclic owner-lattice rigidity.

## 9. Exact rotor diamonds and the saturated owner lattice

Let

\[
 \omega=(L;z_1,\ldots,z_{2Q};R_U).
\]

Choose distinct \(x,x'\in L\) and distinct \(y,y'\in R_U\).  Define

\[
 \omega_y=\mathcal R_{x,y}(\omega),
 \qquad
 \omega_{y'}=\mathcal R_{x,y'}(\omega).
\]

### Theorem 9.1 (two-step arrival diamond)

Both two-step routes

\[
 \omega\xrightarrow{(x,y)}\omega_y
 \xrightarrow{(x',y')}\eta,
\]

\[
 \omega\xrightarrow{(x,y')}\omega_{y'}
 \xrightarrow{(x',y)}\eta
\tag{9.1}
\]

are legal and have the same endpoint

\[
 \eta=
 \left(
 L-\{x,x'\}+\{y,y'\};
 x',x,z_1,\ldots,z_{2Q-2};
 R_U-\{y,y'\}+\{z_{2Q-1},z_{2Q}\}
 \right).
\tag{9.2}
\]

Their state-occurrence columns differ only at the intermediate state.

#### Proof

After the first move, \(x'\) remains in the lower block and the unused
arrival remains in the residual block.  Thus both second moves are legal.
Substitution into (2.4) gives (9.2) on both routes. \(\square\)

Pad both routes by the same continuation to obtain two length-\(M\) walks.
Let \(X=X(\omega)\).  Their owner-incidence difference is exactly

\[
 e_{X-z_Q+y}-e_{X-z_Q+y'}.
\tag{9.3}
\]

### Theorem 9.2 (owner-lattice saturation)

For a fixed carrier \(U\), the integer lattice generated by differences of
equal-length rotor-walk owner columns is

\[
 \boxed{
 \left\{v\in\mathbb Z^{\binom Um}:\sum_Xv_X=0\right\}.}
\tag{9.4}
\]

#### Proof

Every walk column has total owner mass \(M\), so every difference lies in
the right side.

Conversely, take adjacent owners

\[
 Y=A+y,qquad Y'=A+y',qquad |A|=m-1.
\]

Choose

\[
 z\in U-(A\cup\{y,y'\}),qquad X=A+z.
\]

Because \(H-Q\ge2\), construct a state over \(X\) with \(z_Q=z\) and with
\(y,y'\in R_U\).  Because \(m-Q\ge2\), choose distinct \(x,x'\in L\).
Theorem 9.1 then realizes

\[
 e_Y-e_{Y'}
\]

as a difference of two length-\(M\) walk columns.  Adjacent differences
generate the complete zero-sum integer lattice because the Johnson graph
\(J(U,m)\) is connected. \(\square\)

This is the sharp contrast with cyclic packets.  Every cyclic packet has
coordinate point-margin exactly \(m\), so replacing one owner by another
cannot remain a cyclic packet.  The rotor catalog permits that replacement
by an exact local diamond.  Hence the determinant \(-2\) in (8.1) merely
certifies failure of the natural TU matrix; it is not an owner-layer parity,
congruence, or saturation obstruction.

### Proposition 9.3 (the exact vertical counterterm)

Let \(C_Q(\omega)\) be the incidence vector of all \(2Q+1\) controlled
targets in a state, with the owner counted once.  In the diamond above,

\[
 C_Q(\omega_y)-C_Q(\omega_{y'})
 =\sum_{q=0}^Q
   (e_{K_q^-+y}-e_{K_q^-+y'})
  +\sum_{q=1}^Q
   (e_{K_q^++y}-e_{K_q^++y'}),
\tag{9.5}
\]

where

\[
 K_Q^-=L-x,
\]

\[
 K_q^-=L+z_1+\cdots+z_{Q-q-1}\quad(0\le q<Q),
\tag{9.6}
\]

and

\[
 K_q^+=L+z_1+\cdots+z_{Q+q-1}\quad(0\le q\le Q).
\tag{9.7}
\]

The two \(q=0\) cores agree, so that term is counted once in (9.5).

#### Proof

The intermediate state on the first route is

\[
 \omega_y=(L-x+y;x,z_1,\ldots,z_{2Q-1};R_U-y+z_{2Q}).
\]

Insert this state into the definitions of \(L_q\) and \(U_q\).  At every
rank its target has the form displayed in (9.5)--(9.7), with \(y\) as the
last coordinate.  Replacing the first arrival by \(y'\) changes no other
coordinate. \(\square\)

Thus a diamond gives a unit owner correction, but necessarily transports
that correction through an entire nested flag column.  This vertical string
is the exact discrepancy left after owner-lattice saturation.

### Theorem 9.4 (rank-isolated rectangles and the diagonal margin invariant)

For every interior controlled rank

\[
 m-Q+1\le r\le m+Q-1,
\tag{9.8}
\]

integer combinations of rotor diamonds realize every elementary
rank-\(r\) rectangle

\[
 e_{K+a+y}+e_{K+b+y'}
 -e_{K+a+y'}-e_{K+b+y},
 \qquad |K|=r-2,
\tag{9.9}
\]

with four distinct displayed labels outside \(K\), while having zero effect
at every other controlled rank.  Consequently their rank-\(r\) projection
contains

\[
 \ker_{\mathbb Z}A_r^U,
\tag{9.10}
\]

where \(A_r^U\) is the point-versus-\(r\)-set incidence matrix on \(U\).

On the other hand, if \(\Delta=(\Delta_r)\) is any integer sum of diamond
vertical strings, then

\[
 A_r^U\Delta_r=g
\tag{9.11}
\]

is the same point-margin vector \(g\in\mathbb Z^U\) at every controlled
rank.  Thus diamonds alone have an exact diagonal cross-rank point-margin
invariant.

#### Proof

The cores in (9.6)--(9.7), read from bottom to top, form an arbitrary
saturated chain

\[
 K_{m-Q-1}\subset K_{m-Q}\subset\cdots\subset K_{m+Q-1}
\tag{9.12}
\]

inside \(U-\{y,y'\}\): its first increment is \(x\), followed by
\(z_1,\ldots,z_{2Q-1}\).  Conversely, every such core chain extends to a
valid diamond source because \(H-Q\ge2\).

Choose two core chains which agree except that two adjacent increments
\(a,b\) are interchanged.  They differ at exactly one core rank, where the
two cores are \(K+a\) and \(K+b\).  Subtracting their vertical strings
cancels every target rank except rank \(r=|K|+2\), and the surviving
effect is (9.9).  The range (9.8) is exactly the range in which the swapped
pair can be placed among the \(2Q\) core-chain increments.

Elementary rectangles generate \(\ker_{\mathbb Z}A_r^U\): one may eliminate
all sets containing a fixed coordinate by Johnson-adjacent differences,
using a rectangle to realize each difference, and then induct on
\(|U|\).  This proves (9.10).

For the invariant, every rank component of one vertical string is

\[
 e_{K_r+y}-e_{K_r+y'}.
\]

Applying point incidence gives \(e_y-e_{y'}\), independently of \(r\).
Summing strings proves (9.11). \(\square\)

The two boundary ranks \(m-Q\) and \(m+Q\) together contain only

\[
 2N_Q={2W\over\lambda_Q}
 ={2W\over \log m\,e^{\gamma+o(1)}}=o(W)
\tag{9.13}
\]

masks, so they may be appended literally if a rank-isolating absorber is
used only on the interior.  Theorem 9.4 therefore removes all interior
point-balanced lattice discrepancy.  What it does not remove is the
rank-to-rank variation of point margins, nor does an algebraic combination
guarantee that all negative walk columns are present in a chosen
one-walk-per-carrier family.

## 10. Factorially many common-endpoint path variants

The two-step diamond extends to long permutation blocks.

### Theorem 10.1 (arrival-permutation block)

Fix a state \(\omega=(L;z_1,\ldots,z_{2Q};R_U)\).  Choose distinct

\[
 x_0,\ldots,x_{\ell-1}\in L,\qquad
 y_0,\ldots,y_{\ell-1}\in R_U,
 \qquad \ell\le\min\{m-Q,H-Q\}.
\tag{10.1}
\]

For every permutation \(\sigma\in S_\ell\), execute \(\ell\) rotor moves,
using departure \(x_i\) and arrival \(y_{\sigma(i)}\) at time \(i\).
Every such segment is legal, and all \(\ell!\) segments have the same two
endpoints.

#### Proof

At time \(i\), the unused initial lower element \(x_i\) has not been
removed, so it is still in the current lower block.  Likewise the unused
initial residual element \(y_{\sigma(i)}\) is still in the current residual
block.  Thus every move is legal.

After \(\ell\) moves, the lower block is

\[
 L-\{x_0,\ldots,x_{\ell-1}\}
 +\{y_0,\ldots,y_{\ell-1}\},
\]

independent of \(\sigma\).  The ordered queue depends only on the fixed
departure order \(x_0,\ldots,x_{\ell-1}\), and the residual block loses the
same arrival set and gains the same evicted queue set.  Hence the endpoint
is independent of \(\sigma\). \(\square\)

Take \(\ell=H-Q\).  Consecutive such blocks can be prescribed recursively,
because the common endpoint of one block is independent of its internal
permutation.  A length-\(M\) carrier walk can therefore be built with

\[
 g=\left\lfloor{M-1\over H-Q}\right\rfloor
\tag{10.2}
\]

independent permutation blocks and a deterministic remainder.  This gives

\[
 ((H-Q)!)^g
 =\exp((1+o(1))M\log H)
\tag{10.3}
\]

walk variants with the same block-boundary states.

Adjacent transpositions inside these blocks are exactly the diamonds of
Theorem 9.1.  This supplies exponentially many owner-changing integral
directions while retaining one literal path and one initialization per
carrier.  It is the concrete dynamic flexibility absent from a cyclic
packet, whose complete owner support determines its cyclic order up to
reversal.

There is also a useful density statement.  In a uniform rotor walk, a pair
of consecutive moves is an arrival diamond whenever the second departure
is one of the \(m-Q-1\) untouched old lower elements and the second arrival
is one of the \(H-Q-1\) untouched old residual elements.  Its probability is

\[
 \left(1-{1\over m-Q}\right)
 \left(1-{1\over H-Q}\right)=1-o(1).
\tag{10.4}
\]

Partitioning the moves into disjoint consecutive pairs and averaging shows
that some length-\(M\) walk has

\[
 {M\over2}-o(M)
\tag{10.5}
\]

independently switchable diamond blocks.

## 11. Exact remaining integral gate

The graph audit separates three levels.

1. **Uncoupled nested flags.**  A lower-bounded Boolean network gives an
   integral zero-excess-hole solution.
2. **Local chronology.**  The time-expanded carrier network is TU and its
   extreme points are literal rotor walks.
3. **Common target outputs.**  Their intersection is not TU by Theorem 8.1.
   Nevertheless its owner projection has the saturated lattice (9.4), and
   every owner unit move is available through a vertical flag string (9.5).
   Differences of strings generate the full point-balanced rectangle
   lattice separately at every interior rank, but all diamond corrections
   obey the diagonal point-margin law (9.11).

A concrete restricted attack on \((\mathrm{TRP})\) is therefore:

> **Permutation-block TRP.**  Prescribe in every carrier a sequence of the
> common-endpoint blocks of Theorem 10.1.  Choose one arrival permutation in
> every block so that the integral walk family has
> \(\delta_Q=o(W)\), with \(\delta_Q\) defined in (7.3).

This is a genuine product of integral Boolean-lattice path choices, not a
cyclic-order catalog.  It retains one initialization per carrier and has
\(\exp(\Theta(M\log H))\) local choices.  Proving its near-cover property
would prove \((\mathrm{TRP})\).

What is proved here is the exact algebraic improvement over cyclic packets:

\[
 \boxed{
 \text{cyclic determinant-2/no-exchange obstruction}
 \quad\longrightarrow\quad
 \text{rotor unit owner exchanges with vertical counterterm}.}
\tag{11.1}
\]

What is not proved is the positive simultaneous absorption of those
vertical counterterms, including their cross-rank point margins.  That,
rather than total unimodularity, owner-layer lattice saturation, strong
connectivity, or path abundance, is the exact remaining integral problem.

## 12. Cross-carrier second coboundary

The local vertical-counterterm issue is sharpened in
MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md.

Take two arrival diamonds whose saturated base chains differ by one adjacent
increment.  The difference of their vertical strings cancels at every rank
except the rank of that increment swap, where one elementary rectangle
remains.  Giving the two diamond pairs distinct carrier tags turns the
signed four-column identity into a positive two-carrier switch with one
path per carrier on each side and no extra letters.

A paired-swap conveyor repeats this construction for
\(M/2-o(M)\) independent two-step blocks per carrier pair in the controlled
band.  Thus local chronology and coefficient-scale hard-band direction
capacity are no longer open.  The remaining integral problem is the global
one: choose these paired walks so their complete flag supports have
\(\delta_Q=o(W)\).  Prefixes above the truncated collar also require a
separate refined-tail audit if they are to be included in a full-load
kernel.

This last paired-walk gate is now refuted by
MATH_AUDIT_PAIRED_DIAMOND_DUPLICATION_AND_EIGHT_TEMPLATE_20260725.md.
The two carrier sources have the same middle owner at all but one useful
block per collar sweep, forcing \(M/2-o(M)\) equal-owner pairs per carrier
pair and \(W/4-o(W)\) middle collision excess globally.

The local successor uses four diamond edges around a Johnson 4-cycle,
hence eight path templates in four carriers.  Perturbing one edge chain
leaves one rank rectangle while both configurations have distinct source,
intermediate, and endpoint owners.  Its coefficient-scale chronological
packing and global near-cover remain open.
