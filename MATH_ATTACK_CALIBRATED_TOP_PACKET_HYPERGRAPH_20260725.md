# The calibrated top-packet hypergraph at \(H\sim\sqrt{m\log m}\)

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, web input,
or unverified generic matching theorem is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.                           \tag{0.1}
\]

Choose \(H\) to be the **smallest** positive integer such that

\[
 \lambda_H\ge M:=m+H.                            \tag{0.2}
\]

Then

\[
 \boxed{H=(1+o(1))\sqrt{m\log m},}               \tag{0.3}
\]

\[
 \boxed{1\le {\lambda_H\over M}
 <1+O(H/m)=1+o(1),}                               \tag{0.4}
\]

and consequently

\[
 \boxed{
 MN_H={M\over\lambda_H}W=W-o(W),
 \qquad HN_H=o(W).}                               \tag{0.5}
\]

For every top \(U\in\binom{[2m]}M\), one directed cyclic order of \(U\)
gives one promotion cycle of length \(M\).  Its middle owners are the
cyclic \(m\)-windows.  At depth \(q\le H\), its lower and upper flags are
the cyclic intervals of lengths \(m-q\) and \(m+q\), respectively.  Thus
one packet per top supplies exactly \(MN_H=W-o(W)\) owner slots and reset
toll \(O(HN_H)=o(W)\).

The new exact hypergraph statistics are as follows.

* A top belongs to
  \[
  D_T=(M-1)!
  \]
  directed packet columns.
* A middle owner belongs to
  \[
  D_0=\binom mH m!H!
      ={M\over\lambda_H}D_T=(1-o(1))D_T
  \]
  columns.
* If two owners have Johnson distance \(j<H\), their normalized packet
  codegree is exactly
  \[
  \boxed{{2\over\binom mj^2}.}                    \tag{0.6}
  \]
  The maximum is \(2/m^2\), attained at distance one.  Owners at distance
  greater than \(H\) have codegree zero.

Hence the top-owner packet hypergraph is an almost regular near-factor
instance with exceptionally small owner codegrees.  Its uniform orbit
weights give one packet of total weight one at every top, owner load
\(M/\lambda_H=1-o(1)\), and aggregate fractional flag deficiency at most
\(W-MN_H=o(W)\) in every rank.

This does not yet prove an integral near-factor.  Two issues remain.

1. The packet size is \(M+1\asymp m\), so the fixed-uniformity nibble
   theorem cannot simply be invoked while the uniformity grows.  The
   product
   \(M^2(\Delta_2/D)\) stays of constant order at the adjacent-owner
   codegree (0.6).
2. In the augmented owner-and-flag system, a prescribed owner and one of
   its prescribed depth-one flags have normalized same-phase codegree
   \(1/m\), not \(1/m^2\).  This is the deterministic nested-prefix
   correlation.  Treating all rank rows as independent matching parts
   destroys the small-codegree hypothesis.

Thus the calibrated proposal survives every scalar, reset, quotient, and
fractional audit.  The remaining theorem is an integral, top-tagged packet
near-factor which is simultaneously pseudorandom in its cyclic interval
flags.  No sharp counting obstruction is found, but ambient
degree-codegree data alone do not supply the required rounding.

## 1. Exact calibration

The consecutive ratio is

\[
 {\lambda_{h+1}\over\lambda_h}
 ={m+h+1\over m-h}.                                \tag{1.1}
\]

Minimality in (0.2) gives

\[
 \lambda_{H-1}<m+H-1=M-1.                        \tag{1.2}
\]

Using (1.1),

\[
 \lambda_H
 =\lambda_{H-1}{m+H\over m-H+1}
 <(M-1){M\over m-H+1}.                           \tag{1.3}
\]

Dividing by \(M\) and combining with (0.2) yields the exact window

\[
 \boxed{
 1\le{\lambda_H\over M}
 <{M-1\over m-H+1}
 =1+{2H-2\over m-H+1}.}                          \tag{1.4}
\]

In particular, once \(H=o(m)\), equation (0.4) follows.

For \(h=o(m^{2/3})\), Taylor expansion of (1.1) gives uniformly

\[
 \log\lambda_h
 ={h^2\over m}
 +O\left({h\over m}+{h^3\over m^2}\right).       \tag{1.5}
\]

