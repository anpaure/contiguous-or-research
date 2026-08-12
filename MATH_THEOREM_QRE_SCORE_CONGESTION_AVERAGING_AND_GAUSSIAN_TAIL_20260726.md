# QRE score/congestion averaging and the surviving Gaussian lower tail

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Fix one sign and one Gaussian depth

\[
                         q=A\sqrt m+O(1),\qquad A>0,
\]

in the independent-rank-matching maximal graph.  Let \(\tau\) denote an
ordered target half-count profile and \(\kappa\) an ordered middle-owner
profile.  For \(T\in\tau\), let \(R_{\tau\kappa}(T)\) be the exact
overlap-component source/target ratio; it is zero when \(\tau\) is not a
predecessor of \(\kappa\).

This note proves the exact profile-congestion averaging lemma suggested by
the full ordered-profile score.  If

\[
 p_\kappa=\#\{\tau:R_{\tau\kappa}\not\equiv0\},
 \qquad
 H_\tau(T)=\sum_\kappa {R_{\tau\kappa}(T)\over p_\kappa},
\tag{0.1}
\]

then the full raw weighted Hall dual follows from the pointwise condition

\[
                         H_\tau(T)\ge1.             \tag{0.2}
\]

In particular, if \(p_\kappa\le P\) and
\(K_\tau(T):=\sum_\kappa R_{\tau\kappa}(T)\ge P\), then Hall holds.

The condition does not hold automatically.  Restricting to allocations
with at most two promotions in a macroblock, every central source profile
has exactly

\[
 D_{b,q}=[z^q](1+2z+3z^2)^b                         \tag{0.3}
\]

predecessor profiles.  Put

\[
 K_{\tau,2}(T)=
   \sum_{\substack{\kappa:\text{at most two}\\
                         \text{promotions per block}}}
                 R_{\tau\kappa}(T),
 \qquad
 H_{\tau,2}(T)={K_{\tau,2}(T)\over D_{b,q}}.        \tag{0.4}
\]

On every typical ordered profile,

\[
 \boxed{
 \log H_{\tau,2}(T)=C_\tau+2A Z_\tau(T)+o_{\mathbb P}(1),
 \qquad Z_\tau\Rightarrow N(0,1),}                 \tag{0.5}
\]

with convergence of exponential moments on every fixed compact interval.
The deterministic constant \(C_\tau\) may depend on the ordered profile;
no false profile-uniform value is asserted.

Exact mass conservation nevertheless gives

\[
 {1\over N_q}\sum_T H_{\tau(T),2}(T)=e^{A^2+o(1)}. \tag{0.6}
\]

Combining (0.5)--(0.6) yields a uniform positive lower tail:

\[
 \boxed{
 {1\over N_q}\#\{T:H_{\tau(T),2}(T)<1\}
 \ge {1\over2}\Phi\!\left({A^2-\log2\over2A}\right)-o(1)>0.} \tag{0.7}
\]

Thus the sharp profile-count/entropy averaging certificate fails on a
linear target family.  The enormous unweighted score and the enormous
predecessor count cancel at leading entropy; the residual matching-overlap
carrier has constant Gaussian width.

Equation (0.7) is not a Farkas counterexample to unrestricted QRE.  The
exact dual contains a maximum over predecessor target profiles at every
source profile, and a nonuniform macroscopic rerouting may beat uniform
predecessor averaging.  What (0.7) proves is that neither the certified
lower bound for \(K_\tau\), nor the exact predecessor count, nor their
sharp asymptotic comparison closes raw Hall.  A positive theorem must use
the weighted allocation capacities themselves.

This is precisely the fixed-array first-moment gate immediately upstream
of CPCR.  The diverse compiler has already removed within-packet repeats;
CPCR still requires a legal moving-frame/cross-parent state with balanced
two-point floor covariance, which is strictly stronger than repairing
(0.7).

## 1. Exact congestion-averaging lemma

For a nonnegative raw target weight \(y=(y_T)\), put

\[
 A_{\tau\kappa}(y)
 =\sum_{T\in\tau}y_TR_{\tau\kappa}(T).              \tag{1.1}
\]

The exact weighted LP dual is

\[
 \sum_Ty_T\le\sum_\kappa\max_\tau A_{\tau\kappa}(y).
\tag{1.2}
\]

### Lemma 1.1 (predecessor-profile averaging)

For every \(y\ge0\),

