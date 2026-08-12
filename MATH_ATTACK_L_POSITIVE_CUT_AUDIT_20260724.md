# Independent audit: Lane L positive cuts

## Verdict

The main parity-floor identities, factor-of-two conventions, weighted
component-cut formula, cut-locality equivalence, extension-fan identity,
cyclic-distance averages, first-shadow obstruction histogram, and
\(1/(2A)\) high-energy ratio are valid.

The report nevertheless needs three substantive corrections.

1. The proved \(O_A(W)\)-per-rank estimate in Section 3 is an expected
   \(L^1\)-displacement estimate.  It does not bound the quadratic parity
   restitution or locking term by \(O_A(W)\).  That conversion is
   **unsupported**.
2. Connected overlays for every transposition give one sufficient route to
   a counterexample to \(LM_A\), but they are not necessary.  A high-energy
   cut-local factor may have disconnected overlays with every weighted cut
   nonpositive.  The opening “precise dichotomy” and the final statement
   that a counterexample “requires” the rigid connected realization are too
   strong.
3. The canonical MSW factor is known to have an explicit hereditary
   subfamily of at least \(\operatorname{Cat}_{m-4}\) depth-one holes.  It is
   not known to have only that many holes.  The report's upper-sounding
   wording is false and must be replaced by a statement about the certified
   subfamily alone.

There are also several scope and terminology corrections: the weighted
parity functionals need not be integer-valued; the occurrence-pair statistic
describes fair independent signs rather than optimal correlated signs;
“every altered signing” must exclude the two constant antipodal signings;
the \(\Theta(W)\) diagonal-variance statement is uniform in the fixed
Gaussian window but not over all \(2\le r\le m\); and “every legal move”
must mean the transposition-component move class.

With these corrections, the final status remains

\[
\boxed{LM_A\text{ is neither proved nor refuted}.}
\]

## 1. Setup required by the parity calculation

Fix \(m\ge2\), \(1\le q\le H_A\), and a coordinate transposition
\(\tau\).  The parity argument silently uses two previously proved structural
facts:

1. \(F\cap\tau F=\varnothing\) for a coordinate transposition;
2. every ownership component has right side \(R_K=\tau L_K\).

Let \(a_{K,q}\) be the depth-\(q\) histogram of the old, or left, side of
component \(K\).  For an unordered nonfixed \(\tau\)-orbit

\[
p=\{S,T=\tau S\}
\subseteq\binom{[n]}{m-q},
\]

choose the displayed orientation and put

\[
x_K=a_{K,q}(S),\qquad
y_K=a_{K,q}(T),\qquad
z_K=x_K-y_K.
\]

Write

\[
X=\sum_Kx_K=\mu_q(S),\qquad
Y=\sum_Ky_K=\mu_q(T),
\]

\[
z=X-Y,\qquad
\ell=X+Y,\qquad
\pi=\ell\bmod2.
\]

Let \(\varepsilon_K=+1\) select the old side of component \(K\) and
\(\varepsilon_K=-1\) select its new side.  Component equivariance then gives

\[
u_p(\varepsilon)=\sum_K\varepsilon_Kz_K,
\]

and exactly

\[
\mu_{q,F_\varepsilon}(S)
=\frac{\ell+u_p(\varepsilon)}2,\qquad
\mu_{q,F_\varepsilon}(T)
=\frac{\ell-u_p(\varepsilon)}2.
\tag{1.1}
\]

Thus every signing preserves the pair sum \(\ell\).  Moreover,

\[
z_K\equiv x_K+y_K\pmod2,\qquad
\varepsilon_K\equiv1\pmod2,
\]

so

\[
u_p(\varepsilon)\equiv\ell\pmod2.
\tag{1.2}
\]

Consequently

\[
\frac{u_p(\varepsilon)^2-\pi}{2}
\in\mathbb Z_{\ge0}.
\tag{1.3}
\]

Fixed targets \(S=\tau S\) are immutable and contribute zero to every energy
difference.  The report should explicitly state that its sums over \(p\)
range over unordered nonfixed target pairs.

**Classification:** the parity assertions are **valid** after these setup
facts and ranges are made explicit.

## 2. Full-energy normalization and factors of two

The report uses the full floor energy

\[
\mathcal Q_A(F)
=\sum_{q\le H_A}\frac{Q_q(F)}{c_q}
=2\Psi_A(F).
\tag{2.1}
\]

For a pair with loads \(a+b=\ell\) and difference \(d=a-b\),

\[
\begin{aligned}
&(a-c_q)(a-c_q-1)+(b-c_q)(b-c_q-1)\\
&\qquad=
\frac{\ell^2+d^2}{2}
-(2c_q+1)\ell
+2c_q(c_q+1).
\end{aligned}
\tag{2.2}
\]

