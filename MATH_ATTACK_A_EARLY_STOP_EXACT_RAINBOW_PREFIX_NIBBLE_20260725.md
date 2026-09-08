# Early-stopped exact-rainbow prefixes: exact repair and the unchanged LLL scale

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad M=m+H,
\]

where (H) is the calibrated first crossing, and let

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil,
 \qquad \gamma\to\infty,\quad \gamma=o(\log\log m).
\]

Choose an integer

\[
 \frac mH\ll \ell\ll \frac mQ,
 \qquad R=M-\ell .                                      \tag{0.1}
\]

The early-stop proposal has a rigorous positive part.  A marked arc of
(R) consecutive states of every deterministic exact-rainbow rotor cycle
is still a literal physical trajectory segment and is exactly rainbow at
every controlled rank.  Intersecting the old common-priority claims with
the arc and buffering every row by (ell) gives one exact nested prefix
catalogue.  Its uniform fractional loads are at most one, all separate-row
Hall inequalities hold, and its additional scalar leave is exactly

\[
 (2Q+1)\ell N=o(W).                                  \tag{0.2}
\]

Consequently, once a common prefix matching of the size specified below is
supplied, the omitted suffixes can be left completely uncontrolled and
repaired by the already audited literal/collar mechanism at \(o(W)\) cost.
That conditional composition preserves integrality and literal
contiguous-OR realizability.

There is also an unconditional common-nested sparse batch of

\[
 \Theta\!\left(\frac{N}{m^{3/2}}\right)             \tag{0.3}
\]

trajectory prefixes.

However, early stopping does **not** improve the scale of the missing
iteration theorem.  The buffered augmented size is still

\[
 K_\ell=(\sqrt\pi+o(1))m^{3/2};                     \tag{0.4}
\]

indeed it differs from the full value by only (o(m)).  For a fixed
prefix, the exact atomic collision mass against the other carrier
variables is

\[
 (1-o(1))K_\ell,                                    \tag{0.5}
\]

and the owner row alone contributes ((1-o(1))M).  The depth-one relative
pair codegree remains ((2-o(1))/m).  Catalogue entropy remains
(\Theta(m\log m)), so the independent-residual survival horizon remains

\[
 \Theta(\log m/\sqrt m).                            \tag{0.6}
\]

Thus neither the direct LLL, the cardinality-certified sparse activation,
the target-level link kernel, nor the entropy barrier improves by a
nonvanishing factor.

This note does not prove coefficient one.  In this architecture the exact
remaining theorem is a matching of the buffered prefix hypergraph leaving

\[
 e=o(N/\sqrt m)                                     \tag{0.7}
\]

carrier tags unmatched.  The first sparse batch proves only
(e=N-\Theta(N/m^{3/2})).

## 1. Parameters and the buffered prefix claims

Write

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
 \qquad \lambda_q=\frac{W}{N_q}.
\]

Calibration gives

\[
 M\le \lambda_H\le
 M\frac{m+H}{m-H+1}=M(1+O(H/m)),                   \tag{1.1}
\]

and hence

\[
 N=(1+o(1))\frac Wm,\qquad MN=W-o(W).              \tag{1.2}
\]

The window (0.1) is nonempty because (Q=o(H)).  For example,

\[
 \ell=\left\lfloor\frac{m}{\sqrt{HQ}}\right\rfloor
                                                               \tag{1.3}
\]

satisfies

\[
 \frac{H\ell}{m}\to\infty,
 \qquad \frac{Q\ell}{m}\to0.                     \tag{1.4}
\]

For the full deterministic catalogue put

\[
 d_0=M,
 \qquad
 d_q=\min\left\{M,\left\lfloor\frac{N_q}{N}\right\rfloor\right\}
 \quad(1\le q\le Q),                               \tag{1.5}
\]

and

\[
 K_0=M+2\sum_{q=1}^Qd_q.                           \tag{1.6}
\]

The sequence (d_q) is nonincreasing.  Moreover

\[
 d_Q=(1+o(1))\frac{\lambda_H}{\lambda_Q}
     =\frac{m}{(\log m)^{1+o(1)}}\gg\ell .         \tag{1.7}
\]

