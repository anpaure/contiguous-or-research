# First exit from a Johnson top gives two native terminal banks

**Date:** 2026-08-03  
**Status:** unconditional occurrence theorem on every sufficiently long
simple cyclic q1 diagonal. No computation is used. The theorem constructs
two adjacent \(W\)-element physical interval banks at the first exit from
each Johnson top. These banks have a nested same-phase upper type, not the
canonical folded-C8 cross-ray type. Terminal type conversion/acceptance,
background compatibility, and all-k regeneration remain separate.

## 0. Result

Let \(T_0,\ldots,T_{W-1}\) be a cyclic simple Johnson row of distinct
rank-\(r\) sets: consecutive owners have intersection rank \(r-1\).
Assume \(W>r+1\).  (The later address-capacity hypothesis
\(d+r+2<W\) is stronger, and the intended complete middle layer also
satisfies this condition.)
Assume it is realized by one cyclic source word

\[
T_i=\bigcup_{h=i}^{i+d}A_h,                              \tag{0.1}
\]

with every \(A_h\ne\varnothing\). Put

\[
R_i=T_i\cup T_{i+1}.                                     \tag{0.2}
\]

Then \(|R_i|=r+1\). For each \(i\), define the first-exit distance

\[
h_i=\min\{h\ge2:T_{i+h}\not\subseteq R_i\}.              \tag{0.3}
\]

The minimum exists (using \(W>r+1\)) and

\[
2\le h_i\le r+1.                                         \tag{0.4}
\]

Define the immediate-upper, plateau-end, and first-exit occurrences

\[
\begin{aligned}
q_i&=[i,i+d+1]_W,\\
w_i&=[i,i+d+h_i-1]_W,\\
v_i&=[i,i+d+h_i]_W.
\end{aligned}                                            \tag{0.5}
\]

Their values are

\[
\operatorname{OR}(q_i)=\operatorname{OR}(w_i)=R_i,
\qquad
\operatorname{OR}(v_i)=V_i:=R_i\cup T_{i+h_i},           \tag{0.6}
\]

and

\[
|V_i|=r+2.                                                \tag{0.7}
\]

If \(d+r+2<W\), the \(W\) addresses \(w_i\) and the \(W\) addresses
\(v_i\) are pairwise distinct across both banks. Consequently every ticket
\(i\) has the deterministic paired terminal occurrence

\[
(w_i,v_i).                                                \tag{0.8}
\]

These are two already existing intervals of the same word. If one fixed
terminal state accepts the **nested-upper** pair of types \((R_i,V_i)\),
the pairs form an exact two-coordinate terminal bank of size \(W\), with no
appended cells.  This conditional bank is not an occurrence lift of the
canonical cross-ray pair without an additional type-conversion theorem.

The inclusion

\[
R_i\subset V_i                                           \tag{0.9}
\]

is Boolean Hasse, and \(w_i\subset v_i\) is a one-endpoint physical
interval cover. When \(h_i=2\), \(w_i=q_i\), giving the fixed-width q1/q2
ladder. For larger \(h_i\), the intervening source positions change no
value beyond \(R_i\); the complete plateau block from \(q_i\) to \(w_i\),
followed by the final Hasse step, is one canonical source-free route.

## 1. Existence and bound for the first exit

The rank-\(r\) subsets contained in the rank-\((r+1)\) set \(R_i\) are
exactly its \(r+1\) facets. The owner row is simple. Hence at most \(r+1\)
consecutive owners beginning with \(T_i\) can all lie inside \(R_i\).

Because the row has more than \(r+1\) distinct owners, it cannot be wholly
contained in those facets; hence the cyclic forward scan must exit.

The first two, \(T_i,T_{i+1}\), do lie inside \(R_i\). Therefore some
\(T_{i+h}\) with

\[
2\le h\le r+1                                             \tag{1.1}
\]

leaves \(R_i\), proving (0.3)--(0.4).

## 2. Exact rank at first exit

