# Lane S: twisted port factors, exact two-slab composition, and the mirror quota ledger

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, finite search, or web
input is used.

## Authoritative geodesic correction

Every nonidentity twisted factor discussed below is only an abstract open
path ledger unless a separate exterior-moving ambient packet is supplied.
It is not a legal substitution in an ordinary fixed-exterior minimum
wreath slab.

Indeed, for a local \(2s\)-set \(J\), fixed exterior \(O\), and port
\(P\), the proposed twisted endpoints have distance

\[
 d_J\bigl(O\cup P,\,
          O\cup(J\setminus\tau(P))\bigr)
                         =|P\cap\tau(P)|.
\]

An \(s\)-step contiguous segment of a minimum wreath is geodesic, so the
right side must be \(s\). Hence \(\tau(P)=P\) for every row. If the
exterior changes from \(O_L\) to \(O_R\), then the necessary equation is

\[
 |O_L\setminus O_R|=|P\setminus\tau(P)|.
\]

The full exterior lower-state, upper-colour, and crossing-collar ledgers
must then be rebuilt. A later inverse monodromy does not repair a
nongeodesic first slab. Accordingly, the composition laws in this report
are algebraic laws for abstract ledgers, or conditional laws for a future
literal exterior-moving construction; none is a positive fixed-exterior
packet theorem. The exact mixed-phase filter and its application to the
ballot \(C_8\) and \(C_6\) banks are proved in
MATH_ATTACK_S_BALLOT_CYCLE_EXTERIOR_GEODESIC_FILTER_20260726.md.

## 0. Outcome

Let \(J=[2s]\), let

\[
 \mathcal X=\binom Js,\qquad
 \mathcal Y=\binom J{s+1},\qquad
 \mathcal D=\mathcal D_s,\qquad
 N=\operatorname{Cat}_s,
\]

and write \(\bar P=J\setminus P\).

At the abstract local path-ledger level, the zero-monodromy requirement
can be relaxed coherently. A twisted factor
with monodromy \(\tau\in\operatorname{Sym}(\mathcal D)\) is a spanning
path factor whose row rooted at \(P\) ends at
\(\overline{\tau(P)}\). Such a factor is an exact integral partition of all
local \(X/Y\) resources, although its row lengths need not be equal and its
individual rows need not be minimum complement geodesics.

This note proves:

1. Two exactly aligned twisted slabs with monodromies \(\tau\) and
   \(\sigma\) have composite monodromy

   \[
                         \sigma\circ\tau.               \tag{0.1}
   \]

   With an explicitly realized interface chart \(\rho\), the exact formula
   is

   \[
                 \rho^{-1}\circ\sigma\circ\rho\circ\tau. \tag{0.2}
   \]

2. Identity row closure requires inverse monodromy, but that is not enough.
   A two-slab fixed-length alignment also requires an exact rowwise length
   equation, and a nonidentity interface chart requires a literal connector
   with its own complete state and OR ledger.
3. Raw path reversal supplies the algebraic inverse as an
   opposite-polarity factor. A same-polarity \(\mathcal D\)-rooted mirror
   obtained by coordinate reflection has conjugate-inverse monodromy.
4. The mirror first-insertion histogram is the reflected **last-deletion**
   histogram of the original factor. Inverse monodromy therefore neither
   preserves nor cancels a first-edge quota gain automatically.
5. The clean rank-three balanced prefix obstruction from
   MATH_ATTACK_S_BALANCED_FIRST_EDGE_COMPLETION_THEOREM_AND_CUT_20260726.md
   is not rescued: it fails an unlabelled singleton degree cut before any
   endpoint permutation is chosen.
6. A different, already explicit rank-three wrong-monodromy path factor is
   an abstract cap-balanced twist atom. Its reflected mirror has the
   canonical first-edge histogram, so it does not undo the first slab's
   histogram change. It nevertheless fails the fixed-length and direct-seam
   tests, so it is not yet a legal two-slab substitution.

Thus twisted composition is an exact algebraic ledger, but it gives no
physical nonidentity slab. A surviving construction would have to be one
jointly geodesic exterior-moving packet with both boundaries and every
collar exposed; a bi-boundary inverse permutation by itself is
insufficient.

