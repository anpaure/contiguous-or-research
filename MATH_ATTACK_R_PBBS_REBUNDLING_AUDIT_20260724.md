# Adversarial audit of lane R: PBBS rebundling

Date: 2026-07-24

## Verdict

The central local algebra in MATH_ATTACK_R_PBBS_REBUNDLING_REPORT_RAW_20260724.md is correct:

1. deleting the four old edges of a simple alternating \(C_8\) gives four residual paths whose old/new component-incidence multigraph is connected;
2. the cut-shape list, incidence rank \(r+s-1\), centered-vector balance equations, and zero-or-opposite classification are correct;
3. the endpoint-corrected omitted-label formula and the uniform seam-label condition are correct;
4. the clean directed-\(C_4\) dictionary and the PBBS six-residual-label theorem are correct after making two definitions explicit and supplying the missing Dyck-block proof;
5. the constants \(12\binom n{m-1}\), \(8m\), \(16m\), \(nE\le L\le2nE\), and the per-switch component-gain bound \(3\) are correct; and
6. the centered-arc and label-token cancellation barriers have the constants claimed within their stated abstract models.

The report does **not** prove positive-density PBBS rebundling. Four scope corrections are essential.

- The six-label theorem applies to alternating \(C_8\)'s supported by the **initial canonical PBBS factor**. After a switch, the current factor need not satisfy the PBBS residual-label restriction.
- The coarse phrase “clean cycle plus a zero segment or opposite pair” is only a necessary summary. The topology-specific balance table is the lossless condition.
- The \(\Omega(n)\) fragmentation theorem is an isolated label-token obstruction. It is not a PBBS inter-orbit lower bound, and it can fail to apply once auxiliary components import tokens.
- “Positive-density rebundling is necessary” is valid only conditionally for the specified bounded-profile local move class and a starting defect of the asserted order. It is not an unconditional theorem about PBBS or all rebundling architectures.

No exact-wreath counterexample, clean-cycle lower bound, compatible-cancellation density theorem, dynamic route, cleanup theorem, MWB theorem, or labelled synchronization theorem is proved.

## 1. Alternating-\(C_8\) cut shapes and balance equations

### 1.1 Four residual paths and connected incidence: valid

Let \(Z\) be a simple \(F\)-alternating \(C_8\). Its four old edges are pairwise disjoint. If a component of \(F\) is cut \(k\ge1\) times, deleting those edges leaves \(k\) paths. Summing over the touched components gives exactly four residual paths \(P_1,\ldots,P_4\).

Let \(H\) be the bipartite multigraph whose left vertices are the old touched components, whose right vertices are the new touched components, and whose edge \(i\) represents \(P_i\). Then \(H\) is connected. One direct proof is as follows.

- Assign each vertex of \(Z\) to the residual path containing that vertex.
- Across an old edge of \(Z\), the two assigned paths meet the same old-component vertex of \(H\).
- Across a new edge, they meet the same new-component vertex of \(H\).
- Traversing the connected cycle \(Z\) therefore gives a connected walk through the line graph of \(H\), and every \(P_i\) occurs because both of its endpoints lie on \(Z\).

Thus, with \(r=|\mathcal O|\) and \(s=|\mathcal N|\),

\[
r+s=|V(H)|\le |E(H)|+1=5.
\]

The displayed cut-shape table in the raw report is therefore the exhaustive **necessary list** obtained from the five integer partitions of \(4\) and \(r+s\le5\). The word “among” is important: the table does not assert that every listed ordered pair is geometrically realizable.

### 1.2 Rank \(r+s-1\): valid

Let \(M\) be the \(0\)-\(1\) row-by-edge incidence matrix of \(H\). Multiplying every row belonging to \(\mathcal N\) by \(-1\) turns \(M\) into an oriented incidence matrix. Since \(H\) is connected,

\[
\operatorname{rank}_{\mathbb Q}M=r+s-1.
\]

The old-component rows have pairwise disjoint supports and rank \(r\). Hence the new balance rows contribute exactly \(s-1\) independent coefficient-row equations modulo the old equations.

This is a statement about independent **vector equations**. Every centered vector already lies in the coordinate-sum-zero hyperplane; the report does not incorrectly claim \(n(s-1)\) independent scalar equations.

