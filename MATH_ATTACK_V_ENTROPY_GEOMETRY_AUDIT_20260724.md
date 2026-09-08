# Independent audit of the entropy--geometry lane

## Verdict

The principal convex duality, fractional-cover identity, randomized rounding,
peeling theorem, dense-residual equivalence, dimension bounds, and conditional
factor-geometric reduction are valid.  They were rederived independently.

The report nevertheless needs the following corrections and qualifications.

1. The face cost

   \[
   \gamma_C=2\nu(s)+\mathbf 1_{P\ne\varnothing}
                         +\mathbf 1_{N\ne\varnothing}
   \]

   is the exact length of the stated canonical two-copy block.  It is not
   proved to be the minimum length of an arbitrary word covering that face.
   The convention \(\nu(0)=0\) must be stated.
2. Equations (2)--(3), and every expression containing a probability
   distribution on the holes or \(\log(2M/D_{\rm frac})\), require \(M>0\).
   When \(M=0\), all three objectives are separately equal to zero.
3. If \(P=N=\varnothing\), the two nominal opposite faces coincide.  The
   formal two-copy cost is \(2\nu(n)\), but one economical full-cube copy
   costs only \(\nu(n)\).  The exclusion remains harmless for an \(o(W)\)
   criterion because either cost is at least \(W\); it does not preserve the
   exact finite optimization value.
4. The rank-subset bound (12) must be restricted to nonempty sets of depths
   \(Q\).  The case \(s=0\) must be checked separately in (9)--(12); it does
   not change the conclusions.
5. Section 5, as written, does not define its abstract family to be the hole
   family.  The assertion \(|\mathcal G\cap\mathcal H_q|=\Theta_A(W/\sqrt n)\)
   is unsupported for the earlier arbitrary factor-hole family.  The intended
   valid example must explicitly reset

   \[
   \mathcal H:=\mathcal G,
   \qquad
   \mathcal H_q:=\mathcal G\cap\binom{[n]}{m-q}.
   \]
6. “Order-sharp” is correct for the Poisson functional and lower bound (12),
   but not for deterministic repair: in the example the deterministic optimum
   is smaller by a factor \(\Theta(\log n)\).
7. \(\mathrm{FG}_A\) is a valid sufficient factor theorem inside this signed-
   face architecture.  It is not a necessary condition for coefficient one,
   MWB, or even for signed-face repair when the aggregate hole count is larger
   than \(O(W)\).  Accordingly, the opening statement that it is the “sole
   remaining issue” is valid only after restricting to this particular
   \(M=O(W)\), proper-face route.
8. Failure of \(\Psi_{\le K}=o(W)\) obstructs the Poisson certificate.  It
   also obstructs deterministic signed-face repair in the \(M=O(W)\) regime,
   by (7), but not from the inequality \(D_{\rm det}\le\Psi\) alone when
   \(M\) is unrestricted.  The final obstruction language needs this scope.

After these repairs, no decisive theorem in the report is false.  The only
unsupported displayed use is the uncorrected Section 5 reference to the
earlier \(\mathcal H_q\); the broad “sole remaining issue” language also needs
the scope restriction above.

Throughout this audit, logarithms are natural, \(K<m\), holes lie only in the
nonempty lower ranks, and \(0\log0=0\).

## 1. Canonical signed-face block and endpoint cases

Let

\[
C(P,N)=\{P\cup T:T\subseteq U\}
       \cup\{N\cup T:T\subseteq U\},
\qquad U=[n]\setminus(P\cup N),
\]

where \(P\cap N=\varnothing\), and put \(s=|U|\).  Take a nonzero-mask
universal word

\[
B_1,\ldots,B_{\nu(s)}
\]

on \(U\).  Replacing every entry by \(P\cup B_i\) realizes every
\(P\cup T\) with \(T\ne\varnothing\).  If \(P\ne\varnothing\), one literal
entry \(P\) realizes the anchor-only target.  The same construction for
\(N\) gives a block of length

\[
2\nu(s)+\mathbf 1_{P\ne\varnothing}
         +\mathbf 1_{N\ne\varnothing}.
\]

