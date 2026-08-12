# A genuine MSW cell has mesoscopic component variance

Date: 2026-07-25

## 1. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m,
\qquad H=\lceil L\sqrt m\rceil
\]

for fixed \(L>0\).  At depth \(q\), put

\[
c_q=\left\lfloor
\frac{W}{\binom n{m-q}}
\right\rfloor .
\]

Let \(F_m^{\rm MSW}\) be the canonical exact MSW wreath factor and let
\(\tau=(2\ 3)\).  The proved sealed two-wreath components in the
\(F_m^{\rm MSW}/\tau F_m^{\rm MSW}\) ownership overlay give the exact
lower bound

\[
\boxed{
V_{\tau,H}\ge
\operatorname{Cat}_{m-2}
\left(4+8\sum_{q=2}^H\frac1{c_q}\right).}
\tag{1.1}
\]

Consequently, if

\[
I_L:=\int_0^L\frac{dx}{\lfloor e^{x^2}\rfloor},
\]

then

\[
\boxed{
V_{\tau,H}\ge
\left(\frac{I_L}{2L}+o_L(1)\right)Ht.}
\tag{1.2}
\]

This is a lower bound inside one genuine exact-factor cell, not an
abstract vector example.

At every corner \(F_\varepsilon\) of this same ownership-component cube,
the component variance has the same value, while

\[
\mathbb E_\varepsilon
\bigl(A_{\tau,H}(F_\varepsilon)
      -V_{\tau,H}(F_\varepsilon)\bigr)=0.
\tag{1.3}
\]

It follows that no fixed \(0<\eta\le1\) and error
\(r_m=o_L(Ht)\) can make either of the following statements true for all
exact factors:

\[
A_{\tau,H}-V_{\tau,H}\ge \eta V_{\tau,H}-r_m,
\tag{1.4}
\]

or

\[
V_{\tau,H}\le(1-\eta)A_{\tau,H}+r_m.
\tag{1.5}
\]

More generally, if \(a_m,b_m\ge0\), then a universal inequality

\[
A_{\tau,H}-V_{\tau,H}
\ge a_mA_{\tau,H}+b_mV_{\tau,H}-r_m
\tag{1.6}
\]

necessarily satisfies

\[
\boxed{
r_m\ge
(a_m+b_m)
\left(\frac{I_L}{2L}+o_L(1)\right)Ht.}
\tag{1.7}
\]

In particular, if \(a_m+b_m\ge\eta_L/n\) and
\(r_m=C_LHt/n\), then necessarily

\[
\boxed{C_L\ge \frac{\eta_L I_L}{2L}.}
\tag{1.8}
\]

Thus a multiplicative component-variance domination is false on the
correct mesoscopic scale.  A surviving statement may instead be additive
and \(A\)-relative, subtract the exact floor and higher-harmonic rebates,
or average across changing transpositions.  In particular, this result
does **not** refute the additive ceiling

\[
V_{\tau,H}\le A_{\tau,H}+C_LHt,
\]

and it does not settle the transposition-averaged MWB drift inequality.

The Johnson indexing is also unambiguous: exact factor discrepancies and
component innovations have \(U_0=U_1=0\).  The slow baseline is \(U_2\),
not \(U_1\).

---

## 2. Exact ownership-component setup

For a component \(K\) of the ownership overlay between an exact factor
\(F\) and \(\tau F\), let \(L_K,R_K\) be its two sides.  At depth \(q\)
write

\[
\Delta_{K,q}=\mu_q(L_K)-\mu_q(R_K).
\]

Use the weighted norm

\[
\|g\|_H^2=\sum_{q=1}^H\frac{\|g_q\|_2^2}{c_q}.
\]

Then

\[
A_{\tau,H}(F)=
\left\|\sum_K\Delta_K\right\|_H^2,
\qquad
V_{\tau,H}(F)=\sum_K\|\Delta_K\|_H^2.
\tag{2.1}
\]

Every component has equally many rows on its two sides.  Every wreath row
has \(n\) cyclic intervals at depth \(q\), and each coordinate belongs to
exactly \(m-q\) of them.  Hence \(\Delta_{K,q}\) has zero total mass and
zero point margins.  Therefore

\[
\Delta_{K,q}\in\bigoplus_{j\ge2}U_j.
\tag{2.2}
\]

This proves the last indexing assertion in Section 1.

If the sides of the components are signed by
\(\varepsilon_K\in\{\pm1\}\), the corresponding corner is another exact
factor and its coherent displacement is

\[
A_{\tau,H}(F_\varepsilon)
=\left\|\sum_K\varepsilon_K\Delta_K\right\|_H^2.
\tag{2.3}
\]

The individual squared norms do not depend on the corner, so
\(V_{\tau,H}(F_\varepsilon)=V_{\tau,H}(F)\).  Independent fair signs kill
all cross terms in (2.3), giving

\[
\mathbb E_\varepsilon A_{\tau,H}(F_\varepsilon)
=\sum_K\|\Delta_K\|_H^2
=V_{\tau,H}(F).
\tag{2.4}
\]

