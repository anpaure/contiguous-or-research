## Lane R verdict

Positive-density PBBS rebundling is not proved. The route does, however, reduce to a sharp and lossless obstruction:

> Every balanced component-increasing alternating \(C_8\) requires a clean directed \(4\)-cycle on at most six PBBS residual labels, together with either a centered cut segment or an opposite pair of segment vectors.

Neither PBBS homomesy nor the odd-gap rule supplies these proper cancellations. The decisive constants and implications below were independently audited.

### 1. Complete alternating-\(C_8\) balance theorem

Let \(F\) be a componentwise point-regular spanning \(2\)-factor of

\[
O_m=KG(2m+1,m),\qquad n=2m+1,
\]

and let \(Z\) be a simple \(F\)-alternating \(C_8\). Put \(F'=F\triangle Z\).

Deleting the four old factor edges leaves four paths \(P_1,\ldots,P_4\). Define

\[
\zeta(P_i)
=n\sum_{A\in P_i}\mathbf1_A-m|P_i|\mathbf1.
\]

Let \(\mathcal O,\mathcal N\) be the partitions of \([4]\) according to the old and new touched components.

The bipartite incidence multigraph with vertex classes \(\mathcal O,\mathcal N\) and one edge for each \(P_i\) is connected. Otherwise the alternating \(C_8\) itself would split into two alternating subcycles. Hence, writing \(r=|\mathcal O|\), \(s=|\mathcal N|\),

\[
r+s\le5.
\]

The possible ordered cut-shape pairs are consequently among

\[
\begin{array}{c|l}
\text{old shape}&\text{new shapes}\\ \hline
4&4,31,22,211,1111\\
31&4,31,22,211\\
22&4,31,22,211\\
211&4,31,22\\
1111&4.
\end{array}
\]

Old point regularity gives

\[
\sum_{i\in B}\zeta(P_i)=0\qquad(B\in\mathcal O),
\]

and \(F'\) is componentwise point regular exactly when

\[
\boxed{\sum_{i\in B}\zeta(P_i)=0\qquad(B\in\mathcal N).}
\]

The connected incidence matrix has rank \(r+s-1\). Thus, modulo the old equations, new balance imposes exactly \(s-1\) independent vector equations. In particular, only a one-output merge or one-component reordering is automatic.

For the new cut shapes this specializes to:

\[
\begin{array}{c|l}
\text{new shape}&\text{exact balance condition}\\ \hline
4&\text{automatic}\\
31&\zeta(P_i)=0\text{ for the singleton}\\
22&\zeta(P_i)=-\zeta(P_j)\text{ for one pair}\\
211&\text{both singleton vectors vanish}\\
1111&\zeta(P_1)=\cdots=\zeta(P_4)=0.
\end{array}
\]

Therefore every genuine balanced split requires either a centered segment or an opposite pair. Generic four-vector cancellation is insufficient.

### 2. Exact omitted-label form

For a path \(P=(A_0,\ldots,A_{L-1})\), let \(t_x(P)\) count internal edges labelled \(x\), and let

\[
e_x(P)=\mathbf1_{x\in A_0}+\mathbf1_{x\in A_{L-1}}.
\]

Then

\[
\boxed{2\zeta(P)=n(e(P)-t(P))+(L-n)\mathbf1.}
\]

More generally, suppose a new component is sewn from \(h\) paths of total length \(kn\). If \(t_x\) is their combined internal-label count and \(a_x\) counts the added seam edges labelled \(x\), then

\[
\boxed{\text{new component is point regular}
\iff t_x+a_x=k\quad\text{for every }x.}
\]

Indeed, the endpoint incidence satisfies \(e_x=h-a_x\), and summing the preceding path identity gives the result.

For \(k=1\), the new edge-label word is a permutation, so the component is literally a wreath. Thus a one-switch wreath output requires exact uniform completion of every omitted label, not merely correct length.

### 3. Clean directed-\(C_4\) dictionary

For \(K\in\binom{[n]}{m-1}\), put \(B=[n]\setminus K\). Define a directed graph \(D_K^F\) on \(B\) by

\[
u\longrightarrow v
\iff
F\text{ contains }
\{K\cup\{u\},\,B\setminus\{u,v\}\}.
\]

Every vertex has outdegree two.

An alternating \(C_8\) relative to \(F\) is equivalent to a clean directed cycle

\[
u_0\to u_1\to u_2\to u_3\to u_0
\]

in \(D_K^F\), where “clean” means that all four reverse arcs

\[
u_i\to u_{i-1}
\]

are absent. The old edges are the forward matching; the reverse arcs are exactly the proposed new edges. The universal odd-\(C_8\) normal form makes \(K\) unique.

### 4. PBBS six-label bottleneck

Let \(F_{\rm PBBS}\) be the canonical parenthesis-flip factor. For an \((m-1)\)-set \(K\), let \(U_+(K)\) and \(U_-(K)\) be its three unmatched zeros under forward and reverse cyclic parenthesis matching.

If \(u\notin K\), then the two PBBS edge labels at \(K\cup\{u\}\) satisfy

\[
r_+(K\cup\{u\})\in U_+(K),\qquad
r_-(K\cup\{u\})\in U_-(K).
\]

This follows by writing the deficit-three word as three unmatched zeros separated by Dyck blocks: changing any zero to a one consumes two of the old unmatched zeros and leaves the third. The reverse statement is identical because reverse matching realizes the inverse PBBS map.

Hence every arc of \(D_K^{F_{\rm PBBS}}\) enters

\[
S_K=U_+(K)\cup U_-(K),\qquad |S_K|\le6.
\]

Every directed \(C_4\) lies wholly in \(S_K\). Rooting such a cycle, there are at most \(2^3\) choices for its first three directed steps, followed by a closure test. Dividing by four roots gives at most \(12\) directed \(C_4\)'s per core. Therefore

\[
\boxed{
\#\{\text{PBBS-supported alternating }C_8\}
\le12\binom{n}{m-1}
=12\frac{m}{m+2}W
<12W.
}
\]

The independent audit also confirmed:

\[
\boxed{\text{each PBBS factor edge lies in at most }8m\text{ such }C_8\text{s},}
\]

and each middle vertex lies in at most \(16m\).

Consequently, if one could separately prove an \(\Omega(W)\) lower bound on clean cycles, a greedy argument would still give \(\Omega(W/m)=\Omega(W/n)\) vertex-disjoint connectors. Thus the \(12W\) upper bound is a sharp supply gate, not a no-density theorem.

### 5. Quantitative rebundling potential

Let

\[
C_m=\frac Wn,
\qquad
E(F)=C_m-\#\{\text{components of }F\}.
\]

If a component has length \(\ell n\), call \(\ell\) its level. Let \(L(F)\) be the number of vertices in components of level at least two. Then

\[
\boxed{nE(F)\le L(F)\le2nE(F).}
\]

Hence all but \(o(W)\) vertices lie in wreaths exactly when \(E(F)=o(C_m)\).

For an alternating \(C_8\) with \(r\) old and \(s\) new touched components,

\[
E(F')-E(F)=r-s.
\]

Since \(r+s\le5\),

\[
\boxed{E(F)-E(F')\le3.}
\]

Thus, if the PBBS factor has \(E(F_{\rm PBBS})=\Theta(C_m)\), reaching even \(E=o(C_m)\) requires \(\Omega(C_m)=\Omega(W/n)\) net splitting switches. A bounded local template cannot suffice.

A near-wreath factor is not yet an exact wreath factor. Discarding its long components leaves \(L(F)\) uncovered middle vertices, and no integral cyclic completion theorem for that leave is known.

### 6. Sharp existing barriers

The balance-only obstruction is already quantitatively strong:

- For infinitely many \(n=4k+1\), there are simple point-regular \(3n\)-cycles with no proper centered segment. Every \(n\)-vertex segment satisfies

  \[
  \|\zeta(P)\|_1
  \ge2n\left\lfloor\frac{n-1}{6}\right\rfloor.
  \]

  The \(n=9\) member is an actual PBBS component.

- In the label-preserving four-edge model, odd-gap balanced words can require at least

  \[
  \frac14\left\lceil\frac n6\right\rceil
  \]

  directed-four-cycle reversals before any proper balanced component appears.

The second construction is not generally a simple PBBS orbit, so it does not disprove PBBS rebundling. It proves that an \(O(1)\)-switch routing lemma cannot follow from homomesy and odd gaps alone; the natural unresolved scale is \(\Theta(n)\) coordinated switches.

### 7. First-wave correction and implication scope

Once actual wreaths exist, every rooted four-label window has exactly

\[
(m-1)!(m-2)!
\]

profile-\(3\) partner wreaths. Their exact removal/addition masses are

\[
r_1=8,\qquad r_q=4q+6\quad(2\le q\le m-1),
\]

with zero depth-\(m\) effect. But these are ambient partners, not partners already selected in the same exact factor.

For fixed \(A\), one such trade changes the overload or labelled objective by \(O_A(m)\). Therefore \(o(C_m)\) local trades change either objective by only \(o(W)\). A sparse absorber cannot repair a linear defect; positive-density coarse rebundling is genuinely necessary.

## Exact remaining unproved lemmas

1. **Clean-cycle lower bound:** prove \(\Omega(W)\) clean directed \(C_4\)'s across the PBBS auxiliary digraphs. This alone is insufficient.

2. **Compatible cancellation density:** prove that sufficiently many legal connectors carry a zero segment or opposite segment pair with the required new component topology.

3. **Dynamic routing:** prove an \(O(n)\)-scale balanced switch route that lowers \(E\) despite temporary merges and reorderings. The linear fragmentation barrier shows this scale may be optimal.

4. **Integral cleanup:** convert a near-wreath factor into one exact wreath factor without discarding or independently refactoring its leave.

5. **Shadow control:** even \(E=0\) only gives an exact wreath factor. It does not imply fixed-window overload, MWB, or labelled common-owner synchronization.

Accordingly lane R isolates the precise obstruction but does not prove positive-density rebundling, MWB, SYNC, or the coefficient-one OR theorem. No files were edited.

Relevant audited sources: [balanced inter-orbit switching](/Users/amir.nuriyev/Documents/problem/PBBS_BALANCED_INTERORBIT_SWITCHING_20260724.md), [odd-\(C_8\) context audit](/Users/amir.nuriyev/Documents/problem/PBBS_ODD8_CONTEXT_LIFT_AUDIT_20260724.md), [label-arc barriers](/Users/amir.nuriyev/Documents/problem/BALANCED_LABEL_ARC_BARRIERS_20260724.md), and [first-wave synthesis](/Users/amir.nuriyev/Documents/problem/MATH_ATTACK_FIRST_WAVE_SYNTHESIS_20260724.md).
