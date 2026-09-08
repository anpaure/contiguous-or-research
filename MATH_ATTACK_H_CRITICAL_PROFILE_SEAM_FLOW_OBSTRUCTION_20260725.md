# Critical pair-profile seams: exact crossing fans, common-owner flow, and two sharp obstructions

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, or web input is
used.

## 0. Verdict

The componentwise implication

> length-\(\Theta(H)\) blocks whose pair-status profile changes at every
> seam have enough crossing windows to give total defect \(o(W)\)

is false with only those hypotheses: a positive-mass subsystem can satisfy
them while its seam colors miss a macroscopic shoulder.  This does not
rule out a specially coordinated full \(W\)-owner construction whose
remaining seam types repair that shoulder.  What is true is an exact
literal crossing-fan theorem and an exact common-owner capacitated-flow
criterion.

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  The results proved below are as follows.

1. An \(H\)-clean seam contributes exactly \(q\), not \(q+1\), crossing
   windows at depth \(q\).  Their lower and upper targets have explicit
   prefix--suffix formulas.  Under a strong two-sided collar these targets
   form two \(q\)-vertex Johnson paths, simultaneously for every
   \(q\le H\).

2. For an \(FE\leftrightarrow SS\) pair-profile seam, every crossing lower
   target lies on the shoulder

   \[
    (A\text{ singleton},B\text{ empty}),
   \]

   and every crossing upper target lies on

   \[
    (A\text{ full},B\text{ singleton}).
   \]

   Within a subsystem using this fixed seam type, the opposite shoulders
   have no crossing neighbor and each contains
   \(\Theta_A(W)\) targets.  There is a literal positive-mass braid with
   \(\Theta(W/H)\) such profile-changing seams and blocks of length
   \(2H+2\).  Thus critical seam density and local profile change alone do
   not imply profile coverage componentwise.

3. More sharply, for every fixed residual capacity \(B\) and
   \(q\ge2B+1\), there are \(B+1\) pairwise middle-disjoint literal
   two-block paths, all with a genuine \(FE\to SS\) seam, for which the
   central \(q-2B\) lower/upper crossing-target pairs coincide with
   multiplicity \(B+1\).  Their common-owner capacity defect is at least
   \(q-2B\).

4. For a fixed chronology, the crossing windows form a bipartite
   multigraph from lower to upper targets.  The maximum number fitting both
   residual quota marginals is an ordinary integral capacitated flow.  If
   \(\tau_q\) is the number of crossing edges rejected by this flow and
   \(E_q^-+E_q^+\) is the pre-existing internal overquota mass, then the
   final two-sided overload is trapped exactly up to a factor two:

   \[
   E_q^-+E_q^++\tau_q
   \le O_q^-+O_q^+
   \le E_q^-+E_q^++2\tau_q.
   \]

On a fixed Gaussian window all balanced capacities are bounded by a
constant depending only on \(A\).  Hence a factor-specific, two-sided
sufficient gate is an aggregate \(o(W)\) bound for the displayed flow
deficiency.  No theorem presently establishes that bound for one exact
wreath factor and one common literal chronology.  Consequently this
report does not prove constant one.

## 1. Profiles and clean seams

Fix a partition

\[
 [2m+1]=P_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_m
 \mathbin{\dot\cup}\{z\},
 \qquad |P_i|=2.
\tag{1.1}
\]

For an \(m\)-set \(X\), let

\[
 \pi(X)=(F(X),E(X),R(X),\delta(X))
\tag{1.2}
\]

be its pair-status profile: a pair index belongs to \(F,E,R\) when the
pair is respectively full, empty, or singleton in \(X\), and
\(\delta(X)=1_{z\in X}\).

Let

\[
 \cdots,V_{-2},V_{-1},V_0,V_1,V_2,\cdots
\tag{1.3}
\]

be a Johnson path, so consecutive sets have size \(m\) and differ by one
exchange.  The distinguished seam is

\[
 V_1=V_0-\{d\}+\{a\}.
\tag{1.4}
\]

Index the preceding transitions from the seam outward by

\[
 V_{-i}\longrightarrow V_{-i+1}
 =V_{-i}-\{p_i\}+\{s_i\},
 \qquad i\ge1,
\tag{1.5}
\]

and the following transitions by

\[
 V_j\longrightarrow V_{j+1}
 =V_j-\{t_j\}+\{u_j\},
 \qquad j\ge1.
\tag{1.6}
\]

The seam has a **strong two-sided \(H\)-collar** when all coordinates
occurring in

