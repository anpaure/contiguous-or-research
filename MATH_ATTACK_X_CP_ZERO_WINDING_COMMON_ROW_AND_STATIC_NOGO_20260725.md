# Lane X: zero-winding common-row aggregation and the static core-swap no-go

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web search is used.

## 0. Outcome

Put

\[
 N=2m+1,
 \qquad W=\binom{N}{m},
 \qquad B=\operatorname {Cat}_m=\frac WN,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where (A>0) is fixed and (m\to\infty).  This note keeps positive
winding completely separate.

There are two exact conclusions.

First, genuine zero-winding sectors have a stronger literal aggregation
property than an independently appended (O(H))-per-cut chart suggests.
Each sector of duration (s) has a two-parity word of length (3s+2).
In one orientation that word has the *same* ordered ((s-1))-letter word
as prefix and suffix.  Therefore every collection of sectors having the
same literal port can be superposed by exact suffix--prefix identification.
For a coherent family whose open one-step owner paths are pairwise
edge-disjoint, all packet-internal targets have one word of length

\[
 \boxed{
 \sum_{I}(2s(I)+1)+o_A(W)\le W+o_A(W).}
 \tag{0.1}
\]

The (o_A(W)) is uniform over the coherent family.  This is an integral,
literal, coefficient-one aggregation theorem for a substantial special
regime.  It does not assume a numerical (CP_A) bound.

There is a sharper boundary-crossing theorem when successive projected
half-sectors share one carrier and satisfy literal FIFO port matching.  A
chain of \(t\) duration-\(s\) blocks, with \(ts+1\) distinct owner-baseline
positions, has one word of exact length

\[
 ts+1+s.
 \tag{0.1a}
\]

This single word covers every consecutive union and intersection,
including windows crossing internal packet seams.  Hence \(c_s\) coherent
chains at height \(s\) cost exactly \(s c_s\) beyond their distinct owner
baseline; \(\sum_{s\le H}s c_s=O(HB)=o(W)\) would suffice.  This is the
precise positive common-row theorem.  What remains unproved is the
canonical-PBBS clustering needed to obtain so few fixed-carrier FIFO
chains.

Second, the static owner-wreath structure by itself cannot prove

\[
 \overline\nu_H=O_A(B/N).
 \tag{0.2}
\]

For (s=\lfloor a\sqrt m\rfloor), Catalan-positive many normalized
Kneser endpoint pairs satisfy the exact core-swap square and possess all
the advertised ambient-wreath completions.  Moreover, an explicit legal
Kneser recurrence has a core-swap return at every phase, at ordinary
trace density (1/(2s+1)).  These static objects need not be canonical
PBBS trajectories.  Their exact force is nevertheless decisive:

> no (1/N) saving can follow only from the Kneser recurrence, simple
> internal labels, two fixed cores, the endpoint square, or factorial
> ambient-completion multiplicity.

The actual equation relating the terminal edge to the prescribed PBBS
iterate, or an equivalent Dyck/carrier chronology, is indispensable.

There are two unresolved clauses before (0.1) can replace (CP_A) in the
global proof.

1. Standard (CP_A) packing gives disjoint projected step-two traces.  It
   does not automatically give disjoint *paired one-step owner rows*, the
   coherence hypothesis in (0.1).
2. Port superposition preserves every witness internal to a packet row,
   but does not create witnesses for owner windows crossing an external
   packet boundary.

Thus this report proves a real cross-cut/common-row aggregation theorem
and a sharp no-go for the proposed static counting route, but it does not
prove (CP_A), coefficient one, or any positive-winding estimate.

## 1. An exact ordered-run common-row theorem

The literal mechanism is most transparent in an abstract form.

Let

\[
 X_0,X_1,\ldots,X_{L-1}\subseteq\Omega
 \tag{1.1}
\]

be nonempty owner sets.  For every coordinate (x\in\Omega), decompose

\[
 \{j:x\in X_j\}
 \tag{1.2}
\]

into its maximal nonempty integer intervals.  Call these the positive
runs of (x).  For every distinct positive run (R=[\ell,r]), put

\[
 G_R=\{x:R\text{ is a maximal positive run of }x\}.
 \tag{1.3}
\]

Every (G_R) is nonempty by definition.  A coordinate with several
positive runs occurs in several of the letters (G_R); this repetition
is literal and intentional.

### Theorem 1.1 (ordered-run common row)

Suppose the distinct positive runs can be ordered

\[
 R_p=[\ell_p,r_p],\qquad 1\le p\le q,
 \tag{1.4}
\]

so that both sequences

\[
 \ell_1\le\ell_2\le\cdots\le\ell_q,
 \qquad
 r_1\le r_2\le\cdots\le r_q
 \tag{1.5}
\]

are nondecreasing.  Then the nonzero word

\[
 \boxed{G_{R_1},G_{R_2},\ldots,G_{R_q}}
 \tag{1.6}
\]

represents, as contiguous ORs,

* every owner (X_j);
* every consecutive union
  \(igcup_{j=a}^{b}X_j\); and
* every nonempty consecutive intersection
  \(igcap_{j=a}^{b}X_j\).

#### Proof

A run (R_p) contains (j) exactly when

\[
 \ell_p\le j,
 \qquad r_p\ge j.
\]

The first inequality selects a prefix of (1.6), the second a suffix.
Their intersection is one contiguous subword.  Its OR is exactly (X_j),
because every occurrence of a coordinate at (j) belongs to one unique
maximal positive run containing (j).

A run meets ([a,b]) exactly when

\[
 \ell_p\le b,
 \qquad r_p\ge a.
 \tag{1.7}
\]

Again these inequalities select a prefix and a suffix.  The resulting
contiguous subword contains (x) exactly when some positive run of (x)
meets ([a,b]), which is equivalent to

\[
 x\in\bigcup_{j=a}^{b}X_j.
\]

Finally, because ([a,b]) is connected, (x) belongs to every owner in
that interval exactly when one maximal positive run of (x) contains the
whole interval.  The conditions are

\[
 \ell_p\le a,
 \qquad r_p\ge b.
 \tag{1.8}
\]

They also select one contiguous subword, whose OR is the required
intersection.  If the intersection is nonempty, that subword is nonempty.
This proves the theorem. \(\square\)

The hypothesis is exact for this architecture.  If two indispensable
short positive runs have strictly inverted endpoints, no ordering can
make both endpoint sequences nondecreasing.  Thus nested/inverted run
pairs, rather than the number of requested targets, are the local
obstruction to one common row.

## 2. The exact zero-winding two-core word

Consider a genuine zero-winding PBBS return of odd one-step gap

\[
 2s+1<N,
 \qquad 1\le s<m.
 \tag{2.1}
\]

Write the omitted labels as

\[
 a_j=\lambda_{2j}\quad(0\le j\le s),
 \qquad
 b_j=\lambda_{2j+1}\quad(0\le j<s).
 \tag{2.2}
\]

The genuine zero-winding owner theorem gives the following facts.

* The (2s+1) labels
  \(a_0,b_0,a_1,b_1,\ldots,b_{s-1},a_s\) are pairwise distinct.
* There are disjoint cores (K,K'), each of size (m-s>0).
* With

  \[
   \Gamma=(\gamma_0,\ldots,\gamma_{2s})
   =(b_0,\ldots,b_{s-1},a_0,\ldots,a_s),
   \tag{2.3}
  \]

  and (V_j) the cyclic (s)-window of \(\Gamma\) beginning at (j),
  the two owner rows are

  \[
   E_j=K\cup V_j\quad(0\le j\le s),
   \tag{2.4}
  \]

  \[
   O_j=K'\cup V_{s+1+j}\quad(0\le j\le s),
   \tag{2.5}
  \]

  with indices reduced modulo (2s+1).

These conclusions use the actual zero-winding equality and do not follow
from (d(D)=1) alone.

Define the singleton blocks

\[
 \begin{aligned}
 \mathcal A&=(a_{s-1},a_{s-2},\ldots,a_0),\\
 \mathcal B&=(b_{s-1},b_{s-2},\ldots,b_0),\\
 \mathcal C&=(a_s,a_{s-1},\ldots,a_1),
 \end{aligned}
 \tag{2.6}
\]

where a ground label denotes its singleton set-letter.  Put

\[
 \boxed{
 \mathcal W_I=\mathcal A,\ K,\ \mathcal B,\ K',\ \mathcal C.}
 \tag{2.7}
\]

It has exact length

\[
 |\mathcal W_I|=3s+2.
 \tag{2.8}
\]

### Theorem 2.1 (two-core packet compiler)

The word (2.7) represents every set

\[
 \bigcap_{j=p}^{q}E_j,
 \quad
 \bigcup_{j=p}^{q}E_j,
 \quad
 \bigcap_{j=p}^{q}O_j,
 \quad
 \bigcup_{j=p}^{q}O_j,
 \qquad 0\le p\le q\le s.
 \tag{2.9}
\]

Every letter in (2.7) is nonzero.

#### Proof

For the (K)-row, cyclic-window arithmetic in the nonwrapping range
(0\le p\le q\le s) gives

\[
 \bigcap_{j=p}^{q}E_j
 =K\cup\{\gamma_q,\gamma_{q+1},\ldots,
                  \gamma_{p+s-1}\},
 \tag{2.10}
\]

where the active interval is empty for ((p,q)=(0,s)), and

\[
 \bigcup_{j=p}^{q}E_j
 =K\cup\{\gamma_p,\gamma_{p+1},\ldots,
                  \gamma_{q+s-1}\}.
 \tag{2.11}
\]

The subword

\[
 \mathcal A,K,\mathcal B
 =\gamma_{2s-1},\ldots,\gamma_s,K,
  \gamma_{s-1},\ldots,\gamma_0
 \tag{2.12}
\]

lists the active labels in the required reverse order around (K).
The intervals with endpoints

\[
 (\gamma_{p+s-1},\gamma_q)
 \quad\text{and}\quad
 (\gamma_{q+s-1},\gamma_p)
\]

therefore realize (2.10) and (2.11), with (K) itself used when the
active interval is empty.

For the (K')-row,

\[
 V_{s+1+j}
 =\{\gamma_{s+1+j},\ldots,\gamma_{2s}\}
  \cup\{\gamma_0,\ldots,\gamma_{j-1}\}.
 \tag{2.13}
\]

Consequently

\[
 \begin{aligned}
 \bigcap_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{p-1}\}
       \cup\{\gamma_{s+1+q},\ldots,\gamma_{2s}\},\\
 \bigcup_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{q-1}\}
       \cup\{\gamma_{s+1+p},\ldots,\gamma_{2s}\}.
 \end{aligned}
 \tag{2.14}
\]

These are contiguous ORs in

\[
 \mathcal B,K',\mathcal C
 =\gamma_{s-1},\ldots,\gamma_0,K',
  \gamma_{2s},\ldots,\gamma_{s+1}.
 \tag{2.15}
\]

The cores are nonempty because (s<m), and the other letters are
singletons.  This proves the theorem. \(\square\)

The two half-words in (2.12) and (2.15) are instances of Theorem 1.1.
For example, after complement projection and a cyclic shift of the active
order, the positive-run list is

\[
 [0,0],[0,1],\ldots,[0,s],[1,s],\ldots,[s,s].
 \tag{2.16}
\]

The middle run carries the fixed core together with its central active
label.  Thus the local compiler is an exact common row, not an abstract
support count.

## 3. A same-port superposition theorem

The word (2.7) begins and ends with the identical ordered singleton word

\[
 \boxed{
 \mathcal P_I=(a_{s-1},a_{s-2},\ldots,a_1),}
 \tag{3.1}
\]

of length (s-1).  Indeed,

\[
 \mathcal A=(\mathcal P_I,a_0),
 \qquad
 \mathcal C=(a_s,\mathcal P_I).
 \tag{3.2}
\]

### Lemma 3.1 (exact loop-port overlap)

Let (I_1,\ldots,I_t) be duration-(s) genuine zero-winding packets
whose ordered ports (3.1) agree literally.  Identifying the terminal copy
of the common port in (\mathcal W_{I_j}) with the initial copy in
(\mathcal W_{I_{j+1}}) gives one nonzero literal word containing every
(\mathcal W_{I_j}) as a contiguous subword.  Its exact length is

\[
 \boxed{
 t(3s+2)-(t-1)(s-1)
 =t(2s+3)+s-1.}
 \tag{3.3}
\]

Thus, relative to (t(2s+1)) open one-step packet edges, its excess is

\[
 \boxed{2t+s-1.}
 \tag{3.4}
\]

#### Proof

The identified words are the same ordered singleton letters, so the
superposition is literal.  No core or active label is relabelled.  Each
packet word remains a contiguous subword, hence all witnesses from
Theorem 2.1 survive.  Subtracting (s-1) at each of the (t-1) joins
proves (3.3), and (3.4) is arithmetic. \(\square\)

Call a physical packet family **open-row coherent** when its open one-step
edge paths

\[
 e_i,e_{i+1},\ldots,e_{i+2s(I)}
 \tag{3.5}
\]

are pairwise edge-disjoint.  This is stronger than disjointness of the
projected step-two residence traces.

### Theorem 3.2 (coherent zero-winding aggregation)

For every fixed (A>0), let (H=\lceil A\sqrt m\rceil).  Uniformly over
all open-row coherent physical families \(\mathscr P\) of genuine
zero-winding packets with

\[
 1\le s(I)\le H,
 \tag{3.6}
\]

there is one nonzero literal word representing all packet-internal targets
in (2.9) and satisfying

\[
 \boxed{
 |\mathcal W(\mathscr P)|
 \le
 \sum_{I\in\mathscr P}(2s(I)+1)+o_A(W)
 \le W+o_A(W).}
 \tag{3.7}
\]

#### Proof

For every (s), group the packets by their literal port (3.1), and apply
Lemma 3.1 within each group.  Let

\[
 R=|\mathscr P|,
 \qquad
 E=\sum_{I\in\mathscr P}(2s(I)+1),
 \tag{3.8}
\]

and let (G_s) be the number of nonempty port groups of height (s).
Summing (3.4) gives the exact upper ledger

\[
 |\mathcal W(\mathscr P)|
 \le E+2R+\sum_{s=1}^{H}(s-1)G_s.
 \tag{3.9}
\]

Coherence gives

\[
 E\le W,
 \tag{3.10}
\]

because the physical factor has (W) one-step edges.

The labels in (3.1) are pairwise distinct, so

\[
 G_s\le (N)_{s-1}\le N^{s-1}.
 \tag{3.11}
\]

Consequently

\[
 \sum_{s=1}^{H}(s-1)G_s
 \le H^2N^H
 =\exp(O_A(\sqrt m\log m))
 =o_A(W).
 \tag{3.12}
\]

It remains to prove (R=o_A(W)) uniformly, since a height-one packet has
an empty port and receives no saving from (3.1).

Put

\[
 g=\lfloor m^{1/4}\rfloor.
 \tag{3.13}
\]

Every zero-winding duration equals the normalized Dyck height.  If
(F_m(g)) denotes the number of semilength-(m) Dyck roots of height at
most (g), then the complete spatial deck contains at most (NF_m(g))
physical starts of height at most (g).  Hence

\[
 R_{\rm low}\le NF_m(g).
 \tag{3.14}
\]

The path-graph formula and the largest-eigenvalue bound give

\[
 \begin{aligned}
 F_m(g)
 &=\frac2{g+2}\sum_{j=1}^{g+1}
   \sin^2\frac{\pi j}{g+2}
   \left(2\cos\frac{\pi j}{g+2}\right)^{2m}\\
 &\le
 4^m\exp\!\left(-\frac{\pi^2m}{(g+2)^2}\right).
 \end{aligned}
 \tag{3.15}
\]

Wallis' bounds give (W=\Theta(4^m/\sqrt m)).  Therefore

\[
 R_{\rm low}
 \le N4^m e^{-\Theta(\sqrt m)}
 =o(W).
 \tag{3.16}
\]

Every remaining packet has (s>g), and its open path in (3.5) uses at
least (2g+1) distinct edges.  Coherence and (3.10) give

\[
 R_{\rm high}\le\frac W{2g+1}=o(W).
 \tag{3.17}
\]

Thus (R=o(W)).  Substitution of (3.10), (3.12), and (3.16)--(3.17) into
(3.9) proves (3.7). \(\square\)

All asymptotic estimates in this proof are uniform over the chosen
coherent packet family.  No random choice, fractional owner assignment,
or labelled synchronization is used.

### Scope of Theorem 3.2

The theorem is stronger than independent packet concatenation but weaker
than the required global PBBS statement.

* A standard family counted by \(\overline\nu_H\) is disjoint in the
  complement-projected step-two edge set.  Opposite one-step parity rows
  can still cross, so (3.10) is not automatic.
* The word covers precisely the targets whose owner windows lie wholly in
  one of the two packet rows.  A target crossing from a packet to external
  baseline material is not covered merely because both pieces are covered
  separately.
* The owner immediately after the returned edge is outside the open word.
  Individual endpoint owners cost only (O(R)=o(W)) under coherence, but
  their full crossing collars do not.

These are literal-contiguity limitations, not missing scalar constants.

## 3A. A sharp common-carrier FIFO chain theorem

The external-boundary caveat disappears in a stronger, still genuinely
nontrivial, special regime.  The exact condition is persistence of one
carrier across a chain of sliding owner blocks.

Fix integers (s,t\ge1).  Let (C\ne\varnothing), and for
(0\le h\le t) let

\[
 P_h=(p_{h,0},p_{h,1},\ldots,p_{h,s-1})
 \tag{3A.1}
\]

be an ordered (s)-tuple of distinct coordinates.  Assume

\[
 C\cap P_h=\varnothing
 \quad(0\le h\le t),
 \qquad
 P_{h-1}\cap P_h=\varnothing
 \quad(1\le h\le t).
 \tag{3A.2}
\]

Nonadjacent tuples may reuse coordinates.  Define a row of (ts+1)
owners by

\[
 \boxed{
 Y_{(h-1)s+j}
 =C
  \cup\{p_{h-1,j},\ldots,p_{h-1,s-1}\}
  \cup\{p_{h,0},\ldots,p_{h,j-1}\},}
 \tag{3A.3}
\]

for (1\le h\le t) and (0\le j\le s).  The (j=s) owner of block
(h) is the (j=0) owner of block (h+1), so (3A.3) is unambiguous.
Every transition replaces exactly one coordinate.

### Theorem 3A.1 (common-carrier FIFO compiler)

The word

\[
 \boxed{
 \begin{aligned}
 \mathcal F={}&
 (C\cup\{p_{0,0}\}),\ldots,(C\cup\{p_{0,s-1}\}),\\
 & (C\cup\{p_{1,0}\}),\ldots,(C\cup\{p_{1,s-1}\}),\\
 &\hspace{28mm}\cdots\\
 & (C\cup\{p_{t,0}\}),\ldots,(C\cup\{p_{t,s-1}\}),\ C
 \end{aligned}}
 \tag{3A.4}
\]

represents every consecutive union and every consecutive intersection of
the entire owner row (3A.3).  It has exact length

\[
 \boxed{|\mathcal F|=(t+1)s+1.}
 \tag{3A.5}
\]

Since the owner baseline has (ts+1) positions, the exact excess is

\[
 \boxed{s,}
 \tag{3A.6}
\]

independent of the number (t) of blocks.

#### Proof

Concatenate the tuple occurrences into the token line

\[
 P_0P_1\cdots P_t.
 \tag{3A.7}
\]

Equation (3A.3) says that the owner at time (k) is (C) together with
the length-(s) token window beginning at (k).  Condition (3A.2)
ensures that each such window contains (s) distinct coordinates.

For owner times (u\le v), the union of the token windows is the token
interval

\[
 [u,v+s-1],
 \tag{3A.8}
\]

while their intersection is the token interval

\[
 [v,u+s-1]
 \tag{3A.9}
\]

when (v-u<s), and is empty when (v-u\ge s).  More exactly, a token
occurrence at line position \(z\) is present at the owner times

\[
 [z-s+1,z],
\]

clipped to the row.  Thus \(z\in[u,v+s-1]\) exactly when that occurrence's
positive run meets \([u,v]\), and \(z\in[v,u+s-1]\) exactly when it
contains \([u,v]\).  Equal labels in nonadjacent tuples occur at positions
separated by at least \(s+1\), so their positive runs have a missing owner
time between them.  They cannot hand off across a connected query interval
and create an extra intersection coordinate.

Every token occurrence in (3A.4) is enriched by the same carrier (C).
Thus the word interval corresponding to (3A.8) has OR equal to the desired
union, and the interval corresponding to (3A.9) has OR equal to the
desired intersection.  When (3A.9) is empty, the final one-letter word
(C) represents the intersection.  All letters are nonempty.  Counting
the ((t+1)s) enriched token letters and the final carrier gives (3A.5),
and subtraction of (ts+1) proves (3A.6). \(\square\)

### Exact PBBS specialization

One complement-projected half of a genuine zero-winding sector has
exactly the form (3A.3), with

\[
 \begin{aligned}
 P_0&=(a_0,a_1,\ldots,a_{s-1}),\\
 C&=K'\cup\{a_s\},\\
 P_1&=(b_0,b_1,\ldots,b_{s-1}).
 \end{aligned}
 \tag{3A.10}
\]

Indeed the (j)-th projected owner is

\[
 K'\cup\{a_j,\ldots,a_s\}
    \cup\{b_0,\ldots,b_{j-1}\},
 \tag{3A.11}
\]

which is (3A.3).  Therefore consecutive genuine sectors fit the compiler
of Theorem 3A.1 precisely when their boundary data have

* the same carrier (C), and
* literal ordered equality between the outgoing tuple of one block and
  the incoming tuple of the next.

Equality of the common boundary owner together with ordered port equality
forces equality of the residual carriers, so these are exact labelled
conditions, not merely cardinality conditions.

The FIFO order is also necessary for the one-letter-per-run architecture
of Theorem 1.1.  Suppose the \(s\) active coordinates at a common boundary
arrive in the order

\[
 q_0,q_1,\ldots,q_{s-1}
\]

and depart in the order

\[
 q_{\pi(0)},q_{\pi(1)},\ldots,q_{\pi(s-1)}.
\]

Their positive-run left endpoints increase with arrival rank and their
right endpoints increase with departure rank.  The two endpoint lists
admit one common order exactly when \(\pi\) is increasing, hence exactly
when \(\pi\) is the identity.  Every inversion gives a strictly nested
pair of indispensable runs and violates (1.5), provided the corresponding
full-run intersections are among the required targets.  The zero-winding
core-swap port has the correct FIFO order \(b_0,\ldots,b_{s-1}\); its
failure is the carrier change, not an endpoint inversion.

If (T_s) duration-(s) blocks form (c_s) owner-disjoint
common-carrier FIFO chains, Theorem 3A.1 gives

\[
 \boxed{
 \text{total word length}
 =\text{distinct owner baseline}+s c_s.}
 \tag{3A.12}
\]

Equivalently, a half-sector is a decorated directed port edge

\[
 (C;P\longrightarrow Q).
\]

Legal no-cut joins are directed trails inside one fixed-carrier port
multigraph.  The operation is to concatenate the matched token-group
strings under the common carrier and append one shared final \(C\) per
trail.  It is not a suffix--prefix overlap of standalone words, each of
which already ends in its own \(C\).  For a freely reorderable finite
multigraph, the minimum
number of trails in a weak component is

\[
 \max\!\left(
 1,\ \sum_v(d^+(v)-d^-(v))_+
 \right).
 \tag{3A.12a}
\]

Actual factor chronology may impose a stronger restriction.  In either
case the exact scalar target furnished by (3A.12) is

\[
 \sum_{s\le H}s\,c_s=o(W).
 \tag{3A.12b}
\]

Consequently, suppose all chains used over all \(1\le s\le H\) are
pairwise owner-disjoint globally, not merely within each fixed-height
class.  Then their combined distinct owner baseline is at most \(W\).  If
in addition

\[
 \sum_{s\le H}s c_s\le C H B
 \tag{3A.13}
\]

for a fixed constant (C), then

\[
 \text{total word length}
 \le W+CHB
 =W+O_A(W/\sqrt m)
 =W+o_A(W).
 \tag{3A.14}
\]

Unlike arbitrary packet trail regrouping, Theorem 3A.1 covers all owner
windows crossing the internal joins of a FIFO chain.  What is unproved is
the PBBS clustering assertion needed to obtain (3A.13).  The core-swap
identity alone does not preserve the carrier: between its two parity
halves it changes (K'\cup\{a_s\}) to (K\cup\{a_0\}).

There are two exact reasons that a carrier pigeonhole does not supply the
missing clustering.  First, the number of possible carriers of the size
in (3A.10) is

\[
 \binom{2m+1}{m-s+1}
 =W\prod_{j=0}^{s-2}\frac{m-j}{m+2+j}.
 \tag{3A.15}
\]

For \(s=A\sqrt m+O(1)\),

\[
 \prod_{j=0}^{s-2}\frac{m-j}{m+2+j}
 =\exp(-A^2+o_A(1)).
 \tag{3A.16}
\]

Thus the carrier menu is of width scale, not \(o(W/H)\) scale.  Second,
inside one exact core-swap sector the two natural carriers are

\[
 C_{\rm even}=K'\cup\{a_s\},
 \qquad
 C_{\rm odd}=K\cup\{a_0\}.
 \tag{3A.17}
\]

They are disjoint: the two cores are disjoint from one another and from
all active labels, and \(a_s\ne a_0\).  Hence the sector's internal active
port overlap can never itself be a common-carrier FIFO join.  It supports
the \(3s+2\) two-chart word of Section 2, not the sharper baseline-plus-
\(s\) chain word of Theorem 3A.1.

## 4. The exact full-port boundary

There is a second orientation of the two-core common row which exposes the
length-(s) ports

\[
 P_I=(a_0,a_1,\ldots,a_{s-1}),
 \qquad
 Q_I=(a_1,a_2,\ldots,a_s).
 \tag{4.1}
\]

It is obtained from the joint word

\[
 \begin{aligned}
 \mathcal J_I={}&
 \gamma_0,\ldots,\gamma_{s-1},
 K'\cup\{\gamma_s\},
 \gamma_{s+1},\ldots,\gamma_{2s},\\
 &K\cup\{\gamma_0\},
 \gamma_1,\ldots,\gamma_s,
 \end{aligned}
 \tag{4.2}
\]

where the active order is rotated so that

\[
 (\gamma_0,\ldots,\gamma_s)=(a_0,\ldots,a_s).
 \tag{4.3}
\]

The first (2s+1) letters in (4.2) are the ordered-run word for one
projected parity, the last (2s+1) letters are the word for the other,
and their common (s)-letter block is identified.  Thus

\[
 |\mathcal J_I|=3s+2.
 \tag{4.4}
\]

If (Q_I=P_J) literally, the two words overlap in (s) letters.  A
directed trail of (t) packets then has exact length

\[
 t(3s+2)-(t-1)s=t(2s+2)+s.
 \tag{4.5}
\]

More generally, let (h(I,J)) be the largest literal suffix--prefix
overlap between (Q_I) and (P_J), with (0\le h(I,J)\le s).  If (F)
is an acyclic directed path forest on (t) packets, concatenation gives

\[
 \boxed{
 \left|\mathcal J(F)\right|
 =t(3s+2)-\sum_{I\to J\in F}h(I,J).}
 \tag{4.6}
\]

If the forest has (p) paths, subtracting the formal paired-owner count
(t(2s+2)) gives the exact deficit ledger

\[
 \boxed{
 sp+\sum_{I\to J\in F}\bigl(s-h(I,J)\bigr).}
 \tag{4.7}
\]

Thus the weakest port-only statement capable of absorbing a critical
(st=\Theta(W)) family is not exact full-port equality.  It is a
near-perfect acyclic predecessor/successor matching with total overlap
deficit (o(W)).  A maximum-weight bipartite matching without a cycle
opening ledger is not enough.

Even exact full-port balance does not follow from the first seam.  Every
genuine zero-winding packet satisfies

\[
 a_1=a_0-1\pmod N.
 \tag{4.8}
\]

For any nonnegative weights on packets, average the rotations of a maximum
independent set of the odd cycle (C_N).  Some independent set (S)
contains at least

\[
 \frac{\lfloor N/2\rfloor}{N}
 \tag{4.9}
\]

of the total start-label weight.  Restrict to packets with (a_0\in S).
Their input ports start in (S), while by (4.8) their output ports start
outside (S).  Hence no physically oriented output port in this
subfamily equals a physically oriented input port in the same subfamily.

This rules out an automatic chronology-fixed full-port trail theorem.  It
does not rule out long partial overlaps (h=s-o(s)), reversal of complete
packet words, or a different global braid.

## 5. Exact factorial census: completion entropy is neutral

We now isolate why the ambient-wreath multiplicity gives no (CP_A)
saving.

Fix an oriented Kneser edge

\[
 A\mathbin{\dot\cup}B=[N]\setminus\{u\},
 \qquad |A|=|B|=m,
 \tag{5.1}
\]

and fix (1\le s<m).  Put (q=m-s).

Choose an ordered (s)-tuple

\[
 (b_0,\ldots,b_{s-1})
 \tag{5.2}
\]

of distinct members of (A), and an ordered (s)-tuple

\[
 (a_1,\ldots,a_s)
 \tag{5.3}
\]

of distinct members of (B).  Put (a_0=u),

\[
 K=A\setminus\{b_0,\ldots,b_{s-1}\},
 \qquad
 K'=B\setminus\{a_1,\ldots,a_s\}.
 \tag{5.4}
\]

The fixed-core formulas construct one legal simple open Kneser path with
omitted-label word

\[
 a_0,b_0,a_1,b_1,\ldots,b_{s-1},a_s,a_0.
 \tag{5.5}
\]

Conversely, every simple fixed-core path based at (5.1) has a unique
choice of (5.2)--(5.3).  Therefore the number of ordered open paths based
at (5.1) is exactly

\[
 \boxed{
 \left(\frac{m!}{(m-s)!}\right)^2.}
 \tag{5.6}
\]

The endpoint square forgets the two active orders.  Hence the number of
endpoint squares is

\[
 \boxed{\binom ms^2,}
 \tag{5.7}
\]

and every square supports exactly ((s!)^2) open active orders.

For one fixed open path, the two inactive cores can be ordered arbitrarily
in an ambient wreath, giving exactly

\[
 (q!)^2
 \tag{5.8}
\]

rooted marked completions.  Consequently the total completion mass based
at the initial edge is

\[
 \boxed{
 \left(\frac{m!}{q!}\right)^2(q!)^2=(m!)^2,}
 \tag{5.9}
\]

independent of (s).

For (q>0), every completion diverges from the actual returned seam.  Its
next omitted label is the first chosen core label in (K), whereas the
PBBS edge repeats (a_0=u).  Thus completion multiplicity supplies
neither a dynamic certificate nor a mandatory physical tail.  Weighting
sectors by completions is a neutral double count.

## 6. Catalan-dense static endpoint squares

The absence of a static (1/N) saving can be made quantitative.

### Theorem 6.1 (Catalan-positive static core-swap family)

Fix (a>0), and put

\[
 s=\lfloor a\sqrt m\rfloor.
 \tag{6.1}
\]

For all sufficiently large (m), there are at least

\[
 c_a\operatorname {Cat}_m
 \tag{6.2}
\]

distinct normalized oriented initial edges which possess an endpoint
core-swap square of active size (s), together with the complete static
owner/wreath package of Section 5.  Here (c_a>0) depends only on (a).

#### Proof

Let (D) be a Dyck word of semilength (m) and height at most (2s).
Let (U) be the positions of its first (s) up-steps, and let (V) be
the positions of its last (s) down-steps.  Since (s\le m/2), every
position in (U) precedes every position in (V).

Form a word (E) by keeping the bits of (D) on (U\cup V) and
complementing all other bits.  The word (E) has (m) up-steps, and the
up-step sets of (D) and (E) intersect exactly in (U).  In
particular,

\[
 |\mathbf1(D)\cap\mathbf1(E)|=s.
 \tag{6.3}
\]

It remains to check that (E) is Dyck.  Let (h_D(t)) and (h_E(t)) be
the two prefix heights, and put

\[
 u(t)=|U\cap[1,t]|,
 \qquad
 v(t)=|V\cap[1,t]|.
 \tag{6.4}
\]

Then

\[
 \boxed{h_E(t)=-h_D(t)+2(u(t)-v(t)).}
 \tag{6.5}
\]

Before the (s)-th selected up-step, every up-step seen belongs to (U)
and (v(t)=0).  If (d(t)) down-steps have appeared, then

\[
 h_E(t)=-(u(t)-d(t))+2u(t)=u(t)+d(t)\ge0.
 \tag{6.6}
\]

Between (U) and (V), one has (u(t)=s,v(t)=0), so the height bound on
(D) gives

\[
 h_E(t)=2s-h_D(t)\ge0.
 \tag{6.7}
\]

After (V) begins, every future down-step belongs to (V).  If (v(t))
of them have appeared, exactly (s-v(t)) down-steps remain.  Since the
future walk must descend from height (h_D(t)) to zero,

\[
 h_D(t)\le s-v(t).
 \tag{6.8}
\]

Thus

\[
 h_E(t)=-h_D(t)+2(s-v(t))\ge0.
 \tag{6.9}
\]

So (E) is Dyck.  The two oriented (m)-sets determined by (D,E)
have intersection (U) of size (s).  Their two differences have size
(m-s), and the complement of their union has size (s).  These four
parts are exactly the two active sets and two inactive cores of the
endpoint square.  Section 5 supplies all active orders and ambient
completions.

Let (F_m(2s)) count Dyck paths of height at most (2s).  Keeping only
the first positive term in the path-graph formula gives

\[
 F_m(2s)
 \ge
 \frac2{2s+2}\sin^2\frac\pi{2s+2}
 \left(2\cos\frac\pi{2s+2}\right)^{2m}.
 \tag{6.10}
\]

Since (s=a\sqrt m+O(1)), the right side is

\[
 c'_a\frac{4^m}{m^{3/2}}
 \tag{6.11}
\]

for some (c'_a>0).  Wallis' bounds identify this with a positive
constant multiple of \(\operatorname {Cat}_m\).  Distinct (D)'s give
distinct oriented initial edges, proving (6.2). \(\square\)

The theorem deliberately does **not** assert

\[
 E=\phi^{2s+1}D
 \tag{6.12}
\]

or the equivalent PBBS zero-voltage chronology.  Equation (6.12) is
exactly the missing dynamic condition.  Therefore Theorem 6.1 is a no-go
for static certificate counting, not a counterexample to (CP_A).

## 7. A recurrence-level dense core-swap model

There is also no deterministic (N)-scale spacing theorem in the local
owner recurrence.

Fix (1\le s<m), put

\[
 g=2s+1<N,
 \tag{7.1}
\]

and choose active labels

\[
 z_0,z_1,\ldots,z_{g-1}.
\]

Partition the remaining (2(m-s)) labels into cores (K,K'), each of
size (m-s).  For (t\in\mathbb Z), define

\[
 V_t=\{z_{t+1},z_{t+3},\ldots,z_{t+2s-1}\},
 \tag{7.2}
\]

with active subscripts modulo (g), and put

\[
 A_t=
 \begin{cases}
 K\cup V_t,&t\text{ even},\\
 K'\cup V_t,&t\text{ odd}.
 \end{cases}
 \tag{7.3}
\]

### Proposition 7.1 (dense local core-swap recurrence)

Consecutive states (A_t,A_{t+1}) are disjoint (m)-sets whose union is
([N]\setminus\{z_t\}).  The trajectory closes after (2g) steps and

\[
 z_{t+g}=z_t
 \tag{7.4}
\]

for every (t).  Hence every phase begins a simple fixed-core return of
gap (g).

#### Proof

The active windows (V_t,V_{t+1}) are disjoint and partition all active
labels except (z_t): one contains the odd forward offsets from (t),
the other the even forward offsets.  The cores are disjoint.  This proves
the Kneser-edge assertion and identifies the omitted label as (z_t).

Because (g) is odd, shifting by (g) preserves (V_t), repeats the
omitted label, and exchanges the parity, hence the two cores.  Shifting by
(2g) restores both the active window and the core.  The (g) labels in
every half-open gap are distinct.  Thus every return is simple and has
the core-swap square. \(\square\)

This model has the ordinary trace-packing density \(\Theta(1/g)\), not
(1/N).  It is not the canonical PBBS factor: it never omits a core
label and therefore violates the global complete-colour property.  Its
precise implication is that recurrence, simplicity, fixed cores, and
endpoint squares cannot prove (CP_A); a genuinely PBBS-global input is
necessary.

## 8. Exact proved and conditional boundary

### Proved here

1. The ordered-run common-row theorem, including multiple positive runs
   of one coordinate.
2. The exact (3s+2) two-core word for every genuine zero-winding sector.
3. Exact same-port superposition with ledger (3.3)--(3.4).
4. Uniform (W+o_A(W)) internal aggregation for every open-row coherent
   physical zero-winding packet family.
5. The sharp common-carrier FIFO theorem: one chain has exact excess \(s\)
   and covers all windows crossing its internal joins.
6. The exact ((m!)^2) completion census and the fact that every completion
   branches away at the returned seam.
7. A Catalan-positive family of static endpoint core-swap squares at every
   fixed Gaussian height scale.
8. A dense recurrence-level core-swap model showing that the local owner
   laws have only the ordinary (1/s) spacing scale.

### Not proved here

1. (CP_A), either physically or in the quotient.
2. A conversion from projected step-two edge-disjointness to disjoint
   paired one-step owner rows with only (o(W)) loss.
3. A literal cover of arbitrary packet/exterior boundary windows outside
   the proved common-carrier FIFO regime.
4. A near-perfect long-overlap port path cover satisfying (4.7).
5. Any positive-winding packing or fusion theorem.
6. The coefficient-one theorem.

The strongest surviving zero-winding gate is consequently dynamic and
global:

> use the actual PBBS/Dyck chronology to obtain either (a) a coherent
> paired-row decomposition plus external-boundary cover, or (b) a
> near-perfect long-overlap packet path cover with total defect (o(W)).

Static core-swap squares and factorial ambient completions cannot provide
that theorem.

## 9. Independent audit of the decisive step

The packet algebra and the global implication scope were audited
independently.

* The word (2.7), its length (3s+2), all four families in (2.9), and the
  identical ((s-1))-letter prefix/suffix passed exactly.
* The group length (t(2s+3)+s-1), excess (2t+s-1), port-type bound,
  low-height spectral deletion, and high-height edge-volume bound passed
  under the explicit open-row coherence hypothesis.
* The audit rejected the stronger claim that standard projected
  step-two packing implies (3.10).  That rejection is incorporated in the
  theorem statement and in Section 3's scope.
* The audit also confirmed that arbitrary packet regrouping preserves only
  packet-internal witnesses.  No external-boundary witness is claimed.
* The common-carrier FIFO theorem was separately audited.  Its full
  cross-block intersection/union identities, nonadjacent-reuse argument,
  length \((t+1)s+1\), and exact excess \(s\) passed.  The global
  baseline conclusion is explicitly conditioned on owner-disjointness
  across all heights, and chain aggregation is correctly performed by
  merging token strings and appending one shared carrier.
* The factorial census, the returned-seam divergence, the Catalan-dense
  static construction, and the dense recurrence countermodel were checked
  independently.  None is promoted to an actual PBBS counterexample.
