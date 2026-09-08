# A root-lattice buffer makes whole-job configuration rounding exact

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional finite **anonymous tail-rounding** theorem under an
explicit buffered fractional-feasibility premise.  A two-state bank of short
jobs realizes the entire zero-work lattice of socket-tail discrepancies.  It
converts the at most `D` split jobs of a configuration extreme point into an
exact integral tail packing at the **same** depth.  This does not name the
physical socket occurrences or prove their containment incidences.  What is
not proved here is that the critical Boolean/Rayleigh fractional point
contains the required bank with the exact dual margin stated in Section 5.

## 1. Configuration vectors and the elementary exchange

Fix a maximum socket capacity `D>=2`.  A fragmentation of a job of length
`L` has conjugate tail vector

\[
 p=(p_1,\ldots,p_D)\in\mathbb Z_{\ge0}^D,qquad
 p_1\ge\cdots\ge p_D,\qquad \sum_{q=1}^Dp_q=L.    \tag{1.1}
\]

For `1<=j<=D`, let

\[
 u^{(j)}=(\underbrace{1,\ldots,1}_{j},0,\ldots,0) \tag{1.2}
\]

be the vector of the one-piece configuration `(j)`.  For `2<=j<=D`, let

\[
 v^{(j)}=u^{(j-1)}+u^{(1)}                        \tag{1.3}
\]

be the vector of the two-piece configuration `(j-1,1)` of the same
length-`j` job.  Then

\[
 \boxed{v^{(j)}-u^{(j)}=e_1-e_j.}                 \tag{1.4}
\]

The vectors on the right generate the complete integer zero-work lattice

\[
 \mathsf A_{D-1}=
 \{z\in\mathbb Z^D:\sum_{q=1}^Dz_q=0\}.          \tag{1.5}
\]

Indeed, for `z in A_(D-1)`,

\[
 z=\sum_{j=2}^D(-z_j)(e_1-e_j).                  \tag{1.6}
\]

Thus the local split/merge `(j) <-> (j-1,1)` is not merely one useful
trade: it is an integer basis for every aggregate tail error compatible
with conservation of total job length.

## 2. The buffered instance

Let the complete job family be split into a residual family `R` and a
buffer.  Let `K in Z_(>=0)^D` be the complete socket-tail vector.  For each
`2<=j<=D`, the buffer contains

* `R_j` labelled length-`j` jobs in base state `u^(j)`; and
* `R_j` labelled length-`j` jobs in base state `v^(j)`.

Put

\[
 B=\sum_{j=2}^DR_j\bigl(u^{(j)}+v^{(j)}\bigr),
 \qquad K'=K-B.                                   \tag{2.1}
\]

Assume `K'>=0` coordinatewise.  The residual configuration LP has one convex
choice of a fragmentation for each residual job and the tail inequalities

\[
             \sum_{a,p}x_{a,p}p_q\le K'_q\qquad(1\le q\le D).
\]

Assume this LP is feasible and that

\[
 \sum_{a\in\mathcal R}L_a=\sum_{q=1}^DK'_q.       \tag{2.2}
\]

Then its aggregate use is automatically exactly `K'`: every fragmentation
of a length-`L_a` job has coordinate sum `L_a`, every coordinate use is at
most `K'_q`, and the sums of the two vectors agree by (2.2).  Equivalently,
one may assume exact aggregate use directly and omit (2.2).

Let

\[
                         L_{\max}=max_{a\in\mathcal R}L_a.   \tag{2.3}
\]

## 3. Exact buffered rounding

### Theorem 3.1 (root-lattice buffered exact rounding)

Under the hypotheses of Section 2, all residual and buffer jobs admit an
integral fragmentation using exactly the complete tail vector `K`, provided

\[
 \boxed{R_j\ge\left\lceil {D L_{\max}\over j}\right\rceil
        \qquad(2\le j\le D).}                     \tag{3.1}
\]

More generally, if an extreme residual solution has at most `E` split jobs,
it is enough to take

\[
                         R_j\ge\left\lceil {E L_{\max}\over j}\right\rceil.
                                                               \tag{3.2}
\]

#### Proof

Choose an extreme point of the residual configuration LP.  There is one
equality for every residual job and at most `D` independent active aggregate
tail rows.  If more than `D` jobs were split, choosing one positive
configuration as a reference in each such job would give more than `D`
within-job difference directions.  A nonzero linear combination would
annihilate every active aggregate row and every job row; a sufficiently
small signed perturbation would preserve nonnegativity and all inactive
inequalities, contradicting extremality.  Hence at most `D` jobs have more
than one positive configuration.  Every other job is already integral.

