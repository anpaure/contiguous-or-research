# Independent audit of the component-noise overlap identity

Date: 2026-07-24

Audited source: `COMPONENT_NOISE_OVERLAP_IDENTITY_20260724.md`, including the
new facet-star Theorems 6.1 and 6.2.

The live theorem statements were cross-checked against the frozen copies
labelled Theorems 6.1 and 6.2 in
GLOBAL_COMPONENT_NOISE_GATE_NO_GO_20260724.md.

This is a proof audit only.  No finite search, numerical experiment, or web
source was used.

## Verdict

The mathematical core passes.  In particular:

* (R_C=\tau L_C) is correct component by component;
* every component difference has zero total and zero point margins;
* (2.1)--(2.2) and the whole switching-cube identities (3.1)--(3.5),
  including every sign and the factor (1/4), are correct;
* the Johnson spectral formula (4.1) and the three-slack identity (4.2) are
  exact under the full-variance normalization specified below;
* the equality-rigidity and integral target-support arguments are correct
  with the minimizer and fixed-transposition quantifiers made explicit;
* the equitable-two-colouring equations are correct;
* the new first-shadow impossibility theorem is correct for every
  (m\ge18);
* the general sparse Boolean-\(E_2\) exclusion in Theorem 6.2 is correct;
  its deficit, up-operator, and \(4s\)-boundary factors all pass; and
* (6.1)--(6.6), including all factors of two and the separate (r=1)
  case, are correct.

There are, however, several localized corrections or qualifications which
should be made before the note is treated as self-contained.

1. **Define the normalization of \(\Phi\).**  The displayed identity
   (S_H=B_H+\Phi_H) makes (4.2) correct only when \(\Phi_H\) is the full
   integer variance above its floor.  If \(\Phi_q\) denotes the usual
   pair-collision excess, as it does in some companion notes, the variance
   excess is (2\Phi_q) and the last term of (4.2) is
   (8(n-1)\sum_q\Phi_q/c_q), not (4(n-1)\Phi_H).
2. **Keep the global-minimizer hypothesis.**  The first term
   (R_H-D_H) is nonnegative only at a global (H)-window minimizer, or
   under the explicitly weaker hypothesis that every transposition cube is
   locally nondecreasing at (F).  Thus the rigidity paragraph and the
   final assertion that the upper gate is sufficient must retain that
   hypothesis.  The upper gate is not sufficient for an arbitrary factor.
3. **Correct the connected-overlay quantifier.**  A connected overlay for
   one fixed \(\tau\) gives only
   (N_{\tau,H}-A_{\tau,H}=0).  It does not make the global first slack
   (R_H-D_H) vanish unless this happens for every transposition.
4. **State (4.6) per transposition.**  Its correct quantified form is
   \[
   \forall\tau,q,S:\qquad
   \#\{C\in\mathcal C_\tau(F):d_{\tau,q,C}(S)\ne0\}\le1.
   \]
   It gives disjoint target supports inside each fixed-
   \(\tau\) switching cube, not across components belonging to different
   transpositions.
5. **Do not identify every one-component target orbit with a locked NAE
   clause.**  The proved statement is disjointness of the component
   differences on nonfixed target orbits.  The sentence saying that these
   are “exactly the width-one, locked NAE clauses” is neither defined nor
   proved in this note and is too broad without excluding fixed, inactive,
   already robust, or bi-covered orbits.  It should be removed or replaced
   by a separately defined restricted statement about unresolved one-sided
   first-shadow orbits.
6. **Distinguish floor balance from spectral equality.**  The equitable
   colouring condition follows from floor balance together with equality in
   the Johnson gap.  Floor balance alone does not imply it.  At the first
   shadow the formulas \(\theta=2/m\), (8), and (4m-8) require
   (m\ge3).  For (m=2), (W/N_1=2), \(\theta=0\), and the centered
   load is zero.
7. **Clarify the exact-equality wording.**  “Equality in (4.4) with zero
   error” should be replaced by the precise equation
   \(R_H=4(n-1)B_H\) at a global minimizer.  Equation (4.4) itself is an
   asymptotic inequality with an (o(nW)) term.
8. **Minor wording and notation.**  In (2.2), negative aggregate
   correlation gives strict loss and zero correlation gives a tie; hence
   “nonpositive” means “fails to improve,” not “strictly loses.”  The line
   introducing (f) in Section 5 is missing \({\bf1}\) and closing math
   markup.  Before (6.3), define the unweighted rank pieces (R_q,D_q)
   explicitly.