\[
 \boxed{
 \sum_\kappa\max_\tau A_{\tau\kappa}(y)
 \ge\sum_Ty_TH_{\tau(T)}(T).}                     \tag{1.3}
\]

Consequently (0.2) implies the full raw weighted Hall dual.

#### Proof

For fixed \(\kappa\), average only over its \(p_\kappa\) predecessor
profiles:

\[
 \max_\tau A_{\tau\kappa}(y)
 \ge {1\over p_\kappa}\sum_\tau A_{\tau\kappa}(y).
\]

Summing \(\kappa\) and reversing the finite sums gives

\[
 \sum_\kappa\max_\tau A_{\tau\kappa}(y)
 \ge\sum_{\tau,T\in\tau}y_T
          \sum_\kappa{R_{\tau\kappa}(T)\over p_\kappa},
\]

which is (1.3).  If every inner sum is at least one, (1.2) follows for
every \(y\). \(\square\)

More generally one may replace \(p_\kappa^{-1}\) by arbitrary weights
\(c_{\tau\kappa}\ge0\) satisfying

\[
                         \sum_\tau c_{\tau\kappa}\le1.
\tag{1.4}
\]

This recovers exactly the weighted allocation-score theorem.  Uniform
predecessor averaging is therefore the strongest conclusion obtainable
from profile counts alone; any improvement must choose nonuniform
capacities using the actual component ratios.

## 2. Exact central predecessor count

Let the core have \(b=m/d+O(1)\) macroblocks.  Restrict temporarily to
allocations

\[
                         \alpha_j+\gamma_j\le2.
\tag{2.1}
\]

In a central owner profile every half count is at least two and at most
\(d-2\).  In one block there is one zero-promotion choice, two one-promotion
choices, and three two-promotion choices.  Hence the number of lower
predecessor profiles is exactly (0.3).  Complementation gives the same
upper count.

The saddle \(z_0\) of the coefficient in (0.3) satisfies

\[
                         z_0={q\over2b}(1+o(1))
                              ={Ad\over2\sqrt m}(1+o(1)).        \tag{2.2}
\]

Since \(q=o(b)\),

\[
 \log D_{b,q}
 =q\log{2eb\over q}+O(q^2/b+\log q)
 =\left({A\over2}+o(1)\right)\sqrt m\log m.        \tag{2.3}
\]

Allowing arbitrary promotions in one block changes the local predecessor
series to \((1-z)^{-2}\) and the total count to
\(\binom{2b+q-1}{q}\).  At (2.2), allocations of order at least three have
total logarithmic mass

\[
                         O(bz_0^3)=O(d^2/\sqrt m)=o(1).          \tag{2.4}
\]

Thus the two-promotion restriction changes neither the leading entropy nor
the constant Gaussian calculation below.

The finite half-count caps also have negligible effect on the central
core.  If every available half capacity is at least \(c d\), the fraction
of weak \(2b\)-part compositions of \(q\) violating one of the caps is at
most

\[
                         2b\left({q\over2b}\right)^{cd}
                              =e^{-\Theta((\log m)^2)}.           \tag{2.5}
\]

Hence the full predecessor count equals
\((1-o(1))\binom{2b+q-1}{q}\) on every retained central source profile.

## 3. Exact score polynomial

Fix a lower ordered target profile

\[
                         \tau=((a_j,c_j))_{j\le b}.
\]

Relative to the rank-\((a_j+c_j+1)\) matching, write a target's local
statuses as

\[
 (f_j,p_j,s_j,e_j)
 =(f_j,a_j-f_j,c_j-f_j,d-a_j-c_j+f_j).
\tag{3.1}
\]

The exact one-promotion coefficient is

\[
 r_j(T)=e_j\left({1\over p_j+1}+{1\over s_j+1}\right).         \tag{3.2}
\]

Let \(w_j(T)\) be the sum of the three exact component ratios with two
promotions in block \(j\), evaluated in the rank-\((a_j+c_j+2)\)
matching.  The overlap-component decomposition gives the exact identity

\[
 \boxed{
 K_{\tau,2}(T)
 =[z^q]\prod_{j=1}^b(1+r_j(T)z+w_j(T)z^2).}         \tag{3.3}
\]

On the safe overlap core, \(r_j=O(1)\) and \(w_j=O(1)\) uniformly.  The
family where a required singleton or empty/full count exits a fixed
compact fraction of \(d\) has relative mass \(e^{-\Omega(d)}\) per block
and hence total mass \(o(N_q)\) after the usual choice of \(d=C\log m\).

