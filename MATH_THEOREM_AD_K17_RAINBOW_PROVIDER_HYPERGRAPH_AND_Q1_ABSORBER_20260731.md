# Rainbow provider hypergraphs, protected cut banks, and the exact q1 absorber

Date: 2026-07-31  
Lane: AD  
Status: proved reductions and audited finite parameters; no claim that
`nu(17)=24313` is made

## 0. Result and exact boundary

The K17 deep-provider gate is positive at the level requested here.  For the
authenticated 11-component source factor, all 1,838 missing deep upper masks
can be served simultaneously by one-seam Johnson witnesses having

* pairwise distinct departure tails;
* pairwise distinct arrival heads;
* pairwise distinct lower seam colours;
* every seam colour activated by a selected source cut; and
* every selected protected suffix/prefix span disjoint from every selected
  endpoint cut.

The stronger certificate is

    scratch/k17_fragment_endpoint_matching_recycle_protected_20260731.result.json
    SHA-256 3db9e5fc4a6bd9ab467e895de70a75c60376fff016661b6a18ec006900ab5d8a.

Its independent replay is

    scratch/k17_fragment_endpoint_matching_recycle_protected_independent_20260731.audit.json
    SHA-256 d8fe0599568bc58cd4865a92b95bd5c45256716f48111a2c2bfed491f8099b6a.

The producer result's free-text scope is stale: its authoritative booleans
`matching_recycle_lower=true` and `matching_protected_spans=true`, its stored
protected rows, and the independent replays establish the two properties.
Its embedded payload hash is legacy/non-replayable because integer histogram
keys were normalized only after persistence; the file SHA and independent
audits are the provenance anchors.  The producer's duplicated diagnostic
gain increment and unused `rejected_q1_cut_arcs` counter do not enter the
candidate catalogue, constraints, assignment, or any count used below.

This is not yet an installable K17 path.  Its 3,336 forced endpoint cuts miss
one source 3-cycle.  Opening that cycle gives a 3,337-edge cut bank and 1,498
available filler seams, whereas the retained source edges plus the selected
service seams still miss 1,864 rank-ten colours.  Thus the minimum-cut
absorber has the exact deficit

\[
                         1864-1498=366.                 \tag{0.1}
\]

Any seam-only carrier completion of this fixed service selection therefore
needs at least 366 additional safe cuts, even under the optimistic assumption
that those cuts create no new q1 debt.  This does not exclude q1 restitution
by later boundary/compiler cells or reselection of service providers.  It is
a minimum-reservoir obstruction, not a no-go for the full provider bank.

The exact frozen canonical-bank census also closes the three generic
sufficient tests asked for in this lane:

* the direct Haxell `2 Delta` test fails: `82 < 2*548=1096`;
* the uniform dependency-graph LLL charge test fails:
  `2.0936704988826498 > 1/(2e)`;
* the elementary degree consequence of Aharoni--Haxell fails:
  `82 < 1770`.

Failure of a sufficient test is not an impossibility theorem.  The explicit
protected four-resource certificate proves that the service transversal
itself exists despite those failures.

## 1. Exact provider object

### 1.1 Source factor

Let \(F\) be an oriented Johnson 2-factor on a set \(V\) of rank-\(r\)
owners.  Write its successor permutation as

\[
                         \sigma:V\longrightarrow V.
\]

Assume that \(F\) is lower-rainbow: the map

\[
             \lambda(v)=v\cap\sigma(v)                 \tag{1.1}
\]

is a bijection from \(V\) onto the required rank-\((r-1)\) lower colours.
We index the source edge \(v\to\sigma(v)\) by its tail \(v\).

Let \({\cal H}\) be the set of upper targets not internally witnessed by
the disjoint source components.  At the present K17 source,

\[
 |V|=24310,\qquad |{\cal H}|=1838.                      \tag{1.2}
\]

### 1.2 Occurrence-specific provider

