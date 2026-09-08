# Owner-fixed spike charts burn every upper collision at every positive depth

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, or solver is used.

## 0. Statement

Put \(n=2m+1\).  Consider one phase of a pair-omission token matching,
with omitted pair \(A\), and let \(F_A\) be its local exact row factor on
\([n]\setminus A\).  Fix \(1\le q\le H\le m-2\), and suppose \(t\)
selected tokens

\[
 e_i=(S_i,Y_i),\qquad 1\le i\le t,
\]

have distinct lower endpoints and distinct middle owners but the same
upper depth-\(q\) target

\[
 U_q(e_i)=U.
\tag{0.1}
\]

Extend the notation by \(U_0(e_i)=Y_i\), and let

\[
 b_i\in U_q(e_i)\setminus U_{q-1}(e_i)
\tag{0.2}
\]

be the unique coordinate entering the upper flag at depth \(q\).  Choose

\[
 z_i\in[n]\setminus\bigl(U_H(e_i)\cup A\bigr),
 \qquad B_i=\{b_i,z_i\}.
\tag{0.3}
\]

Such a helper exists because \(|U_H|=m+H\) and \(H\le m-2\).  Let
\(\theta_i\) exchange the two coordinates of \(A\) with those of
\(B_i\), in either fixed bijective order.

Replace \(e_i\), independently, either by its old row occurrence or by
the corresponding occurrence in the conjugate row \(\theta_iF_A\).
Every corner is a literal lower-saturating, middle-injective token matching;
indeed its complete lower--owner incidence set \(\{(S_i,Y_i)\}\) is
identical to the old one.  This does not assert that the other middle state
adjacent through \(S_i\) is fixed.

For arbitrary finite nonnegative signed-depth weights, let \(d_i\) be the
stacked flag innovation of the \(i\)-th switch and put

\[
 \mathfrak A=\left\|\sum_{i=1}^t d_i\right\|_w^2,
 \qquad
 \mathfrak V=\sum_{i=1}^t\|d_i\|_w^2.
\]

Then

\[
 \boxed{
 \mathfrak A-\mathfrak V
 \ge w_q^+t(t-1).
 }
\tag{0.4}
\]

Consequently fair independent spike bits lower the average of the two
coherent endpoint factorial-floor energies by at least

\[
 \boxed{\frac14w_q^+t(t-1).}
\tag{0.5}
\]

Equivalently, from the higher-energy coherent endpoint there is an integral
corner with that much energy descent.  Moving all \(t\) occurrences can add
at most \(2t\) physical source-row runs.

This theorem removes the owner-disjoint packing hypothesis from the earlier
overlapping-partner spike construction.  Its two remaining limitations are
explicit: the descent is relative to the higher coherent endpoint, and the
singleton source-row toll is linear in \(t\).

## 1. The central edge is fixed pointwise

The old row lies in \([n]\setminus A\), so every one of its flags avoids
\(A\).  By construction,

\[
 b_i\notin U_{q-1}(e_i)\supseteq Y_i,
 \qquad z_i\notin U_H(e_i)\supseteq Y_i.
\]

Thus the middle owner \(Y_i\) avoids \(B_i\).  The lower endpoint satisfies
\(S_i\subset Y_i\), and hence also avoids \(B_i\).  Therefore

\[
 \theta_iS_i=S_i,
 \qquad
 \theta_iY_i=Y_i.
\tag{1.1}
\]

The conjugate cyclic row is a row of the exact factor
\(\theta_iF_A\) on \([n]\setminus B_i\), and it supplies the same central
token edge

\[
 (\theta_iS_i,\theta_iY_i)=(S_i,Y_i).
\tag{1.2}
\]

Different occurrences are allowed to use different conjugate factor
copies, even when their omitted pairs coincide.  Source rows are labelled
physical word pieces; the construction never asserts that all auxiliary
rows form one common local factor.  This causes no ownership problem
because (1.2) leaves the selected central edge itself unchanged.  Treating
each auxiliary row as a separate labelled copy gives the conservative run
bound in Section 4.

