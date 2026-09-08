# PBBS in-place baseline replacement candidate: exact packet fusion and the crossing/provenance gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad B=\operatorname {Cat}_m,\qquad
 W=\binom{2m+1}{m}=nB,
 \qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed. Consider an actual simple PBBS return of gap
\(2s+1\), with \(1\le s<m\). The following positive and negative
statements are exact.

1. **The exact packet-interior owner-slot primitive exists.** The two
   step-two parity rows contain \(2s+2\) middle owners. There is a
   nonzero circular word of length

   \[
      \boxed{2s+3}
   \tag{0.2}
   \]

   representing every consecutive intersection and union on both rows,
   through their full available depth \(s\). Thus the circular net cost
   over the owner baseline is exactly one. Equal ordered ports splice
   integrally across the complete phase deck. If \(t\) equal-height
   packets form \(c\) literal port chains, one ordinary linear word has length

   \[
      \boxed{t(2s+3)+c(s-1)},
   \tag{0.3}
   \]

   and excess

   \[
      \boxed{t+c(s-1)}
   \tag{0.4}
   \]

   over their \(t(2s+2)\) owner-occurrence slots, provided the full
   packets are owner-occurrence-disjoint. If also \(s\to\infty\), then
   \(c=o(t)\) gives \(o(ts)\) packet-internal excess. This is a genuine
   replacement of the owner-slot packet interior, not an appended seam
   chart. For one isolated packet the circular primitive is not yet an
   ordinary word; its self-contained linearization has length \(3s+2\).
   A separate provenance lemma is still needed before these owner slots
   may be identified with deleted principal \(H\)-erosion letters.

2. **An isolated one-parity sector cannot do this.** One projected row
   has \(s+1\) baseline positions, but its exact PBBS target grid forces
   \(2s+1\) distinct literal certificate positions. If \(c_0\) collar
   positions are also deleted and \(\rho\) certificates are exported
   outside the replacement, the net cost \(\delta\) satisfies

   \[
      \boxed{\delta\ge s-c_0-\rho.}
   \tag{0.5}
   \]

   Thus the success of (0.2) necessarily uses cross-parity sharing, and a
   linear word with net \(o(s)\) must export or absorb \(s-o(s)\) arm
   certificates.

3. **Port fusion does not preserve original crossing chronology.** The
   normalized port in (0.3) records \(s-1\) active singleton labels but
   omits both cores and both boundary owners. Equal ports therefore do
   not imply a Johnson successor edge. If the carrier and actual
   successor are added to the port data, two joined fixed-carrier runs
   concatenate into one longer run; distinct maximal runs have no such
   join under the exact fixed-carrier shared-facet interface. Thus
   normalized-type grouping is not forced to preserve the PBBS order,
   while that chronology-bearing maximal-run interface has no nontrivial
   edges.

4. **The exact \(q=2\) theorem quarantines only bounded depth.** At most
   \(6J\) lower/upper occurrences of depths one and two cross \(J\)
   erased boundaries, so at critical \(J=O(W/H)\) their physical
   catalogue has size \(o(W)\). Converting it to a literal repair after
   erosion deletion is conditional on the provenance interface below.
   In contrast, the audited all-depth dominance seam
   costs \(O(HJ)\), which is \(\Theta(W)\) when
   \(J=\Theta(W/H)\). The parenthesis theorem gives fewer than \(24B\)
   nonunique rooted lower-\(q=2\) occurrences, but \(q=2\) meets only two
   of the \(2s\) forced arm classes (two of \(2s+1\) certificate classes
   after including the neutral class). It cannot control the
   required linear certificate export.

Consequently the in-place lane is settled up to two sharply stated global
interfaces. An owner-disjoint critical packet assignment with sufficiently
few literal port chains can be rebundled internally at
\(o(\text{span})\) owner-slot cost. Independent local owner-slot
replacement and
the exact fixed-carrier chronology-preserving port
splicing are rigorously obstructed. What remains is a noncellular
cross-packet word which simultaneously shares a linear number of arm
certificates, receives a valid erosion-witness provenance assignment, and
realizes the old \(q\ge3\) crossing targets, or a PBBS
theorem showing that the corresponding pin-cap overlap system has
insufficient capacity. No coefficient-one conclusion is claimed.