For each split job choose arbitrarily one configuration from its positive
support.  Let `P` be the resulting integral aggregate residual tail and put

\[
                              e=P-K'.              \tag{3.3}
\]

Every configuration `p` of a length-`L` job satisfies

\[
                              0\le p_j\le {L\over j},          \tag{3.4}
\]

because every piece counted by `p_j` has length at least `j`.  The
fractional mean configuration satisfies the same interval.  Therefore one
split job changes coordinate `j` by at most `L/j`, and

\[
                              |e_j|\le {D L_{\max}\over j}
                              \qquad(1\le j\le D). \tag{3.5}
\]

Both `P` and `K'` have coordinate sum equal to the total residual job
length, so

\[
                              \sum_{j=1}^De_j=0.   \tag{3.6}
\]

For every `j>=2`, perform the following buffer switches.

* If `e_j>0`, switch `e_j` of the base-`u^(j)` jobs to `v^(j)`.
* If `e_j<0`, switch `-e_j` of the base-`v^(j)` jobs to `u^(j)`.

The supply condition (3.1) and (3.5) make every switch possible.  By
(1.4), the total change made by the buffer is

\[
 \Delta=\sum_{j=2}^De_j(e_1-e_j).                 \tag{3.7}
\]

For `j>=2`, its coordinate is `Delta_j=-e_j`, while by (3.6)

\[
                              \Delta_1=\sum_{j=2}^De_j=-e_1.  \tag{3.8}
\]

Thus `Delta=-e`.  The rounded residual use `K'+e`, together with the
switched buffer use `B-e`, is exactly `K`.  Every selected vector is an
integer fragmentation of its own whole job, so the complete packing is
integral.  The proof with `E` in place of `D` is identical. `square`

### Proposition 3.2 (exact anonymous socket interpretation)

Suppose `K` is the conjugate tail of an actual multiset of socket
capacities.  An aggregate fragmentation tail equal to `K` has exactly the
same multiplicity of every piece length as that socket multiset has of the
corresponding capacity.  Hence the pieces can be bijected to the sockets by
equal length.

This conclusion is anonymous.  It does **not** say that a prescribed piece
top is contained in the bottom set of its matched Boolean socket occurrence,
nor that the sockets can be placed on one protected chronology.

#### Proof

With `K_(D+1)=0`, the number of pieces of length exactly `q` is
`K_q-K_(q+1)`, which is also the number of sockets of capacity exactly `q`.
Match within every exact-length class. `square`

### Corollary 3.3 (polynomial bank size)

Choose the minimal values
`R_j=ceil(D L_max/j)` in (3.1).  The buffer then uses

\[
 2\sum_{j=2}^DR_j
 \le 2DL_{\max}\sum_{j=2}^D{1\over j}+2D         \tag{3.9}
\]

jobs.  Hence it has size

\[
                         O(DL_{\max}\log D).       \tag{3.10}
\]

In the central Boolean regime `D=Theta(sqrt(k))` and `L_max=O(k)`, this is
`O(k^(3/2)log k)`.  Its total work is at most

\[
 2\sum_{j=2}^DjR_j=O(D^2L_{\max})=O(k^2).        \tag{3.11}
\]

Both quantities are polynomial and hence exponentially smaller than the
near-central Boolean birth cohorts which would supply these short jobs.
This count comparison alone does not prove that removing the designated
jobs preserves fractional feasibility.

## 4. Exact anonymous same-depth consequence; named coefficient zero remains open

Let the optimal-depth Boolean configuration instance have job
multiplicities `(N_L)` and socket tail `K`.  Theorem 3.1 gives the following
precise sufficient condition for zero **anonymous rounding** charge.

### Buffered fractional interior condition `BFI_D`

There is a feasible fractional configuration point which, after fixing
`R_j` jobs of length `j` in each of the two states `u^(j),v^(j)` for every
`2<=j<=D`, leaves a feasible residual instance with exact residual tail
`K'`, where (3.1) holds.

### Corollary 4.1

`BFI_D` implies an exact **anonymous** integral whole-job fragmentation at
the original depth `D`, using the complete aggregate tail `K`.  Thus the
adjacent-depth absorber is unnecessary for anonymous configuration
integrality.