Thus every independent choice changes only the flag realization attached
to an already selected central edge.  All lower ownership and middle
injectivity are preserved pointwise, with no deletion or owner reservation.
This remains true when different \(B_i\)'s overlap or coincide.

The same observation fixes every lower flag, because every lower flag is a
subset of \(S_i\).

## 2. Nonnegative cross-Gram at every depth

Let \(U_p^{(i)}\) be the old upper depth-\(p\) flag.  At that depth

\[
 (d_i)_p^+
 =\delta_{\theta_iU_p^{(i)}}-\delta_{U_p^{(i)}}.
\tag{2.1}
\]

For \(p<q\), the old upper flag contains neither \(b_i\) nor \(z_i\), so
\((d_i)_p^+=0\).  For \(p\ge q\), it contains \(b_i\) and omits \(z_i\),
so its image differs from it and meets \(A\).

Every old target avoids \(A\).  Hence, for \(i\ne k\), neither of the two
negative cross equalities is possible:

\[
 \theta_iU_p^{(i)}\ne U_p^{(k)},
 \qquad
 U_p^{(i)}\ne\theta_kU_p^{(k)}.
\tag{2.2}
\]

Expansion of the four unit-vector terms therefore gives

\[
 \left\langle(d_i)_p^+,(d_k)_p^+\right\rangle
 =
 \mathbf1_{\{U_p^{(i)}=U_p^{(k)}\}}
 +
 \mathbf1_{\{\theta_iU_p^{(i)}=\theta_kU_p^{(k)}\}}
 \ge0.
\tag{2.3}
\]

At the distinguished depth \(q\), all old targets equal \(U\).  Therefore

\[
 \left\langle(d_i)_q^+,(d_k)_q^+\right\rangle
 =1+\mathbf1_{\{\theta_iU=\theta_kU\}}
 \ge1.
\tag{2.4}
\]

All lower coordinates vanish and different ranks are orthogonal.  Summing
(2.3)--(2.4) with the prescribed weights yields

\[
\begin{aligned}
 \mathfrak A-\mathfrak V
 &=2\sum_{1\le i<k\le t}\langle d_i,d_k\rangle_w\\
 &\ge2w_q^+\binom t2
 =w_q^+t(t-1),
\end{aligned}
\]

which proves (0.4).

## 3. Exact floor Haar identity

Let \(f^0\) and \(f^1=f^0+\sum_i d_i\) be the two coherent endpoint flag
profiles.  A fair independent corner has profile

\[
 f^\varepsilon
 =\frac{f^0+f^1}{2}
 +\frac12\sum_i\varepsilon_i d_i,
 \qquad \varepsilon_i\in\{-1,+1\}.
\tag{3.1}
\]

Therefore

\[
 \mathbb E\|f^\varepsilon\|_w^2
 =\left\|\frac{f^0+f^1}{2}\right\|_w^2
  +\frac14\mathfrak V,
\tag{3.2}
\]

whereas

\[
 \frac{\|f^0\|_w^2+\|f^1\|_w^2}{2}
 =\left\|\frac{f^0+f^1}{2}\right\|_w^2
  +\frac14\mathfrak A.
\tag{3.3}
\]

Every corner has the same total flag mass at every signed depth.  Hence
the linear and integer-floor baseline terms are corner-independent, and
(3.2)--(3.3) are exact for the doubled factorial-floor energy.  Their
difference is \((\mathfrak A-\mathfrak V)/4\), proving (0.5).

If \(E_{\rm hi}=\max\{E(f^0),E(f^1)\}\), then the average corner energy is
at most

\[
 E_{\rm hi}-\frac14w_q^+t(t-1).
\]

Some integral corner obeys the same bound.

## 4. Physical run ledger and the exact frontier

Changing one token can split its old selected source-row run into at most
one additional run and can create at most one new run in its conjugate row.
Thus every corner has

\[
J(M_\varepsilon)\le J(M_0)+2t.
\tag{4.1}
\]

Combining (0.4) with (4.1), the certified coherent curvature per possible
new run is at least

\[
 \boxed{\frac{w_q^+}{2}(t-1).}
\tag{4.2}
\]

