# Exact compound/Graver neighbourhood of the repaired K16 factor through support five

Date: 2026-07-30

Status: proved algebraic decomposition, exhaustive authenticated finite
census in a stated seam-bank fibre, and independent literal replay. This is
a radius-five no-descent theorem only in that fibre. It is not a global
Johnson-fibre or unrestricted-collar no-go.

## 1. Frozen state and conclusion

Let \(F_8\) be the current length-eight-repaired factor

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

and let \(\mathcal E\) be the directed seam bank

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

containing exactly \(211604\) nonidentity seams. Every bank seam is a
Johnson edge, joins source cut indices at cyclic source distance at least
four, and passes the exact positive-residence-four collar test. The frozen
reverse-edge audit has \(26233\) new/new conflict pairs and no old/new
conflict.

Let \(\mathcal H\) be the literal all-depth objective

\[
 \mathcal H(F)=
 \sum_{s=1}^{7}H^-_s(F)+\sum_{s=9}^{16}H^+_s(F),                 \tag{1.1}
\]

where \(H^-_s\) counts absent fixed lower intersections and \(H^+_s\)
counts rank-\(s\) targets absent from every nonempty cyclic interval union.
Prescribed-width upper holes are not counted when another interval witnesses
the same target. The frozen factor has

\[
 H^-_6(F_8)=45,\qquad H^+_{11}(F_8)=48,\qquad
 \mathcal H(F_8)=93,                                           \tag{1.2}
\]

with every other term zero, and minimum positive coordinate-run length four.

The main finite conclusion is

\[
 \boxed{
   F\in\mathcal N_{\rm sep}(F_8,\mathcal E),\quad
   1\le |\operatorname{cut}(F)|\le5,\quad
   Q(F)=Q(F_8)
   \ \Longrightarrow\ \mathcal H(F)\ge93.}                     \tag{1.3}
\]

Here \(Q(F)=Q(F_8)\) is equality of the two complete q1 multiplicity
vectors, not mere q1 coverage. The fibre \(\mathcal N_{\rm sep}\) is
defined in Section 2. Every defect-contacting algebraic packet in (1.3) was
physically materialized and replayed. There are \(298\) such packets, and
none descends.

Thus within this fibre the shortest strict-descent packet, if one exists,
has at least six cuts. This includes all interacting port-cycle products
through support five and is strictly broader than the prior saved C8/C9
single-cycle screens.

## 2. Exact bank fibre

Index the \(12870\) directed source transitions by

\[
 i=(a_i,b_i),\qquad |a_i|=|b_i|=8,\qquad |a_i\triangle b_i|=2.
                                                                    \tag{2.1}
\]

A bank seam \(e=(i,j)\) replaces \(a_i\to b_i\) by
\(a_i\to b_j\). Put

\[
 L_i=a_i\cap b_i,\quad U_i=a_i\cup b_i,\qquad
 L_e=a_i\cap b_j,\quad U_e=a_i\cup b_j.                           \tag{2.2}
\]

For a binary seam vector \(x\), let \(c_i\) indicate that transition
\(i\) is cut. Direction-coherent port balance is

\[
 \sum_{e:\ell(e)=i}x_e=c_i=\sum_{e:r(e)=i}x_e.                   \tag{2.3}
\]

Exact q1 equality is, for every rank-seven \(L\) and rank-nine \(U\),

\[
 \sum_{e:L_e=L}x_e=\sum_{i:L_i=L}c_i,\qquad
 \sum_{e:U_e=U}x_e=\sum_{i:U_i=U}c_i.                            \tag{2.4}
\]

The separated bank fibre consists of the binary solutions of
(2.3)--(2.4) which also satisfy:

1. every selected seam lies in the authenticated bank \(\mathcal E\);
2. any two selected cut indices on one source component have cyclic
   distance at least four;
3. no selected pair is one of the \(26233\) reverse-new-edge conflicts.

The final materialization is still replayed for simplicity and residence.
No q2 or q3 safety condition is imposed before replay, so deep-unsafe,
locally nongainful, and mutually compensating cycles are retained.

