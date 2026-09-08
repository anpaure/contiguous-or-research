# Physical-port arbitrary duals: capacity rows, star peeling, and the parity-passage chronology

**Dated audit: 2026-07-26. Constant-one lane only.**

## 0. Verdict

Let \(\mathcal H_m^\#=(V,\mathscr C)\) be the exact target-regular selected physical strip-port hypergraph, and put \(D=D_1\). The present combination

1. weighted star peeling, and
2. every indicator and fractional target-capacity row

does **not** by itself rule out the rank-diverging, matching-interlocked odd core at additive scale \(o(D/\sqrt m)\).

There is, however, a new exact physical chronology identity which sharpens the residual obstruction substantially:

> Every strong odd Berge cycle has an odd, hence nonzero, number of passages whose two physical targets have the same rank parity.

Every such passage lies in a selected pair link of size \(O(D/m^2)\), whereas a comparable rank-one flag can have size \(\Theta(D/m)\). Consequently, if all strong odd cycles can be hit by

\[
 o(m^{3/2})
\]

fixed same-parity physical pair links, then the arbitrary matching dual closes at

\[
 D+o(D/\sqrt m).
\]

Thus a genuine counterexample must be a **rare-passage mesh**: its odd cycles cannot be killed by \(o(m^{3/2})\) same-parity pair links. This is a physical, rank-chronological strengthening of the previous “matching-interlocked odd core” description.

The missing implication is also exact. Target-capacity rows count available slots for one chosen target set, but do not split those slots into a common family of physical matchings. Applied to an arbitrary dual weight they retain a factor \(b_{U,p}=\lfloor |U|/p\rfloor\). Removing that factor is precisely the matching-interlock problem, so inserting the diagonal capacity census into the weighted star-peeling induction would be circular.

Finally, the independently selected port model admits no further universal affine chronology law beyond the target-degree equations: its exact selection polytope is a product of hypersimplices. Therefore the parity-passage identity is the strongest presently visible chronology invariant which survives targetwise thinning without imposing a new correlated port-selection rule.

## 1. Audited inputs and notation

The audit uses the following proved inputs.

### 1.1 Exact target regularity

Every selected physical target has degree exactly \(D\). For distinct targets \(S,T\), write

\[
 \mathcal L(S,T)=\{C\in\mathscr C:S,T\in e_C^\#\},
 \qquad d^\#(S,T)=|\mathcal L(S,T)|.
\]

### 1.2 Pair kernels

The physical cyclic-pair calculation, followed by the simultaneously chosen exact targetwise thinning, gives uniformly in the band \(|q|\le H=o(m)\),

\[
 {d^\#(S,T)\over D}
 \le {2(r+1)\over\binom{m-H}{r}}+{C_1m\over D}
 \tag{1.1}
\]

when \(S,T\) are comparable at rank gap \(r\ge1\), and

\[
 {d^\#(S,T)\over D}
 \le {4\over(m-H)^2}+{C_1m\over D}
 \tag{1.2}
\]

when they are noncomparable and overlap. The active-disjoint expectation is superpolynomially smaller than \(D/m^2\), with the same harmless additive concentration term. Since \(D\) is exponential in the physical parameter range, \(C_1m=o(D/m^2)\).

In particular, a comparable rank-one flag may have codegree \((2+o(1))D/m\), but every distinct same-rank-parity pair satisfies

\[
 d^\#(S,T)\le \mu_{\rm even},
 \qquad
 \mu_{\rm even}\le(12+o(1)){D\over m^2}.
\tag{1.3}
\]

Indeed, a comparable same-parity pair has even gap \(r\ge2\). Since \(r\le2H=o(m)\), the right side of (1.1) is maximized at \(r=2\), where it is

\[
 {6\over\binom{m-H}{2}}+o(m^{-2})
 ={12+o(1)\over m^2}.
\]

A noncomparable pair is covered by (1.2) or the active-disjoint estimate and has the smaller leading constant \(4\).

### 1.3 Balanced coefficient one

For a strip support \(\mathcal Q\subseteq\mathscr C\), let \(A_{\mathcal Q}\) be the literal physical target-column incidence matrix. If \(A_{\mathcal Q}\) is balanced, then

\[
 \chi_f'(\mathcal Q)\le D.
\tag{1.4}
\]

Equivalently, for every nonnegative matching-dual weight \(y\),

\[
 y(\mathcal Q)\le D\nu_y,
\tag{1.5}
\]

where \(\nu_y=\max\{y(M):M\text{ a physical matching}\}\).

### 1.4 Weighted star peeling

If deleting \(t\) physical target stars leaves an intersecting support, the exact weighted peeling theorem gives

\[
 y(\mathscr C)\le (D+t\mathfrak l_m)\nu_y,
 \qquad
 {\mathfrak l_m\over D}
 =O\!\left({1\over m}+{h\over m^{3/2}}\right)+o(m^{-A}).
\tag{1.6}
\]

This closes only when

\[
 t\left({1\over\sqrt m}+{h\over m}\right)=o(1).
\tag{1.7}
\]

### 1.5 Target-capacity rows

For \(U\subseteq V\) and \(2\le p\le |U|\), set

\[
 a_{U,p}(C)=\left\lfloor {|e_C^\#\cap U|\over p}\right\rfloor,
 \qquad
 b_{U,p}=\left\lfloor {|U|\over p}\right\rfloor.
\tag{1.8}
\]

Every matching \(M\) satisfies

\[
 \sum_{C\in M}a_{U,p}(C)\le b_{U,p},
\tag{1.9}
\]

and the full column census obeys

\[
 \sum_Ca_{U,p}(C)
 \le (1+6\delta)Db_{U,p},
 \qquad \delta=O(1/m),
\tag{1.10}
\]

with \(1+\delta\) at \(p=2\). Fractional target measures obey the same statement.

## 2. The physical rank-parity chronology identity

We now use the actual target chronology, not an abstract bounded-rank hypergraph theorem.

### Definition 2.1

A strong Berge cycle of length \(\ell\) is written

\[
 T_0,C_0,T_1,C_1,\ldots,T_{\ell-1},C_{\ell-1},T_0,
\tag{2.1}
\]

where the targets \(T_i\) and strips \(C_i\) are distinct, and within the chosen rows and columns each row and column has exactly two ones. Thus

\[
 T_i,T_{i+1}\in e_{C_i}^\#
\tag{2.2}
\]

with indices modulo \(\ell\). The passage through \(C_i\) is parity-preserving when

\[
 |T_i|\equiv |T_{i+1}|\pmod 2.
\tag{2.3}
\]

### Theorem 2.2 (odd parity-passage identity)

Every strong odd Berge cycle contains an odd number of parity-preserving passages. In particular it contains at least one.

#### Proof

Let

\[
 \epsilon_i=|T_{i+1}|-|T_i|\pmod2.
\]

Because the chronology returns to \(T_0\),

\[
 \sum_{i=0}^{\ell-1}\epsilon_i=0\pmod2.
\tag{2.4}
\]

Hence the number of parity-changing passages is even. Since \(\ell\) is odd, the complementary number of parity-preserving passages is odd. \(\square\)

### Corollary 2.3 (rare physical passage)

Every strong odd Berge cycle contains a column \(C_i\) belonging to a same-parity pair link

\[
 C_i\in\mathcal L(T_i,T_{i+1})
\]

of cardinality at most \(\mu_{\rm even}=O(D/m^2)\).

This is the exact obstruction to constructing an odd cycle entirely out of the abundant comparable rank-one flags: each rank-one passage flips rank parity, so an odd number of them cannot close.

### Remark 2.4

The statement is stronger than “some passage is not a rank-one flag” in the useful direction: the forced witness has even rank difference. It therefore lands automatically in the \(D/m^2\) pair-kernel tier. No averaging over the cycle is involved.

## 3. A physical low-link transversal theorem

The parity identity becomes quantitatively decisive whenever its rare passages can be chosen from a small global list.

### Theorem 3.1 (same-parity link closure)

Let \(y\ge0\) be a physical matching-dual weight and let \(\mathcal Q=\operatorname{supp}y\). Suppose there are distinct same-rank-parity target pairs

\[
 (S_1,T_1),\ldots,(S_L,T_L)
\]

such that deleting

\[
 Z=\mathcal Q\cap\bigcup_{j=1}^L\mathcal L(S_j,T_j)
\tag{3.1}
\]

leaves a balanced literal physical incidence matrix. Then

\[
 y(\mathcal Q)
 \le \bigl(D+L\mu_{\rm even}\bigr)\nu_y.
\tag{3.2}
\]

Consequently, if \(L=o(m^{3/2})\), then

\[
 y(\mathcal Q)\le\bigl(D+o(D/\sqrt m)\bigr)\nu_y.
\tag{3.3}
\]

#### Proof

Every singleton strip is a matching, so

\[
 y_C\le\nu_y
\tag{3.4}
\]

for every \(C\). By (1.3),

\[
 y(Z)
 \le \sum_{j=1}^L\sum_{C\in\mathcal L(S_j,T_j)}y_C
 \le L\mu_{\rm even}\nu_y.
\tag{3.5}
\]

The restricted dual on \(\mathcal Q\setminus Z\) has matching norm at most \(\nu_y\). Balanced coefficient one gives

\[
 y(\mathcal Q\setminus Z)\le D\nu_y.
\tag{3.6}
\]

Adding (3.5) and (3.6) proves (3.2). Since \(\mu_{\rm even}=O(D/m^2)\), the hypothesis \(L=o(m^{3/2})\) makes the second term \(o(D/\sqrt m)\). \(\square\)

### Corollary 3.2 (necessary form of a Gaussian-scale counterexample)

If, along a subsequence,

\[
 y(\mathcal Q)\ge\left(D+c{D\over\sqrt m}\right)\nu_y
\tag{3.7}
\]

for some fixed \(c>0\), then every family of same-parity pair links whose deletion meets all strong odd Berge cycles of \(A_{\mathcal Q}\) has size

\[
 L\ge\left({c\over12}-o(1)\right)m^{3/2}.
\tag{3.8}
\]

Thus the residual object is not merely rank-diverging. It must distribute its parity-preserving passages over at least order \(m^{3/2}\) distinct physical pair links.

## 4. Why all target-capacity rows do not supply that transversal

The obstruction is a precise weighted scale mismatch.

Fix \(U,p\), abbreviate \(a_C=a_{U,p}(C)\) and \(b=b_{U,p}\), and normalize \(\nu_y=1\). For every threshold \(s\ge0\), the level set

\[
 \mathcal Q_s=\{C:y_C\ge s\}
\]

need not be a matching. Therefore the valid matching row (1.9) gives no direct bound on

\[
 \sum_{C\in\mathcal Q_s}a_C.
\]

The diagonal census (1.10), which is valid for the complete unweighted catalogue, yields only

\[
 \sum_Ca_Cy_C
 =\int_0^{\|y\|_\infty}\sum_{C\in\mathcal Q_s}a_C\,ds
 \le (1+6\delta)Db\|y\|_\infty
 \le (1+6\delta)Db.
\tag{4.1}
\]

The last inequality uses \(y_C\le\nu_y=1\). The factor \(b\) remains.

To replace the right side of (4.1) by order \(D\), one would have to split the \(b\) units of capacity into \(b\) coherent physical matching layers, or produce an equivalent matching-gain decomposition. That is exactly what the rank-diverging matching-interlocked core denies. Hence using (1.10) as if it were a weighted \(D\)-scale estimate is circular.

The same issue persists for every conic linear use of all \(U,p\) simultaneously. Those rows prove that the diagonal point

\[
 {\bf1\over(1+6\delta)D}
\]

lies in the outer polytope cut out by stars, cliques, and target capacities. They do not prove that it lies in the matching polytope. A separating functional outside the Farkas cone generated by those rows is precisely the permitted residual. Weighted star peeling localizes such a functional but does not place it in that cone.

This silence holds at exactly the required scale. For each fixed \(c>0\), since \(\delta=O(1/m)\), eventually

\[
 {1\over D+cD/\sqrt m}
 \le {1\over(1+6\delta)D}.
\tag{4.2}
\]

The outer system is down-monotone, so the Gaussian-scale diagonal on the left satisfies every one of its rows. Hence no nonnegative conic combination of target-star, clique, or target-capacity inequalities can separate that diagonal. Any successful use of capacity information must add a new physical implication between rows; the rows and their audited censuses alone cannot do it.

There is also no hidden small-star conclusion. Equation (1.6) costs \(\mathfrak l_m\) for each actual peeled target star. The capacity census does not bound the star-to-balanced or star-to-intersecting deletion number of an arbitrary weighted support. Thus it cannot force (1.7) for the residual core.

## 5. Exact audit of universal chronology identities after port selection

One might hope that the raw strip chronology supplies an extra linear conservation law capable of coupling the capacity rows. The selected-port construction blocks that route unless the selection rule is changed.

For each nonmiddle target \(T\), let \(\mathscr C(T)\) be its raw incident strips. An exact port choice is a vector

\[
 x^T\in\{0,1\}^{\mathscr C(T)},
 \qquad
 \sum_{C\in\mathscr C(T)}x^T_C=D.
\tag{5.1}
\]

Choices at distinct targets are independent. The convex hull of all exact choices is therefore

\[
 \mathcal P
 =\prod_T
 \left\{x^T\in[0,1]^{\mathscr C(T)}:
       \sum_Cx^T_C=D\right\},
\tag{5.2}
\]

a Cartesian product of hypersimplices.

### Lemma 5.1 (affine chronology erasure)

Suppose an affine functional

\[
 F(x)=\alpha+\sum_T\sum_{C\in\mathscr C(T)}a_{T,C}x^T_C
\tag{5.3}
\]

is constant on every exact port selection. Then, for each fixed target \(T\), the coefficient \(a_{T,C}\) is independent of \(C\). Consequently \(F\) is a linear combination of the exact target-degree equations (5.1), plus a constant.

#### Proof

Fix \(T\), an exact \(D\)-set of its raw incident strips, one selected strip \(C\), and one unselected strip \(C'\). Exchange \(C\) for \(C'\), leaving every other target choice fixed. Constancy of \(F\) gives

\[
 a_{T,C}=a_{T,C'}.
\]

The exchange graph of \(D\)-subsets is connected, so all coefficients in the \(T\)-block are equal. Repeat for every \(T\). \(\square\)

The same exchange proof holds over \(\mathbb F_2\): every universal affine parity identity is generated by the target row-sum parities.

### Consequence 5.2

There is no additional universal linear or mod-two conservation law, inherited merely from raw chronology, that couples different selected target rows. The previously exhibited zero-generator port hole is the concrete local manifestation: a raw chronological rectangle may survive while a target it would force under chronology-closed selection is omitted by independent targetwise thinning.

Lemma 5.1 does **not** erase the rank-parity passage theorem. The latter is a statement about every closed odd sequence of actual selected incidences, not an affine equation satisfied by the whole selected incidence matrix. It survives because target rank is intrinsic and the cycle returns to its initial target.

It does show that a stronger closure identity must come from one of two genuinely new ingredients:

1. a nonlinear theorem assigning the forced same-parity passages of all odd cycles to a small common link family; or
2. a correlated, chronology-closed port selector whose feasible selection polytope is a proper subpolytope of (5.2).

## 6. Final theorem-grade synthesis

### Theorem 6.1 (audited arbitrary-dual boundary)

Under the exact physical-port hypotheses and pair-kernel estimates above:

1. weighted star peeling closes every arbitrary dual with sufficiently small star-to-intersecting deletion number, as in (1.7);
2. all target-capacity rows certify the diagonal to additive \(O(D/m)\), but do not yield a weighted \(D\)-scale matching-gain inequality;
3. every strong odd Berge cycle contains an odd number of same-rank-parity passages, each supported on a pair link of size \(O(D/m^2)\);
4. a same-parity link transversal of size \(o(m^{3/2})\) closes the dual at \(D+o(D/\sqrt m)\);
5. independent exact targetwise port selection has no universal affine cross-target chronology identity beyond exact target degrees.

Therefore weighted star peeling plus all currently proved target-capacity rows do **not** rule out the residual matching-interlocked odd core. Any surviving Gaussian-scale obstruction must, however, be a rank-diverging rare-passage mesh with same-parity-link transversal number \(\Omega(m^{3/2})\). Closing constant one now reduces to proving that such a physical rare-passage mesh cannot occur, or to replacing independent port thinning by a correlated chronology-closed selector.

## 7. Dependency and non-claim ledger

This audit uses:

- MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md for the physical pair kernels;
- MATH_THEOREM_LOCALIZED_FLAG_BOUNDARY_ADAPTIVE_KERNEL_HIGH_COVER_EKR_20260726.md for the exact independent targetwise port construction;
- MATH_THEOREM_PHYSICAL_PORT_ARBITRARY_DUAL_STAR_PEELING_AND_ODD_CORE_REDUCTION_20260726.md for the matching dual and balanced coefficient-one reduction;
- MATH_THEOREM_FINE_STRIP_WEIGHTED_STAR_PEELING_AND_ODD_CAPACITY_CLOSURE_20260726.md for weighted star peeling and all target-capacity rows.

No generic bounded-rank matching theorem is invoked. The balanced-matrix integrality theorem remains the same explicitly imported result already isolated in the arbitrary-dual reduction.

The note does **not** construct the rare-passage mesh, and it does **not** prove it impossible. Its new positive content is the parity-passage identity and the \(o(m^{3/2})\) link-transversal closure. Its negative conclusion is exact for the present proof ingredients: the capacity census is diagonal, star peeling is weighted, and the missing common matching decomposition cannot be inferred from either without an additional physical coupling theorem.