All required witnesses lie internally in the two copied words or in the
literal anchors.  Concatenating different blocks adds incidental OR values but
does not destroy these witnesses and incurs no extra seam entries.

If an anchor is empty, its empty member is not produced by a nonzero-mask
word.  This is harmless here: because \(K<m\), every lower hole and its
complement are nonempty.  Explicitly set \(\nu(0)=0\).  Then the face with

\[
U=\varnothing,\qquad P=S,qquad N=S^c
\]

is the literal two-entry column \(\{S,S^c\}\) of cost two.  Within the
restricted lower-hole universe it is incident only with \(S\), since \(S^c\)
lies in the complementary upper band.

Thus the cost ledger is **valid as a canonical additive construction**.  The
report does not prove that an arbitrary face-covering word cannot be shorter,
so “literal cost” must not be read as an optimality theorem.

## 2. Fenchel dual and entropy reparametrization

Assume \(M=|\mathcal H|>0\).  For \(x\ge0\), direct differentiation gives

\[
2e^{-x}
=\max_{y\ge0}
\left\{y\left(1+\log\frac2y\right)-xy\right\}.
\]

The maximizer is \(y=2e^{-x}\le2\).  Applying this identity coordinatewise
to \(x=A\lambda\), and minimizing over \(\lambda\ge0\), yields

\[
\Psi_{\le K}
=
\max_{\substack{0\le y\le2\\A^Ty\le\gamma}}
\sum_{S\in\mathcal H}
y_S\left(1+\log\frac2{y_S}\right).
\tag{A1}
\]

This interchange is legitimate in finite dimension: the exponential term is
finite and continuous, the linear term plus the nonnegative-orthant indicator
is closed convex, and every face cost is positive.  The literal columns also
imply \(y_S\le2\), so that bound is both the conjugate endpoint and an actual
column constraint.

For nonzero \(y\), set

\[
t=\sum_Sy_S,
\qquad \pi_S=y_S/t.
\]

Writing \(\pi(C)=\sum_{S\in\mathcal H\cap C}\pi_S\), feasibility is exactly

\[
0<t\le
\min\left\{
\frac2{\|\pi\|_\infty},
\min_{C:\pi(C)>0}\frac{\gamma_C}{\pi(C)}
\right\}
=\frac1{\delta(\pi)},
\]

where

\[
\delta(\pi)=
\max\left\{
\frac{\|\pi\|_\infty}{2},
\max_C\frac{\pi(C)}{\gamma_C}
\right\}.
\]

The objective in (A1) becomes

\[
\phi_\pi(t)
=t\left(1+\operatorname{Ent}(\pi)+\log\frac2t\right),
\]

with derivative

\[
\phi_\pi'(t)=\operatorname{Ent}(\pi)+\log\frac2t.
\]

The elementary entropy inequality

\[
\operatorname{Ent}(\pi)\ge-\log\|\pi\|_\infty
\]

and the feasible bound \(t\le2/\|\pi\|_\infty\) show that this derivative is
nonnegative throughout the feasible interval.  Hence the optimum is attained
at \(t=1/\delta(\pi)\), proving

\[
\boxed{
\Psi_{\le K}
=\max_{\pi\in\mathcal P(\mathcal H)}
\frac{1+\operatorname{Ent}(\pi)+\log(2\delta(\pi))}
     {\delta(\pi)}.}
\tag{A2}
\]

This proves the report's equation (1) exactly.  When \(M=0\), the probability
simplex is absent and the separate conclusion \(\Psi_{\le K}=0\) is correct.

Classification: Fenchel dual, factor two in the conjugate, entropy identity,
derivative, and endpoint choice are **valid**.

## 3. Fractional cover, deterministic repair, and rounding

The LP dual of

\[
D_{\rm frac}
=\min\left\{
\gamma^Tx+2\mathbf1^Tz:
Ax+z\ge\mathbf1,\ x,z\ge0
\right\}
\]

is

\[
\max\left\{
\mathbf1^Ty:A^Ty\le\gamma,\ 0\le y\le2
\right\}.
\]

Putting \(y=t\pi\) shows that the best \(t\) for fixed \(\pi\) is
\(1/\delta(\pi)\).  Compactness of the simplex and
\(\delta(\pi)\ge1/(2M)>0\) give

