# REPLACEMENT TEXT

# Universal contiguous-subarray OR arrays: authoritative handoff

**Mathematical state:** 2026-08-22.

This file records the exact finite theorem and the shortest live route to

\[
\nu(k)=(1+o(1))W(k),\qquad
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

It is a proof document, not a research diary. Every assertion used in a live
implication is proved here, either at its point of use or in an appendix.
Status tags mean:

- **[I]**: proved unconditionally in this file;
- **[C]**: the stated conclusion is proved in this file from every displayed
  hypothesis;
- **[O]**: open; and
- **[W]**: the sole exception to literal self-containment: a finite word body
  is external, while its length, hash, encoding, verifier, verifier proof, and
  matching internal lower bound are included here.

No source file, checker, hash, conjecture, or archived branch is a premise of
an [I] or [C] assertion. Section 2.1 records the decisive breakthrough for
every closed \(k=0,\ldots,16\).
Appendix letters and skipped internal numbers are stable historical labels;
omitted branches are not used.

The exact status is:

- **[I]+[W]** \(\nu(k)=B(k)\) for \(0\le k\le16\).
- **[I]+[W]/[O]** \(24313=B(17)\le\nu(17)\le25746\); equality is open.
- **[O]** \(\nu(k)=(1+o(1))W(k)\) is not proved.

There are three logically separate compiler branches:

\[
\begin{array}{c|c|c}
\text{punctured branch}&\text{independent fragment branch}&\text{cycle branch}\\ \hline
A\to\text{two-rank}\to B\to C_{\rm P}&C_{\rm F}&\text{DCC}\\
\downarrow&\downarrow&\downarrow\\
\text{Appendix I.1}&\text{Appendix I.1}&\text{Section 3.3}\\
\downarrow&\downarrow&\downarrow\\
\multicolumn{3}{c}{\nu(n)=(1+o(1))W(n)\ \text{on the respective base subsequences}}\\
\multicolumn{3}{c}{\downarrow\ \text{bounded top-bit splices}\ \downarrow}\\
\multicolumn{3}{c}{\nu(k)=(1+o(1))W(k)\quad[\mathrm C].}
\end{array}
\]

Here Gates \(A,B,C_{\rm P},C_{\rm F}\) are [O]; the Appendix I.1 and
DCC compiler implications are [C]. A DCC construction itself is [O].

The full Baranyai--Katona wreath conjecture is not a premise of any branch.
The independent coherent-tour fragment route in Sections 4.4--4.5 and
Appendix I bypasses Gates A and B; its cross-pairing selection gate is also
open.

<!-- Retain current Sections 1--3 verbatim here. -->

## 4. Live coefficient-one architecture

For the punctured two-rank problem put

\[
b=2r+1,\qquad
\mathcal M=\binom{[b]}r,\qquad
\mathcal L=\binom{[b]}{r-1},\qquad
A=|\mathcal M|,\qquad A/b=\operatorname{Cat}_r.
\]

For the product compiler and coherent tours, \(b\) is odd,
\(|\Omega|=2b\), and \(W=\binom{2b}b\). Context determines which notation is
in force.

### 4.1 The punctured two-rank hypergraph [I]

For a permutation \(w=(w_0,\ldots,w_{b-1})\), with subscripts modulo \(b\),
write

\[
I_k^w(s)=\{w_s,\ldots,w_{s+k-1}\}
\]

and define

\[
E(w)=\{(\mathcal M,I_r^w(s)):s\ne0\}
\;\dot\cup\;
\{(\mathcal L,I_{r-1}^w(s)):s\ne0\}.
\]

It has \(4r\) vertices, \(2r\) on each shore. Its containment graph is a
canonically oriented alternating path, so \(w\mapsto E(w)\) is injective
and there are \(b!\) configurations. Every middle and lower target has
degree

\[
D_M=2r\,r!(r+1)!,\qquad D_L={r+2\over r}D_M.
\]

Weight \(1/D_L\) on every configuration is an optimal fractional matching:
it saturates the lower shore, loads each middle target by \(r/(r+2)\), and
has mass \(|\mathcal L|/(2r)\).

For fixed \(e\), let \(q(T)\) be the number of distinct cyclic boundary cuts
used by \(T\subseteq e\). The boundary graph is
\(\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\})\) with two edges deleted;
every subgraph with \(m\) edges and \(v\) nonisolated vertices has
\(m\le2(v-1)\). Consequently, for an absolute \(C\) and \(|T|\ge2\),

