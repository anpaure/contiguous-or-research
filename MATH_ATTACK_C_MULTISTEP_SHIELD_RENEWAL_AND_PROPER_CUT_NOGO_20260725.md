# Lane C: multistep shield renewal, proper-cut compression, and the exact bypass gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or probabilistic experiment is used.  Every random leaf below is a
literal integral exact middle wreath factor.  Randomness is used only as an
existence proof for one deterministic leaf.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\operatorname{Cat}_m=\frac Wn,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  At depth \(q\), put

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\]

and let \(\mathcal Q_A\) be the unhalved floor energy

\[
\mathcal Q_A(F)=
\sum_{q\le H}\frac1{c_q}
\sum_{|S|=m-q}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
\tag{0.1}
\]

Fix \(0<\gamma<\log4\), and define

\[
J=\left\lfloor\frac{\gamma H}{\log(108m)}\right\rfloor,
\qquad
\Lambda=(J+1)(n-J),
\qquad
a=1-\frac{\Lambda}{n(n-1)}.
\tag{0.2}
\]

The common-row run-cap theorem gives, for every exact factor,

\[
\mathcal L_J(F):=
\sum_{q\le H}\sum_{2\le j\le J}
\frac{\|P_{q,j}f_q(F)\|_2^2}{c_q}
\le
U:=\frac{tH^3}{n}e^{\gamma H}.
\tag{0.3}
\]

Write

\[
\mathcal H_J(F):=
\sum_{q\le H}\sum_{j>J}
\frac{\|P_{q,j}f_q(F)\|_2^2}{c_q}.
\tag{0.4}
\]

For the AB8 statement below, write

\[
W=c_qN_q+\rho_q,\qquad 0\le\rho_q<N_q,
\]

\[
P_q^{\min}=(N_q-\rho_q)\binom{c_q}{2}
+\rho_q\binom{c_q+1}{2},\qquad
b_q=\binom{c_q+1}{2},
\]

and

\[
\Phi_q(F)=\sum_S\binom{\mu_q^F(S)}2-P_q^{\min},
\qquad
\mathfrak F_A(F)=\sum_{q\le H}\frac{\Phi_q(F)}{b_q}.
\tag{0.4a}
\]

This report proves three new exact statements.

1. **A genuine multistep bypass under shield burnout.**  Run \(T\) iid
   uniform transposition heats, recomputing the genuine ownership components
   after every previous choice.  If the expected high-harmonic component
   variance at every time is bounded by the physical row capacity at level
   \(s\), then

   \[
   \boxed{
   \mathbb E\mathcal Q_A(F_T)-\mathcal Q_A(F_0)
   \le
   U-(1-a^T)
   \left(\mathcal H_J(F_0)-\frac{sWD_{m,H}}{\Lambda}\right),}
   \tag{0.5}
   \]

   where

   \[
   D_{m,H}=\sum_{q\le H}
   \frac{(m-q)(m+q+1)-2}{c_q}.
   \tag{0.6}
   \]

   A strict right-hand side produces one literal deterministic terminal
   factor of smaller full floor energy.  This is an actual nonlocal descent,
   not a reduced-objective or fractional statement.

   For the high exact MSW-cell factor, let

   \[
   E_m^*=\frac{t4^H}{2048M_AH^4},\qquad
   M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil,
   \tag{0.7}
   \]

   put also \(K_A=\binom{M_A+1}{2}\), and define

   \[
   s_m^\dagger=
   \left\lfloor\frac{\Lambda E_m^*}{4WD_{m,H}}\right\rfloor.
   \tag{0.8}
   \]

   If the cap in (0.5) holds with \(s=s_m^\dagger\) throughout the heat
   tree and

   \[
   T=T_{1/2}:=
   \left\lceil\frac{\log2}{-\log a}\right\rceil,
   \tag{0.9}
   \]

   then a literal lower-energy endpoint exists for all sufficiently large
   \(m\).  The exact asymptotic scales are

   \[
   T_{1/2}
   =\left(\frac{2\log2}{\gamma A}+o_{A,\gamma}(1)\right)
   \sqrt m\,\log(108m),
   \tag{0.10}
   \]

   and

   \[
   s_m^\dagger\sim
   \frac{\gamma4^H}
   {8192M_AI_AH^3m^{5/2}\log(108m)},
   \qquad
   I_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
   \tag{0.11}
   \]

   This cap cannot hold at time one if the high MSW-cell corner is already
   locally minimal in every transposition cell: Theorem 3.2 below forces a
   time-one cap at least \((4-o(1))s_m^\dagger\).  Thus (0.5) becomes a
   bypass only after a proper preparatory cut has genuinely burned the
   initial shields.