It does **not** by itself close the named lower collar.  At critical work the
fragmentation may use every socket.  The existing MLD--Holder argument needs
a positive unused occurrence reserve to force all pointwise containment
Hall inequalities, and exact aggregate tails do not provide that reserve.
To obtain a named collar one still needs either

1. a separate exact zero-slack named-matching theorem; or
2. a physical tail `K+Delta` with a proved empty reserve `Delta`, while
   applying `BFI_D` to the reduced tail `K`.

Even then, protected trace flow and upper serialization remain separate.

## 5. The remaining analytic margin theorem

Raw cohort abundance does not prove `BFI_D`.  At critical total work, every
socket is priced, and forcing the bank jobs into the particular base tails
`B` can cross a nontrivial configuration facet.  The exact criterion is as
follows.

Let `J=R disjoint_union G`, where `G` is the labelled bank.  For every job
`a`, let `P_a` be its finite configuration menu and define

\[
 m_a(\theta)=\min_{p\in P_a}\langle\theta,p\rangle
 \qquad(\theta\in\mathbb R_{\ge0}^D).             \tag{5.1}
\]

For a bank job `a`, write `bar p_a` for its designated base state (`u^(j)`
or `v^(j)`).  Define the complete-instance dual slack and bank opportunity
cost

\[
 \begin{aligned}
 S_J(\theta)
   &=\langle\theta,K\rangle-\sum_{a\in J}m_a(\theta),\\
 \Pi_G(\theta)
   &=\sum_{a\in G}
       \bigl(\langle\theta,\bar p_a\rangle-m_a(\theta)\bigr).
 \end{aligned}                                    \tag{5.2}
\]

Then the residual fractional instance against `K-B` is feasible if and only
if

\[
                 \boxed{S_J(\theta)\ge\Pi_G(\theta)
                 \quad\hbox{for every }\theta\ge0.}          \tag{5.3}
\]

Indeed, its exact dual slack is

\[
 \langle\theta,K-B\rangle-\sum_{a\in R}m_a(\theta)
   =S_J(\theta)-\Pi_G(\theta),                    \tag{5.4}
\]

and the standard separating-hyperplane dual for a Minkowski sum of finite
configuration polytopes says that nonnegativity of (5.4) for all
nonnegative prices is equivalent to the tail inequalities being feasible.

Both terms in (5.3) are invariant under adding a constant multiple of the
all-ones workload price, and are positively homogeneous.  Thus every
nonconstant price may be normalized to the compact projective section

\[
 \mathcal P_D=\{\theta\in\mathbb R_{\ge0}^D:
                 \min_q\theta_q=0,\ \max_q\theta_q=1\}.      \tag{5.5}
\]

Constant prices give equality on both sides.  On `mathcal P_D`, a
length-`j` bank job pays opportunity cost at most `j`, so

\[
 \Pi_G(\theta)\le2\sum_{j=2}^DjR_j
                 =O(D^2L_{\max}).                \tag{5.6}
\]

Consequently the proof-safe quantitative sufficient condition is

\[
 \inf_{\theta\in\mathcal P_D}S_J(\theta)
       \ge 2\sum_{j=2}^DjR_j.                    \tag{5.7}
\]

More sharply, one may prove the pointwise inequality (5.3).  In a Boolean
asymptotic, a uniform positive **normalized slack density**
`S_J(theta)/W>=epsilon` on (5.5) would dominate the polynomial right-hand
side.  Mere all-price nonnegativity, or a positive raw slack not known to
scale with `W`, does not.

Thus the same-depth lower target is now sharply split into:

1. **all-price nonnegativity** for the complete instance;
2. the stronger exact bank inequality (5.3), for example via the normalized
   quantitative margin (5.7); and
3. Theorem 3.1, which performs exact integer rounding.

No further anonymous integer-normality or Graver-basis assertion is needed
after these rows.  The buffered fractional-interior and physical naming
hypotheses remain substantive.

## 6. Scope

The finite lattice theorem is exact at the anonymous tail level.  It does
not prove `BFI_D`, (5.3), the all-price Rayleigh inequality, a physical
socket-occurrence bank, zero-slack named containment Hall, a boundary-bank
realization, protected serialization, `B(k)+O(1)`, or `nu(k)=B(k)`.  It
identifies a concrete route by which sufficiently strong quantitative
fractional slack could remove anonymous configuration-rounding exceptions
at the original depth.  Further exact named and physical theorems are still
needed before this becomes a coefficient-zero OR-word argument.