## 1. The two fixed-core rows of a simple return

Let

\[
 A_{u+1}=[n]\setminus(A_u\cup\{\lambda_u\})
\tag{1.1}
\]

be the physical PBBS trajectory. Suppose

\[
 \lambda_{2s+1}=\lambda_0
\tag{1.2}
\]

and the half-open list

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2s}
\tag{1.3}
\]

is pairwise distinct. Write

\[
 a_j=\lambda_{2j}\quad(0\le j\le s),\qquad
 b_j=\lambda_{2j+1}\quad(0\le j<s),
\tag{1.4}
\]

and put the active labels in the cyclic order

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
 =(b_0,\ldots,b_{s-1},a_0,\ldots,a_s).
\tag{1.5}
\]

Let (V_j) be the cyclic (s)-window of \(\Gamma\) starting at (j).
The two-step recurrence

\[
 A_{u+2}=A_u-\{\lambda_{u+1}\}+\{\lambda_u\}
\tag{1.6}
\]

gives disjoint cores (K,K'), each of size (m-s), such that the two
parity rows are

\[
 E_j=K\cup V_j\qquad(0\le j\le s),
\tag{1.7}
\]

and

\[
 O_j=K'\cup W_j\qquad(0\le j\le s),
\tag{1.8}
\]

where

\[
 W_j=V_{s+1+j}\quad(0\le j<s),\qquad W_s=V_0.
\tag{1.9}
\]

These are exactly the (2s+2) physical middle owners
(A_0,\ldots,A_{2s+1}), separated into their two step-two orders.
Nothing here is inferred merely from a Dyck deficit or height: the return
and its simple label list are hypotheses.

## 2. Exact circular replacement of the whole packet

Write a coordinate for its singleton set-letter and define

\[
\begin{aligned}
 \mathcal A&=(\gamma_{2s-1},\gamma_{2s-2},\ldots,\gamma_s),\\
 \mathcal B&=(\gamma_{s-1},\gamma_{s-2},\ldots,\gamma_0),\\
 \mathcal C&=(\gamma_{2s},\gamma_{2s-1},\ldots,\gamma_{s+1}).
\end{aligned}
\tag{2.1}
\]

The ordinary word

\[
 \mathcal L=\mathcal A, K,\mathcal B,K',\mathcal C
\tag{2.2}
\]

has length (3s+2).

### Theorem 2.1 (two-core packet chart)

The word \(\mathcal L\) represents, as ordinary contiguous ORs, every
set

\[
 \bigcap_{j=p}^{q}E_j,\quad \bigcup_{j=p}^{q}E_j,
 \quad
 \bigcap_{j=p}^{q}O_j,\quad \bigcup_{j=p}^{q}O_j
 \qquad(0\le p\le q\le s).
\tag{2.3}
\]

#### Proof

For the (K)-row, cyclic-window arithmetic gives

\[
 \bigcap_{j=p}^{q}E_j
 =K\cup\{\gamma_q,\ldots,\gamma_{p+s-1}\},
\tag{2.4}
\]

with an empty active interval when \((p,q)=(0,s)\), and

\[
 \bigcup_{j=p}^{q}E_j
 =K\cup\{\gamma_p,\ldots,\gamma_{q+s-1}\}.
\tag{2.5}
\]

Both are intervals of the subword

\[
 \gamma_{2s-1},\ldots,\gamma_s,K,
 \gamma_{s-1},\ldots,\gamma_0.
\tag{2.6}
\]

For the second row, (1.9) gives

\[
\begin{aligned}
 \bigcap_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{p-1}\}
       \cup\{\gamma_{s+1+q},\ldots,\gamma_{2s}\},\\
 \bigcup_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{q-1}\}
       \cup\{\gamma_{s+1+p},\ldots,\gamma_{2s}\}.
\end{aligned}
\tag{2.7}
\]

These are intervals of

\[
 \gamma_{s-1},\ldots,\gamma_0,K',
 \gamma_{2s},\ldots,\gamma_{s+1}.
\tag{2.8}
\]

Empty arms mean that the corresponding endpoint is the core letter.
Every letter is nonzero because (s<m). \(\square\)

Now put

