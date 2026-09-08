# Rooted promotion-ring catalogues and the physical-port arbitrary-dual gate

**Dated audit: 2026-07-26. Constant-one lane only.**

## 0. Verdict

The physical-port arbitrary-dual conclusion would imply a near-resolution of the promotion-ring catalogue after the correct rooted and tagged capacity lift. There is an exact quantitative bridge:

> If the lifted rooted catalogue has fractional chromatic index
> \[
> D+o(D/\sqrt m),
> \]
> and its compulsory target rows have total degree deficit \(o(DW)\), then one matching chooses one promotion ring from all but \(o(N_H/\sqrt m)\) roots and has total band holes \(o(W)\).

For the middle-only catalogue this bridge is already literal, with

\[
 D=R:=(M-1)!,
\]

the number of oriented cyclic orders modulo rotation on one top.

The existing physical-port theorem cannot presently be invoked to prove the required chromatic estimate. The promotion packet is a union of \(M\) chronological phase strips, not one selected physical strip; arbitrary targetwise port thinning does not preserve its tight-Hamilton and nested-flag incidences. Moreover, the left-root partition does **not** make the incidence matrix balanced and does not bound its odd-minor rank. There are literal strong odd Berge cycles of every odd length

\[
 3\le \ell\le m-H+2
\]

whose columns have pairwise distinct roots and whose rows are middle targets only. Hence the root rows are invisible to these odd cores.

Rooting nevertheless gives a real reduction. Since

\[
 N_H=\exp(O(m)),
 \qquad
 R=\exp((1+o(1))m\log m),
\]

every root-simple support has dual ratio at most \(N_H=o(R/m^A)\) for every fixed \(A\). Thus a Gaussian-scale obstruction must be simultaneously

1. rank-diverging on the right target rows,
2. matching-interlocked across distinct roots, and
3. enormously dense inside the root fibres.

The root partition eliminates sparse odd cores as quantitative obstructions, but it does not eliminate the residual **fibre-dense odd mesh**. The all-target capacity rows also do not close this last gate: their pure-root rows of order \(p\ge2\) vanish identically, and they impose upper capacities rather than the required common lower transversal of the root fibres.

## 1. The concrete rooted middle catalogue

Use the packing-side calibration

\[
 W=\binom{2m}{m},
 \qquad
 N_q=\binom{2m}{m-q},
 \qquad
 \lambda_q={W\over N_q},
\tag{1.1}
\]

and let \(H\) be the least integer such that

\[
 \lambda_H\ge M:=m+H.
\tag{1.2}
\]

Put

\[
 N=N_H,
 \qquad
 T=MN,
 \qquad
 \rho={T\over W}\le1.
\tag{1.3}
\]

The calibrated estimates give

\[
 H=(1+o(1))\sqrt{m\log m},
 \qquad
 W-T=o(W).
\tag{1.4}
\]

A left root is

\[
 A\in\binom{[2m]}{m-H},
 \qquad U=A^c\in\binom{[2m]}M.
\tag{1.5}
\]

For every oriented cyclic order \(\pi\) of \(U\), modulo rotation, let \(P(A,\pi)\) be the rooted middle packet consisting of

1. its root marker \(A\), and
2. the \(M\) cyclic length-\(m\) windows of \(\pi\).

Equivalently, the complements of those owners inside \(U\) are the \(M\) cyclic length-\(H\) windows of the same order, hence one tight Hamilton cycle of the complete \(H\)-uniform hypergraph on \(U=A^c\).

The latter are the middle owners of the exact promotion ring. Let

\[
 \mathcal G_0=(\mathcal A\sqcup\mathcal X,\mathscr P),
 \qquad
 \mathcal X=\binom{[2m]}m,
\tag{1.6}
\]

be this rooted incidence hypergraph. A matching in \(\mathcal G_0\) chooses at most one packet per root and never repeats a middle owner.

### Proposition 1.1 (exact rooted degrees)

Every root has degree

\[
 \boxed{R=(M-1)!.}
\tag{1.7}
\]

Every middle target has degree

\[
 \boxed{
 D_0=\binom mH m!H!=\rho R.}
\tag{1.8}
\]

#### Proof

