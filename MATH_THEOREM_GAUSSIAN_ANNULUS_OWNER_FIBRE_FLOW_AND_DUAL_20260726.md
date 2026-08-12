# Gaussian-annulus owner-fibre flow: exact abstract reuse, LP dual, and the PBBS baseline gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 B=\operatorname {Cat}_m={W\over n},
\tag{0.1}
\]

and let

\[
 h=o(\sqrt m),\qquad
 H=\lceil A\sqrt m\rceil,\qquad
 Q=\{h+1,\ldots,H\},
\tag{0.2}
\]

where \(A>0\) is fixed.  The target annulus consists of ranks

\[
                    m-q,\qquad m+1+q,\qquad q\in Q.
\tag{0.3}
\]

There are two different optimization problems.

1. **Unrestricted owner-fibre problem.**  One abstract middle-root fibre may
   carry one nested lower target and one nested upper target at every
   depth.  This problem is exactly an integral network flow.  It has a
   common balanced solution using \(W\) abstract root paths once, not once
   per depth.  This does not yet identify a path with a paid PBBS position
   or erosion slot.  At depth \(q\), every target has load either

   \[
   c_q=\left\lfloor {W\over N_q}\right\rfloor
   \quad\hbox{or}\quad
   u_q=\left\lceil {W\over N_q}\right\rceil,
   \qquad N_q=\binom{2m+1}{m-q}.
   \tag{0.4}
   \]

   Uniformly for \(q\le A\sqrt m\), these loads are \(O_A(1)\).  Thus
   Gaussian depth creates no abstract owner-capacity or common-nesting
   cost.

2. **Anchored PBBS problem.**  A paid PBBS position does not offer every
   abstract flag.  It offers a finite library of literal,
   chronology-safe, provenance-certified all-depth columns.  Choosing one
   column in every owner fibre is a multiple-choice configuration problem.
   Its exact fractional dual is a weighted owner-fibre Hall inequality.
   Nestedness alone does not make this configuration matrix integral: an
   explicit four-column minor has determinant two.

There is a sharp integral intermediate case.  If each paid occurrence has
one fixed signed cutoff pair and every outer inclusion tail may be
spliced independently, the two signs form one hourglass network.
Hoffman's circulation inequalities are then necessary and sufficient,
and total unimodularity gives an integral solution.  For support-only
quotas the entire all-depth problem collapses to the edge-cover deficiency
of the signed cutoff graph.

Even an integral anchored flag selection is not yet principal PBBS
baseline reuse.  Every selected column whose cost is meant to replace a
principal-baseline letter must be injectively matched to an eligible
endpoint-capped erosion position, and every canonical witness destroyed by
that deletion must be retained or rebuilt.  This is the separate ERP Hall
condition.  The deletion credit is paid once per erosion position; summing
it independently over depths is literal double counting.

Therefore the exact answer is:

\[
\boxed{\text{a common nested flow reuses \(W\) abstract owner roots
across \(q\), integrally,}}
\tag{0.5}
\]

but

\[
\boxed{\text{literal PBBS reuse requires one joint model containing
anchored selection, ERP, and every literal chronology/coverage row.}}
\tag{0.6}
\]

A jointly feasible model with complete literal columns, global interval
placements, exact length/credit accounting, and all collateral witnesses
would conversely prove reuse.  No current theorem proves or refutes that
joint feasibility.

## 1. Exact Gaussian quotas

For \(0\le q\le H\), write

\[
 {\cal V}_q=\binom{[n]}{m-q},
 \qquad
 N_q=|{\cal V}_q|
     =\binom{2m+1}{m-q}.
\tag{1.1}
\]

The lower targets are the members of \({\cal V}_q\).  The upper targets
are their complements and have rank \(m+1+q\).  The exact reciprocal
rank ratio is

\[
 \lambda_q={W\over N_q}
  =\prod_{j=0}^{q-1}{m+2+j\over m-j}.
\tag{1.2}
\]

Put

\[
 c_q=\lfloor\lambda_q\rfloor,\qquad
 r_q=W-c_qN_q,
\tag{1.3}
\]

and

\[
 u_q=c_q+\mathbf 1_{\{r_q>0\}}.
\tag{1.4}
\]

If \(W\) owner columns each claim one target at depth \(q\), the quota
box

\[
 c_q\le\mu_q(T)\le u_q\qquad(T\in{\cal V}_q)
\tag{1.5}
\]

automatically forces exactly \(r_q\) targets to have load \(c_q+1\) and
the remaining targets to have load \(c_q\).

Uniformly for \(q\le A\sqrt m+O(1)\),

