# Lane W: PBBS normalized ports versus crossing-window preservation

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact verdict

Put

\[
 N=2m+1,\qquad B=\operatorname {Cat}_m,\qquad W=NB,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where (A>0) is fixed.  Work in one exact PBBS factor and in one of its
step-two projected owner rows of rank (k\in\{m,m+1\}).  Every statement
below is integral and every constructed witness is an ordinary contiguous
OR in one literal word.

There are two different port notions, and confusing them is exactly the
source of the apparent fusion.

1. A proper maximal depth-(q) fixed-fibre run with (r\ge1) extension
   edges and (r+q+1) owner positions has an exact **sandwich chart** of
   length
   \[
      \boxed{r+2q+1=(r+q+1)+q.}                 \tag{0.1}
   \]
   Its exposed ports are two ordered strings of (q-1) singleton labels.
   These coarse ports forget the fixed carrier.  They suffice for all
   targets internal to the run.

2. For any freely reordered family of quotient runs, let (D_q) be the
   total positive degree imbalance in the directed multigraph of normalized
   singleton ports.  If (c_q) is the number of physical chains/cycles in
   a deckwise-uniform lifted trail decomposition, the canonical sandwich-
   chart construction has exact internal-chart excess
   \[
      \boxed{N\bar R_q+(q-1)c_q,}                \tag{0.2}
   \]
   where \(\bar R_q\) is the quotient run count.  Moreover
   \[
      c_q\le N\bigl(D_q+T_q\bigr),\qquad
      T_q=(N-1)_{q-2}\quad(q\ge2).               \tag{0.3}
   \]
   The catalog term is subexponential and hence (o(W)) uniformly for
   (q\le H).  The exact unresolved internal scalar in this construction is
   \[
      \boxed{\sum_q (q-1)D_q=o(B).}              \tag{0.4}
   \]
   On any growing-depth band this is asymptotically equivalent to
   \(\sum_q qD_q=o(B)\).
   The all-phase deck multiplies each quotient imbalance by (N); it does
   not average that imbalance away.  Even allowing reversal does not make
   (0.4) automatic: an explicit antisymmetric imbalance vector is invariant
   under every choice of chart orientations.

3. The coarse splice in (0.2) preserves only run-internal targets.  It
   freely changes the original PBBS order and therefore loses the windows
   crossing the original run boundaries.  The minimal chronology-bearing
   seam adds the carrier \(S\), retains the ordered \(q-1\) overlap, and
   requires the second run to begin at the actual PBBS successor of the
   first run's terminal owner.  This creates an exact PBBS-specific
   obstruction:

   > **Maximal-run chronological rigidity.**  Such a decorated seam glues
   > the two token lines into one longer fixed-\(S\) run.  Thus two
   > distinct proper maximal runs have no legal decorated join at their
   > original chronological boundary.

   A still stronger full \(q\)-port determines the complete boundary owner
   and is injective on quotient starts, but it describes an owner-overlap
   seam rather than the natural owner-disjoint seam.  Consequently the
   canonical chronology-preserving spine assembly has no joins and retains
   the exact spine-opening term
   \[
      \boxed{(q-1)N\bar R_q.}                    \tag{0.5}
   \]
   Giving every run a private carrier marker raises the declared
   construction to \(Nq\bar R_q\); equal markers may instead be shared.
   At the permitted critical scale \(\bar R_q=\Theta(B/q)\), the spine
   term in (0.5) is already \(\Theta(W)\).

4. The (4H-1) QCF chart still removes the two outer borders of a long
   all-phase block at total cost (O(NH)).  It cannot simply be appended
   at every residual isolated-run boundary: (\Theta(B/H)) quotient
   boundaries would cost (\Theta(W)).  Therefore the requested
   baseline-relative block compiler is **not obtained** by normalized-port
   grouping.  The exact escape left open is a nonlocal, noncellular PBBS
   crossing compiler which shares the crossing targets of many coarse-port
   splices at total (o(W)) cost.

This is an exact obstruction to the proposed fixed-fibre
normalized-port/QCF architecture.  It is not a lower bound against every
possible literal OR word, and no coefficient-one theorem is claimed.

## 1. Exact sandwich chart for one PBBS extension run

Fix (1\le q<k).  Let a proper nonwrapping maximal run have carrier (S),
(r\ge1) consecutive extension starts, and the audited sliding form

\[
 X_t=S\cup\{\gamma_t,\gamma_{t+1},\ldots,
                    \gamma_{t+q-1}\},
 \qquad 0\le t\le L:=r+q.                        \tag{1.1}
\]

Every displayed (q)-window has distinct labels.  Distant labels may
repeat.

### Lemma 1.1 (exact separation of repeated token occurrences)

If \(\gamma_a=\gamma_b\) and (a<b), then

\[
 b-a\ge q+1.                                     \tag{1.2}
\]

#### Proof

If (b-a<q), the two equal occurrences lie in one displayed active
(q)-window, contrary to (1.1).  If (b-a=q), then (a\le L-1) and the
Johnson transition from (X_a) to (X_{a+1}) removes \(\gamma_a\) and
adds \(\gamma_{a+q}=\gamma_a\).  It would be a lazy transition, contrary
to the PBBS owner edge.  Hence (1.2). \(\square\)

Define letters (E_j), (0\le j\le L+q-1), by

\[
 E_j=
 \begin{cases}
  \{\gamma_j\},&0\le j\le q-2,\\
  S\cup\{\gamma_j\},&q-1\le j\le L,\\
  \{\gamma_j\},&L+1\le j\le L+q-1.
 \end{cases}                                     \tag{1.3}
\]

The sandwich word is

\[
 \mathcal C(R)=E_0E_1\cdots E_{L+q-1}S.          \tag{1.4}
\]

All letters are nonempty because (q<k).

For later splicing, distinguish its **spliceable spine**

\[
 \mathcal E(R)=E_0E_1\cdots E_{L+q-1}            \tag{1.4a}
\]

from its terminal carrier marker \(S\).  The marker may be banked as a
standalone one-letter chart anywhere in the final word: it is used only
for intersections whose active part is empty.  Thus a family of runs may
first splice the words \(\mathcal E(R)\) and then append one literal
\(S_R\)-marker for every run.

### Theorem 1.2 (exact run compiler)

For every (0\le a\le b\le L), the word (1.4) contains literal
contiguous witnesses

\[
 \bigcup_{t=a}^{b}X_t
   =\bigcup_{j=a}^{b+q-1}E_j,                    \tag{1.5}
\]

and

\[
 \bigcap_{t=a}^{b}X_t
 =\begin{cases}
   \displaystyle\bigcup_{j=b}^{a+q-1}E_j,&b-a<q,\\[2mm]
   S,&b-a\ge q.
  \end{cases}                                    \tag{1.6}
\]

Its length is exactly

\[
 |\mathcal C(R)|=L+q+1=r+2q+1.                  \tag{1.7}
\]

#### Proof

An occurrence \(\gamma_j\) is active at owner times
([j-q+1,j]), clipped to ([0,L]).  By Lemma 1.1, two occurrence
intervals of the same physical label have at least one absent owner time
between them.  Therefore a label is present in every owner of a connected
interval ([a,b]) exactly when one occurrence interval contains
([a,b]).  This gives the active-label parts of (1.5)--(1.6).

The index interval ([a,b+q-1]) in (1.5) has at least (q) positions
and necessarily meets ([q-1,L]); hence its OR includes (S).  When
(b-a<q), the nonempty interval ([b,a+q-1]) in (1.6) likewise meets
([q-1,L]), so it also includes (S).  When (b-a\ge q), no active
occurrence interval covers ([a,b]), and the terminal letter (S)
represents the intersection.  Finally (1.3) has (L+q) letters and
(1.4) appends one more, proving (1.7). \(\square\)

Thus the (+q) in (0.1) is exact.  The last (S)-letter is indispensable
inside this chart architecture: owner intervals of span at least (q)
have intersection exactly (S).

### PBBS boundary-port form

The exposed singleton ports are

\[
 I_R=(\gamma_0,\ldots,\gamma_{q-2}),\qquad
 O_R=(\gamma_{L+1},\ldots,\gamma_{L+q-1}).       \tag{1.8}
\]

If the run starts at projected index (i) on parity (p), then the PBBS
omitted-label recurrence gives

\[
 I_R=(\lambda_{p+2i},\lambda_{p+2i+2},\ldots,
                  \lambda_{p+2i+2q-4}),          \tag{1.9}
\]

\[
 O_R=(\lambda_{p+2(i+r+1)+1},\ldots,
                  \lambda_{p+2(i+r+q-1)+1}),     \tag{1.10}
\]

where the interior extension identities are

\[
 \lambda_{p+2(i+t)+1}=\lambda_{p+2(i+t+q)},
 \qquad0\le t<r.                                 \tag{1.11}
\]

Hence (I_R) and (O_R) are exactly the two unmatched opposite-parity
boundary strings left by the run.

## 2. Coarse normalized-port trails: exact ledger

Assume (q\ge2).  For an ordered ((q-1))-tuple (P) of distinct
labels, define

\[
 \tau(P)=(p_2-p_1,\ldots,p_{q-1}-p_1)
 \in\mathbb Z_N^{q-2}.                           \tag{2.1}
\]

There are exactly

\[
 T_q=(N-1)_{q-2}                                 \tag{2.2}
\]

possible normalized types.  Here (T_2=1).  Equality
(\tau(O_R)=\tau(I_Q)) is equivalent to a unique translation

\[
 O_R=\rho^{c(R,Q)}I_Q.                           \tag{2.3}
\]

At the physical level, (2.3) identifies the suffix of one spliceable
spine \(\mathcal E(R)\) with the prefix of the uniquely shifted spine
\(\mathcal E(Q)\), saving exactly \(q-1\) letters.  The separately banked
carrier markers are not part of this overlap.

Form a directed quotient multigraph (G_q): each quotient run (R) is
one edge

\[
 \tau(I_R)\longrightarrow\tau(O_R).              \tag{2.4}
\]

For a weak component (C), put

\[
 D_C=\sum_v\bigl(d_C^+(v)-d_C^-(v)\bigr)_+.      \tag{2.5}
\]

If (D_C>0), its edges have a decomposition into exactly (D_C) directed
trails.  If (D_C=0), they have one Euler circuit.  This is the standard
degree-balancing proof: adjoin (D_C) edges from deficit to surplus
vertices to make the component Eulerian, take an Euler circuit, and cut
at the adjoined edges; minimality follows because every open trail accounts
for at most one unit of total positive imbalance.

Attach to every matched quotient join its unique phase voltage from
(2.3).  An open quotient trail lifts to exactly (N) open physical
trails.  If a chosen Euler circuit has total voltage
(\Delta_C\in\mathbb Z_N), its all-phase lift has exactly

\[
 \gcd(N,\Delta_C)                                \tag{2.6}
\]

physical cycles, because its return map on phases is
(u\mapsto u+\Delta_C).  We use the convention
(\gcd(N,0)=N).

### Theorem 2.1 (exact all-phase internal fusion ledger)

Let \(\bar R_q\) quotient run occurrences be supplied together with all
\(N\) phase lifts, and let
\[
 M_q=N\sum_R(r_R+q+1)                            \tag{2.6a}
\]
be the sum of their charged owner baselines, counted with multiplicity.
When the owner segments are pairwise disjoint, this is also their distinct
charged owner baseline.
Choose the trail/Euler decomposition above and put

\[
 c_q=
 N\sum_{C:D_C>0}D_C
 +\sum_{C:D_C=0}\gcd(N,\Delta_C).                \tag{2.7}
\]

Then all run-internal lower intersections and upper unions have a literal
word of exact length

\[
 \boxed{L_q=M_q+N\bar R_q+(q-1)c_q.}             \tag{2.8}
\]

Moreover, with (D_q=\sum_{C:D_C>0}D_C),

\[
 c_q\le N(D_q+T_q).                              \tag{2.9}
\]

#### Proof

Before splicing, the \(N\bar R_q\) spliceable spines together with their
one banked carrier marker per run have total length

\[
 M_q+qN\bar R_q                                  \tag{2.10}
\]

by Theorem 1.2.  A physical chain or opened cycle containing (e) spines
has (e-1) joins, each identifying exactly the (q-1) singleton letters
of a suffix and a prefix.  Summed over all physical components, the number
of joins is (N\bar R_q-c_q).  Subtracting
((q-1)(N\bar R_q-c_q)) from (2.10) gives (2.8).

Every balanced weak component contains at least one occupied normalized
port type, so there are at most (T_q) such components.  Equations
(2.6)--(2.7) and \(\gcd(N,\Delta_C)\le N\) give (2.9). \(\square\)

The same formula remains valid if one opens every lifted Euler cycle and
writes it linearly: (c_q) counts exactly the opened components.  Every
banked \(S_R\) is a nonzero literal one-letter word, so the reordering
does not weaken the empty-active-intersection witnesses.  No cross-factor
identification is used.

### Corollary 2.2 (the exact growing-depth internal gate)

Let \(h=h(m)\to\infty\), (h\le H), and suppose the charged owner
segments of all selected runs with (h\le q\le H) are pairwise disjoint
globally, including across depths.  Then

\[
 N\sum_{q=h}^{H}\bar R_q
 \le {W\over h+2},                               \tag{2.11}
\]

because every nonempty run has at least (q+2\) owner positions.  Also

\[
 N\sum_{q=h}^{H}(q-1)T_q
 \le H^2N^{H-1}=\exp(o_A(m))=o_A(W).             \tag{2.12}
\]

Consequently the coarse-port internal charts have total excess (o_A(W))
if

\[
 \boxed{\sum_{q=h}^{H}(q-1)D_q=o_A(B).}          \tag{2.13}
\]

Conversely, (2.7)--(2.8) show that (2.13) is necessary for this directed
trail architecture up to the already (o(W)) marker and balanced-catalog
terms.

The fixed-fibre packing ledger supplies no estimate of (D_q).  In
particular a directed multigraph with two port types and all
\(\bar R_q\) edges pointing from the first to the second has
(D_q=\bar R_q\), even though its type catalog has size two.  At
\(\bar R_q=\Theta(B/q)), (2.8) is then critical.  Thus the
subexponential catalog alone proves no (o(W)) fusion theorem.

## 3. Reversal does not erase port imbalance

Reversing a literal chart preserves its internal target family, so one
might hope to orient every run so that (G_q) becomes balanced.  There is
an exact obstruction to that inference.

Let (J) be the involution on normalized port types induced by reversing
an ordered port.  For a forward run edge (a_R\to b_R), put

\[
 z_R=e_{a_R}-e_{b_R}.                            \tag{3.1}
\]

Forward orientation contributes (z_R) to the outdegree-minus-indegree
vector.  Reversing the chart contributes (-Jz_R).  Therefore

\[
 \Xi_q:=\sum_R(z_R-Jz_R)                         \tag{3.2}
\]

is independent of every choice of chart orientations: if (d) is the
resulting total imbalance vector, then

\[
 d-Jd=\Xi_q.                                     \tag{3.3}
\]

Since \(\sum_vd(v)=0\), its total positive imbalance is
(D(d)=\|d\|_1/2).  Hence

\[
 \boxed{D(d)\ge {1\over4}\|\Xi_q\|_1.}          \tag{3.4}
\]

For (q\ge3), (J) has no fixed normalized type.  Indeed, if a distinct
ordered port (P) satisfied

\[
 \operatorname {rev}(P)=\rho^cP,
\]

then reversing again would give (2c=0\pmod N).  Since (N) is odd,
(c=0), and the first and last entries of (P) would be equal, a
contradiction.

Thus \(\|\Xi_q\|_1=o(B/q)\) is a necessary condition for a
reversal-based proof of \(D_q=o(B/q)\), not a sufficient one: even
\(\Xi_q=0\) need not admit a balanced orientation.  No claim is made here
that the actual PBBS value of \(\Xi_q\) is critical.  Equation (3.4) is
the exact invariant which any reversal-based proof must beat.

## 4. Fine decorated ports are PBBS-rigid

The singleton arms in (1.8) deliberately omit (S).  That is why two
charts with different carriers can be superposed.  It is also why the
splice says nothing about a target whose original owner window crosses a
run boundary.

The minimal decorated ports at a natural owner-disjoint chronological
seam are

\[
 \widehat\Pi^-(R)
   =(S;\gamma_0,\ldots,\gamma_{q-2}),             \tag{4.1}
\]

\[
 \widehat\Pi^+(R)
   =(S;\gamma_{L+1},\ldots,\gamma_{L+q-1}).       \tag{4.2}
\]

A proposed chronological join \(R\to Q\) additionally requires that
\(X_0(Q)\) be the actual PBBS successor of \(X_L(R)\).  Under that
adjacency, equality
\[
 \widehat\Pi^+(R)=\rho^c\widehat\Pi^-(Q)
                                                               \tag{4.3}
\]
identifies the \(q-1\) coordinates retained across the Johnson edge; the
removed coordinate of \(X_L(R)\) and the added coordinate of \(X_0(Q)\)
complete the two adjacent \(q\)-queues.  The minimal ports (4.1)--(4.2)
do **not** determine either boundary owner.

For comparison, define the stronger full-owner ports

\[
 \Pi^-_{\rm full}(R)
   =(S;\gamma_0,\ldots,\gamma_{q-1}),             \tag{4.3a}
\]

\[
 \Pi^+_{\rm full}(R)
   =(S;\gamma_L,\ldots,\gamma_{L+q-1}).           \tag{4.3b}
\]

Their associated boundary owners are \(X_0\) and \(X_L\), respectively.
They encode an owner-overlap/artificial-cut seam, not the natural
owner-disjoint seam in (4.3).

### Lemma 4.1 (free phase action on PBBS boundary owners)

Every rank-(m) or rank-((m+1)) owner has (N) distinct rotations.

#### Proof

If a nonzero rotation fixed a subset (X\subseteq\mathbb Z_N), then
(X) would be a union of cycles of some common length (d>1) dividing
(N), so (d\mid|X|).  But

\[
 \gcd(N,m)=\gcd(2m+1,m)=1,
 \qquad
 \gcd(N,m+1)=1.
\]

This is impossible. \(\square\)

### Lemma 4.2 (full-owner input-type injectivity)

Among proper maximal depth-(q) runs in one exact PBBS factor, normalized
full-owner decorated input ports are injective on quotient run occurrences.

#### Proof

If
\(\Pi^-_{\rm full}(R')=\rho^c\Pi^-_{\rm full}(R)\), then (4.3a) gives
(X_0(R')=\rho^cX_0(R)).  Rank-(m) owners occur exactly once in an exact
middle factor; rank-((m+1)) projected owners are their complements and
also occur exactly once.  After quotienting the free rotation action from
Lemma 4.1, the two boundary owners therefore give the same quotient owner
occurrence.  The deterministic PBBS successor path from that occurrence
fixes the ordered departure queue and the depth-(q) shadow.  Hence the
two purported run starts are the same occurrence. \(\square\)

For comparison, the entire decorated input-port universe has exactly

\[
 \boxed{
 {1\over N}\binom Nk (k)_q
 =B\,(k)_q}                                      \tag{4.4}
\]

quotient types: choose a rank-(k) owner, choose and order its (q)
active coordinates, and divide the free action by (N).  Here
\((k)_q=k(k-1)\cdots(k-q+1)\), and
\(\binom Nk=W=NB\) for \(k\in\{m,m+1\}\).  Thus there is no small
full-port catalog.  In complement rank (k=m+1), even the raw
carrier count is already of width scale:

\[
 {\binom N{m+1-q}\over\binom Nm}
 =\prod_{j=0}^{q-2}{m-j\over m+2+j}
 =\exp\!\left(-{q(q-1)\over m}+o_A(1)\right).    \tag{4.5}
\]

For (q/\sqrt m\to a\le A), the ratio tends to (e^{-a^2}), not zero.

### Theorem 4.3 (maximal-run chronological decorated-port obstruction)

Let \(R,Q\) be two chronologically oriented proper maximal depth-\(q\)
fixed-fibre runs.

1. Suppose that for one common phase shift \(c\),
   \[
      \rho^cX_0(Q)=\operatorname {succ}(X_L(R)),
      \qquad
      \widehat\Pi^+(R)=\rho^c\widehat\Pi^-(Q).    \tag{4.6}
   \]
   Then \(R,Q\) lie in one larger fixed-carrier extension run.

2. The same conclusion holds under the stronger owner-overlap condition
   \[
      \Pi^+_{\rm full}(R)
       =\rho^c\Pi^-_{\rm full}(Q).                \tag{4.7}
   \]

In particular, two distinct proper maximal runs admit neither a natural
chronological decorated seam of type (4.6) nor a full-owner artificial-cut
seam of type (4.7).

#### Proof

For (4.6), translate \(Q\) by \(c\) and write its token line as
\(\eta_0,\eta_1,\ldots\).  The seam identifies
\[
 (\gamma_{L+1},\ldots,\gamma_{L+q-1})
   =(\eta_0,\ldots,\eta_{q-2})                   \tag{4.8}
\]
under the same carrier \(S\).  Since the shifted owner
\(\rho^cX_0(Q)\) is the actual successor of \(X_L(R)\), that Johnson edge
removes \(\gamma_L\) and adds
\(\eta_{q-1}\).  Glue the two token lines along the common ordered
\(q-1\)-tuple in (4.8).

Every length-\(q\) token window of the glued line lies wholly in one old
line: the terminal window
\((\gamma_L,\ldots,\gamma_{L+q-1})\) belongs to \(R\), and the next
window \((\eta_0,\ldots,\eta_{q-1})\) belongs to \(Q\).  Every pair of
token positions at distance \(q\) is unequal.  This is Lemma 1.1 inside
either old line, and across the seam equality would make the corresponding
actual PBBS Johnson update lazy.  Hence all repeated labels in the glued
line are separated by at least \(q+1\).

It follows exactly as in Theorem 1.2 that every \(q+1\)-owner window
crossing the seam has intersection \(S\).  All intervening starts are
therefore good \(S\)-windows and all their adjacent pairs are
\(S\)-extensions.  Thus \(R,Q\) coalesce, contradicting distinct
maximality.

Under (4.7), the terminal and initial owners are identified and the token
lines overlap in \(q\) ordered coordinates.  Every glued \(q\)-window is
again contained in an old line, and the same nonlazy-update argument gives
the identical conclusion. \(\square\)

### Corollary 4.4 (no original-chronology decorated-port saving)

Let \(\bar R_q\) pairwise owner-disjoint proper maximal quotient runs be
given with their complete phase decks.  In the graph whose possible joins
are their **original PBBS chronological successor seams** satisfying
(4.6), there are no edges between distinct maximal runs.  Hence the
canonical chronology-preserving spine assembly leaves
\[
 N\bar R_q                                       \tag{4.9}
\]
separate physical spines and has the exact constructed spine-opening term
\[
 \boxed{(q-1)N\bar R_q.}                         \tag{4.10}
\]

If the declared construction also gives each run a private carrier marker,
its total opening toll is exactly
\[
 Nq\bar R_q.                                     \tag{4.11}
\]
Carrier markers with equal set value may instead be deduplicated, so
(4.11) is not an optimal-word lower bound.  The spine term (4.10) is the
part left by the absence of chronological port joins; at
\(\bar R_q=\Theta(B/q)\) it is already \(\Theta(W)\).

Nonconsecutive runs may still have equal minimal decorated ports and may
be regrouped.  Such a regrouping creates a new chronology and does not
preserve the original crossing windows.  Lemma 4.2 applies only to the
stronger full-owner port, not to the minimal ports (4.1)--(4.2).  A cyclic
all-extension component may also be cut artificially, but its pieces are
not distinct proper maximal runs.

## 5. Combination with the QCF boundary compiler

Partition the long quotient cycles into blocks of quotient length

\[
 H\ll b\le\ell<2b,
 \qquad b\log N=o(m).                            \tag{5.1}
\]

The exact QCF one-border theorem gives (4H-1) letters at every physical
block cut.  Charged once per shared all-phase block boundary, its total
cost is at most

\[
 N(4H-1)\left\lceil{B\over b}\right\rceil
 =O\!\left({WH\over b}\right)+\exp(o(m))
 =o_A(W).                                        \tag{5.2}
\]

Similarly, if a selected maximal run is declared long when
(r\ge\omega_mq), with \(\omega_m\to\infty\), its exact (q)-letter
opening is at most (r/\omega_m).  For a globally owner-disjoint family,
all long-run openings therefore total at most

\[
 {W\over\omega_m}=o(W).                          \tag{5.3}
\]

Equations (5.2)--(5.3) rigorously remove the outer block borders and the
long equal-shadow atoms.  The residual proper maximal runs have the exact
coarse internal ledger (2.8).  If they are all singleton maximal runs,
then (r=1), their owner baseline is (q+2), and the same formulas hold
with \(\bar R_q=\bar I_q\).  Nothing in the fixed-fibre ledger proves that
every residual short run is a singleton; intermediate runs must simply be
included as edges of the same port graph.

The remaining issue is crossing preservation.  Coarse-port trails reorder
the run charts and erase the original PBBS adjacencies.  Applying the
(4H-1) chart separately at every erased quotient seam would cost

\[
 N(4H-1)J,                                       \tag{5.4}
\]

where (J) is the number of such seams.  If
(J=\Theta(B/H)), (5.4) is \(\Theta(W)\).  At one depth (q\), even the
depth-(q) version (4q-1) costs \(\Theta(W)\) for
(J=\Theta(B/q)).  Thus the success of the outer-border theorem does not
authorize paying it at every isolated internal run.

On the other hand, retaining the actual old successor seam and its carrier
invokes Theorem 4.3 and eliminates every join between distinct maximal
runs.  Nonconsecutive decorated matches may exist, but they create a new
chronology and return to the crossing-support problem.  This is the exact
coarse/fine dichotomy:

\[
 \begin{array}{c|c|c}
 \text{port data}&\text{automatic structure}&\text{targets preserved}\\ \hline
 \text{singleton }(q-1)\text{-port}
   &\exp(o(m))&\text{run-internal only}\\
 \text{carrier + }(q-1)\text{-port + actual successor}
   &\text{no maximal-run seam}&\text{original FIFO crossing}\\
 \text{carrier + full }q\text{-owner port}
   &\text{injective on PBBS starts}&\text{owner-overlap seam}
 \end{array}                                      \tag{5.5}
\]

## 6. Exact conditional baseline-relative compiler and the surviving gate

The preceding identities give a sharp conditional theorem without hiding
any opening term.

### Theorem 6.1 (coarse-port block criterion)

Assume the following for the residual run family of a complete all-phase
block decomposition.

1. All charged owner segments used in the construction, including long
   atoms and residual runs and including comparisons between those two
   classes, are pairwise disjoint.  The minimum
   residual depth \(h(m)\) tends to infinity.  The very same run-chart
   word whose declared length is \(M\) plus the opening terms in
   (2.8) and (5.3) simultaneously gives contiguous literal OR witnesses
   for \(M\) distinct assigned rank-\(m\) middle owners.  Equivalently,
   one may substitute—rather than append—a separately proved combined
   replacement word of that same total length which covers both those
   \(M\) owners and all run-internal targets.  A complement-projected
   rank-\((m+1)\) row is not charged against the middle baseline merely
   by complementation or cardinality.
2. The normalized singleton-port imbalance satisfies
   \[
      \sum_{q=h}^{H}(q-1)D_q=o_A(B).              \tag{6.1}
   \]
3. Let \(\mathcal X\) be the set of distinct required target sets through
   depth (H) not internal to a long atom or residual run and not covered
   by the outer QCF charts.  Then
   \[
      |\mathcal X|=o_A(W).                        \tag{6.2}
   \]
4. Every excluded bounded-depth and short-cycle sector has a literal
   repair of total size (o_A(W)).

Then one exact PBBS factor has a literal word of length

\[
 W+o_A(W)                                        \tag{6.3}
\]

covering every assigned middle owner and every selected lower and upper
target through depth (H).

#### Proof

Use (5.3) on the long runs.  Apply Theorem 2.1 to all residual runs, append
every uncharged middle owner as one letter, and use (2.11)--(2.13).  The
result has length (W+o(W)) and covers all internal targets.  Add the
outer charts from (5.2), the assumed bounded-depth/short-cycle repair, and
one literal letter for each nonempty target in \(\mathcal X\).  Assumptions
(6.1)--(6.2) make every added term (o(W)).  All pieces come from the same
exact factor and every witness is a literal contiguous OR. \(\square\)

Theorem 6.1 is not unconditional.  The fixed-fibre extension ledger proves
neither (6.1) nor (6.2), and Theorem 4.3 shows that replacing the coarse
ports by chronology-bearing ports cannot prove them: that refinement has
no edges between distinct maximal runs.

Thus the exact coefficient-one boundary is now:

\[
 \boxed{
 \text{coarse port imbalance }\sum_q (q-1)D_q
 \quad+\quad
 \text{distinct crossing support }|\mathcal X|.} \tag{6.4}
\]

The catalog and all-phase opening terms are already (o(W)).  What remains
must be a genuinely nonlocal PBBS crossing braid or an independent theorem
that both quantities in (6.4) are (o(W)).  Generic normalized-type
pigeonholing cannot supply either statement.

## 7. Audit corrections and implication scope

1. The source fixed-fibre ledger states its support and packing formulas
   without a cyclic-wrap qualification.  On a cyclic owner component with
   (E) edges, a run of (r) extension starts has support
   \[
      \min(E,r+q),
   \]
   not always (r+q).  For (q+1\le E), its exact cyclic interval-packing
   number is
   \[
      \min\!\left(
       \left\lceil{r\over q+1}\right\rceil,
       \left\lfloor{E\over q+1}\right\rfloor
      \right).
   \]
   Theorems 1.2--6.1 use only proper nonwrapping runs.  Singleton runs on
   long cycles satisfy the displayed source formulas exactly; a cyclic
   all-extension component is a long correlated atom, not a residual
   isolated run.

2. On a cyclic binary extension indicator with (C_q) ones and (R_q)
   nonempty one-runs,
   \[
      R_q\le\min(C_q,E-C_q)\quad(0<C_q<E),
   \]
   while (C_q=E) gives one cyclic run.  This confirms that isolated runs
   can remain at the critical scale; it does not prove that canonical PBBS
   realizes that scale.

3. Formula (2.7) is exact for a chosen deckwise-uniform quotient trail and
   Euler routing.  If phase-dependent routings are permitted in a branching
   balanced voltage graph, the minimum lifted cycle count is the index of
   the subgroup generated by all closed-walk voltages, not necessarily the
   gcd of one chosen Euler voltage.  This can only reduce the already
   (o(W)) balanced-catalog term and does not alter the imbalance term
   (ND_q) or the full-port obstruction.

4. Theorem 4.3 is PBBS-specific: it uses exact owner uniqueness, the
   deterministic PBBS successor, and the nonlazy Johnson updates.  The
   suspension example from the fixed-fibre ledger is not promoted to a
   canonical PBBS counterexample.

5. The obstruction is architectural.  It rules out the inference
   "normalize ports, group equal types, and restore each lost seam by the
   existing QCF border chart."  It does not rule out an interleaved word
   which represents many crossing targets with shared letters and does not
   expose any individual decorated FIFO seam.

6. No complement target is treated as an OR witness.  No fractional
   ownership, cross-factor synchronization, or labelled common-owner
   relaxation is used.  All quantitative claims remain inside one exact
   PBBS factor.

## 8. Final proved/conditional boundary

The theorem-level advance is the exact sandwich/trail identity

\[
 L_q-M_q=N\bar R_q+(q-1)c_q,
\]

the reversal invariant

\[
 D_q\ge\frac14\|\Xi_q\|_1,
\]

and the PBBS maximal-run rigidity theorem saying that the minimal
carrier-decorated port admits no join between distinct maximal runs at an
actual original successor seam; the stronger full-owner port is injective
on PBBS starts.

Therefore all-phase normalization removes the type-catalog cost but does
**not** finish the PBBS block compiler.  Coarse ports leave the two exact
unproved quantities in (6.4); chronology-preserving decorated spines have
the exact linear-scale constructed opening term (4.10).  A coefficient-one conclusion requires a new
nonlocal crossing-window braid or new PBBS estimates proving (6.1)--(6.2).
