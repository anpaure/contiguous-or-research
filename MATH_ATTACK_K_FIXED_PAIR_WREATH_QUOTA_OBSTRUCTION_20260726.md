# Fixed-pair wreath orbits and the exact balanced-quota obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver,
entropy heuristic, or web input is used.

## 0. Verdict

Let

\[
 \Omega=\{\infty\}\sqcup P_1\sqcup\cdots\sqcup P_m,
 \qquad |P_i|=2,
 \qquad n=2m+1,                                      \tag{0.1}
\]

and let

\[
                         G_m=C_2^m\rtimes S_m        \tag{0.2}
\]

swap the two coordinates inside each pair and permute the pairs, while
fixing `infinity`.

There are two different conclusions.

1. **Symmetry alone has no fractional quota obstruction.**  At every
   depth `q`, the `G_m`-fixed part of the fractional balanced-quota
   polytope is nonempty.  The constant high-quota density

   \[
                 x_{\varepsilon,f}={\rho_q\over N_q}             \tag{0.3}
   \]

   on every target orbit is an exact solution.  An integral quota which
   is fully `G_m`-invariant exists exactly when `rho_q` is a subset sum of
   the target-orbit sizes.  Even if this arithmetic condition fails, an
   exact balanced quota can break invariance inside only one orbit, of
   size `O_A(W/sqrt(m))=o_A(W)` uniformly for `q<=A sqrt(m)`.

   There is nevertheless an exact integral state obstruction.  If
   `m=p` is an odd prime and `1<=q<=p-2`, every target orbit has size
   divisible by `p`, while `W=binom(2p+1,p)=2 mod p`.  Hence no literal
   integral depth-`q` histogram, and no integral balanced high family, can
   be pointwise invariant under the full wreath group.  This congruence
   obstruction disappears fractionally and has no `Omega(W)` stability.

2. **The native fixed-pair flow has a macroscopic statewise
   obstruction.**  A pair-geodesic depth-`q` window preserves the
   infinity bit and the number of full pairs.  If every middle owner is
   used once, the total mass forced into target orbit `(epsilon,f)` is
   `V_(epsilon,f)`, whereas that orbit has `T_(epsilon,f,q)` targets.  Put

   \[
   c_q=\left\lfloor{W\over N_q}\right\rfloor,
   \qquad \rho_q=W-c_qN_q.                            \tag{0.4}
   \]

   Let

   \[
   E_{m,q}=\sum_{\varepsilon,f:\ m-\varepsilon-2f<q}
                  V_{\varepsilon,f}                  \tag{0.5a}
   \]

   be the mass of source types having fewer than `q` split pairs.  Treat
   these ineligible starts as a formal zero-capacity cemetery type.  The
   exact missing- and excess-quota masses of the augmented native ledger
   are

   \[
   D^-_{m,q}=\sum_{\varepsilon,f}
       (c_qT_{\varepsilon,f,q}-V_{\varepsilon,f})_+,
   \qquad
   D^+_{m,q}=E_{m,q}+\sum_{\varepsilon,f}
       (V_{\varepsilon,f}-(c_q+1)T_{\varepsilon,f,q})_+,          \tag{0.5}
   \]

   where both displayed sums range only over valid target types
   `m-epsilon-2f>=q`.

   For the cemetery-augmented ideal native histogram `mu_q` and every
   integral balanced quota `beta_q` (extended by zero on the cemetery),
   one has the sharp orbit-level lower bound (attained in the orbit
   relaxation)

   \[
   \boxed{
     {1\over2}\|\mu_q-\beta_q\|_1
       \ge\max\{D^-_{m,q},D^+_{m,q}\}.}               \tag{0.6}
   \]

   The right side is not a tail artefact.  If

   \[
                             q=A\sqrt m+O(1),\qquad A>0,           \tag{0.7}
   \]

   then there is an explicit `kappa_A>0` such that

   \[
   \boxed{
    \liminf_{m\to\infty}{1\over W}
      \max\{D^-_{m,q},D^+_{m,q}\}\ge\kappa_A>0.}     \tag{0.8}
   \]

   Hence a construction which changes the native orbit type on only
   `o(W)` starts retains `Omega_A(W)` balanced-quota overload at this
   single depth.  Escaping the obstruction requires a positive density of
   cross-type windows, pair-frame changes, or genuinely non-pair-geodesic
   seams.