2. **Exact shield-persistence/renewal obstruction.**  If no leaf of this heat block has
   lower full floor energy, then necessarily

   \[
   \boxed{
   \sum_{r=1}^T a^{T-r}\,
   \mathbb E V_{\tau_r}^{>J}(F_{r-1})
   \ge
   4\bigl((1-a^T)\mathcal H_J(F_0)-U\bigr).}
   \tag{0.12}
   \]

   Thus the static giant shields must either survive the suffix weighting or
   be renewed along the recomputed multistep tree strongly enough to repay
   every coherent loss.  Initial one-cell locality alone does not give the
   full space-time inequality (0.12).

3. **Arbitrary-correlation compression and a sharper escape obstruction.**
   In any realized adaptive schedule, with completely arbitrary correlated
   component choices, every empty cut and every all-component cut can be
   deleted.  After conjugating the remaining suffix, the endpoint changes
   only by a coordinate permutation and therefore has exactly the same
   energy.  Hence only a nonempty proper cut of a disconnected fresh overlay
   can change the coordinate orbit.

   Moreover, the AB8 private-token escape bound counts only such **proper
   cuts**, not all transposition letters.  If \(P\) is their number, then

   \[
   \boxed{
   \mathfrak F_A(F_{\rm end})
   \ge\frac1{b_H}
   \left(
   \frac{L_s\operatorname{Cat}_H^2}{2^{P+2}}
   -\frac{L_s\operatorname{Cat}_H}{2}-P_H^{\min}
   \right).}
   \tag{0.13}
   \]

   Thus, for the balanced AB8 cage, reaching \(O(W)\), and hence reaching
   \(O_A(Ht)\), requires

   \[
   \boxed{P\ge H-3\log_2m-O_{A,C}(1)=\Omega_A(\sqrt m)}
   \tag{0.14}
   \]

   genuinely fragmented proper cuts.  Connected stages in a spanning or
   expander word contribute zero to this count and can be compressed away.

The positive theorem (0.5) is conditional on dynamic shield burnout.  No
such burnout theorem is proved.  Conversely, no genuine high-energy exact
factor is constructed whose shields satisfy the renewal lower bound for all
multistep couplings.  Therefore no constant-one conclusion is claimed.

The exact remaining statement is no longer merely “use several
transpositions.”  One must prove that a high-energy exact factor admits a
decision tree containing the required proper fragmented cuts for which the
left side of (0.12) is strictly smaller than its right side, or construct a
genuine exact factor for which every such tree renews the shield budget.

## 1. Exact harmonic and cell quantities

Put

\[
f_q(F)=\mu_q^F-\frac W{N_q}\mathbf1.
\]

Every exact-factor centered profile has zero Johnson degrees zero and one.
Consequently

\[
B_A+\mathcal Q_A(F)=\mathcal L_J(F)+\mathcal H_J(F),
\tag{1.1}
\]

where

\[
B_A=\sum_{q\le H}
\frac{N_q\theta_q(1-\theta_q)}{c_q},
\qquad
\frac W{N_q}=c_q+\theta_q.
\]

Fix a transposition \(\tau\), and let \(K\) range over the freshly
computed genuine ownership components of \(F/(\tau F)\).  If

\[
d_{K,q}=\mu_q(K)-\mu_q(\tau K),
\]

put

\[
V_\tau^{>J}(F)=
\sum_K\sum_{q\le H}\sum_{j>J}
\frac{\|P_{q,j}d_{K,q}\|_2^2}{c_q}.
\tag{1.2}
\]