The pair sum is fixed under component signing, so (2.2) yields

\[
\mathcal Q_A(F_\varepsilon)-\mathcal Q_A(F)
=
\frac12\sum_{q,p}
\frac{u_p(\varepsilon)^2-z_p^2}{c_q}.
\tag{2.3}
\]

Define

\[
\mathfrak G_\tau
=\frac12\sum_{q,p}\frac{z_p^2-\pi_p}{c_q},
\qquad
\mathfrak R_\tau(\varepsilon)
=\frac12\sum_{q,p}
\frac{u_p(\varepsilon)^2-\pi_p}{c_q}.
\tag{2.4}
\]

Then

\[
\boxed{
\mathcal Q_A(F_\varepsilon)-\mathcal Q_A(F)
=
\mathfrak R_\tau(\varepsilon)-\mathfrak G_\tau.
}
\tag{2.5}
\]

There is no factor-of-two error in (2.5).

The report calls this an “exact integral identity.”  The identity is exact
for integral component signings, and each unweighted numerator
\((u^2-\pi)/2\) is a nonnegative integer.  The weighted quantities
\(\mathfrak G_\tau,\mathfrak R_\tau\), however, need not be integers because
of the factors \(c_q^{-1}\).  The terminology should be corrected.

### Hilbert-space conversion

Define

\[
\langle h,g\rangle_A
=\sum_{q\le H_A}
\frac{\langle h_q,g_q\rangle_2}{c_q}.
\tag{2.6}
\]

Let

\[
d_{K,q}=a_{K,q}-\tau a_{K,q},
\qquad
d=\sum_Kd_K,
\]

\[
A_\tau=\|d\|_A^2,\qquad
R_\tau^{\mathrm{Hilb}}(\varepsilon)
=\left\|\sum_K\varepsilon_Kd_K\right\|_A^2,
\]

and

\[
B_\tau^{\mathrm{par}}
=\frac12\sum_{q,p}\frac{\pi_p}{c_q}.
\]

Each moved pair contributes the two coordinates \((z,-z)\), so

\[
\boxed{
\mathfrak G_\tau=\frac{A_\tau}{4}-B_\tau^{\mathrm{par}},
\qquad
\mathfrak R_\tau(\varepsilon)
=\frac{R_\tau^{\mathrm{Hilb}}(\varepsilon)}4
-B_\tau^{\mathrm{par}}.
}
\tag{2.7}
\]

Thus

\[
\boxed{
\mathcal Q_A(F_\varepsilon)-\mathcal Q_A(F)
=
\frac{R_\tau^{\mathrm{Hilb}}(\varepsilon)-A_\tau}{4}.
}
\tag{2.8}
\]

Since \(\mathcal Q_A=2\Psi_A\),

\[
\boxed{
\Psi_A(F_\varepsilon)-\Psi_A(F)
=
\frac{R_\tau^{\mathrm{Hilb}}(\varepsilon)-A_\tau}{8}.
}
\tag{2.9}
\]

For a switched component set \(I\), take \(\varepsilon=-1\) on \(I\) and
\(+1\) on \(I^c\).  Then

\[
R_\tau^{\mathrm{Hilb}}(\varepsilon)-A_\tau
=-4\langle d_I,d_{I^c}\rangle_A,
\]

so

\[
\boxed{
\mathcal Q_A(F_I)-\mathcal Q_A(F)
=-\langle d_I,d_{I^c}\rangle_A,
}
\tag{2.10}
\]

whereas

\[
\boxed{
\Psi_A(F_I)-\Psi_A(F)
=-\frac12\langle d_I,d_{I^c}\rangle_A.
}
\tag{2.11}
\]

This reconciles the apparent factor difference between Lane L and the
trade/Markov report: Lane L uses the full energy \(\mathcal Q_A\), while the
earlier \(-1/2\) cut formula uses the half-energy \(\Psi_A\).

Also \(F_{-\varepsilon}=\tau F_\varepsilon\), hence the two antipodal
children have equal energy and

\[
\mathcal Q_A(F_\varepsilon)+\mathcal Q_A(F_{-\varepsilon})
=
2\mathcal Q_A(F)
+\frac{R_\tau^{\mathrm{Hilb}}(\varepsilon)-A_\tau}{2}.
\tag{2.12}
\]

**Classification:** all displayed parity and factor-of-two identities are
**valid**; only the integer-valued terminology requires correction.

## 3. Cut-locality equivalence

The all-\(+\) signing is \(F\) itself and satisfies

\[
\mathfrak R_\tau(+)=\mathfrak G_\tau.
\]

Therefore

