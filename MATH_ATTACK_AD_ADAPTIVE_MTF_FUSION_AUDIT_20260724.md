# Adversarial audit of adaptive MTF fusion

Date: 2026-07-24

## Verdict

**PASS WITH MATERIAL SCOPE CORRECTIONS.**

The endpoint-throughput theorem, the depth-two shared-seam construction, the canonical adaptive MTF recurrence, the \(K+2H+1\) component length, the cut count, the recovery of every deleted first-band edge colour, the forest bound (17), and the fixed-\(A\) implication to a literal coefficient-one OR word are valid after the hypotheses below are made explicit.

The report needs the following corrections and scope qualifications.

1. The private-substitution lower bound \(E\ge \lceil(N_2-2c_+)/2\rceil\) is valid only for a union-preserving private refinement model in which a length-one replacement is unchanged. It is false for arbitrary in-place substitutions.
2. The depth-two formula is an exact length for the declared canonical-support completion policy, but only an upper bound for an optimal completion, because incidental and cross-component intervals may already cover masks outside the canonical supports.
3. The exact \(K+2H+1\) MTF length requires \(\Theta _0\) to consist of exactly \(H\) singleton blocks and one nonempty residual block. Merely requiring its first \(H\) blocks to be singletons is insufficient.
4. The equality \(P^-_{i,q}=\bigcap_{s=0}^qT_{i+s}\) holds only when \(i+q\le K-1\). At the right boundary the deletion formula using dummy departures remains valid, but the displayed intersection is undefined unless dummy middle states are also supplied.
5. The assertion that the future-deletion core \(L_i\) is forced by the middle chronology is true for the report's explicit canonical lift, not for every saturated one-update MTF lift. A concrete counterexample is given in Section 4 below.
6. In the first-band completion ledger, \(e\) must count certified edges whose lower colours are pairwise distinct and whose upper colours are pairwise distinct separately. Distinct ordered lower-upper pairs alone do not give the term \(2(N_1-e)\).
7. The identity \(c=W-e\) applies only when those \(e\) certified edges are all the forest edges. If uncertified splice edges are present, the correct relation is \(c=W-|E(F)|\le W-e\).
8. The improvement to \((2H+1)\rho_H\) is the explicit reset charge, not an unconditional bound on every loss attributable to cutting: the adaptive support defects can still deteriorate on an \(H^2\rho_H\) scale.

No proof of \((\mathrm{AD}_A)\) is obtained. The surviving missing statement is a joint dynamic theorem for one oriented spanning chronology and one compatible set of MTF boundary choices; separate minimizers of the component count, short-run count, and adaptive support defects do not suffice.

## 1. Endpoint throughput

Let \(A=(A_1,\ldots,A_L)\) be a linear OR word and let \(\mathcal R_r(A)\) be the represented \(r\)-sets.

### Theorem 1.1

For every \(r\),

\[
\boxed{
|\mathcal R_r(A)|
\le \#\{j:|A_j|\le r\}.
}
\tag{1.1}
\]

#### Proof

Choose one witnessing interval \([\ell(S),u(S)]\) for every represented \(r\)-set \(S\). Two intervals with the same left endpoint have nested unions. Distinct equal-cardinality sets cannot be properly comparable, so \(S\mapsto\ell(S)\) is injective. Moreover \(A_{\ell(S)}\subseteq S\), hence \(|A_{\ell(S)}|\le r\). The right-endpoint proof is identical. This argument includes arbitrary seam-crossing and cross-block witnesses. ∎

For

\[
W=\binom{2m}{m},\qquad N_2=\binom{2m}{m-2},
\]

the exact ratio is

\[
\frac{N_2}{W}
=\frac{m(m-1)}{(m+1)(m+2)}
=1-\frac{4m+2}{(m+1)(m+2)}.
\tag{1.2}
\]

Thus every word covering rank \(m-2\) has at least \(N_2=W-O(W/m)\) letters of size at most \(m-2\).

If an old word has \(B\) such letters, inserting \(R\) positions and changing \(t\) old positions gives at most \(B+R+t\) eligible positions. Therefore