## 1. Twisted path factors

### Definition 1.1

A **twisted middle-levels path factor** of monodromy
\(\tau\in\operatorname{Sym}(\mathcal D)\) is a vertex partition of
\(M(J)\) into paths

\[
 K_P:\quad
 P=X_0^P\subset Y_0^P\supset X_1^P\subset\cdots\subset
 Y_{q_P-1}^P\supset X_{q_P}^P=\overline{\tau(P)},
 \qquad P\in\mathcal D.                               \tag{1.1}
\]

The integer \(q_P\) is the number of upper vertices, or Johnson exchanges,
in row \(P\).

The paths own every member of \(\mathcal X\) and every member of
\(\mathcal Y\) exactly once. Consequently

\[
 \sum_{P\in\mathcal D}q_P=|\mathcal Y|=sN,
 \qquad
 \sum_{P\in\mathcal D}(q_P+1)=|\mathcal X|=(s+1)N.    \tag{1.2}
\]

Equation (1.2) fixes only the average

\[
                         \frac1N\sum_Pq_P=s.           \tag{1.3}
\]

It does not imply \(q_P=s\) rowwise. Call a twisted factor **strict** when
\(q_P=s\) for every root.

### Proposition 1.2 (local-graph open traces and orbit cycles)

Every twisted factor gives a literal partition inside the abstract local
odd graph into open traces. Adding the complement seam edges joins those
traces into cycles indexed by the orbits of \(\tau\). This is not an
ambient fixed-exterior wreath realization.

#### Proof

For every upper state in (1.1), put

\[
                    Z_t^P=\{\infty\}\cup(J\setminus Y_t^P). \tag{1.4}
\]

Then

\[
 P,Z_0^P,X_1^P,Z_1^P,\ldots,
 Z_{q_P-1}^P,\overline{\tau(P)}                       \tag{1.5}
\]

is a literal odd-graph path: each \(Z_t^P\) is disjoint from its two
neighbouring \(X\)-states. Exact \(X\)-ownership covers every odd-graph
vertex avoiding \(\infty\), while the bijection

\[
                 Y\longleftrightarrow
                 \{\infty\}\cup(J\setminus Y)          \tag{1.6}
\]

shows that exact \(Y\)-ownership covers every vertex containing
\(\infty\).

For every \(Q\in\mathcal D\), add the literal complement edge

\[
                            \bar Q-Q.                   \tag{1.7}
\]

The path ending at \(\overline{\tau(P)}\) now continues into the path
rooted at \(\tau(P)\). Thus a \(\tau\)-orbit \(O\) gives one cycle of
length

\[
                         \sum_{P\in O}(2q_P+1).         \tag{1.8}
\]

All vertices have degree two and are used once. \(\square\)

For \(\tau=\mathrm{id}\) and \(q_P=s\), (1.8) recovers the ordinary
minimum \((2s+1)\)-wreaths. A nonidentity twist is still an integral
literal odd-graph two-factor, but its cycles may contain several root
ports and have unequal lengths. This distinction is essential at an
external port interface.

## 2. Exact two-slab composition

Let \(F\) and \(G\) be twisted factors on two physical slab copies, with
monodromies \(\tau\) and \(\sigma\). Their internal resource copies are
assumed disjoint.

An **exact direct alignment** consists of the following data.

1. For every \(Q\in\mathcal D\), the exit port \(\bar Q\) of the first slab
   is joined to the entrance port \(Q\) of the second by the fixed literal
   complement seam.
2. The \(N\) seam packets are pairwise resource-disjoint.
3. Every port and collar cell has one stated owner; no endpoint cell is
   silently identified or counted twice.
4. Every crossing collar state and every crossing OR colour is included in
   one stated seam ledger, and that ledger is exhausted exactly once.

These hypotheses are physical. An abstract relabelling of row names is not
an alignment theorem.

### Theorem 2.1 (direct two-slab composition)

Under an exact direct alignment, the concatenated open traces form an
integral partition of the two slab resource sets together with the seam
ledger. Its
monodromy is

\[
                         \boxed{\sigma\circ\tau}.       \tag{2.1}
\]