### 1.3 Centered-vector balance table: valid

For

\[
\zeta(P)=n\sum_{A\in P}{\bf1}_A-m|P|\mathbf1,
\]

additivity and old componentwise point regularity give

\[
\sum_{i\in B}\zeta(P_i)=0\qquad(B\in\mathcal O).
\]

A new component is point regular exactly when the analogous sum over its block \(B\in\mathcal N\) vanishes. Since the total sum of all four vectors is zero, the raw table is exact:

\[
\begin{array}{c|l}
4&\text{automatic},\\
31&\text{the singleton vector is zero},\\
22&\text{one pair consists of opposite vectors},\\
211&\text{both singleton vectors are zero},\\
1111&\text{all four vectors are zero}.
\end{array}
\]

Thus a balanced proper multi-output reconnection requires a centered segment or an opposite pair. Conversely, such a cancellation certifies balance only when it is the singleton or pair selected by the **actual new cut topology**. A generic statement that some zero or opposite pair exists is not by itself a lossless sufficient criterion.

The assertion that only \(s=1\) is automatic is valid algebraically. It does not exclude additional identities special to a particular factor.

## 2. Omitted labels, endpoint correction, and seams

### 2.1 Path identity: valid

For a path \(P=(A_0,\ldots,A_{L-1})\), let \(t_x\) count internal edges with omitted label \(x\), and let

\[
e_x={\bf1}_{x\in A_0}+{\bf1}_{x\in A_{L-1}}.
\]

Every internal edge contributes one to the sum of the memberships of its two endpoints unless its omitted label is \(x\). Therefore

\[
2\iota_x(P)-e_x=L-1-t_x.
\]

Using \(n=2m+1\) gives

\[
\boxed{2\zeta(P)=n(e(P)-t(P))+(L-n)\mathbf1.}
\]

All constants and signs in the raw report are correct.

### 2.2 Sewn-component criterion: valid

Suppose \(h\) paths of total length \(kn\) are sewn cyclically. Let \(a_x\) count added seam edges with omitted label \(x\). A seam labelled \(y\) contributes one endpoint occurrence to coordinate \(x\) exactly when \(x\ne y\), so

\[
e_x=h-a_x.
\]

Summing the path identities gives the cyclic formula

\[
2\iota_x=kn-(t_x+a_x).
\]

Point regularity requires \(2\iota_x=2km=k(n-1)\), and hence exactly

\[
\boxed{t_x+a_x=k\quad\text{for every }x.}
\]

For \(k=1\), every omitted label occurs once. If \(\lambda_i\) labels the edge \(A_iA_{i+1}\), the recurrence around the odd cycle gives, after cyclic reindexing,

\[
A_i=\{\lambda_{i-2},\lambda_{i-4},\ldots,\lambda_{i-2m}\}.
\]

Because multiplication by \(-2\) is invertible modulo odd \(n\), these are precisely the cyclic \(m\)-windows of a wreath. Thus the report's “literally a wreath” conclusion is valid.

## 3. Clean directed-\(C_4\) dictionary

### 3.1 Definition correction

For \(K\in\binom{[n]}{m-1}\), set \(B=[n]\setminus K\). The definition should explicitly require distinct \(u,v\in B\):

\[
u\longrightarrow v
\iff
u\ne v\ \text{ and }\
F\text{ contains }
\{K\cup\{u\},B\setminus\{u,v\}\}.
\]

Without \(u\ne v\), the displayed second set has size \(m+1\), so no factor edge exists; the intended loopless definition is nevertheless clear.

Every \(K\cup\{u\}\) has two distinct \(F\)-neighbours, each uniquely of the displayed form. Hence every vertex of \(D_K^F\) has outdegree exactly two.

### 3.2 Precise bijection: valid

The exact statement is a bijection between

- unrooted simple \(F\)-alternating \(C_8\)'s, and
- pairs consisting of the unique core \(K\) and an unrooted clean simple directed \(C_4\) in \(D_K^F\).

If \(\sigma=(u_0u_1u_2u_3)\), put \(A=\{u_0,u_1,u_2,u_3\}\) and \(Y=B\setminus A\). The old edges are

\[
\left\{
\left\{K\cup\{u_i\},
Y\cup(A\setminus\{u_i,u_{i+1}\})\right\}
:0\le i<4
\right\},
\]