\[
\boxed{R+t\ge N_2-B.}
\tag{1.3}
\]

For the \(T\)-capped first-band word, \(B=0\). For the singleton-capped word, \(B=2c_+\) when \(m\ge3\), where \(c_+\) is the number of nontrivial components. Hence the conclusions about pure insertion, same-length replacement, and preserving the old word as a subsequence are correct at the stated \(W-o(W)\) scale.

The private-refinement statement needs the following precise model. Replace each old letter by a nonempty private block whose union is that old letter, and require a length-one block to be the unchanged old letter. If the replacement lengths are \(\ell_j\) and

\[
E=\sum_j(\ell_j-1),
\]

then every high old letter which creates a low endpoint needs \(\ell_j\ge2\). The number of such blocks is at most \(E\), so the final number of low positions is at most \(B+2E\). Consequently

\[
\boxed{
E\ge\left\lceil\frac{N_2-B}{2}\right\rceil.
}
\tag{1.4}
\]

Without this convention arbitrary one-letter substitutions can change high letters to low letters with zero length overhead, so (1.4) would be false.

For \(H=\lfloor A\sqrt m\rfloor\) and \(d_j=(m-|A_j|)_+\), summing (1.1) over \(q=2,\ldots,H\) gives exactly

\[
\boxed{
\sum_j(\min\{H,d_j\}-1)_+
\ge\sum_{q=2}^{H}\binom{2m}{m-q}.
}
\tag{1.5}
\]

Indeed, the contribution of position \(j\) is the number of integers \(q\in[2,H]\) with \(q\le d_j\). Uniformly for fixed \(A\),

\[
\frac{\binom{2m}{m-q}}W
=\exp\!\left(-\frac{q^2}{m}+O_A(m^{-1/2})\right),
\]

so the Riemann sum yields

\[
\boxed{
\frac1{W\sqrt m}
\sum_j(\min\{H,d_j\}-1)_+
\ge\int_0^Ae^{-t^2}\,dt+o_A(1).
}
\tag{1.6}
\]

The endpoint lower bounds and their constants are therefore accepted. Their scope is architectural: they rule out a \(W+o(W)\) sparse appendage or private refinement of the first-band word, not a pervasive replacement such as the MTF construction.

## 2. Depth-two shared-seam word

Assume \(m\ge3\) and let a globally two-sided-rainbow spanning linear forest in \(J(2m,m)\) be oriented componentwise. For a nontrivial component

\[
T_0,T_1,\ldots,T_s
\]

write its transitions as

\[
T_j=T_{j-1}-\{r_j\}+\{b_j\},\qquad 1\le j\le s.
\]

Put

\[
C_i=T_{i-1}\cap T_i,\qquad
U_i=T_{i-1}\cup T_i,
\]

\[
D_i=C_i\cap C_{i+1},\qquad
V_i=U_i\cup U_{i+1},
\]

and

\[
a_0=T_0\setminus T_1,\qquad
a_s=T_s\setminus T_{s-1}.
\]

Adjacent \(C_i\)'s are distinct \((m-1)\)-subsets of \(T_i\), and adjacent \(U_i\)'s are distinct \((m+1)\)-supersets of \(T_i\). Hence

\[
|D_i|=m-2,\qquad |V_i|=m+2.
\tag{2.1}
\]

Writing the transitions with removed and added coordinates, one obtains for every internal facet

\[
D_{i-1}=C_i\setminus\{b_{i-1}\},\qquad
D_i=C_i\setminus\{r_{i+1}\}.
\]

Thus

\[
C_i\setminus(D_{i-1}\cup D_i)
\]

is empty unless \(b_{i-1}=r_{i+1}=x_i\), in which case it is \(\{x_i\}\). The exceptional case is exactly the coordinate trace \(0,1,1,0\). Let \(Z_i\) be omitted in the first case and equal \(\{x_i\}\) in the second. Then

\[
C_i=D_{i-1}\cup Z_i\cup D_i.
\tag{2.2}
\]