Thus the fixed-pair wreath symmetry is not itself the obstruction.  The
obstruction is the exact type-flow equation carried by a single pair
frame.

## 1. Complete target-orbit classification

For `S subset Omega`, let

\[
 \varepsilon(S)=1_{\{\infty\in S\}},
 \qquad f(S)=\#\{i:P_i\subseteq S\},
 \qquad h(S)=\#\{i:|P_i\cap S|=1\},                  \tag{1.1}
\]

and let `e(S)` count empty pairs.  If `|S|=m-q`, then

\[
 2f+h+\varepsilon=m-q,
 \qquad f+h+e=m.                                     \tag{1.2}
\]

Consequently

\[
 h=m-q-\varepsilon-2f,
 \qquad e=f+q+\varepsilon.                           \tag{1.3}
\]

The valid indices are

\[
 \varepsilon\in\{0,1\},
 \qquad
 0\le f\le\left\lfloor{m-q-\varepsilon\over2}\right\rfloor.   \tag{1.4}
\]

### Theorem 1.1 (odd fixed-pair wreath orbits)

Two rank-`m-q` targets are in the same `G_m`-orbit if and only if they
have the same pair `(epsilon,f)`.  The orbit size is

\[
 \boxed{
 T_{\varepsilon,f,q}
 = {m!\over
      f!(f+q+\varepsilon)!
      (m-q-\varepsilon-2f)!}
      2^{m-q-\varepsilon-2f}.}                       \tag{1.5}
\]

#### Proof

The two displayed statistics are invariant.  Conversely, a pair
permutation aligns the full, empty, and split pair-index sets, and the
independent `C_2` swaps align the chosen endpoints in all split pairs.
This proves transitivity.

The stabilizer has order

\[
 2^{2f+q+\varepsilon}
 f!(f+q+\varepsilon)!
 (m-q-\varepsilon-2f)! .                             \tag{1.6}
\]

Indeed, the internal swap of a full or empty pair fixes the target, while
the swap of a split pair does not.  Divide
`|G_m|=2^m m!` by (1.6) to obtain (1.5). \(\square\)

Summing (1.5) gives the complete target count

\[
                  \sum_{\varepsilon,f}T_{\varepsilon,f,q}
                  =N_q:=\binom{2m+1}{m-q}.           \tag{1.7}
\]

At the middle rank `q=0`, the corresponding source orbit size is

\[
 \boxed{
 V_{\varepsilon,f}
 = {m!\over f!(f+\varepsilon)!
             (m-\varepsilon-2f)!}
       2^{m-\varepsilon-2f}.}                        \tag{1.8}
\]

Hence

\[
                     \sum_{\varepsilon,f}V_{\varepsilon,f}
                     =W:=\binom{2m+1}{m}.            \tag{1.9}
\]

Complementation sends `(epsilon,f,h,e)` to
`(1-epsilon,e,h,f)` and supplies the corresponding upper-target orbit
classification at rank `m+1+q`.  No upper-depth indexing convention is
needed for the lower obstruction below.

If the ground set consists of exactly `m` pairs and has no distinguished
coordinate, suppress `epsilon`.  Then

\[
 (f,h,e)=(f,m-2f-q,f+q),
 \qquad
 T_{f,q}={m!2^{m-2f-q}\over
              f!(f+q)!(m-2f-q)!},                   \tag{1.10}
\]

which is the usual even fixed-frame orbit census.  Every theorem below
has this specialization; the odd form is retained because it is the
literal middle-wreath setting.

## 2. What symmetry alone does and does not force

At depth `q`, let

\[
 c=c_q=\left\lfloor{W\over N_q}\right\rfloor,
 \qquad \rho=\rho_q=W-cN_q.                          \tag{2.1}
\]

A balanced quota is `beta(S)=c+x(S)`, where

\[
 x(S)\in\{0,1\},
 \qquad \sum_Sx(S)=\rho.                             \tag{2.2}
\]

Its fractional convex hull is the hypersimplex

\[
 \mathcal H_q=\left\{x\in[0,1]^{N_q}:\sum_Sx(S)=\rho\right\}.    \tag{2.3}
\]