Thus the buffered prefix counts

\[
 \boxed{c_{q,\ell}=d_q-\ell\quad(0\le q\le Q)}     \tag{1.8}
\]

are positive, nonincreasing, and at most (R=M-\ell).  At each signed
depth (q), claim the first (c_{q,\ell}) retained phases in one common
priority order; at the owner row claim all (R) retained phases.

There is also a maximal re-ranked choice

\[
 \widehat c_{q,\ell}
 =\min\left\{R,\left\lfloor\frac{N_q}{N}\right\rfloor\right\}.   \tag{1.9}
\]

It has weakly smaller scalar leave.  The buffered choice (1.8) is used
below because it is a literal subclaim of every full common-priority
column, it gives an exact repair ledger, and it is the more favorable
choice for testing whether smaller augmented size helps the LLL.

## 2. Exact prefix extraction

Let \({\cal P}(U)\) be any coordinate-symmetric catalogue of the full
length-(M) exact-rainbow cycles from the deterministic gap-permutation
theorem.  Every cycle carries a marked phase-zero seam, and all (M) seam
rotations are included with equal multiplicity.  The decorated full
catalogue also includes every \(M\)-phase priority order with equal
multiplicity, independently of the path.  Retain phases
\(0,1,\ldots,R-1\) and use the priority induced on them.  This induced
order is distributionally a fresh uniform \(R\)-priority, while the
inherited convention certifies that every buffered claim is literally a
subclaim of its full decorated column.

### Theorem 2.1 (literal nested prefix catalogue)

For every carrier (U\in\binom{[2m]}M), the buffered construction has the
following properties.

1. Every retained object is a literal radius-(Q) rotor trajectory segment.
   At every rank (m\pm q), (0\le q\le Q), its retained targets are
   pairwise distinct.
2. The claimed phase sets are nested in (q) on both signed arms.
3. If (A_\ell) is the number of decorated prefix columns above one
   carrier, then every fixed target (S\in\binom{[2m]}{m\pm q}) has
   global catalogue degree
   
   \[
    D_{q,\ell}(S)
     =A_\ell\frac{c_{q,\ell}N}{N_q}.               \tag{2.1}
   \]
   
   Thus weight (1/A_\ell) saturates every carrier tag and gives target
   load
   
   \[
    L_{q,\ell}:=\frac{c_{q,\ell}N}{N_q}\le1.       \tag{2.2}
   \]
4. For every carrier family
   \({\cal C}\subseteq\binom{[2m]}M\), the rank-((m\pm q)) neighbour
   family satisfies
   
   \[
    |N_{m\pm q}({\cal C})|
     \ge \frac{N_q}{N}|{\cal C}|
     \ge c_{q,\ell}|{\cal C}|.                    \tag{2.3}
   \]
   
   Consequently each controlled rank separately admits an integral
   assignment of (c_{q,\ell}) distinct targets to every carrier.

#### Proof

The full trajectory is injective at every controlled rank by the exact
rainbow theorem.  Restriction to a set of phases preserves injectivity.
The (R) retained states and their inherited queue data are actual rotor
states, so consecutive retained phases give a physical trajectory segment.

Let the full (M)-phase priority order be fixed.  Among the first (d_q)
priority phases, at most (ell) lie in the omitted suffix.  Therefore the
first (d_q-\ell=c_{q,\ell}) phases of the priority order induced on the
retained arc all belonged to the old depth-(q) claim.  Since the numbers
(c_{q,\ell}) are nonincreasing, these retained claims are nested.

Coordinate symmetry makes every rank-((m\pm q)) subset of one carrier
occur equally often among the (c_{q,\ell}) distinct claimed targets.
Its local degree is therefore

\[
 A_\ell\frac{c_{q,\ell}}{\binom M{m\pm q}}.
\]

A fixed target lies in

\[
 \binom{2m-(m\pm q)}{M-(m\pm q)}
\]

carriers.  The containment identity

\[
 N\binom M{m\pm q}
 =N_q\binom{2m-(m\pm q)}{M-(m\pm q)}              \tag{2.4}
\]