\[
 \{p_i,s_i:1\le i\le H-1\}
 \cup\{d,a\}
 \cup\{t_j,u_j:1\le j\le H-1\}
\tag{1.7}
\]

are pairwise distinct.  In a constant-profile block, an internal
transition exchanges the two elements of one singleton pair.  In that
setting it is enough that the left and right collar directions are all
distinct and avoid the seam pairs.

The strong collar is slightly stronger than saying that every individual
length-\(H\) interval is geodesic.  That distinction matters for proving
that the different splits of one fan have distinct colors.

## 2. The exact crossing-fan theorem

### Theorem 2.1 -- literal prefix--suffix formulas

Assume (1.4) has a strong two-sided \(H\)-collar.  Fix
\(1\le q\le H\).  For \(0\le r\le q-1\), put

\[
 s=q-1-r.
\tag{2.1}
\]

The unique depth-\(q\) window which uses \(r\) transitions before the
seam, the seam itself, and \(s\) transitions after it is

\[
 V_{-r},V_{-r+1},\ldots,V_0,V_1,\ldots,V_{s+1}.
\tag{2.2}
\]

Its exact lower and upper targets are

\[
\boxed{
 L_{q,r}
 =V_0\setminus
 \bigl(
   \{s_1,\ldots,s_r\}\cup\{d\}
   \cup\{t_1,\ldots,t_s\}
 \bigr),
}
\tag{2.3}
\]

\[
\boxed{
 U_{q,r}
 =V_0\cup
 \bigl(
   \{p_1,\ldots,p_r\}\cup\{a\}
   \cup\{u_1,\ldots,u_s\}
 \bigr).
}
\tag{2.4}
\]

In particular,

\[
 |L_{q,r}|=m-q,
 \qquad |U_{q,r}|=m+q.
\tag{2.5}
\]

For fixed \(q\), the \(q\) lower targets in (2.3) are pairwise distinct,
and so are the \(q\) upper targets in (2.4).

#### Proof

A coordinate added on the left at transition \(-i\) is absent from the
earlier states of (2.2), so every \(s_i\) is absent from the intersection.
The seam departure \(d\) and every right departure \(t_j\) are absent from
later states.  Every other coordinate of \(V_0\) persists throughout the
window.  This proves (2.3).

Dually, every left departure \(p_i\) occurs in an earlier state, the seam
arrival \(a\) occurs in later states, and every right arrival \(u_j\)
occurs in a later state.  No other coordinate outside \(V_0\) occurs.
This proves (2.4).  Pairwise distinctness in (1.7) gives (2.5).

When \(r\) is increased to \(r+1\), the deletion set in (2.3) loses
\(t_{q-1-r}\) and gains \(s_{r+1}\).  The two coordinates are distinct.
More intrinsically, the deletion set contains exactly \(r\) coordinates
from the left-arrival collar and \(q-1-r\) from the right-departure
collar.  Hence different values of \(r\) give different deletion sets.
The same argument applied to (2.4) proves upper distinctness.  Finally,
intersection and union of consecutive middle owners are literal lower and
upper contiguous-OR flags in the standard MTF/Pascal lift.  \(\square\)

### Corollary 2.2 -- exact seam census

Suppose a path is divided into blocks having at least \(H\) middle states,
and let \(J\) internal block boundaries be fused by legal seams.  Then a
depth-\(q\) window with \(q\le H\) crosses at most one seam, and the exact
number of seam-crossing windows is

\[
\boxed{K_q=qJ.}
\tag{2.6}
\]

Thus \(J=\Theta(W/H)\) supplies \(\Theta(W)\) crossing occurrences only
at depths \(q=\Theta(H)\).  At \(q=o(H)\), it supplies only \(o(W)\)
occurrences.

#### Proof

The two seam transitions around one block are separated by at least the
number of states in that block.  Hence no \(q\)-transition interval meets
two seams.  At one internal seam, the start can occupy exactly the \(q\)
positions indexed by \(r=0,\ldots,q-1\) in Theorem 2.1.  Summing over
seams proves (2.6).  \(\square\)

## 3. Exact pair-status signatures

Assume first that the seam does not involve \(z\).  Let \(A\) be the pair
of the departure \(d\), let \(B\) be the pair of the arrival \(a\), and
write \(\bar d\), \(\bar a\) for their mates.  If \(A=B\), the seam only
reverses a singleton orientation and the pair-status profile does not
change.  If \(A\ne B\), the four possibilities are exhaustive:

\[
\begin{array}{c|c|c}
\text{middle profile transition}
 & (L_A,L_B)&(U_A,U_B)\\ \hline
(F,E)\to(R_{\bar d},R_a)
 &(R_{\bar d},E)&(F,R_a)\\
(F,R_{\bar a})\to(R_{\bar d},F)
 &(R_{\bar d},R_{\bar a})&(F,F)\\
(R_d,E)\to(E,R_a)
 &(E,E)&(R_d,R_a)\\
(R_d,R_{\bar a})\to(E,F)
 &(E,R_{\bar a})&(R_d,F).
\end{array}
\tag{3.1}
\]

Every internal collar direction is empty in \(L_{q,r}\) and full in
\(U_{q,r}\).  Every untouched pair has the same status and orientation in
both targets.  If \(z\) is exchanged, then \(z\) is absent from the lower
target and present in the upper target, while the affected ordinary pair
contributes one of the half-statuses \(E\to R\) or \(R\to F\).  This gives
the exhaustive four additional cases involving the unpaired coordinate.

The most important specialization is the first row of (3.1).

### Proposition 3.1 -- the \(FE\leftrightarrow SS\) fan

Let the source packet have profile \((F,E,R,\delta)\), with
\(|F|=f,|E|=e,|R|=r\).  Choose \(A\in F\), \(B\in E\), remove
\(a\in P_A\), and add \(b\in P_B\).  Suppose the other \(q-1\) collar
transitions flip a set \(D\in\binom R{q-1}\) of old-active directions.
If \(\sigma\) is the fixed orientation on \(R\setminus D\), then

\[
\boxed{
 L=P(F\setminus\{A\})
   \cup\{\bar a\}
   \cup\sigma(R\setminus D)
   \cup Z_\delta,
}
\tag{3.2}
\]

\[
\boxed{
 U=P(F\cup D)
   \cup\{b\}
   \cup\sigma(R\setminus D)
   \cup Z_\delta.
}
\tag{3.3}
\]

Their pair-status profiles are respectively

\[
\boxed{(f-1,e+q-1,r-q+2,\delta)}
\tag{3.4}
\]

and

\[
\boxed{(f+q-1,e-1,r-q+2,\delta).}
\tag{3.5}
\]

The inverse \(SS\to FE\) seam has the same lower/upper target signature.

#### Proof

Every pair in \(F\setminus\{A\}\) remains full.  Pair \(A\) contributes
only \(\bar a\) to the intersection but is full in the union.  Pair \(B\)
is empty in the intersection and contributes only \(b\) to the union.
Every flipped direction in \(D\) is empty in the intersection and full in
the union, while every unflipped active direction retains its fixed
orientation.  This proves (3.2)--(3.3).  Counting full, empty, and
singleton pairs gives (3.4)--(3.5).  Intersection and union do not depend
on the direction in which the seam is traversed.  \(\square\)

### Corollary 3.2 -- macroscopic empty shoulders

For fixed seam pairs \(A,B\), no \(FE\leftrightarrow SS\) crossing lower
target lies in the shoulder

\[
 A\text{ empty},\qquad B\text{ singleton},
\tag{3.6}
\]

and no crossing upper target lies in

\[
 A\text{ singleton},\qquad B\text{ full}.
\tag{3.7}
\]

The exact sizes of these two forbidden shoulders are

\[
\boxed{
 2\binom{2m-3}{m-q-1}
}
\tag{3.8}
\]

and

\[
\boxed{
 2\binom{2m-3}{m+q-3}.
}
\tag{3.9}
\]

Uniformly for \(q\le A\sqrt m\), both are \(\Theta_A(W)\).

#### Proof

Equations (3.6)--(3.7) are opposite to the special statuses in the first
row of (3.1).  For (3.8), choose the singleton element of \(B\) in two
ways and then choose the remaining \(m-q-1\) elements outside
\(A\cup B\).  The upper count is identical after forcing both elements of
\(B\) and one of the two elements of \(A\).  Central-binomial ratios are
bounded above and below by positive constants depending only on \(A\)
throughout the fixed Gaussian window.  \(\square\)

The crude profile-class Hall cut is already useful.  If
\(h_{q,\rho}^\pm\) targets of signed profile \(\rho\) remain demanded by
block interiors, and \(s_\theta\) selected seams have central type
\(\theta\), then

\[
 M_{\rm profile}
 \ge
 \sum_{q,\rho,\pm}
 \left(
 h_{q,\rho}^\pm
 -q\sum_{\theta:\rho_q^\pm(\theta)=\rho}s_\theta
 \right)_+.
\tag{3.10}
\]

It ignores all target repetitions, so it is weaker than the exact flow
criterion below.