Intersecting (2.3) with the `G_m`-fixed subspace makes `x` constant on
each orbit.  Thus the exact orbit-level equations are

\[
 0\le x_{\varepsilon,f}\le1,
 \qquad
 \sum_{\varepsilon,f}T_{\varepsilon,f,q}
            x_{\varepsilon,f}=\rho.                  \tag{2.4}
\]

### Proposition 2.1 (fractional compatibility)

The system (2.4) is always feasible.  The constant assignment

\[
                         x_{\varepsilon,f}={\rho\over N_q}        \tag{2.5}
\]

is an exact solution.

Equivalently, choose a uniformly random `rho`-subset of all targets and
put the upper quota on it.  Its law is `G_m`-invariant and its expected
quota is (2.5).  This is an exact finite averaging identity, not an
entropy argument.

There is also a simultaneous nested fractional realization.  Given a
middle set `X`, choose a uniformly random ordering of its `m` elements and
delete the first `q`.  For a fixed lower target `S` of size `m-q`, the
number of pairs `(X,D)` with `X\setminus D=S` and `|D|=q` is

\[
                         \binom{m+1+q}{q}.            \tag{2.6}
\]

Since there are `binom(m,q)` possible deleted `q`-sets in each `X`, the
fractional load of every target is exactly

\[
 {\binom{m+1+q}{q}\over\binom mq}
       ={W\over N_q}=c_q+{\rho_q\over N_q}.          \tag{2.7}
\]

The same random ordering supplies all depths simultaneously, and its law
is invariant under the full symmetric group, hence under `G_m`.  Upper
depths follow by the complementary insertion ordering.  Thus even nested
fractional capacities have no wreath-symmetry defect; the kernel crosses
the native full-pair types.

An integral quota fixed pointwise by `G_m` must put the upper quota on
whole target orbits.  Therefore it exists if and only if

\[
             \boxed{
             \rho=\sum_{(\varepsilon,f)\in I}
                    T_{\varepsilon,f,q}}
                                                               \tag{2.8}
\]

for some set `I` of orbit indices.  This subset-sum condition is the whole
arithmetic obstruction from quota invariance alone.

It is not macroscopic.  For every fixed `A`, uniformly for
`q<=A sqrt(m)`,

\[
       \max_{\varepsilon,f}T_{\varepsilon,f,q}
          =O_A\left({N_q\over\sqrt m}\right)
          =O_A\left({W\over\sqrt m}\right).          \tag{2.9}
\]

To see (2.9), divide consecutive terms in (1.5):

\[
 {T_{\varepsilon,f+1,q}\over T_{\varepsilon,f,q}}
 ={h(h-1)\over
   4(f+1)(f+q+\varepsilon+1)},
 \qquad h=m-q-\varepsilon-2f.                        \tag{2.10}
\]

The sequence is unimodal, its mode lies at `m/4+O_A(sqrt(m))`, and on a
fixed positive multiple of `sqrt(m)` consecutive indices about the mode
the ratios in (2.10) keep every term within a constant factor of the
maximum.  Their sum is at most `N_q`, proving (2.9).

Order the target orbits arbitrarily and add their sizes until the running
sum first reaches `rho`.  Put upper quota on every earlier whole orbit and
on exactly the remaining number of targets in the crossing orbit.  This
is an exact balanced quota, and it breaks `G_m`-invariance on at most the
quantity in (2.9).  Therefore failure of (2.8) cannot by itself impose an
`Omega(W)` coefficient-one toll.  This one-orbit repair concerns the
ordinary balanced-quota polytope; it need not satisfy the extra point
margins of an exact factor histogram, which are classified below.

### Proposition 2.2 (exact integral divisibility obstruction)

Put `k=m-q`.  On the epsilon-sector, every `G_m` target-orbit size is
divisible by

\[
 D_\varepsilon={m\over\gcd(m,k-\varepsilon)}.        \tag{2.11}
\]

Across both sectors every orbit size is divisible by

\[
D={m\over\gcd(m,k(k-1))}.                           \tag{2.12}
\]

Since `k=m-q`, the denominator is also `gcd(m,q(q+1))`.

#### Proof