For fixed \(\varepsilon>0\), substitute

\[
 h_-=(1-\varepsilon)\sqrt{m\log m},\qquad
 h_+=(1+\varepsilon)\sqrt{m\log m}.
\]

Then

\[
 \lambda_{h_-}=m^{(1-\varepsilon)^2+o(1)}<m+h_-,
\]

while

\[
 \lambda_{h_+}=m^{(1+\varepsilon)^2+o(1)}>m+h_+.
\]

Thus \(h_-<H<h_+\) for all large \(m\), proving (0.3).  In particular
\(H=o(m)\), so (1.4) proves (0.4).

Let

\[
 \rho={M\over\lambda_H}.
\]

Then (1.4) gives

\[
 1-O(H/m)<\rho\le1.                               \tag{1.6}
\]

Since \(N_H=W/\lambda_H\),

\[
 MN_H=\rho W=W-O(WH/m)=W-o(W),                   \tag{1.7}
\]

and

\[
 HN_H={H\over\lambda_H}W
 \le {H\over M}W=o(W).                           \tag{1.8}
\]

This proves (0.5).  Notice the direction: the calibrated total slot count
lies just **below** \(W\), unlike the preceding threshold convention
\(\lambda_H\le M\), whose slot count lies just above \(W\).

The outer-tail count is also negligible.  Since

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1}\le e^{-H/m}
 \qquad(q\ge H),                                  \tag{1.9}
\]

one has

\[
 2\sum_{q=H+1}^{m}N_q
 =O\left({m\over H}N_H\right)
 =O(W/H)=o(W).                                    \tag{1.10}
\]

## 2. Exact packet and flags

Fix a top

\[
 U=\{u_0,u_1,\ldots,u_{M-1}\}
\]

with a directed cyclic order.  For cyclic indices, put

\[
 X_t=\{u_t,u_{t+1},\ldots,u_{t+m-1}\}.            \tag{2.1}
\]

The transition

\[
 X_t\longrightarrow X_{t+1}
 =X_t-u_t+u_{t+m}                                 \tag{2.2}
\]

is the last-position promotion in the full radius-\(H\) state with

\[
 \alpha_t=(u_t,u_{t+1},\ldots,u_{t+H-1}),         \tag{2.3}
\]

\[
 \beta_t=(u_{t-1},u_{t-2},\ldots,u_{t-H}).        \tag{2.4}
\]

The \(M\) states form a promotion cycle.  Their flags are

\[
 L_q(t)=\{u_{t+q},\ldots,u_{t+m-1}\},             \tag{2.5}
\]

\[
 U_q(t)=\{u_{t-q},\ldots,u_{t+m-1}\}             \tag{2.6}
\]

for \(0\le q\le H\).  These are cyclic intervals of lengths \(m-q\)
and \(m+q\).  For fixed \(q\), the \(M\) lower flags are distinct; the
\(M\) upper flags are distinct for \(q<H\), while

\[
 U_H(t)=U                                           \tag{2.7}
\]

for every phase.

Call the data

\[
 P(U,\pi)=
 \left(U,\{X_t\}_{t\in\mathbb Z_M},
       \{L_q(t),U_q(t)\}_{q,t}\right)             \tag{2.8}
\]

a directed top packet.  Cyclic rotations of \(\pi\) give the same indexed
packet; reversal is retained as the opposite directed packet.

Selecting one packet at each top creates \(N_H\) promotion cycles.  Cutting
one arc in each cycle gives path count \(N_H\) and reset toll

\[
 2HN_H=o(W)                                        \tag{2.9}
\]

by (1.8).

## 3. The top-owner packet hypergraph

Let \(\mathcal T\) contain one tag vertex \(t_U\) for every top, and let
\(\mathcal V_0=\binom{[2m]}m\) be the owner vertices.  The packet column
\((U,\pi)\) is the hyperedge

\[
 e(U,\pi)=\{t_U\}\cup\{X_t:t\in\mathbb Z_M\}.    \tag{3.1}
\]

It has size \(M+1\).  A matching covering every top tag chooses one packet
per top and makes their owner packets pairwise disjoint.  Since their total
owner mass is \(MN_H=\rho W\), such a matching would cover
\(W-o(W)\) owners.

