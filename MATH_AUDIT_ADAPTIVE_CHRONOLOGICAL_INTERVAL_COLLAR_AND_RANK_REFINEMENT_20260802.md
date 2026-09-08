# Independent audit: interval profiles, multiboundary erosion, collars, and rank refinement

**Date:** 2026-08-02  
**Verdict:** **PASS after one quantifier repair and four TeX-only repairs.**
The new reductions and finite obstructions are proof-safe.  They do not
prove an all-\(k\) \(d(k)+O(1)\) chronology or a contiguous-OR word.

Audited artifacts:

- `MATH_THEOREM_BALANCED_CORE_OWNER_INTERVAL_HALL_AND_MULTIBOUNDARY_EROSION_20260802.md`;
- `MATH_THEOREM_FIXED_COMPLETE_COLLAR_RECURSION_CAPACITY_AND_FORCED_BYPASS_20260802.md`;
- `MATH_THEOREM_CHRONOLOGICAL_ROOT_WIDTH_RANK_REFINEMENT_AND_K41_THREE_CUT_GATE_20260802.md`;
- their three exact audit scripts named in Section 5.

## 1. Owner-interval and interval-profile audit

For a setwise bipartition of sizes \(h,\ell\), a rank-\(R\) owner type is
indexed by \(p=|O\cap H|\) in

\[
 P_R=[p_-,p_+],\qquad p_-=\max(0,R-\ell),\quad p_+=\min(h,R).
\]

A target type \(u=(i,j)\) is contained in precisely the owner types

\[
 I(u)=[\max(i,p_-),\min(R-j,p_+)].                  \tag{1.1}
\]

This follows directly from \(i\le p\) and \(j\le R-p\).  It also proves
the antitonicity \(u\le v\Rightarrow I(v)\subseteq I(u)\).

The endpoint clipping in the theorem note is necessary and correct:

\[
 I(i,j)\subseteq[a,b]
 \Longleftrightarrow
 (a=p_-\text{ or }i\ge a)
 \ 	ext{and}\
 (b=p_+\text{ or }j\ge R-b).                       \tag{1.2}
\]

The unclipped two-inequality formula fails, for example, at an odd-
dimensional right endpoint where \(R-j>p_+\).

The decisive necessity step in the interval theorem is sound.  For an
upset \(U\) and interval \(J\), put

\[
 Q_J=\{u:I(u)\subseteq J\},\qquad U_J=U\cap Q_J.
\]

Antitonicity makes \(Q_J\) an upset.  Restricting to \(U_J\) can create
new roots, but cannot destroy any old root whose interval lies in \(J\):

\[
 R_\tau(U)\cap Q_J\subseteq R_\tau(U_J).            \tag{1.3}
\]

This one-sided inclusion is exactly what necessity needs.  Conversely,
the union of the root intervals splits into disjoint maximal interval
components; every root interval lies in one component.  Summing the
interval inequalities over those components gives the full exposed-root
inequality.  Thus the interval theorem is equivalent to vertex Hall after
the already proved invariant-upset compression.

The profile

\[
 E_\tau(J)=\max\{w(R_\tau(V)):V\subseteq Q_J
       \text{ an invariant chronological upset}\}             \tag{1.4}
\]

is therefore the exact weakest owner-side statistic currently isolated:

\[
                         E_\tau(J)\le\operatorname {cap}(J)
                         \quad\text{for every interval }J.     \tag{1.5}
\]

The maximum over sub-upsets is load-bearing.  At K9 all fifteen complete
rectangle states \(Q_J\) pass, including root mass \(125\) against full
capacity \(126\), while the proper upset

\[
 \{(3,0)\}\cup\{(i,4-i):0\le i\le4\}
\]

has exposed-root mass \(130>126\).  Exhaustive enumeration of every
sub-upset inside every K9 rectangle reproduces the exact profile table and
finds only this full-interval profile deficient.

The adversarial menu recursion is also exact.  At each time, earlier
choices force their upper closure \(F_t\); the freely chosen residual part
is an arbitrary upper set \(A_t\) of the remaining slice.  Exactly the
members of \(A_t\) are roots.  This gives a noncircular finite definition
of (1.4), but no all-\(k\) bound on it.