For a physical row \(C\), let \(w_{C,q}\) be the indicator of its cyclic
rank-\((m-q)\) intervals, and define

\[
\mathscr R_{\tau,H}(F)=
\sum_{q\le H}\frac1{c_q}
\sum_{C\in F}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{1.3}
\]

The exact cyclic-row boundary identity is

\[
\boxed{
\sum_\tau\mathscr R_{\tau,H}(F)=2WD_{m,H},}
\tag{1.4}
\]

where the sum is over the \(T_n=\binom n2\) unordered transpositions.
The right side is independent of \(F\).

For a component with \(u\) old-side rows, Cauchy--Schwarz gives

\[
\sum_{q,j>J}\frac{\|P_{q,j}d_{K,q}\|_2^2}{c_q}
\le
u\sum_{q}\frac1{c_q}
\sum_{C\in K}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{1.5}
\]

Thus \(V_\tau^{>J}\le s\mathscr R_{\tau,H}\) whenever every current
component has at most \(s\) old-side rows.  In this report the same
inequality may be assumed directly; it is weaker than the component-size
cap and measures active high-harmonic amplification.

## 2. A multistep high-harmonic descent theorem

Sample the entire word \(\tau_1,\ldots,\tau_T\) independently and uniformly
from the unordered coordinate transpositions, before exposing any component
sign.  At time \(r\), after observing the
previous exact factor \(F_{r-1}\), freshly compute its genuine
\(\tau_r\)-components and choose all component signs independently and
fairly.  Every leaf is an exact factor.

Let

\[
\alpha_j=1-\frac{j(n-j+1)}{n(n-1)}.
\tag{2.1}
\]

For \(j>J\), monotonicity on the occurring Johnson degrees gives

\[
0\le\alpha_j\le a.
\tag{2.2}
\]

### Theorem 2.1 (exact annealed high-sector inequality)

For every starting exact factor,

\[
\boxed{
\mathbb E\mathcal Q_A(F_T)-\mathcal Q_A(F_0)
\le
U-(1-a^T)\mathcal H_J(F_0)
+\frac14\sum_{r=1}^Ta^{T-r}
\mathbb E V_{\tau_r}^{>J}(F_{r-1}).}
\tag{2.3}
\]

#### Proof

Condition on the entire prefix through time \(r\).  The future iid suffix is
independent of every current component effect.  On Johnson degree \(j\),
its expected squared-norm multiplier is exactly
\(\alpha_j^{T-r}\).  Independent fair component signs kill all
cross-component and cross-time terms.  Therefore the terminal high-sector
mass satisfies

\[
\mathbb E\mathcal H_J(F_T)
\le
a^T\mathcal H_J(F_0)
+\frac14\sum_{r=1}^Ta^{T-r}
\mathbb E V_{\tau_r}^{>J}(F_{r-1}).
\tag{2.4}
\]

The factor \(1/4\) comes from the component perturbation
\(\frac12\sum_K\varepsilon_Kd_K\).

Every terminal leaf is a genuine exact factor, so the uniform literal
run-cap estimate (0.3) gives

\[
\mathcal L_J(F_T)\le U
\]

pointwise.  Also \(\mathcal L_J(F_0)\ge0\).  Subtract (1.1) at the two
endpoints; the fixed floor \(B_A\) cancels exactly.  Combining with (2.4)
proves (2.3).  \(\square\)

### Corollary 2.2 (dynamic-cap descent)

Suppose, more generally, that the heat tree satisfies the annealed bounds

\[
\mathbb E V_{\tau_r}^{>J}(F_{r-1})
\le\frac{2sWD_{m,H}}{T_n}
\qquad(1\le r\le T).
\tag{2.5}
\]

Then (0.5) holds.  In particular, if

\[
\boxed{
\mathcal H_J(F_0)>
\frac{sWD_{m,H}}{\Lambda}+\frac{U}{1-a^T},}
\tag{2.6}
\]