\[
 \mathcal P=(\gamma_{2s-1},\ldots,\gamma_{s+1}),
 \qquad |\mathcal P|=s-1.
\tag{2.9}
\]

The circular word

\[
 \boxed{
 \mathcal Z=\mathcal P,\gamma_s,K,
             \mathcal B,K',\gamma_{2s}}
\tag{2.10}
\]

has length (2s+3). Every (K)-row witness lies in the nonwrapping arc

\[
 \mathcal P,\gamma_s,K,\mathcal B,
\]

and every (K')-row witness lies in the circular arc

\[
 \mathcal B,K',\gamma_{2s},\mathcal P.
\]

Thus \(\mathcal Z\) cyclically represents all targets in (2.3), and
\(\mathcal L=\mathcal Z,\mathcal P\). The whole packet therefore has
circular excess

\[
 (2s+3)-(2s+2)=1,
\tag{2.11}
\]

while the self-contained linear opening costs the additional (s-1)
letters.

### Theorem 2.2 (literal port-chain ledger)

Suppose (t) height-(s) packets are partitioned into (c) directed
chains such that at each chain edge the next packet's initial ordered port
is literally the preceding packet's required terminal port. Then all
packet-internal targets have one ordinary word of length

\[
 \boxed{t(2s+3)+c(s-1).}
\tag{2.12}
\]

#### Proof

Use one unduplicated circular list (2.10) for every packet. At an
internal chain edge, the initial copy of \(\mathcal P\) in the next list
supplies the wrapping terminal copy required by the preceding list. Only
the last packet of each chain needs an appended copy. This proves
(2.12). \(\square\)

The length formula itself does not require disjoint packet owners. Its
interpretation as excess \(t+c(s-1)\) over \(t(2s+2)\) baseline slots
does: the complete \(2s+2\)-owner packets must be owner-occurrence-
disjoint, or every overlap must be charged separately. Moreover,
\(c=o(t)\) gives \(o(ts)\) only in the growing regime \(s\to\infty\).

If ports agree after a cyclic ground rotation, the complete \(n\)-phase
deck still splices integrally: the required phase shift is a translation
of \(\mathbb Z_n\), hence a permutation. This uses no fractional owner
assignment. For a supplied full phase deck, grouping by height and
normalized port produces at most \(\exp(o(m))\) terminal literal chains
for \(s\le H\): the needed ground rotation is implemented by a phase
permutation. Therefore a critical owner-disjoint full-packet family with
\(t=\Theta(W/H)\) has internal excess

\[
O(t)+H\exp(o(m))=o(W).
\tag{2.13}
\]

Indeed, for fixed \(s\ge2\), a port is an ordered \((s-1)\)-tuple of
distinct ground labels. Modulo a common cyclic rotation it has fewer than
\(n^{s-2}\) types. Each normalized type in a complete phase deck produces
at most \(n\) literal chains, since every interpacket phase map is a
translation permutation. Summing over heights and the two orientations
gives fewer than

\[
 2Hn^{H-1}=\exp(O(H\log n))=\exp(o(m))
\tag{2.14}
\]

chains for \(H=O(\sqrt m)\). The bounded cases \(s=1\) are absorbed into
the same bound.

Equation (2.13) concerns packet-internal targets only. It also presupposes
that the two parity owner families have been disjointized so their full
\(2s+2\) baseline credit may be summed; projected-trace disjointness in
one parity alone does not supply this premise.

## 3. Why the one-parity lower bound is not contradicted

For one complemented parity row, rotate the active order so that

\[
 X_j=F\cup\{\eta_j,\eta_{j+1},\ldots,\eta_{j+s}\},
 \qquad 0\le j\le s,
\tag{3.1}
\]

where \(|F|=m-s\). Put

\[
 C=F\cup\{\eta_s\},\qquad
 \ell_i=\eta_{s-i},\qquad \rho_i=\eta_{s+i},
\tag{3.2}
\]

and

\[
 T_{a,b}=C\cup\{\ell_1,\ldots,\ell_a\}
             \cup\{\rho_1,\ldots,\rho_b\}.
\tag{3.3}
\]

Every \(T_{a,b}\), \(0\le a,b\le s\), is a consecutive intersection or
union of the row. Any nonzero literal word representing this grid needs
at least (2s+1) positions: a witness for (C) gives one neutral
position; witnesses for (T_{i,0}) give (s) distinct positions carrying
the successive left pins; witnesses for (T_{0,j}) give (s) further
distinct positions carrying the right pins. The central-marker word

\[
 \{\ell_s\},\ldots,\{\ell_1\},C,
 \{\rho_1\},\ldots,\{\rho_s\}
\tag{3.4}
\]

attains equality.

Consequently a self-contained replacement of this row's (s+1) baseline
slots costs (s). More generally, if it deletes (c_0) collar slots and
exports \(\rho\) of the (2s+1) forced certificate positions, then

\[
 \delta\ge s-c_0-\rho.
\tag{3.5}
\]

The circular word (2.10) escapes this bound exactly by using the other
parity's baseline mass and by leaving one ordered port open for the next
packet. It does not give a self-contained one-row compression.

For several sectors the certificate sharing condition is exact. A
nonneutral class is a pin-cap pair \((p,U)\), meaning that its shared
letter must contain (p) and be a subset of (U). Classes
\((p_\alpha,U_\alpha)\) can share one physical word position if and only if

\[
 \boxed{
 \{p_\alpha:\alpha\}\subseteq\bigcap_\alpha U_\alpha.}
\tag{3.6}
\]

The union of the pins proves sufficiency. This is the exact statewise
overlap problem left after the local lower bound; edge-disjoint return
supports alone do not control it.

## 4. Coarse ports forget chronology

The port \(\mathcal P\) in (2.9) depends only on (s-1) active labels.
It records neither (K,K') nor a boundary owner. Hence literal port
equality cannot certify a physical seam.

### Lemma 4.1 (exact-factor counterexample to port sufficiency)

Fix the active order \(\Gamma\) and partition its inactive complement
into two disjoint \((m-s)\)-sets \(K,K'\). Form one fixed-core packet with
cores \((K,K')\) and a second formal packet with the cores interchanged.
Both have the same normalized port \(\mathcal P\), and both fixed-core
segments extend to exact middle wreaths. Nevertheless the terminal even
owner

\[
 E_s=K\cup V_s
\]

of the first and the initial even owner

\[
 \widetilde E_0=K'\cup V_0
\]

of the second satisfy

\[
 E_s\cap\widetilde E_0=\varnothing,
\tag{4.1}
\]

because (K\cap K'=\varnothing) and the cyclic (s)-windows (V_s,V_0)
are disjoint. A step-two PBBS successor of a rank-(m) owner has
intersection (m-1) with it, so (4.1) is not a chronological Johnson
edge.

The lemma does not claim that both formal packets occur consecutively in
the canonical PBBS factor. It proves the precise logical point: port
equality plus exact-factor completion does not imply physical successor
compatibility.

Adding the missing carrier data creates the opposite obstruction. Let a
maximal fixed-carrier run have the sliding form

\[
 X_i=S\cup\{\xi_i,\ldots,\xi_{i+q-1}\}.
\tag{4.2}
\]

Its decorated outgoing port is

\[
 (S;\xi_{L+1},\ldots,\xi_{L+q-1}),
\]

and its incoming port is defined analogously.

### Lemma 4.2 (chronological decorated-port rigidity)

Suppose two such runs have the same displayed carrier \(S\), their active
ports have the exact ordered \(q-1\) overlap displayed above, and the
initial owner of the second is the actual Johnson successor of the
terminal owner of the first. Assume explicitly that the shared facet of
that Johnson edge is exactly \(S\) together with this common ordered
\((q-1)\)-tuple. Then their token lines concatenate into one
longer fixed-\(S\)
run. In particular two distinct proper maximal runs admit no such join.

#### Proof

Port equality identifies the (q-1) retained token coordinates across
the boundary. The actual nonlazy Johnson edge removes the old first token
and inserts the new last token. Glue the two ordered token lines along
the common (q-1)-tuple. Every length-(q) token window of the glued
line is an old window from one side, including the two windows adjacent to
the seam. A repeated label at distance (q) would make the seam update
lazy; hence no such repetition occurs. Therefore every displayed owner
is an (S)-extension and every intervening depth-(q) intersection is
(S). The two runs are one longer fixed-carrier run, contradicting
distinct maximality. \(\square\)

Lemmas 4.1--4.2 give the exact dichotomy:

\[
\begin{array}{c|c|c}
 \text{interface}&\text{many matches?}&\text{old crossings preserved?}\\ \hline
 \text{normalized singleton port}&\text{possibly}&\text{not forced}\\
 \text{carrier + port + actual successor}&\text{no between maximal runs}
                                      &\text{yes}.
\end{array}
\tag{4.3}
\]

## 5. What exact \(q=2\) chronology does and does not repair

For the centered PBBS successor \(g=f^2\), the audited parenthesis formula
gives, for every rooted turn,

\[
 f^{-2}A\cap A\cap f^2A
   =A\setminus\{p_-(D_A),p_+(D_A)\},
\tag{5.1}
\]

where \(D_A\) is the rooted Dyck suffix of \(A\), and the two
distinguished parenthesis steps are different. Every
rank-\((m-2)\) target occurs, with

\[
 1\le\mu_2^-(T)\le10,
\tag{5.2}
\]

and

\[
 \sum_T(\mu_2^-(T)-1)
 =W-\binom{2m+1}{m-2}<12B.
\tag{5.3}
\]

Thus the mass of rooted \(q=2\) occurrences whose target is nonunique is
less than \(24B\), because

\[
\mu\le2(\mu-1)\qquad(\mu\ge2).
\tag{5.4}
\]

This is the original lower-signed statement. The complemented row in
Section 3 reverses signs: its lower diagonal corresponds to the original
upper \(q=2\) layer. For that layer the audited theorem gives

\[
 1\le\mu_2^+(U)\le3,\qquad
 \sum_U(\mu_2^+(U)-1)
 =W-\binom{2m+1}{m+2}<4B,
\tag{5.4a}
\]

so fewer than \(8B\) rooted upper-\(q=2\) occurrences have nonunique
targets. Thus the two signed layers together have nonunique rooted mass
less than \(32B\).

Inside the one-parity grid (3.3), lower depth \(q\) is the diagonal

\[
 a+b=s-q.
\tag{5.5}
\]

The certificate theorem uses the two full axes
\(T_{i,0},T_{0,i}\), \(1\le i\le s\). Depth \(q=2\) meets only the two
axis classes \(i=s-2\). Hence even perfect rooted \(q=2\) uniqueness
controls only \(O(1)\) of the \(\Theta(s)\) positions which must be shared
or exported in (3.5). For the complemented grid this assertion uses the
upper-signed bound (5.4a), not the lower-signed bound (5.3).

There is also an exact crossing-count distinction. A cut edge belongs to
exactly \(q\) owner windows of \(q+1\) consecutive owners. Therefore
\(J\) erased chronological seams expose at most \(2qJ\) selected target
occurrences at depth \(q\), counting lower intersections and upper unions.
Thus

\[
 \boxed{2(1+2)J=6J}
\tag{5.6}
\]

is the complete physical crossing catalogue for depths one and two. At the
critical packet scale \(J=O(W/H)\), its cardinality is \(o(W)\).
Appending these targets is a valid repair only after a literal exterior
splice/provenance lemma has certified that no other erosion witnesses were
lost.

For all depths through \(H\), the corresponding support-blind sum is

\[
 2J\sum_{q=1}^{H}q=H(H+1)J.
\tag{5.7}
\]

The exact appended crossing chart alone uses \(4H-1\) nonzero letters per
seam: \(2H-1\) for lower targets and \(2H\) for upper targets. Its charged
length at critical density is

\[
 (4H-1)J=\Theta(W)
 \qquad\text{when }J=\Theta(W/H).
\tag{5.8}
\]

The equivalence between short-return packing and the established clustered
additive seam cost shows that clustering does not change this critical
order within that architecture. Equation (5.8) is not a universal lower
bound on an in-place cross-boundary braid.

If the endpoint-capped erosion initialization lost at the cut is charged
as well, the established one-cut ledger is \(5H-1\), not \(4H-1\).
This changes no critical-order conclusion.

Finally, the all-depth PBBS corridor supplies at least one correct
occurrence of every target. It does not say that a correct occurrence
can be chosen away from every reordered packet boundary, and its
pointwise cap is not a unique-witness theorem. Consequently it does not
turn (5.8) into \(o(W)\).

### 5.1 The exact erosion-provenance gap

The packet word in Section 2 has been compared with \(2s+2\)
owner-occurrence slots. The actual coefficient-one baseline, however, is
the endpoint-capped \(H\)-erosion word

\[
 D_i=\bigcap_{h=0}^{H}\widetilde X_{i+h}.
\tag{5.9}
\]

Its canonical witnesses are ranges of erosion indices:

\[
 \bigcap_{u=a}^{b}X_u
   =\bigcup_{i=b-H}^{a}D_i,\qquad
 \bigcup_{u=a}^{b}X_u
   =\bigcup_{i=a-H}^{b}D_i.
\tag{5.10}
\]

Consequently deleting an erosion position indexed inside a packet can
destroy a witness whose owner window is not packet-internal. The shallow
catalogue (5.6) counts physical owner windows crossing the old boundary;
it does not by itself classify every canonical erosion witness using the
deleted indices, nor does it rebuild the endpoint padding of the exterior
erosion paths.

Thus a full baseline substitution additionally requires the following
literal statement.

> **Erosion replacement provenance (ERP\(_H\)).** Assign every selected
> packet owner occurrence credited in Section 2 injectively to a distinct
> deleted \(D_i\) in the same chosen parity and signed trajectory. If the
> principal baseline is the rank-\((m+1)\) complement-projected trajectory
> while the packet chart is written on rank-\(m\) owners, first construct
> the corresponding signed/complemented packet chart; cardinality alone
> gives no credit. Verify that its atlas is exactly the signed atlas
> formerly certified by the deleted \(D_i\)-ranges. Then assign every
> selected target whose old erosion witness meets a deleted packet index
> to one of: (i) a packet-internal witness in the new packet word; (ii) an
> explicitly charged boundary witness in a common cross-packet chart; or
> (iii) an equal-OR witness using no deleted erosion position. The exterior
> endpoint-capped erosion words must splice to that chart with total new
> padding \(o(W)\).

No argument above proves ERP\(_H\). This is the first exact point at which
the owner-slot primitive fails to become a certified deletion of principal
erosion letters.

## 6. Exact proved and conditional boundary

The following is proved.

* A whole simple two-parity packet has an exact circular packet-interior
  word of length \(2s+3\), only one above its \(2s+2\)
  owner-occurrence baseline.
* Literal port chains make the packet-internal replacement an ordinary
  linear word with excess \(t+c(s-1)\); an owner-disjoint critical family
  with \(c=o(t)\) has \(o(\text{total span})\) internal cost.
* A self-contained one-parity replacement has linear cost, and any escape
  must consume or export \(s-o(s)\) exact arm certificates.
* Normalized-port grouping is not physical chronology; under the exact
  shared-facet hypothesis, restoring the carrier and actual successor
  leaves no joins between distinct maximal fixed-carrier runs.
* The exact \(q=2\) parenthesis theorem bounds the physical shallow
  crossing catalogue by \(6J=o(W)\), but turning that catalogue into a
  repair after erosion deletion is conditional on ERP\(_H\). It controls
  only two arm classes per Gaussian sector and does not repair the
  \(q\ge3\) crossing ledger.

What remains is exactly one of the following two statements.

1. **Positive crossing braid.** Construct one literal block word which
   uses the pin-cap compatibility (3.6) to share
   \(\sum s-o(\sum s)\) sector certificates while retaining, or replacing
   by equal-OR witnesses, all old \(q\ge3\) crossing targets, and prove
   ERP\(_H\) for the deleted erosion indices. Its new positions beyond the
   deleted PBBS baseline must be \(o(\sum s)\).

2. **Negative overlap theorem.** Prove from canonical PBBS parenthesis
   chronology that every legal common-letter family in (3.6), after the
   actual owner-successor constraints are imposed, leaves
   \(\Omega(\sum s)\) certificate classes unshared.

The present theorem closes isolated sector-local owner-slot replacement
and the displayed fixed-carrier chronology-preserving port splice, while
proving the strongest available packet-interior positive primitive. It
does not yet certify deletion of the principal erosion letters, and it
neither proves nor refutes the remaining noncellular cross-packet braid.