Write \(\mathcal N^{\rm alg}_{\rm sep}\) for the algebraic superset obtained
by dropping item 3. The finite cycle loops enumerate this superset: they do
not consult the reverse-conflict table before reporting structural, exact,
or noncontact counts. Every strict-descent candidate lies in the contact
part of this superset, and every such candidate is then materialized; all
298 pass physical simplicity. Hence the over-enumeration covers
\(\mathcal N_{\rm sep}\) and is sound for the no-descent theorem, while the
855 unreplayed noncontact rows are only algebraic packets.

This bank restriction is substantial. It omits close same-component ports
and every seam failing its isolated positive collar. It fixes one source
orientation. Hence this is neither the unrestricted \(810810\)-arc
head-assignment fibre nor the complete physical Johnson exchange graph.

## 3. Coupled three-flow and the Graver decomposition

For \(e=(i,j)\), define

\[
 A_e=\left(\mathbf e_j-\mathbf e_i;\ 
            \mathbf e_{L_e}-\mathbf e_{L_i};\ 
            \mathbf e_{U_e}-\mathbf e_{U_i}\right).              \tag{3.1}
\]

In this section “capacity one” means explicitly that \(x_e\in\{0,1\}\)
and

\[
 \sum_{e:\ell(e)=i}x_e\le1\qquad\text{for every port node }i.     \tag{3.1a}
\]

Together with the first block of \(Ax=0\), this also bounds incoming
degree by one. The equation \(Ax=0\) without (3.1a) would allow higher
integer circulations and is not the statement below.

### Theorem 3.1 (exact compound-flow identity)

A capacity-one seam vector \(x\) is a port permutation with exactly the
two source q1 multiplicity vectors if and only if

\[
 Ax=0.                                                           \tag{3.2}
\]

Its port projection decomposes uniquely into vertex-disjoint simple directed
cycles \(C_1,\ldots,C_t\). If

\[
 \sigma(C)=\sum_{e\in C}
 \left(\mathbf e_{L_e}-\mathbf e_{L_{\ell(e)}};\ 
       \mathbf e_{U_e}-\mathbf e_{U_{\ell(e)}}\right),            \tag{3.3}
\]

then \(Ax=0\) is equivalent to

\[
 \sum_{\alpha=1}^t\sigma(C_\alpha)=0.                             \tag{3.4}
\]

#### Proof

The first block of (3.2) is equality of selected tail and freed head
incidence. Capacity one makes every nonempty component indegree-one and
outdegree-one, hence a simple directed cycle. The decomposition is unique.
The last two blocks are exactly (2.4); summing cycle by cycle gives (3.4).
\(\square\)

### Corollary 3.2 (positive Graver characterization)

A capacity-one packet is a positive Graver element of \(A\) if and only if
no proper nonempty subfamily of its port cycles has total signature zero.

Indeed, a flow-balanced binary subvector of a simple directed cycle is
either the whole cycle or empty. Thus conformal kernel subvectors are exactly
zero-signature subfamilies.

### Theorem 3.3 (rigidity through five cuts)

There is no nonzero physically simple exact-q1 packet with one or two cuts
in the authenticated bank. Consequently every physically simple exact
packet of support at most five is positive-Graver primitive.

#### Proof

One cut cannot balance ports because the bank has no identity seam. Two cuts
would be a reciprocal \(C_2\). Its signed physical difference has two old
and two new Johnson edges and lies in the exact owner-degree plus q1 lattice.
The proved circuit-girth theorem says every nonzero element of that lattice
has at least six signed physical edge columns. The only escape is a
nonsimple reversal. The bank has no old/new reverse conflict and every
new/new reverse conflict is excluded, so no physical exact \(C_2\) exists.

If a physically simple exact packet \(x\) of support at most five split
conformally as \(x=y+z\), port balance makes each summand a union of whole
port cycles. Each summand remains physically simple: the authenticated bank
has zero old/new reverse conflicts, while passing to a subset cannot create
a new/new reverse pair. Thus both nonzero summands are physical exact
packets. Each has at least three cuts, forcing \(|x|\ge6\), a contradiction.
\(\square\)

Thus nonlinear interaction between separately exact packets can first occur
at support six. Below six, several nonzero cycle signatures may cancel, but
their union is one positive Graver element.

## 4. All-depth defect contact

Let \(\mathcal A\) be the \(45\) old lower rank-six holes and
\(\mathcal B\) the \(48\) old arbitrary-upper rank-eleven holes. Define

