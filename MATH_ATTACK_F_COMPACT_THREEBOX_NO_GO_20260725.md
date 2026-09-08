# Lane F: an unrestricted endpoint dual closes the compact three-box gate

Date: 2026-07-25

## 0. Result

For integers \(p,q,r\ge 1\), let

\[
Q(p,q,r)=[0,p]\times[0,q]\times[0,r]
\]

with the product order. A literal range-maximum word is a sequence

\[
v_1,\ldots,v_N\in Q(p,q,r)\setminus\{0\}
\]

such that every nonzero target \(T\in Q(p,q,r)\) is the coordinatewise
maximum of some contiguous interval \(v_\ell,\ldots,v_s\). Write
\(g_3(p,q,r)\) for the minimum possible \(N\).

The requested compact theorem is false. The obstruction is not tied to a
canonical braid, a chosen middle order, a common pin, or a restricted class
of words.

### Theorem A (two-endpoint plateau dual)

Put

\[
P=p+q,
\qquad
W=(p+1)(q+1).
\]

If \(r\ge P\), then

\[
\boxed{w(p,q,r)=W}
\tag{0.1}
\]

and every literal range-maximum word satisfies

\[
\boxed{
g_3(p,q,r)
\ge
W+
\left\lceil
\frac{W(r-p-q)}{2r}
\right\rceil .
}
\tag{0.2}
\]

In particular, for every integer \(t\ge1\),

\[
\boxed{
g_3(t,t,3t)
\ge
(t+1)^2+
\left\lceil\frac{(t+1)^2}{6}\right\rceil .
}
\tag{0.3}
\]

Since \(w(t,t,3t)=(t+1)^2\), (0.3) gives

\[
g_3(t,t,3t)-w(t,t,3t)
\ge \frac16t^2.
\tag{0.4}
\]

All three side lengths in this family are comparable to \(t\). Hence the
handoff's uniform estimate

\[
g_3(p,q,r)\le w(p,q,r)+o(R^2)
\]

on fixed compact ratio ranges \(\delta R\le p,q,r\le CR\) is impossible.
This definitively closes Lane F. It does **not** disprove the global
contiguous-OR conjecture: a global word may share physical letters and
witnesses across different product boxes, whereas the rejected reduction
pays for each local box separately.

The remainder is a self-contained proof of Theorem A.

---

## 1. The full-width plateau

Give \(Q(p,q,r)\) the rank

\[
\operatorname{rk}(x,y,z)=x+y+z.
\]

Put

\[
H=r-P\ge0.
\]

For every \(0\le j\le H\), define the plateau layer

\[
\Lambda_j
=
\{(x,y,P+j-x-y):0\le x\le p,\ 0\le y\le q\}.
\tag{1.1}
\]

The displayed third coordinate lies between \(j\) and \(P+j\le r\), so
every point in (1.1) belongs to the box. Thus

\[
|\Lambda_j|=W.
\tag{1.2}
\]

Each \(\Lambda_j\) is an antichain because it is a rank layer. Conversely,
two points in one vertical column \((x,y,*)\) are comparable, so an
antichain contains at most one point in each of the \(W\) vertical columns.
Therefore every antichain has size at most \(W\), while (1.2) attains this
bound. This proves (0.1) exactly.

---

## 2. The two literal endpoint partitions

Fix an arbitrary universal word \(v_1,\ldots,v_N\). For every target
\(T\) in

\[
\mathcal P=\bigcup_{j=0}^{H}\Lambda_j
\tag{2.1}
\]

choose one of its actual contiguous witnesses

\[
I_T=[\ell_T,s_T].
\tag{2.2}
\]

The same selected interval supplies both endpoint systems below. No
compatibility or extremality is imposed on these choices.

### Lemma 2.1 (endpoint chains and orthogonality)