Use the cyclic subgroup which rotates the `m` pair labels.  If a target
has cyclic period `L|m`, it consists of `m/L` repetitions, so
`m/L` divides its number `k-epsilon` of selected paired coordinates.
Hence its cyclic orbit length `L` is divisible by (2.11).  A cyclic orbit
partitions every full `G_m`-orbit, so (2.11) divides the latter.  Taking
the greatest common divisor of the two epsilon-sector divisors and using
`gcd(k,k-1)=1` gives (2.12). \(\square\)

A `G_m`-invariant integral histogram must therefore have epsilon-sector
masses divisible by `D_epsilon`.  A depth-`q` cyclic-factor histogram has
the exact sector masses, with
`Cat_m=W/(2m+1)`,

\[
          M_1=k\operatorname{Cat}_m,
          \qquad
          M_0=(2m+1-k)\operatorname{Cat}_m,           \tag{2.13}
\]

because every cyclic order has exactly `k` length-`k` windows containing
`infinity`.  These divisibilities are necessary for a fully invariant
literal factor histogram.

In particular, let `m=p` be an odd prime and
`1<=q<=p-2`.  Then both divisors in (2.11) equal `p`, so every target
orbit has size divisible by `p`.  Lucas's theorem gives

\[
 W=\binom{2p+1}{p}\equiv2\pmod p.                    \tag{2.14}
\]

Thus no integral `G_p`-invariant histogram of total mass `W` exists at
that depth.  Also `N_q` is a sum of orbit sizes and hence is `0 mod p`,
so

\[
                         \rho_q=W-c_qN_q\equiv2\pmod p.           \tag{2.15}
\]

It cannot be the size of a union of target orbits; no exactly
`G_p`-invariant balanced quota exists either.

For a balanced quota which is meant to equal an exact cyclic-factor
histogram, there is a sharper point-margin criterion.  The numbers of
rank-`k` targets containing and avoiding `infinity` are

\[
 N_1={k\over n}N_q,
 \qquad N_0={n-k\over n}N_q.                         \tag{2.16}
\]

Every factor histogram has the sector masses in (2.13).  If its loads are
`c_q` or `c_q+1`, the numbers of high targets in the two sectors are forced
to be

\[
 h_1={k\rho_q\over n},
 \qquad h_0={(n-k)\rho_q\over n}.                    \tag{2.17}
\]

Therefore an integral `G_m`-invariant, point-regular balanced ledger exists
exactly when these two numbers are integers and there are bits
`z_(epsilon,f) in {0,1}` satisfying

\[
 \sum_fT_{1,f,q}z_{1,f}=h_1,
 \qquad
 \sum_fT_{0,f,q}z_{0,f}=h_0.                         \tag{2.18}
\]

In particular `D_epsilon|h_epsilon` is necessary.  Fractionally,
`z_(epsilon,f)=rho_q/N_q` solves both equations exactly by (2.16), and
the resulting high-set expectation has the correct margin at every
coordinate.  Thus the strengthened point ledger also has no fractional
obstruction.

Greedy selection performed separately in the two epsilon strata realizes
the exact high counts (2.17) while splitting at most one orbit in each
stratum.  By (2.9) the combined exceptional support is still
`O_A(W/sqrt(m))`.  The two partial orbits need not be point-regular among
the ordinary coordinates; that final integral design condition is not
settled by orbit capacity alone.

This is a genuine statewise symmetry obstruction, but it is not an
`Omega(W)` obstruction.  Equations (2.5), (2.7), and (2.9) show that it
vanishes fractionally and can be localized to `o(W)` targets by breaking
symmetry in one orbit.

Finally, the nested fractional kernel cannot usually be made into a
deterministic equivariant selector.  If a middle set `X` has type
`(epsilon,f,h,e)`, its stabilizer has coordinate orbits inside `X` of
sizes `epsilon`, `2f`, and `h`.  An equivariantly selected deleted
`q`-set must be a union of these blocks.  Necessarily

\[
 q\in\{\alpha\varepsilon+2\beta f+\gamma h:
          \alpha,\beta,\gamma\in\{0,1\}\}.           \tag{2.19}
\]

If `m>3q`, take the infinity-absent middle type `f=e=q` and
`h=m-2q>q`.  No nonempty union of its stabilizer blocks has size `q`.
Thus no deterministic `G_m`-equivariant depth-`q` deletion selector exists
on all middle sets.  In particular, for the typical regime
`f=m/4+O(sqrt(m))`, `h=m/2+O(sqrt(m))`, and
`q=O(sqrt(m))`, no such union has size `q` (apart from vacuous exceptional
parameters).  Deterministic statewise equivariance fails even though the
stochastic fractional kernel is exact.