A provider for \(Z\in{\cal H}\) is a tuple

\[
                 p=(Z,a,b,K(p)),                        \tag{1.3}
\]

with the following data.

1. \(a,b\in V\), and \(a\to b\) is a directed Johnson seam.
2. A suffix state ending at \(a\) and a prefix state beginning at \(b\)
   have OR exactly \(Z\).
3. \(K(p)\subseteq V\) is the set of source-edge tails that must remain
   uncut for that literal suffix/prefix witness and its local run guard.
4. The seam itself passes the stated run-1/run-2 local test.

Define its typed resources

\[
 \begin{split}
  t(p)&=a,\\
  h(p)&=b,\\
  z(p)&=\sigma^{-1}(b),\\
  c(p)&=a\cap b,\\
  d(p)&=\lambda^{-1}(c(p)).
 \end{split}                                             \tag{1.4}
\]

Here \(z(p)\) is the source edge whose deletion frees the arrival head
\(b\), and \(d(p)\) is the unique source edge owning the lower colour added
by the seam.  Exact lower-colour recycling forces that donor edge to be cut.
Consequently the physical forced-cut footprint of \(p\) is

\[
                       D(p)=\{t(p),z(p),d(p)\}.          \tag{1.5}
\]

The three entries in (1.5) need not be distinct.  An individually usable
provider must satisfy

\[
                       D(p)\cap K(p)=\varnothing.        \tag{1.6}
\]

The complete audited K17 catalogue has no record failing (1.6).

### 1.3 Four-resource matching and signed conflicts

Ignoring the target part, a provider gives the three-resource edge

\[
                \{t(p)_{\rm out},z(p)_{\rm in},d(p)_{\rm col}\}  \tag{1.7}
\]

on three disjoint copies of the source-edge index set.  Equivalently,
including its target, it is a four-partite hyperedge on

\[
       \{\hbox{target},\hbox{tail},\hbox{arrival},
                         \hbox{lower-colour owner}\}.
\]

Two provider records for different targets are incompatible when they share
a tail, an arrival, or a lower colour, or when

\[
 D(p)\cap K(q)\ne\varnothing
       \quad\hbox{or}\quad
 D(q)\cap K(p)\ne\varnothing.                            \tag{1.8}
\]

The signs in (1.8) matter.  An overlap \(K(p)\cap K(q)\) is harmless: both
records ask that the same source edge be retained.  Therefore representing
every protected edge as an ordinary capacity-one matching resource is
soundly sufficient but is not equivalent; it discards compatible pairs.

## 2. Fixed-cut normalization

The positive donor activation in (1.5) prevents the unrestricted provider
problem from being an ordinary hypergraph matching.  It becomes one after a
cut bank is fixed.

### Theorem 2.1 (fixed-cut provider normalization)

Fix \(S\subseteq V\).  For each target \(Z\), let \({\cal P}_Z(S)\) be the
3-uniform hypergraph whose edges are (1.7) for providers satisfying

\[
                  D(p)\subseteq S,qquad K(p)\cap S=\varnothing.   \tag{2.1}
\]

If the family \((\mathcal P_Z(S):Z\in\mathcal H)\) has a rainbow matching,
then all targets in \(\mathcal H\) have simultaneous literal providers with
distinct tails, arrivals, and lower colours, and every selected protected
span survives cutting \(S\).

Conversely, every simultaneous provider family whose complete physical cut
bank is \(S\) gives such a rainbow matching.

#### Proof

The three copies in (1.7) turn distinct tails, arrivals and colours into
ordinary vertex-disjointness.  Condition (2.1) both activates every donor
and makes all signed conflicts impossible, since every actual cut lies in
\(S\) and every selected protected set avoids \(S\).  Conversely, any
physical installation with cut bank \(S\) necessarily satisfies (2.1), and
its three typed projections are injective. \(\square\)