\[
{\deg(T)\over D_M}\le C^{|T|}r^{\,2-q(T)}.             \tag{4.1}
\]

The exact pair inventory also gives

\[
{1\over D_M}\sum_F\binom{|e\cap F|}{2}
=12+{32\over r}+{99\over2r^2}+O(r^{-3}).              \tag{4.2}
\]

Thus the local enumeration, fractional optimum, and all-order boundary
codegrees are closed. They do not constitute a matching theorem.

### 4.2 Product-law control and stopped descent [I]/[C]

Independently retain lower targets with density \(x\) and middle targets
with density

\[
y={rx+2\over r+2}.
\]

Put \(d_x=D_Mx^{2r}y^{2r-1}\). Conditional on a fixed configuration \(e\)
surviving, let

\[
\mathcal E_x(e)=
\mathbb E\!\left[\sum_{F\ {\rm surviving}}(|e\cap F|-1)_+
\,\middle|\,e\ {\rm survives}\right].
\]

Then

\[
{\mathcal E_x(e)\over r d_x}
=O\!\left({1\over rx^3}\right),                         \tag{4.3}
\]

uniformly for \(x\ge r^{-\alpha}\), every fixed \(\alpha<1/3\). For a fixed
retained target \(v\), the rooted estimate gives

\[
{\operatorname {Var}X_v\over(\mathbb EX_v)^2}
\le {1\over\mathbb EX_v}+O\!\left({1\over rx^3}\right). \tag{4.4}
\]

For each fixed integer \(s\ge1\) and \(\alpha<1/(6s)\),

\[
{\mathbb E(X_v-\mathbb EX_v)^{2s}\over(\mathbb EX_v)^{2s}}
=O_s((rx^3)^{-s}).                                      \tag{4.5}
\]

The moment estimates remain valid after conditioning on both exact shore
sizes, with exponentially small comparison error. They are annealed or
fixed-slice results, not estimates for the adaptive residual law.

For the actual isolated-edge process, after round \(j\) let \(H_j\) be the
residual hypergraph, \(Z_j=|E(H_j)|\), and \(M_j,L_j\) its shores. Put

\[
x_j={|L_j|\over|L_0|},\qquad
\bar d_j^M={2rZ_j\over|M_j|},\qquad
\bar d_j^L={2rZ_j\over|L_j|}.
\]

Fix \(K\ge1\), set \(\gamma=1/(96K)\), and take
\(0<\alpha\le1/(256K)\). In every good round, mark each residual
configuration with probability

\[
p_j={\gamma\over r\bar d_j^M}.                         \tag{4.6}
\]

Assume, until \(x_j\le r^{-\alpha}\), only

\[
\max_{v\in M_j}d_j(v)\le K\bar d_j^M,\qquad
\max_{v\in L_j}d_j(v)\le K\bar d_j^L.                  \tag{4.7}
\]

The internal covariance and drift proof gives

\[
\Pr\!\left(
\begin{array}{c}
\text{the cap persists to the threshold, but a bite estimate}\\
\text{or the resulting two-shore descent fails}
\end{array}\right)
\le e^{-\Omega(r)}.                                    \tag{4.8}
\]

