# PBBS in-place portal replacement: exact packet saving and the crossing gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Let (N=2m+1), and let a simple PBBS return have odd gap (2s+1),
where (1\le s<m). Its (2s+2) middle owners split into two projected
Johnson paths with disjoint fixed cores. The exact two-core portal chart
has cyclic length

\[
 2s+3,
\]

and covers every consecutive intersection and union, at every depth, in
both paths. Thus, relative to the (2s+2) owner positions of the packet,
its cyclic excess is exactly one. This is a genuine in-place packet
interior replacement at net cost (1=o(s)) when (s\to\infty).

The cyclic chart has one ordered singleton port of length (s-1). Opening
one packet in isolation gives a linear word of length (3s+2), hence
excess (s), not (o(s)). If equal-height packets can be joined in
ordered-port-compatible chains, the port is exported from one packet to
the next and (R) packets in (c) chains have exact length

\[
 R(2s+3)+c(s-1).
\]

If the packet owner-occurrence sets are disjoint (or have first been
disjointized with only an explicitly charged endpoint loss), this proves
the desired little-oh replacement for all packet-internal targets whenever

\[
 R+c(s-1)=o(Rs).
\]

It does **not** prove a global PBBS compiler. Ordered-port compatibility
is core-blind and need not preserve even one projected Johnson edge at the
new packet boundary. The exact centered (q=2) chronology makes the
shallow damage cheap: at one exposed old boundary, all lower and upper
windows of depths (1,2) cost at most six literal repairs. But the
remaining support-blind catalogue at depths (3,\ldots,H) has size

\[
 H(H+1)-6
\]

per boundary. The all-depth corridor proves that every target has some
PBBS occurrence; it does not prove an alternative occurrence avoiding
all reordered packet boundaries.

The exact boundary is therefore:

* positive: (+1) cyclic packet replacement and exact ordered-port
  export for all internal targets;
* positive: only (O(1)) shallow repair per exposed boundary, by the
  audited (q=2) chronology;
* unresolved: support-essential growing-depth crossing windows;
* exact first failure: the exported port does not contain the fixed-core
  information required by a physical projected seam.

## 1. The two fixed-core rows

Let the omitted labels of the rainbow return segment be

\[
 a_j=\lambda_{2j}\quad(0\le j\le s),\qquad
 b_j=\lambda_{2j+1}\quad(0\le j<s),
\]

and assume that these (2s+1) labels are pairwise distinct. Put

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
       =(b_0,\ldots,b_{s-1},a_0,\ldots,a_s).
\]

For (i\in\mathbb Z_{2s+1}), let (V_i) be the cyclic (s)-window of
\(\Gamma\) starting at (i). The PBBS two-step recurrence

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}
\]