\[
 \mathcal P=
 \{e:\exists L\in\mathcal A,\ L\subseteq L_e\}
 \ \cup\ 
 \{e:\exists U\in\mathcal B,\ U_e\subseteq U\}.                  \tag{4.1}
\]

This is broader than the old one-seam fixed-width provider flag.

### Lemma 4.1 (necessary contact)

If a materialized packet has \(\mathcal H(F)<93\), it selects a seam in
\(\mathcal P\).

#### Proof

Strict descent must newly cover one old hole. A purported new witness
containing no changed directed adjacency is a contiguous source interval and
was already a source witness. Therefore a genuinely new witness contains a
selected seam \(a_i\to b_j\).

For \(L\in\mathcal A\), every state of the fixed lower witness contains
\(L\), hence \(L\subseteq a_i\cap b_j=L_e\). For
\(U\in\mathcal B\), every state of its arbitrary-width union witness lies
inside \(U\), hence \(U_e=a_i\cup b_j\subseteq U\). \(\square\)

Therefore noncontact exact packets cannot descend and need not be replayed
for a strict-descent no-go. The finite artifact counts them separately and
does not call them certified physical factors.

## 5. Complete low-support classification

The nonidentity port permutation on its \(s\) changed tails is a
derangement. For \(s\le5\), its complete cycle partitions are

\[
\begin{array}{c|c}
s&\text{port-cycle types}\\ \hline
3&C_3,\\
4&C_4,\quad C_2+C_2,\\
5&C_5,\quad C_2+C_3.
\end{array}                                                       \tag{5.1}
\]

For a single cycle the enumerator starts at its unique minimum cut index.
This removes rotations while retaining a legal reverse orientation as a
distinct object. Bank membership certifies adjacent-pair separation;
explicit chord checks cover every nonadjacent pair, and the frozen generator
also asserts full pairwise separation on completion.

For multi-cycle types, every reciprocal \(C_2\) atom and every relevant
\(C_3\) atom is generated without gain, safety, or provider filtering.
Atoms are grouped by the full sparse integer signature (3.3); only opposite
signatures are joined. The full integer signature is recomputed after every
join, so hashing is not evidence. Disjointness and all cross-cycle
separations are then tested. This is an exact meet-in-the-middle enumeration
of both compound rows in (5.1).

These observations prove that the finite loops exhaust
\(\mathcal N^{\rm alg}_{\rm sep}\) through support five and therefore cover
every member of \(\mathcal N_{\rm sep}\). Physical reverse conflicts are
removed by the contact replay, not by the algebraic counts.

## 6. Exact census

The authenticated pre-conflict algebraic census, followed by physical replay
of every contact row, is

```text
scratch/k16_len8_exact_q1_compound_support5_20260730.audit.json
SHA-256 6639dcb48a10c071250a9e3a7d9588170212f09318f5de8ffffcb75d76b48452
```

| type | structural objects | exact-q1 algebraic packets | no old-defect contact | physically replayed | objective histogram |
|---|---:|---:|---:|---:|---|
| \(C_3\) | 7,348 directed cycles | 494 | 375 | 119 | \(93^{45},94^{60},95^{14}\) |
| \(C_4\) | 41,010 directed cycles | 209 | 165 | 44 | \(93^{29},94^{15}\) |
| \(C_2+C_2\) | 1,963 reciprocal \(C_2\) atoms | 0 opposite-signature products | 0 | 0 | empty |
| \(C_5\) | 402,109 directed cycles | 450 | 315 | 135 | \(93^{60},94^{15},95^{15},97^{30},99^{15}\) |
| \(C_2+C_3\) | 1,963 \(C_2\) plus 7,348 \(C_3\) atoms | 0 opposite-signature products | 0 | 0 | empty |

For compound joins, zero means zero compatible opposite-signature products
after disjointness and separation, not zero structural products. The 1,963
reciprocal \(C_2\) atoms have 1,963 distinct signatures; the exact join
census finds no disjoint, pairwise-separated opposite-signature completion.

All \(119+44+135=298\) contact packets are physically simple and
positive-resident with minimum run four. Their smallest objective is 93.
Lemma 4.1 excludes the remaining \(375+165+315=855\) noncontact algebraic
packets from strict descent.

This also corrects an earlier incomplete frontier statement: the all-bank
exact triangle count is 494, not merely the fifteen distinguished inverse
repair triangles.

## 7. Literal replay