Repeated columns which happen to have the same unlabelled owner set are
retained; all degree statements concern this directed-column multihypergraph.

### Proposition 3.1 (exact degrees)

The top and owner degrees are

\[
 \boxed{D_T=(M-1)!,}                               \tag{3.2}
\]

\[
 \boxed{
 D_0=\binom mH m!H!
 ={M\over\lambda_H}D_T=\rho D_T.}                \tag{3.3}
\]

#### Proof

A directed cyclic order of an \(M\)-set, modulo rotation, has
\((M-1)!\) possibilities, proving (3.2).

Fix an owner \(X\).  A containing top is obtained by choosing \(H\) of
the \(m\) coordinates outside \(X\), giving \(\binom mH\) choices.  In a
fixed top, make \(X\) one cyclic block.  Its internal order has \(m!\)
choices, and the cyclic order of that block together with the other \(H\)
singletons has \(H!\) choices.  This proves the first formula in (3.3).

Alternatively, double count packet-owner incidences:

\[
 N_HD_TM=WD_0.
\]

Since \(W=\lambda_HN_H\), this gives the second formula. \(\square\)

Thus the two vertex classes are not exactly regular, but their degree
ratio is \(\rho=1-o(1)\), precisely the unavoidable missing-owner
fraction.

## 4. Exact owner codegrees

For owners \(X,Y\), put

\[
 j=|X\setminus Y|=|Y\setminus X|.                 \tag{4.1}
\]

If a common top \(U\) exists, their complementary \(H\)-sets

\[
 Q_X=U\setminus X,\qquad Q_Y=U\setminus Y        \tag{4.2}
\]

have the same distance \(j\).

### Theorem 4.1 (exact overlap codegree)

For \(1\le j<H\),

\[
 \boxed{
 {\operatorname {codeg}(X,Y)\over D_0}
 ={2\over\binom mj^2}.}                          \tag{4.3}
\]

For \(j>H\), the codegree is zero.  For \(j=H\),

\[
 {\operatorname {codeg}(X,Y)\over D_0}
 \le {M\over\binom mH^2}.                        \tag{4.4}
\]

Consequently, for \(H\ge2\),

\[
 \boxed{
 \max_{X\ne Y}{\operatorname {codeg}(X,Y)\over D_0}
 ={2\over m^2}.}                                 \tag{4.5}
\]

#### Proof

Fix a packet containing \(X\).  Its top is uniformly distributed among
the \(\binom mH\) tops containing \(X\).  To contain \(Y\), it must include
the \(j\) coordinates in \(Y\setminus X\).  Hence

\[
 \Pr(Y\subset U\mid X\subset U)
 ={\binom{m-j}{H-j}\over\binom mH}
 ={\binom Hj\over\binom mj}.                     \tag{4.6}
\]

Condition on such a top and on \(Q_X\) being a cyclic \(H\)-interval.
For \(Q_Y\) also to be an interval when \(j<H\), the specified set
\(Q_X\setminus Q_Y\) must occupy one of the two endpoint blocks of length
\(j\), and the specified set \(Q_Y\setminus Q_X\) must occupy the adjacent
outside block.  Therefore

\[
 \Pr(Q_Y\text{ is an interval}\mid Q_X\text{ is an interval})
 ={2\over\binom Hj\binom mj}.                     \tag{4.7}
\]

Multiplying (4.6) and (4.7) gives (4.3).

If \(j>H\), the union \(X\cup Y\) has more than \(m+H=M\) elements, so
no common top exists.  If \(j=H\), the two complementary \(H\)-sets are
disjoint.  Given the first interval, there are at most \(M\) possible
cyclic locations for the second interval, while a specified \(H\)-subset
of the remaining \(m\) coordinates has probability at most
\(1/\binom mH\) at any one location.  Combine this with the top probability
\(1/\binom mH\) to get (4.4).  Finally (4.3) is maximized at \(j=1\), and
the remaining bounds are smaller for the present growing \(H\). \(\square\)

There are two other elementary codegrees:

\[
 \operatorname {codeg}(t_U,X)=
 \begin{cases}
  m!H!,&X\subset U,\\
  0,&X\not\subset U,
 \end{cases}                                      \tag{4.8}
\]