\[
\boxed{
D_{\rm frac}
=\max_\pi\frac1{\delta(\pi)}
=\frac1{\min_\pi\delta(\pi)}.}
\tag{A3}
\]

This is valid for \(M>0\).  For \(M=0\), the reciprocal expression is
undefined and one must separately state

\[
D_{\rm frac}=D_{\rm det}=\Psi_{\le K}=0.
\]

The relaxation inequality \(D_{\rm frac}\le D_{\rm det}\) is immediate.
For any fixed \(\lambda\), independently select face \(C\) with probability

\[
p_C=1-e^{-\lambda_C}.
\]

The expected selected-block cost is at most

\[
\sum_C\gamma_Cp_C\le\sum_C\gamma_C\lambda_C.
\]

A hole \(S\) remains uncovered with probability

\[
\prod_{C\ni S}e^{-\lambda_C}=e^{-(A\lambda)_S}.
\]

Appending \(S\) and \(S^c\) costs two.  Therefore some deterministic
selection has cost no greater than the Poisson objective, and

\[
D_{\rm frac}\le D_{\rm det}\le\Psi_{\le K}.
\]

For the final inequality in (3), put \(d=D_{\rm frac}\).  For every \(\pi\),

\[
\delta(\pi)\ge1/d,
\qquad
\delta(\pi)\ge1/(2M),
\qquad
\operatorname{Ent}(\pi)\le\log M.
\]

The function

\[
g(u)=\frac{1+\log(2Mu)}u
\]

has derivative

\[
g'(u)=-\frac{\log(2Mu)}{u^2}\le0
\qquad(u\ge1/(2M)).
\]

Using (A2) and \(0<d\le2M\) gives

\[
\boxed{
\Psi_{\le K}
\le d\left(1+\log\frac{2M}{d}\right).}
\tag{A4}
\]

Thus all inequalities in (3), including their constants, are **valid for
\(M>0\)**.  The resulting \(o(W)\) criterion is an actual deterministic
literal construction criterion inside this additive signed-face architecture.

### Full-cube column

When \(P=N=\varnothing\), the two nominal faces coincide.  Under the formal
two-copy convention the column has weight \(2\nu(n)\), but one economical
copy of a universal word covers every relevant nonempty target at cost
\(\nu(n)\).  Hence \(2\nu(n)\) is not the minimum geometric cost.

The asymptotic exclusion is nevertheless correct.  Let \(\Gamma_0\ge W\)
be either the one-copy or two-copy full-column cost.  If an \(o(W)\) Poisson
certificate gives this column intensity \(\lambda_0\), then

\[
\Gamma_0\lambda_0=o(W)
\quad\Longrightarrow\quad
\lambda_0=o(1).
\]

Deleting it multiplies every residual exponential by
\(e^{\lambda_0}=1+o(1)\).  Since the old total residual charge was already
\(o(W)\), the new charge remains \(o(W)\).  Thus proper and unrestricted
columns are equivalent only for the \(o(W)\) existence criterion, not as
finite optimization problems.

Classification: full-cube factor two as a *minimum* is **unsupported**;
formal duplicated cost and asymptotic exclusion are **valid with the stated
qualification**.

## 4. Uniform residual certificates and peeling

For nonempty \(\mathcal G\subseteq\mathcal H\), the literal column above
shows that density \(1/2\) is genuinely attained.  Therefore

\[
\rho(\mathcal G)
=\max\left\{
\frac12,\max_C\frac{|\mathcal G\cap C|}{\gamma_C}
\right\}
\]

is not using an artificial endpoint.  For uniform \(\pi\) on \(\mathcal G\),

\[
\delta(\pi)=\frac{\rho(\mathcal G)}{|\mathcal G|}.
\]

Substitution in (A2)--(A3) proves exactly

\[
D_{\rm frac}\ge\frac{|\mathcal G|}{\rho(\mathcal G)},
\qquad
\Psi_{\le K}\ge
|\mathcal G|\frac{1+\log(2\rho(\mathcal G))}
                    {\rho(\mathcal G)}.
\]