For \(s=1\), emit \(a_0,C_1,a_s\). For \(s=2\), emit

\[
a_0,C_1,D_1,C_2,a_s.
\]

For \(s\ge3\), emit

\[
a_0,C_1,D_1,Z_2,D_2,\ldots,Z_{s-1},D_{s-1},C_s,a_s,
\tag{2.3}
\]

omitting empty \(Z_i\)'s. Every internal \(C_i\) is an interval union \(D_{i-1}\cup Z_i\cup D_i\). Consecutive facet hulls recover the \(T_i\); consecutive middle hulls recover the \(U_i\); and consecutive upper hulls recover the \(V_i\). Hence all advertised masks are literal contiguous unions.

Let \(c_1\) count one-edge components, \(c_{\ge2}\) components with at least two edges, and \(\rho_2\) internal positive runs of exact length two. Including isolated middle vertices literally, the raw word has exactly

\[
W+c_1+2c_{\ge2}+\rho_2
\tag{2.4}
\]

entries.

Define the canonical depth-two support defects by

\[
M_2^-=N_2-|\{D_i\}|,\qquad
M_2^+=N_2-|\{V_i\}|.
\tag{2.5}
\]

Write \(N_1=\binom{2m}{m-1}\). If the forest has \(e\) edges, appending every mask outside the canonical supports gives an explicit five-band word of exactly

\[
\boxed{
W+2c_{\ge2}+c_1+\rho_2
+2(N_1-e)+M_2^-+M_2^+.
}
\tag{2.6}
\]

As a statement about an optimal completion, (2.6) is only an upper bound: incidental intervals, including cross-component intervals, may already cover additional masks.

The number of \(D\)-occurrences is

\[
K_2=e-c_1-c_{\ge2}.
\]

Every length-two positive run gives an equality between adjacent \(D\)-occurrences. In a path, the number of such equality edges for each value is at most its occurrence multiplicity minus one. Therefore

\[
\boxed{
\rho_2
\le e-c_1-c_{\ge2}-N_2+M_2^-
\le W-N_2+M_2^-.
}
\tag{2.7}
\]

This proves the reported weaker bound (6). For the existing near-spanning forest, \(N_1-e=o(W)\) and \(c_1+c_{\ge2}=o(W)\). Thus \(M_2^-+M_2^+=o(W)\) is exactly the vanishing-overhead gate for the declared canonical-support ledger. It is not necessary for a different or optimally completed five-band word.

Depth-one rainbowness does not imply depth-two injectivity, even for adjacent windows. For four distinct coordinates \(a,b,c,d\) and \(R\in\binom{[2m]\setminus\{a,b,c,d\}}{m-2}\), the path

\[
Rab,\ Rbc,\ Rcd,\ Rda
\]

has distinct lower and upper first-band colours, but

\[
D_1=D_2=R,\qquad V_1=V_2=Rabcd.
\]

Thus the support defect in (2.5) is a genuine new condition.

## 3. Corrected adaptive MTF theorem

Let \(1\le H\le m/2\) and let

\[
T_{i+1}=T_i-\{p_i\}+\{q_i\},
\qquad 0\le i\le K-2,
\tag{3.1}
\]

be a finite Johnson walk. An \(H\)-saturated one-step MTF lift means ordered partitions \(\Pi_i\) such that \(T_i\) is the rank-\(m\) prefix, every rank \(m-H,\ldots,m+H\) is a prefix rank, and

\[
\Pi_{i+1}=M_{X_i}(\Pi_i)
\]

for one nonempty update mask per Johnson edge.

### Theorem 3.1

Such a lift exists if and only if

\[
q_a=p_b,\quad 0\le a<b\le K-2
\quad\Longrightarrow\quad
b-a\ge H+1.
\tag{3.2}
\]

Equivalently, there is no internal positive coordinate run of length at most \(H\). No condition on zero-runs is necessary.

### Sufficiency

Put

\[
a=\max(0,K-H-1),\qquad
I=\bigcap_{t=a}^{K-1}T_t.
\]

