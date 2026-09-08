# Lane S: ballot-cycle atoms after the exterior-geodesic correction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## Supersession note

The endpoint filter in this report remains valid, but its original
physical \(C_6\) boundary was later superseded positively.
MATH_THEOREM_SMALLEST_MOVING_EXTERIOR_C6_PACKET_20260726.md constructs a
literal \(e=1\) moving-exterior \(C_6\) with complete collars, and
MATH_THEOREM_PAIRED_C6_STAR_TO_STAR_PACKET_20260726.md constructs its
literal paired star-to-star completion. The statements below that the
endpoint-compatible bank by itself does not construct a packet should not
be read as denying those later local packets.

Their proposed three-reservoir tetrahedral repetition is ruled out in
MATH_ATTACK_S_TETRAHEDRAL_C6_STORAGE_INVARIANT_20260726.md. No
constant-one or positive-density installation follows merely from the
local packets.

## 0. Audited verdict

Let \(J\) have size \(2r\). The ballot-forced functional-cycle bank has to
be separated into three levels.

1. A directed cycle in one incidence matching is only a certificate.
2. If the opposite half-edges are unused by the other incidence matching,
   toggling the cycle gives an exact integral open path ledger. It may
   permute the terminal root labels and may change individual row lengths.
3. Such an open ledger is a literal contiguous segment of a minimum
   ambient wreath only if every resulting row is an ambient Johnson
   geodesic and all ambient lower states, upper union-colours, and crossing
   collars are owned exactly once.

The correction acts at level 3 and is decisive.

For a clean cycle with old roots \(R_0,\ldots,R_{\ell-1}\), cut phases
\(t_0,\ldots,t_{\ell-1}\), and the convention that the root \(R_{i+1}\)
receives the old suffix of \(R_i\), put

\[
                  k_i=|R_{i+1}\setminus R_i|.
\]

If all switched rows share one exterior change
\(O_L\longrightarrow O_R\), where

\[
                  e=|O_L\setminus O_R|,
\]

then endpoint geodesicity forces, for every \(i\),

\[
 \boxed{e=t_{i+1}-t_i+k_i.}                            \tag{0.1}
\]

Consequently

\[
 \boxed{\ell e=\sum_{i=0}^{\ell-1}k_i.}                \tag{0.2}
\]

This is an exact common-exterior filter. Passing it certifies only endpoint
metric compatibility, not a physical packet.

The explicit canonical suffix \(C_8\) bank fails (0.1). In root order its
four required exterior motions are

\[
                         (1,3,0,1).                    \tag{0.3}
\]

Equivalently, its four local displacements sum to \(5\), so (0.2) would
give \(4e=5\). Therefore none of its
\(\operatorname {Cat}_{r-3}\) switches is a common-exterior geodesic
packet. Allowing the four strands separate exterior motions makes the
endpoint metrics individually consistent, but a full fourfold orbit then
has positive total exterior motion and cannot return to the same physical
exterior on one ambient geodesic.

There is a currently known surviving endpoint-metric seed. The
noncanonical root-phase \(C_6\) bank has three displacements equal to
\(1\), so (0.1) holds with \(e=1\). This bank count alone does not install
a packet. The later smallest moving-exterior theorem realizes the same
metric mechanism locally. Equation (0.1) identifies the exact
exterior deletion/insertion menus that a construction would have to use.
Moreover, a later inverse exterior motion cannot restore the original
physical exterior inside one global geodesic. Exterior changes on a fixed
coordinate shore are monotone and add:

\[
 \sum_j |O_{j-1}\setminus O_j|=|O_0\setminus O_k|.     \tag{0.4}
\]

Thus \(O_k=O_0\) forces every summand to vanish. The later local \(C_6\)
packets move the boundary and prove their collars explicitly. Their
installation or repetition still requires a larger global construction.

No carrier improvement, positive-density atlas, or constant-one theorem
is claimed here.

## 1. What the ballot bank actually supplies

Let \(F\) be an oriented rooted path factor of the middle-levels inclusion
graph

\[
       M(J)=\binom Jr\sqcup\binom J{r+1}.
\]