Thus (4) is **valid**.

Assume (5) for \(R\ge1/2\).  While the residual has more than \(u\) holes,
choose a face meeting it in \(b_i\) holes with

\[
r_i:=b_i/\gamma_i\ge R.
\]

For \(R=1/2\), a literal column supplies the endpoint if no larger face does.
Delete the entire current intersection with the chosen face.  The deleted
batches are disjoint, so

\[
\sum_i b_i\le M,
\qquad
\sum_i\gamma_i\le M/R.
\]

Selecting every chosen face and literally repairing the final at most \(u\)
holes gives

\[
D_{\rm det}\le M/R+2u.
\]

For the Poisson construction choose

\[
\lambda_i=\log(2r_i)\ge0.
\]

Every hole deleted at step \(i\) receives exposure at least \(\lambda_i\).
Its assigned block-plus-residual charge is bounded by

\[
\gamma_i\lambda_i+2b_ie^{-\lambda_i}
=\gamma_i(1+\log(2r_i))
=b_i f(r_i),
\]

where \(f(r)=(1+\log(2r))/r\).  Since

\[
f'(r)=-\frac{\log(2r)}{r^2}\le0
\qquad(r\ge1/2),
\]

summation and the final literal repair give

\[
\Psi_{\le K}\le2u+Mf(R).
\]

This proves (6), including the endpoint \(R=1/2\), exactly.

If peeling stalls at nonempty \(\mathcal G\) with \(\rho(\mathcal G)<R\),
put \(y_S=1/R\) on \(\mathcal G\) and zero elsewhere.  Then \(y\le2\), and

\[
\sum_{S\in C}y_S
=\frac{|\mathcal G\cap C|}{R}<\gamma_C.
\]

It is therefore dual-feasible and gives the explicit values

\[
\frac{|\mathcal G|}{R}
\quad\text{for the cover LP},
\qquad
|\mathcal G|f(R)
\quad\text{for the entropy dual}.
\]

At \(R=1/2\), such a stall cannot occur.  The report's matching alternative
is **valid**.

## 5. Equivalence for \(M=O(W)\)

Interpret (8) as the sequential statement

\[
\forall\varepsilon>0:\quad
\inf_{\substack{\mathcal G\subseteq\mathcal H_m\\
|\mathcal G|\ge\varepsilon W_m}}
\rho_m(\mathcal G)\longrightarrow\infty,
\tag{A5}
\]

with the infimum of an empty family equal to \(+\infty\).

Necessity follows from (4): if \(D_{\rm frac}=o(W)\), then uniformly for
\(|\mathcal G|\ge\varepsilon W\),

\[
\rho(\mathcal G)
\ge\frac{|\mathcal G|}{D_{\rm frac}}
\ge\frac{\varepsilon W}{D_{\rm frac}}
\longrightarrow\infty.
\]

Conversely suppose \(M\le CW\) and (A5) holds.  Given \(\eta>0\), first
choose fixed \(\varepsilon>0\) and then fixed \(R\) so large that

\[
2\varepsilon+C f(R)<\eta.
\]

Eventually every residual of size at least \(\varepsilon W\) has density at
least \(R\), so (6), with \(u=\varepsilon W\), gives

\[
\Psi_{\le K}/W<\eta.
\]

The same argument handles \(D_{\rm det}\).  Finally, if
\(D_{\rm frac}/W=x_m\to0\), equation (A4) and \(M\le CW\) give

\[
\frac{\Psi_{\le K}}W
\le x_m\left(1+\log\frac{2C}{x_m}\right)
\longrightarrow0.
\]

Together with the sandwich inequalities, this proves the complete equivalence
in (7)--(8).  The hypothesis \(M=O(W)\) is essential to this proof and is not
merely cosmetic.  If \(M=o(W)\), condition (8) may be vacuous, but literal
repair already proves all three costs are \(o(W)\).

Classification: (7)--(8) are **valid with the stated sequence quantifiers,
empty-infimum convention, and eventual uniform bound \(M\le CW\)**.

## 6. Fixed-rank and dimension bounds