proves (2.1).  Inequality (2.2) follows from (1.5) and (1.8).

Finally, all coordinate labellings are present, so a retained fixed phase
can realize every rank-((m\pm q)) subset of its carrier.  Counting
containment incidences from ({\cal C}) to its shadow gives

\[
 |N_{m\pm q}({\cal C})|
 \ge
 \frac{\binom M{m\pm q}}
      {\binom{2m-(m\pm q)}{M-(m\pm q)}}|{\cal C}|
 =\frac{N_q}{N}|{\cal C}|.
\]

Cloning every carrier (c_{q,\ell}) times and applying Hall proves the
last assertion. \(\square\)

### Endpoint convention

The flags at the two ends are the flags of the inherited full cyclic rotor
states.  They are not recomputed from the owner arc alone.  Equivalently,
one keeps the bounded cyclic collar when the arc is cut and later uses the
audited seam compiler.  Without this convention, the first and last
(q) phases do not contain enough internal history to define both signed
flags, and the exact statement would be false.  Also, (R) states contain
(R-1) transitions; all counts in this note are state-occurrence counts.

## 3. Exact loss, repair, and unmatched-tag threshold

Define the full and buffered scalar leaves by

\[
 \mathcal L_0
 =W-MN+2\sum_{q=1}^Q(N_q-d_qN),                    \tag{3.1}
\]

\[
 \mathcal L_\ell
 =W-RN+2\sum_{q=1}^Q(N_q-c_{q,\ell}N).             \tag{3.2}
\]

### Theorem 3.1 (exact early-stop ledger)

One has the exact identities

\[
 \boxed{K_\ell
 =R+2\sum_{q=1}^Qc_{q,\ell}
 =K_0-(2Q+1)\ell,}                                 \tag{3.3}
\]

\[
 \boxed{\mathcal L_\ell-\mathcal L_0
 =(2Q+1)\ell N=N(K_0-K_\ell).}                    \tag{3.4}
\]

Consequently

\[
 K_\ell=(\sqrt\pi+o(1))m^{3/2},                   \tag{3.5}
\]

\[
 \mathcal L_\ell=o(W).                            \tag{3.6}
\]

Uniformly for all controlled rows,

\[
 L_{q,\ell}=1-o(1).                                \tag{3.7}
\]

#### Proof

Equations (3.3) and (3.4) follow immediately by subtracting (ell) in
each of the (2Q+1) rank-tagged rows.  The full exact-rainbow catalogue
has

\[
 K_0=(\sqrt\pi+o(1))m^{3/2},\qquad
 \mathcal L_0=o(W).
\]

By (0.1),

\[
 (2Q+1)\ell=o(m),qquad
 (2Q+1)\ell N=o(W),                                \tag{3.8}
\]

which proves (3.5)--(3.6).

For (3.7), put (a_q=N_q/N=\lambda_H/\lambda_q).  Uniformly for
(q\le Q),

\[
 a_q\ge a_Q=\frac{m}{(\log m)^{1+o(1)}}\to\infty,
 \qquad \frac\ell{a_q}=o(1).                      \tag{3.9}
\]

If the cap in (1.5) is inactive, then

\[
 L_{q,\ell}
 =\frac{\lfloor a_q\rfloor-\ell}{a_q}=1-o(1).
\]

If it is active, then (c_{q,\ell}=R), while
(a_q\le\lambda_H=M(1+O(H/m))).  Hence

\[
 L_{q,\ell}\ge\frac{M-\ell}{\lambda_H}=1-o(1).
\]

The owner row is the same calculation with (a_0=\lambda_H). \(\square\)

### Proposition 3.2 (uniform individual-row terminal reserve)

Relative to the full balanced (d_qN)-slot ledger, the buffered prefix uses
exactly \(\ell N\) fewer \(0/1\) target slots in every controlled row.
After a rowwise-disjoint buffered support is extended to any
\(d_qN\)-support, these are literally \(\ell N\) residual slots; the
fractional catalogue alone does not realize such a support.  If that
residual set were ambient-uniform in its rank, then every
arrival-controlled row of one carrier would see expected residual capacity
at least