\[
 \log\lambda_q
 ={q(q+1)\over m}+O_A(m^{-1/2}).
\tag{1.6}
\]

Indeed, (1.6) is the negative of the audited logarithm of \(N_q/W\).
Consequently, for all sufficiently large \(m\),

\[
                         u_q\le e^{A^2}+1.
\tag{1.7}
\]

Thus the exact balanced multiplicities stay bounded on every fixed
Gaussian window.

## 2. Exact abstract owner-fibre columns

Fix one oriented exact middle factor

\[
 f:{\cal V}_0\longrightarrow{\cal V}_0,
 \qquad X\cap f(X)=\varnothing.
\tag{2.1}
\]

The map \(f\) is a permutation.  The central upper owner paired with
\(X\) is

\[
                         X^+=[n]\setminus f(X),
\tag{2.2}
\]

which has rank \(m+1\) and contains \(X\).

An abstract owner-fibre column at \(X\) is a pair of deletion flags

\[
 X=S^-_0\supset S^-_1\supset\cdots\supset S^-_H,
 \qquad |S^-_q|=m-q,
\tag{2.3}
\]

and

\[
 f(X)=S^+_0\supset S^+_1\supset\cdots\supset S^+_H,
 \qquad |S^+_q|=m-q.
\tag{2.4}
\]

Its actual signed targets at depth \(q\) are

\[
                         S^-_q,\qquad [n]\setminus S^+_q.
\tag{2.5}
\]

The column is charged once at its root \(X\), regardless of how many
depths in (2.3)--(2.4) it serves.

### Theorem 2.1 (common balanced owner-fibre flow)

For every \(0\le H\le m\), there is an integral choice of one abstract
column (2.3)--(2.4) for every \(X\in{\cal V}_0\) such that, for both
signs, every depth-\(q\) target has load in \([c_q,u_q]\).

In particular, all depths in the Gaussian annulus are carried by the
same \(W\) abstract Boolean owner paths with no additional abstract root.
No PBBS occurrence or principal erosion credit is asserted here.

#### Proof

First construct the lower flags.  Make a layered directed graph with
layer \({\cal V}_q\) at depth \(q\), and put an arc

\[
 S\longrightarrow T
 \quad\Longleftrightarrow\quad
 T\subset S,\quad |S\setminus T|=1.
\tag{2.6}
\]

Give every root \(X\in{\cal V}_0\) one unit of supply.  Split each target
node and gate its throughput between \(c_q\) and \(u_q\).

There is a symmetric fractional flow.  Give every node of
\({\cal V}_q\) throughput

\[
                              \lambda_q={W\over N_q}.
\tag{2.7}
\]

At the step from \(q-1\) to \(q\), a parent has outdegree
\(m-q+1\), while a child has indegree \(m+1+q\).  Put flow

\[
                       {\lambda_{q-1}\over m-q+1}
\tag{2.8}
\]

on every arc.  The exact edge census

\[
 N_{q-1}(m-q+1)=N_q(m+1+q)
\tag{2.9}
\]

shows that the incoming load at every child is \(\lambda_q\).  Since
\(c_q\le\lambda_q\le u_q\), the node gates are respected.

After node splitting, this is an ordinary network with integral lower
and upper capacities.  Its matrix is totally unimodular.  Hence the
fractional flow has an integral feasible counterpart.  Decompose it into
\(W\) unit paths, one from every root \(X\).  These paths are the flags
in (2.3).

Run the same construction independently on roots \(Y\in{\cal V}_0\) for
the positive deletion flags.  Because \(f\) permutes \({\cal V}_0\), pair
the path rooted at \(f(X)\) with the lower path rooted at \(X\).  Taking
complements gives the positive targets in (2.5). \(\square\)

### Corollary 2.2 (no target-only fractional obstruction)

Let \(y_T^\sigma\ge0\) be arbitrary weights on all signed annulus
targets.  In the unrestricted abstract libraries,

\[
 \sum_{\sigma,q,T} y_T^\sigma
 \le
 \sum_{X\in{\cal V}_0}
 \max_{\gamma\text{ an abstract column at }X}
 \sum_{(\sigma,q,T)\in\gamma}y_T^\sigma.
\tag{2.10}
\]

#### Proof

Choose any integral column family from Theorem 2.1 which covers every
target.  Its total collected weight is at least the left side of (2.10),
and is at most the right side. \(\square\)

Thus a separating functional for the real PBBS problem must use the
restriction of the anchored PBBS libraries, a chronology/port price, or
literal provenance.  Pure rank supply cannot separate.

## 3. Frozen-boundary extension and the exact cutoff criterion

Theorem 2.1 rebuilt every flag from depth zero.  The following statements
retain a prescribed shallow boundary.