there is a deterministic realized word and a deterministic sequence of
complete genuine component cuts whose terminal exact factor has strictly
smaller full floor energy.

The stronger pointwise hypothesis

\[
V_\tau^{>J}(G)\le s\mathscr R_{\tau,H}(G)
\tag{2.7}
\]

for every state \(G\) in the heat tree and every \(\tau\) implies (2.5).

#### Proof

The geometric sum and (0.2) give

\[
\begin{aligned}
\frac14\sum_{r=1}^Ta^{T-r}
\mathbb E V_{\tau_r}^{>J}
&\le
\frac{sWD_{m,H}}{2T_n}\frac{1-a^T}{1-a}\\
&=(1-a^T)\frac{sWD_{m,H}}{\Lambda},
\end{aligned}
\tag{2.8}
\]

because \(2T_n(1-a)=\Lambda\).  Substitute in (2.3) to get (0.5).
Condition (2.6) makes its right side strict and negative.  Since the
average of finitely many literal terminal energies is below the starting
energy, one terminal leaf is strictly lower.

Under (2.7), condition on any current state and average over the next
uniform transposition.  Equation (1.4) gives

\[
\mathbb E_\tau V_\tau^{>J}(G)
\le\frac{s}{T_n}\sum_\tau\mathscr R_{\tau,H}(G)
=\frac{2sWD_{m,H}}{T_n},
\]

which is (2.5).  \(\square\)

### Corollary 2.3 (conditional escape from the high MSW cell)

Let \(F_0\) be any corner of the audited high MSW cell for which

\[
\mathcal H_J(F_0)\ge E_m^*.
\tag{2.9}
\]

Take \(s=s_m^\dagger\) from (0.8) and \(T=T_{1/2}\).  If (2.5) holds,
then, for all sufficiently large \(m=m(A,\gamma)\), one literal terminal
factor has lower full floor energy than \(F_0\).

#### Proof

The definitions give

\[
\frac{s_m^\dagger WD_{m,H}}{\Lambda}\le\frac{E_m^*}{4},
\qquad
1-a^{T_{1/2}}\ge\frac12.
\tag{2.10}
\]

Also

\[
\frac U{E_m^*}
=\frac{2048M_AH^7}{n}
e^{-(\log4-\gamma)H}\longrightarrow0.
\tag{2.11}
\]

Hence the right side of (0.5) is at most

\[
U-\frac12\left(E_m^*-\frac{E_m^*}{4}\right)
=U-\frac{3E_m^*}{8}<0
\]

eventually.  Corollary 2.2 supplies the literal leaf.  \(\square\)

The floor-sensitive asymptotic \(D_{m,H}\sim I_Am^{5/2}\), together with

\[
J\sim\frac{\gamma H}{\log(108m)},
\qquad
\Lambda\sim nJ,
\]

gives (0.11).  Since \(-\log a\sim1-a\sim J/n\), it also gives (0.10).

## 3. The exact space-time persistence/renewal obstruction

### Theorem 3.1 (shield persistence or renewal is necessary for failure of descent)

If every terminal leaf in Theorem 2.1 satisfies

\[
\mathcal Q_A(F_T)\ge\mathcal Q_A(F_0),
\tag{3.1}
\]

then (0.12) holds.

Equivalently, if

\[
s_{\rm ren}:=
\frac{\Lambda}{WD_{m,H}}
\left(
\mathcal H_J(F_0)-\frac{U}{1-a^T}
\right)>0,
\tag{3.2}
\]

then at some positive-probability prefix and next transposition,

\[
\boxed{
V_\tau^{>J}(G)\ge
s_{\rm ren}\,\mathscr R_{\tau,H}(G).}
\tag{3.3}
\]

#### Proof

Condition (3.1) makes the left side of (2.3) nonnegative.  Rearrangement
gives (0.12).

For every time \(r\), conditional uniformity of \(\tau_r\) and (1.4)
give

\[
\mathbb E\mathscr R_{\tau_r,H}(F_{r-1})
=\frac{2WD_{m,H}}{T_n}.
\]

Therefore