## 4. The exact common-owner Hall/flow criterion

Fix one already integral literal chronology and one depth \(q\).  Let
\(\mathcal L_q\) and \(\mathcal U_q\) be the lower and upper target sets.
Let \(\alpha_q^-\) and \(\alpha_q^+\) be the load vectors contributed by
all windows internal to blocks.  Every crossing window is one edge

\[
 e=(L_e,U_e)
\tag{4.1}
\]

of a bipartite multigraph

\[
 G_q\subseteq\mathcal L_q\times\mathcal U_q.
\tag{4.2}
\]

The edge, rather than its two endpoints separately, is the physical owner
of the crossing interval.  Keeping edges intact is exactly the required
lower/upper common ownership.

Let \(\beta_q^\pm\) be any prescribed integral quota vectors.  In the
fixed-window overload application they range over the exact balanced
floor/ceiling quotas.  Put

\[
 E_q^\pm
 =\sum_T(\alpha_q^\pm(T)-\beta_q^\pm(T))_+,
\tag{4.3}
\]

and define the residual capacities

\[
 d_q^\pm(T)
 =(\beta_q^\pm(T)-\alpha_q^\pm(T))_+.
\tag{4.4}
\]

Let \(\nu_q\) be the maximum number of edges in a subgraph
\(F\subseteq G_q\) satisfying

\[
 \deg_F(T)\le d_q^\pm(T)
\tag{4.5}
\]

at every lower and upper target.  Write

\[
 K_q=|E(G_q)|,
 \qquad \tau_q=K_q-\nu_q.
\tag{4.6}
\]

Thus \(\tau_q\) is the minimum number of whole crossing windows which
must be rejected before both residual marginals fit.

### Theorem 4.1 -- exact capacitated cut formula

Let \(e_q(X,Y)\) denote the number of crossing edges from
\(X\subseteq\mathcal L_q\) to \(Y\subseteq\mathcal U_q\).  Then

\[
\boxed{
 \nu_q
 =\min_{\substack{X\subseteq\mathcal L_q\\Y\subseteq\mathcal U_q}}
 \left[
 d_q^-(\mathcal L_q\setminus X)
 +e_q(X,\mathcal U_q\setminus Y)
 +d_q^+(Y)
 \right].
}
\tag{4.7}
\]

Equivalently,

\[
\boxed{
 \tau_q
 =\max_{X,Y}
 \left[
 K_q-d_q^-(\mathcal L_q\setminus X)
 -e_q(X,\mathcal U_q\setminus Y)-d_q^+(Y)
 \right].
}
\tag{4.8}
\]

All optimizing subgraphs are integral.

#### Proof

Create a network with a source joined to each lower target \(L\) by an arc
of capacity \(d_q^-(L)\), one unit-capacity arc for every parallel edge of
\(G_q\), and an arc from each upper target \(U\) to the sink of capacity
\(d_q^+(U)\).  Integral flows are exactly the subgraphs satisfying (4.5).

A cut whose source side contains \(X\subseteq\mathcal L_q\) and
\(Y\subseteq\mathcal U_q\) has capacity

\[
 d_q^-(\mathcal L_q\setminus X)
 +e_q(X,\mathcal U_q\setminus Y)
 +d_q^+(Y).
\]

Max-flow/min-cut proves (4.7); subtracting from \(K_q\) gives (4.8).
All capacities are integral, so a maximum flow may be taken integral.
\(\square\)

### Theorem 4.2 -- exact comparison with final overload

After all crossing windows are restored, define

\[
 O_q^\pm
 =\sum_T
 \bigl(
  \alpha_q^\pm(T)+\deg_{G_q}(T)-\beta_q^\pm(T)
 \bigr)_+.
\tag{4.9}
\]

Then

\[
\boxed{
 E_q^-+E_q^++\tau_q
 \le O_q^-+O_q^+
 \le E_q^-+E_q^++2\tau_q.
}
\tag{4.10}
\]

#### Proof

For one target, with \(x=\deg_{G_q}(T)\), the scalar identity

\[
 (\alpha+x-\beta)_+
 =(\alpha-\beta)_+
 +\bigl(x-(\beta-\alpha)_+\bigr)_+
\tag{4.11}
\]

gives

\[
 O_q^-+O_q^+
 =E_q^-+E_q^+
 +\sum_{v\in V(G_q)}(\deg_{G_q}(v)-d_q(v))_+.
\tag{4.12}
\]

Call the last sum \(S_q\).  Deleting one edge decreases \(S_q\) by at
most two.  Since at least \(\tau_q\) edges must be deleted to make every
degree fit, this gives \(S_q\le2\tau_q\).