The upper identity is identical with full and empty edges interchanged.

## 4. Conditional Gaussian saddle

Fix a typical safe ordered profile.  Under its uniform raw target measure,
the blocks are independent and

\[
 f_j\sim\operatorname{Hyp}(d,c_j,a_j),
 \qquad
 \operatorname{Var}f_j
 ={a_jc_j(d-a_j)(d-c_j)\over d^2(d-1)}.             \tag{4.1}
\]

Put \(\bar f_j=a_jc_j/d\).  Taylor expansion of (3.2) gives

\[
 r_j-\mathbb Er_j
 =\beta_j(f_j-\bar f_j)+\xi_j,                     \tag{4.2}
\]

where, uniformly on the safe compact core,

\[
 \beta_j={16\over d}
 +O\!\left({|a_j-d/2|+|c_j-d/2|+1\over d^2}\right),            \tag{4.3}
\]

and

\[
                         z_0\sum_j\xi_j=o_{\mathbb P}(1).       \tag{4.4}
\]

To verify (4.4), the second derivative of (3.2) is \(O(d^{-2})\);
after subtracting its mean, one block remainder has standard deviation
\(O(d^{-1})\).  Hence the sum has standard deviation
\(O(\sqrt b/d)\), which becomes \(O(d^{-1/2})\) after multiplication by
\(z_0=\Theta(d/\sqrt m)\).

Typical ordered profiles satisfy the empirical central moment bounds

\[
 {1\over b}\sum_j
 \left((a_j/d-1/2)^2+(c_j/d-1/2)^2\right)=O(d^{-1}).            \tag{4.5}
\]

Equations (2.2), (4.1)--(4.5) give

\[
 z_0^2\sum_j\beta_j^2\operatorname{Var}f_j
                         =4A^2+o(1).              \tag{4.6}
\]

The Lindeberg condition follows from \(d=o(\sqrt m)\).  Consequently

\[
                         z_0\sum_j(r_j-\mathbb Er_j)
                              \Rightarrow N(0,4A^2).             \tag{4.7}
\]

It remains to pass from the first coefficients to (3.3).  Uniformly for
\(z\asymp z_0\),

\[
 \sum_j\log(1+r_jz+w_jz^2)
 =z\sum_jr_j+z^2\sum_j(w_j-r_j^2/2)+O(bz^3).        \tag{4.8}
\]

The last term is \(O(d^2/\sqrt m)=o(1)\).  The centered quadratic sum,
after multiplication by \(z_0^2\), is
\(O_{\mathbb P}(d^{3/2}/\sqrt m)=o(1)\).  Exponential tilting followed by
the local central limit theorem for a sum of independent
\(\{0,1,2\}\)-valued variables therefore gives a deterministic
profile constant \(C_\tau\) such that

\[
 \log {K_{\tau,2}(T)\over D_{b,q}}
 =C_\tau+z_0\sum_j(r_j-\mathbb Er_j)+o_{\mathbb P}(1).          \tag{4.9}
\]

The same estimates with a fixed exponential tilt of the centered linear
sum prove convergence of exponential moments.  Equations (4.7)--(4.9)
prove (0.5).  Complementation proves the upper statement.

On the safe overlap core the local order-\(\ell\) component-score sum is
at most \(C^\ell(\ell+1)\) for a fixed absolute \(C\).  Therefore, at
the saddle (2.2), the total logarithmic contribution of all
\(\ell\ge3\) terms is again \(O(bz_0^3)=o(1)\).  Together with (2.5),
this shows that the **full** score divided by the full predecessor count
has the same law (0.5).  The two-promotion truncation is only a convenient
exact polynomial representation, not a weakening at Gaussian order.

## 5. Exact global mean

For one arc \((\tau,\kappa)\), overlap-component double counting gives

\[
                         \sum_{T\in\tau}R_{\tau\kappa}(T)
                              =E_{\tau\kappa}\le|\kappa|,       \tag{5.1}
\]

where \(E_{\tau\kappa}\) is the number of source owners in \(\kappa\)
which see the prescribed predecessor profile.  On a safe arc satisfying
(2.1), uniform visibility gives

\[
                         E_{\tau\kappa}=(1-o(1))|\kappa|.       \tag{5.2}
\]

Every retained central owner profile has \(D_{b,q}\) predecessor profiles.
Summing (5.1)--(5.2), first over target profiles and then over owner
profiles, yields