The new Theorem 6.1 needs no substantive repair.  Two proof clarifications
would improve it: specify that (U^*) is taken for unnormalized counting
inner products, and state explicitly why the final density \(\delta\) is
positive.  Also, for a nonfull facet of a bonus set the exact deficit range
is \([m-5,m+2]\); the written looser upper bound (m+3) is still true and
is sufficient for the claimed (m\ge18) threshold.

Theorem 6.2 also needs no substantive repair.  For a nonfull facet of a
member of \(\mathcal B\), the exact deficit interval is
\([s-b,s-1]\), while the written \([s-b,s]\) is a harmless loose interval.
The advertised open limiting range \(0<\theta<1/16\) is correct.  It should
be stated for sequences \(m-r_m=O(\sqrt m)\) and
\(\theta_m\to\theta_0\).  The exact third inequality is
\[
\theta<\frac1{16}+\frac{5(m-r)+10}{16m},
\]
Thus the open-range corollary makes no uniform assertion at
\(\theta_0=1/16\).  The special sequence \(\theta_m\equiv1/16\) is also
covered whenever the required integrality holds, while sequences tending
to \(1/16\) from above may or may not meet the finite-\(m\) inequality.

## 1. Component equivariance and point margins

Fix \(\tau=(a\ b)\).  A row (P) has (n) cyclic middle intervals.  Each
of (a,b) occurs in exactly (m) of them, so their total incidence is

\[
2m=n-1.
\]

If no middle interval were fixed by \(\tau\), every interval would contain
exactly one of (a,b), and the incidence total would instead be (n).
Thus some interval contains both or neither.  That fixed middle set is an
ownership edge from the left vertex (P) to the right vertex \(\tau P\),
so (P) and \(\tau P\) lie in the same overlap component.

The ownership overlay is (n)-regular on both sides.  Every connected
bipartite component therefore has equally many left and right vertices:
counting its edges from both sides gives
(n|L_C|=n|R_C|).  The injection

\[
\tau L_C\subseteq R_C
\]

and equality of the cardinalities prove

\[
R_C=\tau L_C.
\]

Consequently (w_{q,C}=\tau u_{q,C}), proving (1.1)--(1.2).

Put (k_C=|L_C|) and (r=r_q).  Every row contributes (n) cyclic
(r)-intervals, and a fixed point occurs in exactly (r) of them.  Hence
both side histograms have total mass (nk_C) and point margins (rk_C).
Their difference (d_{q,C}) has zero total and zero point margins.

On the rank-(r) Johnson layer, (E_0\oplus E_1) is the span of the
constant function and the point-incidence functions.  The preceding margin
identities therefore give

\[
d_{q,C}\perp E_0\oplus E_1,
\qquad
d_{q,C}\in\bigoplus_{j\ge2}E_j.
\]

The same check for the full centered load is exact.  If
(b=|F|=W/n), then the point margin of \(\mu_q\) is (rb=Wr/n), while

\[
\frac W{N_q}\binom{n-1}{r-1}=\frac{Wr}{n}
\]

is the point margin of its constant mean.  Thus (f_q) also has no
degree-zero or degree-one part.  When (r=1), this forces
(d_{q,C}=f_q=0), since there are no Johnson harmonics of degree at least
two on the singleton layer.

The contracted row-graph description also passes: after identifying the
right row \(\tau P\) with (P), a nonfixed middle orbit
\(\{A,\tau A\}\) joins the two owners and a fixed middle set gives only a
loop.  Contraction preserves exactly the sets (L_C).

## 2. Orbit, correlation, and switching-cube identities

On a nonfixed orbit (p=\{S,\tau S\}), orient the two coordinates so that

\[
z_{C,q,p}=u_{q,C}(S)-u_{q,C}(\tau S).
\]

Since (d_C=\tau u_C-u_C), its two entries on this orbit are
((-z_{C,q,p},z_{C,q,p})).  Therefore

\[
\|d_{q,C}\|_2^2=2\sum_p z_{C,q,p}^2,
\qquad
\left\|\sum_Cd_{q,C}\right\|_2^2
=2\sum_p\left(\sum_Cz_{C,q,p}\right)^2.
\]

Fixed orbits give zero.  Expanding the square, summing over ranks with
weights (1/c_q), and using