Let \(s=|U|\ge1\), and fix rank \(r=m-q\).  With out-of-range binomial
coefficients interpreted as zero,

\[
|C(P,N)\cap\tbinom{[n]}r|
=\binom{s}{r-|P|}+\binom{s}{r-|N|}
\le2\binom{s}{\lfloor s/2\rfloor}.
\]

The standard endpoint-throughput lower bound gives

\[
\nu(s)\ge\binom{s}{\lfloor s/2\rfloor},
\]

so the last quantity is at most \(\gamma_C\).  Hence a face of density at
least \(R\) must meet holes on at least \(\lceil R\rceil\) distinct depths.
This proves (9).

Also

\[
|C(P,N)|\le2^{s+1},
\qquad
\gamma_C\ge2\binom{s}{\lfloor s/2\rfloor}
\ge\frac{2^{s+1}}{\sqrt{2(s+1)}}.
\]

Therefore

\[
\frac{|\mathcal G\cap C|}{\gamma_C}
\le\sqrt{2(s+1)}.
\]

If the left side is at least \(R\), then

\[
s\ge R^2/2-1.
\]

Thus (10)--(11), including their constants, are **valid**.

For \(s=0\), a proper relevant face contains at most one lower-band hole and
has cost two, so its density is at most \(1/2\).  The conclusions above remain
true, but this endpoint requires the separate sentence; the displayed
central-binomial derivation does not cover it.

## 7. Rank-subset bound

Let \(Q\subseteq\{1,\ldots,K\}\) be nonempty and put

\[
\mathcal G_Q=\bigsqcup_{q\in Q}\mathcal H_q,
\qquad M_Q=|\mathcal G_Q|,
\qquad L_Q=\min\{|Q|,\sqrt{2n}\}.
\]

Equation (9) gives

\[
\frac{|\mathcal G_Q\cap C|}{\gamma_C}\le|Q|.
\]

Properness implies \(s\le n-1\), so (10) gives the second bound

\[
\frac{|\mathcal G_Q\cap C|}{\gamma_C}\le\sqrt{2n}.
\]

The \(s=0\) endpoint has density at most \(1/2\).  Consequently

\[
\rho(\mathcal G_Q)\le L_Q.
\]

Applying (4), and using that \(f\) is decreasing, proves

\[
\boxed{
D_{\rm frac}\ge\frac{M_Q}{L_Q},
\qquad
\Psi_{\le K}\ge
\frac{1+\log(2L_Q)}{L_Q}M_Q.}
\]

If \(M_Q=0\), these inequalities are trivially true.  If \(Q=\varnothing\),
however, \(L_Q=0\) and the display is undefined.  This is the required domain
correction to (12).

Moreover, for every nonempty \(Q\),

\[
\frac{M_Q}
{W L_Q/(1+\log(2L_Q))}
\le\frac{\Psi_{\le K}}W.
\]

Thus the little-oh consequence is uniform over all rank subsets.  For
\(K=\lceil A\sqrt m\rceil\), one has

\[
L_{\{1,\ldots,K\}}=\Theta_A(\sqrt m),
\qquad
\log(2L)=\tfrac12\log m+O_A(1),
\]

which yields

\[
\sum_{q\le K}M_q
=o\left(\frac{W\sqrt m}{\log m}\right).
\]

Classification: (12) and its consequences are **valid after restricting to
nonempty \(Q\) and handling \(s=0\) separately**.

## 8. Abstract compressed-hole example

The example must first be repaired notationally.  Choose even

\[
d=\tfrac12\log_2n+O(1),
\]

split a fixed \(d\)-set equally as \(D=P\sqcup N\), let \(s=n-d\), and
define

\[
\mathcal G_q
=C(P,N)\cap\binom{[n]}{m-q},
\qquad
\mathcal G=\bigsqcup_{q=1}^{\lceil A\sqrt m\rceil}\mathcal G_q.
\]

For this abstract example, explicitly set

\[
\boxed{\mathcal H:=\mathcal G,\qquad\mathcal H_q:=\mathcal G_q.}
\tag{A6}
\]

Without (A6), the original statement involving the earlier arbitrary
factor-hole family is unsupported.

Because \(s\) is odd and \(|P|=|N|=d/2\),

