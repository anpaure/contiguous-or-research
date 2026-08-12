# Independent rank matchings: exact profile Hall, raw-cut boundary, and packet grouping

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 [2m]=R\mathbin{\dot\cup}\bigdotcup_{j=1}^b(A_j\dot\cup C_j),
 \qquad |A_j|=|C_j|=d,
 \qquad b=\lfloor m/d\rfloor,
\tag{0.1}
\]

put (M=bd), (delta=m-M<d), and choose an arbitrary bijection

\[
                  \pi_{j,k}:A_j\longrightarrow C_j
                  \qquad(0\le k\le2d).
\tag{0.2}
\]

The choices in (0.2) may be independent and random, but the positive
theorem below is deterministic: it holds for every realized array.

Fix (A>0) and

\[
 q=A\sqrt m+O(1),qquad d\to\infty,qquad
 d^2=o(\sqrt m),qquad {m\over d}e^{-c_0d}=o(1)
\tag{0.3}
\]

for a sufficiently small absolute (c_0>0). Consider the maximal lower
or upper compatibility graph before an (r)-set of axes is retained and
before a packet chronology is chosen.

The following statements are proved.

1. For prescribed ordered half-count profiles and prescribed block
   allocations, the total compatible incidence is independent of every
   bijection (0.2). Exact formulae are given in Lemma 2.1.
2. After deleting the (o(N_q)) targets having a noncentral half-count,
   every weighted Hall inequality whose potential is constant on each
   **ordered** residual/half-count profile has Gaussian expansion

   \[
      \sum_X\max_{T\sim X}y(T)
      \ge (e^{A^2}-o(1))\sum_Ty(T).
   \tag{0.4}
   \]

   Thus independent rank matchings are not needed to remove the
   fixed-allocation deficit at this exact profile-compressed level.
3. Equation (0.4) is not the arbitrary-subset Hall theorem. A target
   family may select a proper subset of one ordered profile, and the proof
   gives no expansion for that family. Independent random matchings make
   such expansion plausible, but a quenched cut theorem is still missing.
4. Even a raw injection in the maximal graph would not choose retained
   packet axes, consecutive compiler windows, a common lower/upper owner,
   or one chronology through all depths. Those are strictly later gates.

Hence this note gives a genuine normalized Hall theorem, but it does not
prove the Gaussian packet theorem or coefficient one.

## 1. The residual fibres and the two ordinary ratios

Every compatible trace preserves its residual subset. Fix (Z\subseteq R),
write (z=|Z|), and put

\[
                         \eta=\delta-z,qquad |\eta|\le\delta.
\tag{1.1}
\]

In the lower graph, the core target and source ranks are respectively

\[
                         M+\eta-q,qquad M+\eta.
\tag{1.2}
\]

Thus an ordinary core target has

\[
 D_T^-(\eta)=\binom{M-\eta+q}{q}
\tag{1.3}
\]

middle supersets, while a middle source contains

\[
 D_X^-(\eta)=\binom{M+\eta}{q}
\tag{1.4}
\]

such lower subsets. In the upper graph the corresponding degrees are

\[
 D_T^+(\eta)=\binom{M+\eta+q}{q},
 \qquad
 D_X^+(\eta)=\binom{M-\eta}{q}.
\tag{1.5}
\]

Put \(\rho_q^\epsilon(\eta)=D_X^\epsilon(\eta)/D_T^\epsilon(\eta)\).
Uniformly for (|\eta|<d), Stirling's product estimate and (0.3) give

\[
             \rho_q^-(\eta)=e^{-A^2+o(1)},\qquad
             \rho_q^+(\eta)=e^{-A^2+o(1)}.
\tag{1.6}
\]

More directly, the logarithm is the central-binomial displacement

\[
 -{q^2\mp2\eta q\over M}
       +O\!\left({q^3+d^2q\over M^2}\right)
 =-A^2+o(1).
\tag{1.7}
\]

This retains the residual floor exactly. No divisibility assumption
(d\mid m) is required.

## 2. Deterministic local incidence identities

Fix one block and one of its matchings. For a lower target let

\[
 |T\cap A|=a,qquad |T\cap C|=c,
\tag{2.1}
\]

and let the source add (alpha) (A)-coordinates and (gamma)
(C)-coordinates, where (ell=alpha+gamma). Compatibility means that
the selected matching edges are empty in (T).

### Lemma 2.1 (exact lower and upper profile incidences)

For every fixed bijection (pi:A\to C), the number of compatible lower
pairs with the data above is

\[
 \boxed{
 I_d^-(a,c;\alpha,\gamma)
 =\binom d{\alpha,\gamma,d-\ell}
   \binom{d-\ell}{a}\binom{d-\ell}{c}.}
\tag{2.2}
\]