\[
\boxed{
F\text{ is }\tau\text{-cut-local}
\iff
\mathfrak G_\tau
=\min_\varepsilon\mathfrak R_\tau(\varepsilon).
}
\tag{3.1}
\]

Equivalently, with

\[
\beta_\tau
=\min_\varepsilon
R_\tau^{\mathrm{Hilb}}(\varepsilon),
\]

\[
\boxed{
F\text{ is }\tau\text{-cut-local}
\iff
\beta_\tau=A_\tau.
}
\tag{3.2}
\]

This is an aggregate equality over the entire fixed window for one common
component signing.  It is not a separate equality for each rank or target
pair.  The sentence that all ideal pair-balancing gain is lost to component
bundling is valid only in this aggregate sense.

**Classification:** the local-minimum equivalence is **valid**, with the
aggregate/common-signing quantifier made explicit.

## 4. Occurrence expansions and their correct scope

The first occurrence identity is

\[
\boxed{
\frac{z^2-\pi}{2}
=
\left\lfloor\frac\ell2\right\rfloor
+\binom X2+\binom Y2-XY.
}
\tag{4.1}
\]

Indeed, the right side is

\[
\frac{z^2-\ell+2\lfloor\ell/2\rfloor}{2}
=\frac{z^2-\pi}{2}.
\]

The componentwise identity is

\[
\boxed{
\frac{\sum_Kz_K^2-\pi}{2}
=
\left\lfloor\frac\ell2\right\rfloor
+\sum_K
\left[
\binom{x_K}{2}+\binom{y_K}{2}-x_Ky_K
\right].
}
\tag{4.2}
\]

Define

\[
P_S^{\mathrm{sep}}
=\sum_{K<J}x_Kx_J,\qquad
P_T^{\mathrm{sep}}
=\sum_{K<J}y_Ky_J,
\]

\[
C_{ST}^{\mathrm{sep}}
=\sum_{K\ne J}x_Ky_J.
\]

Then “their difference” must mean (4.1) minus (4.2), giving

\[
\boxed{
\frac{z^2-\sum_Kz_K^2}{2}
=P_S^{\mathrm{sep}}
+P_T^{\mathrm{sep}}
-C_{ST}^{\mathrm{sep}}.
}
\tag{4.3}
\]

For independent fair component signs,

\[
\mathbb E_\varepsilon u_p(\varepsilon)^2
=\sum_Kz_K^2.
\]

Consequently

\[
\boxed{
\mathfrak G_\tau
-\mathbb E_\varepsilon\mathfrak R_\tau(\varepsilon)
=
\sum_{q,p}\frac{
P_S^{\mathrm{sep}}
+P_T^{\mathrm{sep}}
-C_{ST}^{\mathrm{sep}}
}{c_q},
}
\tag{4.4}
\]

and

\[
\boxed{
A_\tau-\sum_K\|d_K\|_A^2
=
4\sum_{q,p}\frac{
P_S^{\mathrm{sep}}
+P_T^{\mathrm{sep}}
-C_{ST}^{\mathrm{sep}}
}{c_q}.
}
\tag{4.5}
\]

The constants and signs in the report are correct.

The interpretation needs correction.  Equations (4.3)--(4.5) describe fair
independent signing.  They do not characterize the optimum over correlated
signings that appears in cut-locality.  At a cut-local factor,

\[
\beta_\tau=A_\tau
\le\sum_K\|d_K\|_A^2,
\]

so the weighted occurrence statistic in (4.4) is necessarily nonpositive.
The converse is false: fair signs can fail on average while a correlated
component cut still descends.

Accordingly, “separated opposite-target occurrences lock the current
signing” should be weakened to “they oppose fair-sign descent” or “they
contribute component restitution.”  The exact lock is (3.2).

For a balanced pair \(|X-Y|\le1\), it is valid that \(z^2=\pi\), so the pair
has zero ideal gain.  The claim that separated occurrences can impose
positive restitution on “every altered signing” is too strong without a
qualification: the all-\(-\) signing always produces \(\tau F\), has
\(u=-z\), and pays the same zero restitution as all-\(+\).  More generally,
positive restitution may be forced for some nonconstant signings, not for
every nontrivial signing.

**Classification:** the identities are **valid**; the claimed lock
interpretation is **corrected** to fair-sign scope.

## 5. Weighted cut cone

Put

\[
w_{KL}=\langle d_K,d_L\rangle_A.
\]

By (2.10),

\[
\mathcal Q_A(F_I)-\mathcal Q_A(F)
=-\sum_{\substack{K\in I\\L\notin I}}w_{KL}.
\tag{5.1}
\]

Thus cut-locality is exactly

\[
\sum_{\delta I}w_{KL}\le0
\iff
w^+(\delta I)\le w^-(\delta I)
\qquad\text{for every }I.
\tag{5.2}
\]