and the proposed new edges replace \(u_{i+1}\) by \(u_{i-1}\). Thus the new edges are absent from \(F\) exactly when all inverse arcs \(u_i\to u_{i-1}\) are absent.

The universal odd-\(C_8\) normal form shows that the two parity-class intersections have sizes \(m-1\) and \(m-2\). Therefore the intersection of size \(m-1\), namely \(K\), is unique.

## 4. PBBS six-label theorem and counts

### 4.1 Clean-label theorem: valid, but the proof in the raw report is too compressed

For an \((m-1)\)-set \(K\), its deficit-three cyclic word can be cut and written

\[
0D_1\,0D_2\,0D_3,
\]

where the \(D_i\) are Dyck words, possibly empty, and the three displayed zeroes are precisely \(U_+(K)\).

Change any zero \(u\notin K\) into a one.

- If \(u\) lies in a Dyck block, that block now exits with two excess opens, which consume the next two displayed unmatched zeroes.
- If \(u\) is one of the displayed zeroes, it ceases to be a zero and its new open consumes the next displayed zero.

In either case exactly the third old unmatched zero remains. Thus

\[
r_+(K\cup\{u\})\in U_+(K).
\]

Reversing the cyclic order proves

\[
r_-(K\cup\{u\})\in U_-(K).
\]

The two PBBS factor neighbours are the forward and inverse PBBS images, so their omitted labels are \(r_+\) and \(r_-\). Hence every arc of \(D_K^{F_{\rm PBBS}}\) has its head in

\[
S_K=U_+(K)\cup U_-(K),\qquad |S_K|\le6.
\]

Every directed cycle is therefore contained in \(S_K\).

This theorem concerns the canonical PBBS factor. It is not preserved automatically after toggling a connector.

### 4.2 Twelve cycles per core: valid after restoring the omitted factor six

A rooted directed four-cycle has at most six choices for its root and at most \(2^3\) choices for its first three outgoing steps; the fourth step is a closure test. Dividing by four cyclic roots gives

\[
\frac{6\cdot2^3}{4}=12
\]

unrooted directed \(C_4\)'s per core. The same upper bound holds for clean cycles. The raw prose omitted the explicit factor \(6\), although its final constant is correct.

Core uniqueness then yields

\[
\#\{F_{\rm PBBS}\text{-alternating }C_8\}
\le12\binom n{m-1}
=12\frac m{m+2}W<12W.
\]

This is a linear supply upper bound. It is not proved sharp or asymptotically attained.

### 4.3 Edge and vertex multiplicities: valid

Fix a PBBS factor edge \(e=\{A,C\}\) with omitted label \(v\). To represent it as an arc, choose which endpoint is the \(K\cup\{u\}\) endpoint and then choose \(u\) in that endpoint. There are at most \(2m\) such presentations. Once the arc \(u\to v\) is fixed, there are at most \(2\cdot2=4\) choices for the next two arcs of a directed \(C_4\), followed by a closure test. Hence