For an upper target with half-counts (u,v), from which the source
removes (alpha) (A)-coordinates and (gamma) (C)-coordinates,
the exact count is

\[
 \boxed{
 I_d^+(u,v;\alpha,\gamma)
 =\binom d{\alpha,\gamma,d-\ell}
   \binom{d-\ell}{u-\ell}
   \binom{d-\ell}{v-\ell}.}
\tag{2.3}
\]

Both counts are independent of the identity of (pi).

#### Proof

For (2.2), choose (ell) matching edges and designate (alpha) of them
to receive their (A)-endpoint and (gamma) to receive their
(C)-endpoint. The target avoids both endpoints of those edges. On the
remaining (d-ell) edges, choose its (a) (A)-endpoints and its (c)
(C)-endpoints independently.

For (2.3), designate (alpha) edges on which the source contains only
the (C)-endpoint and the upper target adds the (A)-endpoint, and
designate (gamma) edges with the shores reversed. On the remaining
edges the source has (u-ell) (A)-endpoints and (v-ell)
(C)-endpoints. These constructions are bijective. \(\square\)

The corresponding ordinary inclusion counts are

\[
 J_d^-=\binom da\binom dc
          \binom{d-a}{\alpha}\binom{d-c}{\gamma},
\tag{2.4}
\]

\[
 J_d^+=\binom du\binom dv
          \binom u\alpha\binom v\gamma.
\tag{2.5}
\]

Tensoring (2.2)--(2.5) over the labelled blocks gives the exact global
profile incidences. In particular, randomizing (0.2) changes which raw
pairs realize an incidence but not a single aggregate profile total.

## 3. Safe profiles and the two-promotion truncation

Call an ordered target profile safe when

\[
                  {d\over4}\le |T\cap A_j|,|T\cap C_j|
                              \le {3d\over4}
                  \qquad(j\le b).
\tag{3.1}
\]

The same definition is used above. A hypergeometric Chernoff bound,
followed by a union bound over (2b) halves, shows from (0.3) that unsafe
profiles contain (o(N_q)) targets, uniformly over the residual fibres.

Choose an ordinary lower middle superset of a fixed target uniformly. If
(ell_j) additions land in block (j), then

\[
 \Pr\{\max_j\ell_j\ge3\}
 \le b\binom{2d}{3}{(q)_{\underline3}
       \over(M-\eta+q)_{\underline3}}
 =O_A\!\left({d^2\over\sqrt m}\right)=:\varepsilon_m.
\tag{3.2}
\]

The same estimate, with denominator (M+\eta+q), holds for the (q)
deletions from an upper target. It is uniform in the target.

If the target profile is safe and every (ell_j\le2), both expressions
in Lemma 2.1 are positive. Thus every retained ordinary profile arc is an
actual compatible profile arc for every matching array.

## 4. The normalized profile quotient flow

Fix a sign and a residual fibre. Let (w_T(\tau)) and (w_X(\kappa))
be the numbers of raw vertices in the ordered target and owner half-count
profiles. Let (J_{\tau\kappa}) be the ordinary inclusion count, and
retain only safe target profiles and allocations satisfying
(ell_j\le2).

For a safe target profile define

\[
 r_\tau={1\over w_T(\tau)D_T}
           \sum_\kappa J_{\tau\kappa}.
\tag{4.1}
\]

Equation (3.2) gives (r_\tau\ge1-\varepsilon_m). Put

\[
                  F_{\tau\kappa}
                  ={J_{\tau\kappa}\over D_T r_\tau}.
\tag{4.2}
\]

Then

\[
 \sum_\kappa F_{\tau\kappa}=w_T(\tau),
 \qquad
 \sum_\tau F_{\tau\kappa}
 \le{\rho_q^\epsilon(\eta)\over1-\varepsilon_m}
                      w_X(\kappa).
\tag{4.3}
\]

This is an exact capacity flow in the profile quotient. It alone is not
yet the raw profile-compressed Hall dual, because an aggregate arc need
not be visible from every owner in its endpoint profile. The next lemma
supplies the missing support estimate.

## 5. Almost every owner realizes every retained profile arc

### Lemma 5.1 (uniform arc visibility)

There is an absolute (c>0) such that, for every retained lower or upper
profile arc \((\tau\to\kappa)\), at least

\[
                         1-\zeta_m,
 \qquad \zeta_m:=q e^{-cd}=o(1),
\tag{5.1}
\]

of the raw owners in \(\kappa\) have a compatible neighbor in \(\tau\).
The estimate is uniform in the matching array and in the retained arc.