Thus targets of multiplicity \(t/H\to\infty\) are quantitatively cheap at
the literal scale: their available curvature is super-\(H\) per source-row
boundary.  The hard sector is consequently the diffuse bounded- or
\(O(H)\)-multiplicity collision mass, precisely the sector for which the
long interval charts are designed.

The construction works already at \(q=1\): the entering coordinate
\(b_i\) is paired with a helper outside \(U_H(e_i)\).  This does not
contradict the depth-one flatness of the tight adjacent-pair interval chart.
That flatness concerns one common partner pair on a first-avoided carrier;
the present spike chart uses an occurrence-specific pair \(B_i\) and pays
the conservative linear source-row toll.

For constant one, (0.4) supplies the missing full collision mode on an
individual upper spike without any owner-packing loss, including at the
first upper shadow.  What is still
needed is a global selection theorem combining:

1. long interval charts for the numerous low-multiplicity collisions;
2. owner-fixed spikes for concentrated residual collisions;
3. a symmetric or charged endpoint rule controlling the coherent endpoint
   imbalance; and
4. a total added-run bound \(o(W/H)\).

No coefficient-one conclusion is claimed here.

## 5. Exact lower-dual owner-fixed spike

The upper construction has a literal dual on the same central token
matching; it does not require complementation or a second word.

Fix \(q\ge2\), and suppose \(t\) selected tokens have the same lower
depth-\(q\) target

\[
 L_q(e_i)=L.
\tag{5.1}
\]

Along the old lower flag of occurrence \(i\), let

\[
 b_i\in L_{q-1}(e_i)\setminus L_q(e_i)
\tag{5.2}
\]

be the unique coordinate deleted on entry to \(L\), and choose any
\(a_i\in L\).  Put

\[
 \sigma_i=(a_i\ b_i).
\tag{5.3}
\]

Both coordinates lie in \(S_i\), so \(\sigma_i\) fixes \(S_i\) and
\(Y_i\supset S_i\) setwise.  It also fixes the omitted phase pair, which
is disjoint from the entire source row.  Hence \(\sigma_iF_A\) is another
exact factor on the same omitted-pair universe and supplies the same
central edge \((S_i,Y_i)\).  Every upper flag contains \(S_i\), so every
upper flag is fixed setwise as well.

For \(p<q\), the old lower flag contains both \(a_i\) and \(b_i\), and is
therefore fixed.  At depth \(q\),

\[
 \sigma_iL=(L\setminus\{a_i\})\cup\{b_i\}\ne L.
\tag{5.4}
\]

For \(p>q\), the old lower flag is a subset of \(L\).  Its innovation is
zero if it omits \(a_i\), and otherwise its image contains
\(b_i\notin L\).  Consequently, for two distinct occurrences, a nonzero
image at depth \(p\ge q\) can never equal any old target at that depth,
because every old target is contained in the common set \(L\).  Thus all
cross-Gram products are nonnegative, and at depth \(q\) they are at least
one:

\[
 \left\langle
  \delta_{\sigma_iL}-\delta_L,
  \delta_{\sigma_kL}-\delta_L
 \right\rangle
 =1+\mathbf1_{\{\sigma_iL=\sigma_kL\}}
 \ge1.
\tag{5.5}
\]

If \(d_i^-\) denotes the complete signed flag innovation, then exactly as
in Sections 2--3,

\[
 \boxed{
 \left\|\sum_i d_i^-\right\|_w^2
 -\sum_i\|d_i^-\|_w^2
 \ge w_q^-t(t-1),}
\tag{5.6}
\]

and fair independent choices lower the average coherent endpoint
factorial-floor energy by at least

\[
 \boxed{\frac14w_q^-t(t-1).}
\tag{5.7}
\]

All central edges and all upper flags remain fixed.  The same conservative
source-row accounting adds at most \(2t\) runs.

Therefore both signed collision sectors at every depth \(q\ge2\) admit
owner-fixed positive spike charts on one common central matching.  The
remaining global problem is no longer existence of a lower dual; it is the
endpoint-asymmetry and aggregate run-budget problem stated in Section 4.