## 3. Exact projection onto balanced orbit capacities

The following finite lemma isolates every statewise obstruction which can
be read solely from prescribed orbit masses.

Let the target orbits have sizes `T_j`, and prescribe nonnegative integral
occurrence masses `M_j` satisfying

\[
                         \sum_jM_j=W.                 \tag{3.1}
\]

Put

\[
 D^-(M)=\sum_j(cT_j-M_j)_+,
 \qquad
 D^+(M)=\sum_j(M_j-(c+1)T_j)_+.                      \tag{3.2}
\]

### Theorem 3.1 (sharp orbit-capacity projection)

Among all nonnegative integral histograms `mu` with

\[
                 \sum_{S\in\mathcal O_j}\mu(S)=M_j              \tag{3.3}
\]

and all integral balanced quotas `beta`, one has the exact minimum

\[
 \boxed{
 \min_{\mu,\beta}{1\over2}\|\mu-\beta\|_1
       =\max\{D^-(M),D^+(M)\}.}                      \tag{3.4}
\]

Because both histograms have total mass `W`, this half-`l_1` distance is
also the exact one-sided quota overload
`sum_S(mu(S)-beta(S))_+`.

In particular, the orbit capacities are fractionally compatible with
balanced quotas if and only if

\[
                         cT_j\le M_j\le(c+1)T_j
                         \qquad\hbox{for every }j.    \tag{3.5}
\]

#### Proof

For a quota `beta`, put

\[
                         B_j=\sum_{S\in\mathcal O_j}\beta(S).
\]

Then

\[
 cT_j\le B_j\le(c+1)T_j,
 \qquad \sum_jB_j=W.                                 \tag{3.6}
\]

On orbit `j`, the `l_1` distance is at least `|M_j-B_j|`.  Since the two
global masses agree, the total positive and negative orbit-mass
differences agree.  Every index with `M_j<cT_j` forces at least
`cT_j-M_j` negative mass, while every index with
`M_j>(c+1)T_j` forces at least `M_j-(c+1)T_j` positive mass.  This proves
the lower bound by the maximum in (3.4).

For equality, first clamp `M_j` to the interval
`[cT_j,(c+1)T_j]`.  If `D^+>=D^-`, the clamped totals fall short of `W`
by `D^+-D^-`; increase clamped coordinates, within their upper bounds, by
exactly this integral amount.  The available slack is sufficient because
the upper endpoint totals at least `W`.  The case `D^- > D^+` is
symmetric.  This produces integral `B_j` satisfying (3.6) and

\[
             {1\over2}\sum_j|M_j-B_j|=max\{D^-,D^+\}.            \tag{3.7}
\]

Give exactly `B_j-cT_j` targets of orbit `j` upper quota.  Finally choose
an integral histogram of mass `M_j` which agrees with that quota except
for `|M_j-B_j|` units; this is possible by adding surplus units or deleting
quota units inside the orbit.  Equality follows. \(\square\)

If the histogram itself is required to be `G_m`-invariant, then it has
the constant integral value `M_j/T_j` on orbit `j`; hence the additional
divisibility condition

\[
                              T_j\mid M_j             \tag{3.8}
\]

is necessary and sufficient.  This is an integral symmetry condition, not
a fractional capacity condition.

If the prescribed masses and quota are additionally required to share the
exact two infinity-sector totals (2.13), equivalently the high counts
(2.17), the clipping problem separates by `epsilon`.  With

\[
 D^-_\varepsilon=\sum_f(cT_{\varepsilon,f,q}-M_{\varepsilon,f})_+,
 \qquad
 D^+_\varepsilon=\sum_f(M_{\varepsilon,f}-(c+1)T_{\varepsilon,f,q})_+,
                                                               \tag{3.9}
\]

the exact orbit-relaxed minimum becomes

\[
             \sum_{\varepsilon=0}^1
                   \max\{D^-_\varepsilon,D^+_\varepsilon\}.      \tag{3.10}
\]