### Lemma 3.1 (one-sided support continuation)

Let \(0\le h<H\le m\).  Suppose integer path units at lower depth \(h\)
give every \(T\in{\cal V}_h\) load at least one.  If every Boolean
inclusion tail remains allowed, the same units can be continued as nested
flags so that every target in every layer \({\cal V}_q\),
\(h<q\le H\), has positive load.

The complement statement holds for the upper side.

#### Proof

Between ranks \(r\) and \(r-1\), let \({\cal C}\) be a family of
rank-\((r-1)\) children and \(N({\cal C})\) its rank-\(r\) parents.
Double-counting inclusion edges gives

\[
 (n-r+1)|{\cal C}|\le r|N({\cal C})|.
\tag{3.1}
\]

On the lower half, \(n-r+1\ge r\), so

\[
                         |N({\cal C})|\ge|{\cal C}|.
\tag{3.2}
\]

Hall's theorem gives a matching saturating every child.  Reserve one
unit at each matched parent and send it to the matched child.  Send every
remaining parent unit to an arbitrary child.  The resulting next-layer
load is positive everywhere.  Iterate to depth \(H\).  Complementation
proves the upper statement. \(\square\)

Thus, in the inclusion relaxation, no new cross-depth obstruction appears
after a genuine support-complete cutoff assignment.

### Theorem 3.2 (signed cutoff edge-cover criterion)

Let \({\cal O}\) be a family of paid owner occurrences.  Occurrence
\(o\in{\cal O}\) carries a fixed signed cutoff pair

\[
                    L_h(o)\in{\cal V}_h,\qquad
                    U_h(o)\in\overline{{\cal V}_h}.
\tag{3.3}
\]

Let \(G_h\) be the bipartite multigraph with the two cutoff target layers
as shores and one edge \(L_h(o)U_h(o)\) for each paid occurrence \(o\).
Assume arbitrary Boolean inclusion tails beyond the cutoff.

A simultaneous signed support cover through every depth
\(h\le q\le H\) exists if and only if \(G_h\) has no isolated target
vertex.  The exact minimum number of paid occurrences needed is

\[
 \boxed{
 \rho(G_h)=|{\cal V}_h|+|\overline{{\cal V}_h}|-\nu(G_h),}
\tag{3.4}
\]

where \(\nu(G_h)\) is the maximum matching size.

Since both shores have size \(N_h\),

\[
 \rho(G_h)=N_h+\delta_h,
 \qquad
 \delta_h=N_h-\nu(G_h)
 =\max_{{\cal A}\subseteq{\cal V}_h}
       \bigl(|{\cal A}|-|N({\cal A})|\bigr).
\tag{3.5}
\]

#### Proof

Every simultaneous signed flag family selects owner edges which cover
both cutoff shores.  Hence it contains an edge cover of \(G_h\).
Conversely, choose a minimum edge cover.  Its endpoint multiplicities
are positive at every cutoff target.  Apply Lemma 3.1 independently to
the lower and upper endpoint units, and pair the two continued tails back
through the owner edge which supplied their units.  This constructs the
annulus flags.

For a bipartite graph without isolated vertices, the minimum edge-cover
size is the number of vertices minus the maximum matching size.  This is
(3.4).  The standard Hall-deficiency formula gives (3.5). \(\square\)

The condition \(\rho(G_h)\le W\) is the exact support-only test for
fitting the signed cutoff assignment inside \(W\) paid occurrences.
For \(h=o(\sqrt m)\), \(N_h=(1-o(1))W\), so this is equivalently

\[
                         \delta_h\le W-N_h=o(W).
\tag{3.6}
\]

### Theorem 3.3 (hourglass Hoffman criterion)

The more general fixed-pair problem is an integral min-cost flow.
Construct an hourglass network as follows.

1. Orient the lower inclusion layers from depth \(H\) inward to depth
   \(h\).
2. Insert one capacity-one owner arc

   \[
                       L_h(o)\longrightarrow U_h(o)
   \tag{3.7}
   \]

   for every paid occurrence \(o\).
3. Orient the upper inclusion layers from depth \(h\) outward to depth
   \(H\).
4. Split every target node and gate its throughput by a prescribed
   integral interval

   \[
                    \ell_{q,T}^\sigma
                    \le\mu_{q,T}^\sigma
                    \le u_{q,T}^\sigma.
   \tag{3.8}
   \]

Add a supersource joined to every lower depth-\(H\) node and a supersink
joined from every upper depth-\(H\) node, and add a return arc from the
supersink to the supersource.  Then an
integral circulation is exactly a collection of distinct paid owner
occurrences carrying paired nested lower and upper annulus flags with
the target loads in (3.8).