Conversely, while an overloaded vertex remains, delete an incident edge.
Each deletion lowers \(S_q\) by at least one, so at most \(S_q\) deletions
produce a feasible subgraph.  Hence \(\tau_q\le S_q\).  Substitution in
(4.12) proves (4.10).  \(\square\)

For the exact balanced quota class, define

\[
 \mathfrak D_q
 =\min_{\beta_q^-,\beta_q^+}
 \bigl(E_q^-+E_q^++\tau_q\bigr),
\tag{4.13}
\]

and let \(O_q\) be the minimum, over the same quota class, of
\(\max\{O_q^-,O_q^+\}\).  Since the maximum of two nonnegative numbers
lies between half their sum and their sum, (4.10) gives

\[
\boxed{
 \frac12\mathfrak D_q\le O_q\le2\mathfrak D_q.
}
\tag{4.14}
\]

On every fixed Gaussian window, the lower and upper floor capacities
\(c_q^-\) and \(c_q^+\) all lie between \(1\) and a constant \(C_A\).
Let \(c_q\) denote any one of these audited denominators (equivalently,
their minimum or maximum; all choices are constant-comparable).  Therefore

\[
\boxed{
 \sum_{q\le H}\frac{O_q}{c_q}=o(W)
 \quad\Longleftrightarrow\quad
 \sum_{q\le H}\mathfrak D_q=o(W),
}
\tag{4.15}
\]

up to constants depending only on \(A\).  This is exact for the two-sided
seam objective defined here.  Since it controls the relevant one-sided
overload in particular, it is a stronger sufficient fixed-window criterion
for the audited MWB route when the chronology comes from one exact wreath
factor and all nonseam terms are already \(o(W)\).  It is not being called
an equivalent reformulation of the brief's one-sided \(GW\), nor of the
labelled theorem \(CA_A\).

The flow subgraphs at different depths are only analytic certificates for
one fixed chronology.  They are not separate factors, separate seam
choices, or a labelled nested resolution.  In particular, (4.15) does not
by itself prove the stronger labelled statement \(CA_A\).

There is also a topology charge.  Cutting one fully productive seam cycle
removes at most \(q\) crossing windows at each signed depth \(q\), hence at
most

\[
 2\sum_{q=1}^Hq=H(H+1)
\tag{4.16}
\]

credited windows.  Thus \(C H^2=o(W)\) is a safe sufficient condition for
linearizing \(C\) seam cycles without spoiling an \(o(W)\) aggregate
defect estimate.  The weaker reset condition \(CH=o(W)\) alone does not
control lost crossing colors.

### 4.3 One common seam selection

The preceding max flows evaluate a chronology after its seams and ports
have been fixed.  The selection-level statement can also be written
exactly.  Let \(\Omega_{\rm seam}\) be the finite set of integral legal
two-port path factors on the proposed block family.  Thus an element
\(x\in\Omega_{\rm seam}\) fixes one incoming and one outgoing port where
required, satisfies the block indegree/outdegree constraints, and uses one
common seam choice at every depth.  Let \(G_q(x)\),
\(\mathfrak D_q(x)\), and \(C(x)\) be its crossing graph, flow defect, and
number of productive seam cycles which must be cut.  A safe exact
sufficient criterion within this architecture is

\[
\boxed{
 \min_{x\in\Omega_{\rm seam}}
 \left[
 H(H+1)C(x)+\sum_{q\le H}\mathfrak D_q(x)
 \right]=o(W).
}
\tag{4.17}
\]

If the colors actually lost at cycle cuts are entered instead of the safe
upper bound \(H(H+1)C(x)\), the resulting optimization is an exact
necessary-and-sufficient defect criterion for the fixed block
architecture.

Ordinary Hall at each depth does not prove that one integral
\(x\) exists.  The obstruction is already visible in the abstract
four-column incidence matrix

\[
 M=
 \begin{pmatrix}
 1&1&0&0\\
 0&0&1&1\\
 1&0&1&0\\
 1&0&0&1
 \end{pmatrix},
 \qquad |\det M|=2.
\tag{4.18}
\]

The vector with every coordinate \(1/2\) satisfies \(Mx=\mathbf1\),
whereas the four equations force \(x_1=1/2\) and have no integral
solution.  The first two rows may be read as the two local seam choices
and the last two as two nested target marginals.  Each marginal subsystem
is integrally feasible, but the combined system is not.  This is an
abstract warning, not a claimed subconfiguration of a particular exact
factor.  A genuine network-flow proof for selecting \(x\) would require a
rectangular safe-gate property: two partial chronologies meeting the same
gate could be recombined without changing any physical collar or target
color.  No such property is currently proved for the critical blocks.

