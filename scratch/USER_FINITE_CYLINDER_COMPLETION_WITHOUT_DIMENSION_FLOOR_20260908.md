# Finite cylinder completion without a dimension-only error floor

2026-09-08. The user supplied the theorem removing the dimension-only
error floor, its proof with constant16, the all-dimension consequence,
and the vanishing-hole asymptotic refinement. Root and appendix_a
independently audited the finite argument against the actual master
formulas. Ternary_lift independently audited the asymptotic remainder.
All audits PASS. The exact telescoping ratio below further improves
16 to13. This constant improvement is an audit observation; the main
refinement is the user's contribution.

No mathematical program was executed. This note records and checks the
proof supplied in the conversation; it does not claim to have inspected
or executed a separately mentioned verification script whose path was
not supplied. MASTER_HANDOFF.md is unchanged.

## 1. Finite theorem

Let k>=1. Suppose a nonempty linear or cyclic word on [k] has length or
period m, misses at most h nonempty targets, and
\[
m\le(1+\varepsilon)W(k),\qquad 0\le\varepsilon\le1,\qquad
\eta=h/2^k.
\]
Use the ordinary nonzero-base convention of master Section3.9. Put
\[
d_k=
\begin{cases}
0,&\text{linear},\\
(k-2)_+,&\text{cyclic},
\end{cases}
\qquad \delta_k=d_k/W(k),\qquad
t=\lfloor k\eta^{2/3}\rfloor.
\]
Then
\[
\boxed{\frac{\nu(k+t)}{W(k+t)}
\le1+\varepsilon+\delta_k+
13\min\{\eta\sqrt{k},\eta^{2/3}\}.}
\tag{1}
\]
In particular the user's stated constant16 is valid. Formula(1)
includes t=0 and h=0. The substantive proof uses 0<=eta<=1, as always
holds for the actual number of holes. An unnecessarily larger numerical
upper bound h is also harmless; see the end of Section4.

For eta=o(1), the selected t is o(k), and the error beyond epsilon is
\[
O(\eta^{2/3})+
\begin{cases}
0,&\text{linear},\\
O(k^{3/2}2^{-k}),&\text{cyclic}.
\end{cases}
\tag{2}
\]
There is no separate polynomial error depending only on k.

## 2. Exact completion and a uniform fibre bound

Master(3.43), with its stated nonempty-base hypothesis, gives for EVERY
integer t>=0
\[
\nu(k+t)\le 2^t(m+d_k)+h(\nu(t)+1).
\tag{3}
\]
The partial lift preserves all old covered targets through the new
t-cube. Each hole is repaired by its own complete fibre word, including
the hole with empty new-coordinate part. Thus (3) remains an all-target
construction at t=0; it is not merely an asymptotic inequality.

The elementary finite bounds
\[
\frac{2^n}{\sqrt{2(n+1)}}\le W(n)\le
\frac{2^n}{\sqrt{n+1}}\qquad(n\ge0)
\tag{4}
\]
can be proved without a Stirling remainder. Set
a_j=W(2j)/4^j. Its ratio is (2j+1)/(2j+2), and
W(2j+1)/2^{2j+1}=a_{j+1}. Induction gives
a_j<=1/sqrt(2j+1) because
(2j+1)(2j+3)<=(2j+2)^2. Starting at a_1=1/2,
induction gives a_j>=1/(2sqrt(j)) for j>=1 because
(2j+1)^2>=4j(j+1). These two facts imply (4);
n=0 is immediate.

A uniform bound, including bounded fibre dimensions, is
\[
\boxed{\nu(t)+1\le \frac{4\,2^t}{\sqrt{t+1}}\qquad(t\ge0).}
\tag{5}
\]
Here is a slightly shorter audit of the user's AppendixA.3 argument.
For t>=2, let p=ceil(t/2), q=floor(t/2), a=W(p-1), b=W(q).
The exact formula A.3 implies
\[
\nu(t)+1\le
b2^{p-1}+a2^q+3ab+q+3-2a-2b.
\]
Since q>=1, a>=1, and b>=q, the final residual is at most1-q<=0.
Also p,q+1>=t/2. Applying the upper half of (4) gives
\[
\frac{(\nu(t)+1)\sqrt{t+1}}{2^t}
\le \sqrt{\frac{2(t+1)}t}+
\frac{3\sqrt{t+1}}t.
\]
Both terms decrease with t>0. At t=3 the right side is
sqrt(8/3)+2<4. The cases t=0,1,2 use words of lengths0,1,2
directly. This proves (5). The user's alternative bound retaining
q+3 and checking t>=4 is valid as well.

## 3. An exact ratio, with no error at t=0

Set R(k,t)=2^t W(k)/W(k+t). The adjacent ratios are
\[
\frac{2W(j)}{W(j+1)}=
\begin{cases}
(j+2)/(j+1),&j\text{ even},\\
1,&j\text{ odd}.
\end{cases}
\]
Each ratio lies between1 and(j+2)/(j+1). Multiplying telescopically
therefore proves, for ALL integers t>=0,
\[
\boxed{1\le R(k,t)\le
\frac{k+t+1}{k+1}=1+\frac{t}{k+1}.}
\tag{6}
\]
In particular R(k,0)=1 exactly. No separate O(1/k) term is introduced.
This is stronger than the user's sufficient bound1+2t/k.

## 4. Normalize and optimize the finite integer choice

Combining (3)--(6) gives
\[
\frac{\nu(k+t)}{W(k+t)}
\le(1+\varepsilon+\delta_k)R(k,t)+
4\eta\sqrt{\frac{2(k+t+1)}{t+1}}.
\tag{7}
\]
For k>=1, W(k)>=k, so delta_k<=1. For0<=t<=k,
k+t+1<=3k. Consequently
\[
\frac{\nu(k+t)}{W(k+t)}
\le1+\varepsilon+\delta_k+
3\frac tk+10\eta\sqrt{\frac{k}{t+1}},
\tag{8}
\]
where 4sqrt(6)<10. These are finite inequalities.