For every retained packet, the engine constructs the successor permutation
on all 12,870 middle vertices and checks indegree one, Johnson adjacency,
absence of repeated undirected edges, and absence of physical two-cycles.

For every component \(T_0,\ldots,T_{\ell-1}\), fixed lower depth \(q\)
is recomputed as

\[
 I_{s,q}=\bigcap_{h=0}^{q}T_{s+h},\qquad 1\le q\le7,              \tag{7.1}
\]

without going more than once around a component.

For arbitrary upper coverage, fix start \(s\). For each coordinate
\(x\notin T_s\), let \(d_x\) be its first positive cyclic occurrence
before returning to \(s\). The union of the interval of age \(a\) is

\[
 T_s\cup\{x:d_x\le a\}.                                        \tag{7.2}
\]

It changes only at the at most eight distinct first-occurrence distances.
Recording (7.2) after every tied event records every distinct interval union,
not a fixed-width surrogate. Every cyclic positive coordinate run is then
enumerated, and the exact objective is counted from absent masks.

## 8. Reproducibility and independent replay

Generator:

```text
scratch/audit_k16_len8_exact_q1_compound_support5_20260730.cpp
SHA-256 50e5c5e68230ccd4c71fc90cea69bc70d89fb1392247f4220afd5ac14a95cb55
```

Independent verifier:

```text
scratch/audit_k16_len8_exact_q1_compound_support5_independent_20260730.py
SHA-256 c2f07de7c6fb0380f9f1fdbfe8e179f3cd801dbca86231ee777be4738a8a36d6
```

Independent binary reader:

```text
scratch/audit_k16_seam_ledger_permutation_20260730.py
SHA-256 c88f13823c0c57a1934b5fcc541301fa13476bf2ca48b3fc614ed13087604ff2
```

The verifier fail-closes on factor, bank, generator, and census hashes. In
one process it independently materializes all 298 retained packets, checks
zero exact q1 delta rather than q1 coverage, checks port balance and
separation, recomputes all lower and arbitrary-upper holes, and reproduces
every histogram in Section 6.

```text
scratch/k16_len8_exact_q1_compound_support5_20260730.independent.audit.json
SHA-256 c29ba9056b46b5e922edffc651e16367351630485581058a5b4c9116c6c8c904
```

The resource and provenance ledger is

```text
scratch/k16_len8_exact_q1_compound_support5_20260730.manifest.json
SHA-256 b796f97d4dc8ead482044ccbb4e3cb03939fae84da88f13aad6adc6680e975e3
```

The exhaustive run used one H100 CPU, a 1 GiB virtual-memory cap, an external
1,260-second timeout, and a 1,200-second internal advisory deadline. It
completed in 15.83 seconds at 17.5 MiB maximum RSS. The independent replay
used one H100 CPU and a 512 MiB cap; it completed in 5 minutes 9.84 seconds
at 344.2 MiB maximum RSS. No GPU and no heavy local process ran.

## 9. Exact boundary and next gate

Theorems 3.1--3.3, Lemma 4.1, classification (5.1), and the census prove
(1.3):

> In the authenticated direction-coherent, globally four-separated
> 211,604-seam fibre, no positive-resident exact-q1 compound exchange with
> at most five cuts lowers the literal all-depth objective below 93.

Every physically simple exact packet in this radius is one positive Graver
element. The first
unclosed support is six, with port partitions

\[
 C_6,\qquad C_4+C_2,\qquad C_3+C_3,\qquad C_2+C_2+C_2.           \tag{9.1}
\]

Support six is also the first radius at which two separately exact
three-cut packets can have nonlinear shadow synergy. The next exact search
should enumerate every \(C_6\) signature and join all multi-cycle
partitions in (9.1), replaying primitive and decomposable packets.

Nothing here excludes:

1. a six-cut or larger packet in the same bank;
2. interacting collars after dropping global cut separation;
3. a move using a close or isolated-collar-unsafe seam omitted from the bank;
4. reversed-source, moving-frame, or unrestricted Johnson exchanges;
5. a q1-cover-preserving move which changes exact q1 multiplicities.

The oriented bank is not certified closed under the directed
\(C_{15}\)-action, so no orbit quotient was used. This is a rigorous scoped
minimum-support no-go, not a global local-minimum theorem and not a
constant-one proof.
