# PBBS short returns: adjacent-deletion transversals and the Gaussian port trap

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil ,
\tag{0.1}
\]

where \(A>0\) is fixed.  Delete the quotient \(\tau\)-cycles of length
at most \(H+1\), so that every residence support below is a proper,
nonrepeating circular interval.

This note audits the proposed route which recursively orients the two
boundary deletions of every adjacent floor-shadow equality.  It proves
two exact no-go theorems.

1. A complete adjacent-deletion history on a depth-\(q\) equality is
   exactly the choice of one transition edge in its literal
   \((q+1)\)-edge residence support.  Every edge of that support is
   attainable.  Consequently simultaneous adjacent-deletion orientation
   of all equalities through \(q\le H\) is precisely the circular-interval
   transversal problem, with no additional freedom or hidden constraint.
   In particular, if \(\nu_H\) and \(\tau_H\) are respectively its
   packing and transversal numbers, then

   \[
      \boxed{\nu_H\le \tau_H\le \nu_H+c_H\le2\nu_H,}
   \tag{0.2}
   \]

   where \(c_H\) is the number of active quotient cycles.  Thus an
   \(o_A(B_m/\sqrt m)\) adjacent-deletion transversal theorem is
   equivalent, within the sharp factor two, to the still-open quotient
   form of \((ST_A)\).  Positive winding changes which intervals occur,
   but not this equivalence.

2. Adding the exact predecessor-child menus does not create a generic
   Gaussian-window contraction.  In one inverse peak-deletion fibre, the
   optimal integral orientation of all terminal-value classes has maximum
   port load exactly the terminal-zero hyperplane

   \[
      K_0=\binom{y+2d-1}{2d-1}.
   \tag{0.3}
   \]

   On a serial profile, the all-zero history is forced under every
   adaptive orientation.  There are realizable integral profiles of
   length \(L=\Theta_A(\sqrt m)\) with one free leaf at every inverse
   level for which the forced-history fraction is

   \[
      \boxed{1-O_A(m^{-1/2}).}
   \tag{0.4}
   \]

   Hence even Gaussian-many exact, integral, history-dependent child-port
   orientations need not give any vanishing factor.  On the formal
   harmonic profile the exact optimum tends instead to \(1/2\).

These are route obstructions, not a counterexample to \((ST_A)\).  The
critical separated-interval system has packing and transversal both of
order \(B_m/H\), and the same geometry is realizable in the exact
adjacent-shadow Johnson relaxation.  Genuine PBBS fibres also realize
positive local utilization, but the presently certified fibres have
subcritical global Catalan mass.  A proof of \((ST_A)\) must therefore
use a global PBBS chronology theorem which makes the actual interval set
sparse or highly clustered; it cannot follow from the adjacent-equality
dictionary, deletion orientation, circular Hall, or unrestricted
predecessor-port menus alone.

## 1. Literal support of one adjacent equality

Let \((X_i)\) be one complement-projected step-two PBBS owner cycle and
write

\[
 X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\}.
\tag{1.1}
\]

For \(q\ge1\), put

\[
 L_{i,q}=\bigcap_{a=0}^{q}X_{i+a}.
\tag{1.2}
\]

Assume the two adjacent shadows \(L_{i,q},L_{i+1,q}\) are floor-correct.
The exact adjacent-equality dictionary gives

\[
 L_{i,q}=L_{i+1,q}
 \quad\Longleftrightarrow\quad
 \beta_i=\alpha_{i+q}.
\tag{1.3}
\]

In PBBS indices, (1.3) is a consecutive omitted-label gap \(2q-1\).
The common coordinate enters at transition \(i\), is present in the
owners \(X_{i+1},\ldots,X_{i+q}\), and leaves at transition \(i+q\).
Thus its full literal quotient support is

\[
 \boxed{I(i,q)=\{e_i,e_{i+1},\ldots,e_{i+q}\},
        \qquad |I(i,q)|=q+1.}
\tag{1.4}
\]

This agrees with the predecessor-passage convention.  If the physical
gap is written \(2s+1\), then \(q=s+1\), and the insertion-edge support
is \(\{e_D,e_{\tau D},\ldots,e_{\tau^{s+1}D}\}\).

The support (1.4), not merely its two equal shadow values, is used below.
It contains the entry and exit transitions.  Omitting either boundary
would give the wrong transversal and the wrong constant.

## 2. Interval-composition equivalence

Start from an interval of transition edges

\[
 I=[a,b]=\{e_a,e_{a+1},\ldots,e_b\}.
\]

An adjacent deletion removes either its left boundary edge or its right
boundary edge.  Continue until one edge remains.  A history may make its
next choice as an arbitrary function of all earlier choices.

### Theorem 2.1 (one interval)

