# Adjacent-priority interval atlas: exact floor descent below both coherent endpoints

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or
long-running job is used.

## 0. Outcome

This note combines two exact facts:

1. pair-symmetric adjacent-priority coherent endpoints have equal
   factorial floor energy, separately at every signed rank;
2. maximal physical-run packetization has joined Gram gap
   \[
   \mathfrak A-\mathfrak V
   =4\sum_{q=1}^Hw_q^+
      \sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.
   \]

Let \(Q_0\) be the common doubled factorial floor energy of the two
coherent endpoints. A fair independent choice on the maximal run packets
satisfies exactly

\[
\boxed{
 \mathbb E Q_{\rm tok}(M_\varepsilon)
 =Q_0-
   \sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.}
\tag{0.1}
\]

Consequently a deterministic integral interval corner obeys the same
upper bound. If the displayed collision sum is positive, that corner lies
strictly below both coherent endpoints.

Equation (0.1) includes the complete unchanged token background. It also
remains exact at the first upper rank, where the autonomous token mass has
floor quotient \(c_1^+=0\): factorial floor excess is still well defined,
and no division by \(c_1^+\) occurs.

The completion caveat is exact. Adding one fixed but arbitrary completion
preserves the gain below the average completed endpoint energy, but can
destroy equality of the two completed endpoints through a linear cross
term. Descent below both completed endpoints follows if the fixed
completion is invariant under the pair exchange, or more generally
orthogonal to the coherent innovation. Construction of a physical
low-cost completion with that invariance is not proved here.

## 1. Token factorial floors, including \(c_1^+=0\)

Put

\[
 n=2m+1,\qquad
 T=\binom n{m-1}.
\tag{1.1}
\]

Every lower-saturating token matching has exactly \(T\) flags at every
signed depth. At upper depth \(q\), let

\[
 K_q^+=\binom n{m+q},\qquad
 T=c_q^+K_q^++\delta_q^+,\qquad
 0\le\delta_q^+<K_q^+.
\tag{1.2}
\]

For an integral load vector \(x\in\mathbb Z_{\ge0}^{K_q^+}\) of mass \(T\),
write

\[
 P_q(x)=\sum_U\binom{x_U}{2}
\tag{1.3}
\]

and

\[
 P_q^{\min}
 =(K_q^+-\delta_q^+)\binom{c_q^+}{2}
  +\delta_q^+\binom{c_q^++1}{2}.
\tag{1.4}
\]

The doubled factorial floor excess is

\[
 Q_q(x)=2\bigl(P_q(x)-P_q^{\min}\bigr).
\tag{1.5}
\]

It is nonnegative and well defined for every \(c_q^+\ge0\).

At \(q=1\),

\[
 K_1^+=\binom n{m+1}=\binom nm=W,
\qquad
 T=\frac{m}{m+2}W<W.
\tag{1.6}
\]

Therefore

\[
 c_1^+=0,\qquad \delta_1^+=T,\qquad
 P_1^{\min}=0,\qquad Q_1(x)=2P_1(x).
\tag{1.7}
\]

Thus the first upper token floor is collision energy itself. The singular
expression \(1/c_1^+\) must not be used. We instead fix arbitrary
nonnegative rank weights \(w_q^+\) and put

\[
 Q_{\rm tok}^+(M)=\sum_{q=1}^Hw_q^+Q_q(\mu_q^M).
\tag{1.8}
\]

Lower factorial floor energies may be added with arbitrary nonnegative
weights. They are constant throughout the interval atlas below and hence
play no role in the drift.

## 2. Pair-symmetric coherent endpoints

Fix adjacent priority pairs

\[
 A=P_j,\qquad B=P_{j+1},
\]

and let \(\vartheta\) exchange \(A\) and \(B\) coordinatewise. Choose

\[
 F_B=\vartheta F_A.
\tag{2.1}
\]

Let \(M^-\) and \(M^+\) be the first-avoided token matchings for the orders
with \(A,B\) and \(B,A\), respectively. They differ exactly on

\[
 \mathcal D_j
 =\{S:S\cap(A\cup B)=\varnothing,\ 
          S\cap P_h\ne\varnothing\ (h<j)\}.
\tag{2.2}
\]

The exact stratum-permutation theorem in
PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md gives, for every
upper depth \(q\),

\[
 P_q(\mu_q^{M^-})=P_q(\mu_q^{M^+}).
\tag{2.3}
\]

Both endpoints have the same mass, so their floor minima (1.4) are equal.
Hence

\[
 Q_q(M^-)=Q_q(M^+)
\tag{2.4}
\]

rank by rank. Every lower flag is unchanged because it is a subset of a
lower endpoint fixed by \(\vartheta\). Therefore, after including all
signed token floors,

\[
 \boxed{Q_{\rm tok}(M^-)=Q_{\rm tok}(M^+)=:Q_0.}
\tag{2.5}
\]

This equality already includes every token outside \(\mathcal D_j\).
Those tokens are the unchanged background; no orthogonality assumption on
their load vector is being made.

## 3. The interval Haar identity with background

Break \(\mathcal D_j\) into maximal consecutive intervals \(I\) in the
rows of \(F_A\), paired with the corresponding intervals in
\(\vartheta F_A=F_B\). Let

\[
 z_{I,q}=\mu_{I,q}^{B}-\mu_{I,q}^{A}
\tag{3.1}
\]

be the upper depth-\(q\) innovation of interval \(I\). Put

\[
 A_q=\left\|\sum_Iz_{I,q}\right\|_2^2,
\qquad
 V_q=\sum_I\|z_{I,q}\|_2^2.
\tag{3.2}
\]