## 5. A positive-density shoulder obstruction at the critical scale

The empty shoulders in Corollary 3.2 occur in a genuine critical-block
literal braid, not only in one isolated seam.

Fix pair indices \(A,B\), elements \(a\in P_A\), \(b\in P_B\), and keep
the unpaired coordinate \(z\) present.  On the remaining \(m-2\) pairs,
fix a base profile \((F_0,E_0,R)\) satisfying

\[
 2|F_0|+|R|=m-3,
 \qquad s=|R|.
\tag{5.1}
\]

There are two relevant packets:

\[
 \mathcal P_0:
 A\text{ full},\ B\text{ empty},\ z\text{ present},
\tag{5.2}
\]

and the fixed special-orientation layer

\[
 \mathcal P_1:
 A\cap X=\{\bar a\},\ B\cap X=\{b\},\ z\text{ present}.
\tag{5.3}
\]

Both are copies of the orientation cube \(Q_s\) on \(R\), and the
pointwise exchange \(a\leftrightarrow b\) joins corresponding vertices.

Use a cyclic Gray code

\[
 \epsilon_0,\ldots,\epsilon_{2^s-1}
\tag{5.4}
\]

whose transition run is at least \(s-3\log_2s\).  Put

\[
 \ell=2H+2,
 \qquad d=\ell-1,
 \qquad k_s=\left\lfloor\frac{2^s-1}{d}\right\rfloor.
\tag{5.5}
\]

For \(0\le h<k_s\), traverse the \(\ell\) orientations

\[
 \epsilon_{hd},\epsilon_{hd+1},\ldots,
 \epsilon_{(h+1)d}
\tag{5.6}
\]

inside \(\mathcal P_{h\bmod2}\), and join consecutive blocks by the
pointwise exchange.  Blocks in the same packet use disjoint orientation
intervals, so every middle owner is used at most once.

If

\[
 s\ge 2H+4\log_2(2H+2),
\tag{5.7}
\]

then the Gray transition run exceeds \(2H\), and every seam has the strong
two-sided \(H\)-collar (1.7).  In particular, every coordinate residence
and nonresidence interval exceeds \(H\).
Indeed, the \(R\)-directions occur in the original long-run Gray order,
with extra seam transitions only increasing their separation.  The two
special coordinates \(a,b\) change only at consecutive seams, which are
separated by an entire \(\ell\)-state block.  Hence the audited
long-residence theorem makes this a literal radius-\(H\) path.

Every block has constant profile; every seam changes
\(FE\leftrightarrow SS\); and every \(q\le H\) crossing window meets only
one seam.  Therefore every crossing target has the special status from
Proposition 3.1, and the opposite shoulders (3.6)--(3.7) have zero
crossing neighborhood.

It remains to check scale.  Summed over all base profiles, the total
number of orientations is exactly

\[
 \binom{2m-4}{m-3}
 =\left(\frac1{32}+o(1)\right)W.
\tag{5.8}
\]

The number belonging to profiles with
\(s<2H+4\log_2(2H+2)\) is at most

\[
 2^{m-2}(S+1)m^S,
 \qquad S=2H+4\log_2(2H+2),
\tag{5.9}
\]

which is \(o(W)\) because \(S\log m=o(m)\).  For one base profile,
(5.5)--(5.6) use

\[
 k_s\ell=(1+O(1/H))2^s+O(H)
\tag{5.9a}
\]

owners across the two disjoint packets.  Summing the \(O(H)\) term over
all base profiles gives \(O(H3^m)=o(W)\).  Thus the braid uses
\(\Theta(W)\) distinct middle owners, has at most
\(3^{m-2}=o(W/H)\) components, and has

\[
\boxed{\Theta(W/H)}
\tag{5.10}
\]

literal profile-changing seams.

This is a positive-mass subsystem, not a full exact middle factor.  Its
role is precise: it disproves every coverage theorem whose only inputs are
critical block length, seam density, profile change, long collars, and
middle-owner simplicity.  A full theorem must impose an anti-concentration
or Hall condition coupling the seam types to the actual residual target
demands.

## 6. A bounded-capacity duplicate-fan obstruction

The preceding obstruction lives outside the allowed shoulder.  The next
one shows that even inside the allowed shoulder, many clean seams may have
the same colors.

### Theorem 6.1 -- \(B+1\) literal seams with \(q-2B\) common colors