\[
 (H-Q)\frac{\ell N}{N_q}
 =\frac{(H-Q)\ell}{N_q/N}
 \ge(1-o(1))\frac{H\ell}{m}\longrightarrow\infty. \tag{3.10}
\]

Thus buffering every row, rather than truncating only the capped shallow
rows, removes the old sparse-terminal first-moment warning separately in
every rank.

#### Proof

By (1.8), the difference between the full and buffered claim totals is
exactly (ell N) in every row.  Also (d_qN\le N_q), so the corresponding
balanced target ledger may be taken (0/1).  An arrival column has
(H-Q) distinct (y)-choices in each arrival-controlled coordinate.
Uniformity of an (ell N)-subset of the (N_q) targets gives the first
expectation in (3.10).  Finally

\[
 \frac{N_q}{N}\le\frac WN=\lambda_H=(1+o(1))m,
\]

and (1.4) proves divergence. \(\square\)

This is only a one-row first moment.  It says nothing about whether one
and the same arrival lies in the residual sets of all claimed ranks.

### Proposition 3.3 (coefficient-safe composition boundary)

Suppose a matching of the buffered augmented prefix hypergraph selects
one prefix at (N-e) carriers.  Complete each selected prefix by the suffix
of its own inherited full trajectory, and use an arbitrary complete
trajectory at each of the other \(e\) carriers.  Before crediting any
unprotected occurrences from those suffixes and fillers, the number of
uncovered controlled targets is exactly

\[
 \boxed{\mathcal L_\ell+eK_\ell.}                  \tag{3.11}
\]

Thus the selected prefixes, arbitrary full physical filler trajectories at
the remaining carriers, the audited collars, and literal repair give a
coefficient-one construction provided

\[
 eK_\ell=o(W),                                     \tag{3.12}
\]

equivalently

\[
 \boxed{e=o(N/\sqrt m).}                           \tag{3.13}
\]

#### Proof

The matching covers (R(N-e)) distinct owner targets and
(c_{q,\ell}(N-e)) distinct targets in each signed depth-(q) row.
Subtracting these values from the layer sizes and summing gives (3.11).
Filler occurrences can only decrease the number of holes.  Equations
(1.2), (3.5), and (3.6) turn (3.12) into (3.13).

The (N) complete physical trajectories have base length (MN=W-o(W)),
and the established collars cost (O(HN)=o(W)).  The omitted prefix claims
cost (3.4), and all remaining holes may be appended literally.  Thus no
fractional object or nonphysical transversal enters the final word. \(\square\)

The lower inequality (ell\gg m/H) is not needed for Theorems 2.1 or
3.1.  Its role is only terminal: it makes the mean number
((1+o(1))H\ell/m) of ambient-uniform residual owner choices tend to
infinity.  It does not alter (3.13).  Even if the entire early-stop repair
budget were spent on unmatched tags, it would permit only

\[
 \frac eN
 =O\!\left(\frac{Q\ell}{m^{3/2}}\right)
 =o(m^{-1/2}).                                      \tag{3.14}
\]

## 4. An unconditional common-nested sparse batch

Choose one uniform decorated prefix independently above every carrier.
For a rank-tagged target (v), let

\[
 \ell_v=\sum_U\Pr(v\text{ is claimed by the prefix at }U).
\]

By Theorem 2.1, (ell_v=L_{q,\ell}\le1) in its row, and

\[
 \sum_v\ell_v=NK_\ell.                             \tag{4.1}
\]

### Theorem 4.1 (one buffered sparse round)

For every fixed (0<\theta\le1), the buffered prefix hypergraph has a
common-nested matching of at least

\[
 \boxed{
 \left(\theta-\frac{\theta^2}{2}\right)
 \frac{N}{K_\ell}}                                 \tag{4.2}
\]

prefixes.  In particular it has one of size

\[
 \frac{N}{2K_\ell}
 =\Theta(N/m^{3/2}).                                \tag{4.3}
\]

#### Proof

Activate every carrier independently with probability

\[
 \alpha=\frac\theta{K_\ell},
\]

and choose one uniform prefix at every activated carrier.  The expected
number (A) of activated carriers is (alpha N).

