# BCAP quarantine cascade and boundary-star future-service reduction

**Date:** 2026-08-06  
**Method:** connected switch-graph closure and an abstract killed-service
telescoping inequality; no computation or search  
**Status:** hard row quarantine is refuted as a low-loss repair. A
boundary-star future-service potential would close ANG4 from one exact
birth-and-defect budget, but that budget is not supplied by the current
complete-row theorem.

This note continues
MATH_THEOREM_STABILIZER_SHELL_DECOMPOSITION_OF_SCOV4_20260806.md.

## 1. Hard mate quarantine cascades

Let \(\Gamma=(V,E)\) be a switch graph on a complete row orbit. Call
\(L\subseteq V\) mate-closed when

\[
                         u\in L\quad\Longleftrightarrow\quad v\in L
 \qquad(\{u,v\}\in E).
\tag{1.1}
\]

### Proposition 1.1 (connected closure is all or nothing)

If \(\Gamma\) is connected and \(L\) is mate-closed, then

\[
                         L=\varnothing\quad\text{or}\quad L=V.
\tag{1.2}
\]

Consequently, start with all rows live, physically kill one row, and then
repeatedly quarantine every live row whose switch mate is dead. The final
mate-closed family is empty.

#### Proof

Membership in \(L\) is constant across every edge by (1.1), hence constant
along every path. Connectedness proves (1.2). After one row is killed, the
all-live alternative is unavailable, so the closure is empty.
\(\square\)

Every stabilizer shell graph used by the angular Poincaré theorem is
connected. The conclusion therefore applies even if one keeps only a
spanning tree of switches. Keeping a disconnected switch bank avoids the
cascade but also leaves one free constant on every component, so it does
not prove the shell Poincaré inequality.

Thus the proposed repair

> at the first loss of a stabilizer-switch mate, delete the surviving row

cannot be used inside the analytic candidate family at bounded cost. It
may erase a complete coordinate-orbit component after the first physical
deletion. Post-run quarantine of finitely many **selected macros** is a
different operation and does not restore mate closure of the stopped
future-potential rows.

## 2. The abstract service calculation

Let \(Z_i\ge0\) be a predictable boundary-star energy. Suppose

\[
 \mathbb E_i Z_{i+1}
 \le\left(1-{c_sd\over X_i}\right)Z_i+B_i+E_i,
\qquad B_i,E_i\ge0,
\tag{2.1}
\]

where \(c_sd/X_i\le1\). Here:

* \(B_i\) is the newly born star energy at transition \(i\); and
* \(E_i\) is every failure of the ideal \(d/X_i\) service comparison,
  including density/reference variation.

### Theorem 2.1 (boundary-star service telescope)

Under (2.1),

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{d^2\over X_i}Z_i
 \le {d\over c_s}
 \left(Z_0+\mathbb E\sum_{i<\tau}(B_i+E_i)\right).}
\tag{2.2}
\]

In particular,

\[
 \boxed{
 Z_0+\mathbb E\sum_{i<\tau}(B_i+E_i)
 \le {C\over d}\mathsf A}
\tag{BSTAR}
\]

implies

\[
                         \mathbb E\sum_{i<\tau}
                         {d^2\over X_i}Z_i
 \le C'\mathsf A.
\tag{2.3}
\]

#### Proof

Rearrange (2.1):

\[
 {c_sd\over X_i}Z_i
 \le Z_i-\mathbb E_iZ_{i+1}+B_i+E_i.
\]

Take expectations and sum. The \(Z\)-terms telescope and the terminal
term is nonnegative. Multiply by \(d/c_s\). \(\square\)

For ANG4 the intended choice is

\[
                         Z_i=
 \sum_{x,\sigma}{\operatorname {Ang}_{x,i}(\lambda)\over c_x},
\tag{2.4}
\]

with the exact changing-\(c_x\) correction included in \(E_i\). Thus
BSTAR is a sufficient replacement for the pointwise capacity aperture
BCAP. It permits arbitrarily bad live stars at individual times; only
their future-service birth budget matters.

## 3. A linear private subbank gives the service scale

An asymmetric pair \(A,\tau A\) contains one live survivor row. Its
literal support has \(\Theta(d)\) non-slot resources. On the good
one-resource interval, the first Bonferroni inequality gives

\[
 {\Lambda_i(S_A)\over X_i}
 \ge {1\over X_i}\left(
   \sum_{y\in S_A}Y_y
   -\sum_{\{y,z\}\subseteq S_A}Y_{y,z}\right).
\tag{3.1}
\]

