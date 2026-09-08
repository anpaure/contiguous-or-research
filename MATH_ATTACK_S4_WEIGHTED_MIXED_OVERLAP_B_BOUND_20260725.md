# The actual-catalogue mixed-overlap bound at \(s=4\)

Date: 2026-07-25

Method: pure mathematics only.

## 0. Statement and verdict

Work in the symmetric bounded-displacement protected-strip catalogue.  Let
\(A\) be the raw degree of a tag, let \(p\) be the marking probability in
the isolated four-antichain pruning, and put

\[
 D=pA=m^{23/6-o(1)},
 \qquad K=m^{1+o(1)}.                                \tag{0.1}
\]

Here \(K\) is an upper bound for the number of protected targets claimed by
one path.  For a retained path \(P\), define the cross-tag nonlinear
neighbourhood

\[
 N_2(P)=\{E:\operatorname{tag}(E)\ne\operatorname{tag}(P),
                 \ |C(P)\cap C(E)|\ge2\},
 \qquad B_2(P)=|N_2(P)|.                            \tag{0.2}
\]

The isolated-pruning experiment can be chosen, simultaneously with the
usual balanced-fibre exceptional ledger, so that every retained \(P\)
satisfies

\[
 \boxed{
 B_2(P)
 \le m^{o(1)}D{K\over m}+O(mK^2).}                  \tag{0.3}
\]