Join two activated prefixes when they claim a common target in any
rank-tagged row, and let (C) be the number of conflict-graph edges.  A
union bound over atomic target equalities gives

\[
\begin{aligned}
 \mathbb EC
 &\le \frac{\alpha^2}{2}\sum_v\ell_v^2\\
 &\le \frac{\alpha^2}{2}\sum_v\ell_v
  =\frac{\alpha^2NK_\ell}{2}.                     \tag{4.4}
\end{aligned}
\]

Delete one endpoint of every conflict edge.  At least (A-C) prefixes
remain, and they are disjoint simultaneously in all claimed rows.  Taking
expectations in (4.4) proves (4.2).  Every retained edge was one whole
decorated prefix, so common-priority nesting is preserved exactly. \(\square\)

The batch (4.3) covers only

\[
 \Theta\!\left(\frac{NR}{K_\ell}\right)
 =\Theta(W/m^{3/2})=o(W)                           \tag{4.5}
\]

owner occurrences.  Theorem 4.1 is therefore a genuine first round, not a
near-factor theorem.

## 5. The exact collision and link kernels

For a fixed decorated prefix (P) on carrier (U), let (P_r) denote its
claimed targets in one rank-tagged row (r=m\pm q), and put
(|P_r|=c_{q,\ell}).

### Theorem 5.1 (atomic collision mass)

The total atomic collision mass of (P) against all other carrier
variables is exactly

\[
 \boxed{
 \Xi(P)
 =\sum_r c_{q,\ell}
   \left(
    L_{q,\ell}-\frac{c_{q,\ell}}{\binom Mr}
   \right).}                                       \tag{5.1}
\]

Consequently

\[
 \Xi(P)=(1-o(1))K_\ell.                            \tag{5.2}
\]

The owner row alone contributes

\[
 \boxed{
 \Xi_0(P)
 =R^2\left(
    \frac1{\lambda_H}-\frac1{\binom Mm}
   \right)
 =(1-o(1))M.}                                      \tag{5.3}
\]

For fixed carriers (U,V), the exact expected number of common claimed
targets in row (r) is

\[
 \boxed{
 E_{UV,r}
 =c_{q,\ell}^{2}
  \frac{\binom{|U\cap V|}{r}}{\binom Mr^2}.}       \tag{5.4}
\]

If (B_{UV,r}) is the event of at least one row-(r) collision, then

\[
 \frac{E_{UV,r}}{c_{q,\ell}}
 \le \Pr(B_{UV,r})\le E_{UV,r}.                   \tag{5.5}
\]

#### Proof

For (S\in P_r), global symmetry gives

\[
 \sum_V\Pr(S\text{ is claimed at }V)=L_{q,\ell}.
\]

At the fixed carrier (U), a uniform catalogue prefix claims (S) with
probability (c_{q,\ell}/\binom Mr).  Subtracting this same-carrier term
and summing over the (c_{q,\ell}) members of (P_r), then over all rows,
proves (5.1).  Formula (3.7), together with the exponentially small ratios
(c_{q,\ell}/\binom Mr), proves (5.2).  At the owner row,
(L_{0,\ell}=RN/W=R/\lambda_H), which gives (5.3).

For (5.4), each rank-(r) subset of a carrier is claimed with probability
(c_{q,\ell}/\binom Mr).  The two carrier choices are independent, and
exactly \(\binom{|U\cap V|}{r}\) targets are available to both.  Finally, if
(Z) is the intersection size in that row, then

\[
 \mathbf 1_{Z>0}\le Z\le c_{q,\ell}\mathbf 1_{Z>0}.
\]

Taking expectations proves (5.5). \(\square\)

Theorem 5.1 has two precise consequences.

* The probability-proportional LLL on the atomic equality events has
  incident activity mass (Theta(K_\ell)); owner equalities alone have
  mass (Theta(M)).  Deleting an (o(M))-long suffix changes neither
  scale.
* Activating a (p)-fraction of carriers changes the atomic incident mass
  to order (pK_\ell).  The cardinality-certified alteration/LLL scale is
  therefore (p=\Theta(1/K_\ell)), exactly the scale attained in Theorem
  4.1.