For arbitrary real labels \(t_K\), the coarea identity gives

\[
\sum_{K<L}w_{KL}|t_K-t_L|
=
\int_{\mathbb R}
\sum_{\substack{K:t_K>s\\L:t_L\le s}}
w_{KL}\,ds
\le0.
\tag{5.3}
\]

Every finite \(L^1\) semimetric is a nonnegative integral of cut
semimetrics, so the extension to all \(L^1\) cut semimetrics is valid.  It
does not imply a squared-Euclidean or \(L^2\) estimate.

If \(w_{uv}=p>0\), every \(u\)-\(v\) cut contains at least this positive
demand.  Giving each negative edge capacity \(-w_{KL}\), (5.2) implies that
every \(u\)-\(v\) cut has capacity at least \(p\).  Undirected
max-flow/min-cut therefore routes \(p\) units fractionally from \(u\) to
\(v\).

This is a separate single-demand routing theorem for each positive edge.  It
does not give simultaneous bounded congestion for all positive edges.

When an overlay is connected, there is one component and no off-diagonal
Gram graph.  The cut-cone inequalities are then vacuous.  This is an
algebraic vacuity statement, not an existence theorem for high-energy
connected-overlay factors.

**Classification:** the cut-cone, coarea, and single-demand routing claims
are **valid** with these stated limitations.

## 6. The unsupported quadratic locking bound

The report claims that raw cyclic positivity bounds balanced-pair locking by
\(O_A(W)\) per rank.  The proved geometry does not establish this.

Section 3 proves an \(O_A(W)\) expected \(L^1\)-displacement estimate, not an
\(L^2\) or quadratic-restitution estimate.  The gap is real.  An abstract
balanced pair may have

\[
z_1=t,\qquad z_2=-t.
\]

Then \(z=0\) and the ideal gain is zero, while either nonconstant signing has

\[
\frac{u^2-\pi}{2c_q}
=\frac{2t^2}{c_q}.
\tag{6.1}
\]

The corresponding component occurrence mass is only linear in \(t\).
Therefore no \(O(W)\) quadratic bound follows from an \(O(W)\)
\(L^1\)-ledger.

The occurrence-capacity theorem below supplies only

\[
U_q=
\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor,
\]

and raw positivity gives at best order \(U_qW\) for an aggregate quadratic
term.  Already

\[
U_1=\left\lfloor\frac{m+2}{2}\right\rfloor
=\Theta(m).
\]

Whether exact ownership-component geometry improves this to \(O_A(W)\) is
precisely unproved.

The scale arithmetic following the unsupported assertion is conditionally
correct.  Since

\[
H_A\operatorname{Cat}_m
=\frac{H_AW}{n}
=\Theta_A(W/\sqrt m),
\tag{6.2}
\]

an \(O(H_AW)\) error is a factor \(n\) above the terminal energy.  In a
transposition-scale recurrence contracting at rate \(\Theta(1/n)\), a
terminal value \(O(H_A\operatorname{Cat}_m)\) requires additive error

\[
O_A\left(\frac{H_A\operatorname{Cat}_m}{n}\right)
=O_A\left(\frac{H_AW}{n^2}\right).
\tag{6.3}
\]

Thus the stated factors \(n\) and \(n^2\) are correct conditional comparisons,
but the report has not proved that the relevant restitution error is
\(O(H_AW)\).

**Classification:** the \(O_A(W)\)-per-rank quadratic locking claim is
**unsupported**.  The subsequent scale ratios are **valid conditionally**.

## 7. Extension-fan and cyclic-distance geometry

Let \(r=m-q\), and let a component \(K\) contain \(k\) old wreaths.  Its
common middle-root set \(E_K\) has \(nk\) elements and is
\(\tau\)-invariant.  Every cyclic rank-\(r\) interval lies in exactly

\[
m-r+1=q+1
\]

owned cyclic middle intervals.  Therefore

\[
\boxed{
(q+1)\Delta_{K,q}
=
\sum_{X\in E_K}
\left(
\mathbf1_{\partial_q^+(X)}
-\mathbf1_{\partial_q^-(X)}
\right).
}
\tag{7.1}
\]

This is an exact integral identity within one ownership component.

### Single-wreath displacement

If the transposed labels have cyclic distance \(d\in\{1,\ldots,m\}\), then
for \(2\le r\le m\),

\[
\boxed{
\left\|
\tau\mathbf1_{\mathcal I_r(C)}
-\mathbf1_{\mathcal I_r(C)}
\right\|_1
=
\left\|
\tau\mathbf1_{\mathcal I_r(C)}
-\mathbf1_{\mathcal I_r(C)}
\right\|_2^2
=
4\min(d,r)-4\mathbf1_{\{d=r\}}.
}
\tag{7.2}
\]