There are \((M-1)!\) oriented cyclic orders of a fixed \(M\)-set modulo rotation. The middle degree is Proposition 3.1 of the top-fibre packet reduction. Alternatively, double count root-packet-middle incidences:

\[
 NR M=WD_0.
\]

Equation (1.3) gives \(D_0/R=MN/W=\rho\). \(\square\)

### Proposition 1.2 (root and middle pair links)

If \(X\subset U=A^c\), then

\[
 d(A,X)=m!H!,
 \qquad
 {d(A,X)\over R}={M\over\binom Mm}.
\tag{1.9}
\]

If \(X,Y\) are distinct middle targets at Johnson distance \(d\), then

\[
 {d(X,Y)\over D_0}
 ={a_{m,M}(d)\over\binom md^2},
\tag{1.10}
\]

and in particular

\[
 \max_{X\ne Y}d(X,Y)
 ={2D_0\over m^2}
 \le {2R\over m^2}.
\tag{1.11}
\]

Distinct roots have codegree zero.

#### Proof

For (1.9), contract the prescribed length-\(m\) interval in the cyclic order on \(U\); the interval has \(m!\) internal orders and the complementary block has \(H!\) orders. Equation (1.10) is the exact same-rank packet codegree formula. \(\square\)

Thus the middle-only rooted catalogue has maximum degree \(R\) and relative pair codegree \(O(m^{-2})\). These favorable statistics do not themselves prove a growing-rank matching or edge-colouring theorem, because every packet has rank \(M+1\sim m\).

## 2. Exact edge-colouring-to-near-resolution bridge

The useful role of the root partition is most transparent in the fractional edge-colouring LP.

### Lemma 2.1 (distinguished-row averaging)

Let \(\mathcal G\) be any hypergraph, let \(\mathcal R\) and \(\mathcal T\) be distinguished vertex sets, and suppose every edge contains exactly one root in \(\mathcal R\). Assume

\[
 d(a)=D\quad(a\in\mathcal R),
 \qquad
 d(t)=d_t\le D\quad(t\in\mathcal T).
\tag{2.1}
\]

If

\[
 \chi_f'(\mathcal G)\le D+\eta,
\tag{2.2}
\]

then there is a matching \(Q\) such that

\[
 |\mathcal R\setminus V(Q)|
 +|\mathcal T\setminus V(Q)|
 \le
 {\eta\over D+\eta}|\mathcal R|
 +\sum_{t\in\mathcal T}
     \left(1-{d_t\over D+\eta}\right).
\tag{2.3}
\]

The same assertion holds with arbitrary nonnegative weights on the distinguished rows.

#### Proof

Let \((\alpha_Q)\) be a fractional edge colouring of total weight at most \(D+\eta\), enlarged by an empty matching if necessary so its total is exactly \(D+\eta\). Every edge is covered with total colour weight at least one.

For a vertex \(v\), sum those edge-cover inequalities over its \(d(v)\) incident edges. A matching contains at most one of them, hence

\[
 \sum_Q\alpha_Q\mathbf1_{v\in V(Q)}\ge d(v).
\tag{2.4}
\]

Choose \(Q\) with probability \(\alpha_Q/(D+\eta)\). Then

\[
 \Pr(v\notin V(Q))
 \le1-{d(v)\over D+\eta}.
\tag{2.5}
\]

Sum (2.5), using \(d(a)=D\) for roots, and choose an outcome no worse than its expectation. Weighted summation proves the last statement. \(\square\)

### Theorem 2.2 (middle near-resolution from arbitrary-dual closure)

If