At every nonterminal lower vertex, distinguish the selected outgoing
incidence from the selected incoming incidence. A functional-cycle
certificate uses selected outgoing incidences and the opposite incidences
at their upper endpoints.

### Proposition 1.1 (full-factor alternation test)

Let \(F\) be an untwisted \(r\)-step port factor, so each rooted row is a
complement geodesic. For a directed functional cycle over one fixed
\((r-1)\)-core, the lifted incidence cycle is alternating in the full
factor if and only if its selected lower states lie on pairwise distinct
rooted paths. In particular, this applies to the canonical
Chung--Feller factor.

#### Proof

If two successive selected states lie on the same rooted path, the
proposed opposite half-edge at their common upper vertex is exactly the
selected incoming incidence of that path. It therefore cannot be inserted
by an alternating toggle.

Conversely, if a proposed opposite half-edge is already selected incoming,
its lower endpoint is the successor state of the selected outgoing edge
on the same rooted path. Hence two selected states of the functional cycle
lie on that path. Conversely, all lower states over one fixed core are
pairwise Johnson-adjacent. If two lie on one complement geodesic, the
subpath between them is geodesic of Johnson distance one, so they occur at
consecutive phases. The later state is therefore the down-successor of
the earlier selected outgoing incidence (or conversely), so the two are
adjacent under the outgoing functional map and the corresponding opposite
half-edge is selected incoming. Thus a repeated root is equivalent to a
blocked opposite half-edge. With
pairwise distinct roots, every removed incidence and every inserted
incidence alternates around the cycle, and the standard clean strand
splice applies. \(\square\)

The ballot count

\[
 Z_r=\frac{r(r-1)}{r+2}\operatorname {Cat}_r           \tag{1.1}
\]

therefore counts eligible outgoing-matching certificates, not actual
factor switches for an arbitrary host factor.

There is no folded rescue supported on one blocked simple cycle. Write its
two alternating edge shores as \(C=A\mathbin{\dot\cup}B\), where every
edge of \(A\) is a selected outgoing edge of \(F\). Every nonzero signed
degree-zero vector supported on \(C\) is a nonzero scalar multiple of
\(\mathbf1_A-\mathbf1_B\). The direction which removes \(A\) and adds
\(B\) is feasible only if \(B\cap F=\varnothing\); a blocked opposite
edge makes it infeasible. The reverse direction tries to add every already
selected edge of \(A\), and is also infeasible. Hence no nonzero
cycle-supported incidence-set switch exists. Folded \(C_6\) or \(C_8\)
atoms require additional support outside that outgoing functional cycle.

## 2. The exact abstract splice ledger

Assume first that every old rooted path has \(r\) Johnson exchanges.
Let a clean alternating incidence cycle meet the path rooted at \(R_i\)
at lower-state phase \(t_i\), where \(0\le t_i\le r-1\). Orient the cycle so
that the new path rooted at \(R_{i+1}\) receives the suffix of the old path
rooted at \(R_i\). Indices are modulo \(\ell\).

### Lemma 2.1 (row length and endpoint action)

The new path rooted at \(R_{i+1}\) has endpoint
\(J\setminus R_i\) and semilength

\[
                q_{i+1}=r+t_{i+1}-t_i.                \tag{2.1}
\]

In particular,

\[
                \sum_{i=0}^{\ell-1}q_i=\ell r.         \tag{2.2}
\]

#### Proof

The retained prefix contains \(t_{i+1}\) old exchanges. The attached
suffix contains \(r-t_i\) old exchanges. Their sum is (2.1), and the
suffix ends at the old terminal \(J\setminus R_i\). Summing (2.1) around
the cycle telescopes the phase differences. \(\square\)

Thus a clean cycle preserves every local \(X/Y\) vertex integrally and is
orbit-length balanced. Neither fact implies ambient geodesicity.

There is also a carrier warning. If a purported serial gain is obtained
only by reassigning a row-local additive vector \(v\) under a finite-order
twist \(\tau\), then its one-slab difference is a coboundary

\[
                         d=(\tau_*-I)v.
\]

If \(\tau^h=I\), the orbit sum is

\[
 \sum_{j=0}^{h-1}\tau_*^j d
   =(\tau_*^h-I)v=0.                                  \tag{2.3}
\]

