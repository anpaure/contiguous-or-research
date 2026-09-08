# TRP whole-transversal law: exact queue Hall equations and a balanced hidden-color obstruction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result and scope

Put

\[
 M=m+H,\qquad \ell=m-Q,\qquad k=2Q,\qquad r=H-Q,
 \qquad M=\ell+k+r,
\tag{0.1}
\]

and assume

\[
 2\le Q<H<m,\qquad \ell,r\ge2.
\tag{0.2}
\]

For one fixed top (U), a radius-(Q) carrier state is

\[
 \omega=(L;z_1,\ldots,z_k;R),
 \qquad |L|=\ell,\quad |R|=r,
\tag{0.3}
\]

and a rotor edge is

\[
 (L;z_1,\ldots,z_k;R)
 \longrightarrow
 (L-x+y;x,z_1,\ldots,z_{k-1};R-y+z_k)
\tag{0.4}
\]

for (x\in L) and (y\in R).

This note proves three statements.

1. A prescribed state measure (c) is stationary under some legal rotor
   transport if and only if it satisfies the exact weighted Hall system

   \[
    c(A)\le c(N^+(A))\qquad(A\subseteq\operatorname{supp}c).
   \tag{0.5}
   \]

   In particular, stationarity forces equality of all consecutive ordered
   queue-word histograms, not merely equality of point marginals.

2. At the fractional level there is no obstruction.  The uniform state
   measure and the uniform rotor kernel are stationary, and, after summing
   over all tops, give the exact balanced top-rooted flag flow.

3. Aggregate balance does not disintegrate into legal whole
   transversals.  There is an explicit full-coordinate orbit of integral
   (M)-column top tables such that:

   * within every table, all controlled flags are distinct and all
     one-coordinate queue, reservoir, and flag marginals are exact;
   * aggregated over the coordinate orbit, every state occurs with the
     same integral multiplicity and every rank target occurs with the same
     integral multiplicity;
   * nevertheless, the selected-state rotor graph inside every table has
     no edges.  Its Hall deficiency is exactly (M).

Thus even an exactly uniform, maximally symmetric stationary marginal law
does not imply a color-preserving integral path factorization.  This is a
strict strengthening of a non-total-unimodularity warning: the conditional
transport polytope can be empty while every aggregate scalar balance is
exact.

The scope is important.  The orbit uses many colored copies of each top.
It refutes any deduction of a legal trajectory from aggregate balance or
from a stationary law after forgetting the color.  It does **not** prove
that no different one-table-per-top balanced resolution exists.

## 1. Exact stationary-transport criterion

Fix a top (U) and let \(\Omega(U)\) be its state space.  For a
nonnegative state weight (c:\Omega(U)\to\mathbb R_{\ge0}), call a family

\[
 f(\omega,\eta)\ge0\qquad(\omega\to\eta)
\tag{1.1}
\]

a stationary rotor transport of (c) when

\[
 \sum_{\eta:\omega\to\eta}f(\omega,\eta)=c(\omega),
 \qquad
 \sum_{\omega:\omega\to\eta}f(\omega,\eta)=c(\eta).
\tag{1.2}
\]

If (c) is normalized, this is exactly a Markov kernel supported on legal
rotor edges and having stationary measure (c).

### Theorem 1.1 (weighted successor Hall theorem)

A stationary rotor transport of (c) exists if and only if

\[
 \boxed{c(A)\le c(N^+(A))\quad\hbox{for every }A\subseteq\operatorname{supp}c,}
\tag{1.3}
\]

where

\[
 N^+(A)=\{\eta\in\operatorname{supp}c:
                   \omega\to\eta\text{ for some }\omega\in A\}.
\]

If (c) is integral, (f) may be chosen integral; after splitting a
state of weight (c(\omega)) into copies, the resulting successor system
is a disjoint union of directed cycles.

#### Proof

Make a bipartite graph with a source copy and a target copy of
\(\operatorname{supp}c\), joining \(\omega_{\rm out}\) to
\(\eta_{\rm in}\) precisely when \(\omega\to\eta\).  Give the left copy
of \(\omega\) supply (c(\omega)) and the right copy demand
(c(\omega)).  A feasible transportation is exactly (1.2).