Grouping the targets in \(\mathcal P\) by their selected left endpoints
\(\ell_T\) gives a chain partition \(\mathcal C_L\). Grouping them by their
selected right endpoints \(s_T\) gives another chain partition
\(\mathcal C_R\). Moreover, a chain in \(\mathcal C_L\) and a chain in
\(\mathcal C_R\) have at most one target in common.

#### Proof

If two selected intervals have the same left endpoint, the one with the
smaller right endpoint is contained in the other. Coordinatewise maxima
are monotone under interval inclusion, so their targets are comparable.
This proves that every left-endpoint class is a chain. The same argument,
reversing left and right, proves the right-endpoint claim.

If two distinct targets belonged to the same left class and the same right
class, their selected intervals would have the same two endpoints. They
would be the coordinatewise maximum of the same physical interval and
hence would be equal, a contradiction. Thus the partitions are
orthogonal. \(\square\)

Each rank layer is an antichain of size \(W\), so each endpoint partition
has at least \(W\) nonempty chains. Each chain is labelled by one physical
endpoint position, so it has at most \(N\) chains. Consequently

\[
N\ge W.
\tag{2.3}
\]

Write

\[
N=W+D,
\qquad D\in\mathbb Z_{\ge0}.
\tag{2.4}
\]

For \(E\in\{L,R\}\), let \(C_E\) be the number of nonempty chains in
\(\mathcal C_E\), and put

\[
C_E=W+\delta_E.
\tag{2.5}
\]

Then

\[
0\le\delta_E\le D.
\tag{2.6}
\]

---

## 3. Covers forced in one endpoint partition

Fix one endpoint partition and abbreviate its chain count by

\[
C=W+\delta.
\]

For \(0\le j\le H\), let \(A_j\) be the set of chains meeting
\(\Lambda_j\). A chain meets an antichain in at most one point, so

\[
|A_j|=W.
\tag{3.1}
\]

Both \(A_j\) and \(A_{j+1}\) lie in a universe of \(C\) chains. Therefore

\[
|A_j\cap A_{j+1}|
\ge |A_j|+|A_{j+1}|-C
=W-\delta.
\tag{3.2}
\]

Whenever one chain contains a point of \(\Lambda_j\) and a point of
\(\Lambda_{j+1}\), those two points are comparable and their ranks differ
by one. They consequently form a cover edge of the box poset. Summing
(3.2) over the \(H\) adjacent pairs of layers, the endpoint partition
contains at least

\[
H(W-\delta)
\tag{3.3}
\]

plateau cover edges. This does not assume that the endpoint chains are
saturated: membership in these two particular adjacent ranks already
forces a cover.

Use the potential

\[
\phi(x,y,z)=x+y,
\qquad 0\le\phi\le P.
\tag{3.4}
\]

Exactly \(W\) chains meet the bottom layer \(\Lambda_0\). The remaining
\(\delta\) chains begin internally in the plateau slab. Likewise, exactly
\(W\) chains meet the top layer \(\Lambda_H\), and \(\delta\) chains end
internally. The multisets of \(\phi\)-values on \(\Lambda_0\) and
\(\Lambda_H\) are identical: both contain \(x+y\) once for each pair
\((x,y)\in[0,p]\times[0,q]\). Telescoping \(\phi\) on all chains therefore
gives

