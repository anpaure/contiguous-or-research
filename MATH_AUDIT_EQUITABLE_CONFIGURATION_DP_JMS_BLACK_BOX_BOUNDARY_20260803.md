# Independent self-audit: DP/JMS boundary for the equitable configuration host

**Date:** 2026-08-03  
**Audited theorem:**
MATH_THEOREM_EQUITABLE_CONFIGURATION_DP_JMS_BLACK_BOX_BOUNDARY_20260803.md

**Verdict:** PASS, with the explicit scope that this is a direct-black-box
no-go for the canonical labelled host. It is not an impossibility theorem
for its perfect matching, a sparsified host, or a collar absorber.

## 1. Primary-source hypothesis check

### Delcourt--Postle

Corollary 1.17 of arXiv:2204.08981v3 has the quantifier order

\[
 \text{fix }R,g,\beta>0;\quad
 \exists D_\beta,\alpha>0;\quad
 \forall D\ge D_\beta.
\]

Its host is an \(R\)-bounded multihypergraph with

\[
 \Delta(G)\le D,\qquad \Delta_2(G)\le D^{1-\beta},
\]

and the empty-conflict specialization gives a matching of size at least

\[
 {e(G)\over D}(1-D^{-\alpha}).
\]

The theorem file correctly treats \(R,\beta\) as fixed and does not infer
uniform dependence of \(D_\beta\) or \(\alpha\).

### Joos--Mubayi--Smith

Theorem 1.1/3.1 of arXiv:2407.18144v2 fixes the integer edge types and
conflict bound before choosing a sufficiently small fixed
\(\varepsilon>0\). The three rows used in the no-go are exactly

\[
 d_J^\varepsilon\le |P|\le|P\cup Q|
 \le\exp(d_J^{\varepsilon^3}),
\]

\[
 (1-d_J^{-\varepsilon})d_J
 \le\delta_P(H_1)\le\Delta(H_1)\le d_J,
\]

and

\[
 \Delta_2(H_1)\le d_J^{1-\varepsilon}.
\]

No conflict or cleanup hypothesis is used before the contradiction.

## 2. Independent recomputation of the host ledger

Let \(D_*=Wr!\). A fixed pattern has \(W\) owner choices and \(r!\)
labelled orders, so \(d(p_i)=D_*\). A fixed owner has \(W\) patterns and
\(r!\) orders, so \(d(o_T)=D_*\). Every edge has exactly one pattern, so

\[
 e(\mathcal K_r)=W D_*.
\]

For a target \(S\) of rank \(s\), multiplication of its canonical
fractional degree by \(D_*\) gives

\[
 d(S)=D_*{N_s\over\binom{2r}{s}}\le D_*.
\]

Thus \(\Delta=D_*\), with no hidden target overdegree.

For \(S\subset T\), the owner--target codegree is

\[
 D_*{N_s\over W\binom rs}.
\]

At \(s=r-1\),

\[
 N_{r-1}=\binom{2r}{r-1}-b_{r-1}
 =W{r\over r+1}-O(r),
\]

because the complete triangular boundary has \(O(d^2)=O(r)\) cells. The
codegree is therefore

\[
 {D_*\over r+1}-O(D_*/W)
 =(1-o(1)){D_*\over r+1}.
\]

This verifies the decisive lower bound without relying on rank one or a
particular pattern decomposition.

Finally,

\[
 \log D_*=\log W+\log r!=\Theta(r\log r),
 \qquad \log W=\Theta(r).
\]

The optimal total scheduled mass is \(\Theta(dW)\),
\(d=\Theta(\sqrt r)\), and the pattern decomposition is equitable. Hence
the maximum edge size is \(\Theta(\sqrt r)\).

## 3. Independent JMS contradiction

Assume (S2), (H1), and (H2).

1. From (S2), \(W\le\exp(d_J^{\varepsilon^3})\). In particular
   \(d_J^{-\varepsilon}<1/2\) for large \(r\).
2. Then (H1) gives \(D_*\le d_J\le2D_*\).
3. The codegree lower bound and (H2) give
   \(D_*/(2r)\le d_J^{1-\varepsilon}\). Dividing by \(D_*\) and using
   \(d_J/D_*\le2\) yields \(d_J^{-\varepsilon}\ge1/(4r)\), hence
   \(\varepsilon\log d_J\le\log(4r)\).
4. Therefore
   \[
   \varepsilon^3\log d_J
   \le {\log^3(4r)\over(\log d_J)^2}=o(1).
   \]