Necessity of (1.3) follows by sending all mass out of (A): it can enter
only (N^+(A)).  Conversely, the max-flow min-cut theorem says that a
bipartite transportation with equal total supply and demand is feasible
exactly when all inequalities (1.3) hold.  If all weights are integral,
integrality of bipartite flow gives integral (f).  Pair the incoming and
outgoing copies at each state.  Every resulting copy has indegree and
outdegree one, so the copies decompose into directed cycles. \(\square\)

The theorem gives a complete test for stationary realizability.  It also
gives useful compulsory equalities which are absent from rankwise balanced
flow.

### Proposition 1.2 (ordered queue-cylinder stationarity)

If (c) admits a stationary rotor transport, then for every
(1\le s<k), every injective word (w) of length (s), and every
(1\le j<k-s+1),

\[
 \boxed{
 \sum_{\omega:(z_j,\ldots,z_{j+s-1})=w}c(\omega)
 =
 \sum_{\omega:(z_{j+1},\ldots,z_{j+s})=w}c(\omega).}
\tag{1.4}
\]

In particular,

\[
 \boxed{
 c\{(z_1,\ldots,z_{k-1})=w\}
 =c\{(z_2,\ldots,z_k)=w\}.}
\tag{1.5}
\]

For every coordinate (a\in U), the quantities

\[
 q_{a,j}=\sum_{\omega:z_j=a}c(\omega)
\tag{1.6}
\]

are independent of (j).  Their common value (q_a) is also both the
stationary flux at which (a) is selected from (L) and the stationary
flux at which (a) is selected from (R).

#### Proof

On every edge \(\omega\to\eta\), (0.4) gives

\[
 (z_{j+1}(\eta),\ldots,z_{j+s}(\eta))
 =(z_j(\omega),\ldots,z_{j+s-1}(\omega)).
\tag{1.7}
\]

Sum (f(\omega,\eta)) over the edges for which either side equals (w).
The source marginal in (1.2) gives the left occurrence count and the
target marginal gives the right occurrence count, proving (1.4).  Taking
(s=1) proves that (1.6) is independent of (j).

On an edge, the coordinate selected from (L) becomes the target's first
queue coordinate.  Hence its stationary selection flux is (q_{a,1}).
Also the source (R)-selection enters (L), whereas the selected
(L)-coordinate leaves (L).  Summing the indicator of (a\in L) in
the two marginal identities (1.2) shows that these two selection fluxes
are equal.  Both therefore equal (q_a). \(\square\)

After normalizing (c) to a probability measure, (1.5) has the entropy
consequence

\[
 H(z_1\mid z_2,\ldots,z_{k-1})
 =H(z_k\mid z_2,\ldots,z_{k-1}).
\tag{1.8}
\]

Indeed (1.5) equates the two ((k-1))-word distributions; subtract the
entropy of the common middle word.  Rank-set balance does not see (1.5)
or (1.8), because it forgets the order of the queue.

## 2. The canonical fractional stationary law

Every state has exactly

\[
 D=\ell r=(m-Q)(H-Q)
\tag{2.1}
\]

outgoing rotor edges.  It also has (D) incoming edges.  Indeed, if

\[
 \eta=(L';u_1,\ldots,u_k;R'),
\]

choose (y\in L') and (v\in R'), and put

\[
 \omega=(L'-y+u_1; u_2,\ldots,u_k,v; R'-v+y).
\tag{2.2}
\]

Then (0.4), with (x=u_1), sends \(\omega\) to \(\eta\), and every
predecessor arises uniquely this way.  Thus the uniform state measure
\(\pi_U\) is stationary for the kernel (P_U) which chooses
\((x,y)\in L\times R\) uniformly.

For a state at top (U), define its controlled flags by

\[
 F_q^-(\omega)=L\cup\{z_1,\ldots,z_{Q-q}\},
 \qquad 0\le q\le Q,
\tag{2.3}
\]