\[
\sum_{r=1}^Ta^{T-r}
\mathbb E\mathscr R_{\tau_r,H}
=\frac{4WD_{m,H}}{\Lambda}(1-a^T).
\tag{3.4}
\]

If (3.3) failed everywhere on the finite heat tree, the left side of
(0.12) would be strictly smaller than \(s_{\rm ren}\) times (3.4), which
is exactly its right side.  This is impossible.  Replacing strict by
non-strict inequalities yields the displayed non-strict conclusion.
\(\square\)

For the high MSW cell and \(T=T_{1/2}\), equation (2.11) gives

\[
s_{\rm ren}
\ge(1-o(1))\frac{\Lambda E_m^*}{WD_{m,H}}
= (4-o(1))s_m^\dagger.
\tag{3.5}
\]

Thus a failed multistep bypass forces an active shield of the same
exponential scale as the static C theorem at a freshly recomputed state in
the block.  Formula (0.12), rather than the existence of a giant component
only at time zero, is the exact dynamic obstruction.

### Theorem 3.2 (why the uniform-cap bypass cannot start at an all-cell local corner)

Suppose \(F\) is a component-cut local minimum of the **full** floor energy
in every transposition cell.  Then

\[
\boxed{
\frac1{T_n}\sum_\tau V_\tau^{>J}(F)
\ge
\frac{2\Lambda}{T_n}\mathcal H_J(F)-4U.}
\tag{3.6}
\]

Consequently, if the time-one annealed cap (2.5) holds at such an \(F\),
then necessarily

\[
\boxed{
s\ge
\frac{\Lambda\mathcal H_J(F)-2T_nU}{WD_{m,H}}.}
\tag{3.7}
\]

For an all-transposition-local high MSW-cell corner with
\(\mathcal H_J(F)\ge E_m^*\), the right side of (3.7) is

\[
(1-o(1))\frac{\Lambda E_m^*}{WD_{m,H}}
=(4-o(1))s_m^\dagger.
\tag{3.8}
\]

Thus the cap used in Corollary 2.3 is impossible at time one for the exact
all-cell local corner it is meant to escape.  Corollary 2.3 is a genuine
descent theorem for a factor at which shield burnout has already occurred;
it is not an unconditional bypass of local minimality.  A successful
multistep proof must tolerate the initial restitution, filter it through a
long suffix, and prove that freshly recomputed later shields do not renew it.

#### Proof

For one transposition, let \(A_\tau^{>J}\) be the coherent high-sector
displacement, and define \(A_\tau^{\le J},V_\tau^{\le J}\) analogously.
Full-cell locality says that the fair expected full energy change is
nonnegative.  Hence

\[
A_\tau^{>J}
\le V_\tau^{>J}+
\bigl(V_\tau^{\le J}-A_\tau^{\le J}\bigr).
\tag{3.9}
\]

The last bracket divided by four is the fair expected change of
\(\mathcal L_J\).  Every exact child has low-sector mass at most \(U\),
while the current low-sector mass is nonnegative.  Therefore

\[
V_\tau^{\le J}-A_\tau^{\le J}\le4U,
\]

and so

\[
A_\tau^{>J}\le V_\tau^{>J}+4U.
\tag{3.10}
\]

The high-degree Johnson spectral identity gives

\[
\sum_\tau A_\tau^{>J}
\ge2\Lambda\mathcal H_J(F).
\tag{3.11}
\]

Sum (3.10), use (3.11), and divide by \(T_n\) to prove (3.6).  Combining
(3.6) with (2.5) at time one gives (3.7).

Finally,

\[
\frac{T_nU}{\Lambda E_m^*}\longrightarrow0
\]

by (2.11), since \(T_n/\Lambda=O_{A,\gamma}(\sqrt m\log m)\).
Equations (0.8) and (3.7) prove (3.8).  \(\square\)

## 4. Arbitrarily correlated paths: global-step compression

No fairness or frozen-word assumption is used in this section.

Call a realized component cut **empty** if it retains the old side of every
fresh component, **full** if it chooses the new side of every fresh
component, and **proper** otherwise.  An empty cut leaves the current factor
fixed.  A full \(\tau\)-cut sends it to its coordinate relabelling \(\tau F\).