This proves (1.3) using only genuine exact factors.

---

## 3. The sealed MSW components and their exact norms

The MSW factor is indexed by Dyck words of semilength \(m\).  For every
Dyck suffix \(R\in\mathcal D_{m-2}\), the two roots

\[
1100R,\qquad 1010R
\tag{3.1}
\]

form the left side of one sealed two-wreath component for
\(\tau=(2\ 3)\).  Distinct suffixes give distinct components.  Thus there
are exactly

\[
J_m=\operatorname{Cat}_{m-2}
\tag{3.2}
\]

such pairwise independent components.

For completeness, their sealing follows from the four omitted-label words

\[
\begin{aligned}
C&=(4,2,3,1,T),&D&=(2,1,4,3,T),\\
C'&=(4,3,2,1,T),&D'&=(3,1,4,2,T),
\end{aligned}
\tag{3.3}
\]

where \(T\) is the common suffix.  At every middle-window cut, the two
old selected prefix sets and the two new selected prefix sets agree as
multisets.  At the two exceptional cuts the four selected prefix
singletons are, on both sides, \(\{1,2,3,4\}\).  Hence

\[
\mathcal W_m(C)\mathbin{\dot\cup}\mathcal W_m(D)
=
\mathcal W_m(C')\mathbin{\dot\cup}\mathcal W_m(D').
\tag{3.4}
\]

No edge of the middle-set ownership overlay leaves these two rows.  The
pair cannot split into singleton components, because that would make one
odd cyclic order invariant under a single coordinate transposition; a
nonidentity dihedral permutation on \(2m+1\ge5\) positions is not a single
transposition.  Thus (3.1) is a genuine connected component.

The all-rank norm is equally explicit.  Write the common tail in its two
parity lists \(\mathsf E,\mathsf O\), and put

\[
\partial X=e_{X\cup\{3\}}-e_{X\cup\{2\}}.
\]

For \(2\le r\le m-1\), the rank-\(r\) effect of one component is

\[
\Delta_r=
\partial\operatorname{suf}_{r-1}(\mathsf O)
+\partial\operatorname{suf}_{r-1}(\mathsf E)
-\partial\operatorname{pre}_{r-1}(\mathsf E)
-\partial\operatorname{pre}_{r-1}(\mathsf O).
\tag{3.5}
\]

Indeed a cyclic rank-\(r\) interval cancels between the four words unless
it contains exactly one of the four exceptional positions.  There is one
surviving interval at each exceptional position, and its common core is
one of the four prefix/suffix sets in (3.5).

For \(2\le r\le m-2\), the four cores are distinct and avoid
\(2,3\).  Each \(\partial\)-term has two unit entries, so

\[
\|\Delta_r\|_2^2=8.
\tag{3.6}
\]

At \(r=m-1\), the two \(\mathsf O\)-terms cancel and the two
\(\mathsf E\)-terms form one four-entry square.  Hence

\[
\|\Delta_{m-1}\|_2^2=4.
\tag{3.7}
\]

The middle rank \(r=m\) is unchanged by (3.4).  Equations (3.6)--(3.7)
are deterministic identities for every suffix \(R\).

Take \(r=m-q\).  For fixed \(L\) and all sufficiently large \(m\),
\(H\le m-2\).  Thus every component in (3.2) contributes exactly

\[
\|\Delta\|_H^2
=\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}.
\tag{3.8}
\]

Since

\[
\frac W{\binom n{m-1}}=\frac{m+2}{m}\in(1,2)
\]

for \(m\ge3\), one has \(c_1=1\).  The full component variance contains
all the nonnegative contributions of these sealed components.  Summing
(3.8) over (3.2) proves (1.1).

---

## 4. Floor-corrected mesoscopic asymptotics

Uniformly for \(q\le L\sqrt m+1\),

\[
\lambda_q:=\frac W{\binom n{m-q}}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}
\tag{4.1}
\]

and Taylor expansion gives

\[
\log\lambda_q
=\frac{q(q+1)}m
+O_L(m^{-1/2}).
\tag{4.2}
\]

Hence, at every \(x\in[0,L]\) for which \(e^{x^2}\) is not an integer,

\[
\frac1{c_{\lfloor x\sqrt m\rfloor}}
\longrightarrow
\frac1{\lfloor e^{x^2}\rfloor}.
\]

The exceptional \(x\)'s are the finitely many points
\(\sqrt{\log k}\le L\).  The summands are bounded by one and are monotone
step functions between these crossings.  Ordinary Riemann-sum convergence
therefore gives

\[
\frac1{\sqrt m}\sum_{q=1}^H\frac1{c_q}
\longrightarrow I_L.
\tag{4.3}
\]

Also

\[
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
=
\frac{m(m+1)}{4(2m-1)(2m-3)}
\longrightarrow\frac1{16}.
\tag{4.4}
\]

Substituting (4.3)--(4.4) into (1.1) gives

\[
V_{\tau,H}
\ge
\left(\frac12 I_L+o_L(1)\right)t\sqrt m
=
\left(\frac{I_L}{2L}+o_L(1)\right)Ht,
\]