The row entering at \(P\) has composite semilength

\[
                         q_F(P)+q_G(\tau(P)).           \tag{2.2}
\]

Here semilength counts the upper \(Y\)-resources in the two slabs; the
single complement seam edge is part of the separate seam ledger.

It has identity outer row closure if and only if

\[
                         \boxed{\sigma=\tau^{-1}}.      \tag{2.3}
\]

If the two slab slots together require the fixed semilength \(2s\), exact
row alignment further requires

\[
 \boxed{
 q_F(P)+q_G(\tau(P))=2s
 \quad(P\in\mathcal D).}                               \tag{2.4}
\]

In particular, (2.4) is automatic for two strict factors and does not
follow from the aggregate identities (1.2).

#### Proof

The row \(K_P^F\) exits with label \(\tau(P)\), so the direct seam enters
the unique row \(K_{\tau(P)}^G\). That row exits with label
\(\sigma(\tau(P))\), proving (2.1) and (2.2).

Both factors partition their internal resources. Since \(\tau\) is a
permutation, every row of \(G\) is entered once. The exact seam hypotheses
use every interface resource once and do not duplicate any physically
shared collar cell. Hence the concatenated rows partition the complete
two-slab resource-and-seam ledger.

The outer terminal label equals the initial label for every \(P\) exactly
when \(\sigma\tau=\mathrm{id}\), proving (2.3). A fixed two-slab slot has
the required row length exactly when (2.4) holds. \(\square\)

If permutations act on the right, the same physical order is written
\(P\mapsto P\tau\sigma\). The functional composite in (2.1), rather than
the typography, is authoritative.

### Theorem 2.2 (composition through an interface chart)

Suppose a physically realized interface chart

\[
                         \rho:\mathcal D\longrightarrow\mathcal D \tag{2.5}
\]

sends first-slab output label \(Q\) to second-slab input label \(\rho(Q)\),
and the inverse chart is applied at the far boundary of the second slab.
Let

\[
 c_\rho(Q)\ge0,\qquad d_{\rho^{-1}}(R)\ge0             \tag{2.5a}
\]

be the numbers of upper-phase resources in the literal entrance connector
from \(\bar Q\) to the \(\rho(Q)\)-port and in the far-boundary inverse
connector leaving output label \(R\), respectively. A genuine zero-cost
coordinate-frame re-embedding has \(c_\rho=d_{\rho^{-1}}=0\); an inserted
connector network generally does not.
Then the composite monodromy is

\[
 \boxed{
 \rho^{-1}\circ\sigma\circ\rho\circ\tau.}              \tag{2.6}
\]

Identity closure is equivalent to

\[
 \boxed{\sigma=\rho\circ\tau^{-1}\circ\rho^{-1}},      \tag{2.7}
\]

and a prescribed total row semilength \(L\) has the exact condition

\[
 \boxed{
 \begin{aligned}
 q_F(P)&+c_\rho(\tau(P))+q_G(\rho(\tau(P)))\\
 &+d_{\rho^{-1}}(\sigma(\rho(\tau(P))))=L
 \qquad(P\in\mathcal D).
 \end{aligned}}                                       \tag{2.8}
\]

#### Proof

The successive labels are

\[
 P\longmapsto\tau(P)\longmapsto
 \rho(\tau(P))\longmapsto
 \sigma(\rho(\tau(P)))\longmapsto
 \rho^{-1}(\sigma(\rho(\tau(P)))).                     \tag{2.9}
\]

This proves the monodromy formula. The four summands in (2.8) are,
respectively, the first slab, entrance chart, second slab, and exit chart,
so their sum is the literal row semilength. Exact resource ownership follows as in
Theorem 2.1, provided the chart and its crossing collars are literal parts
of the seam ledger. \(\square\)

### Proposition 2.3 (a row chart is not free)

Inside the bare local odd graph, a direct seam edge from \(\bar Q\) to a
root \(R\in\mathcal D\) exists if and only if \(R=Q\).

#### Proof

Both states are \(s\)-subsets of \(J\). They are odd-graph adjacent exactly
when \(\bar Q\cap R=\varnothing\), equivalently \(R\subseteq Q\). Equal
cardinalities force \(R=Q\). \(\square\)