This follows by applying the same clamping proof independently in the two
strata.  Integral ordinary-coordinate point regularity may impose further
labelled conditions, so (3.10) is the sharp orbit relaxation, not a factor
realization theorem.

The projection formula also permits a formal zero-capacity cemetery cell:
take its interval to be `[0,0]` and place mass `E` on it.  It contributes
exactly `E` to `D^+`.  The clamping proof is unchanged.  This convention
will keep the native finite ledger exact when some source types have no
depth-`q` pair-geodesic window.

## 4. The native fixed-pair type-flow identity

Let

\[
 \mathcal I_q=\left\{(\varepsilon,f):m-\varepsilon-2f\ge q\right\}          \tag{4.0}
\]

be the source types with at least `q` split pairs.  A source outside
`mathcal I_q` has no distinct-direction pair-geodesic depth-`q` window.
Its total mass is the number `E_(m,q)` in (0.5a).  Adjoin a formal type
`partial` with

\[
 T_\partial=0,
 \qquad V_\partial=E_{m,q}.                          \tag{4.0a}
\]

Then the genuine eligible source masses together with the cemetery mass
sum exactly to `W`.

For every fixed `A` and `q<=A sqrt(m)`,

\[
                         E_{m,q}=e^{-\Omega_A(m)}W.    \tag{4.0b}
\]

Indeed, under the source weights (1.8) the split-pair count is
`m/2+O(sqrt(m))`; the event that it is below `A sqrt(m)` is a linear
large-deviation tail.  Applying Stirling's two-sided factorial bounds
directly to (1.8) gives (4.0b).  No Gaussian constant below is changed.

Consider a depth-`q` geodesic window which flips `q` distinct coordinate
pairs in one fixed pair frame.  Its lower intersection:

* preserves `infinity` membership;
* preserves every source-full pair;
* turns the `q` flipped source-split pairs into empty pairs; and
* preserves the orientations of all unflipped split pairs.

It therefore maps source type `(epsilon,f)` to target type
`(epsilon,f,q)`.  If every eligible middle owner contributes one such
start, double counting gives the resolution-independent identity

\[
 \boxed{
 \sum_{S\in\mathcal O_{\varepsilon,f,q}}\mu_q(S)
       =V_{\varepsilon,f}.}                           \tag{4.1}
\]

for every `(epsilon,f) in mathcal I_q`; the ineligible sources occupy
`partial`.

The orbit-average load is consequently

\[
 \boxed{
 \lambda_{\varepsilon,f,q}
 ={V_{\varepsilon,f}\over T_{\varepsilon,f,q}}
 =2^q{\binom{f+q+\varepsilon}{q}
             \over
             \binom{m-\varepsilon-2f}{q}}.}          \tag{4.2}
\]

No choice of cube cycle, direction word, phase, or coupled resolution
inside the same pair frame changes (4.1).

For `q>0`, the ideal identity (4.1) cannot by itself be the complete
histogram of an exact odd wreath factor, because it preserves `infinity`
too often.  Indeed

\[
 \sum_fV_{1,f}=m\operatorname{Cat}_m,
 \qquad
 \sum_fV_{0,f}=(m+1)\operatorname{Cat}_m,             \tag{4.2a}
\]

whereas the exact length-`m-q` interval ledger requires

\[
 (m-q)\operatorname{Cat}_m,
 \qquad
 (m+1+q)\operatorname{Cat}_m.                        \tag{4.2b}
\]

Thus at least `q Cat_m` starts must already cross the infinity sectors.
For `q=O(sqrt(m))` this compulsory transport is
`O(W/sqrt(m))=o(W)`.  Section 6 treats all such seams as cross-type
leakage; they are far too sparse to remove the Gaussian obstruction.

Taking the cemetery-augmented vector `M=V` in Theorem 3.1 proves
(0.5)--(0.6).  It also gives a sharp
finite criterion:

\[
 \boxed{
 \hbox{native orbit capacities meet a balanced quota exactly}
 \iff
 E_{m,q}=0\ \hbox{ and }\qquad
 c_q\le\lambda_{\varepsilon,f,q}\le c_q+1
 \quad\hbox{for every valid }(\varepsilon,f).}        \tag{4.3}
\]

After routing the cemetery mass through nonnative starts, the displayed
interval inequalities remain the exact compatibility test for the
eligible native subledger.

