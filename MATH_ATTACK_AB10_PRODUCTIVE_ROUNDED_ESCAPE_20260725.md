# Lane AB10: productive menu escape, exact orbit-profile rounding, and the first-shadow obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, computer
experiment, or long-running local job is used. Every factor below is an
integral exact middle wreath factor, and every switch is a complete ownership
component switch. No signed surrogate and no fractional factor is used.

Status: theorem-level report. The positive construction is genuine: it gives a
balanced rounded exact factor using only bridge labels outside the protected
AB8/K9 menu, with a quantitatively large decrease of the weighted factorial
energy. The same construction also has a sharp negative conclusion: every one
of its rounded endpoints retains \((1/16-o(1))W\) depth-one overload. Thus it
is not a coefficient-one escape. A new orbit-profile theorem removes the old
floor-compatible-profile hypothesis from the joint-TU signing lemma and
isolates the exact remaining nonlocal correlation gate for this one-overlay
route.

The exact packet geometry and balanced-block identity used in Sections 3--4
are the audited results of
`MATH_ATTACK_AB6_DISTINCT_BRIDGE_SCHEDULE_20260725.md`. The canonical
first-shadow input in Section 4 is the independently completed theorem in
`MATH_ATTACK_I_MARKED_GAP_COLLISION_INDEPENDENT_AUDIT_20260725.md`. Their
needed statements and constants are restated below; no conjectural input from
either report is used.

---

## 0. Verdict

Fix \(A>0\), and put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn=\operatorname{Cat}_m,\qquad
 H=\lceil A\sqrt m\rceil .                         \tag{0.1}
\]

At depth \(q\le H\), put

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\quad 0\le\rho_q<N_q,             \tag{0.2}
\]

and let \(O_q(F)\) be half the minimum \(\ell^1\)-distance of the
depth-\(q\) load of \(F\) from an integral quota having \(\rho_q\) entries
\(c_q+1\) and all other entries \(c_q\). Define

\[
 J_A(F)=\sum_{q=1}^H\frac{O_q(F)}{c_q},\qquad
 S_A(m)=\sum_{q=1}^H\frac1{c_q}.                   \tag{0.3}
\]

The following statements are proved.

1. Let \(\mathcal M\) be either the original AB8 protected menu or the
   sharpened K9 protected menu, with its usual parameter
   \(a=\lfloor H/2\rfloor\). For all sufficiently large \(m\), the
   complement of \(\mathcal M\) contains a coordinate matching of size
   \(m\). A single coordinate conjugation sends every one of the

   \[
   L=m-H-3                                                   \tag{0.4}
   \]

   native AB6 packet bridges to distinct edges of this complement.

2. There are exact factors \(F^\sharp\) and \(F^{\rm rd}\) in the conjugated
   MSW packet cube such that every macro-bridge between them lies outside
   \(\mathcal M\), the macro-bridges form a coordinate matching, and every
   packet block of \(F^{\rm rd}\) is balanced to within one component. With

   \[
   K=\sum_{u=H}^{m-4}\operatorname{Cat}_u,\qquad
   L_A=e^{2(A+1)(A+2)},                              \tag{0.5}
   \]

   their weighted quadratic/factorial energy satisfies

   \[
   \boxed{
   \mathcal Q_H(F^\sharp)-\mathcal Q_H(F^{\rm rd})
   >
   K\left[
     \frac{4^H}{32L_AH^4}-(2H-1)
   \right].}
                                                               \tag{0.6}
   \]

   In particular,

   \[
   \frac{\mathcal Q_H(F^\sharp)-\mathcal Q_H(F^{\rm rd})}{W}
   \longrightarrow\infty .                                  \tag{0.7}
   \]

3. If \(r\) is the number of packet signs changed between the coherent and
   rounded endpoints, then

   \[
   \left|r-\frac K2\right|\le\frac L2                  \tag{0.8}
   \]

   and

   \[
   \boxed{
   |J_A(F^{\rm rd})-J_A(F^\sharp)|
   \le r(4S_A-2)
   =\left(\frac{\kappa_A}{192}+o_A(1)\right)
     \frac W{\sqrt m},}
                                                               \tag{0.9}
   \]

   where

   \[
   \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.       \tag{0.10}
   \]

   Thus the enormous quadratic-energy drop moves the shallow overload by
   only \(o(W)\).

4. Every endpoint of this packet cube, including \(F^{\rm rd}\), obeys

   \[
   \boxed{
   J_A(F^{\rm rd})\ge O_1(F^{\rm rd})
   \ge
   (2m-3)\operatorname{Cat}_{m-2}
   -\frac{2W}{m+2}-2K
   =\left(\frac1{16}-o(1)\right)W.}
                                                               \tag{0.11}
   \]

   Therefore label escape, exact factorhood, distinct bridges, balanced
   rounding, and even an arbitrarily large factorial-energy decrease do not
   supply coefficient one.

5. For an arbitrary transposition overlay, an exact orbit-profile floor
   \(\Delta_q^\sigma\) is defined below. One common all-depth component
   signing satisfies

   \[
   O_q\le \Delta_q^\sigma
   +\frac12\sum_p(|D_p|-\pi_p).                       \tag{0.12}
   \]

   Joint total unimodularity makes the second term vanish on every retained
   row. Hence full joint TU realizes the exact orbit-profile floor at every
   depth, with no floor-compatible pair-total hypothesis. This strengthens
   K8's conditional signing theorem but does not prove TU or a small profile
   floor for K's fresh overlay.

6. Every endpoint of the Section 3 packet cube has

   \[
   M_1\ge(1/16-o(1))W                                  \tag{0.13}
   \]

   first-shadow holes. Any one-round escaped overlay that reaches
   \(J_A=o(W)\) must productively split at least

   \[
   (1/16-o(1))W                                        \tag{0.14}
   \]

   target-disjoint hole/duplicate pairs among multiple genuine ownership
   components. Under unit leakage, the exact profile theorem requires
   \((1/8-o(1))W\) nonzero first-shadow row/column incidences. K's currently
   certified direct alignment gives only \(O(B)=o(W)\). Independent fair
   component signs leave \((1/32-o(1))W\) expected holes even in the ideal
   unit-split case.