Such a circulation exists if and only if, for every vertex set \(S\),

\[
 \boxed{
 \sum_{e\in\delta^-(S)}u_e
 \ge
 \sum_{e\in\delta^+(S)}\ell_e.}
\tag{3.9}
\]

With cost zero on paid owner arcs and cost one on specified repair-owner
arcs, minimum cost is integral and is the exact extra-owner requirement.

#### Proof

Node splitting converts every target gate into an arc gate.  All remaining
constraints are arc lower bounds, arc upper bounds, and flow
conservation.  Hoffman's circulation theorem gives (3.9).  The
node--arc incidence matrix is totally unimodular, so integral bounds have
an integral feasible circulation; the same holds for minimum cost.
Decomposing a circulation at the owner arcs gives the asserted paired
flags, and the reverse construction is immediate. \(\square\)

If exact loads \(b_{q-1}\) and \(b_q\) are prescribed on two consecutive
layers, the corresponding capacitated Hall condition is

\[
 b_{q-1}({\cal A})\le b_q(N({\cal A}))
\quad\hbox{for every parent family }{\cal A},
\tag{3.10}
\]

together with equality of total mass.  These adjacent-layer inequalities
compose at all depths.

Theorems 3.2--3.3 are exact only when outer tails may be spliced
independently after their current target state.  PBBS chronology has not
yet been proved to have that target-Markov property.
They are therefore exact criteria for the displayed optional-occurrence
hourglass model, not for a mandatory fixed PBBS chronology.

## 4. The anchored owner-fibre incidence and port-balance program

Let \({\cal R}\) contain every target row required of the bridge:

* both signs and all annulus depths;
* any shallow targets whose old witnesses are to be retained;
* every crossing/provenance claim included in the proposed compiler.

Let \(b\in\mathbb Z_{\ge0}^{\cal R}\) be the required lower load vector.
For every paid PBBS owner fibre \(o\), let \(\Gamma_o\) be its complete
finite library of certified whole-fibre options.  One
\(\gamma\in\Gamma_o\) must already include:

1. its simultaneous all-depth nested flags;
2. its literal anchored intervals or a certified block realization;
3. its exact PBBS sign, parity, and occurrence provenance; and
4. its ordered input/output ports.

The library includes the unchanged/null annulus option whenever a fibre
is permitted to make no new annulus claim; thus the fibre equation below
does not force an unlisted physical operation.

Write

\[
 a_{o,\gamma}\in\mathbb Z_{\ge0}^{\cal R}
\tag{4.1}
\]

for its target-incidence column, and

\[
 g_{o,\gamma}\in\mathbb Z^\Pi
\tag{4.2}
\]

for its port imbalance.  Let

\[
 d_j\in\mathbb Z_{\ge0}^{\cal R},\qquad
 h_j\in\mathbb Z^\Pi,\qquad
 c_j\in\mathbb R_{\ge0}
\]

be respectively the target column, port imbalance, and literal cost of an
auxiliary repair block \(j\).

In (4.3), \(j\) indexes a repair template which may be instantiated
repeatedly at additive cost.  If \(j\) is instead one unique physical
block or slot, impose \(0\le z_j\le1\), or index its available copies
separately.  The displayed dual below is for the repeatable-template
form; ordinary upper-bound dual variables give the unique-slot version.

### Definition 4.1 (fractional anchored incidence/port optimum)

\[
\begin{aligned}
\tau_{\rm fr}=\min\quad&
 \sum_jc_jz_j\\
\text{subject to}\quad&
 \sum_{\gamma\in\Gamma_o}x_{o,\gamma}=1
                    &&(o\in{\cal O}),\\
&
 \sum_{o,\gamma}a_{o,\gamma}x_{o,\gamma}
       +\sum_jd_jz_j\ge b,\\
&
 \sum_{o,\gamma}g_{o,\gamma}x_{o,\gamma}
       +\sum_jh_jz_j=0,\\
&x,z\ge0.
\end{aligned}
\tag{4.3}
\]

The exact integer optimum \(\tau_{\rm int}\) is obtained by requiring

\[
 x_{o,\gamma}\in\{0,1\},\qquad z_j\in\mathbb Z_{\ge0}.
\tag{4.4}
\]

Costs in (4.3) are charged once per whole all-depth column.  If extra
positions are shared nonlocally, they must be represented by one shared
block column \(j\), not charged separately to every owner.

