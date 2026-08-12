# Monotone interval schedules are exactly canonical suffix fragmentations

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact finite equivalence.  For every nondecreasing
integer rank histogram, arbitrary interval-row decompositions and
fragmentations of the canonical horizontal suffix jobs are the same object,
up to a colour-passing operation at interval boundaries.  Consequently the
heterogeneous interval gate in the coefficient-one Boolean construction is
exactly the previously isolated job/socket coagulation gate.  The theorem
does not prove that the required fragmentation exists.

## 0. Outcome

Let

\[
                    0\le n_1\le n_2\le\cdots\le n_m
\tag{0.1}
\]

be an integer histogram, and put `h=n_m`.  For `1<=a<=h`, define

\[
 s_a=\min\{s:n_s\ge a\},\qquad
 J_a=[s_a,m],\qquad L_a=|J_a|=m-s_a+1.
\tag{0.2}
\]

The intervals `J_a` are the horizontal rows of the Ferrers diagram of
`n`.  In particular,

\[
                    n_s=|\{a:s\in J_a\}|.
\tag{0.3}
\]

Fix `W>=1` heterogeneous **nonnegative integer** capacities
`c_1,...,c_W`, and
write

\[
                         D=\max_i c_i.
\tag{0.4}
\]

Empty capacity bins may be unused.  If the histogram is nonzero, the case
`D=0` is immediately infeasible and may be discarded.

The main theorem says that the following are equivalent.

1. The histogram is the coverage vector of intervals `I_1,...,I_t`,
   injectively assigned to capacity bins, with `|I_j|` at most the capacity
   of its bin.
2. Every canonical suffix job `J_a` can be cut into consecutive nonempty
   pieces, and all resulting piece lengths can be injected into the same
   capacity bins.

Thus an interval schedule cannot evade the canonical residual-chain
fragmentation problem by exchanging height labels between different ranks.
Every such exchange is merely a handoff of one canonical job colour from an
ending interval to an interval starting at the next position.

For the complete nonempty residual Boolean histogram, the canonical job
length multiset is exactly the one obtained by restricting any
symmetric-chain decomposition below the cutoff and deleting the empty set.
The unique bottom-zero chain then joins the bottom-one length class, as
recorded explicitly in Section 3.  Hence, after this common empty-set
convention, the exact heterogeneous system in
`MATH_THEOREM_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_20260804.md`
and the exact job/socket configuration system in
`MATH_THEOREM_RAYLEIGH_JOB_SOCKET_COAGULATION_EXACT_REDUCTION_20260804.md`
are not merely analogous: on the monotone complete-layer face they are
literally equivalent finite formulations.

## 1. Canonical colour-passing theorem

An **interval realization** of `n` is a finite multiset `mathcal I` of
nonempty integer intervals in `[1,m]` such that

\[
                    |\{I\in\mathcal I:s\in I\}|=n_s
                    \qquad(1\le s\le m).
\tag{1.1}
\]

### Theorem 1.1 (canonical suffix fragmentation)

Every interval realization `mathcal I` admits a colouring

\[
                         \kappa:\mathcal I\longrightarrow[h]
\tag{1.2}
\]

such that, for every colour `a`, the intervals of colour `a`, in their
natural left-to-right order, are pairwise disjoint consecutive pieces whose
union is exactly `J_a`.

Conversely, independently fragmenting every `J_a` into consecutive
nonempty pieces produces an interval realization of `n`.

Moreover, the colouring in the forward direction does not change any
interval or its length.

### Proof

Sweep the positions from left to right.  Put `n_0=0`.  Suppose the active
intervals at position `s-1` have already been coloured bijectively by

\[
                         [n_{s-1}].
\tag{1.3}
\]

At the boundary before position `s`, let `E_s` be the intervals ending at
`s-1`, let `B_s` be the intervals beginning at `s`, and let the remaining
intervals continue across the boundary.  Taking the difference of the two
coverage counts gives

\[
                         |B_s|-|E_s|=n_s-n_{s-1}\ge0.
\tag{1.4}
\]

Keep the colours of every continuing interval.  Assign `|E_s|` of the new
intervals bijectively the colours just released by `E_s`, and assign the
remaining `n_s-n_(s-1)` new intervals the new colours

\[
                         n_{s-1}+1,\ldots,n_s.
\tag{1.5}
\]

There are exactly enough intervals by (1.4).  The active colour set at
position `s` is therefore `[n_s]`, so the induction continues.  At `s=1`
the same rule simply assigns the colours `1,...,n_1`.

Fix a colour `a`.  It first becomes active precisely at the least position
`s_a` for which `n_(s_a)>=a`.  Because the active colour sets `[n_s]` are
nested and `n` is nondecreasing, colour `a` is active at every subsequent
position through `m`.  Whenever its current interval ends at `s-1`, the
construction passes the same colour to an interval beginning at `s`.
Consequently its coloured intervals are consecutive, do not overlap, and
partition `[s_a,m]=J_a`.