\[
\|\textstyle\sum_Cd_C\|_H^2
=\sum_C\|d_C\|_H^2+2\sum_{C<D}\langle d_C,d_D\rangle_H
\]

proves (2.1)--(2.2), including the sign and factor:

\[
N_{\tau,H}-A_{\tau,H}
=-4\sum_{q\le H}\frac1{c_q}
  \sum_p\sum_{C<D}z_{C,q,p}z_{D,q,p}.
\]

In particular, if the weighted aggregate correlation on the right is
negative, fair switching has positive mean energy drift; if it is zero, the
mean drift is zero; and if it is positive, fair switching has negative mean
drift.

Let (D=\sum_Cd_C=\tau f-f).  Since \(\tau d_C=-d_C\), switching a set
(I) of components gives

\[
\tau f_I
=\tau f-\sum_{C\in I}d_C
=f+\sum_{C\notin I}d_C
=f_{I^c}.
\]

This proves (3.1), since \(\tau\) is an isometry.  For independent
(X_C\in\{0,1\}) with mean (1/2), isometry also gives

\[
\langle f,D\rangle_H=-\frac12\|D\|_H^2=-\frac12A_{\tau,H},
\]

and direct expansion gives

\[
\mathbb E\left\|\sum_CX_Cd_C\right\|_H^2
=\frac14\bigl(N_{\tau,H}+A_{\tau,H}\bigr).
\]

Hence

\[
\mathbb E_Ie_\tau(I)
=-\frac12A_{\tau,H}
 +\frac14(N_{\tau,H}+A_{\tau,H})
=\frac14(N_{\tau,H}-A_{\tau,H}),
\]

which verifies (3.2).

At a global minimizer every cube vertex is another exact factor and has
(e_\tau(I)\ge0).  Thus (3.3) follows.  If equality holds, the nonnegative
function (e_\tau) has mean zero and vanishes at every cube vertex.
Expanding singleton and two-component vertices yields respectively

\[
2\langle f,d_C\rangle_H+\|d_C\|_H^2=0,
\qquad
\langle d_C,d_D\rangle_H=0\quad(C\ne D).
\]

Conversely these identities make every subset expansion vanish.  This
proves (3.3)--(3.5) and the stated cube rigidity.

The two elementary zero-mixing cases are also sound, apart from the NAE
terminology flagged above.  A connected overlay has one component, hence
only the two isometric vertices (F,\tau F).  If distinct (d_C)'s have
disjoint supports, they are pairwise orthogonal.  In fact this already
makes the full cube constant even without a minimizer hypothesis: writing

\[
h=\frac{f+\tau f}{2},\qquad f=h-\frac12D,
\]

one has \(\tau h=h\), \(\tau d_C=-d_C\), and hence

\[
2\langle f,d_C\rangle_H
=-\langle D,d_C\rangle_H=-\|d_C\|_H^2.
\]

Together with pairwise orthogonality this is exactly (3.4)--(3.5).

## 3. Johnson spectrum and the three slacks

For clarity, write

\[
\lambda_q=\frac W{N_q}=c_q+\alpha_q,
\qquad 0\le\alpha_q<1,
\]

and

\[
V_q^{\min}=N_q\alpha_q(1-\alpha_q).
\]

This is the minimum of
\(\|\mu_q-\lambda_q{\bf1}\|_2^2\) among integer vectors of total (W).
The self-contained normalization needed in the note is

\[
\Phi_q^{\rm var}
:=\|f_q\|_2^2-V_q^{\min}\ge0,
\qquad
\Phi_H^{\rm var}:=\sum_{q\le H}\frac{\Phi_q^{\rm var}}{c_q}.
\]

Then (S_H=B_H+\Phi_H^{\rm var}).  If
\(\Phi_q^{\rm pair}\) instead denotes pair-collision excess, the exact
integer identity is

\[
\Phi_q^{\rm var}=2\Phi_q^{\rm pair}.
\]

This is the sole normalization issue in (4.2).

For an unordered transposition sum on the rank-(r) layer, each Johnson
edge is counted twice in the squared norm.  Since the Johnson Laplacian has
eigenvalue (j(n-j+1)) on (E_j),

\[
\sum_\tau\|\tau f_q-f_q\|_2^2
=2\sum_{j\ge2}j(n-j+1)\|f_q^{(j)}\|_2^2.
\]