This criterion already fails at very shallow depth.  For example, at
`epsilon=f=0`,

\[
                    \lambda_{0,0,q}={2^q\over\binom mq}.          \tag{4.4}
\]

At `q=1`, `c_1=1`, so `lambda_(0,0,1)=2/m<1` for `m>2`.
Thus an exact native fixed-pair balanced histogram does not exist even at
depth one.  This single extreme orbit is exponentially small and by itself
does not close coefficient one; the Gaussian theorem below does.

Moreover, a literal histogram which is both native and fully
`G_m`-invariant would require every number in (4.2) to be an integer by
(3.8).  Equation (4.4) rules this out already at `q=1,m>2`.  Wreath
symmetrization therefore produces a fractional histogram, not one literal
invariant factor.

## 5. Gaussian quota obstruction with exact constants

Fix `A>0` and let

\[
                         q=A\sqrt m+O(1).             \tag{5.1}
\]

The exact rank ratio satisfies

\[
                         {W\over N_q}\longrightarrow e^{A^2}.    \tag{5.2}
\]

Under the target probability law

\[
 \Pr\{(\varepsilon,f)\}
 ={T_{\varepsilon,f,q}\over N_q},                    \tag{5.3}
\]

Stirling expansion of (1.5), uniformly on bounded standardized windows,
gives a variable `Z_m` with

\[
 Z_m\Longrightarrow Z\sim N(0,1),
 \qquad
 \log\lambda_{\varepsilon,f,q}
      =-A^2+2AZ_m+o(1).                               \tag{5.4}
\]

Here is the expansion explicitly.  Conditional on `epsilon`, the target
type has saddle

\[
 f_{*,\varepsilon}
 ={(m-q-\varepsilon)^2\over4m}+O(1),                 \tag{5.4a}
\]

and the second logarithmic difference of (1.5) is
`-16/m+o(1/m)`.  Hence

\[
 Z_m={4(f-f_{*,\varepsilon})\over\sqrt m}
       \Longrightarrow N(0,1).                       \tag{5.4b}
\]

Taking logarithms in (4.2) gives

\[
 \log\lambda
 =q\log2+
   \sum_{i=1}^q\log(f+\varepsilon+i)
  -\sum_{i=0}^{q-1}\log(m-\varepsilon-2f-i).         \tag{5.4c}
\]

At the saddle this is `-q^2/m+o(1)=-A^2+o(1)`, while

\[
 {\partial\over\partial f}\log\lambda
        ={8q\over m}+o(m^{-1/2}).                    \tag{5.4d}
\]

The quadratic Taylor remainder on a bounded `Z_m` window is `o(1)`.
Equations (5.4a)--(5.4d) prove (5.4).

The bounded bit `epsilon` changes the saddle by `O(1)` and the logarithm
by `O(m^(-1/2))`, so both epsilon strata have the same limit.  The exact
factorial ratios in (4.2), together with the Gaussian tails from Stirling,
give uniform integrability for the positive parts below.  The cemetery
contribution satisfies `E_(m,q)/N_q=o(1)` by (4.0b), so it
does not alter either limit.  Thus, on every subsequence for which
`c_q=c` is constant,

\[
 {D^-_{m,q}\over N_q}\longrightarrow
             d^-_{A,c}:=\mathbb E(c-L)_+,
 \qquad
 {D^+_{m,q}\over N_q}\longrightarrow
             d^+_{A,c}:=\mathbb E(L-c-1)_+,           \tag{5.5}
\]

where

\[
                         L=e^{-A^2+2AZ}.              \tag{5.6}
\]

For `a>0`, put

\[
                         z_a={A^2+\log a\over2A}.      \tag{5.7}
\]

Gaussian truncation evaluates the two constants exactly:

\[
 \boxed{
 d^-_{A,c}
   =c\Phi(z_c)-e^{A^2}\Phi(z_c-2A),}                 \tag{5.8}
\]

\[
 \boxed{
 d^+_{A,c}
   =e^{A^2}\Phi(2A-z_{c+1})
      -(c+1)\Phi(-z_{c+1}).}                         \tag{5.9}
\]

Both are strictly positive: the lognormal variable `L` has positive
probability below `c` and above `c+1`.

If `e^(A^2)` is not an integer, then eventually