This is an obstruction to the direct atomic or probability-proportional
LLL.  It is **not** a theorem that every asymmetric correlated selection
must fail: several atomic equalities may be combined into one carrier-pair
event, and a successful construction may exploit that geometry.

### Proposition 5.2 (the vertical codegree does not improve)

In the ordinary cyclic exact-rainbow subcatalogue, for every owner \(X\)
and facet \(S\subset X\), \(|S|=m-1\), the maximal prefix convention
(1.9) has the exact identity

\[
 \frac{\widehat{\deg}_\ell(X,S)}{\widehat{\deg}_\ell(X)}
 =\frac{2-1/R}{m}.                                  \tag{5.6}
\]

For the buffered convention (1.8), priority symmetry gives

\[
 \boxed{
 \frac{\deg_\ell(X,S)}{\deg_\ell(X)}
 =\frac{c_{1,\ell}}R\frac{2-1/R}{m}
 =\frac{2-o(1)}m.}                                  \tag{5.7}
\]

The analogous upper cofacet identities also hold.

#### Proof

For large \(m\), \(d_1-\ell=R-O(1)\).
First take the maximal prefix convention (1.9), where every retained
depth-one phase is claimed.  Condition on a full cyclic packet containing
 \(X\) and then on a uniformly marked \(R\)-phase arc containing its owner
phase.  A prescribed facet \(S\) is the forward boundary facet with
probability \(1/m\), and that occurrence is always retained.  It is the
backward boundary facet with probability \(1/m\), and that preceding phase
is retained unless the owner phase is first in the arc, an event of
probability \(1/R\).  No other rank-\((m-1)\) interval equals \(S\).  This
gives (5.6).

Under the buffered convention, only \(O(1)\) additional phases are lost at
depth one because

\[
 d_1\ge M-2,
\]

whereas \(c_{1,\ell}=d_1-\ell=R-O(1)\).  Independently of the marked
arc, a uniform priority claims each retained depth-one phase with
probability \(c_{1,\ell}/R\).  Multiplying (5.6) by this factor proves
(5.7).  The upper calculation is identical. \(\square\)

Thus the exact early-stop window does not improve the raw vertical
codegree input.  In particular, an argument whose quantitative leave is
only a square-root function of that codegree remains at the critical
(m^{-1/2}) scale and supplies no vanishing improvement required by
(3.13).  This last sentence is a limitation of that class of estimates,
not a lower bound on the true matching number.

### Proposition 5.3 (priority thinning improves only the short-path constant)

Sample independently at every carrier a symmetric rooted exact-rainbow
path together with its uniform induced prefix priority.  At time
\(t\), impose collision events only in rows whose priority claims \(t\).
The total same-time bad-event mass incident with one carrier variable is

\[
 \eta_{\mathrm{pr}}
 =
 \frac{
  1+2\sum_{q=1}^Q
       \lambda_q(c_{q,\ell}/R)^2
 }{\lambda_H}
 +o(m^{-1/2})
 =
 \left(\sqrt\pi+o(1)\right)m^{-1/2}.                \tag{5.8}
\]

The audited chronology-preserving path-variable LLL criterion applies
whenever

\[
 T\eta_{\mathrm{pr}}\le\frac18,                    \tag{5.9}
\]

The largest horizon certified by this criterion is therefore
\(T=O(\sqrt m)=o(R)\).  Such a block contains \(TN=o(W)\) physical
occurrences.  This is not a universal upper bound on every correlated LLL
or direct construction.

#### Proof

At one fixed time and signed depth \(q\), a carrier claims that time with
probability \(c_{q,\ell}/R\).  Priorities at two carriers are independent,
so a collision event acquires the square of this factor.  Conditional on
being claimed, coordinate symmetry makes the rank-\((m\pm q)\) flag
uniform in its carrier.  The containment identity therefore gives
other-carrier equality mass

\[
 \frac{\lambda_q}{\lambda_H}
 -\frac1{\binom M{m\pm q}}.
\]

Summing the owner and both signed rows proves the first expression in
(5.8).

Put \(a_q=N_q/N=\lambda_H/\lambda_q\).  The buffered ratio satisfies