There are \(2\min(d,r)\) intervals containing exactly one transposed label;
normally all leave the cyclic interval family after swapping, while at
\(d=r\) exactly two are exchanged with each other.

Since

\[
\Delta_{K,q}
=\sum_{C\in L_K}
\left(
\tau\mathbf1_{\mathcal I_r(C)}
-\mathbf1_{\mathcal I_r(C)}
\right),
\]

triangle inequality and (7.2) imply the report's looser bound

\[
\|\Delta_{K,q}\|_1
\le
\sum_{C\in K}
\begin{cases}
2(q+2d_C),&d_C\le m-q,\\
2(m+d_C),&d_C>m-q.
\end{cases}
\tag{7.3}
\]

The displayed inequality is valid but should be called a rigorous upper
bound, not an exact or sharp formula.

For a fixed wreath and a uniform coordinate transposition, \(d\) is uniform
on \(\{1,\ldots,m\}\).  Summing the looser bound gives

\[
\begin{aligned}
&\frac1m
\left[
\sum_{d=1}^{m-q}(2q+4d)
+\sum_{d=m-q+1}^{m}(2m+2d)
\right]\\
&\qquad=
2m+2q+2-\frac{q(q+1)}m.
\end{aligned}
\]

Every old wreath occurs exactly once in the sum over components, even though
the component partition depends on \(\tau\).  Hence

\[
\boxed{
\mathbb E_\tau
\sum_K\|\Delta_{K,q}\|_1
\le
\operatorname{Cat}_m
\left(
2m+2q+2-\frac{q(q+1)}m
\right).
}
\tag{7.4}
\]

The constant in (7.4) is correct.

The sharper identity (7.2) also gives

\[
\mathbb E_\tau
\sum_K\|\Delta_{K,q}\|_1
\le
\operatorname{Cat}_m
\frac{4(r(n-r)-2)}{n-1}.
\tag{7.5}
\]

Both (7.4) and (7.5) are \(O_A(W)\) on a fixed Gaussian window.  Neither
controls quadratic component restitution.

### Occurrence capacity

A fixed rank-\(r=m-q\) target has

\[
\binom{n-r}{m-r}
=\binom{m+q+1}{q}
\]

middle extensions.  Each wreath occurrence consumes its \(q+1\) distinct
cyclic middle extensions, and exact middle ownership makes these consumed
extension sets disjoint across occurrences.  Therefore

\[
\boxed{
\mu_q(S)
\le
\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor.
}
\tag{7.6}
\]

The denominator and constant are correct.

**Classification:** (7.1), (7.3), (7.4), and (7.6) are **valid**; (7.3) is
nonsharp, and none supplies the missing quadratic bound.

## 8. Diagonal variance

The exact single-wreath identity (7.2) gives

\[
\boxed{
\mathbb E_\tau
\left\|
\tau\mathbf1_{\mathcal I_r(C)}
-\mathbf1_{\mathcal I_r(C)}
\right\|_2^2
=
\frac{4(r(n-r)-2)}{n-1},
\qquad 2\le r\le m.
}
\tag{8.1}
\]

The \(-2\), the factor \(4\), and the denominator \(n-1\) are all correct.
The lower bound \(r\ge2\) is essential; at rank one every wreath contains
the whole singleton family, so the difference is zero.

Summing over all \(W/n=\operatorname{Cat}_m\) wreaths gives

\[
D_r^{\mathrm{diag}}
=
\frac Wn
\frac{4(r(n-r)-2)}{n-1}.
\tag{8.2}
\]

For \(r=m-q\),

\[
r(n-r)-2
=m^2+m-q(q+1)-2.
\]

Uniformly for \(q\le A\sqrt m\),

\[
D_r^{\mathrm{diag}}
=W\left(1+O_A(m^{-1})\right),
\tag{8.3}
\]

so the report's \(\Theta(W)\)-per-rank assertion is valid in its intended
fixed-window context.

It is false if read uniformly over every \(2\le r\le m\).  For fixed \(r\),
(8.2) is only \(\Theta(W/m)\).  The report should attach the fixed-window
qualifier directly to the \(\Theta(W)\) sentence.

Writing the component sums as

\[
\sum_K\left\|\sum_{C\in K}g_C\right\|_2^2
=
\sum_C\|g_C\|_2^2
+2\sum_K\sum_{C<D\in K}\langle g_C,g_D\rangle,
\]

shows that reducing the central diagonal contribution \(\Theta(W)\) to
Catalan scale \(O(W/n)\) requires negative cross-term cancellation of order
\(W\).  Triangle inequalities and extension-capacity estimates erase these
cross terms.  The report's qualitative cancellation conclusion is valid.