\[
                         c_q=c_A:=\lfloor e^{A^2}\rfloor.         \tag{5.10}
\]

If `e^(A^2)=K` is an integer, then for all large `m`,
`c_q` belongs to `{K-1,K}`.  Define

\[
 \mathcal C_A=
 \begin{cases}
 \{\lfloor e^{A^2}\rfloor\},&e^{A^2}\notin\mathbb Z,\\
 \{K-1,K\},&e^{A^2}=K,
 \end{cases}                                         \tag{5.11}
\]

and

\[
 \boxed{
 \kappa_A=e^{-A^2}
   \min_{c\in\mathcal C_A}
      \max\{d^-_{A,c},d^+_{A,c}\}>0.}               \tag{5.12}
\]

Since `N_q/W -> e^(-A^2)`, equations (5.5)--(5.12) prove (0.8).

For `c=1`, (5.8) reduces after normalization by `W` to the familiar
fixed-frame support constant

\[
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2).                      \tag{5.13}
\]

The new point is that (5.8)--(5.9) retain the exact factorial floor at
every fixed `A`, including ranges where `c_q>1`.

## 6. Robustness under cross-type leakage

Let `M_(epsilon,f)` be the actual target-orbit masses of a construction,
and extend it by `M_partial=0`.  Let `V_hat` be the eligible native vector
together with `V_partial=E_(m,q)`.  Suppose at most `L_q` of its `W`
starts fail the native type rule (4.1), counting every ineligible source
as nonnative.  Moving one occurrence from its native orbit or cemetery
cell to an actual target orbit changes the augmented mass vector by
half-`l_1` distance one.  Therefore

\[
 {1\over2}\|\widehat M-\widehat V\|_1\le L_q.         \tag{6.1}
\]

For an exact odd factor, (4.2a)--(4.2b) already force

\[
             L_q\ge\max\{E_{m,q},q\operatorname{Cat}_m\}.       \tag{6.1a}
\]

This is only `O_A(W/sqrt(m))` at Gaussian depth and is absorbed by the
error term below.

Distance to the balanced-capacity box, with the total-mass hyperplane
imposed, is one-Lipschitz in this norm.  Combining Theorem 3.1 with (6.1)
gives, for every labelled histogram and every balanced quota,

\[
 \boxed{
 {1\over2}\|\mu_q-\beta_q\|_1
 \ge\max\{D^-_{m,q},D^+_{m,q}\}-L_q.}               \tag{6.2}
\]

At `q=A sqrt(m)+O(1)`, (5.12) yields

\[
 {1\over2}\|\mu_q-\beta_q\|_1
                  \ge(\kappa_A-o(1))W-L_q.           \tag{6.3}
\]

Here `c_q=O_A(1)`.  Thus the same conclusion remains macroscopic after
the factorial-floor weight `1/c_q` used in the constant-one objective.

Thus `L_q=o(W)` leaves a macroscopic statewise quota defect.  Conversely,
any fixed-pair construction with `o(W)` quota overload at this depth must
have

\[
                         L_q\ge(\kappa_A-o(1))W.       \tag{6.4}
\]

This is the exact constant-one implication: a positive density of starts
must cross the native wreath orbits.  Pair permutations and within-pair
swaps cannot accomplish that, because they preserve `(epsilon,f)`; a
different pair frame or a nonlocal cross-type seam is required.

## 7. Scope and surviving route

Proved:

* the complete `G_m` target-orbit classification and stabilizers;
* exact compatibility of pure fractional orbit quotas;
* the exact integral subset-sum condition for a fully invariant quota;
* the sharp finite projection formula (3.4);
* native source-to-target orbit totals and likelihood ratios;
* an explicit positive Gaussian factorial-floor obstruction; and
* robustness against `o(W)` cross-type leakage.

Not proved, and not claimed:

* that every construction respecting the abstract group action must obey
  the native type flow (4.1);
* that the subset-sum condition (2.6) always fails; or
* that mixing pair frames is integrally or chronologically realizable.

Pure symmetry is fractionally harmless.  The theorem closes the
single-frame, type-preserving architecture and sharpens the surviving
design requirement: a coefficient-one construction must realize
`Theta_A(W)` ownerwise cross-orbit transport while preserving literal
contiguous-OR chronology and the complete lower/upper ledgers.