The equation in the third line of (4.3) balances port types.  Type
balance alone does not choose compatible port pairings, force
connectivity, or order the pieces into one chronology-respecting word.
Thus (4.3) is exact for its declared incidence/port-balance model.  It is
a physical literal program only when the columns are already complete
globally glueable blocks, or after explicit pairing, order, connectivity,
and successor variables have been added.  Every dual statement below is
exact for the displayed LP and extends in the usual way when those extra
linear rows are present.

### Theorem 4.2 (full LP dual)

Give an infeasible primal the extended value \(+\infty\).  The exact dual
of (4.3), with equality in the extended sense, is

\[
 \boxed{
 \tau_{\rm fr}
 =
 \sup_{\substack{y\ge0,\ \lambda\in\mathbb R^\Pi\\
                  d_j\cdot y+h_j\cdot\lambda\le c_j\ (\forall j)}}
 \left[
 b\cdot y-
 \sum_{o\in{\cal O}}
 \max_{\gamma\in\Gamma_o}
 \bigl(a_{o,\gamma}\cdot y+
       g_{o,\gamma}\cdot\lambda\bigr)
 \right].}
\tag{4.5}
\]

#### Proof

Give the target inequalities dual variable \(y\ge0\), the port equality
dual variable \(\lambda\), and the fibre equation at \(o\) a free dual
variable \(\alpha_o\).  The paid-column constraints are

\[
 \alpha_o+a_{o,\gamma}\cdot y+
 g_{o,\gamma}\cdot\lambda\le0,
\tag{4.6}
\]

and the repair-column constraints are those displayed under the maximum
in (4.5).  The dual objective is

\[
                         b\cdot y+\sum_o\alpha_o.
\tag{4.7}
\]

For fixed \(y,\lambda\), maximize (4.7) by taking

\[
 \alpha_o=
 -\max_{\gamma\in\Gamma_o}
  \bigl(a_{o,\gamma}\cdot y+
        g_{o,\gamma}\cdot\lambda\bigr).
\tag{4.8}
\]

Substitution gives (4.5). \(\square\)

Thus a positive value in (4.5) is an exact fractional lower bound on the
new literal cost.  In particular, take support demands \(b_T=1\) on every
target row and binary support incidences
\(a_{o,\gamma,T}=\mathbf 1_{\{T\in\gamma\}}\).  With no port rows and one
singleton repair letter of cost one for every target,

\[
 \boxed{
 \tau_{\rm fr}
 =\max_{0\le y_T\le1}
 \left[
 \sum_Ty_T-
 \sum_o\max_{\gamma\in\Gamma_o}
       \sum_{T\in\gamma}y_T
 \right].}
\tag{4.9}
\]

The paid fibres alone give a fractional support cover if and only if

\[
 \boxed{
 \sum_Ty_T\le
 \sum_o\max_{\gamma\in\Gamma_o}
       \sum_{T\in\gamma}y_T
 \quad\hbox{for every }y\ge0.}
\tag{4.10}
\]

All nonnegative weights are required; indicator cuts alone are not
sufficient for a general configuration library.

### Corollary 4.3 (exact quota-box separation)

Suppress repair columns.  Let \(\ell,u\) be exact lower and upper quota
vectors, and retain the port equation.  Fractional feasibility is
equivalent to

\[
 \boxed{
 \sum_{y_r\ge0}\ell_ry_r+
 \sum_{y_r<0}u_ry_r
 \le
 \sum_o\max_{\gamma\in\Gamma_o}
 \bigl(a_{o,\gamma}\cdot y+
       g_{o,\gamma}\cdot\lambda\bigr)}
\tag{4.11}
\]

for every \(y\in\mathbb R^{\cal R}\) and
\(\lambda\in\mathbb R^\Pi\).

#### Proof

The left side is the minimum of \(y\cdot v\) over the box
\(\ell\le v\le u\).  The right side is the support function of the
Minkowski sum of the owner-fibre column polytopes, evaluated jointly with
the port coordinate.  Separation of this Minkowski sum from
\([\ell,u]\times\{0\}\) is exactly (4.11). \(\square\)

The exact zero-repair integral criterion for the displayed
incidence/port-balance program is the corresponding semigroup membership:

\[
 \boxed{
 \exists\,\gamma_o\in\Gamma_o\ (o\in{\cal O}):
 \quad
 \sum_oa_{o,\gamma_o}\ge b,\qquad
 \sum_og_{o,\gamma_o}=0.}
\tag{4.12}
\]

For a repair budget \(E\), add auxiliary columns whose total cost is at
most \(E\).  Unlike (4.10)--(4.11), (4.12) cannot in general be tested by
the fractional dual.

## 5. The uniform annulus dual and long rethreading

Let

\[
                         t=H-h.
\tag{5.1}
\]

In this section assume explicitly that the anchored candidate set has
\(|{\cal O}|=W\).