### Theorem 4.1 (exact deletion of global stages)

Let

\[
F_0\longrightarrow F_1\longrightarrow\cdots\longrightarrow F_D
\tag{4.1}
\]

be any realized adaptive path of genuine freshly recomputed transposition
component cuts.  The bridge labels and component choices may have arbitrary
dependence and arbitrary correlation.  If the path has \(P\) proper cuts,
then there is a genuine path

\[
F_0\longrightarrow G_1\longrightarrow\cdots\longrightarrow G_P
\tag{4.2}
\]

consisting only of proper cuts, and a coordinate permutation \(\pi\), such
that

\[
G_P=\pi F_D.
\tag{4.3}
\]

Consequently

\[
\boxed{\mathcal Q_A(G_P)=\mathcal Q_A(F_D).}
\tag{4.4}
\]

Fresh component sizes, properness, and all rowwise lower-shadow data are
preserved under the conjugations used to form (4.2).

#### Proof

Delete an empty stage directly.  Suppose the first remaining global stage
is a full \(\tau\)-cut

\[
X\longrightarrow\tau X.
\]

Conjugate every state and every operation in the later suffix by \(\tau\).
If the next original operation used a transposition \(\sigma\), its
conjugate uses \(\tau\sigma\tau\).  The ownership overlay and the selected
component subset are carried bijectively by \(\tau\), so the conjugated
operation is again a genuine complete component cut and is proper exactly
when the original one was proper.  The conjugated suffix now starts at

\[
\tau(\tau X)=X,
\]

so the full stage has disappeared.  Its new endpoint is \(\tau F_D\), a
coordinate relabelling of the old endpoint.

Iterate.  Every deletion reduces the number of nonproper stages, so the
process terminates with (4.2).  The accumulated conjugations form the
permutation \(\pi\).  Coordinate invariance of every depth floor energy
proves (4.4).  \(\square\)

### Corollary 4.2 (connected stages are spectrally sterile)

If the current \(F/(\tau F)\) overlay is connected, its only two cuts are
empty and full.  Hence that stage can always be deleted as in Theorem 4.1.
In particular, coherent midpoint contraction assigned to a connected stage
is repaid exactly by the fact that the two literal leaves are coordinate
images of equal energy.  No correlation with later component choices turns
that stage itself into a proper shield-breaking operation.

This does not say that its global relabelling has no effect on the names of
later bridges.  Theorem 4.1 says the exact stronger statement: the same
effect is obtained by conjugating those later bridge names, with the global
stage removed.

### Corollary 4.3 (a correlated escape from an all-cell local factor needs two proper cuts)

Suppose \(F\) is locally minimal against every complete component signing
in every transposition cell.  If an arbitrarily correlated adaptive path
ends at \(G\) with

\[
\mathcal Q_A(G)<\mathcal Q_A(F),
\]

then its compressed path contains at least two proper cuts.  Its first
proper cut has energy at least \(\mathcal Q_A(F)\); a later proper cut must
recover that entire preparation height and make a strict additional gain.

#### Proof

By Theorem 4.1, a path with zero proper cuts ends in the coordinate orbit of
\(F\) and has equal energy.  A path with one proper cut compresses to a
single genuine component signing from \(F\), followed only by a coordinate
relabeling of its endpoint.  All-cell locality makes that endpoint energy
at least \(\mathcal Q_A(F)\).  Hence strict decrease requires at least two
proper cuts.  The statement about the first preparation height is the same
locality inequality.  \(\square\)

## 5. Finite-word rigidity against every correlated coupling

The preceding compression has an exact wordwise form.

Fix a word \(w=(\tau_1,\ldots,\tau_T)\).  For
\(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_{r})\in\{0,1\}^{r}\),
write

\[
\rho_r(\varepsilon)=
\tau_r^{\varepsilon_r}\cdots\tau_1^{\varepsilon_1}.
\tag{5.1}
\]

Define the subword-conjugacy set

