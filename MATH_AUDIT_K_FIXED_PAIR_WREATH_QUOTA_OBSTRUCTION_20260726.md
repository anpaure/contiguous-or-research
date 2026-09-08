# Audit of the fixed-pair wreath quota obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver,
entropy heuristic, or web input is used.

Audited source:
`MATH_ATTACK_K_FIXED_PAIR_WREATH_QUOTA_OBSTRUCTION_20260726.md`.

## 0. Verdict

Post-audit status: the source report now includes the cemetery type,
separates the one- versus two-partial-orbit scopes, and states the
complement rank directly.  The corrections listed below have therefore
been applied.

The principal conclusion survives audit:

* the odd hyperoctahedral orbit classification is exact;
* the fixed part of the fractional balanced-quota polytope is nonempty;
* the integral whole-orbit obstruction is only arithmetic;
* the sharp orbit-mass projection is
  \(\max\{D^-,D^+\}\), with no missing factor two;
* at \(q=A\sqrt m+O(1)\), the native fixed-pair type law has an
  \(\Omega_A(W)\) factorial-floor defect; and
* repairing that defect requires \(\Omega_A(W)\) ownerwise transport
  between native types.

The Gaussian normalizations, including (5.8)--(5.12) and the case in
which \(e^{A^2}\) is an integer, are correct.

There is, however, one substantive finite-exactness correction and two
scope corrections.

1. A middle source type with fewer than \(q\) split pairs has no
   distinct-direction pair-face depth-\(q\) window.  Thus the displayed
   vector \(V_{\varepsilon,f}\), when indexed only by genuine target
   orbits, does not have total mass \(W\).  The exact finite projection
   must either add a zero-capacity cemetery type carrying the ineligible
   source mass, or count every such source as compulsory cross-type
   leakage.  This changes no Gaussian constant because the ineligible
   mass is \(e^{-\Omega_A(m)}W\).
2. Breaking symmetry inside one target orbit proves an
   \(O_A(W/\sqrt m)\) repair only for the bare balanced-quota total.  It
   does not automatically produce an integral ordinary-coordinate
   one-design.  With the two infinity-sector totals prescribed, at most
   one partial orbit in each sector suffices for those two totals, but
   ordinary point regularity remains an additional labelled condition.
3. The complement of a rank-\((m-q)\) target has rank
   \(m+1+q\).  The sentence assigning it to "upper depth \(q\)" versus
   "upper depth \(q-1\)" is convention-dependent and should be removed
   unless that upper-depth convention is defined explicitly.

After the first correction is made, the report is theorem-grade.  In
particular, the coefficient-one no-go is unaffected.

## 1. Orbit classification and exact counts

Let

\[
 \Omega=\{\infty\}\sqcup P_1\sqcup\cdots\sqcup P_m,
 \qquad G_m=C_2^m\rtimes S_m.
\]

For a rank-\((m-q)\) set, write \(\varepsilon\) for infinity membership
and \(f,h,e\) for its numbers of full, split, and empty pairs.  Then

\[
 h=m-q-\varepsilon-2f,
 \qquad e=f+q+\varepsilon.
\]

Pair permutations align the three pair classes, and internal swaps align
the chosen endpoint in every split pair.  Thus \((\varepsilon,f)\) is a
complete orbit invariant.  The stabilizer order is

\[
 2^{2f+q+\varepsilon}f!(f+q+\varepsilon)!
 (m-q-\varepsilon-2f)!,
\]

so the source formula

\[
 T_{\varepsilon,f,q}
 =\frac{m!2^{m-q-\varepsilon-2f}}
 {f!(f+q+\varepsilon)!(m-q-\varepsilon-2f)!}
\]

is exact.  Substitution \(q=0\) gives the displayed
\(V_{\varepsilon,f}\).  The sums over valid indices are respectively
\(N_q=\binom{2m+1}{m-q}\) and
\(W=\binom{2m+1}{m}\).

Complementation sends

\[
 (\varepsilon,f,h,e)\longmapsto(1-\varepsilon,e,h,f)
\]

and preserves orbit size.  Its rank is exactly \(m+1+q\).

## 2. Fractional quotas and the nested deletion kernel

Put

\[
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad \rho_q=W-c_qN_q.
\]

The fixed fractional quota equations are

\[
 0\le x_{\varepsilon,f}\le1,
 \qquad
 \sum_{\varepsilon,f}T_{\varepsilon,f,q}x_{\varepsilon,f}
 =\rho_q.
\]