\[
|\mathcal G_q|
=2\binom{s}{\lfloor s/2\rfloor-q}.
\]

Uniform local central-binomial estimates for
\(1\le q\le A\sqrt m\) give

\[
\binom{s}{\lfloor s/2\rfloor-q}
=\Theta_A(2^s/\sqrt s).
\]

Since \(2^d=\Theta(\sqrt n)\) and
\(W=\Theta(2^n/\sqrt n)\), this yields

\[
|\mathcal G_q|=\Theta_A(W/\sqrt n),
\qquad
|\mathcal G|=\Theta_A(W).
\]

Using the inherited constant-factor upper bound

\[
\binom{s}{\lfloor s/2\rfloor}
\le\nu(s)
=O\!\left(\binom{s}{\lfloor s/2\rfloor}\right),
\]

and noting that both anchors are nonempty, gives

\[
\gamma_C=2\nu(s)+2
=\Theta(W/\sqrt n).
\]

The chosen face gives

\[
\rho(\mathcal G)
\ge |\mathcal G|/\gamma_C
=\Omega_A(\sqrt n),
\]

while (10) gives \(\rho(\mathcal G)=O(\sqrt n)\).  Therefore

\[
\rho(\mathcal G)=\Theta_A(\sqrt n).
\]

One-face intensity

\[
\lambda=\log\frac{2|\mathcal G|}{\gamma_C}
\]

gives

\[
\Psi_{\le K}
\le
\gamma_C\left(1+\log\frac{2|\mathcal G|}{\gamma_C}\right)
=O_A(W\log n/\sqrt n).
\]

Conversely, the uniform-distribution lower certificate (4) gives

\[
\Psi_{\le K}
\ge|\mathcal G|f(\rho(\mathcal G))
=\Omega_A(W\log n/\sqrt n).
\]

Thus the claimed order

\[
\Psi_{\le K}=\Theta_A(W\log n/\sqrt n)=o(W)
\]

is **valid after correction (A6)**; it is not merely an upper estimate.

A single deterministic copy of the chosen block costs
\(\gamma_C=\Theta(W/\sqrt n)\) and covers all holes.  The lower bound

\[
D_{\rm frac}\ge|\mathcal G|/\rho(\mathcal G)
=\Theta(W/\sqrt n)
\]

shows that both fractional and deterministic optima have this order.  Hence
the example exhibits a genuine \(\Theta(\log n)\) gap between the Poisson
functional and deterministic face selection.

It is order-sharp for the universal **Poisson** rank-subset lower bound (12).
It is not order-sharp for deterministic repair.  It remains an abstract hole
family and is not shown to arise from any exact wreath factor.

## 9. Audit of \(\mathrm{FG}_A\) and its implications

Assume \(\mathrm{FG}_A\).  Take

\[
R=R_m,
\qquad
u=W/R_m,
\qquad
M\le C_AW
\]

in the peeling theorem.  Every residual with more than \(u\) holes satisfies
the required density condition, so

\[
\frac{\Psi_{\le K}}W
\le
\frac2{R_m}
+C_A\frac{1+\log(2R_m)}{R_m}
\longrightarrow0.
\]

The report's extra \(+o(1)\) is unnecessary except for harmless integer
rounding.  This implication is **valid**.

For each fixed integer \(A\), choose the threshold beyond which the preceding
ratio is small.  A standard slow diagonal choice gives \(A=A(m)\to\infty\)
while retaining the fixed-window estimate and, if necessary, imposing
\(A(m)=o(\sqrt m)\) so that \(K<m\).  Properness ensures every repair block
has free dimension strictly below \(n\), avoiding circular use of \(\nu(n)\).
Appending the proper signed-face blocks preserves their internal witnesses.
Together with the already audited exact-wreath seams and outer tails, this
does give a literal coefficient-one construction.

The positive scope statements at the end of the report are correct:

- this proves binary-hole repair, not MWB or balanced multiplicities;
- it gives no common-owner synchronization;
- none of these statements proves anything about arbitrary contiguous-OR
  architectures outside proper signed-face repair.