\[
\begin{aligned}
\sum_{C'}
\bigl(\phi(\max C')-\phi(\min C')\bigr)
&=
\sum_{\text{internal chain ends}}\phi
-
\sum_{\text{internal chain starts}}\phi\\
&\le P\delta.
\end{aligned}
\tag{3.5}
\]

Along a box-poset chain, \(\phi\) never decreases. Every horizontal cover
(an \(x\)- or \(y\)-increment) raises \(\phi\) by one, whereas a vertical
\(z\)-cover leaves \(\phi\) unchanged. Hence at most \(P\delta\) of the
covers counted in (3.3) are horizontal. The endpoint partition contains
at least

\[
H(W-\delta)-P\delta
=HW-(H+P)\delta
=HW-r\delta
\tag{3.6}
\]

vertical target-poset cover edges.

The right side of (3.6) is allowed to be negative; then it is merely a
vacuous lower bound. This causes no sign problem when the two endpoint
ledgers are added.

---

## 4. Orthogonality closes the ledger

There are exactly

\[
WH
\tag{4.1}
\]

vertical cover edges in the plateau slab: for each of the \(W\) columns,
there is one edge across each of its \(H\) adjacent rank transitions.

No vertical cover can occur in both endpoint partitions. Indeed, if the
two targets of such a cover were in one common left-endpoint chain and one
common right-endpoint chain, those two chains would have two common
targets, contradicting Lemma 2.1. Applying (3.6) to both partitions and
using the capacity (4.1) yields

\[
\bigl(HW-r\delta_L\bigr)
+
\bigl(HW-r\delta_R\bigr)
\le HW.
\tag{4.2}
\]

Thus

\[
HW
\le r(\delta_L+\delta_R)
\le 2rD,
\tag{4.3}
\]

where the final inequality is (2.6). Since \(D\) is an integer,

\[
D
\ge
\left\lceil\frac{HW}{2r}\right\rceil
=
\left\lceil
\frac{W(r-p-q)}{2r}
\right\rceil.
\tag{4.4}
\]

Combining (2.4) and (4.4) proves (0.2). When \(H=0\), the conclusion
correctly reduces to \(D\ge0\); the strict counterexample uses \(H>0\).

---

## 5. Quantitative closure of the compact lane

More generally, fix positive integers \(a,b,c\) with \(c>a+b\), and put

\[
p=at,\qquad q=bt,\qquad r=ct.
\]

Theorem A gives

\[
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-w(at,bt,ct)}{t^2}
\ge
\frac{ab(c-a-b)}{2c}>0.
\tag{5.1}
\]

For the integral ray \((a,b,c)=(1,1,3)\), formula (4.4) is exactly (0.3).
If the comparison scale is chosen as the longest side \(R=3t\), then
(0.4) becomes

\[
g_3(t,t,3t)-w(t,t,3t)
\ge \frac1{54}R^2.
\tag{5.2}
\]

Thus the contradiction is independent of the harmless convention used for
the common compact scale \(R\). It occupies the full open fixed-ratio cone
\(c>a+b\), not merely one exceptional sequence.

This no-go concerns the handoff's compact-comparability quantifier
\(\delta R\le p,q,r\le CR\). It does not by itself refute the narrower
near-cube assertion \(p/R,q/R,r/R\to1\); that narrower assertion is not
the assigned uniform gate.

---

## 6. Adversarial scope audit

The proof uses only the following literal facts.

1. Every selected witness is an actual contiguous physical interval.
2. Enlarging an interval at one fixed endpoint can only increase its
   coordinatewise maximum.
3. The same selected interval supplies both its left and right endpoint;
   the proof never chooses the two endpoint systems independently.
4. The two endpoint partitions need not be saturated, canonical, or
   balanced.
5. No unique occurrence, common pin, or factorability hypothesis is used.
6. Empty physical endpoint classes are harmless; only nonempty classes are
   counted, and there are at most \(N\) of them.
7. Possible negative values of the individual lower bound (3.6) remain
   legitimate lower bounds and do not reverse any inequality.
8. All finite rounding is confined to the final integer ceiling (4.4).

The main proof was independently reconstructed three ways after this
write-up. All three audits verified the chain counts, the potential
telescope, the disjoint vertical-cover ledger, the ceiling direction, and
the specialization (0.3). No auditor found a hidden endpoint-choice or
literal-realizability assumption.

Therefore an explicit braid cannot evade the theorem by changing witness
choices, interleaving ranks, using multiple occurrences, or crossing
selected intervals. The lane ends with the rigorous no-go (0.3), not an
unproved replacement lemma.