The constant assignment \(x_{\varepsilon,f}=\rho_q/N_q\) satisfies
them exactly.  This remains correct despite the fact that \(G_m\) has
two coordinate orbits: the assignment is constant across both infinity
sectors, hence is the full-rank barycentre, not merely a separate
sectorwise average.

The simultaneous deletion calculation also checks.  If
\(|S|=m-q\), there are

\[
 \binom{m+1+q}{q}
\]

middle sets together with an unordered deleted \(q\)-set leading to
\(S\), while each middle set has \(\binom mq\) possible deleted sets.
Consequently the load is

\[
 \frac{\binom{m+1+q}{q}}{\binom mq}
 =\frac{\binom{2m+1}{m}}{\binom{2m+1}{m-q}}
 =\frac W{N_q}.
\]

A single random ordering of each middle set couples these deletion
kernels monotonically in \(q\).  This is a valid fractional nested
certificate; it is not a deterministic equivariant selector.

The deterministic-selector obstruction (2.19) is also correct.  The
stabilizer orbits inside a middle set have sizes
\(\varepsilon,2f,h\).  Hence an equivariantly deleted set must have size

\[
 \alpha\varepsilon+2\beta f+\gamma h,
 \qquad \alpha,\beta,\gamma\in\{0,1\}.
\]

For \(\varepsilon=0,f=e=q,h=m-2q\) and \(m>3q\), none of the nonzero
such sums equals \(q\).

## 3. Integral orbit arithmetic

The whole-orbit subset-sum criterion is exact for a pointwise
\(G_m\)-fixed high family.  The cyclic pair-label argument also gives the
correct divisors

\[
 D_\varepsilon=\frac m{\gcd(m,m-q-\varepsilon)},
 \qquad
 D=\frac m{\gcd(m,q(q+1))}.
\]

Indeed, a cyclic orbit of length \(L\mid m\) has repetition number
\(m/L\), which divides the number \(m-q-\varepsilon\) of selected
paired coordinates.  Hence \(D_\varepsilon\mid L\), and consequently
\(D_\varepsilon\) divides every full \(G_m\)-orbit in that sector.

For \(m=p\) an odd prime and \(1\le q\le p-2\), both selected paired
coordinate counts lie strictly between zero and \(p\).  Every orbit size
is therefore divisible by \(p\).  Lucas's theorem gives

\[
 \binom{2p+1}{p}\equiv2\pmod p,
 \qquad
 N_q\equiv0\pmod p,
 \qquad
 \rho_q\equiv2\pmod p.
\]

Thus neither a total-mass-\(W\) invariant integral histogram nor a
whole-orbit invariant balanced high family exists.  This is an exact
infinite-family obstruction, but it supplies no linear stability: one
partial orbit has only \(O_A(W/\sqrt m)\) targets in the Gaussian
window.

For a complete cyclic length-\(k\) histogram, where \(k=m-q\), the
infinity sector masses are

\[
 M_1=k\operatorname{Cat}_m,
 \qquad M_0=(2m+1-k)\operatorname{Cat}_m.
\]

The high counts (2.17) follow exactly by subtracting the constant floor:

\[
 h_1=\frac{k\rho_q}{2m+1},
 \qquad
 h_0=\frac{(2m+1-k)\rho_q}{2m+1}.
\]

The separate subset sums (2.18) are therefore necessary and sufficient
for an orbit-union quota having the prescribed two sector totals.
Ordinary-coordinate point regularity is automatic fractionally, but not
for an arbitrary integral partial orbit.

## 4. Audit of the sharp projection formula

Let orbit sizes be \(T_j\), prescribed masses be \(M_j\), and put

\[
 y_j=M_j-cT_j,
 \quad
 D^-=\sum_j(-y_j)_+,
 \quad
 D^+=\sum_j(y_j-T_j)_+.
\]

Clamping \(y_j\) to \([0,T_j]\) changes its total from \(\rho\) to
\(\rho+D^- -D^+\).  Restoring total \(\rho\) costs
\(|D^--D^+|\) further units.  Therefore the unhalved \(\ell^1\) cost is

\[
 D^-+D^++|D^--D^+|=2\max\{D^-,D^+\},
\]

and hence

\[
 \min\frac12\|\mu-\beta\|_1=\max\{D^-,D^+\}.
\]