Fix an integer \(B\ge1\), and assume

\[
 q\ge2B+1,
 \qquad m\ge2q+2.
\tag{6.1}
\]

There exist \(B+1\) pairwise middle-disjoint literal paths, each divided
into two constant-profile blocks of exactly \(q\) states and joined by a
genuine \(FE\to SS\) seam, with the following property.  For exactly
\(q-2B\) split positions, all \(B+1\) paths have the same lower target and
the same upper target.  These \(q-2B\) target pairs are mutually distinct.

Consequently, if every residual target capacity is at most \(B\), then
the common-owner flow deficiency of these seams satisfies

\[
\boxed{\tau_q\ge q-2B.}
\tag{6.2}
\]

#### Construction

Let

\[
 I=\{-q+1,-q+2,\ldots,q-1\}.
\tag{6.3}
\]

Choose disjoint coordinate pairs \(\{a_i,b_i\}\), \(i\in I\), a core
\(C\) of size

\[
 |C|=m-(2q-1),
\tag{6.4}
\]

an element \(\ell\in C\), and a coordinate
\(o\notin C\cup\{a_i,b_i:i\in I\}\).  Use the physical pairs

\[
 P^- =\{a_0,\ell\},
 \qquad P^+=\{b_0,o\},
 \qquad P_i=\{a_i,b_i\}\quad(i\ne0),
\tag{6.5}
\]

and complete them arbitrarily to the partition (1.1).

For \(v\in\{0,1\}^I\), let \(c_i(v)=a_i\) for \(v_i=0\) and
\(c_i(v)=b_i\) for \(v_i=1\); let \(\bar c_i(v)\) be its mate.  Define

\[
 X_s^v
 =C\cup\{\bar c_i(v):i<s\}
     \cup\{c_i(v):i\ge s\},
 \qquad -q+1\le s\le q.
\tag{6.6}
\]

The transition \(s\to s+1\) flips direction \(i=s\).  Take

\[
 v^{(0)}=0,
 \qquad
 \operatorname{supp}v^{(j)}=\{-j,+j\},
 \quad1\le j\le B.
\tag{6.7}
\]

Split each path as

\[
 X_{-q+1}^v,\ldots,X_0^v
 \quad\Vert\quad
 X_1^v,\ldots,X_q^v.
\tag{6.8}
\]

The seam removes \(a_0\) and inserts \(b_0\).  At \(P^-\), the status
changes from full to the singleton \(\{\ell\}\); at \(P^+\), it changes
from empty to the singleton \(\{b_0\}\).  Every other transition flips
one singleton physical pair.  Hence both blocks have constant profile and
the seam is exactly \(FE\to SS\).

#### Middle-disjointness

Encode the orientation of \(X_s^v\) on the indexed directions by a bit
vector.  It is

\[
 v\oplus1_{\{i<s\}}.
\tag{6.9}
\]

If \(X_s^{v^{(j)}}=X_t^{v^{(k)}}\), then

\[
 v^{(j)}\oplus v^{(k)}
\tag{6.10}
\]

must be an interval in the linear order on \(I\).  For \(j\ne k\), this
set is either \(\{-j,j\}\) or a four-set
\(\{-j,j,-k,k\}\).  It contains both signs but omits \(0\), so it is not
an interval.  Thus all displayed middle owners are distinct.

#### Literal realization

Order first the departure coordinates

\[
 c_{-q+1}(v),\ldots,c_{q-1}(v),
\]

then the core \(C\), and then the arrival coordinates

\[
 \bar c_{-q+1}(v),\ldots,\bar c_{q-1}(v).
\]

Complete this list to a cyclic order on \(2m-1\) coordinates.  The
successive length-\(m\) windows beginning at the displayed initial window
are exactly (6.6).  Every interval of at most \(q\) transitions flips
distinct coordinates, so the path is geodesic and literal through depth
\(q\).

#### Coinciding fans

For crossing split \(r\in\{0,\ldots,q-1\}\), the complete transition-index
set is

\[
 D_r=\{-r,-r+1,\ldots,q-1-r\}.
\tag{6.11}
\]

The ordinary collar directions are

\[
 \widehat D_r=D_r\setminus\{0\}.
\tag{6.11a}
\]

The lower target empties every physical pair direction in
\(\widehat D_r\), the upper target fills it, and every indexed physical
pair outside \(D_r\) keeps its initial orientation.  Index \(0\) is the
special \(FE\to SS\) transition and has the half-statuses prescribed by
Proposition 3.1.  If

\[
 B\le r\le q-1-B,
\tag{6.12}
\]