#### Proof

Consider first a lower local arc. The source half-counts are
(a'=a+alpha,c'=c+gamma). For a uniformly chosen source with these
counts, let

\[
 F=|X_A\cap\pi^{-1}(X_C)|.
\tag{5.2}
\]

Then (F\) is hypergeometric. The numbers of singleton matching edges
occupied on the (A)- and (C)-shores are (a'-F) and (c'-F).
Deleting the prescribed (alpha,gamma) coordinates is possible exactly
when

\[
                         a'-F\ge\alpha,qquad
                         c'-F\ge\gamma,
\tag{5.3}
\]

or (F\le\min(a,c)). If (5.3) fails and
(alpha+gamma\le2), then (F) lies within two of its largest possible
value. Since (a,c\in[d/4,3d/4]), the hypergeometric product formula gives

\[
                         \Pr\{\text{failure in this block}\}
                              \le e^{-cd}
\tag{5.4}
\]

after decreasing (c) absolutely. Explicitly, when (a\le c), failure
requires all but at most one of the (a+\alpha) selected (A)-points to
map into a set of at most (3d/4+2) selected (C)-points; summing those
two terminal hypergeometric terms is at most
\(\operatorname{poly}(d)(4/5)^{d/4}\). The case \(c<a\) is symmetric.

For an upper local arc, let the target half-counts be \((u,v)\), so the
source half-counts are \(a'=u-\alpha\) and \(c'=v-\gamma\). Adding an
\(A\)-point uses a \(C\)-shore singleton of the source and adding a
\(C\)-point uses an \(A\)-shore singleton. Thus visibility is equivalent
to

\[
                    c'-F\ge\alpha,\qquad a'-F\ge\gamma.       \tag{5.5}
\]

Failure means \(F>v-\ell\) or \(F>u-\ell\). Since
\(\ell=\alpha+\gamma\le2\), this again puts \(F\) within two of
\(\min(a',c')\), its maximum possible value. The source half-counts lie
in \([d/4-2,3d/4]\), so the same terminal hypergeometric estimate proves
(5.4).

Uniform owners in a fixed ordered global profile factor over blocks. A
retained allocation touches at most (q) blocks. The union bound proves
(5.1). \(\square\)

## 6. The actual profile-compressed weighted Hall theorem

### Theorem 6.1 (deterministic ordered-profile Hall expansion)

Let (y(T)\ge0) be constant on each safe ordered profile, including its
residual subset, but otherwise arbitrary. For every owner profile
(kappa), choose, among the arcs with \(F_{\tau\kappa}>0\), a retained
adjacent target profile \(\tau_\kappa\)
maximizing that profile value. Lemma 5.1 gives

\[
 \sum_{X\in\kappa}\max_{T\sim X}y(T)
 \ge(1-\zeta_m)w_X(\kappa)y(\tau_\kappa).
\tag{6.1}
\]

On the other hand, expanding the quotient flow and then taking this one
maximum gives

\[
 \sum_Ty(T)
 =\sum_{\tau,\kappa}F_{\tau\kappa}y(\tau)
 \le\sum_\kappa y(\tau_\kappa)\sum_\tau F_{\tau\kappa}
 \le {\rho_q^\epsilon(\eta)\over1-\varepsilon_m}
       \sum_\kappa w_X(\kappa)y(\tau_\kappa).
\tag{6.2}
\]

Combining (6.1)--(6.2), and then summing the residual fibres, yields

\[
 \boxed{
 \sum_Ty(T)
 \le {e^{-A^2}+o(1)\over
              (1-\varepsilon_m)(1-\zeta_m)}
       \sum_X\max_{T\sim X}y(T).}
\tag{6.3}
\]

The coefficient in (6.3) is strictly below one for every fixed (A>0)
and all sufficiently large (m). This proves (0.4), separately for both
signs.

The distinction from the quotient-only statement is material. Aggregate
incidence counts prove (4.3); Lemma 5.1 is what allows the profile maximum
to be evaluated on actual raw owners.

## 7. The exact raw gate

The proof of (6.3) uses that (y) is constant within an ordered
half-count profile. It gives no inequality for a weight supported on an
arbitrary subset of one such profile. Independent random matchings are
reused by exponentially many vertices, so concentration of the
(e^{o(m)}) profile totals is not a union bound over all raw cuts.

A sufficient missing theorem is the following quenched expansion property.
After deleting (o(N_q)) targets and (o(W)) owners, with probability
(1-o(1)) over the independent array (0.2),

\[
 |N(\mathcal A)|\ge(1+\delta_A)|\mathcal A|
 \quad\hbox{for every raw target family }\mathcal A,
\tag{7.1}
\]