Fix one sign.  Give every annulus target of that sign weight \(1/t\), and
give all rows of the other sign weight zero.  One endpoint-rooted nested
flag contains at most one distinct target of the chosen sign at each
depth, so it has weight at most one.  Let

\[
 d_o=\max_{\gamma\in\Gamma_o}
       |\gamma\cap\{\text{annulus target rows of that sign}\}|.
\tag{5.2}
\]

The support dual (4.9) gives

\[
 \boxed{
 \tau_{\rm fr}\ge
 {1\over t}
 \left(\sum_{q\in Q}N_q-\sum_od_o\right).}
\tag{5.3}
\]

Separately, if \(e\) auxiliary endpoints suffice, the same incidence
capacity gives the necessary inequality

\[
 \boxed{
 \sum_od_o+et\ge\sum_{q\in Q}N_q.}
\tag{5.4}
\]

This is the common-start ledger.  It agrees numerically with the uniform
dual, but (5.4) is not a claim that every auxiliary literal endpoint is
one of the singleton repair columns used to derive (5.3).

More directly, let \(a_o\) be the number of annulus depths actually
threaded through the paid endpoint \(o\), and put

\[
 R_d=|\{o:a_o\ge d\}|.
\tag{5.5}
\]

At a fixed depth, distinct equal-rank targets have distinct witness
starts.  There are \(W\) selected middle-owner starts and only \(e\)
other word positions.  Summing this start-incidence statement through
the \(t\) annulus depths gives directly

\[
 \boxed{
 \sum_oa_o+et\ge\sum_{q\in Q}N_q.}
\tag{5.5a}
\]

Then

\[
\boxed{
R_d\ge
{\sum_{q\in Q}N_q-et-W(d-1)\over t-d+1}}
\tag{5.6}
\]

for \(1\le d\le t\), whenever the numerator is positive.  Indeed,

\[
 \sum_oa_o\le R_dt+(W-R_d)(d-1),
\tag{5.7}
\]

while (5.5a) gives the reverse lower bound.

At a lower common left endpoint, targets of \(d\) distinct ranks have
\(d\) distinct right endpoints before the middle-owner right endpoint.
Hence \(a_o\ge d\) forces that owner witness to contain at least \(d+1\)
positions.  Reversing the word gives the identical upper
common-right-endpoint conclusion.

Use the audited Gaussian estimate

\[
 N_q\ge\rho_AW,\qquad \rho_A={1\over2}e^{-A^2}.
\tag{5.8}
\]

If \(e=o(W)\), \(0<\alpha<\rho_A\), and
\(d=\lfloor\alpha t\rfloor\), then

\[
 \boxed{
 R_d\ge
 \left({\rho_A-\alpha\over1-\alpha}-o(1)\right)W.}
\tag{5.9}
\]

Taking \(\alpha=\rho_A/2\) forces density

\[
                         {\rho_A\over2-\rho_A}-o(1)
\tag{5.10}
\]

of the paid endpoints to carry \(\Theta_A(\sqrt m)\) nested annulus
depths.  This sharpens the constants in the earlier long-endpoint theorem.
It is a necessity statement, not an obstruction to the abstract flow:
Theorem 2.1 supplies enough long flags.

## 6. Nestedness is not integrality

The hourglass theorem is integral because all admissible columns are
paths in one common network.  A general owner-specific list of nested
flags need not have this property.

### Proposition 6.1 (determinant-two owner-list obstruction)

Let

\[
 X_1=\{1,2,3,4,5\},\qquad
 X_2=\{1,2,3,4,6\}.
\tag{6.1}
\]

At a shallower selected depth put

\[
 A_1=\{1,2,3\},\qquad A_2=\{1,2,4\},
\tag{6.2}
\]

and at a deeper selected depth put

\[
 B_1=\{1\},\qquad B_2=\{2\}.
\tag{6.3}
\]

Give owner \(X_1\) the two options

\[
 (A_1,B_1),\qquad(A_2,B_2),
\tag{6.4}
\]

and owner \(X_2\) the two options

\[
 (A_1,B_2),\qquad(A_2,B_1).
\tag{6.5}
\]

Every displayed pair extends through the missing intermediate ranks to a
genuine nested deletion flag.  Taking one half of each of the four
columns covers \(A_1,A_2,B_1,B_2\) exactly once.  No integral choice of
one option in each owner fibre does so.

Moreover, on rows \((X_1,X_2,A_1,B_1)\), the four columns give

\[
 \begin{pmatrix}
 1&1&0&0\\
 0&0&1&1\\
 1&0&1&0\\
 1&0&0&1
 \end{pmatrix},
\qquad |\det|=2.
\tag{6.6}
\]