For the converse, (0.3) says that exactly `n_s` canonical jobs contain
position `s`.  Fragmenting a job changes neither its union nor its
pointwise coverage.  The union of all pieces therefore has coverage
vector `n`.  `square`

### Corollary 1.2 (length multiset equivalence)

Let `lambda` be any multiset of positive interval lengths.  There is an
interval realization of `n` having length multiset `lambda` if and only if
the jobs of lengths `L_1,...,L_h` can be fragmented into pieces having
aggregate length multiset `lambda`.

This is stronger than equality of total work and number of rows.  It
preserves the complete piece-length histogram.

## 2. Exact heterogeneous-capacity equivalence

### Theorem 2.1 (interval bins iff fragmented jobs fit)

The following are equivalent.

1. There are intervals `I_1,...,I_t` realizing `n` and an injection
   `phi:[t]->[W]` such that

   \[
                              |I_j|\le c_{\phi(j)}.
   \tag{2.1}
   \]

2. For every `a`, the integer `L_a` has a composition

   \[
                       L_a=\ell_{a,1}+\cdots+\ell_{a,r_a},
                       \qquad \ell_{a,j}\ge1,
   \tag{2.2}
   \]

   and all pairs `(a,j)` admit an injection `psi` into `[W]` satisfying

   \[
                              \ell_{a,j}\le c_{\psi(a,j)}.
   \tag{2.3}
   \]

### Proof

Apply Theorem 1.1 to an interval realization from item 1.  The intervals
of colour `a` partition `J_a`, so their lengths give (2.2); retain their
old bin assignments to get (2.3).

Conversely, cut `J_a` consecutively into pieces with lengths (2.2).  By
Theorem 1.1's converse these pieces realize `n`, and (2.3) assigns them to
the capacities.  `square`

Writing

\[
                         K_q=|\{i:c_i\ge q\}|,
\tag{2.4}
\]

the injection in (2.3) exists for a proposed set of compositions exactly
when

\[
              \sum_{a,j}{\bf1}_{\{\ell_{a,j}\ge q\}}\le K_q
              \qquad(q\ge1).
\tag{2.5}
\]

Thus the complete rank-only problem is the integer configuration system

\[
 \boxed{
 \begin{array}{c}
 L_a=\sum_j\ell_{a,j},\quad
 \ell_{a,j}\in\{1,\ldots,D\}\quad(a=1,\ldots,h),\\[1mm]
 \#\{(a,j):\ell_{a,j}\ge q\}\le K_q\quad(q=1,\ldots,D).
 \end{array}}
\tag{2.6}
\]

The displayed upper bound on every piece is essential.  Equivalently one
may retain (2.5) for all `q>=1` and put `K_q=0` for `q>D`.

No named Boolean set occurs in (2.6).  Once (2.6) is solved, the interval
rows lift to adaptively named skipless Boolean chains by Theorem 2.2 of
the capacitated Hall-ladder note.  Conversely, failure of (2.6) already
rules out every interval-row lift, before named containment or literal
serialization is considered.

## 3. Boolean residual jobs

Put

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad D=d(k),
 \qquad t_0=r-D,
\tag{3.1}
\]

and first take the complete residual histogram

\[
                         n_s={k\choose s},
                         \qquad 1\le s<t_0.
\tag{3.2}
\]

If `t_0<=1`, this residual histogram is empty and the statements below
are vacuous; otherwise `m=t_0-1>=1` as required by Theorem 1.1.

Use rank position `s` itself in Theorem 1.1, so `m=t_0-1`.  A canonical
job beginning at rank `b` has length

\[
                              L=t_0-b.
\tag{3.3}
\]

The number of jobs beginning at `b` is

\[
 \begin{cases}
   {k\choose1}=k,&b=1,\\[1mm]
   {k\choose b}-{k\choose b-1},&2\le b<t_0.
 \end{cases}
\tag{3.4}
\]

Indeed, these are exactly the new horizontal Ferrers rows appearing when
the column height rises from rank `b-1` to rank `b`, with the nonempty-ideal
convention `n_0=0`.  This convention matters at `b=1`: the unique
symmetric chain containing the empty set loses that element and its
remaining lower fragment has the same length `t_0-1` as a chain beginning
at rank one.  Consequently (3.3)--(3.4) are also exactly the length
histogram obtained by restricting any symmetric-chain decomposition below
`t_0` and then deleting the empty set.  If the empty set is retained
instead, the usual multiplicity
`{k\choose b}-{k\choose b-1}` applies starting at `b=0`.

### Corollary 3.1 (two formulations coincide)

For the complete residual histogram (3.2), the following rank-only
statements are equivalent.

1. The histogram has a capacity-compatible interval-row decomposition.
2. The residual pieces of an abstract symmetric-chain length histogram can
   be cut and injected into the collar capacities.
3. The integer configuration system (2.6), with job multiplicities
   (3.4), is feasible.

The equivalence is about rank lengths.  It does not require choosing one
particular symmetric-chain decomposition, and it does not assert that a
fixed residual SCD chunk is contained in a fixed collar SCD socket.