This is the correct way to handle protected spans.  It neither treats
keep--keep overlap as a conflict nor postpones an unrecorded cut--keep test.

## 3. Exact residual filler theorem

Let \(M\) be a rainbow service matching from Theorem 2.1.  Put

\[
 A=\{t(p):p\in M\},\quad
 B=\{z(p):p\in M\},\quad
 C=\{d(p):p\in M\}.                                     \tag{3.1}
\]

All three sets have size \(|M|\) and are subsets of \(S\).  After cutting
the source edges indexed by \(S\), define the residual shores

\[
 \begin{split}
 L&=S\setminus A,\\
 R&=\sigma(S\setminus B),\\
 Q&=\lambda(S\setminus C).
 \end{split}                                             \tag{3.2}
\]

They have the common size

\[
                       f=|S|-|M|.                        \tag{3.3}
\]

A residual filler seam \(x\to y\) supplies the triple

\[
                     (x,y,x\cap y)\in L\times R\times Q. \tag{3.4}
\]

### Theorem 3.1 (cyclic and linear filler equivalence)

Assume all selected seams are locally admissible and all required protected
sets avoid \(S\).

1. A perfect matching of the residual hypergraph (3.4) is equivalent to a
   completion, without additional cuts, to a spanning directed 2-factor
   having the exact original lower-colour palette.
2. If \(f\ge1\), to obtain a spanning directed path, choose one terminal
   element of \(L\), one initial element of \(R\), and one omitted boundary
   colour of \(Q\).
   A matching of the remaining \(f-1\) elements is degree- and
   lower-palette-exact.  It is one path if and only if the resulting partial
   successor graph is acyclic.

#### Proof

Every cut source edge creates one free outgoing tail and one free incoming
head.  The service seams consume precisely \(A\) and \(\sigma(B)\); hence
the unconsumed ports are (3.2).  The deleted lower colours are
\(\lambda(S)\), while the service seams restore \(\lambda(C)\); hence the
missing colours are exactly \(Q\).  A perfect three-shore matching consumes
each remaining port and colour once, proving the cyclic assertion in both
directions.

For a linear path exactly one outgoing tail, one incoming head, and the one
standard boundary lower colour remain unused.  Degree at most one then gives
a disjoint union of directed paths and cycles.  It is one spanning path
exactly when no directed cycle remains. \(\square\)

### 3.2 Immediate-upper tasks

Let \({\cal U}(S,M)\) be the rank-\((r+1)\) targets missing after retaining
all source edges outside \(S\) and adding the service seams in \(M\).  Put

\[
                          q=|{\cal U}(S,M)|.              \tag{3.5}
\]

Every Johnson filler seam supplies exactly one such union.  Therefore a
necessary condition for a linear completion is

\[
                          q\le f-1.                       \tag{3.6}
\]

Assume \(f\ge1\).  When (3.6) holds, form \(f-1\) tasks: the \(q\) real missing targets and
\(f-1-q\) dummy tasks.  After fixing the terminal, initial and omitted-colour
resources, give a real task \(U\) precisely those triples (3.4) satisfying

\[
                            x\cup y=U,                    \tag{3.7}
\]

and give a dummy task every otherwise admissible filler.  A rainbow matching
saturating these tasks is equivalent to simultaneous degree, lower-colour
and q1 completion.  Adding acyclicity is equivalent to obtaining one path.

This task hypergraph is the exact residual q1 absorber.  It is not captured
by three independent endpoint, colour and q1 matchings.

### Corollary 3.2 (seam-only additional-cut lower bound)

Suppose a cut bank \(S_0\) leaves \(q_0\) q1 targets missing and has
\(f_0-1\) linear filler slots.  If \(A\subseteq V\setminus S_0\) is any new
cut set disjoint
from every selected protected span, then every completion using only the
resulting carrier seams to restore q1 satisfies