The apparent equality of scale in the two sums is not an obstruction:
one may retain a sufficiently small fixed fraction of a private blocker
bank.

### Lemma 3.1 (private-subbank service)

Suppose a live row \(A\) contains a bank \(R_A\subseteq S_A\) with

\[
 |R_A|\ge c_Bd,\qquad
 Y_y\ge c_0\quad(y\in R_A),\qquad
 Y_{y,z}\le {C_2\over d}\quad(y\ne z\in R_A).
\tag{3.2}
\]

Then there is an absolute \(c_s>0\), depending only on
\(c_B,c_0,C_2\), such that

\[
                         {\Lambda_i(S_A)\over X_i}
 \ge {c_sd\over X_i}.
\tag{3.3}
\]

#### Proof

Choose \(R_A'\subseteq R_A\) with

\[
 |R_A'|=m=\lfloor\epsilon d\rfloor,
\qquad
 0<\epsilon<
 \min\{c_B/2,c_0/(2C_2)\}.
\]

Bonferroni on only this subbank gives

\[
 \begin{aligned}
 \Lambda_i(S_A)
 &\ge\Lambda_i(R_A')\\
 &\ge\sum_{y\in R_A'}Y_y
   -\sum_{\{y,z\}\subseteq R_A'}Y_{y,z}\\
 &\ge c_0m-{C_2\over d}{m\choose2}
 \ge c_sd
 \end{aligned}
\]

for all sufficiently large \(d\). \(\square\)

Thus the weakest \(O(1/d)\) pair cap is quantitatively sufficient; no
\(O(d^{-2})\) internal codegree is needed. The actual service-side gate is
now precise:

* expose, for every asymmetric survivor, a literal bank of
  \(c_Bd\) blockers whose singles stay good and whose internal pairs
  satisfy (3.2); or
* put the failure of that bank into \(E_i\) and prove its cumulative
  BSTAR charge.

The general selected-relation theorem tests marked carrier pairs, not
automatically every pair in every analytic composite row. Therefore
Lemma 3.1 does not silently assert that (3.2) is already available for
the boundary-star family.

## 4. Exact source of star births

For a stabilizer transposition \(\tau\), the angular boundary vector is

\[
 D_{\tau,x}(i)
 =\sum_A\bar\mu_A(i)t_A(i)z_A(x)\chi_A(y)
          (l_A(i)-l_{\tau A}(i)).
\tag{4.1}
\]

It changes only when a transition \(G\) kills exactly one member of a
live pair \(A,\tau A\), or later kills an existing survivor. At the first
event, the literal expected row coefficient is exactly

\[
                         {a_G(i)\over X_i}\mu_i^+(A;G),
\tag{4.2}
\]

the complete-row first-kill tuple.

However, the birth contribution to \(Z_{i+1}\) is the adjoint star square

\[
 \sum_x{1\over c_x'}
 \left(
   \sum_{\substack{A:\text{ toggled by }G}}
      \pm\mu_i^+(A;G)t_Az_A(x)\chi_A(y)
 \right)^2,
\tag{4.3}
\]

together with its linear cross against the pre-existing star. The
complete-row conjugation theorem prices each full primal row switch with
coefficient (4.2). It does not identify the square of the sum in (4.3)
with that diagonal ledger.

Consequently the exact remaining birth statement is

\[
 \boxed{
 \mathbb E\sum_{i<\tau}
 \left[
   Z_{i+1}
   -\left(1-{c_sd\over X_i}\right)Z_i
 \right]_+
 \le {C\over d}\mathsf A,}
\tag{BIRTHSTAR}
\]

after the predictable density/reference correction has been separated.
BIRTHSTAR implies BSTAR with \(E_i=0\); a signed version may split the
same positive part between \(B_i\) and \(E_i\).

### 4.1 Adjoint star coalescing is deterministic

Although the exact first-kill coefficient is still to be matched, the
same-output cross terms in (4.3) do not require a fourth moment.

Let \(\mathcal T\) be the rows toggled by one transition and one oriented
shell generator. Put

\[
 B_x=\sum_{A\in\mathcal T}\nu_Az_A(x),
\qquad
 D_x=\sum_{A\in\mathcal T}\epsilon_A\nu_Az_A(x),
\qquad |\epsilon_A|\le1,
\tag{4.5}
\]

where \(\nu_A\) is the literal post-update coefficient, including the
bounded multiplier \(t_A\). Let

\[
                         g_x=\sum_{A\ {\rm live}}\nu_Az_A(x),
\qquad c_x=\beta_TY_x,
\qquad f_x={g_x\over c_x}-1.
\tag{4.6}
\]

Assume \(\mathcal T\) is a subfamily of the live rows, so
\(0\le B_x\le g_x\).

### Lemma 4.1 (actual-vector star inequality)

If \(n_T(A)=\sum_xz_A(x)\le C_nd\), then

\[
 \boxed{
 \sum_x{D_x^2\over c_x}
 \le Cd\sum_{A\in\mathcal T}\nu_A
      +{C\over d}\sum_{A\in\mathcal T}
                 \nu_A(K_Tf)(A)^2.}
\tag{4.7}
\]

#### Proof

Since \(|D_x|\le B_x\le g_x\),

\[
 {D_x^2\over c_x}\le {g_xB_x\over c_x}
 =(1+f_x)B_x.
\tag{4.8}
\]

Sum \(x\) and interchange the incidence sums:

\[
 \sum_x(1+f_x)B_x
 =\sum_{A\in\mathcal T}\nu_A
       \bigl(n_T(A)+(K_Tf)(A)\bigr).
\tag{4.9}
\]

For every real \(u\),

\[
                         u\le {d\over2}+{u^2\over2d}.
\tag{4.10}
\]

Use (4.10) on \(u=(K_Tf)(A)\) and the row-size bound.
\(\square\)

Thus star coalescing would reduce to two diagonal birth ledgers:

\[
 \boxed{
 \begin{aligned}
 \operatorname {BMASS}:&\quad
 \mathbb E\sum_{\rm births}\sum_{A\in\mathcal T}\nu_A
 \le {C\over d^2}\mathsf A,\\
 \operatorname {BSCORE}:&\quad
 \mathbb E\sum_{\rm births}\sum_{A\in\mathcal T}
       \nu_A(K_Tf)(A)^2
 \le C\mathsf A.
 \end{aligned}}
\tag{4.11}
\]

Indeed (4.7) and (4.11) give total born star energy
\(O(\mathsf A/d)\), exactly the BIRTHSTAR scale.

BSCORE has the same complete-row score as blocker conjugation. BMASS is
the score-free absolute boundary count. The next proposition shows that
BMASS is not merely unproved: it is false at the required scale in the
generic product residual. Therefore Lemma 4.1 is a correct deterministic
upper bound but not the route to BIRTHSTAR.

### 4.2 Absolute boundary mass is generically macroscopic

Take a coordinate-mate pair \(A,\tau A\), each with \(R\) physical
resources and overlap \(s=|A\cap\tau A|\). Retain resources independently
with probability \(p\), and give a surviving row the compensated
coefficient \(wp^{-R}\).

### Proposition 4.2 (BMASS obstruction)

The expected absolute asymmetric coefficient is

\[
 \boxed{
 \mathbb E\left[
 wp^{-R}\left|
 {\bf1}_{\{A\ {\rm live}\}}-
 {\bf1}_{\{\tau A\ {\rm live}\}}
 \right|\right]
 =2w(1-p^{R-s}).}
\tag{4.12}
\]

For every nonidentical pair at separator density \(p\asymp1/d\), this is
\(\Theta(w)\). Hence an orbit average containing a positive proportion of
nonidentical mate pairs has absolute boundary mass comparable to its
complete base mass, not \(O(d^{-2})\) times that mass.

#### Proof

Exactly one row survives with probability

\[
 2\left(p^R-p^{2R-s}\right)
 =2p^R(1-p^{R-s}).
\]

Multiply by \(wp^{-R}\). \(\square\)

The small object is the **signed covariance** after summing the orbit,
not its absolute variation. Any boundary-star potential must retain the
signs \(l_A-l_{\tau A}\) and their product-residual cancellation through
the birth calculation. Replacing them by BMASS loses the decisive
cancellation before service is applied.

## 5. Proof boundary

The two proposed process modifications now have exact verdicts.

1. **Hard mate quarantine fails:** connected shell closure cascades from
   one killed row to the whole switch component.
2. **Future service is viable only in signed form:** it converts ANG4 to
   a signed boundary-pair birth covariance plus the literal
   private-subbank service comparison (3.3). The positive BMASS
   relaxation is refuted by Proposition 4.2.

Neither ordinary good loads, equal complete-orbit coefficients, nor the
current diagonal complete-row first-kill estimate proves (4.3). The
smallest remaining analytic theorem is therefore:

\[
\boxed{\text{coefficient-faithful signed star-covariance birth}
 \quad+\quad \text{its }d/X\text{ survivor service}.}
\]

This formulation does not require every live star to satisfy BCAP
pointwise.