If a triangular boundary bank deletes counts `b_s` and the retained
histogram

\[
                         n_s={k\choose s}-b_s
\tag{3.5}
\]

remains nondecreasing, the same theorem applies verbatim.  Its job
multiplicities become `n_b-n_(b-1)`.  In the coefficient-one application
the boundary bank has at most `D(D+1)/2` total deletions.  Every
positive binomial gap through the residual range is at least
`C_1-C_0=k-1`, and
`D(D+1)/2=(pi/16+o(1))k<k-1`.  Hence every sufficiently large retained
instance remains nondecreasing.  This observation concerns monotonicity
only and does not prove (2.6).

For completeness, if

\[
                         \Delta_s={k\choose s}-{k\choose s-1},
\]

then a direct calculation gives

\[
 {\Delta_{s+1}\over\Delta_s}\ge1
 \quad\Longleftrightarrow\quad
                         (k-2s)^2\ge k+2.
\tag{3.6}
\]

On the residual range `s<t_0`, the asymptotic
`D=(sqrt(pi/8)+o(1))sqrt(k)` makes (3.6) strict for all sufficiently large
`k`.  Hence every positive adjacent binomial gap there is at least
`Delta_1=k-1`.  If `B=sum_s b_s<=D(D+1)/2`, then, for `s>=2`,

\[
 n_s-n_{s-1}=\Delta_s-b_s+b_{s-1}
              \ge (k-1)-B>0,
\]

while the first column satisfies `n_1-n_0=k-b_1>=k-B>0` under the
nonempty-ideal convention `n_0=0`.  This supplies the claimed monotonicity
rather than merely a comparison of total counts.

## 4. Dual boundary and exact surviving theorem

For a nonnegative price vector `theta=(theta_1,...,theta_D)`, define its
integer covering closure

\[
 \psi_\theta(L)=\min\left\{
      \sum_{q=1}^D\theta_qp_q:
      p_q\in\mathbb Z_{\ge0},\quad
      \sum_{q=1}^D qp_q\ge L
                         \right\}.
\tag{4.1}
\]

Every feasible fragmentation obeys

\[
               \sum_a\psi_\theta(L_a)
               \le\sum_{q=1}^D K_q^{=}\theta_q,
\tag{4.2}
\]

where `K_q^==|{i:c_i=q}|`.  This is the exact configuration-dual
inequality after fractional relaxation, in the following precise sense.
For a job of length `L`, call a vector
`p=(p_1,...,p_D)` a socket configuration when

\[
                         \sum_{q=1}^D qp_q\ge L.
\tag{4.3}
\]

Using more than `L` nonempty sockets is never needed: from any cover with
more than `L` sockets, retain any `L` of them, whose total capacity is still
at least `L`.  Thus every relevant configuration really can be trimmed
into positive pieces totalling `L`: start every retained socket with one
unit and distribute the remaining `L-|p|` units within the aggregate spare
capacity.

After deleting redundant sockets as above, each job has a finite set
`P_L` of configurations.  The fractional configuration LP chooses one
point of `conv(P_L)` for every job, with aggregate type-`q` socket use at
most `K_q^=`.  Equivalently, the supply vector `K^=` belongs to

\[
       \sum_a\operatorname{conv}(P_{L_a})+\mathbb R_{\ge0}^D.
\]

Separation of this closed upward polyhedron shows that the LP is feasible
if and only if (4.2) holds for **every** `theta>=0`: for fixed `theta`,
minimization separates over the jobs and gives exactly
`psi_theta(L_a)`.  An integral fragmentation gives one such configuration
per job, proving necessity directly.  The all-grid Bellman programme
studies precisely this family of inequalities; the integer problem can
additionally require a finite residue absorber.

The combined conclusions are therefore

\[
 \boxed{
 \begin{array}{c}
 \text{atomic Gale majorisation is a proper relaxation};\\
 \text{interval rows are exactly canonical suffix-job fragmentations};\\
 \text{the Gaussian coagulation/configuration dual is the exact fractional}\\
 \text{continuum form of the heterogeneous interval gate};\\
 \text{after that rank-only gate, Boolean naming is automatic on}\\
 \text{complete or co-selected layers, but run serialization is not.}
 \end{array}}
\tag{4.4}
\]

The next rank-only theorem must therefore either construct the integer
fragmentations (2.6), including the triangular residue correction, or
prove every covering-price inequality (4.2) and then supply an exact
integer absorber.  An arbitrary atomic matrix cannot replace this step.

## 5. Dependencies

1. `MATH_THEOREM_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_20260804.md`;
2. `MATH_THEOREM_CHAIN_DEPENDENT_SCD_GAUSSIAN_FRAGMENTATION_RIGIDITY_20260804.md`;
3. `MATH_THEOREM_RAYLEIGH_JOB_SOCKET_COAGULATION_EXACT_REDUCTION_20260804.md`;
4. `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md`.