\[
       |{\cal U}(S_0\cup A,M)|\le f_0-1+|A|.              \tag{3.8}
\]

Since cutting more source edges cannot restore a missing q1 target before
fillers are added,

\[
             |A|\ge q_0-(f_0-1)                          \tag{3.9}
\]

whenever the right side is positive.

#### Proof

Each additional cut creates at most one additional filler-seam slot, and
each filler seam has one rank-\((r+1)\) union.  This proves (3.8).  The
monotonicity of retained source coverage gives (3.9). \(\square\)

## 4. Matching theorems: exact applicability

### 4.1 Aharoni--Haxell

We use the following imported theorem.

> **Aharoni--Haxell rainbow-matching theorem (rank three).**  If
> \(\mathcal G_1,\ldots,\mathcal G_n\) are 3-uniform hypergraphs on a common
> resource set and
> \[
>   \nu\!\left(\bigcup_{i\in I}\mathcal G_i\right)
>                  >3(|I|-1)                              \tag{4.1}
> \]
> for every nonempty \(I\subseteq[n]\), then there are pairwise disjoint
> edges \(g_i\in\mathcal G_i\).

Applied to \(\mathcal P_Z(S)\), this gives the service matching in Theorem
2.1.  It does not supply the residual filler or acyclicity.

For \(I=\mathcal H\), the matching number in (4.1) is at most \(|S|\).
Thus with \(n=1838\), this sufficient theorem requires

\[
                    |S|\ge3(1838-1)+1=5512.              \tag{4.2}
\]

The current protected certificate uses only 3,336 forced cuts, so (4.1)
cannot certify that particular bank.  This does not contradict its explicit
matching: (4.1) is sufficient, not necessary.  Numerically, 5,512 is below
the K17 scalar slack 7,401, so an enlarged-bank Aharoni--Haxell route is not
ruled out by cut cardinality alone.

### Lemma 4.1 (degree consequence of Aharoni--Haxell)

Suppose every target family contains at least \(\delta\) distinct resource
triples,
one resource triple belongs to at most \(\mu\) target families, and the
union resource 3-graph has maximum vertex degree \(\Delta_R\).  Then (4.1)
holds if

\[
                 \delta\ge3\mu(3\Delta_R-2).             \tag{4.3}
\]

#### Proof

For \(|I|=s\), the union contains at least \(\delta s/\mu\) distinct
resource triples.  A greedy hypergraph matching removes at most
\(3\Delta_R-2\) triples per chosen edge, and hence has size at least

\[
            \frac{\delta s}{\mu(3\Delta_R-2)}.
\]

Under (4.3) this is at least \(3s>3(s-1)\), proving (4.1). \(\square\)

For K17, the exact values are

\[
 \delta=82,\qquad \mu=5,\qquad \Delta_R=40,              \tag{4.4}
\]

so the right side of (4.3) is

\[
                 3\cdot5\cdot(3\cdot40-2)=1770.          \tag{4.5}
\]

Thus this degree corollary does not certify K17.  These parameters come from
the unrestricted canonical bank.  An application of Lemma 4.1 to a fixed cut
bank must recompute them after the filter (2.1).

### 4.2 Haxell independent transversals

Without fixing \(S\), put all provider records into the conflict graph
defined by shared typed resources and (1.8), partitioned by target, with all
intra-target conflict edges deleted.  The
imported Haxell `2 Delta` corollary gives an independent transversal when

\[
                 \min_Z|\mathcal P_Z|\ge2\Delta(\Gamma). \tag{4.6}
\]

The exact K17 catalogue has the cross-target degree

\[
       \min_Z|\mathcal P_Z|=82,qquad \Delta(\Gamma)=548. \tag{4.7}
\]

Hence (4.6) asks for 1,096 choices per target and fails.  Again this is only
failure of the generic sufficient condition; the explicit protected
transversal exists.

### 4.3 A self-contained dependency-graph LLL criterion