Thus a nonidentity \(\rho\) in Theorem 2.2 requires a genuine connector
network; changing row labels on paper does not preserve literal
realizability.

## 3. Raw reversal and the same-polarity mirror

### Proposition 3.1 (opposite-polarity inverse)

Reverse every path of a \(\tau\)-twisted factor. For \(Q\in\mathcal D\),
the reversed row

\[
                    \operatorname{rev}K_{\tau^{-1}(Q)} \tag{3.1}
\]

runs from \(\bar Q\) to \(\tau^{-1}(Q)\). Hence raw reversal is an exact
\(\overline{\mathcal D}\)-to-\(\mathcal D\) factor with inverse monodromy.
It partitions the same abstract \(X/Y\) resource sets; on a disjoint copied
slab it gives an integral opposite-polarity inverse.

If it follows \(F\) through its natural direct interface, row \(P\) has
two-slab semilength

\[
                              2q_F(P).                  \tag{3.2}
\]

Consequently raw reversal is fixed-length aligned exactly when \(F\) is
strict.

#### Proof

The endpoint statement follows by reversing
\[
 \tau^{-1}(Q)\leadsto
 \overline{\tau(\tau^{-1}(Q))}=\bar Q.
\]
Reversal preserves every vertex and edge. The first slab row \(P\) enters
the reverse of that same row, so the lengths add as in (3.2). \(\square\)

Raw reversal has the correct algebraic polarity, but the second slab is not
\(\mathcal D\)-rooted. Set complementation cannot normalize it inside
\(M(J)\): it sends an upper \((s+1)\)-set to an \((s-1)\)-set and destroys
the \(Y\)-shore.

For a same-polarity mirror, let \(g\) be a coordinate permutation of \(J\)
such that

\[
                         g(\overline{\mathcal D})=\mathcal D, \tag{3.3}
\]

and define the induced port permutation

\[
                         \alpha(P)=g(\bar P).           \tag{3.4}
\]

Since coordinate permutations commute with complement,
\[
                         g(P)=\overline{\alpha(P)}.     \tag{3.5}
\]

### Theorem 3.2 (same-polarity mirror)

Reverse every row of \(F\) and apply \(g\) coordinatewise. The resulting
factor \(M_gF\) is an exact \(\mathcal D\)-rooted twisted factor of
monodromy

\[
 \boxed{
             \tau_{M_gF}=\alpha\circ\tau^{-1}\circ\alpha^{-1}.} \tag{3.6}
\]

All \(X/Y\) vertices are still used exactly once.

#### Proof

The mirrored row associated with the original root \(P\) starts at

\[
                 g(\overline{\tau(P)})=\alpha(\tau(P)) \tag{3.7}
\]

and ends at

\[
                         g(P)=\overline{\alpha(P)}.     \tag{3.8}
\]

Put \(Q=\alpha(\tau(P))\). Then
\(P=\tau^{-1}(\alpha^{-1}(Q))\), so (3.8) equals

\[
 \overline{\alpha(\tau^{-1}(\alpha^{-1}(Q)))}.
\]

This is (3.6). Reversal preserves the two vertex multisets and \(g\) is an
automorphism of the inclusion graph, proving exact ownership. \(\square\)

For the standard order reflection

\[
                         R(i)=2s+1-i,                  \tag{3.9}
\]

the map

\[
                         \iota(P)=R(\bar P)             \tag{3.10}
\]

is the reverse-complement involution of Dyck words. Indeed, if
\(H_P(k)\) is the Dyck height, then

\[
                         H_{\iota(P)}(k)=H_P(2s-k)\ge0. \tag{3.11}
\]

Thus the standard mirror has monodromy

\[
                         \iota\tau^{-1}\iota.           \tag{3.12}
\]

Through the direct same-frame seam it cancels \(\tau\) if and only if

\[
                         [\tau,\iota]=1.                \tag{3.13}
\]

Through the interface chart \(\rho=\iota\), Theorem 2.2 turns (3.12) into
an inverse for every \(\tau\), but Proposition 2.3 shows that the chart
needs either a genuine frame re-embedding or a physical connector, whose
resource and length terms must be included in (2.8).