\[
 F_q^+(\omega)=L\cup\{z_1,\ldots,z_{Q+q}\},
 \qquad 0\le q\le Q.
\tag{2.4}
\]

The symmetric group of (U) is transitive on states and on subsets of
every fixed size, while (2.3)--(2.4) are equivariant.  Consequently, under
\(\pi_U\), each flag of rank (s) is uniform on \(\binom Us\).

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad N_s=\binom{2m}s,
 \qquad \mathcal T=M|\mathcal U|.
\tag{2.5}
\]

Give every top mass (M) times its uniform stationary state measure.  For
a fixed ambient rank-(s) target (S), its total flag mass is

\[
 \frac{M}{\binom Ms}
 \#\{U\in\mathcal U:S\subseteq U\}
 =\frac{M}{\binom Ms}\binom{2m-s}{M-s}
 =\frac{M\binom{2m}M}{\binom{2m}s}
 =\frac{\mathcal T}{N_s}.
\tag{2.6}
\]

This is exactly the symmetric fractional throughput of the balanced
top-rooted flag flow.  Hence there is a stationary coupling with the
desired balanced marginal at the level of measures.  The remaining issue
is whether it admits a color-preserving integral disintegration with only
(M) columns at each top.

## 3. A locally balanced (M)-column anticycle

Identify one top with the cyclic group

\[
 U_0=\mathbb Z_M.
\]

Use cyclic half-open interval notation, with the following representatives
in \(\{0,1,\ldots,M-1\}\).  Put

\[
 L_0=\{Q,Q+1,\ldots,m-1\},
 \qquad
 R_0=\{m+Q,m+Q+1,\ldots,M-1\},
\tag{3.1}
\]

and define the queue-offset word

\[
 (\sigma_1,\ldots,\sigma_k)
 =(0,1,\ldots,Q-1, m,m+1,\ldots,m+Q-1).
\tag{3.2}
\]

For every (i\in\mathbb Z_M), let

\[
 \omega_i=
 \bigl(i+L_0; i+\sigma_1,\ldots,i+\sigma_k; i+R_0\bigr).
\tag{3.3}
\]

All additions are modulo (M).  The three displayed parts partition
\(U_0\), so these are valid carrier states.

Complete each state to a full top-rooted nested column through all ranks

\[
 m-H,m-H+1,\ldots,M
\tag{3.3a}
\]

as follows.  Below its deepest controlled lower flag, use the translates
of

\[
 B_s^-=\{m-s,m-s+1,\ldots,m-1\}
 \qquad(m-H\le s\le m-Q),
\tag{3.3b}
\]

and above its deepest controlled upper flag use the translates of

\[
 B_s^+=\{0,1,\ldots,s-1\}
 \qquad(m+Q\le s\le M).
\tag{3.3c}
\]

At the joining ranks, (3.3b) is \(\{Q,\ldots,m-1\}=A_Q^-\) and
(3.3c) is \(\{0,\ldots,m+Q-1\}=A_Q^+\), so these sets really form one
nested column with the controlled flags.

### Theorem 3.1 (rainbow anticycle table)

The (M)-state table

\[
 \mathcal C_0=\{\omega_i:i\in\mathbb Z_M\}
\tag{3.4}
\]

has all of the following properties.

1. For each queue position (j) and each coordinate (a\in U_0), exactly
   one state has (z_j=a).  Each coordinate belongs to exactly \(\ell\)
   of the sets (L_i) and exactly (r) of the sets (R_i).
2. At every proper column rank \(m-H\le s<M\), the (M) flags are
   distinct.  Every coordinate belongs to exactly (s) of them.  At the
   top rank (M), all (M) columns have the required common root (U_0).
   Hence this is an exact per-top floor/ceiling balanced full flag table,
   not merely a controlled-band table.
3. There is no rotor edge from one member of \(\mathcal C_0\) to another.
   Therefore the stationary-transport Hall deficiency of this table is
   exactly (M).  Moreover, its length-\((k-1)\) prefix and suffix
   histograms have disjoint supports, so the \(\ell^1\) defect in (1.5)
   is exactly \(2M\), even though every length-one positional histogram
   is perfectly balanced.