## 9. First-shadow obstruction histogram

Let

\[
r=m-1,\qquad
N=\binom nr,\qquad
R=W-N=\frac{2W}{m+2}.
\tag{9.1}
\]

### Point-regular baseline

Put \(g=\gcd(n,r)\).  Since

\[
g=\gcd(2m+1,m-1)\in\{1,3\}
\]

and

\[
\frac{Rr}{n}
=r\operatorname{Cat}_m-\binom{n-1}{r-1}
\in\mathbb Z,
\]

coprimality after division by \(g\) gives

\[
\frac ng\mid R.
\tag{9.2}
\]

For the cyclic action on \(r\)-subsets, every stabilizer order divides both
\(n\) and \(r\), hence divides \(g\).  Thus orbit sizes are \(n\) when
\(g=1\), and \(n\) or \(n/3\) when \(g=3\).  Every orbit is point-regular.

When \(g=3\), write \(n=3s,r=3t\).  The short-orbit elements are the unions
of \(t\) of the \(s\) triples of the order-three subgroup, giving

\[
\frac1s\binom st
\]

short orbits.  This supplies at least two short orbits for all sufficiently
large relevant \(m\).  The number of full orbits is also sufficient:
short-orbit elements number at most \(2^s\), while \(N-R\) has central
binomial order \(2^n/\operatorname{poly}(n)\).

Therefore, for all sufficiently large \(m\), one can express

\[
R=an+b\frac n3,\qquad b\in\{0,1,2\},
\]

and select \(a\) full orbits and \(b\) short orbits.  Their union
\(\mathcal H\) is point-regular and has size \(R\).

The report's construction is valid, but divisibility alone is not a complete
proof; the short- and full-orbit abundance argument above must be included.

### Rectangle perturbation

Put

\[
b_0=\mathbf1+\mathbf1_{\mathcal H}
\]

and, for four distinct labels \(a,b,c,d\), define

\[
v(S)
=
(\mathbf1_{a\in S}-\mathbf1_{b\in S})
(\mathbf1_{c\in S}-\mathbf1_{d\in S}),
\qquad
\mu=b_0+v.
\]

Then \(v\in\{-1,0,1\}\), \(U_rv=0\), and \(\sum_Sv(S)=0\).  Each sign occurs
on exactly

\[
2C,\qquad
C=\binom{n-4}{r-2}
=\binom{2m-3}{m-3},
\tag{9.3}
\]

because each sign is the union of two prescribed two-in/two-out patterns.

The baseline has total

\[
\sum_Sb_0(S)=N+R=W
\]

and point margin

\[
\binom{n-1}{r-1}+\frac{Rr}{n}
=\frac{Wr}{n}
=r\operatorname{Cat}_m.
\]

Adding \(v\) preserves both.  Also

\[
0\le\mu(S)\le3.
\]

A fixed \((m-1)\)-target has \(m+2\) middle extensions, and each occurrence
uses its two distinct cyclic middle extensions.  Hence

\[
\mu(S)
\le\left\lfloor\frac{m+2}{2}\right\rfloor,
\]

so the proposed \(\mu\le3\) respects this necessary capacity for \(m\ge4\).
These are necessary marginal and capacity constraints only; they do not
establish Boolean factor realizability.

### Energy lower bound

For \(m\ge3\),

\[
c_1=\left\lfloor\frac WN\right\rfloor=1.
\]

Let

\[
h_\pm
=|\mathcal H\cap\{v=\pm1\}|.
\]

Only cells with \(\mu=0\) or \(3\) contribute to \(Q_1\), and each contributes
\(2\).  Therefore

\[
\begin{aligned}
Q_1(\mu)
&=2\bigl((2C-h_-)+h_+\bigr)\\
&=4C+2(h_+-h_-)\\
&\ge4C-2R.
\end{aligned}
\tag{9.4}
\]

Moreover,

\[
\frac{4C}{W}
=\frac{(m+1)(m-2)}
{(2m+1)(2m-1)},
\qquad
\frac{2R}{W}
=\frac4{m+2}.
\]

Thus

\[
\boxed{
\frac{Q_1(\mu)}W
\ge
\frac{(m+1)(m-2)}
{(2m+1)(2m-1)}
-\frac4{m+2}
=\frac14-o(1).
}
\tag{9.5}
\]

There is no missing factor two: this is the full \(Q_1\)-energy.  The
half-energy contribution is \(Q_1/2\).

### Signed selector scope

Choose any exact factor \(F_0\) with first-shadow histogram \(\mu_0\).
Because

\[
\mu-\mu_0\in\ker_{\mathbb Z}U_r,
\]