The converse obstruction sentence needs one further qualification.  Failure
of \(\Psi_{\le K}=o(W)\) directly obstructs the Poisson certificate.  Under
the accompanying bound \(M=O(W)\), equivalence (7) shows that it also
obstructs deterministic additive signed-face repair.  Without \(M=O(W)\),
the one-sided inequality \(D_{\rm det}\le\Psi\) does not permit that converse.

However, \(\mathrm{FG}_A\) includes the additional restriction \(M=O(W)\).
The exact rank-subset bounds do not rule out successful signed-face repair
with a larger aggregate hole family.  Thus \(\mathrm{FG}_A\) is a clean
sufficient target, not a necessary characterization of the entire signed-
face lane or of coefficient one.

## 10. Claim classification

| Claim | Verdict | Required qualification |
|---|---|---|
| Canonical proper-face cost | **Valid** | Exact for the stated two-copy block; not proved minimum. Declare \(\nu(0)=0\). |
| Fenchel dual | **Valid** | Use \(M>0\); \(0\log0=0\). |
| Entropy/\(\delta\) formula (1) | **Valid** | \(M=0\) handled separately. |
| Derivative and endpoint \(t=1/\delta\) | **Valid** | Entropy lower bound supplies monotonicity. |
| Fractional identity (2) | **Valid** | Only for \(M>0\); all costs are zero when \(M=0\). |
| Inequalities and rounding (3) | **Valid** | Restricted additive architecture; \(M>0\). |
| Full-cube cost \(2\nu(n)\) as minimum | **Unsupported** | Faces coincide; one copy costs \(\nu(n)\). |
| Full-cube exclusion at \(o(W)\) scale | **Valid after correction** | Only asymptotic criterion equivalence, not finite equality. |
| Uniform residual lower bounds (4) | **Valid** | \(\mathcal G\ne\varnothing\). |
| Peeling bounds (5)--(6) | **Valid** | Endpoint \(R=1/2\) supplied by literal columns. |
| Stall dual certificate | **Valid** | No stall exists at \(R=1/2\). |
| Equivalence (7)--(8) | **Valid** | Sequential quantifiers, inf-empty convention, eventual \(M\le CW\). |
| Fixed-rank bound (9) | **Valid** | Displayed derivation for \(s\ge1\); handle \(s=0\) separately. |
| Dimension bounds (10)--(11) | **Valid** | Same \(s=0\) endpoint qualification. |
| Rank-subset bound (12) | **Valid after correction** | Require nonempty \(Q\); \(M_Q=0\) is trivial. |
| Section 5 per-rank count as written | **Unsupported** | Must reset the abstract hole family by (A6). |
| Corrected abstract example | **Valid** | Uses inherited \(\nu(s)=O(\text{width})\); not factor-realized. |
| “Order-sharp” example | **Valid only for Poisson** | False/unsupported if read as deterministic order-sharpness. |
| \(\mathrm{FG}_A\Rightarrow\Psi=o(W)\) | **Valid** | Purely conditional on unproved \(\mathrm{FG}_A\). |
| Slow diagonalization to coefficient one | **Valid** | Proper-face, literal-repair route only. |
| \(\mathrm{FG}_A\) as the sole remaining global theorem | **Unsupported without scope restriction** | It is one sufficient \(M=O(W)\) target, not necessary for all repairs or words. |
| Failure of \(\Psi=o(W)\) obstructs deterministic signed-face repair | **Valid only with scope** | Valid when \(M=O(W)\) by (7); otherwise it directly obstructs only the Poisson functional. |

## Final audited status

The report establishes a correct exact dual description of its restricted
Poisson functional and a correct deterministic peeling/rounding theorem.  It
also gives a valid conditional coefficient-one route and a valid abstract
example showing that \(\Theta(W)\) aggregate holes can be compressed.

What remains unproved is not an analytic duality or cost identity.  It is the
existence of one exact wreath factor whose actual hole family satisfies a
sufficient dense-residual geometry condition.  The corrected audit must keep
that conclusion scoped to proper signed-face repair and must not identify
\(\mathrm{FG}_A\) with MWB, labelled synchronization, or a necessary
condition for arbitrary contiguous-OR constructions.