#### Proof

For fixed (j,a), the unique solution of

\[
 i+\sigma_j=a
\]

is (i=a-\sigma_j), proving the queue assertion.  The reservoir assertions
follow in the same way by counting translates of (L_0) and (R_0).

The base lower and upper flags are

\[
 A_q^-=
 \{0,\ldots,Q-q-1\}\cup\{Q,\ldots,m-1\},
\tag{3.5}
\]

\[
 A_q^+=\{0,1,\ldots,m+q-1\},
\tag{3.6}
\]

with the first interval in (3.5) empty when (q=Q).  The flags of
\(\omega_i\) are (i+A_q^\pm).

Every proper nonempty cyclic interval has trivial translation stabilizer:
its directed entry boundary is unique and must be fixed.  This proves the
claim for (3.6), for (q=0) in (3.5), and for (q=Q) in (3.5).  If
(0<q<Q), the complement of (A_q^-) has two cyclic components, of
lengths (q) and (H), separated by nonempty gaps.  Since (q<H), its
length-(H) component is unique.  A translation stabilizing (A_q^-)
must fix that proper interval, and hence is zero.  Thus every orbit in
(3.5)--(3.6) has size (M).  This proves distinctness.  A coordinate is
contained in exactly \(|A_q^\pm|=m\pm q\) translates, proving exact point
incidence.

The extension sets (3.3b)--(3.3c) are proper nonempty cyclic intervals at
every rank below (M), so the same boundary argument proves that their
(M) translates are distinct.  A coordinate occurs in exactly (s)
translates of an (s)-set.  At rank (M), every translate is (U_0), as
required.  Since

\[
 \binom Ms\ge M\qquad(1\le s<M),
\tag{3.6a}
\]

with equality only at (s=1,M-1), these distinct proper-rank flags have
exactly the local floor/ceiling loads for (M) columns.  This completes
the proof of item 2.

It remains to prove the absence of edges.  If
\(\omega_i\to\omega_j\), the deterministic queue shift in (0.4) gives

\[
 j+\sigma_{t+1}=i+\sigma_t
 \qquad(1\le t<k).
\tag{3.7}
\]

Hence all successive differences \(\sigma_{t+1}-\sigma_t\) must equal the
same residue (i-j).  But (3.2) has successive difference (1) inside
each of its two blocks and difference

\[
 m-(Q-1)=m-Q+1
\tag{3.8}
\]

at their join.  These residues are different because (m>Q).  This is a
contradiction.

In the bipartite successor graph on the selected table, the neighbourhood
of all (M) source states is empty.  The Hall deficiency is therefore at
least (M), and it cannot exceed the total source mass (M).  The same
calculation shows that no source prefix

\[
 (i+\sigma_1,\ldots,i+\sigma_{k-1})
\]

equals any selected target suffix

\[
 (j+\sigma_2,\ldots,j+\sigma_k).
\]

Each of the two collections contains (M) distinct words, each with
weight one.  Their supports are disjoint, so the sum of the absolute
histogram differences is (M+M=2M). \(\square\)

Thus exact per-top floor/ceiling balance at every rank of the full nested
column, including complete diversity at every proper rank, does not imply
even one legal successor between the selected carrier states.

## 4. Full-coordinate orbit: exact aggregate balance and conditional emptiness

Embed (U_0) in the ambient coordinate set ([2m]), and let

\[
 G=S_{2m}.
\]

For each (g\in G), retain a color labelled (g), with top

\[
 U_g=gU_0
\]

and selected table

\[
 \mathcal C_g=g\mathcal C_0.
\tag{4.1}
\]

Rotor transitions commute with coordinate relabelling, so Theorem 3.1
gives:

\[
 \boxed{\text{Every color }g\text{ has successor Hall deficiency exactly }M.}
\tag{4.2}
\]

On the other hand, the aggregate multicover is exactly balanced at every
level.

### Theorem 4.1 (uniform integral orbit with no conditional transport)