At (j=2) the coefficient is (4(n-1)).  Subtracting it gives

\[
2\{j(n-j+1)-2(n-1)\}
=2(j-2)(n-j-1),
\]

which is nonnegative for every occurring (j\ge3).  This proves both
lines of (4.1), with all constants correct.

For every factor, the following is an algebraic identity:

\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)S_H\bigr)\\
&+4(n-1)\Phi_H^{\rm var}.
\end{aligned}
\]

At a global minimizer all three terms on the right are nonnegative:

* (R_H-D_H=\sum_\tau(N_{\tau,H}-A_{\tau,H})\ge0) by cube
  minimality;
* the middle term is nonnegative by the preceding spectrum; and
* the last term is nonnegative by the integer variance floor.

Moreover (3.2) gives exactly

\[
R_H-D_H=4\sum_\tau\mathbb E_Ie_\tau(I),
\]

so (4.2)--(4.3) pass.  Without minimizer or cube-local minimality, the
first term can have either sign; this is why the final sufficient-gate
statement needs the missing hypothesis.

If

\[
R_H\le4(n-1)B_H+o(nW)
\]

holds at such a minimizer, every one of the three nonnegative slacks is
(o(nW)), and

\[
4(n-1)\Phi_H^{\rm var}=o(nW)
\quad\Longrightarrow\quad
\Phi_H^{\rm var}=o(W).
\]

Thus the analytic implication stated after (4.4) is valid under the
minimizer hypothesis.  A connected overlay for a single \(\tau\) merely
sets that \(\tau\)-summand of the first slack to zero.  Independently of
connectivity, the third term already is the desired floor-excess quantity;
the identity alone gives no upper bound on it.

## 4. Exact equality and targetwise support

Assume now that (F) is a global (H)-window minimizer and that the exact
baseline equation

\[
R_H=4(n-1)B_H
\]

holds.  Every nonnegative slack in the preceding identity is zero.  Since
the rankwise floor excesses are themselves nonnegative, every controlled
rank is floor-balanced.  The middle spectral slack vanishes only in
Johnson degree two (apart from the zero function), and every
\(N_{\tau,H}-A_{\tau,H}\) vanishes.  Cube rigidity then makes every child
in every fixed-\(\tau\) cube have the same total energy (B_H), hence zero
floor excess at every rank.

Fix \(\tau,q,S\).  For every component subset (I), therefore,

\[
\mu_q(S)+\sum_{C\in I}d_{\tau,q,C}(S)\in\{c_q,c_q+1\}.
\]

If the initial value is (c_q), singleton subsets force each increment to
belong to \(\{0,1\}\), and a two-element subset forbids two increments
equal to (1).  If the initial value is (c_q+1), singleton subsets force
each increment to belong to \(\{-1,0\}\), and a pair forbids two
increments equal to (-1).  Thus the exact conclusion is

\[
\#\{C\in\mathcal C_\tau(F):d_{\tau,q,C}(S)\ne0\}\le1.
\]

The proof is exact.  Only the omitted \(\tau\)-quantifier in the source
needs correction.

## 5. Equitable two-colouring arithmetic

Let a balanced rank-(r) load be

\[
\mu=c{\bf1}+{\bf1}_{\mathcal B},
\qquad
f={\bf1}_{\mathcal B}-\theta{\bf1},
\qquad
\theta=|\mathcal B|/N.
\]

Suppose (f\in E_2), so
(L_Jf=2(n-1)f).  Put \(\lambda_2=2(n-1)\).  If
(S\notin\mathcal B) and (x) of its Johnson neighbours lie in
\(\mathcal B\), then

\[
(L_Jf)(S)=-x=-\lambda_2\theta,
\]

so (x=\lambda_2\theta).  If (S\in\mathcal B) and (y) of its
neighbours lie outside \(\mathcal B\), then

\[
(L_Jf)(S)=y=\lambda_2(1-\theta).
\]

This proves (5.2).  In particular \(\lambda_2\theta\) is an integer; the
second count is then automatically integral because \(\lambda_2\) is an
integer.

At the first shadow,

\[
r=m-1,
\qquad
\frac W{N_1}=\frac{m+2}{m}=1+\frac2m.
\]

For (m\ge3), this gives \(\theta=2/m\) and

\[
2(n-1)\theta=8,
\qquad
2(n-1)(1-\theta)=4m-8.
\]