Let \(\Gamma\) be any provider conflict graph with target parts
\(P_1,\ldots,P_n\).  Choose one provider independently from each \(P_i\),
using probabilities \(x_p\) with

\[
                       \sum_{p\in P_i}x_p=1.             \tag{4.8}
\]

In the following formulas \(q\sim p\) always means a cross-part conflict.
For each such conflict \(pq\), let \(B_{pq}\) be the bad
event that both records are selected.  Define

\[
 Z_i=\sum_{p\in P_i}x_p\sum_{q\sim p}x_q,qquad
 z=\max_i Z_i.                                           \tag{4.9}
\]

### Theorem 4.2 (conflict-mass LLL)

If

\[
                         z\le\frac1{2e},                 \tag{4.10}
\]

then \(\Gamma\) has an independent transversal.

#### Proof

Use the standard asymmetric local lemma in its \(\mu\)-form.  Let
\(\mathcal D\) be the event-dependency graph in which two bad events are
adjacent when they involve a common target choice.  It is enough
to have

\[
 \Pr(B)\le
 \frac{\mu_B}{\prod_{C\in\mathcal D(B)\cup\{B\}}(1+\mu_C)}. \tag{4.11}
\]

If \(z=0\), there are no bad events of positive probability.  Otherwise put

\[
                  \mu_{pq}=\frac{\Pr(B_{pq})}{2z}.
\]

An event \(B_{pq}\), involving target parts \(i,j\), is dependent only on
events involving \(i\) or \(j\).  By (4.9), the total closed-neighborhood
\(\mu\)-mass is at most

\[
 \frac{Z_i+Z_j-\Pr(B_{pq})}{2z}\le1.
\]

Therefore

\[
 \prod_{C\in\mathcal D(B_{pq})\cup\{B_{pq}\}}(1+\mu_C)\le e,
\]

and the right side of (4.11) is at least

\[
             \frac{\Pr(B_{pq})}{2ez}\ge\Pr(B_{pq})
\]

by (4.10).  The local lemma now gives positive probability of avoiding every
conflict. \(\square\)

With the uniform distribution inside each K17 target class, the exact census
gives

\[
  1.218606988622993\le Z_i\le2.0936704988826498,          \tag{4.12}
\]

whereas

\[
                 \frac1{2e}=0.18393972058572117.         \tag{4.13}
\]

Thus this valid coarse dependency-graph LLL criterion fails.  A nonuniform
distribution or a genuinely smaller lopsidependency graph remains
unexcluded.  An LLL conditioned on a uniformly random four-resource matching
would require a negative-dependence theorem not proved here.

### 4.4 Alternating augmentation

The following exact sufficient criterion is useful for finite CEGAR and does
not assume a global degree bound.

### Lemma 4.3 (compatible augmenting chain)

Let \(M\) be a compatible partial transversal and let target \(0\) be
unserved.  Suppose there are distinct matched records
\(m_1,\ldots,m_t\in M\) and pairwise compatible new records
\(p_0,\ldots,p_t\), where \(p_0\) serves target 0 and \(p_i\) serves the
target of \(m_i\) for \(i\ge1\), such that no \(p_i\) conflicts with
\(M\setminus\{m_1,\ldots,m_t\}\).  Then

\[
       M'=(M\setminus\{m_1,\ldots,m_t\})
                           \cup\{p_0,\ldots,p_t\}        \tag{4.14}
\]

is a compatible partial transversal of size \(|M|+1\).

#### Proof

The new records are pairwise compatible, avoid every retained record, and
replace each displaced target exactly once while serving one new target.
Thus (4.14) is compatible and gains one record. \(\square\)

If every proper compatible partial transversal admits such a chain, repeated
augmentation proves a complete transversal.  This is sufficient, not
necessary: a 3-resource hypergraph may require a branching augmenting tree.
No such all-partial-transversal condition has been audited for K17.