and two different top tags have codegree zero.

## 5. Flag degrees and the augmented packet system

For \(0\le q\le H\), let

\[
 \mathcal V_q^- =\binom{[2m]}{m-q},\qquad
 \mathcal V_q^+ =\binom{[2m]}{m+q}.               \tag{5.1}
\]

Decorate every packet column by the flag sets in (2.5)-(2.6).  For
\(q<H\), it contains \(M\) distinct vertices in each of
\(\mathcal V_q^-\) and \(\mathcal V_q^+\).  It also contains \(M\)
distinct lower depth-\(H\) flags and the one upper depth-\(H\) top tag.

### Proposition 5.1 (exact flag degrees)

Every target in either rank \(m-q\) or rank \(m+q\), for \(q<H\), has
column degree

\[
 \boxed{
 D_q=D_T{MN_H\over N_q}
 =D_T{M\lambda_q\over\lambda_H}
 =D_T\rho\lambda_q.}                              \tag{5.2}
\]

Every lower depth-\(H\) target has degree \(MD_T\), while every upper
depth-\(H\) target is a top and has degree \(D_T\).

#### Proof

There are \(N_HD_T\) packet columns.  At a proper flag rank, every column
contains \(M\) distinct targets.  Coordinate transitivity makes their
degrees equal, so division by \(N_q\) gives (5.2).  The two depth-\(H\)
claims follow in the same way, using (2.7) on the upper side. \(\square\)

The exact integral target can now be stated with binary variables
\(z_{U,\pi}\):

\[
 \sum_{\pi}z_{U,\pi}=1\qquad(U\in\mathcal T),      \tag{5.3}
\]

middle collision

\[
 C_0=MN_H-\left|\bigcup_{z_{U,\pi}=1}\{X_t\}\right|=o(W), \tag{5.4}
\]

and flag holes

\[
 h_q^\pm=
 \left|\mathcal V_q^\pm\setminus
 \bigcup_{z_{U,\pi}=1}\{L_q(t)\text{ or }U_q(t)\}\right|
 =o(W)                                             \tag{5.5}
\]

for every \(q\le H\).  At upper depth \(H\), (5.3) gives \(h_H^+=0\)
exactly.

This is the **augmented calibrated top-packet near-factor**.

It should not be converted into an ordinary matching by simply adjoining
all flag vertices to (3.1).  At depth \(q>0\), the average required flag
multiplicity is about \(\lambda_q\), not one; forcing flag disjointness
would discard valid capacity.  One may formally clone target vertices
according to floor/ceiling quotas, but the nested same-phase correlations
then remain.

### Proposition 5.2 (critical cross-rank codegree)

Fix an owner \(X\) and a rank-\((m-1)\) facet \(T\subset X\).  Among packet
columns containing \(X\), the fraction in which the phase of \(X\) has
lower flag \(T\) is exactly

\[
 \boxed{{1\over m}.}                               \tag{5.6}
\]

The analogous owner/upper-first-flag fraction is also \(1/m\).

#### Proof

Condition on a packet containing \(X\).  In its directed cyclic interval,
the coordinate deleted at the next phase is uniformly distributed over
the \(m\) coordinates of \(X\).  The lower first flag is \(T\) exactly
when that coordinate is the unique member of \(X\setminus T\), proving
(5.6).  Reversal or the identical entrance calculation gives the upper
statement. \(\square\)

Thus owner-owner codegrees are of order \(D_0/m^2\), but the augmented
owner-flag incidence already has order \(D_0/m\).  This is not an error:
one flag is deterministically attached to every owner phase.  It explains
why an all-ranks hypergraph matching theorem cannot use only the
owner-owner codegree (4.5).

## 6. Exact fractional near-factor

Give every packet column at a fixed top weight

\[
 {1\over D_T}.                                     \tag{6.1}
\]

Then every top has total weight one.  Equations (3.3) and (5.2) give

\[
 \text{owner load}=\rho={M\over\lambda_H}=1-o(1), \tag{6.2}
\]

and, at every proper flag rank,

\[
 \text{target load}=\rho\lambda_q.                \tag{6.3}
\]

If \(\rho\lambda_q\ge1\), every flag target is fractionally covered.  If
\(\rho\lambda_q<1\), the total fractional deficiency at that rank is