\[
 \frac{c_{q,\ell}}R
 =(1+o(1))\min\{1,a_q/M\}
\]

uniformly for \(q\le Q\).  The capped indices have
\(q=O(\sqrt H)\) and contribute \(o(\sqrt m)\) to the numerator sum.
At every uncapped index,

\[
 \lambda_q(c_{q,\ell}/R)^2
 =(1+o(1))\lambda_q^{-1}.
\]

The central expansion and \(Q/\sqrt m\to\infty\) give

\[
 \sum_{q=1}^Q\lambda_q^{-1}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m.
\]

Since \(\lambda_H=(1+o(1))m\), (5.8) follows.  Treating each entire
length-\(T\) path and priority as one variable, a bad event uses two such
variables.  The same asymmetric-LLL calculation as in the audited
short-path theorem applies when (5.9) holds. \(\square\)

Thus common priorities remove the earlier endpoint polylogarithm from the
fresh same-time mass, but an \(R\sim m\) prefix is still longer than the
certified LLL horizon by a factor \(\Theta(\sqrt m)\).

## 6. Entropy and the failed iteration shortcut

Let \(A_0\) count full decorated paths above a carrier.  After quotienting
the irrelevant ordering of the omitted \(\ell\) phases, but retaining all
path-labelled multiplicities, let \(A_\ell\) count the resulting buffered
prefixes.  Then

\[
 \log A_0-\log A_\ell
 =\log\frac{M!}{R!}=O(\ell\log m)=o(m\log m).       \tag{6.1}
\]

If instead every full-priority extension is retained as a separate
labelled multiplicity, then \(A_\ell=A_0\) at the priority level, which is
an even more generous entropy count.  After quotienting physically
identical state prefixes as well, each prefix has at most

\[
 ((m-Q)(H-Q))^\ell\frac{M!}{R!}
\]

full rotor/priority completions, so the logarithmic loss is still only
\(O(\ell\log m)\).  In a convention-independent form,

\[
 0\le \log A_0-\log A_\ell
 \le \ell\log((m-Q)(H-Q))+\log\frac{M!}{R!}
 =O(\ell\log m),
\]

where the left equality may occur when all parallel labels are retained.
Conversely, the cyclic-order and priority
subcatalogue already has logarithmic size ((2+o(1))m\log m).  The entire
gap-permutation parametrization has logarithmic size (O(m\log m)).
Therefore

\[
 \boxed{\log A_\ell=\Theta(m\log m).}              \tag{6.2}
\]

### Proposition 6.1 (unchanged product-residual horizon)

Suppose every claimed target is independently available with probability
(1-\delta).  Then the expected number of viable buffered prefixes at one
carrier is

\[
 A_\ell(1-\delta)^{K_\ell}.                        \tag{6.3}
\]

Uniformly over the known deterministic catalogue, this tends to zero
superpolynomially once

\[
 \delta\gg\frac{\log m}{\sqrt m}.                 \tag{6.4}
\]

The same conclusion holds under an
(exp(o(m\log m)))-multiplicative product approximation.

#### Proof

Equations (3.5) and (6.2) give

\[
 \log\bigl(A_\ell(1-\delta)^{K_\ell}\bigr)
 \le O(m\log m)-\delta(\sqrt\pi+o(1))m^{3/2}.
\]

This tends to (-\infty) with magnitude (omega(m\log m)) under
(6.4).  Multiplying by (exp(o(m\log m))) does not change the sign. \(\square\)

Early stopping therefore changes neither side of the entropy comparison
at leading order.  It cannot promote the one-round LLL distribution into
a product-like multiround invariant.

There is an owner-only version of the same warning.  For rooted cyclic
prefixes let (D_\ell) be the number above one carrier.  A fixed owner lies
in (D_\ell R/\binom Mm) of them.  One selected prefix on another carrier
meets at most (H) owners of the first full cyclic packet.  Hence the raw
one-step Lipschitz bound on available prefixes is

\[
 H D_\ell\frac{R}{\binom Mm}.                      \tag{6.5}
\]

At a product owner density (y), the benchmark available count is
(D_\ell y^R).  At (y=1/\log m), the logarithm of the ratio of (6.5) to
that benchmark is