Write u=k eta^{2/3}. If t=floor(u)>=1, then t/k<=eta^{2/3}
and t+1>u, so (8) has overhead at most13 eta^{2/3}.
Also u>=1 implies eta^{2/3}<=eta sqrt(k).

If t=0, use (3) directly:
\[
\frac{\nu(k)}{W(k)}
\le1+\varepsilon+\delta_k+\frac{h}{W(k)}
\le1+\varepsilon+\delta_k+2\eta\sqrt{k}.
\]
Here u<1 implies eta sqrt(k)<=eta^{2/3}; h=0 is included.
This proves (1).

If an artificial upper bound h gives eta>1, the same conclusion is
trivial: (4)--(5) give nu(n)/W(n)<=4sqrt(2) for every n, whereas
the right side of (1) is at least14. Thus no hidden eta restriction
invalidates the stated finite inequality for an upper bound on holes.

## 5. Consequences in every large target dimension

For linear base families in every sufficiently large dimension put
\[
e_K=\sup_{j\ge\lfloor K/2\rfloor}\varepsilon_j,\qquad
a_K=\sup_{j\ge\lfloor K/2\rfloor}\eta_j.
\]
If e_K,a_K tend to zero, take
t=floor(K a_K^{2/3}) and k=K-t. Eventually k>=K/2 and t<=k.
Use the base in dimension k in (8). When a_K>0,
t+1>K a_K^{2/3}, giving
\[
t/k=O(a_K^{2/3}),\qquad
\eta_k\sqrt{k/(t+1)}\le a_K^{2/3}.
\]
When a_K=0, t=0 and no fibre repair is needed. Hence
\[
\frac{\nu(K)}{W(K)}\le1+e_K+O(a_K^{2/3}).
\tag{9}
\]
For cyclic families add O(K^{3/2}2^{-K/2}). This uses the actual
target dimension K, not only the particular completed dimensions.

Examples of errors beyond epsilon+delta_k are:

| Hole density | Added coordinates | Completion error |
|---|---|---|
| O(k^{-1}) | O(k^{1/3}) | O(k^{-2/3}) |
| O(k^{-3/2}) | O(1) | O(k^{-1}) |
| O(k^{-2}) | zero eventually | O(k^{-3/2}) |

For h=O(W(k)), the established O(k^{-1/3}) error is unchanged.
The balancing exponent2/3 has not been improved.

## 6. Leading asymptotic constant when the fibre grows

Suppose eta tends to zero and k eta^{2/3} tends to infinity. Write
A=1+epsilon and B=c_9 eta, and take an integer t nearest
k(B/A)^{2/3}. Then t tends to infinity, t=o(k), and
1/k=o(eta^{2/3}). The already proved asymptotic upper bound
nu(t)<=(c_9+o(1))W(t), the central-binomial asymptotics, and (3)
give, with lambda=t/k,
\[
\frac{\nu(k+t)}{W(k+t)}
\le \sqrt{1+\lambda}
\left(A+\frac{B}{\sqrt{\lambda}}\right)+
o(\eta^{2/3}).
\]
The repair-word remainder is o(eta sqrt(k/t))=o(eta^{2/3}).
Width-ratio errors are O(1/k), and fibre-width errors have an extra
factor O(1/t). The fibre's extra1 contributes, after dividing by
eta^{2/3}, O(sqrt(t)2^{-t})=o(1). Cyclic cutting is exponentially
small compared with eta^{2/3}. Integer rounding changes lambda by
O(1/k), and the derivative of the displayed function is bounded in
that neighborhood. Thus all these errors have the asserted scale.

The exact minimum occurs at lambda=(B/A)^{2/3}, yielding
\[
\boxed{\frac{\nu(k+t)}{W(k+t)}
\le\left((1+\varepsilon)^{2/3}+
 (c_9\eta)^{2/3}\right)^{3/2}+
o(\eta^{2/3}).}
\tag{10}
\]
If epsilon tends to zero, the coefficient of eta^{2/3} beyond
1+epsilon is (3/2)c_9^{2/3}+o(1). This note uses that exact expression;
no separate decimal evaluation was needed for the audit.

## 7. Previously recorded binary-ten material and claim boundary

The conditional full42-row coefficient1.175932662442944... is already
proved and exactly enclosed in Section5 of
BINARY10_PARTIAL_MACRO_COVER_REPAIR_LEDGER_20260908.md.
The seven-cycle exclusion is already recorded under Symmetry reductions
in BINARY10_INVOLUTION_FINITE_GATE_20260907.md.

The user's argument for that exclusion is correct. A physical full
prefix rectangle determines its unordered shores as its unique
complementary pair of rank-five targets. If a nontrivial seven-cycle
stabilized a row, its action on those two shores would be trivial,
forcing an invariant five-set. Such a set cannot be a union of a
seven-orbit and three fixed points. Thus the rotated row is distinct.
A row covering the fixed three-set has two distinct immediate prefix
extensions by moving labels. A rotation takes one extension to the
other, forcing a repeated rank-four target. But42 rows have exactly
42*5=210=binom(10,4) rank-four occurrences, so all-rank coverage
requires those targets exactly once. This is a contradiction.

Invariance here means invariance of the row bank, not merely its
full-cube union. The result does not exclude unrestricted42-row banks.
Neither such a bank nor a near-width density-almost-cover family has
been supplied. The new finite completion theorem strengthens the
conditional route; it does not improve the certified full-cube
coefficient c_9=1.180703803847... or prove coefficient one.