Hence abstract orbit repetition can retain a useful signed load only
through a non-row-local term, such as a crossing collar or a genuinely
moving exterior. That term must be computed literally.

## 3. Exact mixed-phase exterior compatibility

Let \(O_L,O_R\) be equally sized subsets of coordinates outside \(J\).
Assume that \(O_L\cup P\) and \(O_R\cup(J\setminus Q)\) are ambient
middle sets of the same size. Put

\[
                         e=|O_L\setminus O_R|.
\]

### Theorem 3.1 (distance decomposition)

For all \(P,Q\in\binom Jr\),

\[
 \boxed{
 d_J\bigl(O_L\cup P,\,
          O_R\cup(J\setminus Q)\bigr)
                 =e+|P\cap Q|
                 =e+r-|P\setminus Q|.}                \tag{3.1}
\]

#### Proof

The elements of the first endpoint absent from the second are the
disjoint union

\[
            (O_L\setminus O_R)\mathbin{\dot\cup}(P\cap Q).
\]

Johnson distance between equal-sized sets is the size of this difference,
which gives (3.1). \(\square\)

### Theorem 3.2 (mixed-phase cycle filter)

In the setting of Lemma 2.1, suppose all switched paths are to be
contiguous subpaths of minimum ambient wreaths with the same exterior
pair \((O_L,O_R)\). Then for every \(i\),

\[
 \boxed{
 e=t_{i+1}-t_i+|R_{i+1}\setminus R_i|.}                \tag{3.2}
\]

Consequently,

\[
 \boxed{
 \ell e=\sum_{i=0}^{\ell-1}|R_{i+1}\setminus R_i|.}    \tag{3.3}
\]

Conversely, (3.2) is sufficient only for the existence of some ambient
geodesic between each pair of displayed endpoints. It is not sufficient
for simultaneous \(X/Y\)-ownership or for the specified splice to be
literal.

#### Proof

The row rooted at \(R_{i+1}\) has, by Lemma 2.1, length

\[
                         r+t_{i+1}-t_i
\]

and endpoint \(O_R\cup(J\setminus R_i)\). Every contiguous subpath of a
minimum wreath is geodesic. By Theorem 3.1 its endpoint distance is

\[
                         e+r-|R_{i+1}\setminus R_i|.
\]

Equating length and distance gives (3.2). Summing (3.2) over the cycle
telescopes the phase differences and proves (3.3).

If (3.2) holds, the displayed endpoint distance equals the prescribed
length, so an abstract shortest Johnson path between those two endpoints
exists. Nothing in the distance equation coordinates different rows or
their upper union-colours. \(\square\)

### Corollary 3.3 (fixed-exterior rigidity)

If \(O_L=O_R\), then every cycle satisfying Theorem 3.2 has

\[
                         R_{i+1}=R_i
\]

for every \(i\). In particular, no nonidentity clean twist occurs in a
fixed-exterior slab.

#### Proof

Equation (3.3) has a zero left side and a sum of nonnegative integers on
the right. Hence every set difference vanishes; equal cardinalities give
equality of the roots. Equation (3.2) then also forces equal cut phases.
\(\square\)

### Corollary 3.4 (exact exchange menus)

Whenever one switched row of length \(q\) passes the endpoint-metric test,
every ambient geodesic between its endpoints deletes exactly

\[
 (O_L\setminus O_R)\mathbin{\dot\cup}(P\cap Q)         \tag{3.4}
\]

and inserts exactly

\[
 (O_R\setminus O_L)\mathbin{\dot\cup}
             \bigl(J\setminus(P\cup Q)\bigr).          \tag{3.5}
\]

Each displayed menu has size

\[
                         e+|P\cap Q|=q.
\]

These occurrencewise menus, not the abstract local palette alone, are the
input to any crossing-collar proof.

## 4. The canonical suffix \(C_8\) bank is physically excluded

The explicit rank-three alternating cycle is

\[
 124-1246-146-1456-145-1345-134-1234-124.             \tag{4.1}
\]

Its four old root strands and local phases are

\[
\begin{array}{c|c}
R_0=124&0\\
R_1=123&2\\
R_2=125&1\\
R_3=134&0.
\end{array}                                            \tag{4.2}
\]