In the multiset of all pairs ((g,\omega)) with
(g\in G) and \(\omega\in\mathcal C_g\):

1. every ambient radius-(Q) state occurs exactly

   \[
    \boxed{
    b_{\rm st}=M(m-H)!(m-Q)!(H-Q)!}
   \tag{4.3}
   \]

   times;
2. every ambient rank-(s) target, for every column rank
   \(m-H\le s\le M\), occurs exactly

   \[
    \boxed{b_s=M\,s!\,(2m-s)!}
   \tag{4.4}
   \]

   times as the corresponding flag;
3. every top (U\in\binom{[2m]}M) supports exactly

   \[
    \boxed{b_{\rm top}=M\,M!\,(2m-M)!}
   \tag{4.5}
   \]

   state occurrences.

Nevertheless, no positive amount of any color's mass can be transported
to the next round without changing its color.

#### Proof

The group (G) acts transitively on ambient states of the prescribed
block sizes.  The number of such states is

\[
 |\Omega|=
 \frac{(2m)!}{(2m-M)!(m-Q)!(H-Q)!}.
\tag{4.6}
\]

There are (M(2m)!) colored state occurrences in total.  Transitivity
therefore gives the common multiplicity

\[
 \frac{M(2m)!}{|\Omega|}
 =M(m-H)!(m-Q)!(H-Q)!,
\]

proving (4.3).

For a fixed column rank (s), each colored state occurrence supplies
one rank-(s) flag.  The coordinate group is transitive on rank-(s)
targets, so their common multiplicity is

\[
 \frac{M(2m)!}{\binom{2m}s}
 =M\,s!\,(2m-s)!,
\]

which proves (4.4).  A fixed top has

\[
 M!(2m-M)!
\]

preimages of (U_0) under (G), and each corresponding color has (M)
states.  This proves (4.5).

Finally, (4.2) says that the color-preserving successor graph has no edge.
Thus its only feasible transported mass is zero, whereas every color has
mass (M). \(\square\)

Let

\[
 K_0=M!(2m-M)!,
\tag{4.6a}
\]

the number of colors lying over any fixed top.  Divide the full orbit
weights by (K_0).  Then every actual top has mass exactly (M), while a
rank-(s) target has mass

\[
 \frac{b_s}{K_0}
 =\frac{M\binom{2m}{M}}{\binom{2m}{s}}
 =\frac{\mathcal T}{N_s}.
\tag{4.6b}
\]

Thus the normalized orbit is exactly the balanced fractional top-rooted
flow of (2.6), together with an explicit disintegration into integral
(M)-column rainbow tables.  Every conditional table remains maximally
Hall-deficient.

After color is forgotten, (4.3) is precisely an integral multiple of the
uniform state measure from Section 2.  In fact it admits an **integral**
uniform rotor transport: put multiplicity

\[
 b_{\rm edge}=\frac{b_{\rm st}}D
 =M(m-H)!(m-Q-1)!(H-Q-1)!
\tag{4.6c}
\]

on every directed rotor edge.  Every state then has total incoming and
outgoing multiplicity (Db_{\rm edge}=b_{\rm st}).  Integral bipartite
flow assigns the individual colored occurrences to these edge copies.
That assignment necessarily reconnects different colors over a common
top, because no target state of an edge from a color-(g) occurrence lies
in \(\mathcal C_g\).

This gives an exact disintegration obstruction:

\[
 \boxed{
 \begin{array}{c}
 \text{uniform stationary state law}\ +
 \text{exact integral rank balance}\ +
 \text{internally rainbow top tables}
 \\
 \not\Longrightarrow
 \text{stationary legal transport inside the given top tables}.
 \end{array}}
\tag{4.7}
\]

The obstruction is invisible to entropy after color is forgotten.  The
uniform rotor kernel has conditional entropy

\[
 H(\omega_{t+1}\mid\omega_t)=\log D,
\tag{4.8}
\]

the maximum possible because every state has (D) successors.  Conditional
on a color (g), however, there is no supported successor kernel at all.
Thus maximal marginal entropy does not imply an integral or even fractional
color-preserving factorization.

