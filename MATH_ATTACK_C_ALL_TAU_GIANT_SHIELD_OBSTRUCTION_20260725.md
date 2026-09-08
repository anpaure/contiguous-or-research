# Lane C: all-transposition local minima require giant component shields

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer algebra, or numerical experiment is used.

---

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil L\sqrt m\rceil,
\]

where \(L>0\) is fixed.  At depth \(q\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q},\qquad c_q=\lfloor\lambda_q\rfloor,
\]

and let

\[
\mathcal Q_H(F)
=\sum_{q=1}^H\frac1{c_q}
  \sum_{S\in\binom{[n]}{r_q}}
  (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
\tag{0.1}
\]

be the exact unhalved floor energy of an exact middle wreath factor \(F\).
Write

\[
\beta_q=N_q\{\lambda_q\}(1-\{\lambda_q\}),\qquad
B_H=\sum_{q=1}^H\frac{\beta_q}{c_q},
\tag{0.2}
\]

and

\[
\mathcal E_H(F):=B_H+\mathcal Q_H(F)
=\sum_{q=1}^H\frac{\|\mu_q^F-\lambda_q\mathbf1\|_2^2}{c_q}.
\tag{0.3}
\]

For a coordinate transposition \(\tau\), let \(s_\tau(F)\) be the largest
number of old-side wreath rows in one freshly computed ownership component of
\(F\) versus \(\tau F\).  For an integer \(s\ge0\), define

\[
k_s(F)=\#\{\tau:s_\tau(F)>s\}.
\tag{0.4}
\]

All statements below are for sufficiently large \(m=m(L)\), so that in
particular \(H\le m-2\).  This note proves the following
all-transposition structural theorem.

> **Giant-shield theorem.**  If \(F\) is a component-cut local minimum of
> \(\mathcal Q_H\) for every coordinate transposition, then
> \[
> \boxed{
> k_s(F)\ge
> \left\lceil n-1-
> \frac{sW D_{m,H}}{2\mathcal E_H(F)}
> \right\rceil
> }
> \tag{0.5}
> \]
> for every integer \(s\ge0\), where the exact row-capacity constant is
> \[
> \boxed{
> D_{m,H}
> =\sum_{q=1}^H
> \frac{(m-q)(m+q+1)-2}{c_q}.}
> \tag{0.6}
> \]

Thus a high all-transposition local minimum cannot be shielded only by
microscopic or mesoscopic ownership components.  Quantitatively, let
\(\mathscr X_m\) be the genuine intrinsic \((2\ 3)\)-cell of the canonical
MSW factor used in AB7.  Put

\[
K_L=
\binom{\left\lceil e^{2(L+1)(L+2)}\right\rceil+1}{2},
\qquad
R_m=\frac{4^H}{2048K_L nH^4}-1.
\tag{0.7}
\]

Every corner of \(\mathscr X_m\) has

\[
\mathcal Q_H(F)\ge2WR_m.
\tag{0.8}
\]

In particular, a corner minimizing \(\mathcal Q_H\) on the finite cell is a
genuine prescribed-\((2\ 3)\) floor-energy lock and still satisfies (0.8).
This is the exact floor-corrected starting point whose simultaneous upgrade is
being tested here; it need not be the factorial-objective minimizer selected in
AB7.

Consequently, if a corner of this cell were locally minimal for **every**
transposition, then, for

\[
s_m=\left\lfloor
\frac{(n-1)R_m}{D_{m,H}}
\right\rfloor,
\tag{0.9}
\]

it would satisfy

\[
\boxed{
k_{s_m}(F)\ge
\left\lceil\frac{3(n-1)}4\right\rceil.}
\tag{0.10}
\]

Moreover, with

\[
I_L=\int_0^L\frac{dx}{\lfloor e^{x^2}\rfloor}>0,
\tag{0.11}
\]

one has

\[
\boxed{
s_m\sim
\frac{4^H}{2048K_L I_L H^4m^{5/2}}
=\exp\bigl((L\log4+o_L(1))\sqrt m\bigr).}
\tag{0.12}
\]

The complete native MSW transposition matching has only \(m-1=(n-3)/2\)
edges.  Hence at least

\[
\boxed{\left\lceil\frac{n+3}{4}\right\rceil}
\tag{0.13}
\]

of the transpositions counted in (0.10) are nonnative.  In particular, the
prescribed AB7 cell and the native microscopic packet atlas alone cannot
certify a simultaneous lock: any corner selected there which is in fact
all-transposition locked must obtain its remaining shielding from linear-many
genuinely fresh nonnative components, each with
\(\exp((L\log4+o_L(1))\sqrt m)\) rows.

This is a genuine-factor obstruction with the same all-transposition local
quantifier.  It does **not** prove that such giant shields cannot exist.
Indeed, a connected overlay is one component and makes the direct local
condition vacuous for that transposition.  Thus the precise proved boundary is:

* prescribed-cell, native-packet, bounded-component simultaneous locking is
  impossible;
* all-transposition local minimality in the AB7 cell remains possible only
  through linear-many giant nonnative shields;
* excluding or constructing that giant-shield configuration is the remaining
  exact statement on this lane.

---

## 1. Exact cell quantities

For a fixed transposition \(\tau\), let \(K\) range over the freshly computed
ownership components of \(F\) versus \(\tau F\).  Orient the old and new sides
as \(K\) and \(\tau K\), and at depth \(q\) put

\[
d_{K,q}=\mu_q(K)-\mu_q(\tau K).
\tag{1.1}
\]

Use the weighted norm

\[
\|g\|_H^2=\sum_{q=1}^H\frac{\|g_q\|_2^2}{c_q}.
\tag{1.2}
\]

Then

\[
A_{\tau,H}(F)
=\left\|\sum_Kd_K\right\|_H^2
=\|f(F)-\tau f(F)\|_H^2,
\tag{1.3}
\]

where \(f_q(F)=\mu_q^F-\lambda_q\mathbf1\), and

\[
V_{\tau,H}(F)=\sum_K\|d_K\|_H^2.
\tag{1.4}
\]

Every complete-side signing of the components is another integral exact
factor.  Independent fair signs have mean coherent square \(V_{\tau,H}\).
Therefore, if the current corner minimizes \(\mathcal Q_H\) in its full
\(\tau\)-cell, then

\[
\boxed{A_{\tau,H}(F)\le V_{\tau,H}(F).}
\tag{1.5}
\]

This retains the exact floor: on one cell \(\mathcal Q_H\) differs from one
quarter of the coherent square by a cell-constant term, so no floor residue is
discarded in (1.5).

There is also the universal bound

\[
\boxed{A_{\tau,H}(F)\le4\mathcal E_H(F),}
\tag{1.6}
\]

because every coordinate permutation is orthogonal and
\(\|f_q-\tau f_q\|_2\le2\|f_q\|_2\).

---

## 2. The exact cyclic-row capacity

Fix a depth \(q\) and abbreviate

\[
r=r_q=m-q,
\qquad d_q=r(n-r)=(m-q)(m+q+1).
\tag{2.1}
\]

For a wreath row \(C\), let \(w_{C,q}\) be the indicator of its \(n\)
cyclic rank-\(r\) intervals.

### Lemma 2.1 (exact all-colour row displacement)

If \(2\le r<n/2\), then for every wreath row \(C\),

\[
\boxed{
\sum_\tau\|w_{C,q}-\tau w_{C,q}\|_2^2
=2n(d_q-2),}
\tag{2.2}
\]

where the sum is over unordered coordinate transpositions.

#### Proof

The Johnson graph \(J(n,r)\) has degree \(d_q=r(n-r)\).  The \(n\)
cyclic \(r\)-intervals in one row induce exactly \(n\) Johnson edges:
consecutive cyclic intervals overlap in \(r-1\) coordinates, and when
\(r<n/2\) no other pair of distinct cyclic \(r\)-intervals has overlap
\(r-1\).  Hence the Johnson edge boundary of the row family has size

\[
nd_q-2n=n(d_q-2).
\]

Every Johnson edge is generated by one unique coordinate transposition.  A
boundary edge contributes two unit coordinates to
\(w_{C,q}-\tau w_{C,q}\), and an internal or external edge contributes zero.
Summing over \(\tau\) therefore gives twice the boundary size, proving
(2.2). \(\square\)

For later use, define the rowwise displacement capacity

\[
\mathscr R_{\tau,H}(F)
=\sum_{q=1}^H\frac1{c_q}
  \sum_{C\in F}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{2.3}
\]

Lemma 2.1 and \(|F|=W/n\) give the exact weighted identity

\[
\boxed{
\sum_\tau\mathscr R_{\tau,H}(F)
=2W D_{m,H}.}
\tag{2.4}
\]

In particular, the right side is factor-independent.

### Lemma 2.2 (bounded-component variance capacity)

Let \(\mathcal T\) be any family of transpositions such that every ownership
component of every \(\tau\in\mathcal T\) has at most \(s\) old-side rows.
Then

\[
\boxed{
\sum_{\tau\in\mathcal T}V_{\tau,H}(F)
\le2sW D_{m,H}.}
\tag{2.5}
\]

#### Proof

For one component \(K\),

\[
d_{K,q}=\sum_{C\in K}(w_{C,q}-\tau w_{C,q}).
\]

Cauchy--Schwarz gives

\[
\|d_{K,q}\|_2^2
\le |K|\sum_{C\in K}
\|w_{C,q}-\tau w_{C,q}\|_2^2
\le s\sum_{C\in K}
\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{2.6}
\]

Thus, for every \(\tau\in\mathcal T\),

\[
V_{\tau,H}(F)\le s\mathscr R_{\tau,H}(F).
\tag{2.7}
\]

Sum over \(\tau\in\mathcal T\), enlarge to all transpositions, and apply
(2.4).  Equivalently, rank by rank Lemma 2.1 gives

\[
\sum_{\tau\in\mathcal T}V_{\tau,q}
\le s\frac Wn\,2n(d_q-2)
=2sW(d_q-2).
\tag{2.8}
\]

Multiply by \(1/c_q\) and sum over \(q\le H\).  This is (2.5).
\(\square\)

The rank hypotheses hold throughout the fixed Gaussian window for all
sufficiently large \(m\), since \(H\le m-2\).

---

## 3. Proof of the giant-shield theorem

Every exact factor discrepancy has zero total and zero point margins at each
depth: one wreath row contributes total mass \(n\), and each point lies in
exactly \(r_q\) of its rank-\(r_q\) cyclic intervals.  Thus

\[
f_q\in\bigoplus_{j\ge2}E_{q,j}
\tag{3.1}
\]

in the Johnson harmonic decomposition.

The Johnson Laplacian has eigenvalue \(j(n-j+1)\) on \(E_{q,j}\).  Since
the first possible degree is \(j=2\),

\[
\sum_\tau\|f_q-\tau f_q\|_2^2
=2\langle f_q,L_{J(n,r_q)}f_q\rangle
\ge4(n-1)\|f_q\|_2^2.
\tag{3.2}
\]

After weighting and summing in \(q\),

\[
\boxed{
\sum_\tau A_{\tau,H}(F)
\ge4(n-1)\mathcal E_H(F).}
\tag{3.3}
\]

Let

\[
\mathcal L_s=\{\tau:s_\tau(F)>s\},
\qquad |\mathcal L_s|=k_s(F).
\]

For \(\tau\in\mathcal L_s\), use the universal bound (1.6).  For
\(\tau\notin\mathcal L_s\), all-transposition local minimality and (1.5)
give \(A_{\tau,H}\le V_{\tau,H}\), while Lemma 2.2 bounds the sum of those
variances.  Consequently

\[
\begin{aligned}
4(n-1)\mathcal E_H
&\le\sum_\tau A_{\tau,H}\\
&\le4k_s\mathcal E_H
  +\sum_{\tau\notin\mathcal L_s}V_{\tau,H}\\
&\le4k_s\mathcal E_H+2sWD_{m,H}.
\end{aligned}
\tag{3.4}
\]

Since \(\mathcal E_H>0\) on every nontrivial fixed window, rearrangement
proves (0.5). \(\square\)

Two immediate exact consequences are worth recording.

1.  If every transposition component has at most \(s\) rows, then

    \[
    \boxed{
    \mathcal E_H(F)
    \le\frac{sW D_{m,H}}{2(n-1)}.}
    \tag{3.5}
    \]

    This consequence is not by itself an MWB-scale estimate.  Indeed,
    (5.5) below and \(n-1=2m\) give

    \[
    \frac{sW D_{m,H}}{2(n-1)}
    =\left(\frac{sI_L}{4}+o_L(1)\right)Wm^{3/2},
    \tag{3.6}
    \]

    whereas

    \[
    H\operatorname{Cat}_m
    =\left(\frac L2+o_L(1)\right)Wm^{-1/2}.
    \tag{3.7}
    \]

    Even the formal minimum \(s=1\) therefore leaves a factor
    \((I_L/(2L)+o_L(1))m^2\) in scale.  The theorem is a sharp obstruction
    to the super-mesoscopic AB7 lock, not a standalone proof of MWB.

2.  More generally, if \(\mathcal E_H\) is large, then the obstruction
    cannot be placed in one prescribed transposition.  Inequality (0.5)
    forces linearly many distinct transposition colours to carry large
    components.

The second point is why the theorem is stronger than the observation that the
AB7 \((2\ 3)\)-hierarchy itself has a macroscopic top component.

---

## 4. Exact insertion of the AB7 floor lower bound

AB7 uses the undoubled factorial excess

\[
\Phi_q(F)
=\sum_S\binom{\mu_q^F(S)}2-P_q^{\min}
\]

and the normalization

\[
\mathfrak F_L(F)
=\sum_{q=1}^H
\frac{\Phi_q(F)}{\binom{c_q+1}{2}}.
\tag{4.1}
\]

The relation to (0.1) is exact:

\[
\begin{aligned}
\mathcal Q_H(F)
&=\sum_{q=1}^H\frac{2\Phi_q(F)}{c_q}\\
&=\sum_{q=1}^H(c_q+1)
  \frac{\Phi_q(F)}{\binom{c_q+1}{2}}
\ge2\mathfrak F_L(F).
\end{aligned}
\tag{4.2}
\]

For every corner of the genuine AB7 cell,

\[
\mathfrak F_L(F)
\ge W\left(
\frac{4^H}{2048K_L nH^4}-1
\right)=WR_m.
\tag{4.3}
\]

Equations (4.2)--(4.3) prove (0.8), and hence

\[
\mathcal E_H(F)\ge2WR_m.
\tag{4.4}
\]

Because the full intrinsic cell is finite and closed under every complete
\((2\ 3)\)-component signing, a \(\mathcal Q_H\)-minimum corner exists and is
locally minimal for that prescribed transposition.  No comparison between the
factorial and floor-energy minimizing corners is needed: the lower bound (4.4)
holds at every corner.

Apply (0.5) with \(s=s_m\).  From (0.9),

\[
\frac{s_mWD_{m,H}}{2\mathcal E_H(F)}
\le
\frac{s_mD_{m,H}}{4R_m}
\le\frac{n-1}{4}.
\tag{4.5}
\]

This proves (0.10).

The native coordinate edges are

\[
\mathcal N_m
=\{(2u+2\ \ 2u+3):0\le u\le m-2\},
\qquad |\mathcal N_m|=m-1=\frac{n-3}{2}.
\tag{4.6}
\]

Subtracting their total number from (0.10), and using that \((n-3)/2\) is
an integer, gives

\[
\left\lceil\frac{3(n-1)}4\right\rceil-
\frac{n-3}{2}
=\left\lceil\frac{n+3}{4}\right\rceil,
\]

which proves (0.13).

---

## 5. Floor-corrected asymptotics

The exact load ratio is

\[
\lambda_q
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\tag{5.1}
\]

Uniformly for \(q\le L\sqrt m+1\),

\[
\log\lambda_q
=\frac{q(q+1)}m+O_L(m^{-1/2}).
\tag{5.2}
\]

Therefore the bounded step function \(1/c_q\) has the Riemann-sum limit

\[
\frac1{\sqrt m}\sum_{q=1}^H\frac1{c_q}
\longrightarrow
I_L=\int_0^L\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{5.3}
\]

The finitely many integer crossings of \(e^{x^2}\) are harmless because the
step function is bounded and Riemann integrable.

Also, uniformly on this window,

\[
\frac{(m-q)(m+q+1)-2}{m^2}=1+O_L(m^{-1}).
\tag{5.4}
\]

Combining (5.3)--(5.4) gives the exact floor-sensitive asymptotic

\[
\boxed{
D_{m,H}\sim I_L m^{5/2}.}
\tag{5.5}
\]

Since \(R_m\to\infty\), the floor in (0.9) is negligible.  Substitute
(0.7) and (5.5):

\[
\begin{aligned}
s_m
&\sim
\frac{n-1}{I_L m^{5/2}}
\frac{4^H}{2048K_L nH^4}\\
&\sim
\frac{4^H}{2048K_L I_LH^4m^{5/2}}.
\end{aligned}
\tag{5.6}
\]

Because \(H=L\sqrt m+O(1)\),

\[
\log s_m
=L(\log4)\sqrt m-\frac92\log m+O_L(1),
\tag{5.7}
\]

which proves (0.12).

---

## 6. Precise proved and conditional boundary

The theorem rules out the following proposed upgrade of the prescribed AB7
lock:

* choose a minimum corner of the \((2\ 3)\)-cell;
* conjugate or add only the native contextual size-two packet cells;
* suppose all remaining fresh transposition overlays have polynomially bounded
  components;
* conclude simultaneous local minimality.

Indeed, (0.10)--(0.13) show that every such all-transposition local corner
would require at least \(\lceil(n+3)/4\rceil\) nonnative transpositions with a component
larger than every fixed power of \(m\).

What is **not** proved is equally important.  Large or connected fresh
overlays are not forbidden.  If a \(\tau\)-overlay is connected, its cell has
at most the two globally relabelled antipodes, which have equal energy; that
transposition is automatically locally locked.  Hence neither component count,
cell conjugation, nor lexicographic minimization inside the original high cell
can finish the argument without controlling these giant nonnative shields.

The next exact same-quantifier statement is therefore one of the following.

1. **AB7 giant-shield exclusion:** every corner of \(\mathscr X_m\) has a
   nonnative transposition and a complete-component cut which lowers
   \(\mathcal Q_H\); necessarily the proof must work even when the relevant
   component has \(\exp(\Theta_L(\sqrt m))\) or more rows.
2. **All-transposition counterexample:** construct one corner of
   \(\mathscr X_m\) for which every transposition cell is minimized, thereby
   exhibiting the linear-many giant shields forced by (0.10).

The first would close this high-cell obstruction and advance
\(\mathrm{LM}_L\); the second would refute \(\mathrm{LM}_L\).  The present
report proves the giant-shield dichotomy but neither branch.

---

## 7. Audit checklist

The proof has four normalization points at which a factor-of-two error would
change the conclusion.

1. \(\mathcal Q_H\) is the unhalved floor polynomial, while
   \(\mathcal E_H=B_H+\mathcal Q_H\) is the full centered squared norm.
2. One Johnson boundary edge contributes two, not one, to
   \(\|w_C-\tau w_C\|_2^2\); this is the factor two in (2.2) and (2.4).
3. The Johnson \(E_2\) eigenvalue is \(2(n-1)\), and the norm-difference
   identity contributes a second factor two, giving (3.3).
4. Since \(\binom{c_q+1}{2}=c_q(c_q+1)/2\), the floor energy is exactly
   \((c_q+1)\) times the factorial summand, giving
   \(\mathcal Q_H\ge2\mathfrak F_L\).

The all-transposition local hypothesis is used only for the colours whose
components have at most \(s\) rows.  The remaining \(k_s\) colours are charged
by the unconditional bound \(A_{\tau,H}\le4\mathcal E_H\).  Thus (0.5) does
not silently assume a component-size bound at the large shield colours.