The positive result is therefore a productive *collision-energy* escape and
an exact rounded factor, but not a productive shallow-overload escape. For this
one-overlay packet route, the missing coefficient-one input is an
\(\Omega(W)\)-scale nonlocal component-correlation theorem, not another
label-count or seam-count statement.

Here “menu escape” means that every bridge label of the constructed packet
path lies outside the protected menu. The starting state is a conjugated MSW
packet-cube endpoint, not the AB8/K9 invariant-fibre minimizer. No adaptive
transition from that caged minimizer to this family is asserted.

---

## 1. Exact normalizations

For an exact factor \(F\), let \(\mu_q^F(S)\) be the number of cyclic
rank-\((m-q)\) occurrences of target \(S\). Every exact factor has

\[
 \sum_S\mu_q^F(S)=W.                                  \tag{1.1}
\]

Let \(\mathcal B_q\) be the set of all vectors \(b\) with exactly
\(\rho_q\) entries \(c_q+1\) and every other entry \(c_q\). Then

\[
 O_q(F)=\frac12\min_{b\in\mathcal B_q}
          \|\mu_q^F-b\|_1.                            \tag{1.2}
\]

The weighted quadratic energy used by AB6 is

\[
 \mathcal Q_H(F)
 =\sum_{q=1}^H\frac1{c_q}
   \sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).           \tag{1.3}
\]

If \(\Phi_q\) is factorial collision excess above the exact
adjacent-integer floor, then direct expansion using (0.2) gives

\[
 \sum_S(\mu_q-c_q)(\mu_q-c_q-1)=2\Phi_q.              \tag{1.4}
\]

Thus a decrease of \(\mathcal Q_H\) is a genuine decrease of a weighted
factorial collision objective. It is not, by itself, a decrease of \(J_A\).

For fixed \(A\), the standard local limit estimate gives

\[
 S_A(m)=(\kappa_A+o_A(1))\sqrt m,                     \tag{1.5}
\]

with \(\kappa_A\) as in (0.10). No asymptotic estimate is used in an
integrality argument below.

At depth one,

\[
 N_1=\binom n{m-1}=\frac m{m+2}W,\qquad
 c_1=1,\qquad
 \rho_1=\frac{2W}{m+2}.                               \tag{1.6}
\]

### Lemma 1.1 (holes are literal overload)

For every exact factor,

\[
 \boxed{O_1(F)\ge M_1(F),\qquad J_A(F)\ge M_1(F),}    \tag{1.7}
\]

where \(M_1(F)=|\{S:\mu_1^F(S)=0\}|\).

#### Proof

Every depth-one quota entry is one or two. Hence every hole contributes at
least one to

\[
 \sum_S(b(S)-\mu_1^F(S))_+.
\]

The quota and load have the same total mass, so this positive deficit equals
half their \(\ell^1\)-distance. Minimize over quotas. Since \(c_1=1\), the
depth-one summand of \(J_A\) is \(O_1\). \(\square\)

---

## 2. A matching outside every protected menu used here

Regard a transposition menu as a simple graph on the \(n\) coordinate
labels.

### Lemma 2.1 (complement matching)

Let \(G\) be any graph on \(2m+1\) vertices whose connected components all
have size at most \(m\). Then the complement of \(G\) contains a matching of
size \(m\).

#### Proof

All edges between distinct connected components of \(G\) lie in its
complement. It therefore suffices to find a near-perfect matching in the
complete multipartite graph whose parts are the components of \(G\).

Induct on \(m\). Choose one vertex from each of two largest nonempty parts and
match them. After deleting these vertices, there are \(2m-1\) vertices. Every
part has size at most \(m-1\): the two selected largest parts were reduced, and
an untouched part of size \(m\) would force three original parts of size at
least \(m\), whose total \(3m\) exceeds \(2m+1\) for \(m\ge2\). The induction
hypothesis supplies \(m-1\) further edges. The base case \(m=1\) is immediate.
\(\square\)

For the original AB8 menu with parameter \(a\), the nontrivial coordinate
components have sizes

\[
 a+1,\qquad a+2H+2,\qquad 2.                          \tag{2.1}
\]

For the sharpened K9 menu they have sizes

\[
 a+2,\qquad a+2H+3,\qquad 2,2,\ldots,2.               \tag{2.2}
\]

Taking \(a=\lfloor H/2\rfloor\), every size in (2.1)--(2.2) is
\(O_A(\sqrt m)<m\) for sufficiently large \(m\). Lemma 2.1 therefore applies
to both menus.

The native AB6 bridges are

\[
 \tau_s=(2s+2\ \ 2s+3),
 \qquad 2\le s\le m-H-2.                              \tag{2.3}
\]

They form a matching of size \(L=m-H-3\le m\). Choose \(L\) edges from the
complement matching in Lemma 2.1. Since two matchings of the same size are
isomorphic as labelled graphs, there is a coordinate permutation \(g\) such
that

\[
 \rho_s:=g\tau_sg^{-1}\notin\mathcal M
 \quad(2\le s\le m-H-2).                              \tag{2.4}
\]

Coordinate conjugation preserves exactness, every load norm, every quota
distance, and ownership-component structure. Thus all native AB6 packet
statements transfer verbatim to the labels \(\rho_s\).

This proves simultaneous label-theoretic avoidance of the full protected
menu, not merely avoidance of one prescribed bridge. It does not connect the
protected cage minimizer to this packet cube.

---

## 3. The exact packet cube and its rounded endpoint

Write \(C_t=\operatorname{Cat}_t\). For each index in (2.3), put

\[
 M_s=m-s-2,\qquad k_s=C_{M_s}.                        \tag{3.1}
\]