rank-isolated integral selector surjectivity gives a signed
\(z\in\ker_{\mathbb Z}A_m\) with rank-\(r\) image
\(\mu-\mu_0\) and zero image at every other selected lower rank.
Consequently \(x_{F_0}+z\) is an integral signed exact-middle solution with
histogram \(\mu\).

This removes a lattice or congruence obstruction only.  It gives no
nonnegative wreath coefficients, packing-compatible support, or Boolean
exact factor.  The report states this limitation correctly.

**Classification:** the baseline, rectangle perturbation, capacity,
energy lower bound, exact ratio, and signed lift are **valid**.  The orbit
construction needs the omitted abundance proof.

## 10. Connected-overlay counterexample route

Let \(U_F\) be the space of functions constant on the middle blocks of \(F\).
The standard overlay argument gives

\[
\dim(U_F\cap\tau U_F)
=
\#\{\text{components of the }F\text{-versus-}\tau F
\text{ ownership overlay}\}.
\tag{10.1}
\]

Therefore

\[
U_F\cap\tau U_F=\langle\mathbf1\rangle
\tag{10.2}
\]

is exactly overlay connectedness.

If the overlay is connected, its component cube has one bit.  The only
transposition-component outcomes are \(F\) and \(\tau F\), and these have
the same coordinate-invariant energy.  Thus connectedness for every
transposition makes \(F\) transposition-cut-local.

The phrase “every legal move merely relabels \(F\)” must mean every move in
this transposition-component class.  It is false if read as every possible
exact-factor bitrade.

If a Boolean exact factor realizes the histogram in Section 9 and satisfies
(10.2) for every transposition, then

\[
\mathcal Q_A(F)\ge Q_1(\mu)
=\left(\frac14-o(1)\right)W.
\]

Since

\[
H_A\operatorname{Cat}_m
=\frac{H_AW}{n},
\]

\[
\boxed{
\frac{\mathcal Q_A(F)}
{H_A\operatorname{Cat}_m}
\ge
\left(\frac1{2A}+o(1)\right)\sqrt m.
}
\tag{10.3}
\]

The coefficient \(1/(2A)\) is correct.  Infinitely many such factors would
refute \(LM_A\).

This is a sufficient obstruction route, not a necessary form of a
counterexample.  A high-energy factor with disconnected overlays but every
weighted component cut nonpositive would also refute \(LM_A\).

## 11. Canonical MSW comparison

The exact component hierarchy gives

\[
\#\{\text{components in the }(2\,3)\text{-overlay}\}
=\sum_{j=0}^{m-2}\operatorname{Cat}_j.
\tag{11.1}
\]

This is greater than one for \(m\ge3\).  At \(m=2\) it equals one, so the
report's unqualified strict inequality needs that minor range correction.
For the asymptotic blueprint, the MSW factor therefore fails the
all-transpositions-connected condition.

The hole claim requires a substantive wording correction.  What is proved
is an explicit hereditary subfamily of at least
\(\operatorname{Cat}_{m-4}\) depth-one holes.  The source explicitly states
that the MSW factor has additional holes and that their total asymptotics are
unknown.  Therefore the sentence

> its proved all-dimensional hole family has only
> \(\operatorname{Cat}_{m-4}\) members

must be replaced by

> the currently certified hereditary subfamily contains
> \(\operatorname{Cat}_{m-4}\) members.

This certified subfamily alone is below the target scale because

\[
\frac{\operatorname{Cat}_{m-4}}
{H_A\operatorname{Cat}_m}
\sim\frac1{256H_A}\longrightarrow0.
\]

It neither upper-bounds the complete MSW hole contribution nor rules out a
different high-energy mechanism.  The disconnected \((2\,3)\)-overlay only
rules MSW out from the particular rigid-connected blueprint.

**Classification:** the component count is **valid** for \(m\ge3\); the
“only \(\operatorname{Cat}_{m-4}\)” hole claim is **corrected/unsupported as
an upper bound**.

## 12. Implication scope and corrected logical alternatives

The exact unproved positive-cut lemma is:

> For every fixed \(A>0\), there is \(C_A<\infty\) such that, for all
> sufficiently large \(m\), every exact factor satisfying
> \[
> \mathcal Q_A(F)>C_AH_A\operatorname{Cat}_m
> \]
> has some transposition \(\tau\) and component subset \(I\) with
> \[
> \langle d_I,d_{I^c}\rangle_A>0.
> \]

If this holds, repeated strict descent terminates in the finite exact-factor
space at a cut-local factor with

\[
\mathcal Q_A(F)=O_A(H_A\operatorname{Cat}_m).
\]

Since \(Q_q\ge2O_q\),

\[
\sum_{q\le H_A}\frac{O_q(F)}{c_q}
\le\frac12\mathcal Q_A(F)
=o(W),
\]

because