The possible terminal edges of complete adjacent-deletion histories on
\(I\) are exactly the edges of \(I\).

More precisely, a history ending at \(e_{a+t}\) makes exactly \(t\) left
deletions and \(b-a-t\) right deletions.  Conversely any ordering of
those deletions is legal and ends at \(e_{a+t}\).

#### Proof

Every deletion preserves a nonempty subinterval of \(I\), so the terminal
edge belongs to \(I\).  If \(t\) left boundary edges and
\(b-a-t\) right boundary edges are removed, the sole surviving edge is
\(e_{a+t}\).  Removing these prescribed boundary edges in any order is
legal because at every proper prefix at least one edge remains. \(\square\)

Let \(\mathcal I\) be any family of proper circular intervals on a
disjoint union of cycles.  A simultaneous deletion orientation is one
complete history for every \(I\in\mathcal I\).  Let \(T\) be the set of
distinct terminal edges used by those histories.

### Theorem 2.2 (simultaneous orientation equals transversal)

\[
 \boxed{
 \min_{\text{simultaneous deletion histories}}|T|
 =\tau(\mathcal I),}
\tag{2.1}
\]

where \(\tau(\mathcal I)\) is the minimum cardinality of an edge set
meeting every interval in \(\mathcal I\).

With integral edge capacities \(b_e\ge0\), histories can be chosen so
that at most \(b_e\) intervals terminate at \(e\) if and only if

\[
 |\mathcal F|
 \le\sum_{e\in\bigcup_{I\in\mathcal F}I}b_e
 \qquad\text{for every }\mathcal F\subseteq\mathcal I.
\tag{2.2}
\]

#### Proof

By Theorem 2.1, every terminal edge chosen for \(I\) belongs to \(I\).
Thus the set of distinct terminals is a transversal.  Conversely, given
a transversal \(T\), choose for each \(I\) one edge of \(T\cap I\) and
use Theorem 2.1 to reach it.  This proves (2.1).

For (2.2), replace every edge \(e\) by \(b_e\) clones and apply Hall's
marriage theorem to the bipartite incidence graph
\(I\sim e\Longleftrightarrow e\in I\).  Theorem 2.1 lifts the resulting
assignment to deletion histories. \(\square\)

This theorem includes full adaptivity.  Earlier choices alter the current
subinterval, but they alter it only through the two numbers of boundaries
already deleted.  The expanded history graph is a directed acyclic
network, and its terminal projection is exactly the interval-incidence
graph in (2.2).  There is therefore no separate ``adaptive orientation''
gain after literal supports have been retained.

On a line, the interval-incidence matrix has the consecutive-ones
property, so its fractional packing and transversal polyhedra are
integral.  Equivalently, the greedy earliest-right-end algorithm proves
equality of packing and transversal numbers.  The cyclic boundary costs
at most one point.

### Corollary 2.3 (circular factor two)

If \(\nu_C,\tau_C\) are the packing and transversal numbers on one active
cycle, then

\[
 \nu_C\le\tau_C\le\nu_C+1\le2\nu_C.
\tag{2.3}
\]

Consequently, after summing over active cycles,

\[
 \nu(\mathcal I)\le\tau(\mathcal I)
 \le\nu(\mathcal I)+c(\mathcal I)
 \le2\nu(\mathcal I),
\tag{2.4}
\]

where \(c(\mathcal I)\le\nu(\mathcal I)\) is the number of active
cycles.

#### Proof

Choose a point \(x\) in one interval on the cycle.  The intervals not
containing \(x\) become line intervals after cutting at \(x\), so they
have a transversal of size equal to their packing number, at most
\(\nu_C\).  Add \(x\).  This proves the middle inequality.  Every active
cycle contains at least one member of a maximum cyclewise packing, so
\(c(\mathcal I)\le\nu(\mathcal I)\). \(\square\)

Apply this to all genuine PBBS adjacent equalities through \(q\le H\).
The voltage bound deletes only

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(m))
            =o(B_m/\sqrt m)
\tag{2.5}
\]

short-cycle roots.  Therefore a simultaneous orientation with
\(o_A(B_m/\sqrt m)\) distinct terminal quotient edges exists if and only
if the short-return packing is \(o_A(B_m/\sqrt m)\), up to the harmless
factor two in (2.4).  After the exact \(N\)-phase lift this is precisely
the physical \(o_A(B_m\sqrt m)\) gate.

No winding assumption entered the proof.  Winding is a label on the
return equation which determines membership in \(\mathcal I\); once the
literal support (1.4) is fixed, the deletion and Hall statements are
identical for zero and positive winding.

## 3. Sharp critical interval obstruction

Let a cycle have \(M(q+1)\) transition edges and partition it into the
\(M\) intervals