The audited MSW packet theorem supplies \(k_s\) pairwise owner-disjoint
genuine size-two components for \(\tau_s\). Components belonging to distinct
indices \(s\) also have disjoint owner and middle-root supports. Every choice
of their sides is therefore an integral exact factor. Moreover, a packet
currently on its translated side remains a complete component when its own
overlay is freshly recomputed.

Conjugate this whole cube by \(g\). All these conclusions remain true, and
every macro-label is outside \(\mathcal M\).

For a packet component \((s,i)\), orient its two load contributions and write

\[
 d_{s,i}=a_{s,i}-\rho_sa_{s,i},\qquad
 D_s=\sum_{i=1}^{k_s}d_{s,i},                         \tag{3.2}
\]

\[
 V_s=\sum_{i=1}^{k_s}\|d_{s,i}\|_H^2,\qquad
 \Lambda_s=\|D_s\|_H^2-V_s,                          \tag{3.3}
\]

where

\[
 \|x\|_H^2=\sum_{q=1}^H\frac{\|x_q\|_2^2}{c_q}.     \tag{3.4}
\]

The previously audited shifted-pile lemma gives, since \(M_s\ge H\),

\[
 \|D_s\|_H^2
 \ge \frac{2C_{M_s-H}C_H^2}{c_H}.                    \tag{3.5}
\]

The exact one-packet squared norms are four at depth one and eight at every
depth \(2,\ldots,H\). Therefore

\[
 V_s=k_s\left(4+8\sum_{q=2}^H\frac1{c_q}\right)
 \le(8H-4)k_s.                                       \tag{3.6}
\]

For sufficiently large \(m\),

\[
 c_H\le L_A,\qquad
 C_H\ge\frac{4^H}{4H^2},\qquad
 C_{M_s-H}>\frac{k_s}{4^H}.                           \tag{3.7}
\]

Substitution in (3.5) gives

\[
 \|D_s\|_H^2>\frac{4^H}{8L_AH^4}k_s                 \tag{3.8}
\]

and hence

\[
 \boxed{
 \frac{\Lambda_s}{4}
 >k_s\left[
   \frac{4^H}{32L_AH^4}-(2H-1)
 \right].}                                           \tag{3.9}
\]

### Lemma 3.1 (coherent-to-balanced exact rounding)

There is a coherent cube endpoint \(F^\sharp\) and a balanced endpoint
\(F^{\rm rd}\) such that

\[
 \mathcal Q_H(F^\sharp)-\mathcal Q_H(F^{\rm rd})
 \ge\frac14\sum_s\left(1+\frac1{\kappa_s}\right)
       \Lambda_s,                                    \tag{3.10}
\]

where \(\kappa_s=k_s-1\) for even \(k_s\) and \(\kappa_s=k_s\) for odd
\(k_s\). In block \(s\), the rounded endpoint differs from the coherent one
in either \(\lfloor k_s/2\rfloor\) or
\(\lceil k_s/2\rceil\) packet signs.

#### Proof

Every cube load has the affine form

\[
 \mu(F_\varepsilon)
 =\bar\mu+\frac12\sum_{s,i}\varepsilon_{s,i}d_{s,i}. \tag{3.11}
\]

Choose one coherent sign for each block, proceeding backward through the
blocks, so that its inner product with the already chosen later residual is
nonnegative. In block \(s\), sample a balanced sign vector. For even \(k_s\)
use equally many signs of each kind. For odd \(k_s\), append one zero dummy
column and balance the \(k_s+1\) signs. If

\[
 X_s=\sum_i\varepsilon_{s,i}d_{s,i},
\]

then

\[
 \mathbb EX_s=0,\qquad
 \mathbb E\|X_s\|_H^2
 =V_s-\frac{\Lambda_s}{\kappa_s}.                    \tag{3.12}
\]

Expanding the quadratic energy in (3.11), the backward coherent choice makes
the remaining linear term nonnegative, so the expected block gain is at least

\[
 \frac14\left(1+\frac1{\kappa_s}\right)\Lambda_s.    \tag{3.13}
\]

Sum over blocks. The balanced product law has finite support, so one
deterministic outcome has at least its mean total gain. All its coordinates
are whole component choices, hence the outcome and every sequential
microstep realizing it are integral exact factors. \(\square\)

Combining (3.9)--(3.10) proves (0.6).

### Lemma 3.2 (packet count)

The total packet count satisfies

\[
 K=\sum_{u=H}^{m-4}C_u> C_{m-4}>\frac B{256},         \tag{3.14}
\]

\[
 K\le\frac B2,                                       \tag{3.15}
\]

and

\[
 \boxed{\frac KB\longrightarrow\frac1{192}.}        \tag{3.16}
\]

#### Proof

The first inequality uses \(C_m<4^4C_{m-4}\). The packet families are
pairwise owner-disjoint and every packet contains two owner rows, proving
\(2K\le B\).

For (3.16), write \(u=m-j\). For every fixed \(j\),

\[
 \frac{C_{m-j}}{C_m}\longrightarrow4^{-j}.           \tag{3.17}
\]

For \(r\ge2\),

\[
 \frac{C_{r-1}}{C_r}=\frac{r+1}{4r-2}\le\frac12.      \tag{3.18}
\]

Hence \(C_{m-j}/C_m\le2^{-j}\) throughout the present sum for all large
\(m\). This is a summable geometric majorant, while the omitted lower tail
has \(m-H\to\infty\). Dominated convergence gives

\[
 \lim\frac KB=\sum_{j=4}^{\infty}4^{-j}=\frac1{192}.
\]

\(\square\)

Equations (3.14) and (0.6) give

\[
 \frac{\mathcal Q_H(F^\sharp)-\mathcal Q_H(F^{\rm rd})}{W}
 >\frac1{256n}
 \left[
   \frac{4^H}{32L_AH^4}-(2H-1)
 \right],                                            \tag{3.19}
\]