\[
\mathscr C_w=
\left\{
\rho_{r-1}(\varepsilon)^{-1}\tau_r
\rho_{r-1}(\varepsilon):
1\le r\le T,\ 
\varepsilon\in\{0,1\}^{r-1}
\right\}.
\tag{5.2}
\]

Every member is a coordinate transposition.

### Theorem 5.1 (subword-conjugacy rigidity)

Let \(F\) be an exact factor.  If

\[
F/(\sigma F)\text{ is connected for every }\sigma\in\mathscr C_w,
\tag{5.3}
\]

then every leaf obtained by following the word \(w\), with arbitrary
jointly correlated component choices, is a coordinate image of \(F\).
Consequently

\[
\boxed{
\mathcal Q_A(F_{\rm leaf})=\mathcal Q_A(F)}
\tag{5.4}
\]

for every leaf and every depth window.

#### Proof

Induct on the word position.  Suppose the current leaf is \(\rho F\),
where \(\rho\) is an earlier subword product.  Conjugating its
\(\tau_r\)-overlay by \(\rho^{-1}\) gives the overlay

\[
F/\bigl((\rho^{-1}\tau_r\rho)F\bigr),
\]

which is connected by (5.3).  Thus the current cell has only the empty and
full choices, and the next factor is either \(\rho F\) or
\(\tau_r\rho F\), both coordinate images.  The induction is pathwise, so
no independence, fairness, or lack of correlation is required.  Coordinate
invariance proves (5.4).  \(\square\)

For a two-letter word \((\tau,\sigma)\), condition (5.3) asks for only the
three connected overlays

\[
\boxed{\tau,\qquad\sigma,\qquad\tau\sigma\tau.}
\tag{5.5}
\]

Hence a proposed two-step commutator or correlated cancellation can already
be completely locked by three genuine connected transposition overlays.
For a word whose subword conjugacies cover all transpositions, ordinary
all-transposition rigidity is sufficient, but Theorem 5.1 is strictly
wordwise and assumes only (5.3).

## 6. Proper cuts, rather than letters, disperse private piles

The next theorem strengthens the AB8 escape-depth ledger.  It applies to
arbitrary correlated and adaptive paths.

### Lemma 6.1 (proper-cut token-support growth)

Suppose one labelled group of occurrence tokens is initially supported on
at most \(b\) target values.  Along a realized path with \(P\) proper cuts,
its endpoint tokens are supported on at most

\[
\boxed{b2^P}
\tag{6.1}
\]

target values, independently of the number of empty, full, or connected
transposition stages.

#### Proof

At every component cut, the exact row bijection sends each occurrence token
either from \(S\) to \(S\), or from \(S\) to \(\tau S\).  An empty stage
fixes every token.  A full stage sends every token through the same
permutation \(\tau\), so it maps the current support bijectively and does
not change its cardinality.  At a proper stage, a current support
\(\mathcal U\) is sent into

\[
\mathcal U\cup\tau\mathcal U,
\]

whose cardinality is at most \(2|\mathcal U|\).  Iterate over the \(P\)
proper stages.  \(\square\)

### Theorem 6.2 (AB8 escape counts proper fragmented cuts)

Use the AB8 cage factor \(G_{m,s}\).  Its

\[
L_s=\operatorname{Cat}_{m-s-H-2}
\]

private token groups each contain \(\operatorname{Cat}_H\) selected tokens
and are initially supported on two target values.  Let \(F_{\rm end}\) be
the endpoint of an arbitrary adaptive path, and let \(P\) be the number of
proper cuts in that realized path.  Then (0.13) holds.

Consequently, if \(\mathfrak F_A(F_{\rm end})\le CW\), then

\[
\boxed{
P\ge
2(H-s)-10-
\log_2\!\left(
K_AnH^4\left(C+1+\frac1{2n}\right)
\right).}
\tag{6.2}
\]

#### Proof

Apply Lemma 6.1 with \(b=2\) to each labelled group.  If \(a_X\) are the
endpoint multiplicities of one group, then Cauchy--Schwarz gives