\[
e\text{ lies in at most }8m\text{ supported alternating }C_8\text{'s}.
\]

Every middle vertex has two factor edges, and an alternating \(C_8\) through it uses exactly one of them. Thus every middle vertex lies in at most \(16m\) such cycles.

If an independent theorem supplied \(\Omega(W)\) clean cycles, greedy selection would give \(\Omega(W/m)=\Omega(W/n)\) vertex-disjoint underlying \(C_8\)'s, since selecting one cycle conflicts with at most \(8\cdot16m\) cycles. This would not yet give balanced, component-increasing, component-disjoint, or simultaneously applicable rebundling moves.

## 5. Quantitative component potential

Let the component levels be \(\ell_1,\ldots,\ell_c\). Point regularity implies every component length is \(\ell_jn\), and

\[
\sum_j\ell_j=C_m=\frac Wn.
\]

Therefore

\[
E(F)=C_m-c=\sum_j(\ell_j-1),
\]

while

\[
\frac{L(F)}n=\sum_{\ell_j\ge2}\ell_j.
\]

Since \(\ell-1\le\ell\le2(\ell-1)\) for every \(\ell\ge2\),

\[
\boxed{nE(F)\le L(F)\le2nE(F).}
\]

Thus \(E=o(C_m)\) is equivalent to all but \(o(W)\) vertices lying in level-one components **of the current factor**. Section 2 proves that these level-one odd-graph components are wreaths.

If a switch replaces \(r\) old components with \(s\) new ones, then

\[
E(F')-E(F)=r-s,
\qquad
E(F)-E(F')=s-r\le3.
\]

Consequently, conditional on

\[
E(F_{\rm PBBS})=\Theta(C_m),
\qquad E(F_T)=o(C_m),
\]

every route requires \(\Omega(C_m)=\Omega(W/n)\) switches and also that many net component-increasing events up to the factor \(3\).

The raw sentence “a bounded local template cannot suffice” should be replaced by:

> A bounded number, or more generally \(o(C_m)\), of alternating-\(C_8\) operations cannot suffice under the displayed hypothesis. A fixed bounded-size template would have to be applied \(\Omega(C_m)\) times.

The argument does not rule out one template repeated at positive density or prove the existence of that many compatible connectors. The hypothesis \(E(F_{\rm PBBS})=\Theta(C_m)\) is not established in the raw report.

## 6. Cancellation barriers

### 6.1 Infinite centered-arc obstruction: valid with an explicit congruence

The construction applies for

\[
n=4k+1\ge9,
\qquad 3\nmid\frac{n+1}{2},
\]

equivalently \(n\equiv1\) or \(9\pmod{12}\). Thus it gives infinitely many dimensions, as claimed.

For every \(n\)-vertex segment \(P\), the coordinate deviations consist of \(a\) entries \(+1\), \(a\) entries \(-1\), and the rest zero, where

\[
\left\lfloor\frac{n-1}{6}\right\rfloor
\le a\le
\left\lceil\frac{n-1}{6}\right\rceil.
\]

Therefore

\[
\|\zeta(P)\|_1
=2na
\ge2n\left\lfloor\frac{n-1}{6}\right\rfloor.
\]

Complementary \(2n\)-segments are also noncentered. Since \(\gcd(m,n)=1\), a centered segment must have length divisible by \(n\); consequently the constructed simple point-regular \(3n\)-cycle has no proper centered segment.

The \(n=9\) example is isomorphic, by rotation and coordinate relabeling, to an actual canonical-PBBS \(27\)-cycle. This is one finite PBBS component, not an asymptotic PBBS obstruction family.

### 6.2 Linear label-token barrier: valid only in its isolated model

For \(n=3g\) odd, \(g\ge3\), and \(r\ge2\), the clustered word

\[
\mathcal W_{n,r}
=(1,2,3)^r(4,5,6)^r\cdots(n-2,n-1,n)^r
\]

has distinct adjacent labels and odd same-label gaps. Every proper subset containing exactly \(k\) copies of every label requires at least

\[
\left\lceil\frac n6\right\rceil
\]

cyclic intervals. After \(t\) label-preserving four-edge switches, a final whole component uses at most \(4t\) intervals of the initial token word. Hence

\[
t\ge\frac14\left\lceil\frac n6\right\rceil,
\]

with the integer strengthening

\[
t\ge\left\lceil\frac{\lceil n/6\rceil}{4}\right\rceil.
\]

For an actual point-regular odd-graph closed walk one may take \(r\) odd, but the walk is generally nonsimple and not PBBS.

Moreover, the proof treats \(\mathcal W_{n,r}\) as the entire initial token universe. If switches import tokens from auxiliary components, the intersection of a final component with \(\mathcal W_{n,r}\) need not contain the same number of every label, so the interval lemma no longer applies. Thus this theorem is not a PBBS inter-orbit or catalytic-rebundling lower bound.

Only an abstract \(\Omega(n)\) barrier is proved. The phrase “natural unresolved scale \(\Theta(n)\)” is heuristic: no \(O(n)\) legal balanced route is established.

## 7. Profile-3 absorbers and objective changes

The following imported first-wave facts are valid for \(m\ge2\).

- Every normalized oriented rooted four-label window of a wreath has exactly

\[
(m-1)!(m-2)!
\]

unoriented profile-3 partner wreaths.
- The removal/addition masses are

\[
r_1=8,
\qquad r_q=4q+6\quad(2\le q\le m-1),
\]

with zero depth-\(m\) effect.

These are ambient partner and seam-mass statements. They do not provide partners already selected in the same exact factor, disjoint absorbers, exact nonzero-cell counts, or exact half-\(L^1\) changes.

For fixed \(A\), summing the masses through \(q\le A\sqrt m\) gives \(O_A(m)\). The corresponding pointed-owner bounds give the same order for the minimized labelled objective. Hence \(t=o(C_m)\) such trades change either fixed-window weighted objective by only

\[
o(C_m)\,O_A(m)=o(W).
\]

The correct implication is conditional and route-specific:

> If the starting and desired endpoint objectives differ by at least \(\delta W\), and every step is one of these profile-3 trades, then \(t=\Omega_{A,\delta}(C_m)\).

This does not prove that PBBS has a linear objective defect, that \(\Omega(C_m)\) selected partners or disjoint connectors exist, or that another larger-footprint/global operation cannot repair the factor.

## 8. Corrected implication scope and unsupported lemmas

### 8.1 What the initial-factor theorem really says

For the **initial canonical PBBS factor**, every balanced component-increasing alternating \(C_8\) must consist of

1. a clean directed \(C_4\) contained in \(S_K=U_+(K)\cup U_-(K)\) for its unique core \(K\); and
2. the topology-specific centered-vector cancellation prescribed by the new cut shape.

After the first switch, item 1 need not hold for the current factor. Item 2 continues to hold for every componentwise point-regular factor.

Thus the headline claim is correct only after inserting “supported by the initial PBBS factor” and replacing the coarse cancellation disjunction by the exact topology table when sufficiency is intended.

### 8.2 Still unsupported

The following remain unproved.

1. **Clean-cycle density:** \(\Omega(W)\) clean directed \(C_4\)'s in the PBBS auxiliary digraphs.
2. **Tightness of the supply bound:** any lower construction showing that the \(12W\) upper bound is sharp even in order or constant beyond the trivial possible linear order.
3. **Compatible cancellation density:** enough clean cycles whose actual path vectors satisfy their required singleton or pair equations.
4. **Dynamic routing:** a legal balanced route, of \(O(n)\) or any controlled scale, that repeatedly lowers \(E\) despite temporary merges and changes to the auxiliary digraphs.
5. **Positive-density availability:** \(\Omega(C_m)\) compatible, jointly applicable connectors or selected profile-3 partners.
6. **PBBS excess:** an asymptotic theorem \(E(F_{\rm PBBS})=\Theta(C_m)\), if that hypothesis is needed.
7. **Relative integral cleanup:** convert a near-wreath factor to an exact wreath factor while preserving the obtained wreath bulk or changing a quantitatively controlled owner set.
8. **Shadow control:** obtain fixed-window overload, MWB, or labelled common-owner synchronization from the rebundled factor.

An independently existing exact wreath factor does not solve item 7: cleanup must preserve the structural progress just obtained. Even a hypothetical cleanup changing only \(L=o(W)\) middle owners would have the crude fixed-window cost \(O_A(L\sqrt m)\), which need not be \(o(W)\); one needs a stronger leave rate or aligned shadow cancellation.

Finally,

\[
E=0
\Longrightarrow
\text{the current factor is an exact wreath factor},
\]

but there is no proved implication

\[
E=0
\Longrightarrow
\text{small overload, MWB, or labelled synchronization}.
\]

This is a missing implication, not a proved counterexample. The labelled statement remains strictly stronger than overload MWB.

## Final corrected verdict

Lane R supplies a correct local classification and two genuine cancellation barriers. Its strongest rigorous conclusion is:

> A balanced component-increasing \(C_8\) supported by the initial PBBS factor requires both a clean directed four-cycle inside a six-label residual set and the exact topology-compatible zero/opposite cancellation. Neither condition is currently known at positive density, and neither PBBS homomesy nor the odd-gap rule implies it.

The route does not yet prove positive-density rebundling, an exact-factor cleanup preserving the rebundled bulk, fixed-window overload, MWB, SYNC, or the coefficient-one contiguous-OR theorem.

The cut-rank calculation, PBBS residual-label proof, cycle-count constants, potential signs, and cancellation scopes were independently rederived in separate audits.
