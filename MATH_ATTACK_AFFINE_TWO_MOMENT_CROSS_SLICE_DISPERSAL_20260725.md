# Two affine moments and the cross-slice physical pair-label term

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Fix one global coordinate labelling

\[
 h:[2m]\longrightarrow\mathbb F_p,
 \qquad p>3,\qquad p=m^{1/2+o(1)},
 \tag{0.1}
\]

and define the two power-sum labels

\[
 \chi _1(S)=\sum_{u\in S}h(u),
 \qquad
 \chi _2(S)=\sum_{u\in S}h(u)^2.                    \tag{0.2}
\]

There are two exact positive conclusions.

1. On an affine base schedule, every protected signed row has a linear
   \(\chi _1\)-trace and a quadratic \(\chi _2\)-trace.  After eliminating
   phase, its moment labels lie on one explicit parabola in
   \(\mathbb F_p^2\).  Two nonidentical row parabolas have at most two
   common labels.
2. A commuting adjacent switch changes only one physical column and
   changes its \(\chi _1\)-label by \(0\) or \(\pm\alpha\).  Hence, even
   on the full switch orbit of an affine base, a fixed row moment label
   has only constant phase multiplicity.  For two outer slices
   \(\omega,\omega'\), with \(f_\omega,f_{\omega'}\) physically effective
   switch directions, the number of coincidences of **ordered
   target-pair moment labels** is

   \[
    \boxed{
    {\cal C}_{\omega,\omega'}
    \le m^{o(1)}f_\omega f_{\omega'}.}               \tag{0.3}
   \]

If the main square weight in a slice is uniform over
\(\Theta(f_\omega^2)\) direction pairs, (0.3) gives

\[
 \boxed{
 { {\cal C}_{\omega,\omega'}\over
       \Theta(f_\omega^2f_{\omega'}^2)}
 \le {m^{o(1)}\over f_\omega f_{\omega'}}.}          \tag{0.4}
\]

Thus, when

\[
 f_\omega,f_{\omega'}=p\,m^{-o(1)}
 =m^{1/2-o(1)},                                     \tag{0.5}
\]

the normalized cross-slice collision factor is

\[
 p^{-2}m^{o(1)}=m^{-1+o(1)}.                        \tag{0.6}
\]

The estimate survives arbitrary nonnegative **scalar outer-slice
weights**.  Trace-equivalent priority slices cause the worst case
\(\Theta(f_\omega f_{\omega'})\), but no worse; they do not destroy
(0.6).

This does not yet prove the full survival-conditioned four-walk bound.
Three bridges remain.

1. Almost all size-biased feasible slices must have
   \(f_\omega=p\,m^{-o(1)}\).  The current down-set theorem does not prove
   this.
2. The replacement of a feasible down-set by uniform weight on its full
   switch cube must have negligible error in the inverse-degree
   pair-square norm, not merely in unweighted \(\ell _1\).
3. The affine object must be the **switch orbit of an affine base**.
   The subcatalogue in which every switch vertex is itself affine contains
   no nontrivial adjacent-switch edge.

Subject to these bridges, the polynomial moments do disperse the remaining
outer scalar-slice physical pair labels at exactly the required
\(m^{-1+o(1)}\) scale.  Without them, no unconditional estimate for
\(N_\omega(x,y)\) follows.

## 1. Exact base-row traces

Use a length-\(p\) affine base grid

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_p\}
    \cup\{b_1,\ldots,b_j\},                         \tag{1.1}
\]

with

\[
 h(a_r)=A+\alpha r,\qquad
 h(b_r)=B+\alpha r,
 \qquad
 \alpha\ne0,\qquad \delta=B-A.                     \tag{1.2}
\]

Indices are read in \(\mathbb F_p\).  Since both affine strings use every
field element exactly once,

\[
 \sum_{r=1}^p(A+\alpha r)
 =
 \sum_{r=1}^p(A+\alpha r)^2=0,                      \tag{1.3}
\]

and similarly for the \(b\)-string.  Put

\[
 c_1=\chi _1(C),\qquad c_2=\chi _2(C).              \tag{1.4}
\]

For signed depth \(d\in[-Q,Q]\), define

\[
 F_d(t)=G_{t-d,t},
 \qquad
 v_d=\delta+\alpha d.                               \tag{1.5}
\]

The affine admissibility condition is \(v_d\ne0\) for every protected
\(d\).  Directly summing the two affine strings gives

\[
 \boxed{
 \chi _1(F_d(t))
 =
 r_d+v_dt,}                                         \tag{1.6}
\]

where

\[
 r_d=c_1+dA-{\alpha d(d-1)\over2}.                  \tag{1.7}
\]

For the second moment,

\[
 \boxed{
 \chi _2(F_d(t))
 =
 s_d+
 v_d\left[
     \alpha t^2+
     \bigl(2A+\delta+\alpha(1-d)\bigr)t
     \right],}                                      \tag{1.8}
\]

where

\[
 s_d
 =
 c_2+dA^2-A\alpha d(d-1)
 +{\alpha^2d(d-1)(2d-1)\over6}.                    \tag{1.9}
\]

These formulas are polynomial identities over \(\mathbb F_p\), so they
remain valid for negative \(d\).

### 1.1 Lower rows

For \(L_q(t)=G_{t+q,t}=F_{-q}(t)\),

\[
 \boxed{
 \chi _1(L_q(t))
 =
 c_1-qA-{\alpha q(q+1)\over2}
 +(\delta-\alpha q)t,}                              \tag{1.10}
\]

and

\[
\boxed{
\begin{aligned}
 \chi _2(L_q(t))
 &=
 c_2-qA^2-A\alpha q(q+1)
 -{\alpha^2q(q+1)(2q+1)\over6}\\
 &\quad+
 (\delta-\alpha q)
 \left[
   \alpha t^2+
   \bigl(2A+\delta+\alpha(q+1)\bigr)t
 \right].
\end{aligned}}                                      \tag{1.11}
\]

### 1.2 Upper rows

For \(U_q(t)=G_{t-q,t}=F_q(t)\),

\[
 \boxed{
 \chi _1(U_q(t))
 =
 c_1+qA-{\alpha q(q-1)\over2}
 +(\delta+\alpha q)t,}                              \tag{1.12}
\]

and

\[
\boxed{
\begin{aligned}
 \chi _2(U_q(t))
 &=
 c_2+qA^2-A\alpha q(q-1)
 +{\alpha^2q(q-1)(2q-1)\over6}\\
 &\quad+
 (\delta+\alpha q)
 \left[
   \alpha t^2+
   \bigl(2A+\delta+\alpha(1-q)\bigr)t
 \right].
\end{aligned}}                                      \tag{1.13}
\]

At \(q=0\), both formulas give the owner trace

\[
 \chi _1(X_t)=c_1+\delta t,
 \qquad
 \chi _2(X_t)
 =c_2+\delta\bigl[\alpha t^2+(2A+\delta+\alpha)t\bigr].
 \tag{1.14}
\]

## 2. The exact parabola catalogue

Put

\[
 \lambda_d=2A+\delta+\alpha(1-d),
 \qquad
 \kappa_d={\alpha\over v_d}.                        \tag{2.1}
\]

Eliminating \(t=(\chi _1-r_d)/v_d\) from (1.6)--(1.8) gives

\[
 \boxed{
 \chi _2
 =
 \kappa_d(\chi _1-r_d)^2
 +\lambda_d(\chi _1-r_d)+s_d.}                     \tag{2.2}
\]

Equivalently, the row curve is determined by

\[
 \Theta_d=
 \left(
 \kappa_d,\,
 \lambda_d-2\kappa_dr_d,\,
 s_d+\kappa_dr_d^2-\lambda_dr_d
 \right).                                          \tag{2.3}
\]

### Lemma 2.1 (base-row collision dichotomy)

Let \(R,R'\) be protected rows from two affine base slices.  Then exactly
one of the following holds.

1. \(\Theta(R)\ne\Theta(R')\), and \(R,R'\) have at most two common
   \((\chi _1,\chi _2)\)-labels.
2. \(\Theta(R)=\Theta(R')\), and their complete moment traces lie on the
   same parabola; they can have as many as \(p\) common labels.

#### Proof

Subtract the two equations (2.2), now viewed as polynomials in
\(\chi _1\).  Unless all three coefficients agree, the difference is a
nonzero polynomial of degree at most two and has at most two roots.  If
all coefficients agree, the curves are identical.  Since \(v_d\ne0\),
each individual phase-to-\(\chi _1\) map is injective. \(\square\)

Inside one affine slice, distinct protected depths have distinct
curvatures:

\[
 \kappa_d={1\over\delta/\alpha+d}.                  \tag{2.4}
\]

Because \(|d-d'|<p\), one has

\[
 d\ne d'\quad\Longrightarrow\quad
 \kappa_d\ne\kappa_{d'}.                            \tag{2.5}
\]

Thus two different signed ranks in one slice never have identical moment
curves.

For two fixed ordered depth pairs \((d,e)\) and \((d',e')\), Lemma 2.1
gives the complete base-slice ordered-pair catalogue:

\[
\begin{array}{c|c}
\text{trace equivalences}&
\text{number of ordered pair-label coincidences}\\ \hline
\text{neither component equivalent}&\le4,\\
\text{exactly one component equivalent}&\le2p,\\
\text{both components equivalent}&\le p^2.
\end{array}                                        \tag{2.6}
\]

The last line is the genuine worst case.  It occurs, for example, for
distinct priority slices over the same affine base grid.

## 3. The full adjacent-switch orbit

There is an architectural point which cannot be skipped.  A nontrivial
adjacent switch destroys the literal affine order (1.2).  Therefore the
four-walk switch cube is not contained in the catalogue obtained by
requiring every trajectory to be affine.

The correct object is an affine **base** together with its entire
commuting adjacent-switch orbit.

Fix disjoint adjacent phase transpositions.  One toggle changes one
intermediate owner and, in every protected signed rank, one target in the
same physical column.  Under (1.2), the two exchanged coordinate labels
differ by \(\pm\alpha\).  Hence, for every switch vertex
\(\varepsilon\), there are functions

\[
 e_{d,t}(\varepsilon)\in\{-1,0,1\}                 \tag{3.1}
\]

such that

\[
 \boxed{
 \chi _1(F_d^\varepsilon(t))
 =
 r_d+v_dt+\alpha e_{d,t}(\varepsilon).}             \tag{3.2}
\]

At any physical phase, at most one of the disjoint switches contributes.
If the alternative target replaces a coordinate of label \(z\) by one
of label \(z+\alpha e\), then exactly

\[
 \boxed{
 \chi _2(F_d^\varepsilon(t))
 =
 \chi _2(F_d^0(t))
 +2\alpha e\,z+\alpha^2e^2.}                       \tag{3.3}
\]

Equations (3.2)--(3.3) are the exact switched row traces.  Priority
decoration may delete or reweight an occurrence, but it does not alter
its moment label.

### Lemma 3.1 (constant row-label multiplicity on switch orbits)

Let \(T,T'\) be phase subsets from two, possibly different, affine-base
switch slices.  For fixed signed depths \(d,d'\),

\[
\begin{aligned}
 \#\{(t,t')\in T\times T':\,
 &(\chi _1,\chi _2)(F_d^\varepsilon(t))\\
 &=(\chi _1,\chi _2)(F_{d'}^{\varepsilon'}(t'))\}
 \le3\min\{|T|,|T'|\}.                              \tag{3.4}
\end{aligned}
\]

#### Proof

Moment equality implies \(\chi _1\)-equality.  Fix \(t\in T\).  By
(3.2), for each of the three possible values
\(e_{d',t'}(\varepsilon')\in\{-1,0,1\}\), the equation

\[
 r_d+v_dt+\alpha e_{d,t}
 =
 r'_{d'}+v'_{d'}t'+\alpha'e'_{d',t'}               \tag{3.5}
\]

determines at most one \(t'\), since \(v'_{d'}\ne0\).  Thus there are at
most three choices of \(t'\) for every \(t\).  Reverse the roles of the
two slices and take the smaller bound. \(\square\)

The second moment is not needed for the worst-case constant in (3.4);
its role is to give the sharper base dichotomy (2.6) and to identify the
switched coordinate labels.  Indeed, when
\(\Delta_1=h(v)-h(u)\ne0\) and
\(\Delta_2=h(v)^2-h(u)^2\),

\[
 h(v)+h(u)={\Delta_2\over\Delta_1},                 \tag{3.6}
\]

so \((\Delta_1,\Delta_2)\) recovers the ordered pair of exchanged hash
labels because \(2\) is invertible.

## 4. Ordered target-pair moment labels

Fix two signed ranks \(d,e\).  Their values are determined by the two
target ranks in one pair-square block, so there is no sum over all
\(2Q+1\) rows.

Let \(J_\omega\) be the physically effective switch directions in an
outer slice \(\omega\), and let

\[
 \tau_\omega:J_\omega\longrightarrow I
 \tag{4.1}
\]

send a switch direction to its unique affected physical phase.  The map
\(\tau_\omega\) is injective for disjoint adjacent switches.  Define the
ordered moment-pair label

\[
\begin{aligned}
 \Psi_\omega(i,j)=\big(&
 \chi _1(F_d^\omega(\tau_\omega(i))),
 \chi _2(F_d^\omega(\tau_\omega(i))),\\
 &
 \chi _1(F_e^\omega(\tau_\omega(j))),
 \chi _2(F_e^\omega(\tau_\omega(j)))
 \big).
\end{aligned}                                       \tag{4.2}
\]

Let \({\cal Q}_\omega\subseteq J_\omega^2\) be any family of ordered
distinct direction pairs.  Put

\[
 {\cal C}_{\omega,\omega'}
 =
 \#\{((i,j),(i',j'))\in
       {\cal Q}_\omega\times{\cal Q}_{\omega'}:
       \Psi_\omega(i,j)=\Psi_{\omega'}(i',j')\}.    \tag{4.3}
\]

### Theorem 4.1 (cross-slice ordered-pair collision)

Uniformly over the two outer slices,

\[
 \boxed{
 {\cal C}_{\omega,\omega'}
 \le9 f_\omega f_{\omega'},
 \qquad f_\omega=|J_\omega|.}                       \tag{4.4}
\]

If the bounded-displacement presentation has \(m^{o(1)}\) possible local
orientations or priority states for one affected column, the right side
becomes \(m^{o(1)}f_\omega f_{\omega'}\).

#### Proof

Ignore the restrictions defining \({\cal Q}_\omega\) and
\({\cal Q}_{\omega'}\).  For the first target component, Lemma 3.1 gives
at most

\[
 3\min\{f_\omega,f_{\omega'}\}
\]

coincident phase pairs.  The same is true for the second component.
Choosing the two component coincidences determines the two ordered
direction pairs because each \(\tau\) is injective.  Their product is at
most

\[
 9\min\{f_\omega,f_{\omega'}\}^2
 \le9f_\omega f_{\omega'}.
\]

Restricting to the legal square families can only decrease this number.
\(\square\)

## 5. Weighted outer-slice consequence

Suppose the uniform-full-cube replacement assigns weight \(a_\omega\) to
each legal direction pair of slice \(\omega\), and suppose

\[
 |{\cal Q}_\omega|\ge c f_\omega^2.                 \tag{5.1}
\]

Let \(N_\omega(x,y)\) be the resulting weight of squares carrying the
ordered physical target pair \((x,y)\).  Exact physical equality implies
equality of the four moment labels.  Grouping physical pairs by their
moment labels can only add nonnegative cross terms.  Theorem 4.1 therefore
gives

\[
 \boxed{
 \sum_{x,y}N_\omega(x,y)N_{\omega'}(x,y)
 \le m^{o(1)}a_\omega a_{\omega'}
                   f_\omega f_{\omega'}.}          \tag{5.2}
\]

Write

\[
 S_\omega=a_\omega|{\cal Q}_\omega|
 \ge ca_\omega f_\omega^2.                         \tag{5.3}
\]

Then

\[
 \sum_{x,y}N_\omega(x,y)N_{\omega'}(x,y)
 \le
 {m^{o(1)}S_\omega S_{\omega'}
  \over f_\omega f_{\omega'}}.                     \tag{5.4}
\]

Consequently, for arbitrary nonnegative outer scalar weights already
absorbed into the \(a_\omega\)'s, if

\[
 f_\omega\ge f_*=p\,m^{-o(1)}
\]

on the retained size-biased slice mass, then

\[
\boxed{
\begin{aligned}
 \sum_{x,y}\sum_{\omega\ne\omega'}
 N_\omega(x,y)N_{\omega'}(x,y)
 &\le
 {m^{o(1)}\over f_*^2}
 \left(\sum_\omega S_\omega\right)^2\\
 &=m^{-1+o(1)}
 \left(\sum_\omega S_\omega\right)^2.
\end{aligned}}                                      \tag{5.5}
\]

This is precisely the desired raw cross-slice pair-label dispersal
factor.  Notice that no upper bound on the concentration of the scalar
weights \(a_\omega\) is used.

If the down-set replacement leaves a nonuniform direction-pair weight
\(w_\omega(i,j)\), the same proof applies to the uniform main term.
An \(m^{o(1)}\) pointwise ratio

\[
 \max_{i\ne j}w_\omega(i,j)
 \le m^{o(1)}{S_\omega\over f_\omega^2}             \tag{5.6}
\]

also suffices directly.  The present down-set theorem proves aggregate
\(\ell _1\) closeness, not (5.6); its error must be charged separately.

## 6. Affine vertices versus an affine-base switch orbit

The distinction used in Section 3 is necessary.

### Lemma 6.1 (an affine word has no nontrivial affine adjacent switch)

Let

\[
 z_i=B+\alpha i,\qquad \alpha\ne0,
 \]

be a full affine word indexed by \(\mathbb F_p\).  Let \(\pi\) be a product
of a subset of fixed disjoint adjacent transpositions.  If the permuted
word \(z_{\pi(i)}\) is also affine in \(i\), then \(\pi\) is the identity.

#### Proof

If

\[
 B+\alpha\pi(i)=B'+\alpha'i,
\]

then

\[
 \pi(i)=c+ri
\]

as a map of \(\mathbb F_p\).  Since \(\pi\) is an involution and every
displacement \(\pi(i)-i\) is \(0\) or a neighbouring unit, the affine
function

\[
 c+(r-1)i
\]

takes at most three values.  If \(r\ne1\), it takes all \(p>3\) values, a
contradiction.  Hence \(r=1\).  Involutivity gives \(2c=0\), and \(p\) is
odd, so \(c=0\).  Thus \(\pi\) is the identity. \(\square\)

Therefore an all-vertices-affine restriction deletes every switch edge
and every switch square.  Equations (3.2)--(3.3) show the viable
alternative: impose the affine equations only on a labelled base
trajectory and retain its complete bounded-displacement switch orbit.

This enlargement requires a fresh tag- and target-degree audit.  The
earlier affine partition function counts affine base schedules, not
automatically their labelled switch-orbit multiplicities.

## 7. What is and is not closed

The polynomial-moment calculation closes the following purely
cross-slice statement:

\[
 \boxed{
 \text{dense, uniformly weighted, physically effective affine-base
 switch slices have outer pair-label collision }m^{-1+o(1).}
 \tag{7.1}
\]

It also shows that trace-equivalent priority clones are not a
counterexample.  They attain the \(f_\omega f_{\omega'}\) numerator in
(4.4), but the two independent switch directions supply
\(f_\omega^2f_{\omega'}^2\) total square mass.

The survival-conditioned term is

\[
 \sum_{x,y}\sum_{\omega\ne\omega'}
 {N_\omega(x,y)N_{\omega'}(x,y)
  \over D_t(x)D_t(y)}.                              \tag{7.2}
\]

To deduce the required four-walk inequality from (5.5), one must still
prove:

1. \(f_\omega=p\,m^{-o(1)}\) outside a size-biased \(o(W)\) slice ledger;
2. the nonuniform down-set replacement error is summable after the
   factors \(D_t(x)^{-1}D_t(y)^{-1}\) are inserted;
3. the affine-base switch-orbit catalogue has the required target-fibre
   lower bounds and retains them under dynamic quarantine.

These are not formalities.  In particular, unweighted moment-label
collision does not control a term with arbitrarily small denominators.
The time-zero target-load theorem and the stopped lower-degree theorem are
still required.

Thus the answer is conditional but substantive:

\[
 \boxed{
 \begin{array}{l}
 \text{the two-moment hash supplies exactly the missing }
 m^{-1+o(1)}
 \text{ outer-label factor;}\\
 \text{the present catalogue has not yet supplied the dense-slice,
 denominator, and switch-orbit bridges.}
 \end{array}}
 \tag{7.3}
\]

No marginal target estimates were multiplied anywhere in the argument.