#### Proof

The half--half fractional assertion is immediate.  If the two chosen
columns agree on the shallow target, the other shallow target is missed.
If they differ there, they agree on the deep target, so the other deep
target is missed.  Direct expansion gives the determinant in (6.6).
\(\square\)

The natural sufficient condition restoring integrality is
**tail-splicing rectangularity**:

> whenever two allowed partial flags reach the same target state, every
> prefix of one may be followed by every allowed suffix of the other.

Under this hypothesis the columns are precisely paths of a common
state-expanded DAG.  If the entire allowed language—including paired
signs, occurrence state, ports, and every constrained incidence
row—appears as one single-commodity network with quota rows realized as
node or arc throughputs, the extended formulation is a network polytope
and the Hoffman/TU theorem applies.  Prefix--suffix closure of bare target
flags alone does not make arbitrary provenance rows TU.  Proposition 6.1
shows that
nestedness without this Markov closure is insufficient.  The proposition
does not say that rectangularity is necessary for every accidentally
integral finite library.

## 7. Principal-baseline credit is a second matching

The owner-fibre program counts one paid root once across all depths.  To
identify that root with a deleted principal PBBS erosion position requires
another integral assignment.

Call an option \((o,\gamma)\) **ERP-active** when its use is meant to
replace, and hence earn the one-time credit of, a principal PBBS erosion
position.  The unchanged/null option and any option paid for independently
are not ERP-active.  For an ERP-active selected option \((o,\gamma)\), let

\[
                         P(o,\gamma)
\tag{7.1}
\]

be its eligible same-sign, same-parity endpoint-capped erosion slots.
Let \(d_i\in\mathbb Z_{\ge0}\) be the capacity of erosion slot \(i\)
(normally \(d_i=1\)).  Introduce matching variables

\[
 p_{o,\gamma,i}\ge0,\qquad i\in P(o,\gamma),
\tag{7.2}
\]

with

\[
 \sum_{i\in P(o,\gamma)}p_{o,\gamma,i}=x_{o,\gamma},
\tag{7.3}
\]

and

\[
 \sum_{o,\gamma}p_{o,\gamma,i}\le d_i.
\tag{7.4}
\]

Equations (7.3)--(7.4) are imposed only on the ERP-active options; all sums
in (7.3)--(7.6) below have this same scope.  For a fixed integral
owner-column selection, (7.3)--(7.4) has an integral solution if and only if
the capacitated Hall inequalities

\[
 \boxed{
 |{\cal S}|
 \le\sum_{i\in N({\cal S})}d_i
 \quad\hbox{for every selected option family }{\cal S}}
\tag{7.5}
\]

hold.  This is the exact ERP injection.

The earned deletion credit of a selected matching is

\[
 R_{\rm ERP}
 =\sum_{o,\gamma,i}p_{o,\gamma,i}
 =\sum_{o,\gamma}x_{o,\gamma}
 \le\sum_i d_i.
\tag{7.6}
\]

Each matched erosion position earns its one available credit once.  The
total available credit \(\sum_i d_i\) is also counted once, and is attained
only when all those capacities are used.  Neither quantity depends on the
number of depths served by the matched flag.  The reason separate depth
ledgers are invalid is exact.  An
interior erosion position \(D_i\) belongs, at depth \(q\), to

\[
                         H-q+1
\tag{7.7}
\]

canonical lower witness intervals and

\[
                         H+q+1
\tag{7.8}
\]

canonical upper witness intervals.  This is exactly \(2H+2\) canonical
incidences at every depth.  Deleting \(D_i\) once can earn one baseline
letter, but it can disturb all incidences (7.7)--(7.8).  The credit may
never be re-earned at another depth.  Retaining or reconstructing all
those witnesses merely prevents collateral loss from invalidating that
single credit.

Likewise, one interior or cyclic seam with its full window set lies in
exactly \(q\) depth-\(q\) owner windows.  Counting both signs, \(J\) such
seams expose

\[
 2J\sum_{q=q_0}^{H}q
 =
 J\bigl[H(H+1)-(q_0-1)q_0\bigr]
\tag{7.9}
\]

crossing occurrences.  Equation (7.9) is occurrence mass, not the length
of an optimally shared literal repair.  At a finite truncated boundary,
the corresponding count is at most (7.9).

The \(2s+3\)-letter chart for one simple two-parity PBBS return is a
genuine local example of common all-depth reuse against its \(2s+2\)
owner-occurrence slots.  It does not prove (7.5) for the principal
erosion baseline, nor reconstruct all crossing witnesses.

## 8. Exact literal interval criterion