## 4. Exact boundary-histogram transformation

For a row of \(F\), write

\[
 X_t=X_{t-1}-a_t(P)+b_t(P),
 \qquad 1\le t\le q_P.                                \tag{4.1}
\]

Define the four boundary histograms

\[
\begin{aligned}
 \mathrm{FI}_F(j)&=\#\{P:b_1(P)=j\},&
 \mathrm{FD}_F(j)&=\#\{P:a_1(P)=j\},\\
 \mathrm{LI}_F(j)&=\#\{P:b_{q_P}(P)=j\},&
 \mathrm{LD}_F(j)&=\#\{P:a_{q_P}(P)=j\}.
\end{aligned}                                         \tag{4.2}
\]

Here FI is first insertion, FD first deletion, LI last insertion, and LD
last deletion.

### Theorem 4.1 (mirror boundary ledger)

The same-polarity mirror satisfies

\[
\boxed{
\begin{aligned}
 \mathrm{FI}_{M_gF}&=g_*\mathrm{LD}_F,&
 \mathrm{FD}_{M_gF}&=g_*\mathrm{LI}_F,\\
 \mathrm{LI}_{M_gF}&=g_*\mathrm{FD}_F,&
 \mathrm{LD}_{M_gF}&=g_*\mathrm{FI}_F.
\end{aligned}}                                        \tag{4.3}
\]

Consequently, relative to a baseline factor \(F_0\),

\[
 \boxed{
 \Delta\mathrm{FI}_{M_gF}
   =g_*(\mathrm{LD}_F-\mathrm{LD}_{F_0}).}             \tag{4.4}
\]

A mirror retains a first-edge quota gain \(\Delta\mathrm{FI}\) exactly
when

\[
                         g_*\Delta\mathrm{LD}
                         =\Delta\mathrm{FI},            \tag{4.5}
\]

and cancels it exactly when the left side is
\(-\Delta\mathrm{FI}\). Neither relation follows from monodromy.

#### Proof

The mirrored row is

\[
 g(X_{q_P}),g(X_{q_P-1}),\ldots,g(X_0).                \tag{4.6}
\]

Its first inserted coordinate is
\[
 g(X_{q_P-1}\setminus X_{q_P})=g(a_{q_P}),
\]
and its first deleted coordinate is \(g(b_{q_P})\). The last mirrored
exchange similarly inserts \(g(a_1)\) and deletes \(g(b_1)\). Summing over
the rows proves (4.3)--(4.5). \(\square\)

### Proposition 4.2 (the only universal transition totals)

Let
\[
 d_j=\#\{P\in\mathcal D:j\in P\}.
\]
Every twisted factor, independently of \(\tau\), satisfies

\[
 \sum_{P}\sum_{t=1}^{q_P}\mathbf1_{\{b_t(P)=j\}}
      =N-d_j,                                         \tag{4.7}
\]

\[
 \sum_{P}\sum_{t=1}^{q_P}\mathbf1_{\{a_t(P)=j\}}
      =d_j.                                           \tag{4.8}
\]

These identities impose no equality between FI and LD.

#### Proof

The number of insertions of \(j\) is the number of upper states containing
\(j\), minus the number of pre-exchange lower states containing \(j\).
The pre-exchange lower states are all of \(\mathcal X\) except the terminal
set \(\overline{\mathcal D}\). Since

\[
 \binom{2s-1}{s}=\binom{2s-1}{s-1},                   \tag{4.9}
\]

the global upper and lower point counts agree. The terminal set contains
\(j\) on exactly \(N-d_j\) roots, proving (4.7).

Similarly, the post-exchange lower states are all of \(\mathcal X\) except
the initial set \(\mathcal D\), giving (4.8). \(\square\)

Thus a trade has zero total insertion and deletion deviation after summing
over all phases, but its first-insertion deviation can be transferred to
arbitrary later boundary phases. A one-sided quota theorem cannot predict
the mirror quota.

## 5. The rank-three prefix obstruction remains impossible

Consider the clean balanced first segments