\[
 N_q(1-\rho\lambda_q)
 =N_q-MN_H
 \le W-MN_H=o(W).                                 \tag{6.4}
\]

Thus:

### Theorem 6.1 (fractional augmented near-factor)

The calibrated packet orbit has one packet of total weight one at every
top, owner deficiency \(W-MN_H=o(W)\), and aggregate flag deficiency
\(o(W)\) at every band rank.

In fact the deficiencies sum to \(o(W)\) over the whole growing band, not
merely rank by rank.  Put \(L=MN_H\).  The deficit in one represented rank
is exactly \((N_q-L)_+\).  Equations (1.5) and (1.6) give

\[
 W-L=O(WH/m),\qquad
 \log{W\over L}=O(H/m).                            \tag{6.5}
\]

Also, uniformly for \(q\le H\),

\[
 \log{W\over N_q}
 ={q^2\over m}
 +O\left({q\over m}+{q^3\over m^2}\right).       \tag{6.6}
\]

Thus \(N_q\le L\) once \(q\ge c\sqrt H\), for a sufficiently large
absolute constant \(c\).  There are only \(O(\sqrt H)\) remaining depths,
and each positive deficit is at most \(W-L\).  Therefore

\[
 \sum_{q=0}^{H}(N_q-L)_+
 =O\left({WH^{3/2}\over m}\right)=o(W),           \tag{6.7}
\]

because \(H\asymp\sqrt{m\log m}\).  The same bound holds above the
middle.  Hence the uniform orbit weights solve the augmented fractional
problem with **aggregate** band deficiency \(o(W)\).  The only missing step
is integral correlated rounding.

## 7. Why independent top rounding fails

Choose one directed cyclic order independently and uniformly at every top.
Fix an owner \(X\).  In any one containing top, the probability that it is
one of the \(M\) cyclic windows is

\[
 {M\over\binom MH}.                                \tag{7.1}
\]

There are \(\binom mH\) containing tops, independently sampled.  Their
mean number of hits is

\[
 \binom mH{M\over\binom MH}
 ={M\over\lambda_H}=\rho=1-o(1).                  \tag{7.2}
\]

Since the individual probability in (7.1) tends to zero,

\[
 \Pr(X\text{ is missed})
 =\left(1-{M\over\binom MH}\right)^{\binom mH}
 =e^{-1}+o(1).                                    \tag{7.3}
\]

Therefore independent topwise selection leaves

\[
 (e^{-1}+o(1))W                                  \tag{7.4}
\]

owners uncovered in expectation.  The same occupancy phenomenon occurs
in every shallow flag rank whose fractional load tends to one.  Exact top
tags and the correct scalar slot count therefore do not make independent
rounding viable.

## 8. The matching boundary

Ignoring flags, the top-owner hypergraph has:

\[
 \text{edge size }M+1\asymp m,
\]

\[
 {D_0\over D_T}=1-o(1),
\]

and

\[
 {\Delta_2\over D_0}={2\over m^2}.                \tag{8.1}
\]

These are precisely the statistics expected of a near-factor instance.
However, the uniformity grows with \(m\), and

\[
 M^2{\Delta_2\over D_0}=2+o(1),                  \tag{8.2}
\]

rather than tending to zero.  Therefore the usual fixed-uniformity
degree-codegree nibble implication is not a theorem here.  The adjacent
owner pairs causing (8.2) are not diffuse noise: in every packet they are
the \(M\) consecutive edges of one quotient cycle.

The top tags expose useful extra structure:

1. every selected packet has a different top automatically;
2. within a top, every owner occurs in the same number \(m!H!\) of cyclic
   orders;
3. the maximum owner codegree comes only from the two possible cyclic
   adjacencies at each Johnson distance; and
4. all flags are deterministic interval shadows of that same cyclic
   quotient row.

A successful integral theorem must use this quotient-row structure, for
example through an absorption scheme which trades whole cyclic intervals
between tops.  Treating the columns as anonymous \((M+1)\)-sets discards
the only information not already summarized by the critical expression
(8.2).