Even an integral flag selection and ERP matching do not by themselves
produce one set-letter word.  Once proposed witness intervals have been
placed, literal realizability has an exact finite test.

Let \({\cal K}\) be the selected typed witness-occurrence set.  Occurrence
\(r\in{\cal K}\) claims the set \(T_r\), and is assigned an interval

\[
                         I_r\subseteq\{1,\ldots,L\}.
\tag{8.1}
\]

Different occurrences may claim the same underlying set; they remain
separate when quotas or provenance require distinct witnesses.

For every word position \(j\), put

\[
 A_j=\bigcap_{\substack{r\in{\cal K}\\j\in I_r}}T_r,
\tag{8.2}
\]

with \(A_j=[n]\) when no selected interval contains \(j\).

### Theorem 8.1 (cap--union realization of prescribed interval unions)

There is a nonzero set-letter word \(Z_1,\ldots,Z_L\) such that

\[
                         \bigcup_{j\in I_r}Z_j=T_r
 \qquad(r\in{\cal K})
\tag{8.3}
\]

if and only if

\[
 \boxed{
 A_j\ne\varnothing\quad(1\le j\le L),\qquad
 T_r=\bigcup_{j\in I_r}A_j\quad(r\in{\cal K}).}
\tag{8.4}
\]

#### Proof

If (8.3) holds and \(j\in I_r\), then \(Z_j\subseteq T_r\).  Hence
\(Z_j\subseteq A_j\), so \(A_j\ne\varnothing\), and

\[
 T_r=\bigcup_{j\in I_r}Z_j
 \subseteq\bigcup_{j\in I_r}A_j
 \subseteq T_r.
\tag{8.5}
\]

This proves necessity.  Conversely, if (8.4) holds, take
\(Z_j=A_j\).  The letters are nonzero and (8.3) follows. \(\square\)

The packet pin--cap overlap condition is the one-position specialization
of (8.4).  This is an iff only for finding arbitrary nonempty set letters
which realize the prescribed interval-union equations.  It does not
enforce PBBS successor, sign, parity, anchor provenance, control of
unintended occurrences, or the coefficient-one length ledger; those must
still be imposed on the proposed interval ordering.

## 9. Exact proved and open boundary

The following are proved.

1. The unrestricted owner-fibre annulus has an exact common integral
   balanced flow.  The same \(W\) abstract roots serve every depth, with
   Gaussian multiplicity at most \(e^{A^2}+1\).  This is not yet paid
   PBBS baseline credit.
2. A prescribed support-complete shallow flow extends through the annulus
   whenever all Boolean inclusion tails remain available.
3. For fixed signed cutoff pairs with optional occurrence selection and
   independently spliceable Boolean tails, the exact support-only owner
   requirement is the edge-cover number (3.4), and the general integral
   criterion for the displayed hourglass relaxation is the Hoffman system
   (3.9).
4. Equations (4.5), (4.9), and (4.11) are the exact fractional duals for
   the declared anchored incidence/port-balance libraries; physical
   gluing rows must be included if they are not internal to the columns.
5. The uniform dual forces the positive-density Gaussian rethreading in
   (5.9)--(5.10).
6. Restricted nested libraries need not be integral; Proposition 6.1 is
   an exact determinant-two obstruction.
7. Principal baseline deletion additionally requires the ERP Hall
   inequalities (7.5), with the credit counted once across all depths.
8. Once intervals are proposed, (8.4) is necessary and sufficient for
   their prescribed interval-union equations to be realized simultaneously
   by arbitrary nonzero set letters.  It is not by itself a PBBS compiler
   criterion.

The following are not proved.

1. The actual PBBS anchored libraries satisfy the target-Markov
   tail-splicing property.
2. Their simultaneous-depth integer optimum differs from the fractional
   optimum by \(o(W)\).
3. A joint lower/upper cutoff graph with the required PBBS provenance has
   edge-cover number at most \(W+o(W)\).
4. The chosen physical columns satisfy ERP, all crossing-target
   reconstruction, and the cap--union criterion in \(W+o(W)\) positions.

Thus a common nested flow genuinely removes the apparent sum over depths
at the abstract owner-fibre level.  The smallest remaining positive
criterion is a target-Markov/rectangular PBBS state expansion whose
hourglass Hoffman cuts have \(o(W)\) repair cost, followed by ERP and the
literal interval test.  A negative theorem must instead exhibit either

* a dual weight in (4.5) of value \(\Omega(W)\);
* \(\Omega(W)\) replicated integral obstruction beyond the
  determinant-two toy cell; or
* an ERP/interval cut of \(\Omega(W)\).

No such PBBS-specific certificate is currently proved.