All data are integral, so the correction can be made integrally.  Inside
each orbit, surplus can be added to arbitrary entries and deficit can be
removed from the nonnegative quota entries.  Thus equality in the
orbit-relaxed problem is genuine.  There is no missing factor two.

If the two infinity-sector totals are separately fixed, the same proof
must be run in each sector, giving

\[
 \sum_{\varepsilon=0}^1
 \max\{D^-_\varepsilon,D^+_\varepsilon\},
\]

as stated.  Further labelled point constraints are outside this orbit
relaxation.

## 5. The ineligible-source correction

For a middle source type \((\varepsilon,f)\), put

\[
 h^0_{\varepsilon,f}=m-\varepsilon-2f.
\]

A depth-\(q\) pair-face window using distinct directions exists only if
\(h^0_{\varepsilon,f}\ge q\).  Equivalently, only then is
\((\varepsilon,f)\) a valid rank-\((m-q)\) target type.  Define

\[
 E_{m,q}:=
 \sum_{\varepsilon,f:\ h^0_{\varepsilon,f}<q}
 V_{\varepsilon,f}.
\]

Then

\[
 \sum_{\varepsilon,f:\ h^0_{\varepsilon,f}\ge q}
 V_{\varepsilon,f}=W-E_{m,q},
\]

not \(W\).  Consequently the sentence "taking \(M=V\) in Theorem 3.1"
is not literally valid if the index set contains only genuine target
orbits.

There are two equivalent exact repairs.

* Add a formal cemetery type \(\partial\) with
  \(T_\partial=0\) and \(M_\partial=E_{m,q}\).  Then the total prescribed
  mass is \(W\), and the corrected excess term is
  \[
   \widehat D^+
   =E_{m,q}+
    \sum_{h^0_{\varepsilon,f}\ge q}
      \bigl(V_{\varepsilon,f}-(c_q+1)T_{\varepsilon,f,q}\bigr)_+,
  \]
  while \(\widehat D^-\) is the displayed deficient-orbit sum over
  valid types.  The sharp formal projection is
  \(\max\{\widehat D^-,\widehat D^+\}\).
* Alternatively, declare every ineligible source to be a compulsory
  nonnative start.  Then it contributes to the leakage variable in
  Section 6, and all native type equations are asserted only on eligible
  sources.

In either formulation there is no complete all-native literal histogram
unless \(E_{m,q}=0\).  The source report itself already detects a larger
odd-sector incompatibility, so its intended object is the ideal native
ledger followed by leakage repair, not an actually existing all-native
factor.

For \(q=A\sqrt m+O(1)\), Stirling's inequalities applied to (1.8) show

\[
 E_{m,q}=e^{-\Omega_A(m)}W.
\]

Indeed the split-pair count is \(m/2+O(\sqrt m)\) on the central source
mass, whereas \(h^0<q=O(\sqrt m)\) is a linear large deviation.  Thus
the cemetery correction is invisible in every limit in Section 5 and
in the \(\Omega_A(W)\) conclusion.

The separate infinity-sector mismatch is exact and much larger than
this tail.  Native sources have sector masses

\[
 m\operatorname{Cat}_m,
 \qquad (m+1)\operatorname{Cat}_m,
\]

whereas a complete length-\((m-q)\) interval ledger has masses

\[
 (m-q)\operatorname{Cat}_m,
 \qquad (m+1+q)\operatorname{Cat}_m.
\]

Therefore at least

\[
 q\operatorname{Cat}_m=\frac q{2m+1}W
\]

starts must cross the infinity sectors.  At Gaussian depth this is
\(O_A(W/\sqrt m)=o(W)\), so it does not weaken the linear full-type
obstruction.

## 6. Gaussian normalization and exact constants

Let \(q=A\sqrt m+O(1)\), and under the target law define

\[
 Z_m=\frac{4(f-f_{*,\varepsilon})}{\sqrt m},
 \qquad
 f_{*,\varepsilon}
 =\frac{(m-q-\varepsilon)^2}{4m}+O(1).
\]

The ratio of consecutive target masses has logarithmic second difference
\(-16/m+o(1/m)\), so \(Z_m\Rightarrow N(0,1)\).  Directly from the
factorial ratio,

\[
 \lambda_{\varepsilon,f,q}
 =\frac{V_{\varepsilon,f}}{T_{\varepsilon,f,q}}
 =2^q\frac{(f+q+\varepsilon)!}{(f+\varepsilon)!}
       \frac{(m-q-\varepsilon-2f)!}
            {(m-\varepsilon-2f)!},
\]