which proves (1.2).  Since the integrand defining \(I_L\) is positive,
the constant is strictly positive for every fixed \(L>0\).

There is a useful comparison with the exact integer floor.  Put

\[
\beta_q=N_q\{\lambda_q\}(1-\{\lambda_q\}),
\qquad
B_H=\sum_{q\le H}\frac{\beta_q}{c_q}.
\]

The floor Riemann sum is

\[
\frac{B_H}{W\sqrt m}\longrightarrow
\kappa_L:=
\int_0^L
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.
\tag{4.5}
\]

The unavoidable slow-\(U_2\) replenishment in the floor-corrected heat
recurrence is \(2B_H/n\).  The sealed components alone have noise trace

\[
\frac14V_{\tau,H}^{\rm sealed}
\sim \frac{I_L}{8}t\sqrt m.
\]

Consequently

\[
\frac{V_{\tau,H}^{\rm sealed}/4}{2B_H/n}
\longrightarrow\frac{I_L}{16\kappa_L}.
\tag{4.6}
\]

Thus genuine microscopic components already live on the exact
floor-replenishment scale.  Formula (4.6) is a scale comparison, not an
isotype claim: the sealed effects may contain Johnson degrees above two,
whose separate spectral rebate must still be retained.

---

## 5. Quantitative no-go for multiplicative variance domination

Let \(\mathscr C_m\) be the genuine \((2\ 3)\)-ownership cell containing
\(F_m^{\rm MSW}\).  By (2.4),

\[
\mathbb E_{G\in\mathscr C_m}
[A_{\tau,H}(G)-V_{\tau,H}(G)]=0.
\tag{5.1}
\]

Therefore at least one corner \(G_m\in\mathscr C_m\) satisfies

\[
A_{\tau,H}(G_m)\le V_{\tau,H}(G_m).
\tag{5.2}
\]

Every corner has the same component norms, so (1.2) holds at \(G_m\):

\[
V_{\tau,H}(G_m)
\ge(\gamma_L+o_L(1))Ht,
\qquad
\gamma_L=\frac{I_L}{2L}>0.
\tag{5.3}
\]

To retain the natural \(1/n\) coefficient, assume (1.6) holds at every
exact factor and average it over all corners of \(\mathscr C_m\).
Equations (2.4) and (5.1) give

\[
0\ge(a_m+b_m)V_{\tau,H}-r_m.
\]

Now use (1.2).  This proves (1.7), and (1.8) follows when
\(a_m+b_m\ge\eta_L/n\).

Suppose (1.4) held for every exact factor.  At \(G_m\), its left side is
nonpositive by (5.2), while its right side is

\[
\eta(\gamma_L+o_L(1))Ht-o_L(Ht)>0
\]

for large \(m\), a contradiction.

Suppose instead that (1.5) held.  Since \(0\le A_{\tau,H}(G_m)\le
V_{\tau,H}(G_m)\),

\[
V_{\tau,H}(G_m)-(1-\eta)A_{\tau,H}(G_m)
\ge \eta V_{\tau,H}(G_m)
\ge(\eta\gamma_L+o_L(1))Ht,
\]

again contradicting \(r_m=o_L(Ht)\).  This proves both no-go statements.

The argument uses neither an independent-occupancy model nor a formal
component pattern.  Every corner used above is an integral exact wreath
factor.

---

## 6. Exact surviving statement

The no-go has a precise boundary.

1. It rules out suppressing genuine component variance by a fixed
   multiplicative factor with sub-mesoscopic additive slack.
2. It does not prove a corner with
   \(V_{\tau,H}-A_{\tau,H}=\Omega_L(Ht)\).  The zero trace (5.1) gives a
   nonpositive gap corner but no quantitative negative tail.
3. It does not refute an additive ceiling
   \(V_{\tau,H}\le A_{\tau,H}+C_LHt\), or even prove that
   \(o_L(Ht)\) additive slack is impossible.  The sealed components force
   the raw variance and the floor replenishment to have scale \(Ht\), but
   the zero-trace identity alone does not force the difference \(V-A\) to
   have that scale at any corner.
4. A single bad transposition has weight \(\binom n2^{-1}\) under uniform
   transposition averaging.  Thus this fixed-cell theorem does not refute
   the scale-correct averaged drift target

   \[
   \frac14\mathbb E_\tau(A_{\tau,H}-V_{\tau,H})
   \ge
   \frac{\eta_L}{n}\mathcal Q_H
   -\frac{C_L}{n}Ht.
   \tag{6.1}
   \]

The next exact statement in this lane is therefore not another raw
variance estimate.  It must control the **transposition-averaged,
floor-corrected difference** in (6.1), with the \(U_2\) floor term and the
higher-harmonic rebate kept separately, or it must use a suffix-filtered
adaptive sequence in which ownership components are recomputed.  Harmonic
margins and one fixed component cube cannot supply such a bias: the former
leave the physical \(U_2\) mode, while the latter has the exact zero trace
(5.1).