At most \(H\) transitions occur in this suffix, so

\[
|I|\ge m-H\ge H.
\]

Choose distinct \(d_0,\ldots,d_{H-1}\in I\) and set

\[
p_{K-1+r}=d_r,\qquad 0\le r<H.
\tag{3.3}
\]

The no-short-run condition and (3.3) imply that every required list \(p_i,\ldots,p_{i+H}\) is distinct and contained in \(T_i\). Define

\[
L_i=T_i\setminus\{p_i,\ldots,p_{i+H-1}\}.
\tag{3.4}
\]

Choose distinct \(z_1,\ldots,z_H\in T_0^c\) and, crucially, set

\[
\Theta_0=(\{z_1\},\ldots,\{z_H\},R_0),
\qquad
R_0=T_0^c\setminus\{z_1,\ldots,z_H\}.
\tag{3.5}
\]

Since \(m-H\ge H\ge1\), \(R_0\ne\varnothing\). Recursively set

\[
\Theta_{i+1}=(\{p_i\},\Theta_i-\{q_i\})
\tag{3.6}
\]

and

\[
\Pi_i=(L_i,\{p_{i+H-1}\},\ldots,\{p_i\},\Theta_i).
\tag{3.7}
\]

Each \(\Theta_i\) partitions \(T_i^c\). If \(q_i\) is one of its first \(H\) singleton blocks, deleting that block leaves \(H-1\) old leading singletons and prepending \(\{p_i\}\) restores \(H\). If \(q_i\) lies later, all first \(H\) survive and \(\{p_i\}\) supplies one more. Hence arbitrary short zero-runs are harmless.

Directly,

\[
L_{i+1}=(L_i\setminus\{p_{i+H}\})\cup\{q_i\}.
\tag{3.8}
\]

Applying \(M_{L_{i+1}}\) to (3.7) gives

\[
\begin{aligned}
M_{L_{i+1}}(\Pi_i)
={}&(L_{i+1},\{p_{i+H}\},\ldots,\{p_{i+1}\},
\{p_i\},\Theta_i-\{q_i\})\\
={}&\Pi_{i+1}.
\end{aligned}
\tag{3.9}
\]

Thus the report's state recurrence is exact.

The exposed masks are

\[
P^-_{i,q}
=T_i\setminus\{p_i,\ldots,p_{i+q-1}\},
\qquad 0\le q\le H,
\tag{3.10}
\]

and

\[
P^+_{i,q}
=T_i\cup\{\text{first \(q\) singleton blocks of }\Theta_i\}.
\tag{3.11}
\]

When \(i+q\le K-1\),

\[
P^-_{i,q}=\bigcap_{s=0}^qT_{i+s}.
\tag{3.12}
\]

Near the right boundary, (3.10) remains valid using dummy departures, but (3.12) is not an identity among actual path vertices. At depth one,

\[
P^-_{i,1}=T_i\cap T_{i+1},\qquad
P^+_{i+1,1}=T_i\cup T_{i+1}.
\tag{3.13}
\]

Hence all original two-sided depth-one colours survive exactly.

The state \(\Pi_0\) in (3.5)–(3.7) has exactly \(2H+2\) blocks. Writing these blocks in reverse and then appending \(L_1,\ldots,L_{K-1}\) gives exactly

\[
\boxed{K+2H+1}
\tag{3.14}
\]

nonempty word entries.

### Necessity

In any one-step MTF lift, the entering coordinate \(q_i\) must belong to the new first block. Otherwise it remains in an old tail block after the residual old middle block containing \(p_i\), so no prefix can include \(q_i\) while excluding \(p_i\).

The block containing \(q_i\) therefore starts at position one. Each later update either refreshes it to position one or creates at most one additional block before its residual block. If \(q_i=p_j\) and \(\ell=j-i\), its block position immediately before departure is at most \(\ell\). At the departure step, the new middle prefix must stop before the residual block containing \(q_i\), so its block depth is at most \(\ell\).