## 2. Erosion and bounded-sidecar audit

For root bank \(R_t\), palette \(A_t=\bigcup_{u\in R_t}I(u)\), and carried
suffix palette \(S_{t+1}=\bigcup_{s>t}A_s\), define

\[
 \rho_t=\operatorname {cap}(A_t)-w(R_t),\qquad
 \varepsilon_t=\operatorname {cap}(A_t\cap S_{t+1}).
\]

Finite additivity gives

\[
 \operatorname {cap}(A_t\cup S_{t+1})-\operatorname {cap}(S_{t+1})
 =\operatorname {cap}(A_t)-\varepsilon_t.
\]

Summing from late to early and substituting
\(w(R_t)=\operatorname {cap}(A_t)-\rho_t\) proves exactly

\[
 w(R_\tau(U))-|\Gamma_R(U)|
 =\sum_t(\varepsilon_t-\rho_t).                    \tag{2.1}
\]

No laminarity or connectedness assumption is hidden here.

The K9 and K46 arithmetic independently replays:

\[
\begin{array}{c|c|c|c}
 &\text{bank reserves}&\text{overlap erosion}&\text{deficiency}\\ \hline
K9&(0,16)&20&4\\
K46&(1\,488\,213\,570\,689,\ 2\,251\,954\,787\,055)
 &3\,804\,801\,426\,540&64\,633\,068\,796.
\end{array}
\]

Thus independent local-bank expansion is not compositional.

The literal bounded-component sidecar is refuted correctly.  There are
\(R\) top-target orbit types, each with a one- or two-point owner interval.
Some one of \(q\) blocks contains at least \(\lceil R/q\rceil\) of them.
Taking every third occupied index gives a same-time top-rank upset with at
least

\[
             \left\lceil {1\over3}
             \left\lceil {R\over q}\right\rceil\right\rceil   \tag{2.2}
\]

disconnected palette components.  At \(q=d+O(1)\), this is
\(\Omega(\sqrt{k})\).  The obstruction concerns a literal endpoint list;
it does not refute the aggregate interval profile (1.4).

## 3. Complete-collar audit

For a pre-collar block \(P_i\) and \(F\subseteq P_i\), take the
chronological upset generated by \(F\).  Its time-\(i\) members are exactly
\(\operatorname {Up}_{P_i}(F)\), all exposed; every later generated member
has an earlier generator and is not exposed.  Its owner shadow is
\(\Gamma_{m+1}(F)\).  Hence

\[
 |\operatorname {Up}_{P_i}(F)|\le|\Gamma_{m+1}(F)|.             \tag{3.1}
\]

This argument is independent of the number of complete later ranks.  In
particular every pre-collar block must itself have a containment matching
into the owners.  Appending a collar cannot repair a bad lower block.

The principal-star counterblock is also correctly scoped.  If

\[
 {\cal F}_{A,L}=\{S:A\subseteq S,\ |S|\le m-L\}
\]

has mass at most \(W\) but larger than its rank-\(m+1\) owner shadow, it is
a capacity-legal one-block violation of (3.1) after every \(L\)-rank
collar.  Choosing \(|A|=\lceil\log_2(4\sqrt{k})\rceil\) proves existence
for every fixed \(L\) and all sufficiently large odd \(k\).  This refutes
only an unsplit bad block, not witness-adaptive splitting.

For a dedicated collar, scalar counting gives

\[
 Q_L=\left\lceil {\Lambda\over W}+E_L\right\rceil,
 \qquad
 E_L=\sum_{j=0}^{L-1}
       \left(1-{{k\choose m-j}\over W}\right).                 \tag{3.2}
\]

The exact ratio product

\[
 {{k\choose m-j}\over W}
 =\prod_{u=0}^{j-1}{m-u\over m+2+u}
\]

gives

\[
 E_L=\left({2\over3}+o(1)\right){L^3\over k}
 \quad(L\to\infty,\ L=o(\sqrt{k})).                \tag{3.3}
\]