These are necessary conditions for simultaneous floor balance and spectral
equality.  They do not follow from floor balance alone and are not by
themselves sufficient for realization by a wreath factor.

## 6. Audit of the new first-shadow impossibility theorem

Theorem 6.1 is correct.  In fact its contradiction concerns an arbitrary
bonus family on the Johnson layer; it does not use wreath realizability.

Assume (m\ge18), put (r=m-1), (k=m-2), and suppose that
\(\mathcal B\subseteq\binom{[n]}r\) has density (2/m) and centered
indicator in (E_2).  By the preceding equitable-colouring calculation,
every nonbonus (r)-set has (8) bonus neighbours and every bonus
(r)-set has (4m-8) nonbonus neighbours.

For (T\in\binom{[n]}k), define

\[
\kappa(T)=\#\{S\in\mathcal B:T\subset S\}.
\]

There are (n-k=m+3) extensions of (T).  If not all are bonus, choose a
nonbonus extension (S\).  Each bonus extension of (T) differs from (S)
by one Johnson exchange and all are distinct, so \(\kappa(T)\le8\).  Hence

\[
\kappa(T)\le8\quad\text{or}\quad\kappa(T)=m+3.
\]

Call (T) full in the second case.  Fix (S\in\mathcal B).  A bonus
Johnson neighbour (S') shares a unique (k)-facet (T=S\cap S') with
(S); therefore

\[
\sum_{\substack{T\subset S\\|T|=k}}(\kappa(T)-1)
=r(n-r)-(4m-8)
=(m-1)(m+2)-(4m-8)
=m^2-3m+6.
\]

Adding the (r=m-1) facets gives

\[
\sum_{T\subset S,\ |T|=k}\kappa(T)=m^2-2m+5.
\]

If all facets were full, the sum would be

\[
(m-1)(m+3)=m^2+2m-3,
\]

so the total deficit is exactly (4m-8).  For a nonfull facet of this
bonus (S), one also has \(\kappa(T)\ge1\); thus its exact deficit lies in

\[
m-5\le(m+3)-\kappa(T)\le m+2.
\]

The source's upper bound (m+3) is merely loose.  For (m\ge18), even
that loose bound gives

\[
3(m+3)<4m-8<5(m-5).
\]

Consequently exactly four facets of (S) are nonfull, exactly (m-5) are
full, and the four nonfull \(\kappa\)-values sum to (20).  The
four-nonfull-facet deduction is therefore valid.

Let \(\mathcal T\) be the family of full (k)-sets.  A nonbonus (r)-set
contains no full facet, while every bonus (r)-set contains exactly
(m-5) of them.  For the up-incidence operator

\[
(Ug)(S)=\sum_{\substack{T\subset S\\|T|=k}}g(T)
\]

this proves the Boolean identity

\[
U{\bf1}_{\mathcal T}=(m-5){\bf1}_{\mathcal B}.
\]

With unnormalized counting inner products, direct multiplication gives

\[
U^*U=(n-k)I+A_{J(n,k)}.
\]