Suspending after a Dyck prefix of semilength \(r-3\) shifts every phase by
\(r-3\). Thus

\[
 (t_0,t_1,t_2,t_3)=(r-3,r-1,r-2,r-3).                \tag{4.3}
\]

The endpoint permutation is

\[
 R_0\mapsto R_3,\qquad
 R_1\mapsto R_0,\qquad
 R_2\mapsto R_1,\qquad
 R_3\mapsto R_2.                                      \tag{4.4}
\]

The switched row lengths, root displacements, and exterior requirements
are therefore

\[
\begin{array}{c|c|c|c}
\text{root}&q(R)&|R\setminus\tau(R)|&
q(R)-|R\cap\tau(R)|\\ \hline
R_0&r&1&1\\
R_1&r+2&1&3\\
R_2&r-1&1&0\\
R_3&r-1&2&1.
\end{array}                                            \tag{4.5}
\]

### Theorem 4.1 (common-exterior \(C_8\) no-go)

For every \(r\ge3\), no member of the suffix \(C_8\) family is realizable
as the displayed switched paths inside a slab having one common pair of
exteriors.

#### Proof

The four rows in (4.5) require \(e=1,3,0,1\), respectively. A common
exterior pair has one value of \(e\), so it cannot satisfy all four.
Equivalently, the displacements in (4.5) sum to \(5\), whereas (3.3)
would require \(4e=5\). \(\square\)

The exact bank size is

\[
 \operatorname {Cat}_{r-3}
 =\frac{r(r-1)(r+1)}
 {8(2r-1)(2r-3)(2r-5)}\operatorname {Cat}_r
 =\left(\frac1{64}+O(r^{-1})\right)\operatorname {Cat}_r. \tag{4.6}
\]

It touches

\[
 4\operatorname {Cat}_{r-3}
   =\left(\frac1{16}+O(r^{-1})\right)\operatorname {Cat}_r \tag{4.7}
\]

rows. These constants remain valid as an abstract path-ledger occurrence
theorem. They supply zero certified literal twisted packets.

Allowing row-dependent exterior pairs would require, in root order, the
four separate motions in (4.5), together with the four distinct deletion
and insertion menus (3.4)--(3.5). That is a new ambient packet, not a
local substitution. In particular, the equality of the abstract local
\(X/Y\) ledger does not prove equality of the ambient upper colours,
because the exterior carried by an intermediate local colour is now
row- and time-dependent.

## 5. Exterior motion cannot be restituted inside a geodesic

The abstract proposal also used finite-order serial repetition to cancel
endpoint monodromy. The following invariant shows why an inverse exterior
move cannot be hidden later in the same fixed-support packet.

### Lemma 5.1 (coordinate monotonicity)

Let

\[
                         S_0,S_1,\ldots,S_L
\]

be a geodesic in a Johnson graph from \(A=S_0\) to \(B=S_L\). Then every
coordinate has monotone membership along the path:

1. a coordinate in \(A\setminus B\) is deleted exactly once and never
   reinserted;
2. a coordinate in \(B\setminus A\) is inserted exactly once and never
   deleted;
3. a coordinate in \(A\cap B\) remains present; and
4. a coordinate outside \(A\cup B\) remains absent.

#### Proof

The path length is \(d_J(A,B)\). At every step the distance to \(B\) must
drop by exactly one; otherwise the remaining number of steps could not
reach \(B\). Hence each step deletes an element outside \(B\) and inserts
an element of \(B\). The four assertions follow. \(\square\)

### Theorem 5.2 (exterior additivity and no restitution)

Fix a coordinate subset \(E\), choose times

\[
                  0=u_0<u_1<\cdots<u_k=L,
\]

and put \(O_j=S_{u_j}\cap E\). Then

\[
 \boxed{
 \sum_{j=1}^k |O_{j-1}\setminus O_j|
                  =|O_0\setminus O_k|,
 \qquad
 \sum_{j=1}^k |O_j\setminus O_{j-1}|
                  =|O_k\setminus O_0|.}               \tag{5.1}
\]

In particular, if \(O_k=O_0\), then \(O_j=O_0\) for every \(j\).

#### Proof

By Lemma 5.1, once an \(E\)-coordinate leaves the path state it never
returns. Hence the sets