\[
\begin{array}{c}
 123-1236-136,\qquad
 124-1246-146,\qquad
 125-1245-245,\\
 134-1234-234,\qquad
 135-1235-235.
\end{array}                                             \tag{5.1}
\]

Their first-insertion histogram is

\[
                         2e_2+e_4+2e_6,                \tag{5.2}
\]

the canonical sharp-cap histogram.

### Proposition 5.1

The prefix system (5.1) is not the first layer of any twisted factor, for
any \(\tau\in\operatorname{Sym}(\mathcal D_3)\).

#### Proof

Changing \(\tau\) changes only which member of the fixed terminal set
\(\overline{\mathcal D}_3\) is paired with each residual start. It does
not change a residual vertex demand.

The lower vertex \(126\) is neither a selected residual start nor a member
of \(\overline{\mathcal D}_3\), so its residual demand is two. Its three
upper neighbours are

\[
                         1236,\quad1246,\quad1256.      \tag{5.3}
\]

The first two are saturated first-upper resources in (5.1). Only
\(126-1256\) remains, so no residual degree factor exists. The singleton
cut is

\[
                              2\le1.                    \tag{5.4}
\]

This failure precedes monodromy and is independent of \(\tau\).
\(\square\)

## 6. A genuine rank-three twist atom and why it still does not align

There is a different spanning path factor:

\[
\begin{aligned}
 K_{123}={}&123-1236-136-1346-146-1246-126-1256-156-1456-456,\\
 K_{124}={}&124-1234-234-2346-236-2356-256,\\
 K_{125}={}&125-1235-235-2345-345-3456-346,\\
 K_{135}={}&135-1356-356,\\
 K_{134}={}&134-1345-145-1245-245-2456-246.
\end{aligned}                                          \tag{6.1}
\]

Its lower and upper states partition \(\mathcal X\) and \(\mathcal Y\).
Indeed, the lower states in (6.1) are

\[
\begin{gathered}
123,124,125,126,134,135,136,145,146,156,\\
234,235,236,245,246,256,345,346,356,456,
\end{gathered}                                         \tag{6.1a}
\]

and the upper states are

\[
\begin{gathered}
1234,1235,1236,1245,1246,1256,1345,1346,1356,1456,\\
2345,2346,2356,2456,3456.
\end{gathered}                                         \tag{6.1b}
\]

The entries in each list are distinct, and the counts are
\(\binom63=20\) and \(\binom64=15\).
Its monodromy is

\[
                         \tau=(124\ 134\ 135),          \tag{6.2}
\]

with \(123,125\) fixed, and its semilengths are

\[
\begin{array}{c|ccccc}
 P&123&124&125&134&135\\ \hline
 q_P&5&3&3&3&1.
\end{array}                                            \tag{6.3}
\]

The first-insertion and last-deletion histograms, read directly from
(6.1), are

\[
 \mathrm{FI}_F=2e_3+e_5+2e_6,                         \tag{6.4}
\]

\[
 \mathrm{LD}_F=2e_1+e_3+2e_5.                         \tag{6.5}
\]

Both have maximum two, the sharp rank-three coordinate cap.

Under order reflection \(R(i)=7-i\),

\[
                         R_*\mathrm{LD}_F
                         =2e_2+e_4+2e_6,               \tag{6.6}
\]

which is exactly the canonical rank-three first-edge histogram. Therefore,
relative to a canonical-canonical two-slab baseline, the reflected mirror
does **not** cancel the first slab's histogram change: the mirror contributes
zero additional change at this one-coordinate histogram. This is a real
positive boundary fact, but it is not a full carrier or crossing-collar
profile theorem.

It does not yet give a legal aligned inverse pair.

First, Proposition 1.2 gives single-factor orbit-cycle lengths

\[
                         11,\quad7,\quad17,             \tag{6.7}
\]

not five minimum \(7\)-cycles.

Second, the natural opposite-polarity inverse has two-slab row
semilengths

\[
                         2q_P=(10,6,6,6,2),             \tag{6.8}
\]

not the required constant \(2s=6\).

Third, for rank three the reverse-complement port involution is

\[
                         \iota=(125\ 134).              \tag{6.9}
\]

Hence the same-polarity reflected mirror has monodromy