Indeed, (T) itself is counted once for each of its (n-k) extensions,
and each Johnson neighbour (T') is counted in the unique set
(T\cup T').  The Johnson adjacency eigenvalue on (E_j) is

\[
(k-j)(n-k-j)-j.
\]

After adding (n-k), the (U^*U) eigenvalue is

\[
(k+1-j)(n-k-j).
\]

For (0\le j\le k), both factors are positive; at the largest possible
(j=k), the second factor is (n-2k=5).  Thus (U) is injective.  The
operator is (S_n)-equivariant, hence maps each multiplicity-free Johnson
harmonic (E_j) into the same (E_j) at rank (k+1).  Since the right
side of the Boolean identity lies in (E_0\oplus E_2), injectivity gives

\[
{\bf1}_{\mathcal T}\in E_0\oplus E_2.
\]

It remains to check the boundary count.  Fix full (T) and (z\notin T).
Then (S=T\cup\{z\}\) is bonus.  The facet (T) is full, so the four
nonfull facets of (S) are precisely four sets of the form

\[
T-\{x\}+\{z\}.
\]

These are exactly four Johnson neighbours of (T) outside
\(\mathcal T\) associated with this (z).  A Johnson neighbour determines
its added point (z) uniquely, so the (n-k=m+3) groups do not overlap.
Thus every full (T) has exactly

\[
4(m+3)
\]

neighbours outside \(\mathcal T\).  Moreover \(\mathcal T\ne\varnothing\):
the bonus family has positive density (2/m), and every bonus set has
(m-5>0) full facets.  Hence, with

\[
\delta=\frac{|\mathcal T|}{\binom nk}>0,
\]

the degree-two equitable-colouring equation applied at a member of
\(\mathcal T\) instead requires outside degree

\[
2(n-1)(1-\delta)=4m(1-\delta)<4m.
\]

This contradicts (4(m+3)>4m), and proves Theorem 6.1.

The theorem rules out exact first-shadow spectral equality for
(m\ge18).  Its consequence for the global baseline is valid when the
first shadow is in the controlled window and the exact baseline equation is
assumed at a global minimizer, because only then do the three nonnegative
slacks force floor balance and pure degree two.  The theorem supplies no
quantitative stability estimate for the allowed (o(nW)) error, and the
source correctly does not claim one.

## 7. Audit of the general facet cascade, Theorem 6.2

Theorem 6.2 passes.  Let \(2\le r\le m\), put
\[
k=r-1,\qquad s=n-r+1=n-k,
\]
and let the nonempty proper family
\(\mathcal B\subseteq\binom{[n]}r\) have density \(\theta\) with
\[
{\bf1}_{\mathcal B}-\theta{\bf1}\in E_2.
\]
The degree-two Johnson Laplacian eigenvalue is \(2(n-1)=4m\).
Equitability therefore gives the two cross-degrees
\[
b=4m\theta,\qquad d=4m(1-\theta).
\]
Because both colour classes are nonempty, these are actual neighbour
counts and hence integers.

For \(T\in\binom{[n]}k\), let \(\kappa(T)\) count its extensions in
\(\mathcal B\).  Its extension star has size \(n-k=s\).  If it is not
full, choose an extension \(S_0\notin\mathcal B\).  Every one of the
\(\kappa(T)\) bonus extensions differs from \(S_0\) by one Johnson
exchange, so all are distinct bonus neighbours of \(S_0\).  Consequently
\[
\kappa(T)\le b
\]
for every nonfull \(T\).

Now fix \(S\in\mathcal B\).  Every bonus neighbour \(S'\) of \(S\) shares
the unique facet \(T=S\cap S'\), whence
\[
\sum_{\substack{T\subset S\\|T|=r-1}}(\kappa(T)-1)
=r(n-r)-d.
\]
Since \(S\) has \(r\) facets and \(s=n-r+1\),
\[
\begin{aligned}
\sum_{\substack{T\subset S\\|T|=r-1}}(s-\kappa(T))
&=rs-\bigl(r(n-r)-d+r\bigr)\\
&=d.
\end{aligned}
\]
Full facets contribute zero.  Thus the sum of the deficits over precisely
the nonfull facets is \(d\), as claimed.

For a nonfull facet of this particular bonus set, \(1\le\kappa(T)\le b\).
Its exact deficit interval is therefore
\[
s-b\le s-\kappa(T)\le s-1.
\]
The source uses the weaker upper bound \(s\), which remains valid.  Thus
the sufficient lower hypothesis \(3s<d\) could be weakened to
\(3(s-1)<d\), although this does not change the limiting \(1/16\)
threshold.  Under the stated hypotheses
\[
b<s,\qquad 3s<d<5(s-b),
\]
at most three nonfull facets have total deficit at most \(3s<d\), whereas
at least five have total deficit at least \(5(s-b)>d\).  The number of
nonfull facets is therefore exactly four.  This verifies the general
deficit cascade without any omitted case.

Let \(\mathcal T\subseteq\binom{[n]}{r-1}\) be the full facets.  No set
outside \(\mathcal B\) contains a full facet, and each set in
\(\mathcal B\) has exactly \(r-4\) full facets.  Hence
\[
U{\bf1}_{\mathcal T}=(r-4){\bf1}_{\mathcal B}.
\]
The hypothesis \(r>4\) is essential here: it makes the scalar \(r-4\)
nonzero and also ensures that every bonus set supplies a full facet.

The needed injectivity is valid in the entire stated rank range.  With
counting inner products and \(k=r-1\),
\[
U^*U=(n-k)I+A_{J(n,k)}
\]
has eigenvalue
\[
(k+1-j)(n-k-j)
\]
on \(E_j\).  Since \(k\le m-1\), the second factor at its minimum
\(j=k\) is
\[
n-2k=n-2r+2\ge3.
\]
Thus \(U\) is injective and intertwines each Johnson harmonic with the
same harmonic at rank \(r\).  The Boolean identity and \(r-4\ne0\) imply
\[
{\bf1}_{\mathcal T}\in E_0\oplus E_2.
\]

The \(4s\) boundary count is also exact.  Fix \(T\in\mathcal T\).  Each of
its \(s\) extensions has the form \(S=T\cup\{z\}\) and belongs to
\(\mathcal B\).  The facet \(T\) is full, while exactly four other facets
of \(S\) are nonfull.  They have the form
\[
T-\{x\}+\{z\}
\]
and are exactly four neighbours of \(T\) outside \(\mathcal T\) associated
with \(z\).  Every Johnson neighbour of \(T\) determines its added point
\(z\) uniquely, so different extension stars do not double-count a
boundary neighbour.  Therefore
\[
\deg_{\mathcal T^c}(T)=4s.
\]

The family \(\mathcal T\) is nonempty because \(\mathcal B\ne\varnothing\)
and every member of \(\mathcal B\) has \(r-4>0\) full facets.  If
\[
\delta=\frac{|\mathcal T|}{\binom n{r-1}}>0,
\]
the \(E_2\) equitable-colouring equation instead gives, for every
\(T\in\mathcal T\),
\[
\deg_{\mathcal T^c}(T)=4m(1-\delta)<4m.
\]
But \(r\le m\) gives
\[
s=n-r+1\ge m+2,
\qquad 4s>4m,
\]
a contradiction.  This proves Theorem 6.2.

The asymptotic density calculation also passes.  More precisely, let
\[
q_m=m-r_m\ge0,\qquad q_m=O(\sqrt m),
\qquad s_m=m+q_m+2,
\]
and put \(b_m=4m\theta_m\), \(d_m=4m(1-\theta_m)\).
The three exact inequalities become
\[
\begin{aligned}
b_m<s_m
&\iff
\theta_m<\frac14+\frac{q_m+2}{4m},\\
3s_m<d_m
&\iff
\theta_m<\frac14-\frac{3q_m+6}{4m},\\
d_m<5(s_m-b_m)
&\iff
\theta_m<\frac1{16}+\frac{5q_m+10}{16m}.
\end{aligned}
\]
If \(\theta_m\to\theta_0\in(0,1/16)\), all three hold for large \(m\).
This proves the open limiting range stated in the source.  There is no
uniform endpoint conclusion for arbitrary sequences with
\(\theta_m\to1/16\).  The particular sequence
\(\theta_m\equiv1/16\) does satisfy the strict inequalities eventually
whenever cross-degree integrality permits it; a sequence approaching the
endpoint from above may fail them.

Finally,
\[
{\bf1}_{\mathcal B^c}-(1-\theta){\bf1}
=-\bigl({\bf1}_{\mathcal B}-\theta{\bf1}\bigr)\in E_2.
\]
Applying the same theorem to the complementary family gives the symmetric
fixed-density exclusion \(15/16<\theta<1\), with the exact finite
conditions obtained by interchanging \(b\) and \(d\).  This complement
claim is correct.

The accompanying phrase “positive portions of a generic Gaussian window”
is informal rather than a quantified consequence as written.  A rigorous
version should choose a compact interval of \(x=q/\sqrt m\), away from the
integer crossings of \(e^{x^2}\), on which
\[
\{e^{x^2}\}\in(0,1/16)\cup(15/16,1),
\]
and then use the uniform ratio asymptotic to obtain \(\Theta(\sqrt m)\)
excluded depths.  Without such a quantifier, that phrase should be treated
as motivation, not as an additional theorem.

Like Theorem 6.1, Theorem 6.2 is an exact Boolean-\(E_2\) obstruction.  It
does not supply the quantitative \(L^2\)-stability estimate needed to rule
out an \(o(nW)\) spectral slack; the source does not overclaim this point.

## 8. Row-level identities

Let \(\mathcal A_{P,r}\) be the (n) cyclic (r)-intervals in (P).  The
squared norm of
(g_{P,\tau,r}={\bf1}_{\tau\mathcal A_{P,r}}-
{\bf1}_{\mathcal A_{P,r}}) is the size of the symmetric difference.

For (2\le r\le m), if the swapped points have shorter cyclic distance
\(\ell\), exactly (2\min(r,\ell)) cyclic (r)-windows contain one but
not both points.  Normally each such window and its image contribute two
elements to the symmetric difference.  Exactly when \(\ell=r\), one pair
of these windows is exchanged within \(\mathcal A_{P,r}\), removing four
contributions.  Hence

\[
\|g_{P,\tau,r}\|_2^2
=4\min(r,\ell)-4{\bf1}_{\{\ell=r\}},
\]

which proves (6.1).

For each \(\ell\in\{1,\ldots,m\}\), an odd (n)-cycle has exactly (n)
unordered pairs at distance \(\ell\), and

\[
\sum_{\ell=1}^m\min(r,\ell)
=\frac{r(n-r)}2.
\]

Therefore

\[
\sum_\tau\|g_{P,\tau,r}\|_2^2
=4n\frac{r(n-r)}2-4n
=2n\bigl(r(n-r)-2\bigr),
\]

verifying (6.2).  When (r=1), every row's cyclic interval family is the
complete singleton layer, so \(\tau h_{P,1}=h_{P,1}\) and
(g_{P,\tau,1}=0) term by term.  Formula (6.2), and hence the diagonal
formula derived from it, must not be used at (r=1).

Define explicitly

\[
R_q:=\sum_\tau\sum_{C\in\mathcal C_\tau(F)}
       \|d_{\tau,q,C}\|_2^2,
\qquad
D_q:=\sum_\tau\|\tau\mu_q-\mu_q\|_2^2.
\]

Then (R_H=\sum_qR_q/c_q), (D_H=\sum_qD_q/c_q), and

\[
d_{\tau,q,C}=\sum_{P\in L_C}g_{P,\tau,r_q}.
\]

Expanding this square gives diagonal row terms plus twice the unordered
row-pair inner products.  Since \(|F|=W/n\), summing the diagonal terms in
(6.2) over all rows gives

\[
\frac Wn\,2n\bigl(r_q(n-r_q)-2\bigr)
=2W\bigl(r_q(n-r_q)-2\bigr).
\]

This proves (6.3), including its cross-term factor (2).  Expanding
(D_q) instead includes every row pair.  Subtracting it from (R_q)
leaves precisely the pairs in distinct components with a minus sign and
factor (2), proving (6.4).  At (r=1), both (R_q) and (D_q) are zero.

At the first shadow (r=m-1),

\[
r(n-r)-2=(m-1)(m+2)-2=m^2+m-4,
\]

which proves (6.5).  For (m\ge3),

\[
N_1=\frac{mW}{m+2},
\qquad
\alpha_1=\frac2m,
\]

so

\[
V_1^{\min}
=N_1\alpha_1(1-\alpha_1)
=\frac{2W(m-2)}{m(m+2)}.
\]

Since (4(n-1)=8m),

\[
4(n-1)V_1^{\min}
=16W\frac{m-2}{m+2},
\]

verifying (6.6).  The ratio of this floor scale to the row-diagonal term is
\(\Theta(m^{-2})\), so the stated cancellation requirement is accurate.

## 9. Correct final formulation

A precise version of the note's final sufficient statement is the
following.

**Proposition.**  Fix a controlled window (H), and let (F) be a global
minimizer of (S_H) over exact middle wreath factors.  If

\[
R_H(F)\le4(n-1)B_H+\varepsilon_m,
\qquad 0\le\varepsilon_m=o(nW),
\]

then

\[
\Phi_H^{\rm var}(F)\le\frac{\varepsilon_m}{4(n-1)}=o(W).
\]

**Proof.**  At (F), all three terms in (4.2) are nonnegative, so the last
one is at most the left side and hence at most \(\varepsilon_m\).  Divide
by (4(n-1)).  \(\square\)

For the fixed-window overload route, this proposition must be available for
each fixed (H_A=\lceil A\sqrt m\rceil), followed by the established
diagonalization.  The new Theorem 6.1 shows that exact attainment of the
baseline is impossible for (m\ge18) once (q=1) is included, but it does
not contradict an (o(nW))-accurate upper gate.  Theorem 6.2 supplies
further exact Boolean-\(E_2\) exclusions at sparse and complementary dense
bonus densities, but likewise no quantitative near-equality estimate.  No
estimate in the note proves the upper gate; the remaining input is still a
quantitative factor-fibre cancellation or stability theorem.

Subject to the corrections and quantifiers listed in the verdict, the
audited identities are accepted.