\[
\sum_X\binom{a_X}{2}
\ge
\frac{\operatorname{Cat}_H^2}{2^{P+2}}
-\frac{\operatorname{Cat}_H}{2}.
\tag{6.3}
\]

The labelled groups are disjoint.  Collisions between distinct groups and
unselected occurrences only increase the complete factorial moment.
Summing (6.3), subtracting the exact integral floor \(P_H^{\min}\), and
dividing by the exact normalizer

\[
b_H=\binom{c_H+1}{2}
\]

proves (0.13).

The Catalan estimates used in AB8 are unchanged after replacing its total
step count by \(P\):

\[
\frac{L_s\operatorname{Cat}_H^2}{2^{P+2}}
>
\frac{W2^{2(H-s)-P-10}}{nH^4},
\]

\(b_H\le K_A\),
\(P_H^{\min}\le Wb_H\), and
\(L_s\operatorname{Cat}_H<W/n\).  Rearrangement gives (6.2).
\(\square\)

For \(s=\lfloor H/2\rfloor\) and fixed \(C\), equation (6.2) is (0.14).
The same conclusion applies a fortiori to an endpoint with
\(\mathfrak F_A=O_A(Ht)\), since \(Ht=o(W)\).

## 7. Exact proved/conditional boundary

### Proved

1. The multistep high-sector estimate (2.3) retains the full integer floor,
   uses genuine recomputed ownership components, and selects one literal
   lower-energy leaf whenever (2.6) holds.
2. Once a dynamic cap at the exponential static-shield scale has been
   achieved, it gives an actual \(O(\sqrt m\log m)\)-stage escape from the
   high MSW cell.  Theorem 3.2 proves that this cap cannot hold initially at
   an all-cell local corner.
3. Failure of the block escape forces the exact space-time
   persistence/renewal inequality (0.12), and hence an exponential active
   shield at some freshly recomputed node of the heat tree.
4. Every arbitrary correlated schedule compresses to its proper cuts,
   without changing endpoint energy.
5. A finite subword-conjugacy family of connected overlays blocks every
   correlated signing of that word.
6. The AB8 escape lower bound counts \(\Omega_A(\sqrt m)\) proper
   fragmented cuts, not merely transposition letters.

### Not proved

1. The annealed shield-burnout estimate (2.5) is not known for arbitrary
   high-energy exact factors.
2. Static giant-shield abundance does not imply burnout after a proper cut.
   The same owner rows may be recycled into a new giant component.
3. No theorem forces a spanning or expander word to contain the proper cuts
   counted in (0.14).  Its coherent midpoint may contract while every
   literal stage is connected and hence compressible.
4. Negative cross-time terms from deliberately correlated proper cuts are
   algebraically possible, but no genuine exact-factor routing theorem is
   proved that realizes enough of them simultaneously across the Gaussian
   window.
5. No high-energy exact factor satisfying permanent subword-conjugacy
   rigidity is constructed.

The next exact statement is therefore the following proper-cut shield
burnout lemma.

> **Proper-cut shield burnout (UNPROVED).**  Whenever
> \(\mathcal H_J(F)>K_AHt\), there is a literal decision tree of
> \(T=O_{A,\gamma}(n/J)\) freshly recomputed transposition cells, containing
> the required proper cuts, for which
> \[
> \sum_{r=1}^Ta^{T-r}\mathbb E V_{\tau_r}^{>J}(F_{r-1})
> <4\bigl((1-a^T)\mathcal H_J(F)-U\bigr).
> \tag{7.1}
> \]

By Theorem 2.1, (7.1) immediately emits a literal factor of smaller full
floor energy.  Iterating to a global minimum would prove the fixed-window
bound and enter the audited constant-one route.  Theorem 5.1 and
Theorem 6.2 show exactly what a proof must defeat: finite connected-overlay
corridors and \(\Omega_A(\sqrt m)\) necessary proper fragmentation events.
Constructing a genuine high-energy exact factor for which every such tree
satisfies the reverse inequality would close this multistep lane in the
opposite direction.

Neither alternative is established here, so no constant-one theorem is
claimed.