The owner-preserving version of this proposal is analyzed in
`MATH_ATTACK_ALTERNATING_PACKET_OWNER_EXCHANGES_20260725.md`. Its signed
shadow image is the full zero-point-margin lattice, but an Eulerian
owner-overlay cycle is not generally a packet subtrade: atomicity forces
closure under all \(M\) owner incidences, hence under whole connected
overlay components. Nontrivial squarefree components must also lie in the
coordinate 2-core of their active top family. The remaining positive route
therefore requires long packet-cycle reassemblies with bounded top
congestion, not ordinary alternating-cycle decomposition.

There is nevertheless a canonical near-preserving reassembly once the
owner near-transversal exists: for every coordinate permutation \(g\), the
reindexed family \(g\mathcal F\) differs from \(\mathcal F\) in only
\(o(W)\) owner occurrences. Hybridizing across matched-overlay components
has congestion one, and cutting a component adds exactly the owner-boundary
counterterm recorded in that note. Thus frame mixing itself has no further
owner-capacity toll; the open issue is shallow collision descent across a
low-boundary automorphism overlay.

## 9. Exact remaining theorem

The calibrated route reduces coefficient one to the following statement.

> **Calibrated top-packet near-factor \((\mathrm{CTPF})\).**  At the first
> depth \(H\) satisfying \(\lambda_H\ge m+H\), choose one directed cyclic
> order in every top \(U\in\binom{[2m]}{m+H}\) so that the resulting
> packets have total middle collision \(C_0=o(W)\) and satisfy the aggregate
> flag-hole bound
> \[
> \sum_{q=1}^{H}(h_q^-+h_q^+)=o(W).                \tag{9.1}
> \]

The aggregate condition in (9.1) is essential.  Merely requiring
\(h_q^\pm=o(W)\) separately at every one of the growing number \(2H\) of
ranks does not imply an \(o(W)\) literal repair cost.

No collision deletion or packet fragmentation is needed.  Keep every
selected packet intact and cut only one promotion edge in each of the
\(N_H\) packet cycles.  The packets use \(L=MN_H\) state entries and have
only \(N_H\) path initializations, whose total excess is \(O(HN_H)=o(W)\).
Since their owner union has size \(L-C_0\), append the

\[
 W-(L-C_0)=W-L+C_0                              \tag{9.2}
\]

missing middle owners literally.  The packet entries plus these middle
repairs total \(W+C_0\).  Append the flag holes in (9.1), and finally the
outer tails (1.10).  The resulting nonzero contiguous-OR word has length

\[
 W+C_0+o(W)=W+o(W).                              \tag{9.3}
\]

Thus collision clustering is not an additional gate: repeated owner
occurrences are harmless at total scale \(o(W)\) when the complete packet
cycles are retained.

## 10. Audit ledger

### Proved

1. The calibrated depth satisfies \(H\sim\sqrt{m\log m}\).
2. The overshoot is \(\lambda_H/(m+H)=1+O(H/m)=1+o(1)\).
3. The packet owner mass is \(MN_H=W-o(W)\), and its reset toll is
   \(HN_H=o(W)\).
4. One cyclic order per top is an exact full-depth promotion packet.
5. The top and owner degrees are (3.2)-(3.3).
6. The exact owner-pair codegree is (4.3), with maximum \(2/m^2\).
7. All flag degrees are (5.2), and owner/first-flag codegree is \(1/m\).
8. Uniform orbit weights solve the augmented near-factor fractionally with
   \(o(W)\) deficiency summed over the entire growing band.
9. Independent topwise rounding leaves a positive fraction of owner holes.
10. The two outer tails contain only \(O(W/H)=o(W)\) masks.
11. Owner collisions of total size \(o(W)\) require no extra packet cuts;
    keeping all cycles intact gives the exact length ledger (9.2)--(9.3).

### Open

1. An integral owner-disjoint packet near-factor selecting one order at
   every top.
2. Simultaneous aggregate \(o(W)\)-hole control for all cyclic interval
   flag ranks.
3. Therefore \((\mathrm{CTPF})\) and coefficient one by this route.

No counting obstruction refutes the calibrated packet proposal.  Its
owner-only hypergraph lies exactly at a growing-uniformity codegree
boundary, and its augmented all-ranks version has a stronger deterministic
owner-flag correlation.  Those are the two issues an integral proof must
exploit rather than average away.