Exposure of every rank \(m-H,\ldots,m\) forces the middle prefix to contain at least one nonempty block reaching rank \(m-H\), followed by \(H\) singleton increments. Its depth is therefore at least \(H+1\). Hence \(\ell\ge H+1\), proving (3.2).

The report's phrase “\(H+1\) later blocks must precede it” is off by one: at least \(H\) blocks must precede it, so its position must be at least \(H+1\). The resulting prohibition of runs of length at most \(H\) is correct.

Theorem 3.1 is a local theorem for a finite linear walk. It gives no global support distinctness, no cyclic closure, and no estimate for the adaptive defects in \((\mathrm{AD}_A)\). Necessity uses only the lower ranks through \(m-H\); the construction supplies the upper ranks as well.

## 4. The future-deletion core is not universally forced

In the explicit construction, (3.4) is of course forced once that construction and its constant block layout are chosen. It is not forced among all saturated one-step lifts of the same middle chronology.

Here is a one-edge counterexample for \(H=1\) and \(m\ge4\). Choose four distinct coordinates \(y,p,x,q\) and a set \(R\) of size \(m-3\) disjoint from them, and put

\[
T_0=R\cup\{y,p,x\},\qquad
T_1=R\cup\{y,x,q\}.
\]

Let \(\Theta\) partition the complement of \(T_0\) and begin with a singleton block. Define

\[
\Pi_0=(\{y\},\{p\},R,\{x\},\Theta)
\]

and use the update mask

\[
X=R\cup\{x,q\}.
\]

Then

\[
M_X(\Pi_0)=(X,\{y\},\{p\},\Theta-\{q\})=:\Pi_1.
\]

The state \(\Pi_0\) exposes ranks \(m-1,m,m+1\): its rank-\((m-1)\) prefix is \(R\cup\{y,p\}\), its middle prefix is \(T_0\), and the first singleton of \(\Theta\) supplies rank \(m+1\). The state \(\Pi_1\) exposes the same three ranks using \(X\), \(X\cup\{y\}=T_1\), and \(X\cup\{y,p\}\).

However, the canonical future-deletion core would be

\[
T_0\setminus\{p\}=R\cup\{y,x\},
\]

which is not the exposed rank-\((m-1)\) prefix \(R\cup\{y,p\}\). The flag depth drops from four blocks to two, which is allowed while remaining \(H\)-saturated.

Therefore the report's final “forced core” paragraph must be read as a statement about its explicit canonical MTF refactor. A different separately chosen core is not ruled out in principle; realizing one would require a different global MTF state-transversal theorem, as the report's final alternative already suggests.

## 5. Cutting short runs and preserving cut colours

Let an oriented spanning linear forest have \(c\) components, \(e\) certified edges whose lower colours are pairwise distinct and whose upper colours are separately pairwise distinct, and \(\rho_H\) internal positive runs of length at most \(H\).

Cut the **entry edge** of every such run. One Johnson edge adds only one coordinate, so distinct runs have distinct entry edges. Deleting all these edges raises the component count exactly to

\[
\boxed{c+\rho_H.}
\tag{5.1}
\]

Adjacent cuts merely create singleton components. Cutting cannot create a new internal short run; every remaining internal run was already internal before cutting.

Consider a cut edge

\[
T\longrightarrow T'=T-\{p\}+\{q\}.
\]