## 5. Exact K17 census

The source factor is

    scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
    SHA-256 3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e.

The exact frozen canonical-shortest-witness catalogue has

\[
\begin{array}{c|r}
\text{holes} & 1838\\
\text{safe directed arcs} & 228466\\
\text{target-provider records} & 269968\\
\text{target degree range} & 82\text{--}876\\
\text{maximum provider-record tail/head/colour load} & 53,53,44\\
\text{maximum distinct-triple tail/head/colour degree} & 36,40,33\\
\text{distinct-triple tail--head/tail--colour/head--colour codegree}
    & 1,7,7\\
\text{provider-record tail--head/tail--colour/head--colour load} & 5,12,12\\
\text{target--tail/head/colour codegree} & 16,14,7\\
\text{maximum cut-footprint role-incidence load} & 110\\
\text{maximum protect-site load} & 157\\
\text{exact option-conflict maximum degree} & 548.
\end{array}                                               \tag{5.1}
\]

Alternative protected spans, whether equal-length or longer, are not expanded
as separate records in this census.  Thus the resource triples are complete
for the one-seam arc bank, while the reported signed conflict graph is the
frozen canonical shortest-witness sufficient bank, not a WLOG conflict graph
over every occurrence variant.  The cut-footprint load 110 counts typed
\(D\)-role incidences; the exact conflict computation deduplicates repeated
physical options.

The census is

    scratch/ad_k17_provider_hypergraph_parameters_20260731/
      provider_hypergraph_v6.audit.json
    SHA-256 5943681ad909f156a5a264d03776c6127ca197d10e408bc600479cb63ec260fd
    payload a07537fe0ff9a7dc33bab3a7bca7961057a58ed6f7ddb93f73d1de0b21bf017c.

The replay script is

    scratch/audit_ad_k17_provider_hypergraph_parameters_20260731.py
    SHA-256 d778e9b630378ae3aebdef42a5fa339e4bc8614793d79592fa2f2873db45d7f4.

It ran once on one H100 CPU under a 300-second/2-GiB cap, used 504,532 KiB
maximum resident memory, and finished in 39.19 seconds.  It performs only an
exact catalogue census; it invokes no solver.

### 5.1 Protected service certificate

For the protected certificate, the selected witness spans have histogram

\[
                  4^{1825},\qquad5^{12},\qquad6^1.       \tag{5.2}
\]

Their union contains 6,800 source edges, and their total incidence is 7,366.
The forced endpoint cut bank has

\[
 |A|=|B|=|C|=1838,quad |A\cap B|=340,quad |S|=3336.     \tag{5.3}
\]

All 1,838 service witnesses have \(K(p)\cap S=\varnothing\).  The selected
service partial matching creates no new directed cycle.  However \(S\) hits
only ten of the eleven source components.  The untouched component is

\[
                 (59957,92725,125489),                   \tag{5.4}
\]

and none of its three edge tails is protected.  Cutting any one gives

\[
               |S^*|=3337,qquad
               |S^*|-|M|=1499                           \tag{5.5}
\]

path macros, hence 1,498 filler slots in a final path.

The exact q1 ledger before fillers is

\[
\begin{array}{c|r}
\text{source q1 colours destroyed by }S & 2206\\
\text{distinct q1 unions of 1838 service seams} & 1784\\
\text{service repeat excess} & 54\\
\text{destroyed colours restored by service} & 342\\
\text{q1 colours still missing} & 1864.
\end{array}                                               \tag{5.6}
\]

All three choices in (5.4) delete the same already-duplicated q1 union, so
the last line of (5.6) remains 1,864.  Equations (5.5)--(5.6) prove (0.1).

The independent AD replay is

    scratch/ad_k17_fourresource_provider_matching_protected_20260731.audit.json
    SHA-256 ce3f595ec76930132f15a970a1e18fe4a97f327da66f1944f79e6a2db3a957bf
    payload 56a565228ee5ecec944b8d433de71471c6c388efd00b7c07f5e53f67fe5ea984.