gives disjoint cores (K,K'), each of size (m-s), such that

\[
 E_j=K\cup V_j\qquad(0\le j\le s),
\tag{1.1}
\]

and

\[
 O_j=K'\cup W_j\qquad(0\le j\le s),
\tag{1.2}
\]

where

\[
 W_j=V_{s+1+j}\quad(0\le j<s),\qquad W_s=V_0.
\tag{1.3}
\]

These are exactly the even and odd projected orders of the (2s+2)
middle owners in the segment. Every consecutive interval in either row is
a geodesic Johnson interval. In particular, for (0\le p\le q\le s),

\[
 \bigcap_{j=p}^{q}E_j
 =K\cup\{\gamma_q,\ldots,\gamma_{p+s-1}\},
\tag{1.4}
\]

\[
 \bigcup_{j=p}^{q}E_j
 =K\cup\{\gamma_p,\ldots,\gamma_{q+s-1}\}.
\tag{1.5}
\]

For the odd row,

\[
 \bigcap_{j=p}^{q}O_j
 =K'\cup\{\gamma_0,\ldots,\gamma_{p-1}\}
       \cup\{\gamma_{s+1+q},\ldots,\gamma_{2s}\},
\tag{1.6}
\]

\[
 \bigcup_{j=p}^{q}O_j
 =K'\cup\{\gamma_0,\ldots,\gamma_{q-1}\}
       \cup\{\gamma_{s+1+p},\ldots,\gamma_{2s}\}.
\tag{1.7}
\]

Empty displayed ranges are omitted. These identities follow directly by
intersecting or uniting cyclic (s)-windows.

## 2. Exact cyclic and linear portal words

Write a coordinate for its singleton set-letter, and define

\[
\begin{aligned}
 \mathcal A&=(\gamma_{2s-1},\gamma_{2s-2},\ldots,\gamma_s),\\
 \mathcal B&=(\gamma_{s-1},\gamma_{s-2},\ldots,\gamma_0),\\
 \mathcal C&=(\gamma_{2s},\gamma_{2s-1},\ldots,\gamma_{s+1}),\\
 \mathcal P&=(\gamma_{2s-1},\gamma_{2s-2},\ldots,\gamma_{s+1}).
\end{aligned}
\tag{2.1}
\]

The first three blocks have length (s), while the ordered port
\(\mathcal P\) has length (s-1).

### Theorem 2.1 (two-core portal chart)

The linear word

\[
 \boxed{\mathcal L=\mathcal A,\ K,\ \mathcal B,\ K',\ \mathcal C}
\tag{2.2}
\]

has length (3s+2) and realizes every set in (1.4)--(1.7) as a
contiguous OR. The cyclic word

\[
 \boxed{
 \mathcal Z=\mathcal P,\ \gamma_s,\ K,\
             \mathcal B,\ K',\ \gamma_{2s}}
\tag{2.3}
\]

has length (2s+3) and realizes the same family by cyclic intervals.
Appending one terminal copy of (\mathcal P) to (2.3) gives (2.2), up
to cyclic rotation.

#### Proof

The subword

\[
 \gamma_{2s-1},\ldots,\gamma_s,K,
 \gamma_{s-1},\ldots,\gamma_0
\]

has, across (K), exactly the active intervals in (1.4)--(1.5), read in
reverse coordinate order. Hence it realizes every even-row target.

The subword

\[
 \gamma_{s-1},\ldots,\gamma_0,K',
 \gamma_{2s},\ldots,\gamma_{s+1}
\]

does the same for (1.6)--(1.7). This proves the linear assertion.

In the cyclic word (2.3), the even-row witnesses use the nonwrapping arc

\[
 \mathcal P,\gamma_s,K,\mathcal B,
\]

whereas the odd-row witnesses use the other directed arc

\[
 \mathcal B,K',\gamma_{2s},\mathcal P.
\]

Thus both families are cyclic intervals. A second copy of
\(\mathcal P\) opens the latter arc without changing any OR, producing
the linear word. Every letter is nonempty because (s<m), so
\(|K|=|K'|=m-s\ge1\). \(\square\)

The packet contains (2s+2) middle owners. Therefore

\[
 |\mathcal Z|-(2s+2)=1,
\tag{2.4}
\]

whereas

\[
 |\mathcal L|-(2s+2)=s.
\tag{2.5}
\]

The packet interior is consequently cheap; opening its ordered port is
the whole local linear toll.

### Corollary 2.2 (exact port-chain ledger)

Suppose (R) equal-height packets with disjoint owner-occurrence sets are
partitioned into (c) directed chains such that the outgoing ordered port
of each packet is literally the incoming ordered port of the next, after
one common coordinate rotation of the complete physical phase deck. A
normalized isomorphism without this literal phase matching is not enough.
Then all packet-internal lower and upper targets have one ordinary literal
word of length

\[
 \boxed{R(2s+3)+c(s-1).}
\tag{2.6}
\]

Relative to the (R(2s+2)) packet-owner positions, the exact excess is

\[
 \boxed{R+c(s-1).}
\tag{2.7}
\]

#### Proof

Use one cyclic chart (2.3) per packet. At an internal chain join, the
next packet's initial copy of (\mathcal P) is the preceding packet's
missing terminal copy. Only the final packet of each chain needs an
appended port. Summation gives (2.6)--(2.7). \(\square\)

This corollary is integral and literal. It covers packet interiors only;
it deliberately does not assert that a chain join is an edge of the
original PBBS chronology.

## 3. Exact shallow-boundary quarantine

Consider one exposed boundary of an original projected path. At depth
(q\), exactly (q) rooted owner windows of (q+1) owners cross that
boundary. Appending both their lower intersections and their upper unions
therefore costs at most (2q) set-letters.

### Lemma 3.1 (boundary catalogue)

For one exposed boundary, the complete support-blind repair catalogue is

\[
 2\sum_{q=1}^{H}q=H(H+1).
\tag{3.1}
\]

The depths (q=1,2) contribute exactly at most

\[
 2(1+2)=6,
\tag{3.2}
\]

leaving

\[
 \boxed{H(H+1)-6}
\tag{3.3}
\]

possible lower/upper crossing occurrences at depths (3,\ldots,H).

#### Proof

A length-((q+1)) interval crosses a fixed boundary precisely when its
start is one of the (q) positions immediately preceding the boundary.
Each such owner interval supplies one lower and one upper target. Sum over
the stated depths. \(\square\)

A two-parity packet interval has at most four exposed path boundaries.
Thus the exact worst-case packet ledger is

\[
 24
\tag{3.4}
\]

shallow repairs and

\[
 4\bigl(H(H+1)-6\bigr)
\tag{3.5}
\]

remaining deep crossing occurrences.

The audited centered (q=2) parenthesis theorem says that every rooted
turn has the correct rank and that the lower and upper (q=2) target
systems are complete. Therefore the repairs in (3.4) are genuine literal
sets of the required ranks. For (R=O(W/H)) critical packets, appending
all of them costs (O(R)=O(W/H)=o(W)).

This is the exact gain from the new (q=2) chronology. It removes every
shallow-boundary ambiguity but does not alter (3.3). The all-depth PBBS
corridor supplies at least one correct occurrence of every target, but it
does not assert that one may choose those occurrences outside all exposed
boundaries simultaneously. Replacing (3.3) by an (o(H)) or support-level
catalogue is precisely the remaining theorem.

## 4. Ordered-port compatibility is not physical chronology

The port (\mathcal P) in (2.1) contains only active singleton labels.
It contains neither fixed core. Consequently equality of ordered ports
does not imply a projected Johnson seam.

### Proposition 4.1 (core-blind port countermodel)

Fix one active cycle (\Gamma) and its inactive partition

\[
 K\mathbin{\dot\cup}K',\qquad |K|=|K'|=m-s.
\]

Let one abstract simple-sector completion have projected row

\[
 E_j=K\cup V_j,
\]

and let a second completion use the swapped core

\[
 E'_j=K'\cup V_j.
\]

Their normalized ordered ports are literally identical. Nevertheless the
natural forward join from the last first-row owner to the first second-row
owner is not a Johnson edge:

\[
 \boxed{E_s\cap E'_0=\varnothing.}
\tag{4.1}
\]

#### Proof

The two cores are disjoint and are disjoint from every active label.
Moreover

\[
 V_s=\{\gamma_s,\ldots,\gamma_{2s-1}\},\qquad
 V_0=\{\gamma_0,\ldots,\gamma_{s-1}\},
\]

so (V_s\cap V_0=\varnothing). This proves (4.1). Both owners have rank
(m), whereas a Johnson edge between rank-(m) owners requires
intersection size (m-1). \(\square\)

The proposition is a countermodel to an implication from ordered-port
data. It does not claim that the canonical PBBS factor places these two
completions adjacently. Its content is exact: the certificate that exports
the (s-1) literal singleton positions does not include the core data
needed to preserve the old boundary chronology.

There are therefore two distinct compatibility gates.

1. **Literal arm compatibility.** For target-square certificate classes
   with pins (p_\alpha) and caps (U_\alpha), one letter may serve all
   classes exactly when

   \[
    \{p_\alpha\}_\alpha\subseteq\bigcap_\alpha U_\alpha.
   \tag{4.2}
   \]

   Ordered-port equality is a strong instance of this condition.

2. **Physical chronology compatibility.** Prescribed boundary middle
   owners must be disjoint in the odd graph, or prescribed projected
   owners must intersect in rank (m-1) in the Johnson graph. Equation
   (4.2) alone does not imply either condition.

The cyclic portal chart solves the first gate for packet interiors. It
does not solve the second gate for the original crossing collars.

## 5. Exact implication boundary

The following theorem is proved.

> For any supplied owner-disjoint family of simple Gaussian PBBS packets
> whose literal physical ordered ports form chains with
> (R+c(s-1)=o(Rs)), there is a literal word with
> (o(Rs)) net excess over their owner mass which covers every lower and
> upper packet-internal target at every depth. After exposing the original
> packet boundaries, every lower and upper depth-(1) and depth-(2)
> crossing target may be restored with (O(R)=o(Rs)) further letters.

The following is not proved.

> The growing-depth crossing targets left at the original packet
> boundaries have (o(Rs)) distinct support-essential mass, or admit a
> nonlocal baseline rethreading of that cost.

In particular, neither the (q=2) parenthesis formula nor the all-depth
support corridor turns an arbitrary normalized-port chain into a physical
PBBS chain. The exact missing input is a cross-packet theorem that exports
the ordered port while simultaneously preserving the old core/collar
targets, or proves that the targets thereby lost already have intact
occurrences elsewhere.

The critical double-deck packing theorem by itself does not supply the
owner-disjoint literal port chains assumed above: trace-disjointness in
each deck does not automatically give cross-disjointness between the two
packet families. That ownership/disjointization step is part of the same
remaining global gate.