Its lower colour is \(T-p\) and its upper colour is \(T'+p=T\cup T'\). On the left component prescribe \(p\) as the first terminal dummy departure. On the right prescribe \(p\) as the first initial upper singleton. The right prescription is legal because \(p\notin T'\).

For the left prescription, trace \(p\) backwards from \(T\) inside the post-cut left component. If \(p\) became absent within the preceding \(H\) transitions, its most recent entry together with the present exit would form an internal positive run of length at most \(H\). That entry edge would also have been cut, so it could not lie inside the same post-cut component. Hence \(p\) belongs to every one of the last \(\min(H+1,K_{\rm left})\) middle states. The terminal intersection therefore contains \(p\) and has size at least \(m-H\ge H\), so \(H-1\) further distinct dummies can be chosen.

Consequently

\[
P^-_{{\rm last},1}=T-p,
\qquad
P^+_{{\rm first},1}=T'+p,
\]

and every certified first-band colour of every deleted edge is retained without extra word entries. Incoming-upper and outgoing-lower boundary prescriptions on the same component are independent.

## 6. Forest length and adaptive supports

For each post-cut component with \(K\) middle vertices, choose the exact initialization (3.5). Its word has \(K+2H+1\) entries. Since the forest is spanning, summing \(K\) gives \(W\). Therefore the raw concatenated word has exactly

\[
\boxed{W+(2H+1)(c+\rho_H)}
\tag{6.1}
\]

entries, including singleton components.

For \(q\ge2\), define globally across all post-cut components

\[
\mathcal L_q=\{P^-_{i,q}:\text{all middle states for the chosen boundary data}\},
\qquad
\mathcal U_q=\{P^+_{i,q}:\text{all middle states for the chosen boundary data}\},
\]

as **sets** of labels, not occurrence multisets, and put

\[
\widetilde M_q^-=N_q-|\mathcal L_q|,
\qquad
\widetilde M_q^+=N_q-|\mathcal U_q|.
\tag{6.2}
\]

Here “boundary choices” means the one jointly chosen compatible boundary assignment: the supports range over all middle states for that assignment, not over the union of every possible assignment.

All orientations, free dummy departures, initial singleton choices, residual blocks, and the forced cut-colour prescriptions are part of the existential data defining these supports. The defects are not functions of the unoriented middle forest alone.

There are \(W\) designated occurrences per signed depth. If \(D_q^\pm\) is the occurrence-duplicate excess, then exactly

\[
D_q^\pm=W-|\mathcal L_q\text{ or }\mathcal U_q|
=(W-N_q)+\widetilde M_q^\pm.
\tag{6.3}
\]

Thus repetitions are already charged through the support defect; there is no additional duplicate term.

At depth one the retained certified colours give support size at least \(e\) on each side. Hence literal completion costs at most \(2(N_1-e)\). It need not cost exactly this much because boundary flags can add more colours. Appending every absent deeper mask once gives the rigorous bound

\[
\boxed{
L_{\rm band}
\le
W+(2H+1)(c+\rho_H)
+2(N_1-e)
+\sum_{q=2}^{H}
(\widetilde M_q^-+\widetilde M_q^+).
}
\tag{6.4}
\]

No separate deterministic \(H^2\rho_H\) erosion-loss term is hidden in (6.4). The **explicit physical reset charge** drops from \(H^2+2H\) per cut in ordinary erosion to \(2H+1\) per cut; its cost is the replacement of consecutive upper unions by adaptive recency flags. The support-defect sum can still deteriorate by as much as an \(H^2\rho_H\)-scale amount after cutting and collisions. Precisely that possibility is left to \((\mathrm{AD}_A)\); (6.4) does not by itself bound all short-run-attributable overhead by \(O(H\rho_H)\).

The bound is joint. Pairwise distinct ordered lower-upper colour pairs are not enough: the \(e\) lower colours must be mutually distinct and the \(e\) upper colours must be mutually distinct separately.

## 7. Component splicing and the remaining adaptive defect

If the original spanning forest has no uncertified edges and \(e\) denotes its total edge count, then

\[
c=W-e=\operatorname{Cat}_m+(N_1-e).
\]

More generally, when \(e\) counts only certified edges and endpoint splicing has added uncertified edges,

\[
c=W-|E(F)|\le W-e
=\operatorname{Cat}_m+(N_1-e).
\]

Thus \(N_1-e=o(W)\) implies only \(c=o(W)\), not \(Hc=o(W)\).

Unconstrained endpoint splicing can reduce the number of components to \(O(W/m)\), including in the presence of isolated vertices. Here is the required extension of the published nontrivial-path argument. At a maximal splice forest let \(c_+\) and \(c_0\) be the nontrivial and isolated component counts, and let \(S\) be the set of distinct endpoints. Then

\[
|S|=2c_++c_0,
\qquad
e_{J(2m,m)}(S)\le c_+,
\qquad
2c_+\le |S|.
\]

The Johnson spectral supersaturation inequality is

\[
2e_J(S)
\ge
\frac{m(m+1)|S|^2}{W}-m|S|.
\]

Combining the inequalities gives

\[
|S|\le\frac Wm,
\qquad
c=c_++c_0\le |S|\le\frac Wm.
\tag{7.1}
\]

Thus \(Hc=o(W)\) for fixed-\(A\), \(H=\Theta(\sqrt m)\). Reversing and concatenating paths preserves every old internal first-band colour.

This does not prove \((\mathrm{AD}_A)\). Arbitrary splices can create new short positive runs and can cause global collisions among the adaptive flags. Moreover, the current near-rainbow forest has no previously proved deep-support bound to “preserve.” The missing theorem must construct the spliced chronology while simultaneously controlling \(\rho_H\) and all supports in (6.2).

## 8. Correct surviving lemma and constants

For every fixed \(A>0\), let \(H=\lceil A\sqrt m\rceil\). For large \(m\), \(m\ge2H\). The corrected missing theorem is the following joint statement.

> **Adaptive MTF fusion lemma \((\mathrm{AD}_A)\) — UNPROVED.** There is one oriented spanning Johnson linear forest, together with all compatible cut, dummy-departure, and initial-\(\Theta\) choices, such that its certified first-band colours satisfy \(N_1-e=o(W)\) and
> \[
> H(c+\rho_H)
> +\sum_{q=2}^{H}
> (\widetilde M_q^-+\widetilde M_q^+)
> =o(W).
> \]

All \(o(W)\) terms are for fixed \(A\), and every quantity belongs to the same chronology and the same boundary data. Since \(2H+1\le3H\) for \(H\ge1\), (6.4) then gives

\[
L_{\rm band}=W+o_A(W).
\tag{8.1}
\]

The theorem is sufficient, not known necessary. A different literal OR architecture could exploit noncanonical MTF cores, cross-component witnesses, or a non-MTF chronology.

## 9. Tail, parity, and implication scope

The fixed-\(A\) implication is correct. The audited SCD-product construction covers the complementary ranks outside \(m-H,\ldots,m+H\). Its normalized limiting cost is

\[
\begin{aligned}
T(A)={}&4(A^2+\tfrac12)e^{-A^2}\operatorname{erf}(A)
+\frac{4A}{\sqrt\pi}e^{-2A^2}
+2\sqrt2\,\operatorname{erfc}(\sqrt2A)\\
={}&O((1+A^2)e^{-A^2}),
\end{aligned}
\tag{9.1}
\]

and \(T(A)\to0\).

Thus \((\mathrm{AD}_A)\) for every fixed \(A\) gives

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{\binom{2m}{m}}
\le1+T(A).
\]

One must first take \(m\to\infty\) for fixed \(A\), and only then let \(A\to\infty\). No growing-\(A\) uniformity is assumed. Sperner's lower bound supplies the reverse inequality. Finally,

\[
\nu(2m+1)\le2\nu(2m)+1,
\qquad
\binom{2m+1}{m}
=\frac{2m+1}{m+1}\binom{2m}{m},
\]

so coefficient one transfers to odd dimensions.

This lane constructs a literal contiguous-OR word directly. It proves neither MWB nor labelled wreath synchronization and uses no exact wreath factor. Its only remaining positive theorem is the joint dynamic support statement \((\mathrm{AD}_A)\).

## Final audited status

The report's central quantitative advance survives:

\[
\boxed{
\text{the explicit physical reset charge is }(2H+1)\rho_H
\text{ rather than }(H^2+2H)\rho_H.
}
\]

The endpoint lower bounds, depth-two construction, MTF recurrence, no-short-positive-run criterion, cut-colour recovery, reset constants, forest ledger, and final fixed-\(A\) implication are all rigorous with the corrections above. The unresolved issue is not MTF legality or reset accounting; it is simultaneous adaptive support control after dynamically chosen endpoint splices.