\[
 \iota\tau^{-1}\iota=(124\ 135\ 125)\ne\tau^{-1}.      \tag{6.10}
\]

It does not cancel through the direct seam. A chart \(\rho=\iota\) would
repair the algebra, but Proposition 2.3 requires a nontrivial physical
connector for that chart.

In fact, no mirror chart can repair both the algebra and the row lengths.
Let a same-polarity mirror be normalized by an arbitrary admissible
coordinate permutation, with induced port permutation \(\alpha\). Its
monodromy is

\[
                         \mu=\alpha\tau^{-1}\alpha^{-1}. \tag{6.10a}
\]

Every chart \(\rho\) which makes this mirror an inverse has the form

\[
                         \rho=\alpha c,
 \qquad c\tau=\tau c.                                  \tag{6.10b}
\]

Indeed,

\[
 \rho^{-1}\mu\rho=\tau^{-1}
 \quad\Longleftrightarrow\quad
 c^{-1}\tau^{-1}c=\tau^{-1}.                           \tag{6.10c}
\]

Through this chart, first-slab row \(P\) enters the mirror of original row
\(c(P)\), because

\[
 \rho\tau(P)=\alpha c\tau(P)=\alpha\tau(c(P)).         \tag{6.10d}
\]

Thus fixed-length alignment would require

\[
                         q_F(P)+q_F(c(P))=6
 \quad(P\in\mathcal D_3).                              \tag{6.10e}
\]

But every element of the centralizer of
\(\tau=(124\ 134\ 135)\) preserves its fixed-root set
\(\{123,125\}\). On that set the two lengths are \(5\) and \(3\).
For \(P=123\), the left side of (6.10e) is therefore either \(10\) or
\(8\), never \(6\). Any literal connector adds a nonnegative length term,
so it cannot repair this excess. Hence **no coordinate-normalized mirror,
with any algebraically cancelling chart, supplies an aligned inverse for
this rank-three twist**.

Finally, a direct same-polarity inverse \(G\) satisfying both monodromy
and row-length alignment would need

\[
\begin{array}{c|ccccc}
 Q&123&124&125&134&135\\ \hline
 q_G(Q)&1&5&3&3&3,
\end{array}                                            \tag{6.11}
\]

because \(q_G(\tau(P))=6-q_F(P)\). No factor with this prescribed inverse
monodromy, length vector, full \(X/Y\) ledger, and compatible boundary
quota is constructed here.

## 7. Exact proved and open boundary

The following are proved.

1. Twisted factors are local-graph open-trace partitions and close
   abstractly into \(\tau\)-orbit cycles after complement seams; they are
   not fixed-exterior ambient wreath slabs.
2. Direct two-slab monodromy is \(\sigma\circ\tau\); charted monodromy is
   \(\rho^{-1}\sigma\rho\tau\).
3. Identity monodromy, exact seam ownership, and the rowwise length
   equation are three separate requirements.
4. Raw reversal supplies an opposite-polarity inverse. A normalized
   same-polarity mirror supplies the conjugate inverse
   \(\alpha\tau^{-1}\alpha^{-1}\).
5. Mirror quota is reflected last-deletion quota, not first-insertion
   quota.
6. The balanced rank-three prefix obstruction cannot be twisted because
   its degree Hall cut already fails.
7. The explicit rank-three wrong-monodromy factor is a genuine balanced
   twist and its reflected mirror does not undo its first-edge histogram
   change, but every mirror/chart pair fails fixed-length alignment by the
   centralizer obstruction (6.10a)--(6.10e).

The exact remaining positive target is therefore:

> Construct two twisted factors \(F,G\), an exact literal seam chart
> \(\rho\), and complete crossing-collar ledgers such that
> \[
> \rho^{-1}\sigma\rho\tau=\mathrm{id},\qquad
> q_F(P)+c_\rho(\tau P)+q_G(\rho\tau(P))
> +d_{\rho^{-1}}(\sigma\rho\tau(P))=2s
> \]
> for every root, while the sum of their full carrier-resolved boundary
> quota deviations has the required cap-reducing sign.

No theorem in this note constructs that bi-boundary inverse pair, and no
constant-one conclusion is claimed.