Let \(b_q\) denote the complete load from tokens outside
\(\mathcal D_j\). If \(a_{I,q}\) is the phase-\(A\) load of interval \(I\),
then a corner indexed by independent fair
\(\epsilon_I\in\{0,1\}\) has

\[
 x_{\epsilon,q}
 =b_q+\sum_Ia_{I,q}+\sum_I\epsilon_Iz_{I,q}.
\tag{3.3}
\]

Its midpoint is

\[
 \bar x_q
 =b_q+\sum_Ia_{I,q}+\frac12\sum_Iz_{I,q}.
\tag{3.4}
\]

Independence gives

\[
 \mathbb E\|x_{\epsilon,q}\|_2^2
 =\|\bar x_q\|_2^2+\frac14V_q,
\tag{3.5}
\]

whereas polarization gives

\[
 \frac{\|\mu_q^{M^-}\|_2^2+\|\mu_q^{M^+}\|_2^2}{2}
 =\|\bar x_q\|_2^2+\frac14A_q.
\tag{3.6}
\]

The background \(b_q\) appears identically in (3.5) and (3.6), so it
cancels from their difference:

\[
 \mathbb E\|x_{\epsilon,q}\|_2^2
 -\frac{\|\mu_q^{M^-}\|_2^2+\|\mu_q^{M^+}\|_2^2}{2}
 =-\frac14(A_q-V_q).
\tag{3.7}
\]

Every corner has mass \(T\). The linear term in
\(2P_q(x)=\|x\|_2^2-T\) and the floor minimum \(2P_q^{\min}\) are therefore
corner-independent. Thus (3.7) is also the exact doubled factorial-floor
identity

\[
 \mathbb E Q_q(x_{\epsilon,q})
 -\frac{Q_q(M^-)+Q_q(M^+)}2
 =-\frac14(A_q-V_q).
\tag{3.8}
\]

This proof uses neither \(c_q^+>0\) nor division by \(c_q^+\), so it
includes (1.7).

## 4. Substitution of the exact joined Gram

For \(S\in\mathcal D_j\), let \(U_q(S)\) be its phase-\(A\) upper flag and
put

\[
 \mu_{q,U}
 =|\{S\in\mathcal D_j:U_q(S)=U\}|.
\tag{4.1}
\]

The exact pair-swap Gram formula is

\[
 \langle d_{S,q},d_{T,q}\rangle
 =2\,{\bf1}_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}.
\tag{4.2}
\]

Different starts in one physical row have distinct proper upper windows
for \(q\le H\le m-2\). Hence duplicate occurrences always lie in
different interval packets. Expanding (3.2) therefore gives

\[
 \begin{aligned}
 A_q-V_q
 &=2\sum_{I<J}\langle z_{I,q},z_{J,q}\rangle\\
 &=4\sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.
 \end{aligned}
\tag{4.3}
\]

Multiply (3.8) by \(w_q^+\), sum over \(q\), and use (2.5) and (4.3).
This proves (0.1).

In particular there is an integral corner \(M_{\rm dec}\) with

\[
 \boxed{
 Q_{\rm tok}(M_{\rm dec})
 \le Q_0-
   \sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.}
\tag{4.4}
\]

When the collision sum is nonzero, (4.4) is strict and both coherent
endpoints have energy \(Q_0\). The decreasing corner is therefore neither
coherent endpoint.

## 5. Exact completion caveat

Let \(r_q\) be a fixed completion load added to every token corner, and
write

\[
 z_q=\mu_q^{M^+}-\mu_q^{M^-}=\sum_Iz_{I,q}.
\tag{5.1}
\]

The independent-corner identity relative to the average of the two
completed coherent endpoints is unchanged:

\[
 \mathbb E Q_{\rm full}(x_\epsilon+r)
 =\frac{Q_{\rm full}(M^-+r)+Q_{\rm full}(M^++r)}2
  -\sum_qw_q^+
    \sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.
\tag{5.2}
\]

Indeed \(r_q\) is part of the common background in (3.3)--(3.7).

However, even though the token endpoints have equal energy, the completed
endpoint difference contains the cross term

\[
 \boxed{
 Q_{\rm full}(M^++r)-Q_{\rm full}(M^-+r)
 =2\sum_qw_q^+\langle r_q,z_q\rangle.}
\tag{5.3}
\]

Here all corner-independent floor and mass terms cancel. Thus (5.2) alone
only gives descent below the average completed endpoint energy.

A sufficient condition for descent below both completed endpoints is

\[
 \sum_qw_q^+\langle r_q,z_q\rangle=0.
\tag{5.4}
\]

In particular (5.4) holds if every \(r_q\) is
\(\vartheta\)-invariant. The coherent innovation \(z_q\) is
\(\vartheta\)-anti-invariant, so the two vectors are orthogonal.
Under (5.4), the completed coherent endpoints are equal-energy and (4.4)
holds verbatim for their full energy, with \(Q_0\) replaced by their common
completed energy and with the appropriate positive full-word weights.

For an arbitrary fixed completion, a corner is still guaranteed below
both completed endpoints only when the token gain \(D\) satisfies

\[
 D\ge
 \left|\sum_qw_q^+\langle r_q,z_q\rangle\right|,
\qquad
 D=\sum_qw_q^+
    \sum_{U:U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.
\tag{5.5}
\]

Construction of a literal completion which simultaneously:

1. supplies the omitted \(W-T\) owners and flags,
2. preserves the \(o(W/H)\) run-boundary budget, and
3. satisfies (5.4) at every required adjacent chart,

is not proved. That is the precise completion boundary. No constant-one
conclusion is claimed.