\[
\frac{H_A\operatorname{Cat}_m}{W}
=\frac{H_A}{n}
=O_A(m^{-1/2}).
\]

Thus

\[
LM_A
\Longrightarrow
\text{fixed-window unlabelled overload}
\Longrightarrow
MWB
\]

after slow diagonalization.  This implication is **valid**.  It does not
produce a balanced nested resolution or labelled common-owner
synchronization.

The opening alternatives are not an exhaustive logical dichotomy.  The true
negation of \(LM_A\) is the existence of high-energy exact factors satisfying

\[
\langle d_I,d_{I^c}\rangle_A\le0
\]

for every transposition and every component subset \(I\).  Such factors need
not have connected overlays or the special first-shadow histogram above.

Accordingly:

- “realize the rigid connected factor” is one explicit sufficient
  counterexample program;
- “a counterexample requires the rigid-realization lemma” is false as a
  necessity statement;
- “a proof requires a fragmentation/locking theorem” is acceptable only as
  a description of this lane's current support-feasible route, not as a
  logical necessity for every proof of \(LM_A\);
- even a counterexample to \(LM_A\) would refute only this route-specific
  lemma, not MWB or the contiguous-OR conjecture.

## 13. Claim classification

### Valid

- Pair-sum preservation, parity floor, and nonnegativity of every unweighted
  restitution numerator.
- The exact full-energy identity (2.5).
- The Hilbert conversions (2.7)--(2.11) and every factor of two.
- The cut-locality equivalence (3.1)--(3.2), with one common signing over the
  whole window.
- Both occurrence identities and their separated-pair difference.
- The full-energy cut formula, cut-cone inequality, coarea identity, and
  single-demand negative-edge routing theorem.
- The extension-fan identity, per-wreath displacement bound, averaged
  \(L^1\) constant, occurrence capacity, and exact diagonal-variance formula.
- The point-regular baseline construction for all sufficiently large \(m\),
  after adding the orbit-abundance proof.
- The rectangle histogram's point margins, nonnegativity, capacity, energy
  lower bound, and exact asymptotic ratio.
- The signed selector lift in the unrestricted signed fibre only.
- The equivalence between (10.2) and connected ownership overlays.
- The \(1/(2A)\) energy ratio for the explicitly unproved rigid Boolean
  realization.
- The implication \(LM_A\Rightarrow\) fixed-window unlabelled overload
  \(\Rightarrow MWB\).

### Corrected

- Weighted parity functionals are rational in general, not integer-valued.
- The occurrence-pair statistic controls fair independent signs, not the
  correlated-sign optimum.
- “Every altered signing” must exclude at least the all-plus and all-minus
  antipodal constant signings.
- The local-minimum restitution equality is aggregate over all ranks and
  pairs for one common component signing.
- The report's \(L^1\) displacement bound is valid but nonsharp and is not a
  quadratic estimate.
- The \(\Theta(W)\) diagonal sum is uniform only in the fixed Gaussian
  central window, not for all \(2\le r\le m\).
- “Every legal move” means every transposition-component switch, not every
  exact-factor bitrade.
- Connected overlays are a sufficient counterexample route, not a necessary
  one.
- The MSW component-count inequality needs \(m\ge3\).
- The certified \(\operatorname{Cat}_{m-4}\) MSW family is a lower subfamily,
  not the total set of holes.

### Unsupported or unproved

- \(LM_A\) itself.
- An \(O_A(W)\)-per-rank bound on quadratic parity restitution derived from
  raw cyclic positivity or the \(L^1\) extension ledger.
- Any simultaneous bounded-congestion routing of all positive Gram demands
  from the single-demand min-cut statement.
- The Boolean realization of the proposed high-energy first-shadow
  histogram.
- Simultaneous connectedness of every transposition overlay for such a
  realizing factor.
- Any necessity claim for the rigid connected-overlay counterexample
  blueprint.
- Any upper bound of \(\operatorname{Cat}_{m-4}\) on the full MSW hole
  family.
- Any implication from \(LM_A\) to labelled common-owner synchronization.

## Final assessment

Lane L correctly isolates positive weighted component cuts as a sufficient
descent mechanism and gives a sound signed high-energy obstruction
histogram.  It does not yet connect the \(O_A(W)\) cyclic \(L^1\) geometry
to quadratic restitution, nor does it realize its signed obstruction inside
a Boolean exact factor.

The exact surviving questions are therefore:

\[
\boxed{
\begin{array}{l}
\text{Proof route: show that every high-energy exact factor has a positive}\\
\text{transposition-component cut;}\\[2mm]
\text{counterexample route: construct any high-energy cut-local exact factor,}\\
\text{not necessarily one with connected overlays.}
\end{array}
}
\]

Neither statement is currently proved.