\[
 \boxed{
 \chi_f'(\mathcal G_0)\le R+o(R/\sqrt m),}
\tag{2.6}
\]

then there is a matching containing one packet from all but \(o(N/\sqrt m)\) roots and covering \(W-o(W)\) distinct middle owners.

#### Proof

Apply Lemma 2.1 to the roots alone, with \(D=R\). The number of missed roots is at most

\[
 {\eta\over R+\eta}N=o(N/\sqrt m).
\tag{2.7}
\]

Every chosen packet supplies \(M\) distinct middle owners, and matching disjointness makes owners from different packets distinct. Hence the number of middle holes is

\[
 W-M|Q|
 \le (W-MN)+M\,o(N/\sqrt m)
 =o(W),
\tag{2.8}
\]

using (1.4) and \(MN\le W\). \(\square\)

This theorem is the exact positive interface. No integral near-resolution theorem beyond (2.6) is hidden in the root bookkeeping.

## 3. Nested ranks and the correct tagged capacity lift

A full untagged promotion ring has \(M\) occurrences at every internal rank. It cannot be placed under capacity one at all deeper ranks because \(T/N_q>1\) there. On the packing side, use the truncated tag census

\[
 L_q=\min(N_q,T).
\tag{3.1a}
\]

Thus all \(T\) middle phases are active, while at depth \(q\) exactly \(L_q\) phases have tag at least \(q\). Since \(L_H=N_H=N\), every root receives one tag \(H\). The tag multiplicities \(L_d-L_{d+1}\), together with the \(N\) top tags, telescope to \(T=MN\), so they fill all ring phases. The monotone ring-tag construction applies verbatim. The unavoidable scalar shortage satisfies

\[
 \sum_{q=0}^H(N_q-L_q)
 =\sum_{q=0}^H(N_q-T)_+=o(W).
\tag{3.1b}
\]

Fix for the moment one tag word on each root. Write

\[
 a_{U,q}=|\{i:d_{U,i}\ge q\}|,
 \qquad
 \sum_Ua_{U,q}=L_q.
\tag{3.1}
\]

Because the tag word has a unique tag \(H\), a tagged cyclic order is naturally aligned at that phase. We therefore retain all \(M!\) bijections from the cyclic phase positions to \(U\), and put

\[
 D_{\rm tag}=M!=MR.
\tag{3.1c}
\]

Keeping these formal aligned copies is harmless and preserves exact coordinate symmetry.

For sign \(\sigma\in\{-,+\}\), set

\[
 B_q^- =\binom M{H+q},
 \qquad
 B_q^+ =\binom M{H-q}.
\tag{3.2}
\]

Let \(\mathcal U_q^\sigma(S)\) be the tops compatible with target \(S\) at signed rank \(m\pm q\). When all \(D_{\rm tag}\) aligned cyclic orders are retained over every root, the degree of \(S\) in the fixed-tag rooted catalogue is

\[
 \boxed{
 {d_{q,S}^\sigma\over D_{\rm tag}}
 ={1\over B_q^\sigma}
   \sum_{U\in\mathcal U_q^\sigma(S)}a_{U,q}.}
\tag{3.3}
\]

Indeed, for a fixed active phase, its omitted interval is uniform among the \(B_q^\sigma\) subsets of the required size. Summing (3.3) over all rank targets gives

\[
 \sum_Sd_{q,S}^\sigma=D_{\rm tag}L_q,
\tag{3.4}
\]

so the mean target degree is \(D_{\rm tag}L_q/N_q\le D_{\rm tag}\). It equals \(D_{\rm tag}\) once \(N_q\le T\); its total arithmetic deficit over the shallow ranks is \(o(D_{\rm tag}W)\) by (3.1b).

Define the one-sided degree deficit

\[
 \mathfrak D(\mathbf d)
 ={1\over D_{\rm tag}}
  \sum_{q,\sigma,S}(D_{\rm tag}-d_{q,S}^\sigma)_+.
\tag{3.5}
\]

At \(q=0\) the two signs denote the same middle row and are counted only once.

This is the catalogue form of the literal missing-shadow mean gate. It is not implied by the scalar tag census (3.1). The heat audit's mean term measures the corresponding squared nonuniformity.

For targets of degree above \(D_{\rm tag}\), split their incident occurrences into capacity clones of degree at most \(D_{\rm tag}\), with one primary clone of degree exactly \(D_{\rm tag}\). For targets of degree below \(D_{\rm tag}\), retain one primary clone of degree \(d_{q,S}^\sigma\). This is a literal capacity decoration: packets assigned to different clones may repeat the same physical target, and each repeat is counted against its target capacity. Denote the resulting rooted hypergraph by \(\widehat{\mathcal G}(\mathbf d)\).

### Theorem 3.1 (all-depth conditional near-resolution)

Suppose

\[
 \mathfrak D(\mathbf d)=o(W)
\tag{3.6}
\]

and

\[
 \chi_f'\bigl(\widehat{\mathcal G}(\mathbf d)\bigr)
 \le D_{\rm tag}+o(D_{\rm tag}/\sqrt m).
\tag{3.7}
\]

Then one matching chooses packets from all but \(o(N/\sqrt m)\) roots and has total signed-band missing-shadow count \(o(W)\).

#### Proof

Apply the weighted form of Lemma 2.1, giving every missed root weight \(M\), every missed primary target clone weight one, and every other row weight zero. The root contribution is

\[
 M N\,o(1/\sqrt m)=o(W).
\tag{3.8}
\]

The total number of band targets is

\[
 W+2\sum_{q=1}^HN_q=\Theta(W\sqrt m).
\tag{3.9}
\]

Thus the colouring excess contributes

\[
 o(1/\sqrt m)\,\Theta(W\sqrt m)=o(W).
\tag{3.10}
\]

The degree-deficit contribution is exactly \(\mathfrak D(\mathbf d)=o(W)\). A target is covered whenever its primary clone is covered. At every rank the selected matching uses at most

\[
 \sum_Ua_{U,q}=L_q\le N_q
\]

target occurrences. Hence its repeat excess is at most its missing-target count: if \(c\) targets are covered using \(s\le N_q\) occurrences, then the holes and repeats are \(N_q-c\) and \(s-c\), respectively. Thus repeats are also \(o(W)\) in aggregate and may be discarded and repaired at additive \(o(W)\). \(\square\)

The two hypotheses are genuinely separate. Target-capacity rows address the legal clone capacities. They do not prove the degree-balance condition (3.6), and they do not prove the arbitrary-dual closure (3.7).

## 4. The rooted arbitrary dual

For a nonnegative packet weight \(y\), put

\[
 \nu_y=\max\{y(Q):Q\text{ a legal rooted target-capacity matching}\}.
\tag{4.1}
\]

Fractional edge-colouring duality gives

\[
 \chi_f'(\mathcal G)=\sup_{y\ne0}{y(\mathscr P)\over\nu_y}.
\tag{4.2}
\]

For each root \(A\), define its total and maximum fibre weights

\[
 Y_A=\sum_{P\in\mathscr P_A}y_P,
 \qquad
 w_A=\max_{P\in\mathscr P_A}y_P.
\tag{4.3}
\]

Since \(|\mathscr P_A|=R\),

\[
 Y_A\le Rw_A,
 \qquad
 y(\mathscr P)=\sum_AY_A.
\tag{4.4}
\]

The correct rooted representative theorem is the fibre-**average**, not fibre-maximum, assertion

\[
 \boxed{
 \text{For every }y\ge0\text{, some legal matching }Q\text{ obeys }
 y(Q)\ge(1-o(m^{-1/2})){1\over R}\sum_AY_A.}
\tag{4.5}
\]

Indeed, (4.4)--(4.5) give

\[
 y(\mathscr P)
 \le\bigl(R+o(R/\sqrt m)\bigr)\nu_y.
\tag{4.6}
\]

Conversely, (4.6) for every \(y\) implies (4.5), with the asymptotically equivalent reciprocal error. Thus (4.5) is exactly the rooted form of the missing arbitrary-dual gate.

The tempting stronger bound with \(\sum_Aw_A\) in place of \(R^{-1}\sum_AY_A\) is false. Give weight one to the three packet columns in the \(\ell=3\) construction of Theorem 5.1 and zero to every other packet. The three positive columns are pairwise conflicting, so \(\nu_y=1\), whereas \(\sum_Aw_A=3\). This failure is harmless at the coefficient-one scale because \(R^{-1}\sum_AY_A=3/R\). The root partition averages fibre mass; it does not select all fibre maxima.

Equation (4.5) is not a consequence of the individual target-capacity rows. It asks for one common weighted contention resolution of the uniform root-fibre averages and is precisely the matching-interlock gate.

There is an exact sparsity reduction. If a support \(\mathcal Q\) contains at most \(s\) packets over every root, then, for every \(y\) supported on \(\mathcal Q\),

\[
 y(\mathcal Q)\le sN\max_Py_P\le sN\nu_y.
\tag{4.7}
\]

Consequently any dual with ratio exceeding \(R\) must have

\[
 \max_A|\mathcal Q\cap\mathscr P_A|
 \ge {R\over N}.
\tag{4.8}
\]

Since \(R/N\) grows faster than every power of \(m\), the root partition rules out every fibre-sparse support as a coefficient-one obstruction. What survives must be fibre-dense.

## 5. Root-simple strong odd cycles still have growing rank

The root partition does not balance the catalogue incidence matrix.

### Theorem 5.1 (literal growing root-simple odd cycles)

For every odd integer

\[
 3\le\ell\le m-H+2,
\tag{5.1}
\]

the rooted middle catalogue \(\mathcal G_0\) contains a strong odd Berge cycle of length \(\ell\) whose packet columns have distinct roots and whose cycle rows are all middle targets.

#### Proof

Choose a set \(K\) of size \(m-1\), distinct labels

\[
 a_0,\ldots,a_{\ell-1}\notin K,
\]

and a set \(F\) of size \(H-1\), disjoint from \(K\) and all the labels. This is possible because

\[
 \ell+H-1\le m+1=|[2m]\setminus K|.
\]

Put indices modulo \(\ell\), and define

\[
 X_i=K\cup\{a_i\},
 \qquad
 U_i=K\cup F\cup\{a_i,a_{i+1}\},
 \qquad
 A_i=U_i^c.
\tag{5.2}
\]

Then \(|X_i|=m\), \(|U_i|=m+H=M\), and the roots \(A_i\) are distinct. Order \(K=(k_1,\ldots,k_{m-1})\) and \(F=(f_1,\ldots,f_{H-1})\). On \(U_i\), take the cyclic order

\[
 \pi_i=
 (a_i,k_1,\ldots,k_{m-1},a_{i+1},f_1,\ldots,f_{H-1}).
\tag{5.3}
\]

Its length-\(m\) window beginning at \(a_i\) is \(X_i\), and the next window is \(X_{i+1}\). No other \(X_j\) lies in \(U_i\), since \(U_i\) contains no label other than \(a_i,a_{i+1}\). Thus, on rows \(X_0,\ldots,X_{\ell-1}\) and columns

\[
 P_i=P(A_i,\pi_i),
\]

column \(P_i\) has ones exactly in rows \(X_i,X_{i+1}\). Each row likewise has two ones. The resulting odd square submatrix is a strong odd Berge cycle. \(\square\)

### Consequences

1. Adding the nested-rank rows cannot destroy this submatrix; balancedness is hereditary under row deletion.
2. Root rows do not meet the displayed cycle because its columns have distinct roots and the root rows were not selected.
3. Every cycle passage is a same-rank middle pair and lies in the \(O(R/m^2)\) codegree tier. Hence this example is compatible with the rare-passage chronology reduction.
4. The \(p=2\) target-capacity row on \(\{X_0,\ldots,X_{\ell-1}\}\) detects this individual odd cycle, but the diagonal capacity census does not provide a common decomposition for many interlocked copies.

The displayed cycle alone is not an \(R\)-scale dual obstruction: it uses one packet per root, and (4.7) makes every root-simple support negligible because \(N=o(R)\). Its purpose is sharper: it proves that root partitioning does not imply balancedness, bounded odd rank, or elimination of the physical rare-passage mechanism. A harmful obstruction would have to embed many such minors in a fibre-dense support.

## 6. Why the existing physical-port theorem does not transfer automatically

There are four distinct gaps.

### 6.1 Packet columns are chronological unions

The selected physical-port theorem is proved for one strip column with an independently selected set of its physical target ports. A promotion packet is the union of \(M\) phase chains constrained to be the windows of one cyclic order. Replacing it by \(M\) independent strip columns loses the requirement of one tight Hamilton cycle on \(U=A^c\).

### 6.2 Independent port thinning is not literal here

At the middle rank, every active phase literally owns its length-\(m\) window. Deleting that incidence while retaining the packet would allow two selected rings to repeat an owner without recording a conflict. At the nested ranks, arbitrary deletion similarly breaks the symmetric-chain target ledger. Capacity cloning may label legal repetitions, but it cannot erase literal primary incidences.

Thus the product-hypersimplex port selection used for physical strips is not a legal regularization of the promotion catalogue.

### 6.3 The localized EKR and off-edge-star inputs must be reproved

The pair degrees (1.9)--(1.11) are favorable, and adjacent nested ranks have the known \(\Theta(1/m)\) relative codegree. But the arbitrary-dual theorem also uses a weighted nonstar EKR theorem and an adaptive off-edge-star kernel for its exact physical strip geometry. Neither statement has been proved for unions of cyclic-order packets. Degree and pair-codegree formulae alone do not supply them.

### 6.4 Root rows do not close the odd core

For a set \(B\) of root vertices and every \(p\ge2\), each packet satisfies

\[
 \left\lfloor{|e_P\cap B|\over p}\right\rfloor=0,
\tag{6.1}
\]

because it has exactly one root. Hence every pure-root target-capacity row of order at least two is identically zero. The root star rows say only “at most one packet per root”; they do not say that one common matching meets almost every root.

The latter is the lower-transversal assertion extracted from fractional edge colouring in Lemma 2.1. It is not an upper-capacity inequality.

## 7. Final theorem-grade boundary

### Theorem 7.1 (rooted promotion-ring arbitrary-dual reduction)

The following statements are proved.

1. The concrete middle rooted catalogue has root degree \(R=(M-1)!\), middle degree \(\rho R\), and maximum relative nonroot pair codegree \(2/m^2\).
2. An arbitrary-dual estimate \(\chi_f'\le R+o(R/\sqrt m)\) would yield a middle near-resolution covering \(W-o(W)\) owners.
3. For a fixed packing-side truncated tag census, the all-depth extension additionally requires the one-sided degree-balance condition \(\mathfrak D=o(W)\); together with \(\chi_f'\le D_{\rm tag}+o(D_{\rm tag}/\sqrt m)\) it yields total band holes \(o(W)\).
4. Every fibre-sparse dual support is negligible at the \(R\)-scale.
5. Nevertheless the rooted catalogue contains root-simple strong odd cycles of every growing odd length up to \(m-H+2\), so root partitioning does not remove the rank-diverging odd-minor mechanism.
6. All current target-capacity rows are insufficient to force the weighted root transversal (4.5), and the physical-strip EKR/star-peeling theorem has not been transferred to tight-Hamilton packet unions.

Therefore the physical-port arbitrary-dual machinery gives an exact and attractive sufficient route to promotion-ring near-resolution, but not a completed proof. The root partition sharpens the residual obstruction from an arbitrary rank-diverging odd core to a **fibre-dense, root-transversal-interlocked odd core**. Closing the catalogue requires a new packet-level arbitrary-dual theorem; the weighted representative bound (4.5) is one sufficient form. It must be combined with the tag-degree balance (3.6), or replaced by a packet-specific analogue of the localized EKR and physical chronology peeling strong enough to imply both conclusions.

## 8. Dependency ledger

This audit uses:

- TOP_FIBRE_PROMOTION_PACKET_REDUCTION_20260725.md for the exact packet degrees, same-rank codegrees, nested codegrees, and fractional root selection;
- MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md for the literal promotion-ring and tagged nested-target formula;
- MATH_AUDIT_CRITICAL_FULL_TOP_PROMOTION_RING_HEAT_AND_TAIL_20260726.md for the exact tag census and the fixed-tag mean-degree gate;
- MATH_THEOREM_PHYSICAL_PORT_ARBITRARY_DUAL_STAR_PEELING_AND_ODD_CORE_REDUCTION_20260726.md and MATH_AUDIT_PHYSICAL_PORT_CAPACITY_STAR_PEELING_AND_PARITY_CHRONOLOGY_20260726.md for the arbitrary-dual, balanced-core, and rare-passage reductions;
- MATH_THEOREM_FINE_STRIP_WEIGHTED_STAR_PEELING_AND_ODD_CAPACITY_CLOSURE_20260726.md for the target-capacity outer rows.

No generic growing-rank matching or edge-colouring theorem is invoked.