### Corollary 4.2 (global colors with one anticycle table at every top)

The one-top orbit can be strengthened so that every color is a complete
global top schedule.  For every

\[
 U\in\binom{[2m]}M
\]

fix an arbitrary bijection \(\phi_U:U_0\to U\), and put

\[
 \mathcal C=\bigsqcup_U \phi_U\mathcal C_0.
 \tag{4.9}
\]

Thus \(\mathcal C\) has exactly \(M\) columns at every top and

\[
 T=M\binom{2m}M
 \tag{4.10}
\]

columns in total.  For each \(g\in G\), regard \(g\mathcal C\) as one
global color.  Then every color again has exactly \(M\) columns at every
top; within every top all proper-rank flags are distinct and the
selected-state rotor graph has no edges.  Over all \(|G|=(2m)!\) colors,
every ambient quotient state occurs exactly

\[
 \boxed{T(m-H)!(m-Q)!(H-Q)!}
 \tag{4.11}
\]

times, and every ambient rank-\(s\) target occurs exactly

\[
 \boxed{T\,s!(2m-s)!}
 \tag{4.12}
\]

times.

#### Proof

The first assertions hold for \(\mathcal C\) by Theorem 3.1 and are
preserved by coordinate relabelling.  Fix one indexed column \(c\) of
\(\mathcal C\) and one ambient quotient state \(\omega\).  Transitivity
of \(G\) on quotient states shows that the permutations sending the state
of \(c\) to \(\omega\) form a coset of its stabilizer, of size

\[
 (m-H)!(m-Q)!(H-Q)!.
\]

Summing over the \(T\) indexed columns proves (4.11).  The same argument
at rank \(s\), whose stabilizer has size \(s!(2m-s)!\), proves
(4.12). \(\square\)

Dividing the global orbit by \(|G|=(2m)!\) leaves mass exactly (M) at
every top, because every individual global color already has that top
mass, and gives every rank-(s) target mass

\[
 \frac{T\,s!(2m-s)!}{(2m)!}
 =\frac{T}{\binom{2m}{s}}.
\tag{4.13}
\]

Thus color averaging is exactly, not asymptotically, the balanced
fractional top-rooted flow.

This global form still does not say that one color has the ambient
floor/ceiling target loads of the balanced-flow theorem.  It says
something different and exact: global one-table-per-top structure, local
floor/ceiling diversity inside every table, and exact aggregate target
balance do not force even one color-preserving rotor edge.  A
desymmetrization theorem must therefore control a conditional queue law,
not only aggregate rank loads.

## 5. Exact boundary for the whole-transversal route

At the coefficient-one calibration,

\[
 Q=\sqrt{m(\log\log m+o(\log\log m))},
 \qquad
 H=(1+o(1))\sqrt{m\log m},
\tag{5.1}
\]

so (0.2) holds for all sufficiently large (m), and

\[
 M=m+H=(1+o(1))m.
\tag{5.2}
\]

The conditional deficiency in (4.2) is therefore

\[
 M=(1+o(1))m
\tag{5.3}
\]

for every color: it is total, not a lower-order loss.  There are no
exceptional colors and no first legal edge to iterate.

Consequently a successful whole-transversal theorem must preserve more
than the exact balanced top-rooted flag measure.  It must produce, before
forgetting the top-table label, one of the following equivalent pieces of
information:

1. all weighted successor Hall inequalities (1.3);
2. a color-preserving circulation (1.2);
3. an integral cycle factorization of the selected state copies.

For an open trajectory cover, the corresponding split-graph maximum
matching and its Hall deficiency give the necessary boundary slack.  In
the anticycle table that matching has size zero, so its minimum directed
path-cover number is exactly (M), not (o(M)).

The ordered cylinder equations (1.4)--(1.5) are mandatory low-complexity
tests, but they are not asserted to be sufficient; the full Hall system is
the exact condition.  The construction above closes the proposed shortcut
from aggregate balanced stationarity to integral rotor trajectories.  It
does not close the possibility of choosing a different balanced integral
resolution whose top tables satisfy the Hall system from the outset.