whose right side tends to infinity. This proves (0.7).

---

## 4. Exact shallow-overload cost of the rounded family

### Lemma 4.1 (one packet action)

One contextual packet toggle has exact half-\(\ell^1\) load action

\[
 a_1=2,\qquad a_q=4\quad(2\le q\le H).               \tag{4.1}
\]

Consequently, if two packet-cube vertices differ in \(r\) signs, then

\[
 \boxed{
 |J_A(F')-J_A(F)|\le r(4S_A-2).}                     \tag{4.2}
\]

#### Proof

The four-arm cancellation leaves four signed unit cells at depth one and
eight at every deeper depth, giving (4.1). Distance to a fixed set is
one-Lipschitz, so the quota distance \(O_q\) changes by at most the
half-\(\ell^1\) action. Sum

\[
 \frac2{c_1}+4\sum_{q=2}^H\frac1{c_q}=4S_A-2,
\]

using \(c_1=1\). Telescope over the \(r\) toggles. \(\square\)

Let \(r_s\) be the number of signs changed in block \(s\) between
\(F^\sharp\) and \(F^{\rm rd}\). Lemma 3.1 gives

\[
 r_s\in\{\lfloor k_s/2\rfloor,\lceil k_s/2\rceil\}.
\]

Thus, with \(r=\sum_sr_s\),

\[
 \left|r-\frac K2\right|\le\frac L2.                \tag{4.3}
\]

Since \(L=O(m)=o(B)\), (1.5), (3.16), and \(n\sim2m\) turn (4.2) into

\[
 |J_A(F^{\rm rd})-J_A(F^\sharp)|
 \le
 \left(\frac{\kappa_A}{192}+o_A(1)\right)
 \frac W{\sqrt m}.                                   \tag{4.4}
\]

This proves (0.8)--(0.9). Every cube endpoint differs from the conjugated
canonical factor in at most \(K\) packet signs, so the safe reference bound is

\[
 |J_A(F)-J_A(gF_m^{\rm MSW})|
 \le K(4S_A-2)
 =\left(\frac{\kappa_A}{96}+o_A(1)\right)
   \frac W{\sqrt m}.                                  \tag{4.5}
\]

The reference factor itself is not low-overload.

### Theorem 4.2 (macroscopic first-shadow obstruction)

Every vertex \(F\) of the conjugated scheduled packet cube satisfies

\[
 \boxed{
 M_1(F)\ge
 \left[
 (2m-3)C_{m-2}-\frac{2W}{m+2}-2K
 \right]_+.}                                         \tag{4.6}
\]

In particular,

\[
 J_A(F)\ge\left(\frac1{16}-o(1)\right)W.             \tag{4.7}
\]

#### Proof

The independently audited marked-gap theorem gives

\[
 M_1(F_m^{\rm MSW})
 \ge (2m-3)C_{m-2}-\frac{2W}{m+2}.                   \tag{4.8}
\]

One contextual packet switch has exactly two positive first-shadow cells and
therefore fills at most two old holes. Every cube endpoint is reached from the
canonical corner by at most \(K\) such switches. Coordinate conjugation does
not change the number of holes. This proves (4.6).

The exact ratio is

\[
 \frac{(2m-3)C_{m-2}}W
 =\frac{m(m+1)}{4(2m-1)(2m+1)}\longrightarrow\frac1{16}.  \tag{4.9}
\]

Also \(2/(m+2)\to0\) and, by (3.15),

\[
 \frac{2K}{W}\le\frac1n\to0.                        \tag{4.10}
\]

Now use Lemma 1.1. \(\square\)

Theorem 4.2 proves (0.11). It also shows that no refinement of the signs
inside this owner-disjoint packet atlas can yield coefficient one. The atlas
does not move enough depth-one holes, even though its coherent depth-\(H\)
pile has enormous quadratic energy.

---

## 5. Exact orbit-profile rounding for one fresh overlay

The next theorem applies to an arbitrary exact factor, not just the packet
family.

Fix a transposition \(\sigma\), an exact factor \(F\), and the genuine
ownership components \(\mathscr C\) of the \(F\)-versus-\(\sigma F\)
overlay. Let \(a_C\) be the old-side load contribution of component \(C\).
Every sign vector \(\varepsilon\in\{\pm1\}^{\mathscr C}\) selects one
complete side of each component and gives a literal integral exact factor
\(F_\varepsilon\).

At depth \(q\), a \(\sigma\)-fixed target \(X\) has an invariant load
\(f_X\). For a moved pair \(p=\{S,\sigma S\}\), put

\[
 \ell_p=\mu_q^{F_\varepsilon}(S)
       +\mu_q^{F_\varepsilon}(\sigma S),              \tag{5.1}
\]

\[
 z_{pC}=a_C(S)-a_C(\sigma S),\qquad
 D_p(\varepsilon)=\sum_C\varepsilon_Cz_{pC},          \tag{5.2}
\]

\[
 \pi_p=\ell_p\bmod2,\qquad
 L_p=\sum_C|z_{pC}|,\qquad
 V_p=\sum_Cz_{pC}^2.                                  \tag{5.3}
\]

Then

\[
 \mu_q^{F_\varepsilon}(S)=\frac{\ell_p+D_p}2,
 \qquad
 \mu_q^{F_\varepsilon}(\sigma S)=\frac{\ell_p-D_p}2, \tag{5.4}
\]

and

\[
 D_p(\varepsilon)\equiv\ell_p\pmod2.                 \tag{5.5}
\]

### Definition 5.1 (exact orbit-profile floor)

For a fixed target choose \(r_X\in\{0,1\}\). For a moved pair choose
\(r_p\in\{0,1,2\}\), interpreted as the number of ceiling entries assigned
to that pair. Subject to

\[
 \sum_{X\ \mathrm{fixed}}r_X+\sum_{p\ \mathrm{moved}}r_p=\rho_q, \tag{5.6}
\]

define

\[
 \boxed{
 \Delta_q^\sigma
 =\frac12\min_r\left[
   \sum_{X\ \mathrm{fixed}}|f_X-(c_q+r_X)|
  +\sum_{p\ \mathrm{moved}}|\ell_p-(2c_q+r_p)|
 \right].}                                           \tag{5.7}
\]

Every balanced quota induces a feasible \(r\). Aggregating its error over
\(\sigma\)-orbits and using the triangle inequality gives the invariant lower
bound

\[
 \boxed{O_q(F_\varepsilon)\ge\Delta_q^\sigma}         \tag{5.8}
\]

for every sign vector.

### Theorem 5.2 (profile plus signing residue)

For every common component sign vector,

\[
 \boxed{
 O_q(F_\varepsilon)
 \le\Delta_q^\sigma
 +\frac12\sum_p(|D_p(\varepsilon)|-\pi_p).}           \tag{5.9}
\]

#### Proof

Choose an optimizer in (5.7). For one moved pair put

\[
 T=2c_q+r_p,\qquad a=\ell_p-T.                        \tag{5.10}
\]

If \(r_p=0\) or \(r_p=2\), the two quota entries have difference
\(\delta=0\).
If \(r_p=1\), choose \(\delta\in\{\pm1\}\) nearest to \(D_p\). The exact
pair contribution to half the \(\ell^1\)-distance is

\[
 \frac14\bigl(|a+D_p-\delta|+|a-D_p+\delta|\bigr)
 =\frac12\max\{|a|,|D_p-\delta|\}.                   \tag{5.11}
\]

We claim

\[
 \max\{|a|,|D_p-\delta|\}
 \le |a|+|D_p|-\pi_p.                                \tag{5.12}
\]

There are four parity cases.

* If \(r_p\) and \(\ell_p\) are even, (5.12) is the ordinary
  \(\max\le\) sum inequality.
* If \(r_p\) is even and \(\ell_p\) is odd, both \(a\) and \(D_p\) are
  nonzero odd integers, so their maximum is at most their sum minus one.
* If \(r_p=1\) and \(\ell_p\) is odd, choose
  \(\delta=\operatorname{sgn}D_p\); then
  \(|D_p-\delta|=|D_p|-1\).
* If \(r_p=1\) and \(\ell_p\) is even, \(a\) is nonzero odd. When
  \(D_p=0\), the nearest \(|D_p-\delta|\) is one and is absorbed by
  \(|a|\). When \(D_p\ne0\), the nearest value is \(|D_p|-1\).

Thus (5.12) holds even when the selected quota-total parity differs from the
invariant pair-total parity. Fixed targets contribute exactly their term in
(5.7). Sum (5.11)--(5.12) over the target orbits. \(\square\)

### Corollary 5.3 (unconditional fair rounded factor)

Independent fair component signs obey

\[
 \mathbb E|D_p|
 \le\sqrt{\mathbb ED_p^2}=\sqrt{V_p}.                \tag{5.13}
\]

Hence one common deterministic all-depth signing gives

\[
 \boxed{
 J_A(F_\varepsilon)
 \le
 \sum_{q=1}^H\frac{\Delta_q^\sigma}{c_q}
 +\frac12\sum_{q=1}^H\sum_p
       \frac{\sqrt{V_p}-\pi_p}{c_q}.}                \tag{5.14}
\]

At least half of all sign vectors satisfy twice the right side. Conditional
expectations can select one without leaving the exact factor cube.

### Corollary 5.4 (joint-TU profile realization)

Form the one vertically concatenated all-depth matrix

\[
 Z=(z_{pC})_{q\le H}.                                \tag{5.15}
\]

Suppose deleting one joint row set

\[
 \mathcal R=\bigsqcup_{q=1}^H\mathcal R_q            \tag{5.16}
\]

makes the remaining matrix totally unimodular. Then one common integral
signing satisfies

\[
 \boxed{
 O_q(F_\varepsilon)
 \le\Delta_q^\sigma
 +\frac12\sum_{p\in\mathcal R_q}(L_p-\pi_p),}        \tag{5.17}
\]

and

\[
 \boxed{
 J_A(F_\varepsilon)
 \le\sum_q\frac{\Delta_q^\sigma}{c_q}
 +\frac12\sum_q\sum_{p\in\mathcal R_q}
       \frac{L_p-\pi_p}{c_q}.}                       \tag{5.18}
\]

If \(\mathcal R=\varnothing\), then simultaneously

\[
 \boxed{O_q(F_\varepsilon)=\Delta_q^\sigma
        \quad(1\le q\le H).}                         \tag{5.19}
\]

#### Proof

Let \(Z'\) be the retained matrix and, for each retained row, put

\[
 s_p=\sum_C z_{pC}.
\]

Consider

\[
 \mathcal P=\left\{x\in[0,1]^{\mathscr C}:
 \left\lfloor\frac{s_p}{2}\right\rfloor
 \le (Z'x)_p\le
 \left\lceil\frac{s_p}{2}\right\rceil
 \text{ for every retained }p\right\}.               \tag{5.20}
\]

The half-vector belongs to \(\mathcal P\). Since \(Z'\) is TU, stacking
\(Z',-Z',I,-I\) is TU; all right sides are integral, so the nonempty bounded
polytope has an integral vertex \(x\in\{0,1\}^{\mathscr C}\). Put
\(\varepsilon_C=1-2x_C\). Then

\[
 D_p=s_p-2(Z'x)_p
\]

has magnitude zero for even \(s_p\) and one for odd \(s_p\). Since
\(s_p\equiv\ell_p\pmod2\), this gives one column signing with

\[
 |D_p|=\pi_p                                          \tag{5.21}
\]

on every retained row. On a deleted row,

\[
 |D_p|\le L_p.                                       \tag{5.22}
\]

Insert these estimates in Theorem 5.2. When no row is deleted, combine the
upper bound with (5.8). \(\square\)

This is stronger than K8's earlier statement: no assumption that fixed loads
or moved pair totals already match a floor/ceiling profile is required. Their
entire failure is paid exactly by \(\Delta_q^\sigma\).

### Corollary 5.5 (entrywise near-TU)

Suppose

\[
 Z=Z_0+E,                                             \tag{5.23}
\]

where \(Z_0\) is one joint integral TU matrix, and put

\[
 K_p=\sum_C|E_{pC}|.                                  \tag{5.24}
\]

Both \(Z\) and \(Z_0\) are integral, so \(E\) is integral and every \(K_p\)
is a nonnegative integer.

Then one common exact endpoint satisfies

\[
 \boxed{
 J_A(F_\varepsilon)
 \le\sum_q\frac{\Delta_q^\sigma}{c_q}
 +\sum_{q,p}\frac{K_p}{c_q}.}                        \tag{5.25}
\]

#### Proof

Choose a parity-optimal TU signing for \(Z_0\). If \(K_p=0\), the row has no
residue. If \(K_p\ge1\), then

\[
 |D_p|-\pi_p
 \le |D_p^{(0)}|+|(E\varepsilon)_p|
 \le1+K_p\le2K_p.                                   \tag{5.26}
\]

Apply Theorem 5.2. \(\square\)

---

## 6. Exact productivity certificate

The profile theorem also gives a sufficient quantitative certificate for an
escaped label to be productive.

For each depth choose a balanced quota \(b_q\) attaining \(O_q(F)\), and put

\[
 e_q(S)=\mu_q^F(S)-b_q(S).                            \tag{6.1}
\]

For a candidate transposition \(\sigma\), define its opposite-error mixing

\[
 \mathsf M_{q,\sigma}(b_q)
 =\sum_{\substack{p=\{S,\sigma S\}\\
                   e_q(S)e_q(\sigma S)<0}}
   \min\{|e_q(S)|,|e_q(\sigma S)|\}.                 \tag{6.2}
\]

### Theorem 6.1 (mixing minus synchronization leakage)

The quota \(b_q\) induces a feasible orbit profile and

\[
 \boxed{
 \Delta_q^\sigma
 \le O_q(F)-\mathsf M_{q,\sigma}(b_q).}               \tag{6.3}
\]

Consequently, under the joint row-deletion hypothesis of Corollary 5.4, one
exact endpoint satisfies

\[
 \boxed{
 J_A(F_\varepsilon)
 \le J_A(F)
 -\sum_q\frac{\mathsf M_{q,\sigma}(b_q)}{c_q}
 +\frac12\sum_q\sum_{p\in\mathcal R_q}
       \frac{L_p-\pi_p}{c_q}.}                       \tag{6.4}
\]

#### Proof

On a moved pair, the full quota-error contribution is

\[
 \frac12(|e_q(S)|+|e_q(\sigma S)|),                  \tag{6.5}
\]

while its orbit-total contribution is

\[
 \frac12|e_q(S)+e_q(\sigma S)|.                      \tag{6.6}
\]

The difference is zero for equal signs and is the minimum magnitude for
opposite signs. Fixed-target contributions are unchanged. Summing proves
(6.3); combine it with (5.18). \(\square\)

Thus full joint TU makes every positive amount of opposite quota-error mixing
productive. With deleted rows, (6.4) certifies strict descent whenever the
weighted mixing exceeds the displayed synchronization-leakage charge. This is
a sufficient certificate, not a necessary condition for descent. What remains
unproved for this route is the geometric statement that some
outside-menu \(\sigma\) has this property on an arbitrary exact factor, or on
K's prepared factor in particular.

---

## 7. First-shadow obstruction to a one-round escaped overlay

The obstruction below is pathwise and does not assume independent signs.

Let \(F_0\) be any packet-cube endpoint from Section 3, let \(\sigma\) be an
arbitrary transposition, and form the freshly recomputed ownership components.
For a moved target pair \(p=\{S,T=\sigma S\}\), call \(p\) *productively
split* if, after orienting it so that

\[
 \mu_1^{F_0}(S)=0,\qquad \mu_1^{F_0}(T)=t\ge2,         \tag{7.1}
\]

the \(t\) occurrences of \(T\) meet at least two distinct ownership
components. Let \(\mathcal P_\sigma(F_0)\) be the set of these pairs.

### Theorem 7.1 (necessary productive splitting)

Every whole-component signing \(G\) satisfies

\[
 \boxed{
 M_1(G)\ge M_1(F_0)-|\mathcal P_\sigma(F_0)|,}        \tag{7.2}
\]

and therefore

\[
 \boxed{
 J_A(G)\ge
 (2m-3)C_{m-2}-\frac{2W}{m+2}-2K
 -|\mathcal P_\sigma(F_0)|.}                         \tag{7.3}
\]

In particular, \(J_A(G)=o(W)\) requires

\[
 \boxed{
 |\mathcal P_\sigma(F_0)|
 \ge\left(\frac1{16}-o(1)\right)W.}                  \tag{7.4}
\]

#### Proof

Transposition equivariance interchanges, component by component, the two
occurrence counts on \(S,T\). A fixed hole remains a hole. On a moved pair:

* a \((0,0)\) pair retains both holes;
* a \((0,1)\) pair retains one hole;
* if a \((0,t)\), \(t\ge2\), is supported in only one component, its endpoint
  is either \((0,t)\) or \((t,0)\), so it retains one hole.

Only a productively split pair can remove its old hole, and it removes at most
one. Distinct target orbits are disjoint, proving (7.2). Now use Theorem 4.2
and Lemma 1.1. \(\square\)

### Corollary 7.2 (row-distance capacity)

Let \(\mathcal R\) be the old rows in the switched components. For
\(C\in\mathcal R\), let \(d_C\le m\) be the shorter cyclic distance between
the bridge labels in row \(C\). The exact positive first-shadow action of one
row is

\[
 \lambda_{m-1}(d)
 =2\min(m-1,d)-2\mathbf1_{\{d=m-1\}}.                 \tag{7.5}
\]

Hence

\[
 \sum_{C\in\mathcal R}\lambda_{m-1}(d_C)
 \ge M_1(F_0)-J_A(G).                                \tag{7.6}
\]

If \(J_A(G)=o(W)\), then

\[
 \boxed{
 \sum_{C\in\mathcal R}d_C
 \ge\left(\frac1{32}-o(1)\right)W,\qquad
 |\mathcal R|
 \ge\left(\frac1{16}-o(1)\right)B.}                 \tag{7.7}
\]

#### Proof

A switched row can fill at most its positive first-shadow action, proving
(7.6). Use

\[
 \lambda_{m-1}(d)\le2d,
 \qquad
 \lambda_{m-1}(d)\le n-3,                            \tag{7.8}
\]

Theorem 4.2, and \(W=nB\). \(\square\)

For this one-round packet-cube route, the missing resource is not merely
\(\Omega(W)\) middle seams. It is \(\Omega(W)\) targetwise productive
containment, spread through a positive fraction of all owner rows with a
linear total cyclic-distance budget.

---

## 8. Why the independent fair-sign first moment cannot replace correlation

At depth one, examine the orbit-profile floor from Section 5. A fixed hole
costs at least \(1/2\) in \(\Delta_1^\sigma\). A moved \((0,0)\) pair costs
at least one. A one-hole pair \((0,t)\) with
\(t\notin\{2,3,4\}\) costs at least \(1/2\). For the profile-compatible
pairs \((0,3)\) and \((0,4)\), an optimizer either spends ceiling entries or
pays the corresponding profile error.

Consequently,

\[
 \boxed{
 \#\{\text{holes not lying in a moved }(0,2)\text{ pair}\}
 \le2\Delta_1^\sigma+\rho_1.}                        \tag{8.1}
\]

### Proof of (8.1)

Fix an optimizer \(r\) in (5.7), and let \(h_{\mathcal O}\) count the holes
of orbit \(\mathcal O\) which are not in a moved \((0,2)\) pair. The following
local inequalities hold:

\[
 h_{\{X\}}=1
 \le |0-(1+r_X)|                                      \tag{8.2a}
\]

for a fixed hole,

\[
 h_{\{S,T\}}=2
 \le |0-(2+r_p)|                                      \tag{8.2b}
\]

for a moved \((0,0)\) pair, and, for a moved \((0,t)\) pair with
\(t\ge1\), \(t\ne2\),

\[
 h_{\{S,T\}}=1
 \le |t-(2+r_p)|+r_p.                                \tag{8.2c}
\]

Indeed, if \(r_p=0\), the first term in (8.2c) is at least one because
\(t\ne2\); if \(r_p\ge1\), its second term is already at least one. Sum these
inequalities over all exceptional orbits. The absolute-value terms are
exactly at most \(2\Delta_1^\sigma\), while

\[
 \sum_{p\ \mathrm{moved}}r_p\le\rho_1.
\]

This proves (8.1). \(\square\)

Suppose now that

\[
 M_1(F_0)\ge\left(\frac1{16}-o(1)\right)W            \tag{8.3}
\]

and an escaped overlay has \(\Delta_1^\sigma=o(W)\). Since
\(\rho_1=2W/(m+2)=o(W)\), (8.1) forces

\[
 \left(\frac1{16}-o(1)\right)W                       \tag{8.4}
\]

target-disjoint moved \((0,2)\) pairs.

If unit leakage \(z_{pC}\in\{-1,0,1\}\) also holds, the two occurrences in
each such pair lie in exactly two distinct active components, with equal
initial leakage sign. A parity-optimal signing must give those two columns
opposite signs. Thus the depth-one leakage matrix alone contains at least

\[
 \boxed{
 2M_1(F_0)-o(W)
 \ge\left(\frac18-o(1)\right)W}                      \tag{8.5}
\]

nonzero hole-pair/component incidences.

The independent fair-sign first moment is quantitatively insufficient even in
this ideal unit-split geometry. On one \((0,2)\) row, both signs agree with
probability \(1/2\), leaving one hole, and disagree with probability \(1/2\),
leaving no hole. By linearity of expectation over the target-disjoint pairs,

\[
 \boxed{
 \mathbb E M_1(F_\varepsilon)
 \ge\left(\frac1{32}-o(1)\right)W.}                  \tag{8.6}
\]

K's direct first-shadow alignment theorem currently supplies at most
\(4B=o(W)\) directly aligned incidences for one fresh colour. This is not an
upper bound on genuinely nonlocal leakage incidences. Therefore the
\((11/288-o(1))W\) middle-seam theorem does not itself construct the required
first-shadow constraint graph. A successful overlay and its ownership geometry
must supply almost all of (8.5) through genuinely nonlocal component
containment. In the ideal
width-two depth-one constraint graph, it must violate only \(o(W)\) of the
required pair constraints. Under the standing weighted profile bound, full
all-depth TU is one sufficient mechanism for producing such a sign. The
deleted-row and entrywise near-TU variants are sufficient when their weighted
leakage charge in (5.18) or (5.25), respectively, is \(o(W)\). None of these
conditions is proved necessary.

Equation (8.6) is a no-go for an expectation/first-moment proof based on
uniform independent fair signs. It is not a no-go for the existence of an
exceptional successful sign vector in the same support, and not a no-go for a
correlated TU-style selection.

---

## 9. Independent audit of decisive constants and implications

The two decisive parts were checked by independent derivations.

### 9.1 Productive-family audit

1. **Menu escape.** The argument uses only connected-component sizes of the
   menu graph. It applies to both the original and sharpened protected menus.
   A single global conjugation maps the whole native matching; no bridge is
   relabelled independently. This proves a menu-avoiding packet family, not a
   path beginning at the protected invariant-fibre minimizer.

2. **Exact factors.** Packet owner supports are disjoint. Each balanced choice
   selects one complete side of every genuine size-two component. Translated
   packets remain genuine after recomputation. Hence the macro-endpoint and
   every microstep are integral exact factors.

   The coherent start \(F^\sharp\) is selected existentially by the backward
   signing argument. It is not asserted to be the canonical corner, and the
   cost of preparing it from that corner is not included in (0.6). Theorem
   4.2 deliberately controls every cube corner, so this scope issue does not
   affect the shallow-overload obstruction.

3. **Energy constant.** Equations (3.5)--(3.8) give

   \[
   \|D_s\|_H^2>\frac{4^H}{8L_AH^4}k_s,\qquad
   V_s\le(8H-4)k_s.
   \]

   Dividing their difference by four gives exactly

   \[
   \frac{4^H}{32L_AH^4}-(2H-1),
   \]

   with no missing factor two.

4. **Packet density.** The Catalan tail starts at gap four, so its limit is
   \(\sum_{j\ge4}4^{-j}=1/192\), not \(1/256\). The latter is only the safe
   one-block lower bound.

5. **Rounded overload constant.** The rounded endpoint changes
   \((1/384+o(1))B\) signs from the coherent endpoint. Multiplication by
   \((4\kappa_A+o(1))\sqrt m\), followed by
   \(B=W/(2m+1)\), gives \(\kappa_A/192\) in (0.9).

6. **First-shadow subtraction.** One packet can fill at most two old holes,
   so the full cube subtracts \(2K\), not \(K\). Since \(2K\le B=o(W)\),
   the \(1/16\) limit survives.

### 9.2 Orbit-profile audit

1. The pair variable \(r_p\) counts ceiling entries, so the global constraint
   is exactly (5.6). There is no uncharged quota remainder.

2. The pair half-\(\ell^1\) formula is \(\frac12\max(|a|,|D-\delta|)\).
   The four parity cases in Theorem 5.2 explicitly cover the formerly omitted
   case where the invariant total and quota total have different parity.

3. One common sign vector is used for every depth. Separate depthwise TU
   statements are insufficient.

4. Full joint TU realizes \(\Delta_q^\sigma\), not necessarily zero. This is
   the corrected implication scope: TU removes signing residue but cannot
   remove an invariant orbit-profile defect.

5. Fair rounding provides the upper certificate (5.14), but, under the
   hypotheses of Section 8, (8.6) is an independent lower bound on its expected
   first-shadow holes in the ideal unit-split K geometry. It does not exclude a
   rare successful sign vector.

---

## 10. Exact proved/conditional boundary

### Proved

* A full matching of coordinate labels exists outside both protected menus.
* The entire AB6 distinct-bridge packet schedule can be conjugated into that
  complement.
* A balanced integral rounded endpoint has the exact energy gain (0.6).
* Its change in \(J_A\) from the coherent endpoint is
  \(O_A(W/\sqrt m)=o(W)\), with leading upper constant
  \(\kappa_A/192\).
* Every endpoint in this family still has
  \((1/16-o(1))W\) depth-one overload.
* The exact orbit-profile rounding theorem, joint-TU realization theorem,
  entrywise near-TU bound, and mixing-minus-leakage productivity certificate are
  valid for every actual transposition overlay.
* Any successful one-round escape from an endpoint of the Section 3 packet
  cube needs \((1/16-o(1))W\) productively split hole pairs and a
  positive-density owner-row action budget.
* On an endpoint satisfying the Section 8 hypotheses, including
  \(\Delta_1^\sigma=o(W)\) and unit leakage, uniform independent fair signs
  have expected first-shadow overload \(\Omega(W)\), so their first moment
  cannot certify the repair.

### Unproved

* No theorem produces the required \(\Omega(W)\) nonlocal first-shadow split
  rows for K's fresh overlay.
* No theorem proves that their all-depth leakage matrix is TU. Nor is there a
  proof of a deleted-row set with
  \[
   \frac12\sum_q\sum_{p\in\mathcal R_q}
   \frac{L_p-\pi_p}{c_q}=o(W),
  \]
  or an integral TU approximation with
  \[
   \sum_{q,p}\frac{K_p}{c_q}=o(W).
  \]
* No theorem bounds the full orbit-profile sum

  \[
  \sum_{q\le H}\frac{\Delta_q^\sigma}{c_q}=o(W)       \tag{10.1}
  \]

  for a productive outside-menu bridge on every exact factor.
* No actual \(J_A\)-decreasing escaped family with terminal
  \(J_A=o(W)\) is constructed here.
* No literal contiguous-OR word and no coefficient-one conclusion is claimed.

The exact boundary for this one-overlay route is now quantitative. Any
successful endpoint necessarily has

\[
 \sum_{q\le H}\frac{\Delta_q^\sigma}{c_q}=o(W),
\]

and, on an endpoint of the Section 3 packet cube, the productive splitting and
row-action resources of Theorem 7.1 and Corollary 7.2. A one-overlay joint-TU
construction would be sufficient for coefficient one if the whole right side
of (5.18) were \(o(W)\). Corollary 5.5 gives the analogous sufficient condition

\[
 \sum_q\frac{\Delta_q^\sigma}{c_q}
 +\sum_{q,p}\frac{K_p}{c_q}=o(W)
\]

for an entrywise TU approximation. Alternatively, in the descent formulation, (6.4)
certifies a terminal \(o(W)\) endpoint when its whole displayed right side is
\(o(W)\); merely making mixing larger than leakage proves one strict descent,
not termination. Repeated descents would require a separate cumulative
convergence theorem. None of these sufficient conditions is asserted to be
necessary. The present AB6 family proves that labels and quadratic productivity
can escape; Theorems 4.2, 7.1, and (8.5)--(8.6) prove why the available rounding
arguments do not yet escape the constant-one obstruction.