By minimality of \(h_i\),

\[
T_i,T_{i+1},\ldots,T_{i+h_i-1}\subseteq R_i.             \tag{2.1}
\]

The first two already have union \(R_i\), so

\[
\bigcup_{j=0}^{h_i-1}T_{i+j}=R_i.                        \tag{2.2}
\]

The last inside owner \(T_{i+h_i-1}\) and first outside owner
\(T_{i+h_i}\) are Johnson adjacent. The latter is obtained by deleting one
coordinate and inserting one coordinate. Since it is not contained in
\(R_i\), the inserted coordinate lies outside \(R_i\); it is the only
coordinate of \(T_{i+h_i}\) outside \(R_i\). Therefore

\[
|R_i\cup T_{i+h_i}|=|R_i|+1=r+2,                        \tag{2.3}
\]

proving (0.7) and (0.9).

## 3. Literal interval identity

From (0.1),

\[
\bigcup_{j=0}^{h}T_{i+j}
=\bigcup_{t=i}^{i+d+h}A_t.                               \tag{3.1}
\]

For \(h=1\), this is the value of \(q_i\) and equals \(R_i\). For every
\(1\le h<h_i\) it remains \(R_i\), so in particular \(w_i\) has value
\(R_i\). For \(h=h_i\), (2.2)--(2.3) show that it equals \(V_i\).
This proves (0.5)--(0.6).

The interval \(w_i\) is obtained at the end of the plateau and \(v_i\) is
obtained from it by adding exactly the right endpoint \(i+d+h_i\). The
first value increase is therefore the final physical cover step, from
\(R_i\) to \(V_i\). The nested interval block is a literal witness of one
Boolean rank-one extension.

## 4. Address capacity

Every \(w_i\) and \(v_i\) has cyclic start address \(i\). Under
\(d+r+2<W\), all their lengths are strictly between zero and \(W\), so the
start is uniquely recoverable from the oriented cyclic interval address.
Thus \(i\ne j\) implies

\[
w_i\ne w_j,\qquad v_i\ne v_j,\qquad w_i\ne v_j.          \tag{4.1}
\]

For one index,

\[
|v_i|=|w_i|+1.                                           \tag{4.2}
\]

Therefore no \(v_i\) equals a \(w_j\). The two banks contain \(2W\)
distinct physical interval addresses even if some Boolean values \(R_i\)
or \(V_i\) repeat.

As usual for OR words, overlap of constituent source positions of two
different interval addresses is not a capacity collision. If a stronger
auxiliary model node-prices every intervening singleton or intermediate
interval, the contracted plateau route may fail; that is not the native
interval-address model.

## 5. Exact scope

The theorem proves from a simple cyclic q1 owner row alone:

1. a first-exit distance at most \(r+1\) for every seam;
2. a rank-\((r+2)\) occurrence above every immediate-upper occurrence;
3. two adjacent \(W\)-element terminal banks at the plateau exits; and
4. deterministic paired records \((w_i,v_i)\) requiring no extra positions.

It does not prove:

1. that the canonical cross-ray terminal ticket accepts \((R_i,V_i)\);
2. that all guards, deadlines, or transported background retain both cells;
3. that a node-priced implementation accepts plateau contraction;
4. a q1-exact simple carrier in every dimension; or
5. lower compilation, residence, regeneration, or
   \(\nu(k)\le B(k)+O(1)\).

Thus raw interval-address supply is no longer absence of a second native
\(W\)-cell bank.  The canonical two-cross-ray capacity theorem is **not**
discharged: its tickets require separately addressed opposite-ray
coordinates, normally in opposite phases, whereas `(w_i,v_i)` is a
same-phase nested Hasse pair with

\[
                         R_i\subset V_i,\qquad |V_i-R_i|=1.
\]

The remaining statement is a type-preserving conversion/acceptance theorem
from the canonical ticket pair to these first-exit upper occurrences in one
complete cap/background state.