for some fixed (delta_A>0). Max-flow/min-cut and bipartite integrality
would then give a raw injection. A cut-norm theorem for the product random
permutation kernels, or a compression theorem forcing a minimum cut to be
profile-measurable, would suffice. Neither is proved here.

The Gaussian kernel assertion in
`MATH_THEOREM_RANDOM_RANK_MATCHING_ALLOCATION_HALL_PROFILE_20260726.md`
does not fill this gap. Its uniform coefficient census is sketched rather
than proved, and its displayed routing by
(phi(y)e^{-Ay}) gives owner load depending on (y), not uniform owner
load. The deterministic argument above replaces the valid coarse
conclusion and does not use that routing.

## 8. Literal factors and selector grouping are later gates

For a retained product cell (Q_S), averaging over all admissible active
(n)-sets and all affine conjugates of the valid trace-injective compiler
selects each physical signed (q)-face with exact probability

\[
                         {2^q\over\binom Sq}.
\tag{8.1}
\]

Indeed the active set contains the face support with probability
(\binom nq/\binom Sq), and a conjugated factor selects that face with
probability (2^q/\binom nq). This is an exact fractional whole-cell
twirl. In its target formula one must include the indicator that the
source cell is retained, (S\ge n). Its total mass equals the retained
owner mass (G), so its Gaussian mean is (G/N_q=e^{A^2+o(1)}).

This twirl is not a choice of one option per cell. Nor can all its labels
be installed for free through selector fibres. If (t) fixed selector
axes are frozen in (Q_S), every trace support avoids them, and the exact
accessible fraction of (q)-supports is

\[
                         {\binom{S-t}q\over\binom Sq}
                         \le e^{-tq/S}.
\tag{8.2}
\]

A literal target decodes one selector row, so an orthogonal array over
the other rows does not average (8.2) targetwise. Cross-cell cylinder
cover and one common lower/upper, all-depth compiler label remain
necessary.

The implication chain is therefore only

\[
 \boxed{
 \text{grouped packet chronology}
 \Longrightarrow \text{selected-axis raw injection}
 \Longrightarrow \text{maximal raw injection}
 \Longrightarrow \text{profile Hall (6.3)}.}
\tag{8.3}
\]

No reverse implication in (8.3) is proved.

## 9. Adversarial audit

The strongest assertion here is (6.3). Its scope has four sharp edges.

1. (A>0) is fixed. If (A\to0), the Gaussian slack is (A^2+o(A^2)),
   and the errors in (3.2) and (5.1) would need a correspondingly sharper
   comparison.
2. The targets with unsafe half-counts are discarded. Their total mass is
   (o(N_q)), but they are not individually matched.
3. Lemma 5.1 proves visibility of one whole profile arc from almost every
   owner. It does not give edge distribution against a subset hidden
   inside that profile.
4. The theorem is one depth and one sign at a time. It neither couples the
   two signs nor supplies the nested common chronology required by the
   contiguous-OR compiler.

Thus independent local-rank matchings rigorously close the coarse
allocation-profile deficit, but the quenched raw cut (7.1) and the grouped
physical Hall theorem remain open.

## 10. Independent re-audit of Lemma 5.1 and (6.3)

The visibility lift and the weighted inequality pass.

For the lower sign, a source in the prescribed profile has respectively
\(a'-F\) and \(c'-F\) singleton edges occupied on the two shores. Hence
it sees the prescribed target profile exactly when (5.3) holds. Failure
places the hypergeometric variable \(F\) within at most two of
\(\min(a',c')\). The safe bounds keep both sample sizes in a fixed compact
subinterval of \((0,d)\), so the two terminal probabilities are uniformly
\(e^{-\Omega(d)}\). Equation (5.5) gives the identical conclusion above.
Product structure of a fixed ordered owner profile and a union bound over
the at most \(q\) touched blocks prove (5.1). The hypothesis (0.3) indeed
implies \(q e^{-cd}=o(1)\), after choosing its absolute constant
\(c_0\le c\).

For (6.3), no union bound over all adjacent profiles is taken. For each
owner profile \(\kappa\), one first fixes the single profile
\(\tau_\kappa\) maximizing the given profile-constant potential among
the arcs carrying the quotient flow. Lemma 5.1 then applies to that one
arc and proves (6.1). The displayed expansion of the quotient flow in
(6.2) proves the other inequality. Division by \(1-\zeta_m\) and the
uniform residual-fibre estimate (1.6) give exactly (6.3).

This audit does not extend (6.3) to a potential varying inside one ordered
profile; that remains the raw-cut gate in Section 7.