5. Taking logarithms twice in (S2) requires
   \(\log\log W\le\varepsilon^3\log d_J\), but the left side is
   \(\log r+O(1)\).

The contradiction is exact. It permits \(\varepsilon\) to depend on
\(r\); it is stronger than merely citing the fixed-parameter quantifiers.

## 4. Independent DP scale check

Let \(D\ge D_*\) be the DP nominal degree. Its displayed guarantee is

\[
 W{D_*\over D}(1-D^{-\alpha}).
\]

For this guarantee to be \((1-o(1))W\), necessarily
\(D/D_*=1+o(1)\). Then

\[
 {D_*\over2r}\le D^{1-\beta}
 \quad\Longrightarrow\quad
 D^\beta=O(r),
\]

so \(\beta=O(\log r/\log D)=O(1/r)\). This is incompatible with one fixed
\(\beta>0\) along the family.

For fixed \(\beta\), the smallest nominal scale allowed by the codegree
row is

\[
 D\ge(D_*/(2r))^{1/(1-\beta)}.
\]

Consequently the theorem's normalized numerical guarantee is at most

\[
 {D_*\over D}
 \le(2r/D_*^\beta)^{1/(1-\beta)}=o(1).
\]

The theorem file describes the *guaranteed lower bound* as becoming
useless; it does not claim that all matchings are small.

## 5. Adversarial scope checks

### 5.1 Could lower target degrees violate regularity first?

No, and the theorem does not claim so. DP needs only maximum degree for the
coloring conclusion. JMS needs the pointwise lower bound only on the
chosen \(P\)-shore; choosing patterns gives degree exactly \(D_*\).
Lower \(Q\)-degrees are permitted.

### 5.2 Could a larger nominal degree repair either application?

For JMS, (H1) forces \(d_J\le2D_*\) once (S2) is nontrivial. For DP, a
larger \(D\) can repair the formal power-codegree row but reduces the
published guarantee by \(D_*/D\); the fixed-\(\beta\) repaired scale gives
only \(o(W)\).

### 5.3 Do variable configuration sizes invalidate the ledger?

No. DP permits bounded, nonuniform edges. JMS has a fixed edge type, but
the two equitable sizes can be equalized with edge-private dummy
\(Q\)-vertices. This does not alter the decisive old degrees, codegrees,
or ambient size. JMS additionally fixes this padded size before its
asymptotic, while that size grows as \(\Theta(\sqrt r)\).

### 5.4 Does labelled multiplicity create an artificial obstruction?

The audited host is explicitly the canonical **labelled** configuration
multihypergraph. DP explicitly permits multihypergraphs. A simple JMS
encoding can add a private label vertex to every edge; this leaves every
old critical pair unchanged. Collapsing or sparsifying orders more
aggressively changes the host and lies outside the direct audit.

### 5.5 Does the result reject all sparsifications?

No. A polynomial-degree sparsification could turn a polynomial relative
codegree into a fixed power of its new degree. One would first have to
prove simultaneous degree and all-codegree concentration across the
exponential Boolean vertex set. More importantly, DP still fixes its edge
bound while the configuration size grows, and exact collar completion
remains absent. The theorem correctly lists this as a possible new route.

### 5.6 Does the residual \(O(r^{-2})\) ledger become useless?

No. It proves the natural collision parameter
\(K^2\rho_2=O(r^{-1})\), favorable for a tailored growing-uniformity
nibble. It fails only to instantiate a theorem phrased with a fixed power
of the much larger labelled degree.

### 5.7 Could DP or JMS give an exact size-\(W\) result after all?

DP's cited corollary is an almost-matching/coloring theorem and has no
absorber. JMS is \(P\)-perfect if all of its rows hold, but those rows are
already contradictory for the natural host; a private completion must
also be decoded with all physical collisions restored. The audit makes no
claim against a different exact theorem.

## 6. Final boundary

Certified:

    full canonical labelled host:
      max degree D*=Wr!,
      pair codegree Omega(D*/r),
      edge size Theta(sqrt r);

    JMS:
      S2 + H1 + H2 are numerically incompatible;

    DP:
      no fixed-parameter direct application gives (1-o(1))W,
      and nominal-degree inflation makes its displayed guarantee o(W).

Deliberately not claimed:

    the canonical host has no perfect matching;
    all sparsifications fail;
    all collar-first factorizations fail;
    no Boolean-specific growing-uniformity theorem can work.

Within that scope, the theorem is proof-safe.