\[
 I_j=\{e_{j(q+1)},\ldots,e_{(j+1)(q+1)-1}\},
 \qquad0\le j<M.
\tag{3.1}
\]

Then

\[
 \boxed{\nu(\{I_j\})=\tau(\{I_j\})=M.}
\tag{3.2}
\]

Indeed the intervals are pairwise disjoint, and one point in each is
both necessary and sufficient.  At \(q=H\) and total edge volume
\(E\), this is the critical order \(E/(H+1)\).

The arbitrary-depth suspension construction realizes isolated
depth-\(H\) extensions with this order of packing inside the exact
floor-correct adjacent-shadow Johnson relaxation while retaining
rainbowness at every shallower depth.  It is not asserted to be the
canonical PBBS quotient.  Separately, genuine PBBS mountain and
fixed-core fibres realize a positive limiting fraction of the same local
interval capacity, but their currently certified total Catalan mass is
subcritical.  Thus (3.2) is a sharp dual obstruction to the orientation
axioms, not a global counterexample to \((ST_A)\).

## 4. Exact integral orientation of predecessor-child menus

One might try to strengthen adjacent deletion by first applying peak
deletion and orienting a parent return toward one of its many predecessor
children.  The exact integral minimax problem can also be solved.

Fix a reduced core of rank \(d\), and distribute \(y\) free inverse leaves
among its \(2d+1\) slots.  Let \(z\) be the terminal-slot occupancy.  The
complete fibre and its terminal layers have sizes

\[
 P(d,y)=\binom{y+2d}{2d},
 \qquad
 K_z(d,y)=\binom{y-z+2d-1}{2d-1}
 \quad(0\le z\le y).
\tag{4.1}
\]

A parent in terminal layer \(z\) has the legal pairwise-disjoint
predecessor-child ports

\[
 \Gamma(z)=\{0,1,\ldots,z\}.
\tag{4.2}
\]

The same menu is valid for positive winding: it uses only particle order,
the no-wrap hypothesis, and consecutive predecessor selections.

### Theorem 4.1 (exact integral minimax load)

Orient every individual parent sheet of layer \(z\) to one port in
\(\Gamma(z)\).  If \(L_i\) is the resulting load of port \(i\), then

\[
 \boxed{
 \min_{\text{integral orientations}}\max_iL_i=K_0(d,y).}
\tag{4.3}
\]

The same conclusion holds after restricting the active terminal values
to any nonempty initial interval \(\{0,1,\ldots,Z\}\).

#### Proof

Every one of the \(K_0\) sheets in terminal layer zero has the singleton
menu \(\Gamma(0)=\{0\}\).  Thus every orientation has \(L_0\ge K_0\).

For the reverse inequality, orient every layer \(z\) to its last port
\(i=z\).  Then \(L_i=K_i\).  The sequence \(K_i\) is nonincreasing, so
\(L_i\le K_0\) for every \(i\).  The proof is unchanged for an initial
interval of active layers. \(\square\)

Thus the optimal integral one-level factor relative to the complete
fibre is