\[
                         O_{j-1}\setminus O_j
\]

are pairwise disjoint, and their union is exactly
\(O_0\setminus O_k\). The inserted differences are likewise pairwise
disjoint and have union \(O_k\setminus O_0\). This proves (5.1). If
\(O_k=O_0\), both right sides are zero, so every difference is empty and
\(O_j=O_0\). \(\square\)

### Corollary 5.3 (inverse-monodromy repetition does not repair geometry)

Suppose several serial slabs lie on one ambient minimum wreath and use a
fixed exterior coordinate shore \(E\). If slab \(j\) requires positive
exterior motion \(e_j=|O_{j-1}\setminus O_j|\), then

\[
                         |O_0\setminus O_k|
                              =\sum_j e_j.             \tag{5.2}
\]

Thus endpoint permutations may multiply to the identity while exterior
motion cannot cancel. A packet with the same physical exterior at entrance
and exit has \(e_j=0\) in every constituent slab.

This applies before any carrier calculation. A rotating-frame construction
can evade the statement only by changing which coordinates belong to the
local interface or by exporting a nonzero net boundary displacement.
Either change requires a new full ambient factor and its crossing collars;
it is not serial composition of ordinary local holes.

### Corollary 5.4 (a complete clean-cycle orbit has positive exterior drift)

Let a nontrivial clean \(\ell\)-cycle be realized serially so that one
physical row traverses a complete orbit of its root labels. Permit the
exterior motion to depend on the current root, but keep one fixed physical
exterior shore \(E\), and suppose every stage lies on one ambient
geodesic. If the stage associated with transition \(i\) has motion

\[
                         e_i=t_{i+1}-t_i+k_i,
 \qquad k_i=|R_{i+1}\setminus R_i|,
\]

then

\[
 \boxed{\sum_{i=0}^{\ell-1}e_i
                  =\sum_{i=0}^{\ell-1}k_i>0.}          \tag{5.3}
\]

Consequently the exterior restriction after the orbit cannot equal its
restriction before the orbit.

#### Proof

The phase differences telescope. Every two adjacent roots of a nontrivial
clean cycle are distinct, so every \(k_i\ge1\), proving strict positivity.
Theorem 5.2 identifies the left side with the net number of physical
exterior coordinates deleted over the orbit. If the entrance and exit
restrictions were equal, that number would be zero. \(\square\)

For the suffix \(C_8\), the root-order motions
\((1,3,0,1)\) sum to \(5\). Thus even the row-dependent metric repair
cannot be closed by the formal order-four repetition on one fixed physical
shore.

## 6. A metric-compatible seed: root-phase \(C_6\)

Let \(|K|=r-1\), choose distinct \(a,b,c\notin K\), and put

\[
 P_a=K+a,\qquad P_b=K+b,\qquad P_c=K+c.
\]

Assume these three petals are the actual rooted-path labels and that their
selected incidences are the phase-zero outgoing edges. This is exactly the
situation in the explicit noncanonical host bank below. For a hexagon at a
later common phase, the petals are cut states rather than root labels, and
the following displacement calculation need not hold.

The alternating hexagon

\[
 P_a-(K+a+b)-P_b-(K+b+c)-P_c-(K+c+a)-P_a             \tag{6.1}
\]

cyclically splices the three root strands at phase zero. In one
orientation,

\[
 \tau(P_a)=P_c,\qquad
 \tau(P_b)=P_a,\qquad
 \tau(P_c)=P_b.                                       \tag{6.2}
\]

Every row retains length \(r\), and

\[
 |P_u\setminus\tau(P_u)|=1
 \qquad(u=a,b,c).                                     \tag{6.3}
\]

Therefore Theorem 3.2 passes exactly with

\[
                         e=1.                         \tag{6.4}
\]

Write

\[
                  D=J\setminus(K\cup\{a,b,c\}),
                  \qquad |D|=r-2,
\]

and suppose

\[
 O_L\setminus O_R=\{x\},\qquad
 O_R\setminus O_L=\{y\}.
\]

Corollary 3.4 gives the exact endpoint menus:

\[
\begin{array}{c|c|c}
\text{root}&\text{deleted coordinates}&\text{inserted coordinates}\\ \hline
P_a&K\cup\{x\}&D\cup\{b,y\}\\
P_b&K\cup\{x\}&D\cup\{c,y\}\\
P_c&K\cup\{x\}&D\cup\{a,y\}.
\end{array}                                            \tag{6.5}
\]

The metric equation guarantees that an individual geodesic with each menu
exists. It does not say that the three paths partition the ambient lower
states or their adjacent-union colours. Notice in particular that a
moving exterior destroys the fixed local rank: during a path, an exchange
may transfer cardinality between \(J\) and its exterior. The ordinary
middle-levels \(X/Y\) partition therefore cannot simply be adjoined to one
common spectator.

There is an explicit noncanonical host factor containing

\[
                         \operatorname {Cat}_{r-3}     \tag{6.6}
\]

pairwise vertex-disjoint phase-zero clean hexagons. It touches

\[
 3\operatorname {Cat}_{r-3}
   =\left(\frac3{64}+O(r^{-1})\right)\operatorname {Cat}_r \tag{6.7}
\]

rows. Equations (6.4)--(6.5) upgrade this only to a positive-density bank
of endpoint-metric-compatible seeds.

Three coherently oriented abstract copies have \(\tau^3=I\). If one tries
to realize them serially with one fixed exterior shore and then restore
the entrance exterior, each copy requires \(e=1\), while Theorem 5.2
requires

\[
                         0=|O_0\setminus O_3|=1+1+1,
\]

a contradiction. Thus the order-three repetition is not a closed literal
packet.

## 7. Exact proved and conditional boundary

The following statements are proved.

1. The full-factor alternation test rejects every folded member of the
   outgoing functional bank and accepts exactly its clean members.
2. The clean suffix \(C_8\) family has exactly
   \(\operatorname {Cat}_{r-3}\) pairwise disjoint abstract switches and
   affects \(4\operatorname {Cat}_{r-3}\) rows.
3. Every common-exterior mixed-phase cycle must satisfy (3.2), hence the
   divisibility and average-displacement law (3.3).
4. The suffix \(C_8\) violates that law: its required exterior motions are
   \((1,3,0,1)\).
5. Exterior motion is additive and cannot be undone later on a minimum
   wreath with a fixed coordinate shore.
6. The noncanonical root-phase \(C_6\) bank passes the endpoint test with
   \(e=1\), and its complete endpoint menus are (6.5).

The following statements remain unproved and are not inferred.

1. No positive-density installation of the root-phase \(C_6\) bank with
   exact global lower, upper-colour, and crossing-collar ownership is
   constructed here. Later reports do construct bounded local packets.
2. No carrier gain follows from the \(C_6\) bank. Its aggregate
   first-insertion and first-deletion marginals cancel; only a
   row-resolved crossing term could survive.
3. A rotating-frame construction with overlapping local coordinate sets
   is not ruled out by Theorem 5.2, but it must be presented as one global
   geodesic factor, not as independently valid twisted slabs.
4. The abstract ballot-cycle bank gives no contribution to
   coefficient one until one of those literal constructions is supplied.

## 8. Independent audit points

The decisive calculation was checked in both indexing conventions.

In receiving-root order \(R_1,R_2,R_3,R_0\), the suffix \(C_8\) requires

\[
                         (3,0,1,1).
\]

In the fixed root order \(R_0,R_1,R_2,R_3\), used in (4.5), this is

\[
                         (1,3,0,1).
\]

The apparent difference is only a cyclic reindexing.

The no-restitution theorem uses geodesicity, not merely simplicity. It
would be false for an arbitrary nonminimum Johnson walk, because such a
walk may delete and later reinsert a coordinate. Every row relevant to a
minimum wreath is geodesic, so the hypothesis is exactly the required one.
Here the exterior \(E\) is a fixed physical coordinate subset on one
geodesic half of the wreath. Equality only after a coordinate or row
relabeling is insufficient, and the statement is not applied across the
cyclic closing edge. A genuinely moving-front packet which exits with a
different physical exterior is not obstructed by Theorem 5.2.

Finally, all positive counts in this note are counts of abstract
alternating-cycle occurrences or endpoint-compatible seeds. None is
silently promoted to a literal OR word.