If \(x_E=1/A'_{\operatorname{tag}(E)}\) is the uniform weight on each good
retained tag fibre and \(A'_U\ge cD\), then

\[
 \boxed{
 b_2(P):=\sum_{E\in N_2(P)}x_E
 \le m^{o(1)}{K\over m}
       +O\!\left({mK^2\over D}\right).}             \tag{0.4}
\]

At (0.1), the additive term in (0.4) is

\[
 {mK^2\over D}=m^{-5/6+o(1)}=o(1).                 \tag{0.5}
\]

The leading span-one term is only \(m^{o(1)}K/m=m^{o(1)}\).  Therefore
the proved conclusion is

\[
 B_2(P)\le Dm^{o(1)},                               \tag{0.6}
\]

not \(B_2=o(D)\).  Width at most three cannot remove this leading channel:
two adjacent comparable grid cells already form a width-one common shape.

This bound is not strong enough for the matching dual.  In fact the
cross-tag parameter \(B_2\) misses the decisive first-order obstruction
entirely.  A pure distinct-tag singleton line system with no common target
has at most \(K^2-K+1=o(D)\) supports, so an unblown projective-plane
obstruction cannot occur at \(D\)-scale.  On the other hand, the class of
literal return-free strip multicovers contains a three-tag Shannon
blow-up of size \(3D/2\), with every cross-tag intersection a singleton and
hence \(B_2=0\).  This is an actual-catalogue class obstruction, not a claim
that a particular previously fixed pruning outcome contains the blow-up.

Thus the exact remaining gates are joint, weighted inequalities:

1. a canonical pair-star sum for the nonlinear sector; and
2. an odd-bundle inequality for the singleton sector.

Neither follows from a marginal or average \(B_2\)-estimate.

## 1. Exact span bound for one target pair

Write the full grid of one oriented geodesic as

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
             \cup\{b_1,\ldots,b_j\}.                \tag{1.1}
\]

For two distinct cells \(S=G_{i,j}\) and \(T=G_{i',j'}\), put

\[
 a=|S\setminus T|,\qquad b=|T\setminus S|,
 \qquad t=a+b=|i-i'|+|j-j'|.                       \tag{1.2}
\]

Let \(d(S)\) be the number of raw candidates claiming \(S\), and let
\(d(S,T)\) be the number claiming both.  The exact stabilizer-orbit pair
formula gives, uniformly in the protected band,

\[
 {d(S,T)\over d(S)}
 \le
 m^{o(1)}{1+a+b\over
      \binom{|S|}{a}\binom{2m-|S|}{b}}.             \tag{1.3}
\]

All protected ranks are \(m+O(Q)\), and \(a,b\le2g=o(m)\).  With
\(n=m-g\), both \(|S|\) and \(2m-|S|\) are at least \(n\).  Moreover

\[
 \binom{|S|}{a}\binom{2m-|S|}{b}
 \ge \binom n a\binom n b
 \ge \binom n{a+b}.                                 \tag{1.4}
\]

The last inequality follows from

\[
 \binom n a\binom{n-a}b
   =\binom n{a+b}\binom{a+b}a
\]

and \(\binom n b\ge\binom{n-a}b\).  Hence

\[
 \boxed{
 {d(S,T)\over d(S)}
 \le m^{o(1)}{t+1\over\binom{m-g}{t}}.}             \tag{1.5}
\]

This is a joint two-target orbit probability.  No two marginal estimates
have been multiplied.

## 2. How many span-\(t\) pairs can one strip contain?

Let \(N_t(P)\) be the number of unordered pairs in \(C(P)\) having span
\(t\).  Once the first grid cell is chosen, the displacement of the second
is one of

\[
 (\pm r,\pm(t-r)),\qquad 0\le r\le t.
\]

There are at most \(4(t+1)\) signed displacements.  Dividing the ordered
count by two gives

\[
 \boxed{N_t(P)\le2K(t+1).}                          \tag{2.1}
\]

This deliberately counts cells outside the protected diagonals as well,
so it remains an upper bound for every priority-decorated strip.

The target calibration is \(d(S)\le A\).  If

\[
 R_2(P)=|\{E:\operatorname{tag}(E)\ne\operatorname{tag}(P),
                    |C(P)\cap C(E)|\ge2\}|
\]

is computed in the raw catalogue, the pair-star union bound, (1.5), and
(2.1) give

\[
\begin{aligned}
 {R_2(P)\over A}
 &\le \sum_{\{S,T\}\subset C(P)}{d(S,T)\over A}\\
 &\le \sum_{\{S,T\}\subset C(P)}{d(S,T)\over d(S)}\\
 &\le m^{o(1)}K
    \sum_{t=1}^{2g}{2(t+1)^2\over\binom{m-g}{t}}.   \tag{2.2}
\end{aligned}
\]

For \(u_t=(t+1)^2/\binom{m-g}{t}\),

\[
 {u_{t+1}\over u_t}
 ={(t+2)^2\over(t+1)(m-g-t)}
 =o(1)                                               \tag{2.3}
\]

uniformly for \(1\le t\le2g\), because \(g=o(m)\).  Thus the \(t=1\)
term dominates and

\[
 \boxed{{R_2(P)\over A}\le m^{o(1)}{K\over m}.}     \tag{2.4}
\]

This is the complete raw width-three-compatible span sum.  The argument
does not need to enumerate Ferrers shapes: choosing a common target pair
already dominates every shape of size at least two.

## 3. Passing the bound through isolated pruning

The small pair fibres require care.  It is false that every one of them
has large enough expectation for relative Chernoff concentration.

Let \(Y_{S,T}\) be the number of independently marked candidates claiming
both \(S,T\).  Then

\[
 Y_{S,T}\sim\operatorname{Bin}(d(S,T),p).
\]

There are only \(\exp(O(m))\) physical target pairs.  A standard binomial
upper-tail estimate therefore gives a constant \(C_0\), chosen larger
than the exponential counting constant, such that with probability
\(1-o(1)\), simultaneously for every pair,

\[
 \boxed{Y_{S,T}\le2p\,d(S,T)+C_0m.}                 \tag{3.1}
\]

Indeed, for means at least \(C_0m/4\) use the multiplicative Chernoff
bound, and for smaller means use
\(\Pr(Y\ge C_0m)\le(e\mathbb EY/(C_0m))^{C_0m}\); increasing \(C_0\)
makes the union bound summable.

Isolation only deletes marked candidates.  Hence the retained pair degree
\(d'(S,T)\) also obeys (3.1).  For a retained \(P\),

\[
\begin{aligned}
 B_2(P)
 &\le\sum_{\{S,T\}\subset C(P)}d'(S,T)\\
 &\le2p\sum_{\{S,T\}\subset C(P)}d(S,T)
       +C_0m\binom K2\\
 &\le m^{o(1)}D{K\over m}+O(mK^2),                 \tag{3.2}
\end{aligned}
\]

by (2.4) and \(D=pA\).  This proves (0.3).

The event (3.1) has probability \(1-o(1)\).  Intersecting it with the
weighted balanced-fibre experiment does not enlarge its exceptional
ledger asymptotically: if \(L_{\rm exc}\) denotes that nonnegative ledger,
then

\[
 \mathbb E[L_{\rm exc}\mid(3.1)]
 \le {\mathbb E L_{\rm exc}\over\Pr((3.1))}
 =(1+o(1))\mathbb E L_{\rm exc}.
\]

Thus an outcome satisfies both the usual \(o(W)\) ledger and (3.1).

On a good tag fibre, \(x_E=1/A'_U\le1/(cD)\).  Dividing (3.2) by \(cD\)
proves (0.4).

## 4. The exact weighted pair-star identity

For an unordered target pair \(q=\{S,T\}\), put

\[
 I_q(P)=\mathbf1_{\{q\subset C(P)\}},
 \qquad \lambda_q=\sum_Px_PI_q(P).                  \tag{4.1}
\]

Tonelli's identity gives

\[
\begin{aligned}
 \sum_{P,E}x_Px_E\binom{|C(P)\cap C(E)|}{2}
 &=\sum_{P,E}x_Px_E\sum_qI_q(P)I_q(E)\\
 &=\boxed{\sum_q\lambda_q^2}.                       \tag{4.2}
\end{aligned}
\]

Deleting same-tag ordered pairs on the left can only decrease it.  Thus
the average nonlinear overlap is exactly pair-star energy, not a product
of unproved marginals.

However, (4.2) is an average under the particular point \(x\).  The
matching dual permits arbitrary nonnegative test weights \(y_P\), which
may concentrate on a small structured subsystem.  Neither (0.4) nor
(4.2) controls that concentration.

For a no-common-target intersecting family \(\mathcal F\), let
\(\mathfrak C_x(\mathcal F)\) be the infimum, over the canonical choices
of \(A\in\mathcal F\) and \(B_s\in\mathcal F\) with \(s\notin B_s\), of

\[
 \mathfrak C_x(\mathcal F)
 =
 \inf_{A,(B_s)}
 \sum_{s\in A}\sum_{t\in B_s}
       x\bigl(\mathcal F(s,t)\bigr).                \tag{4.3}
\]

The canonical pair-star cover proves the exact one-sided inequality

\[
 x(\mathcal F)\le\mathfrak C_x(\mathcal F).         \tag{4.4}
\]

Consequently

\[
 \boxed{
 \sup_{\mathcal F}\mathfrak C_x(\mathcal F)
 \le1+o(1/Q)}                                      \tag{4.5}
\]

is a sufficient nonlinear clique-cut theorem.  The stronger bound
\(o(1/Q)\) would make the entire non-star clique sector exceptional.
Estimate (0.4) is only a row sum and implies neither version.

For comparison, the generic linear/nonlinear decomposition with maximum
nonlinear degree \(B\) gives

\[
 |\mathcal F|
 \le(B+1)\max\{K^2-K+1,K+B\}.                       \tag{4.6}
\]

To make its right side \(o(D)\), it is enough, and at these scales
essentially necessary for that argument, that

\[
 B=o(D/K^2)
 \quad\hbox{and}\quad
 B=o(\sqrt D).                                      \tag{4.7}
\]

Here \(D/K^2=m^{11/6-o(1)}\), whereas (0.3) is only \(Dm^{o(1)}\).
Thus \(D\gg K^2\) and width at most three do not close even the generic
clique reduction.  Moreover, Section 5.2 shows that setting the
cross-tag \(B\) all the way to zero still does not close the full matching
dual.

## 5. Can a line-system obstruction occur at \(D\)-scale?

There are two different questions.

### 5.1 Pure distinct-tag singleton systems: no

Let \(\mathcal L\) be a pairwise intersecting family of supports of rank at
most \(K\), assume every two distinct supports meet in exactly one target,
and assume the total intersection is empty.  Then

\[
 \boxed{|\mathcal L|\le K^2-K+1.}                   \tag{5.1}
\]

To see this, choose \(A,B\in\mathcal L\) with \(A\cap B=\{z\}\), and
choose \(F\in\mathcal L\) avoiding \(z\).  The members containing \(z\)
inject into their distinct intersection points with \(F\), so there are at
most \(K\) of them.  Every member avoiding \(z\) injects into
\((A\setminus\{z\})\times(B\setminus\{z\})\), so there are at most
\((K-1)^2\).  This proves (5.1), sharply for a projective plane.

Since \(K^2/D=m^{-11/6+o(1)}\), such an unblown line system is \(o(D)\).
It cannot cause a \(D\)-scale clique or a constant matching-dual loss.

### 5.2 Tag-fibre blow-ups: yes for the legal catalogue class

The literal construction in
MATH_ATTACK_A_ACTUAL_STRIP_SHANNON_MATCHING_OBSTRUCTION_20260725.md
gives three actual return-free tag bundles, each of size \(D/2\), whose
cross intersections are the three distinct cyclic owner targets.  With
fillers, all tag and target degrees are at most \(D\), while the union of
the three bundles has size \(3D/2\) and matching number one.  Every
cross-tag intersection is a singleton.  Consequently

\[
 B_{2,\mathrm{cross}}=0,
 \qquad \chi_f'\ge {3D\over2}.                      \tag{5.2}
\]

This proves that a first-order line-system obstruction can occur at
\(D\)-scale in the class of actual protected-strip multicovers, despite
perfect nonlinear overlap bounds.  It does **not** prove that a particular
fixed isolated-pruning outcome retains half of each of those three raw
fibres.  That fixed-point incidence statement remains open.  Likewise, a
growing projective plane is known to be an abstract width-one obstruction,
but no embedding as a large family of actual return-free strips is proved.

If same-tag pairs are included in \(B_2\), the Shannon construction has
\(B_2\ge D/2-1\), because the variants in one triangle bundle share their
two endpoint owners.  For the mixed-overlap census the relevant convention
is the cross-tag one in (0.2).

## 6. Exact residual inequality

The singleton Shannon subsystem shows that no improvement of the
cross-tag \(B_2\)-bound can by itself close coefficient one.  For every
physical cyclic triple of bundle subfamilies
\(\mathcal A_1,\mathcal A_2,\mathcal A_3\), the chosen pruning point must
satisfy

\[
 \boxed{
 x(\mathcal A_1)+x(\mathcal A_2)+x(\mathcal A_3)
 \le1+o(1/Q).}                                      \tag{6.1}
\]

Target capacities give only the three pairwise inequalities
\(x(\mathcal A_i)+x(\mathcal A_{i+1})\le1\), which admit the forbidden
vector \((1/2,1/2,1/2)\).

More generally the required conclusion is the weighted matching-cover
inequality

\[
 \sum_Px_Py_P
 \le(1+o(1/Q))
 \max_{M\ {\rm matching}}\sum_{P\in M}y_P
 \qquad(y_P\ge0).                                   \tag{6.2}
\]

The nonlinear pair-star gate (4.5) and the singleton odd-bundle gate
(6.1) are the two first irreducible cases.  The span calculation proves
the available \(B_2\)-estimate, but neither gate follows from it.

## 7. Final audit

1. The proof uses the exact joint pair formula (1.3), not a product of
   target marginals.
2. Tiny pair fibres are handled by the additive \(C_0m\) term in (3.1);
   no false relative concentration is asserted.
3. The additive pruning error is \(O(mK^2)=o(D)\) at the \(s=4\) scale.
4. The leading span-one contribution is \(DK/m\), so no strict \(o(D)\)
   follows from the stated asymptotics.
5. Width three controls larger Ferrers shapes but cannot improve a
   two-cell width-one chain.
6. The actual Shannon theorem is used only as a catalogue-class
   obstruction.  Retention of the required half-fibres by one fixed
   pruning point is not claimed.