Its script is

    scratch/audit_ad_k17_fourresource_provider_matching_20260731.py
    SHA-256 66730fdd453614f441ff4ba25a66318f61f494e9370f51a71fe9a5cbdb413347.

### 5.2 Precise proved/conditional boundary

Proved for this K17 factor:

1. local safe providers exist for every deep hole;
2. one simultaneous protected four-resource service transversal exists;
3. its minimum cut bank and source-opening correction are exact;
4. its fixed-\(M\), seam-only minimum residual q1 capacity fails by exactly
   366;
5. the three generic sufficient criteria tested on the frozen canonical bank
   do not certify that bank.

Still open:

1. reselect service providers jointly with q1 loss, use boundary/compiler q1
   restitution, or add at least 366 protected-safe cuts and solve the
   enlarged seam-only task absorber;
2. preserve or re-service every previously covered deeper upper target after
   all cuts;
3. make the residual matching order-acyclic and connected;
4. pass the exact global staircase and common-cap compiler.

## 6. All-k zero-defect braid-service lemma

### Theorem 6.1 (sufficient all-k rainbow braid service)

Fix a dimension \(k\), a lower-rainbow directed middle factor \(F_k\), and a
cut bank \(S_k\).  Let \({\cal D}_k\) contain every deep target that would be
missing after the planned cuts, including old targets whose last internal
witness would be destroyed.  Assume:

1. \(S_k\) meets every source component.
2. The fixed-cut provider hypergraphs \(\mathcal P_Z(S_k)\),
   \(Z\in\mathcal D_k\), have a rainbow matching \(M_k\).  It is sufficient,
   for example, that (4.1) hold; a bank of closed provider packets satisfying
   Haxell's `2 Delta` condition is another sufficient hypothesis.
3. Every selected provider span avoids \(S_k\), and every old deep target not
   re-served by \(M_k\) has at least one designated retained witness whose
   protected span avoids \(S_k\).
4. With \(f_k=|S_k|-|M_k|\ge1\), the immediate-upper debt has size at most
   \(f_k-1\), and the exact task hypergraph of Section 3.2 has a rainbow
   matching of size \(f_k-1\).
5. The entire successor graph formed by retained source edges, service seams,
   and filler seams is acyclic (equivalently, the service partial graph is a
   path forest and its contracted filler graph is acyclic).
6. Every seam passes the required local run guard, and the resulting literal
   chronology satisfies the exact staircase and common-cap compiler at total
   length \(B(k)\).

Then the braid is one literal spanning middle path; it services every deep
target in \({\cal D}_k\), preserves every protected old target, restores every
immediate-upper target, and uses every deleted lower colour except the single
prescribed boundary colour exactly once.  The common compiler therefore gives
a universal contiguous-OR word of length \(B(k)\).  Together with the
independent lower bound \(\nu(k)\ge B(k)\),

\[
                           \nu(k)=B(k).                  \tag{6.1}
\]

#### Proof

Theorem 2.1 gives simultaneous literal service with no cut through a selected
or retained protected witness.  Theorem 3.1 and the task matching in Section
3.2 give the exact in/out degrees, lower palette and q1 palette.  Acyclicity
turns the degree-correct cover into one path.  Hypothesis 3 supplies all deep
upper intervals.  Hypothesis 6 is exactly the remaining residence and
integral compiler implication.  Thus the resulting word is literal and
universal at length \(B(k)\); the independent lower bound gives equality.
\(\square\)

Theorem 6.1 is conditional only in its explicitly listed hypotheses.  It
does not assert that Aharoni--Haxell, Haxell, or the uniform LLL verifies any
of those hypotheses at K17.  The exact next finite gate is the q1-aware
enlarged-cut task absorber, followed by old-shadow retention and chronology.
