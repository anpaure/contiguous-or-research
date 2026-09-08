# Independent audit of `GLOBAL_COMPONENT_NOISE_GATE_NO_GO_20260724.md`

## Verdict

The mathematical core passes.  In particular, the normalization of the
unscaled component noise, the sharp spectral baseline (4(n-1)), the
three-slack identity, Theorems 6.1 and 6.2, the Gaussian-window baseline,
the row self-energy expansion, and the formal connected-overlay
countermodel are all correct.

The note does **not** prove the component-noise gate, and it does not claim
to.  Its main conclusion is valid: at a global minimizer the proposed gate
is a much stronger near-equality theorem than low floor energy alone.

I found no constant or sign error.  I recommend one short proof insertion
in the robust-stability discussion, plus several minor scope/notation
clarifications listed below.

## 1. Setup and normalizations

Let

\[
Q_q=\|f_q\|_2^2-V_q^{\min}
   =\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

The stated inequality (2O_q\le Q_q) is correct.  Consequently

\[
2\sum_{q\le H}\frac{O_q}{c_q}\le Q_H.
\]

The definitions

\[
N_{\tau,H}=\sum_C\sum_q c_q^{-1}\|u_{q,C}-w_{q,C}\|_2^2,
\qquad
R_H=\sum_\tau N_{\tau,H}
\]

are the **unscaled** component-noise convention.  Under fair component
choices the conditional variance is one quarter of this quantity.  All
later factors of (1/4), (4(n-1)), and (8(n-1)) are consistent with
that convention.

Minor editorial fix: in the setup, `n=2m+1,qquad` should be
`n=2m+1,\qquad`.

## 2. Component equivariance

Proposition 3.1 is correct.

For a row (P), the (n) middle windows contain the two transposed
coordinates a total of (2m=n-1) times.  Therefore they cannot all contain
exactly one of the two coordinates.  A window containing both or neither
is fixed by the transposition and gives an overlap edge joining (P) to
(\tau P).  The map (P\mapsto\tau P) therefore maps the left side of a
component injectively into its right side.  Regularity gives equal side
sizes, hence surjectivity and

\[
w_{q,C}=\tau u_{q,C}.
\]

Each collection of (k) cyclic rows has total mass (nk) and point
margin (r_qk), so every component difference has zero constant and
degree-one Johnson parts.  The same is true of every full centered
profile (f_q).

## 3. Switching-cube identity and equality conditions

For a uniform subset (I) of components,

\[
\mathbb E f_I=\frac{f+\tau f}{2},
\]

and the independent-sign variance is (N_{\tau,H}/4).  Since

\[
\left\|\frac{f+\tau f}{2}\right\|_H^2-\|f\|_H^2
=-\frac14\|f-\tau f\|_H^2,
\]

equation (4.1),

\[
\mathbb E e_\tau(I)=\frac14(N_{\tau,H}-A_{\tau,H}),
\]

is exact.

At a global minimizer every child has no smaller objective, so
(N_{\tau,H}\ge A_{\tau,H}).  Equality forces every child to have the same
energy.  Singleton and two-component expansions give exactly

\[
2\langle f,d_C\rangle_H+\|d_C\|_H^2=0,
\qquad
\langle d_C,d_{C'}\rangle_H=0.
\]

The converse is also correct.  A connected overlay has one component and
therefore (N_{\tau,H}=A_{\tau,H}) identically; connectivity alone cannot
yield descent.

For the targetwise equality claim (6.1), one implicit step is valid but
worth stating: zero total slack first gives (Q_H=0), and since every
rank-floor excess is nonnegative, every parent rank is balanced.  Equality
of the switching-cube energy then puts every child at the same aggregate
floor (B_H), hence every child is balanced at every rank.  Only after
this observation does the subset-sum argument imply that at a fixed target
at most one component increment is nonzero.

## 4. Spectral constant and the three-slack identity

For unordered coordinate transpositions,

\[
\sum_\tau\|f-\tau f\|_2^2
=2\sum_{j\ge2}j(n-j+1)\|f^{(j)}\|_2^2.
\]

Because exact-factor profiles have no (E_0) or (E_1) part, the sharp
lowest eigenvalue is attained at (j=2) and equals (4(n-1)).  Moreover

\[
j(n-j+1)-2(n-1)=(j-2)(n-j-1),
\]

so (5.1) is correct:

\[
D_H-4(n-1)S_H
=2\sum_q\frac1{c_q}\sum_{j\ge3}
(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\]

Thus, at a global minimizer,

\[
R_H-4(n-1)B_H
=(R_H-D_H)
 +(D_H-4(n-1)(B_H+Q_H))
 +4(n-1)Q_H
\]

is indeed a sum of three nonnegative terms.  The deductions
(Q_H=o(W)), (R_H-D_H=o(nW)), and total (j\ge3) mass (o(W)) from an
(o(nW)) upper error are correct.  For (q\ge1), the relevant Johnson
degrees lie below the middle, and
(2(j-2)(n-j-1)\ge2(n-4)) for (j\ge3).

The coefficient meta-observation is also correct: from a proposed bound

\[
R_H\le4(n-1)B_H+\gamma_mQ_H+e_m
\]

one gets

\[
(4(n-1)-\gamma_m)Q_H\le e_m.
\]

Hence an error merely known to be (o(nW)) forces (Q_H=o(W)) in a
scale-robust way only with a gap (4(n-1)-\gamma_m=\Omega(n)), or more
generally when (e_m=o((4(n-1)-\gamma_m)W)).

## 5. Theorems 6.1 and 6.2

### Theorem 6.1

All constants check.

At the first shadow (r=m-1), the balanced bonus density is
(\theta=2/m).  A Boolean (E_2) bonus family would therefore have
outside-to-bonus degree (8) and bonus-to-outside degree (4m-8).

For a ((m-2))-set (T), its extension star has size (m+3).  If it is
not full, then its bonus multiplicity is at most (8).  For a bonus
((m-1))-set (S),

\[
\sum_{T\lessdot S}(\kappa(T)-1)
=(m-1)(m+2)-(4m-8)=m^2-3m+6,
\]

so

\[
\sum_{T\lessdot S}\kappa(T)=m^2-2m+5.
\]

Relative to all facets being full, the deficit is (4m-8).  A nonfull
facet contributes between (m-5) and (m+3).  For (m\ge18), three
such deficits have total at most (3m+9<4m-8), while five have total at
least (5m-25>4m-8).  Hence there are exactly four nonfull facets and
(m-5) full facets.

The identity

\[
U\mathbf1_{\mathcal T}=(m-5)\mathbf1_{\mathcal B}
\]

is correct.  Also

\[
U^*U=(n-k)I+A_{J(n,k)}
\]

has eigenvalue

\[
(k+1-j)(n-k-j)>0
\]

on (E_j), so (U) is injective here.  Every full facet has exactly four
boundary neighbours for each of its (m+3) extensions, giving boundary
degree (4(m+3)).  An (E_2) Boolean family would instead have boundary
degree (4m(1-\delta)<4m).  The contradiction is valid.

### Theorem 6.2

The generalization is also correct.  Here (s=n-r+1) is the size of an
extension star, and the degree-two Johnson eigenvalue is (4m), so

\[
b=4m\theta,\qquad d=4m(1-\theta)
\]

are the two cross-degrees and hence integers.  A nonfull facet has
(\kappa\le b), so each of its deficits lies in ([s-b,s]).  The strict
inequalities

\[
3s<d<5(s-b)
\]

force exactly four nonfull facets.  Since (r>4), full facets exist;
the same injective up-operator argument applies.  Their boundary degree is
(4s>4m), because (r\le m) implies (s\ge m+2), contradicting the
(E_2) boundary degree (4m(1-\delta)<4m).

For (r=m-O(\sqrt m)) and fixed (0<\theta<1/16), all inequalities in
(6.10) hold eventually.  Complementation gives the corresponding
exclusion for (15/16<\theta<1).

Minor clarification: the phrase “preserves Johnson harmonic degree” is
best read as “intertwines each (E_j) with the corresponding (E_j) in
the next rank”; injectivity is what permits pulling the (E_0\oplus E_2)
conclusion back through (U).

## 6. Gaussian baseline

Uniformly for (q\le A\sqrt m),

\[
\log\frac{W}{N_q}=\frac{q^2}{m}+O_A(m^{-1/2}).
\]

Writing (t=W/N_q), (c=\lfloor t\rfloor), and
(\theta=\{t\}), one has

\[
\frac{V_q^{\min}}{c_qW}
=\frac{\theta(1-\theta)}{ct}=\varphi(t).
\]

The function (\varphi) extends continuously by zero at every integer,
including from the left because (\theta(1-\theta)\to0).  It is bounded,
so the Riemann-sum argument is valid and gives

\[
\frac{B_H}{W\sqrt m}
\longrightarrow
\int_0^A\varphi(e^{x^2})\,dx.
\]

The integral is positive for every (A>0), because its integrand is
positive except at the discrete set (e^{x^2}\in\mathbb Z).  Therefore
(B_H=\Theta_A(W\sqrt m)), and the baseline
(4(n-1)B_H) has order (nW\sqrt m).  An (o(nW)) excess is indeed a
relative (o(m^{-1/2})) requirement.

## 7. Robust-stability implication: valid, but insert one estimate

The proposed implication from a uniform Boolean-(E_2) stability theorem
to failure of the component-noise gate is sound.  The note should make the
following quantitative bridge explicit.

Define the pointwise-clamped adjacent-integer vector (b\in\{c,c+1\}^N)
by choosing the nearer floor value on each side of the interval
([c,c+1]).  Then

\[
\|\mu-b\|_2^2\le Q_q.
\]

Its mass discrepancy satisfies

\[
\Delta:=\left|\sum_Sb(S)-W\right|
\le\sqrt N\,\|b-\mu\|_2
\le\sqrt{NQ_q}.
\]

Flip exactly (\Delta) entries of (b) in the required direction to
obtain a balanced vector (b'=c+\mathbf1_{\mathcal B}).  Since
(\|b-b'\|_2^2=\Delta),

\[
\|\mu-b'\|_2^2
\le2\|\mu-b\|_2^2+2\|b-b'\|_2^2
\le2Q_q+2\sqrt{NQ_q}.
\tag{A.1}
\]

Thus (Q_q=o(N)) really does imply (\|\mu-b'\|_2^2=o(N)).  This is the
missing displayed justification behind the sentence “the adjustment cost
is (o(N)).”

On a fixed Gaussian window, (c_q=O_A(1)) and (N_q=\Theta_A(W)).
Consequently (5.3) gives (Q_q=o(N_q)) and (j\ge3) mass (o(N_q))
uniformly rank by rank (the note states the weaker “all but
(o(\sqrt m))” version).  Exact-factor profiles have zero (E_1) part;
(A.1) transfers the small (E_1\oplus E_{\ge3}) projection to the Boolean
bonus vector.  Choosing a compact interval strictly inside a portion of
the range of (\{e^{x^2}\}) gives a positive proportion of depths with
bonus density in that interval.  Hence the stated uniform stability bound
would contradict (5.3).

Recommended wording fix: replace “after changing at most the mass
discrepancy ... the adjustment cost is (o(N))” by (A.1), since merely
counting changed coordinates does not by itself bound squared distance.

## 8. Row self-energy

Equation (8.1) is correct for (2\le r\le m).  There are
(2\min(r,\ell)) cyclic (r)-windows containing exactly one of the two
transposed coordinates.  Normally their images leave the cyclic-window
family.  When and only when (\ell=r), two such windows are exchanged
inside the family, subtracting four from the symmetric-difference size:

\[
\|\tau h_{P,r}-h_{P,r}\|_2^2
=4\min(r,\ell)-4\mathbf1_{\{\ell=r\}}.
\]

An odd (n)-cycle has exactly (n) unordered coordinate pairs of each
shorter distance (1,\ldots,m).  Therefore

\[
\sum_\tau\|\tau h_{P,r}-h_{P,r}\|_2^2
=4n\left(\sum_{\ell=1}^r\ell+(m-r)r-1\right)
=2n(r(n-r)-2).
\]

There are (W/n) rows.  Expanding the squared component sums yields
exactly (8.3), including the coefficient (2) on row cross terms.  At
the first shadow (r=m-1), the diagonal is

\[
2W(m^2+m-4).
\]

Also

\[
V_1^{\min}=\frac{2W(m-2)}{m(m+2)},
\]

so

\[
4(n-1)V_1^{\min}=16W\frac{m-2}{m+2}.
\]

Thus floor-scale noise retains only (O(m^{-2})) of the row-diagonal
mass, and even an (o(nW)) error retains only (o(m^{-1})).  These
cancellation statements are correctly normalized.

Minor scope clarification: (8.1)--(8.2) are stated for (2\le r\le m).
The controlled depths with (r=1), if ever included, have constant
singleton loads in an exact factor and contribute zero separately.

## 9. Formal countermodel

The countermodel is internally correct and is labelled appropriately as
formal rather than an exact factor.

For (T=(W/n)h_{P,r}), the vector is integral because (W/n) is the
Catalan number.  It has total mass (W), point margin (rW/n), and is a
sum (with repetition) of (W/n) genuine cyclic-row incidence vectors.
All coordinate relabellings have equal centered energy.  Declaring one
connected component for every transposition gives difference
(\tau T-T), zero total and point margins, equivariance, and
(N_\tau=A_\tau).

Since (T) has value (W/n) on (n) targets and zero elsewhere,

\[
\left\|T-\frac WN\mathbf1\right\|_2^2
=\frac{W^2}{n}-\frac{W^2}{N}
=\frac{W^2}{n}\left(1-\frac nN\right).
\]

This is exponentially larger than (V^{\min}\le N/4) in the central
regime.  Hence the listed abstract properties cannot imply the desired
component-noise upper bound.  The construction does not purport to satisfy
exact middle ownership, so it does not disprove the gate on the true
factor fibre.

## Required fixes

1. Insert estimate (A.1) in the robust-stability paragraph.  The claimed
   conclusion is correct, but the current one-sentence justification skips
   the squared-distance bound.
2. Fix the setup typo `n=2m+1,qquad`.
3. Optionally state explicitly, before (6.1), why equality of the aggregate
   switching energy makes every child balanced at every rank.
4. Optionally clarify the up-operator wording and the harmless (r=1)
   scope noted above.

No theorem statement or numerical constant needs correction.