On success, the accepted configurations form a matching leaving
\(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of the middle
shore. The cap also preserves an \(\exp(r\log r)\) average-degree floor
through the required \(O_K(r\log r)\) rounds. Equation (4.8) is a
stopped-event statement; it is not a conditional probability given the
future event that the cap persists.

### 4.3 The all-depth capacity boundary [I]/[C]

For a matching \(\mathcal P\) of punctured configurations, retain its starts
\((w,s)\) with \(s\ne0\), and for \(1\le q\le H\) define

\[
h_q^-(\mathcal P)=\binom b{r-q}
-\left|\{I_{r-q}^w(s):(w,s)\text{ is retained}\}\right|,
\]

\[
h_q^+(\mathcal P)=\binom b{r+1+q}
-\left|\{I_{r+1+q}^w(s):(w,s)\text{ is retained}\}\right|. \tag{4.9}
\]

If the unmatched lower-shore density is \(x\), then whenever
\(H\ge\lfloor\sqrt{rx}/4\rfloor\) and \(rx\ge64\),

\[
\sum_{q\le H}(h_q^-+h_q^+)
\ge {7\over32}|\mathcal L|\sqrt r\,x^{3/2}.            \tag{4.10}
\]

Therefore aggregate \(o(A)\) Gaussian-band holes require

\[
x=o(r^{-1/3}).                                         \tag{4.11}
\]

The stopped descent in Section 4.2 ends earlier, so Gate A alone cannot give
all-depth coverage. There are two exact continuations:

1. continue the same literal bank below (4.11) and prove distinct coverage
   at every depth \(q\le H\); or
2. prove a positive fractional cover of mass
   \(O(x\operatorname{Cat}_r)\); C.10 then rounds it to
   \(O(x\log r\,\operatorname{Cat}_r)\) compatible rows while leaving only
   \(o(A)\) holes.

For the second route, the logarithmic rounding overhead is harmless because
\(x\log r=o(1)\) in the live fixed-power range. The missing input is the
fractional cover itself, equivalently a capacity-sized hole-aligned
external-window degree tail. Uniform use of the complete survivor catalogue
does not supply it. Appendices H.11, H.15, and H.16 prove a local affine identity and
remote shore-difference and Venn-gap estimates. They do not convert those
estimates into one positive cover on the stopped residual at every depth;
that conversion remains open.

### 4.4 A direct literal fragment compiler [C]

Put \(|\Omega|=2b\), with odd \(b\), and
\(H=\lceil\sqrt{2b\log(2b)}\rceil\), \(g=b+H\). For all sufficiently large
\(b\), \(H\le b-2\). A physical fragment of core length \(L\) is a
singleton word with \(L\) consecutive designated starts such that, for
every \(s\in[b-H,b+H]\), all \(L\) length-\(s\) windows at those starts
exist and contain distinct letters.  Linearize the fragment by retaining
the core and its following \(g-1\) letters, at cost \(L+g-1\).

Take fragments whose middle cores are pairwise target-disjoint. Let \(M\)
be the total core size, \(t\) the number of fragments, and \(h_s\) the
number of rank-\(s\) targets absent from all designated windows. Then

\[
\boxed{
\nu(2b)\le M+(g-1)t
+\sum_{s=b-H}^{b+H}h_s
+\sum_{|s-b|>H}\binom{2b}s.}                           \tag{4.12}
\]

Every designated witness lies inside its own block, so overlaps outside
the disjoint middle cores cause no serialization conflict. Appending one
set-valued letter per absent target proves (4.12). The binomial tail in
(4.12) is \(o(W)\). Hence

\[
M=(1-o(1))W,\qquad (g-1)t=o(W),\qquad
\sum_{s=b-H}^{b+H}h_s=o(W)                              \tag{4.13}
\]

imply \(\nu(2b)=(1+o(1))W\).

An explicit sufficient schedule chooses any
\(a_b\to\infty\), \(a_b=o(\log b)\), constants \(0<c<2\), \(0<\theta<1\),
and

\[
L_b=\left\lfloor{cb\log b\over a_b}\right\rfloor.
\]

If \(O(a_b)\) residual-disjoint fragment matchings, each covering at least a
\(\theta\)-fraction of the current middle residual, leave at most
\(e^{-a_b}W\) middle targets and have aggregate off-middle band holes
\(o(W)\), then \(t\le W/L_b\) and

\[
(g-1)t=O\!\left({a_b\over\log b}W\right)=o(W),
\]

so (4.13) holds. This is a complete compiler theorem. The correlated
fragment matchings and their literal band coverage are open.

### 4.5 Coherent-tour banks [I]

Fix a perfect pairing \(\mathcal Q=\{P_0,\ldots,P_{b-1}\}\) of \(\Omega\)
and a directed cyclic order of its pairs. A coherent tour \(T(x)\), indexed
by \(x\in\mathbb F_2^b\), consists of \(b\) FIFO packets and has

\[
q=b(b-1)
\]

distinct internal middle targets. Each such target is defect one relative
to \(\mathcal Q\): one pair is empty, a different pair is doubled, and all
other pairs are split. The stratum has exactly

\[
q2^{b-2}                                                \tag{4.14}
\]

targets. Thus one pairing supports at most
\(2^{b-2}/(1-\varepsilon)\) rankwise-disjoint tours after retaining
\((1-\varepsilon)q\) targets from each. A near-factor consequently needs

\[
\Omega(2^b/b^{5/2})                                     \tag{4.15}
\]

different pairings. Conversely, for every \(a_b\to\infty\), a menu of

\[
(a_b+o(1)){4\over\sqrt\pi}{2^b\over b^{5/2}}            \tag{4.16}
\]

pairings misses at most \(e^{-a_b}W\) middle targets.

For one pairing and order, equality of targets from \(T(x)\) and \(T(x')\)
at ranks \(b-1,b,b+1\) depends only on \(x+x'\). The forbidden set
\(\mathcal B\subseteq\mathbb F_2^b\setminus\{0\}\) satisfies

\[
|\mathcal B|\le M_b:=2b^3+8b^2-16b.                    \tag{4.17}
\]

For every integer \(1\le H=o(b/\log b)\), there is, for all sufficiently
large \(b\), a full-rank map

\[
A:\mathbb F_2^b\longrightarrow\mathbb F_2^d,\qquad
d=\lceil\log_2(4M_b)\rceil,
\]

such that, for \(C=\ker A\),

\[
C\cap\mathcal B=\varnothing,\qquad d(C^\perp)>H.        \tag{4.18}
\]

Every coset of \(C\) is therefore a jointly three-rank-disjoint bank of
\(2^{b-d}=2^b/\operatorname{poly}(b)\) tours. The cosets exactly fourfold
resolve the fixed-pairing middle stratum. Dual distance makes each coset
exactly \(H\)-wise uniform in the state bits, so within a fixed pairing and
order all cosets have identical target-incidence profiles of order at most
\(H\). In particular every ground coordinate belongs to exactly half of the
middle targets in every bank, independently of the pairing; any
target-disjoint union of whole banks preserves this half-star balance.

This is local, not Gate C. Banks from different pairings can collide;
higher-order profiles can depend on the pairing; the selected tours have not
been placed with \(q-o(q)\) flags in one common extendable symmetric-chain
factor; and ranks outside \(b-1,b,b+1\) remain uncontrolled.

## 5. Exact remaining gates

### Gate A [O]: quenched cap preservation

For one fixed \(K>1\), and \(0<\alpha\le1/(256K)\), run the actual
isolated-edge process of Section 4.2 and stop at the first round when either
\(x_j\le r^{-\alpha}\) or one inequality in (4.7) fails. Prove

\[
\Pr(\text{the degree cap fails before the density threshold})=o(1). \tag{5.1}
\]

Together with (4.8), this yields the punctured two-rank near-factor. The
boundary codegrees, annealed and exact-slice moments, bite concentration,
empirical degree floor, and stopped descent are already proved. A maximum
degree cap does not generically propagate itself; the proof must exploit the
punctured interval geometry. The shortest current product-law target is the
tail-relative signed connected-carrier hierarchy under the appropriate Palm
law: its first unresolved member is the connected two-star, and the signed
higher-star remainder must be controlled with it. Stopped slice, center,
erosion, and purge transfer are then still required.

### Gate B [O]: critical all-depth cover-down

On the same literal bank produced after Gate A, prove one of:

- continuation to \(x=o(r^{-1/3})\) together with
  \(\sum_{q\le H}(h_q^-+h_q^+)=o(A)\); or
- a compatible positive fractional cover of the holes of mass
  \(O(x\operatorname{Cat}_r)\), followed by the proved rounding theorem,
  which uses \(O(x\log r\,\operatorname{Cat}_r)\) physical rows.

The rows must cover all depths \(q\le H=\lceil\sqrt{b\log b}\rceil\) in one
common occurrence state. Raw capacity, conservation, complete-catalogue
averaging, or a two-rank matching does not prove this gate. The
zero-avoidance lemmas in Appendix H are only partial estimates: the missing
output is still a compatible positive cover, on this stopped bank, at all
displayed depths simultaneously.

### Gate C [O]: either product lift or independent fragment selection

There are two distinct interfaces; they must not be conflated.

- **Gate \(C_{\rm P}\).** From the same literal \(b\)-coordinate row bank
  produced by Gate B, construct on
  \(\Omega=[b]\mathbin{\dot\cup}[b]'\) a family of physical fragments
  satisfying the three conditions in (4.13), equivalently (I.41).
  This includes the presently missing product lift, all-offset coverage,
  and serialization.
- **Gate \(C_{\rm F}\).** Independently select repaired coherent-tour
  fragments from the balanced coset banks of Section 4.5 so that (I.41)
  holds.  This requires cross-pairing target-disjoint selection and
  all-band literal repair, but does not use Gates A or B.

Either output is already a literal compiler antecedent; no common
symmetric-chain factor or odd DCC is silently assumed.

### Gate D [O]: finite \(k=17\)

Independently close \(24313\le\nu(17)\le25746\). Witnesses constructed in
different occurrence states cannot be composed without a literal common
replay.

## 6. Completion implications

If Gates A, B, and \(C_{\rm P}\) are proved with their common-object
requirements, the resulting literal fragment family satisfies (4.13),
equivalently Appendix I.1's finite compiler hypothesis. That
compiler gives

\[
\nu(k)=(1+o(1))W(k).
\]

This would be a genuine construction: deterministic if the gates are
constructive, or a probabilistic existence construction with a finite
positive-probability sample space otherwise. It would not imply the literal
equality \(\nu(k)=W(k)\); the proved lower bound is
\(B(k)=W(k)+\Theta(\sqrt k)\).

Independently, \(C_{\rm F}\) gives the same fragment hypothesis and hence
the same conclusion without Gates A or B. If an odd singleton cycle is
instead constructed, the DCC criterion of Section 3.3 is a third,
logically separate compiler. In either fragment route the base dimensions
are \(2b\) with odd \(b\); the top-bit splice, used at most three times,
covers every sufficiently large dimension with asymptotic ratio one.

## 7. Scope walls

1. The Baranyai--Katona wreath conjecture is not required by either
   fragment branch.
2. A two-rank matching controls only the vertices in its hypergraph; it says
   nothing by itself about deeper windows.
3. Annealed or exact-slice estimates do not imply their adaptive quenched
   analogues.
4. Exact regularity, small pair codegree, and bounded local statistics do
   not generically force a near-matching; Appendix C.6 gives a counterexample.
5. Nominal product degrees are not tangent-invariant under an isolated-edge
   bite. The stopped descent correctly uses empirical shore averages.
6. Separately constructed factors, retirement assignments, banks, and
   compilers cannot be composed unless they use one common literal
   occurrence state.
7. A fixed-pairing coset resolution is not a cross-pairing near-factor.
   Low-order balance does not control every residual obstruction.
8. Overlap between fragment domains is harmless only because each fragment
   is linearized in its own block. Middle-core disjointness, \(W+o(W)\)
   total mass, \(o(W)\) holes, and \(o(W)\) seams remain mandatory.

## 8. Completion ledger and audit contract

| item | status | exact boundary |
|---|---|---|
| rank-witness lower bound and central maximizer | [I] | closed |
| exact values \(0\le k\le16\) | [I]+[W] | only literal word bodies are external |
| \(k=17\) | [I]+[W]/[O] | \(24313\le\nu(17)\le25746\) |
| DCC implies coefficient one | [C] | closed |
| punctured local profile and fractional optimum | [I] | closed |
| all-order boundary codegrees and boundary polymers | [I] | closed |
| fixed-target product/exact-slice moments | [I] | closed in the stated ranges |
| cap-preserving stopped descent | [C] | succeeds unless the cap fails first |
| Gate A | [O] | quenched cap preservation |
| all-depth capacity bound and fractional-cover rounding | [I]/[C] | positive hole-aligned cover is open |
| zero-avoidance local affine gap, remote shore-difference bound, and Venn-gap localization | [I] | closed partial Gate-B lemmas |
| conversion of zero-avoidance estimates into one all-depth positive cover | [O] | no such stopped-bank cover is proved |
| Gate B | [O] | critical cover-down on one literal bank |
| physical-fragment literal compiler | [C] | fragment selection and band holes are open |
| pairing menus and balanced three-rank coset banks | [I] | local; cross-pairing selection is open |
| Gate \(C_{\rm P}\) | [O] | product lift from the Gate-B bank to (I.41) |
| Gate \(C_{\rm F}\) | [O] | cross-pairing selection and all-band repair to (I.41) |
| coefficient-one theorem | [O] | no assembled construction |

Every refresh must:

1. retain a complete proof for every [I] and [C] assertion;
2. retain the full \(k=0,\ldots,16\) breakthrough table;
3. recompute every [W] hash and run the included finite-word verifier;
4. keep the word bodies as the only exception to literal self-containment;
5. repeat every hypothesis when invoking a conditional theorem;
6. preserve the stopped-event form (4.8), not conditioning on future cap
   persistence;
7. distinguish two-rank, all-depth, and serialization conclusions; and
8. never mark coefficient one proved until one literal construction passes
   the analytic interval-union verification.

The finite theorem through \(k=16\) is closed. The coefficient-one
asymptotic remains open at punctured Gates A, B, and \(C_{\rm P}\), at
independent Gate \(C_{\rm F}\), and at the separate DCC construction.

---

# INTEGRATION MAP (not part of the mathematical document)

Line numbers refer to the 733,153-byte pre-minification
MASTER_HANDOFF.md with SHA-256
\(33bd71151ad52a52866b917b90abcd795fcfdee9b195824c77237f468bd20c43\);
its Appendix A starts at line 2370.

| old lines | old content | action |
|---:|---|---|
| 1--341 | title and expanded status recital | replace with this draft's front matter through the placeholder |
| 342--797 | Sections 1--3 | retain verbatim |
| 524--577 | Section 2.1, including both value tables, the complete \(k=0,\ldots,16\) breakthrough table, and \(k=17\) | specifically protect; it lies inside retained lines 342--797 |
| 798--840 | Section 4 notation and large ledger | replace by new Section 4 introduction |
| 841--1050 | old Sections 4.1--4.2 | delete from the live route |
| 1051--1376 | old Sections 4.3--4.7 | replace by new Sections 4.1--4.3 |
| 1377--1412 | old Section 4.8 Dyck alternative | delete from the live core; archive only |
| 1413--1647 | old Gate A | replace by new Gate A and compact Section 4.2 |
| 1648--1771 | old Gate B | replace by new Gate B and compact Section 4.3 |
| 1772--2029 | old Gate C | replace by new Gate C and Sections 4.4--4.5 |
| 2030--2036 | old Gate D | replace by new Gate D without changing status |
| 2037--2047 | old alternative gate | delete from the live core; archive only |
| 2048--2129 | old Section 6 scope warnings | replace by new Section 7 |
| 2130--2248 | old proof/provenance map | delete entirely |
| 2249--2369 | old completion audit | replace by new compact Section 8 |
| 2370 onward | Appendices A onward | outside this assignment |

After integration, remove the placeholder and this entire integration map.