then \(\widehat D_r\) contains \(\{-j,+j\}\) for every
\(1\le j\le B\).  Changing
from \(v^{(0)}\) to any \(v^{(j)}\) only toggles directions which the
target subsequently empties or fills.  Therefore all \(B+1\) lower and
upper targets coincide for every \(r\) in (6.12).  There are exactly
\(q-2B\) such values.  Different \(r\)'s have different sets \(D_r\),
which are recovered from \(U_{q,r}\setminus L_{q,r}\); hence the target
pairs are distinct.

Each of the \(q-2B\) parallel classes has \(B+1\) edges but endpoint
capacity at most \(B\).  At least one edge per class is rejected by every
common-owner flow, proving (6.2).  \(\square\)

For a fixed Gaussian window, take \(B\) larger than every balanced quota
capacity \(c_q+1\).  Then \(B=O_A(1)\), while
\(q=\Theta(\sqrt m)\), so (6.2) is \(\Theta(q)\).  The construction has
critical block length, changing profile, clean literal collars, and exact
middle disjointness.  It is not asserted to occur inside one preselected
exact wreath factor, and no global packing of these gadgets is claimed.
Its conclusion is the sharp one needed here: the desired Hall bound cannot
be deduced from the local seam hypotheses alone.

## 7. Exact surviving lemma and adversarial audit

The smallest factor-specific statement which survives both obstructions is
the following.

> **Critical common-owner seam-flow lemma -- UNPROVED.**  For every fixed
> \(A>0\), construct one exact middle wreath factor together with one
> owner-preserving literal chronology of its pointed occurrences, divided into
> blocks of lengths between \(c_AH\) and \(C_AH\), and one common integral
> two-port path factor such that:
>
> 1. all but \(o(W/H)\) selected boundaries are literal
>    profile-changing seams with strong two-sided \(H\)-collars;
> 2. after charging any cycle cuts, the crossing multigraphs satisfy
>    \[
>      \sum_{q\le H}
>      \min_{\beta_q^-,\beta_q^+}
>      \bigl(E_q^-+E_q^++K_q-\nu_q\bigr)=o(W);
>    \]
> 3. the same selected seams and ports are used at every depth; and
> 4. cycle breaking loses \(o(W)\) useful crossing colors, for example by
>    having \(o(W/H^2)\) productive cycles.

By (4.14)--(4.15), this lemma composes quantitatively into the audited
fixed-window overload route and hence, after diagonalization and the
audited tail theorem, into the constant-one OR bound.  The lemma is not
proved here.

The following adversarial checks were made.

1. **Off-by-one.**  A depth-\(q\) crossing interval has \(q\) possible
   starts.  The seam uses one of its \(q\) transitions, leaving
   \(q-1\) internal directions.  All formulas and profile counts use this
   convention.

2. **Literal rank.**  Pairwise distinct transition labels give exactly
   \(q\) deletions and \(q\) additions, so (2.5) is exact.  The explicit
   gadget is a segment of actual sliding length-\(m\) windows.

3. **Fan distinctness.**  Ordinary geodesicity of each one window is not
   silently used to compare different splits.  Theorem 2.1 assumes the
   stronger union collar.  The gadget satisfies it because all
   \(2q-1\) directions are distinct.

4. **Integrality and common ownership.**  The flow uses whole crossing
   edges \((L,U)\), not independently selected lower and upper
   occurrences.  Max-flow integrality is exact.

5. **Depthwise scope.**  The optimizing flow at a depth is a certificate
   for loads in one already fixed chronology.  It does not authorize
   different seam factors at different depths and does not produce the
   stronger labelled nested resolution.

6. **Obstruction scope.**  The positive-density braid is only a
   \(\Theta(W)\)-owner subsystem, and Theorem 6.1 is not packed into one
   prescribed exact factor.  They refute a hypothesis-only seam theorem;
   they do not refute the factor-specific lemma above or the contiguous-OR
   conjecture.

7. **Existing two-port theorem.**  The previously proved independent
   two-port selection loses \(8HJ/b\) blocks and requires \(b/H\to\infty\).
   The profile-capacity obstruction forces \(b=O(H)\).  Therefore that
   theorem cannot fill the fixed-aspect-ratio gap by discarding bad blocks;
   incoming and outgoing ports must be correlated at the critical scale.

Two independent proof audits checked the crossing formulas, the four
ordinary-pair profile cases, the max-flow cut, the factor-two overload
comparison, middle-disjointness of the toggle construction, and the exact
\(q-2B\) deficiency.  No constant-one conclusion is claimed.