\[
 \boxed{
 \beta(d,y)={K_0(d,y)\over P(d,y)}
 ={2d\over y+2d}.}
\tag{4.4}

The uniformly split stochastic orientation has the larger factor
\(\rho(d,y)\), but optimizing integrally changes only the constant.  It
does not change the summability boundary below.

## 5. Adaptive serial orientation and the forced-zero history

Fix a pruning-rank profile

\[
 r_0>r_1>\cdots>r_{L+1}>0,
 \qquad
 y_j=r_j-2r_{j+1}+r_{j+2}\ge0.
\tag{5.1}
\]

After a bottom core and the complete profile are fixed, the unrestricted
inverse choices form a Cartesian product.  At level \(j\), put

\[
 P_j=\binom{r_j+r_{j+2}}{2r_{j+1}},
 \qquad
 K_{j,0}=\binom{r_j+r_{j+2}-1}{2r_{j+1}-1},
\tag{5.2}
\]

so

\[
 \beta_j={K_{j,0}\over P_j}
 ={2r_{j+1}\over r_j+r_{j+2}}.
\tag{5.3}

An orientation at level \(j\) may depend on the complete earlier port
history.  A terminal history is the resulting word
\((i_0,\ldots,i_{L-1})\).

### Theorem 5.1 (adaptive recourse trap)

In the unrestricted serial predecessor-port system, every adaptive
integral orientation has a history column of load at least

\[
 \boxed{\prod_{j=0}^{L-1}K_{j,0}.}
\tag{5.4}

This is sharp.  The minimum possible maximum history load, divided by
the complete profile-fibre size \(\prod_jP_j\), is exactly

\[
 \boxed{\prod_{j=0}^{L-1}\beta_j.}
\tag{5.5}

#### Proof

At every level, terminal value zero has only port zero.  Hence every
inverse tower whose terminal value is zero at all \(L\) levels is forced,
under every adaptive rule, to the single history
\((0,\ldots,0)\).  Cartesian factorization gives exactly
\(\prod_jK_{j,0}\) such towers.  This proves (5.4).

For sharpness, use at every level the orientation \(i_j=z_j\), even after
conditioning on the earlier history.  The history
\((i_0,\ldots,i_{L-1})\) then has load
\(\prod_jK_{j,i_j}\), which is at most \(\prod_jK_{j,0}\).
Thus equality holds. \(\square\)

On the rational harmonic profile

\[
 r_j={R\over j+1},
\tag{5.6}
\]

whenever the displayed ranks are integral,

\[
 \beta_j
 ={(j+1)(j+3)\over(j+2)^2}
 =1-{1\over(j+2)^2}.
\tag{5.7}

Therefore

\[
 \boxed{
 \prod_{j=0}^{L-1}\beta_j
 =\prod_{n=2}^{L+1}\left(1-{1\over n^2}\right)
 ={L+2\over2(L+1)}\longrightarrow{1\over2}.}
\tag{5.8}

This is the exact integral point-margin invariant.  It is stronger than
merely observing that the stochastic harmonic deficits are summable.

There is also a fully integral Gaussian-length obstruction, with no
denominator issue in (5.6).

### Theorem 5.2 (Gaussian-length realizable profile)

For every fixed \(A>0\), there is \(c_A>0\) and, for all sufficiently
large \(m\), a realizable integral pruning profile of length

\[
 L=\lfloor c_A\sqrt m\rfloor\le H
\tag{5.9}

such that \(y_j=1\) for every \(0\le j<L\) and

\[
 \boxed{
 \prod_{j=0}^{L-1}\beta_j=1-O_A(m^{-1/2}).}
\tag{5.10}

#### Proof

Take

\[
 c_A=\min\{A/2,1/10\},
 \qquad L=\lfloor c_A\sqrt m\rfloor,
\]

and define, for \(0\le j\le L+1\),

\[
 r_j=m-2Lj+\binom j2.
\tag{5.11}

Then

\[
 r_j-r_{j+1}=2L-j>0,
 \qquad
 r_j-2r_{j+1}+r_{j+2}=1.                         \tag{5.12}
\]

Moreover

\[
 r_{L+1}=m-\frac32L(L+1)\ge(0.98-o(1))m,          \tag{5.13}
\]

so all ranks are positive.  A nonincreasing leaf-count sequence is a
plane-tree pruning profile: realize it by taking an ordered root forest
of unary paths, with the number of paths surviving the \(j\)-th pruning
round equal to \(r_j-r_{j+1}\), and extend one path to absorb the
remaining tail.  Thus (5.11) is realizable.

Since \(y_j=1\), equations (5.3) and (5.12) give

\[
 \beta_j={2r_{j+1}\over2r_{j+1}+1}.
\]

Using \(\prod(1-x_j)\ge1-\sum x_j\) and (5.13),

\[
 \prod_{j<L}\beta_j
 \ge1-\sum_{j<L}{1\over2r_{j+1}+1}
 =1-O_A(L/m)
 =1-O_A(m^{-1/2}).
\]

This proves (5.10). \(\square\)

The ranks in Theorem 5.2 remain \(\Theta(m)\), so every gap at most
\(2H-1\) is nonwrapping at every one of these \(L\) deletion levels.
The obstruction therefore is not caused by a reduced-circumference
boundary.

## 6. Exact scope and the surviving theorem

Theorem 2.2 is an equivalence for the **actual** PBBS return intervals.
It says that adjacent-deletion orientation cannot be used as an
independent proof of \((ST_A)\): proving the needed orientation cost is
already proving the interval transversal, hence the packing theorem up to
factor two.

Theorems 4.1--5.2 concern the stronger, unrestricted predecessor-port
profile relaxation.  They prove that even its optimal integral adaptive
orientation has no universal Gaussian-depth contraction.  Their precise
caveat is important.  A realizable pruning profile need not support a
PBBS decorated-passage tower at every displayed level.  Thus (5.10) is
not a family of globally critical PBBS return starts and does not refute
\((ST_A)\).  Actual chronology can still win only by proving that:

1. the dynamically eligible passage towers avoid these high-retention
   profiles in aggregate;
2. transported active sheets occupy \(o(1)\) of the exact cover degree;
   or
3. the genuine long-period starts have divergent short-lag clustering,
   making their interval packing little-oh despite critical one-point
   mass.

Every one of these is information beyond the adjacent-shadow equality
dictionary and beyond local deletion orientation.  Positive winding is
fully included in the interval equivalence and in the no-wrap child-port
menus; the unresolved issue is its global occurrence chronology, not an
orientation sign or an omitted support edge.