and its logarithm satisfies

\[
 \log\lambda_{\varepsilon,f,q}
 =-A^2+2AZ_m+o(1)
\]

uniformly on bounded \(Z_m\)-windows.  Also

\[
 \frac W{N_q}\longrightarrow e^{A^2}.
\]

The constants (5.8)--(5.9) are correctly normalized per target mass
\(N_q\).  If \(Z\sim N(0,1)\),

\[
 L=e^{-A^2+2AZ},
 \qquad z_a=\frac{A^2+\log a}{2A},
\]

then

\[
 \mathbb E(c-L)_+
 =c\Phi(z_c)-e^{A^2}\Phi(z_c-2A),
\]

and

\[
 \mathbb E(L-c-1)_+
 =e^{A^2}\Phi(2A-z_{c+1})
  -(c+1)\Phi(-z_{c+1}).
\]

The positive-part convergence on the upper tail is justified as follows.
Under the target law,

\[
 \mathbb E\lambda_{\varepsilon,f,q}
 =\frac{W-E_{m,q}}{N_q}longrightarrow e^{A^2}
 =\mathbb E L.
\]

Together with convergence in distribution of the nonnegative likelihood
ratios, convergence of first moments gives the required uniform
integrability.  The lower positive part is bounded by \(c\).

If \(e^{A^2}\notin\mathbb Z\), the floor is eventually constant.  If
\(e^{A^2}=K\in\mathbb Z\), convergence of \(W/N_q\) implies only

\[
 c_q\in\{K-1,K\}
\]

for all sufficiently large \(m\).  Taking the minimum over these two
values, as in (5.11)--(5.12), is exactly the correct floor-edge treatment.
Both lognormal tails have positive probability, so every candidate
constant is strictly positive.  Finally \(N_q/W\to e^{-A^2}\), proving
the normalization in \(\kappa_A\).

For \(c=1\), multiplying the per-\(N_q\) deficit by
\(N_q/W\to e^{-A^2}\) gives

\[
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2),
\]

exactly as stated.

## 7. Leakage stability and implication scope

After adjoining the cemetery cell, let \(\widehat V\) be the complete
ideal native mass vector.  If \(L_q\) starts are nonnative, including all
ineligible sources, then

\[
 \frac12\|M-\widehat V\|_1\le L_q.
\]

Distance to the balanced-capacity box inside the total-mass hyperplane is
one-Lipschitz in half-\(\ell^1\).  Hence

\[
 \frac12\|\mu_q-\beta_q\|_1
 \ge
 \max\{\widehat D^-_{m,q},\widehat D^+_{m,q}\}-L_q.
\]

Since the cemetery correction is \(o(W)\) at Gaussian depth, the source
report's bound

\[
 \frac12\|\mu_q-\beta_q\|_1
 \ge(\kappa_A-o(1))W-L_q
\]

is correct.  In particular, \(o(W)\) cross-type transport leaves an
\(\Omega_A(W)\) quota defect, and any native-frame construction with
\(o(W)\) quota overload must move \((\kappa_A-o(1))W\) starts between
types.

This implication closes only the architecture in which all but \(L_q\)
starts obey the diagonal law

\[
 (\varepsilon,f)\longmapsto(\varepsilon,f).
\]

It does not obstruct mixtures of pair frames or exact nonlocal trades that
move positive-density mass between these orbit types.  Nor does fractional
quota feasibility prove chronology, ownership completion, or literal
contiguous-OR realizability.

## 8. Required source corrections

The source can be made fully exact with the following changes.

1. In (0.5), (0.6), and the sentence following (4.2b), either include the
   formal cemetery type and its excess \(E_{m,q}\), or state the result
   only for the ideal eligible ledger and route all ineligible sources
   through \(L_q\).
2. Replace "taking \(M=V\) in Theorem 3.1" by the cemetery-augmented
   application above.
3. Restrict the one-partial-orbit \(O_A(W/\sqrt m)\) conclusion to bare
   quota totals.  For prescribed infinity-sector totals one may use at
   most one partial orbit per sector; full labelled point regularity is
   not proved by this greedy argument.
4. State directly that lower rank \(m-q\) complements to upper rank
   \(m+1+q\), avoiding the undefined depth-index shift.

With these corrections, the report's central theorem and every
constant-one implication pass.