\[
 \begin{aligned}
 \sum_TK_{\tau(T),2}(T)
 &=\sum_{\tau,\kappa}E_{\tau\kappa}\\
 &=(1-o(1))D_{b,q}W.
 \end{aligned}                                                     \tag{5.3}
\]

The unsafe target and owner profiles have \(o(N_q)\) and \(o(W)\) mass,
respectively.  Dividing (5.3) by \(D_{b,q}N_q\) proves (0.6).

This conservation argument intentionally does not assign one value to
\(C_\tau\).  Ordered half-count fluctuations can move that constant by
\(O(1)\); only their global weighted mean is needed.

## 6. A linear lower tail

Let

\[
 M_\tau={1\over|\tau|}
       \sum_{T\in\tau}H_{\tau,2}(T).
\tag{6.1}
\]

By (0.6), the \(|\tau|\)-weighted average of \(M_\tau\) over retained
target profiles is \(e^{A^2+o(1)}\).  Markov's inequality shows that
profiles of total target mass at least \((1/2-o(1))N_q\) satisfy

\[
                         M_\tau\le2e^{A^2+o(1)}.                 \tag{6.2}
\]

For such a typical profile, (0.5) and exponential-moment convergence give

\[
                         M_\tau=e^{C_\tau+2A^2+o(1)}.
\tag{6.3}
\]

Hence

\[
                         C_\tau\le\log2-A^2+o(1).               \tag{6.4}
\]

Using (0.5) once more,

\[
 \Pr_{T\in\tau}\{H_{\tau,2}(T)<1\}
 \ge
 \Phi\!\left({A^2-\log2\over2A}\right)-o(1).                  \tag{6.5}
\]

The right side is a positive constant for every fixed \(A>0\).  Summing
over the profiles in (6.2) proves (0.7).

Thus the carrier lower tail is not an artifact of one quotient-flow
normalization.  It already survives the sharp uniform averaging over all
predecessor profiles.

### Proposition 6.1 (failure of the average is not a Farkas cut)

The implication in Lemma 1.1 cannot be reversed.  Even for one target
coordinate and two predecessor source profiles, take arc scores

\[
                         R_1=0,qquad R_2={3\over2}.
\]

Uniform predecessor averaging gives \(H=3/4<1\), whereas the exact dual
support function uses \(\max(R_1,R_2)=3/2\ge1\).  Direct sums give the
same separation for arbitrarily many target coordinates.

Therefore the positive-density failure in (0.7) is a rigorous no-go for
the profile-count/entropy proof, but it is not itself a violating dual
weight.  To refute QRE one must additionally show that the low-score
targets align so that the maxima in (1.2) cannot reroute them among their
predecessor profiles.  No such rank-diverse alignment theorem is proved
here.

## 7. What this settles

The following are proved.

1. Lemma 1.1 is the exact Hall theorem obtainable by comparing the full
   ordered-profile score with predecessor-profile congestion.
2. Score and congestion have the same leading entropy.
3. Their normalized ratio has a nondegenerate Gaussian overlap carrier.
4. The pointwise uniform-averaging certificate fails on a linear target
   family, for both signs.

The following are not proved.

1. A violating weight vector for the unrestricted max-dual (1.2).
2. Failure of every nonuniform capacity system (1.4).
3. Raw QRE failure for independent rank matchings.
4. CPCR or coefficient one.

Accordingly, profile counting is exhausted as a proof route.  A successful
fixed-array QRE theorem must choose capacities using the actual
rank-diverse component ratios, macroscopically differently from both the
ordinary quotient flow and uniform predecessor averaging.  Alternatively,
one must exhibit a genuine rank-diverse Farkas cut.  The present Gaussian
lower tail proves that no entropy surplus can substitute for that missing
weighted theorem.

## 8. Alignment with the diverse compiler and CPCR

The diverse-order compiler supplies exact within-packet two-sided trace
injectivity and removes the common-order syndrome.  It does not alter the
maximal-graph predecessor competition analyzed above.  The dispersed or
random-parallel selector can transfer a proved raw weighted certificate
to selected axes at \(o(W)\) additional loss, but it cannot create the
certificate.

Normalized moving-frame orbit averaging can flatten the one-point score,
which is a macroscopic operation consistent with the lower-tail obstruction.
CPCR asks for more: one legal common all-depth, two-sign state whose loads
have the extremal floor/ceiling second moment.  Even a nonuniform solution
of (1.4) would settle only the raw first-moment Hall gate.  The surviving
coefficient-one target remains the cross-parent factorial covariance of
CPCR, not packet-local chronology.