Thus \(d+O(1)\) forces \(L=O(k^{1/3})\) in this architecture.  When
\(L=d-1\), the excess coefficient is

\[
 \int_0^{\sqrt{\pi/8}}(1-e^{-2x^2})\,dx
 =0.13165526428568464\ldots .                       \tag{3.4}
\]

The independent exact replay gives K121 scalar depth \(8=d+1\), but K201
scalar depth \(11=d+2\); K153 is the first odd dimension where this
specific layout reaches at least \(d+2\).

The complete-base reset bound is conditional only on the explicitly
stated anchored lower-factor antecedent.  Its scalar excess is

\[
 \left(\sqrt{\pi/2}+o(1)\right){L^2\over\sqrt{k}},              \tag{3.5}
\]

so a \(d+O(1)\) base-reset argument requires \(L=O(k^{1/4})\).  This is
not a lower bound for global skipping.

Finally, only \({k\choose t}\) chains can meet the first collar rank
\(t=m-L+1\), and each carries at most one target from each of \(b\) lower
times.  Therefore at least

\[
 \left\lceil{(M_<-b{k\choose t})_+\over b}\right\rceil         \tag{3.6}
\]

lower-carrying chains skip rank \(t\).  At K121 this is exactly

\[
65\,819\,038\,470\,988\,494\,034\,825\,456\,661\,865\,107
=0.3434407704\ldots W.
\]

Hence the certified K121 factor cannot be reinterpreted as a rank-55 reset
with only \(O(1)\) exceptional chains.

## 4. Root width and rank-refinement audit

The root-width theorem requires the middle owner rank
\(R=\lceil k/2\rceil\), now stated explicitly.  For a
containment-monotone chronology, roots from distinct times are
incomparable.  The union of a maximum antichain from each same-time root
bank is therefore an antichain and a Boolean symmetric-chain decomposition
injects it into distinct middle owners.  This proves

\[
 |R_\tau(U)|-|\Gamma_R(U)|
 \le\sum_t(|R_t|-\operatorname {width}(R_t)).                    \tag{4.1}
\]

A failed upset must consequently contain comparable same-time roots.
Splitting that one block between their ranks adds successor arcs and
removes none; the old upset remains an upset because weak-time containment
already included the same-time relation.  At least the upper root ceases
to be exposed, so that witness strictly improves.

The original informal statement used containment monotonicity for the
block-count bound.  That quantifier was too weak and has been repaired.
The \(q+r-1\) bound requires **global rank order**

\[
                         |x|<|y|\Longrightarrow\tau(x)\le\tau(y),
\]

because only then can each rank boundary cross at most one time block.
The one-block exchange itself still needs only containment monotonicity.

For the frozen K41 ascending-mask chronology, exact enumeration confirms:

- every refinement by zero, one, or two global rank cuts fails;
- the three exhaustive obstruction cases have deficits
  \(3\,796\,297\,200\), \(6\,407\,937\,150\), and
  \(6\,659\,211\,024\); and
- cuts \(\{17,18,19\}\) give eight capacity-legal blocks and both the
  dense and sparse networks return \(2^{40}-1\).

Thus three cuts are necessary and sufficient only within this frozen
pure-refinement class.  No lower bound on arbitrary K41 orderings or on a
universal additive constant follows.

## 5. Replay and scope

The following commands all pass independently:

```text
python3 scratch/audit_balanced_core_multiboundary_erosion_20260802.py
python3 scratch/audit_fixed_complete_collar_recursion_20260802.py
python3 scratch/audit_k41_rank_refinement_gate_20260802.py
```

The first two reconstruct all displayed binomial arithmetic.  The K41
audit exhausts every at-most-two-cut refinement and checks the three-cut
repair in independent dense and product-Hasse encodings.

Still **unproved** are adaptive all-\(k\) control of (1.4), a constant-size
root-chain breaker, an anchored \(d+C\) factor, and every literal overlap,
endpoint, address/history, residence, compiler, or regenerative theorem.