\[
 R\log\log m-\log\binom MH+O(\log m)
 =(1-o(1))m\log\log m\to\infty.                   \tag{6.6}
\]

The subtraction of (ell\log\log m=o(m\log\log m)) is negligible.
Thus the raw bounded-difference/link-flatness barrier also survives the
early stop.

Finally, density alone still cannot replace link control.  Fix a point
(a).  The middle-layer star

\[
 \{X:a\in X\}
\]

has density (1/2).  A cyclic top containing (a) has exactly (m)
consecutive owner phases containing (a), while

\[
 R=M-\ell>m
\]

because (ell=o(H)).  Hence no (R)-phase cyclic prefix is contained in
the star.  The early-stopped catalogue therefore still has dense
prefix-free residuals.

## 7. The exact surviving theorem

For the buffered prefix hypergraph, the coefficient-one gate is now the
following single statement.

> **Early-stopped nested link-flatness/matching theorem
> \(\mathrm{ESNLF}(Q,\ell)\) — UNPROVED.**  The exact-rainbow buffered
> prefix catalogue has a target-disjoint matching on
> 
> \[
>  N-o(N/\sqrt m)
> \]
> 
> carrier tags.

A strictly stronger sufficient formulation is that a sparse-round process
can be iterated while preserving whole-column availability and the
carrier-pair kernels (5.4) until only \(o(N/\sqrt m)\) tags remain.  Matching
existence does not imply that particular iterative invariant.

Proposition 3.3 proves that \(\mathrm{ESNLF}(Q,\ell)\) composes with the
audited physical collars and literal repair into coefficient one.  Theorem
4.1 proves its first sparse batch.  Theorems 5.1 and 6.1 show why neither a
fresh-round atomic LLL nor a product-residual iteration proves it.

If every sparse batch removed only a constant multiple of the currently
unmatched (1/K_\ell) fraction, reaching (3.13) would take

\[
 \Theta(K_\ell\log m)
 =\Theta(m^{3/2}\log m)                            \tag{7.1}
\]

batches.  This is a statement about that sparse-batch architecture, not a
lower bound against a direct global matching construction.

## 8. Adversarial audit

1. **Cyclic seam.**  A cyclic path has no first state until a phase seam is
   marked.  All rotations must be included, or the seam must be chosen
   independently of coordinate names.  Otherwise the symmetry used in
   (2.1), (5.1), and (5.4) fails.
2. **Endpoint flags.**  The exact endpoint claims use the inherited full
   rotor states/collar.  Recomputing flags from the isolated owner prefix
   would invalidate Theorem 2.1.
3. **Labelled entropy.**  Keeping multiplicities can overcount physically
   identical prefixes.  Proposition 6.1 is an obstruction even under that
   generous overcount, so quotienting cannot rescue the product argument.
4. **Atomic versus grouped LLL.**  Equation (5.2) is an exact atomic
   collision ledger.  It does not rule out a correlated asymmetric LLL or
   a carrier-pair resampling scheme which exploits multiple equalities at
   once.
5. **One round versus iteration.**  Theorem 4.1 uses only the initial
   symmetric loads.  It proves no preservation of those loads after the
   first deletion and therefore cannot be iterated as written.
6. **Unmatched-tag threshold.**  Formula (3.11) is exact for the certified
   disjoint prefix claims before filler occurrences are credited.  Filler
   paths may fortuitously cover some holes, so (3.13) is the exact threshold
   for this certificate, not a universal necessity theorem for all
   possible compilers.
7. **Repair scope.**  The suffix repair deliberately abandons exact
   completion of all balanced quota multiplicities.  It repairs support at
   (o(W)) literal cost, which is sufficient for coefficient one but not
   for the stronger exact TRP completion theorem.

The stable conclusion is therefore positive but limited: early stopping
is fully compatible with exact rainbow chronology, nested integral claims,
and literal repair, and it yields a rigorous first common-nested sparse
batch.  Its quantitative gain is only (o(m)) in an
(\Theta(m^{3/2}))-sized atom, so the multiround common-column theorem is
not made easier at leading order.
