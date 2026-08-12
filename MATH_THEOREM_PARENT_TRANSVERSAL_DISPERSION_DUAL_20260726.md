# Parent-transversal substitution: exact overload identities and the dispersion dual

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

A `D_(r+1)`-port-transversal local factor is an exact parent-context
substitute, but port-transversality by itself says nothing about lower-shadow
dispersion.  The correct depth-`r` object attached to a parent
replacement is the histogram of **all** depth-`r` windows meeting its
interior, including windows which cross either parent boundary.  The map
which records only the distinguished child-window target is not enough.

For one replacement the change of cap overload has an exact hinge
formula.  If `delta` is its full signed depth-`r` histogram, then

\[
 K_{r,b}(F')-K_{r,b}(F)=G_b(\delta;\mu)-R_b(\delta;\mu),
\]

where `R_b` is the amount removed from slots already above the cap and
`G_b` is the amount inserted beyond the available sub-cap room.  At the
row-power cap `b=p`, every subsequent row-power lift has missing-shadow
count at least

\[
 \left[K_{r,p}(F)+G_p-R_p-(W-N_r)\right]_+ .
\]

For a library of parent substitutes there is an exact fractional
dispersion theorem.  On an additive parent atlas, or after grouping all
overlapping parents into joint atoms, the least averaged overload equals
a weighted dual in which **every fractional target weight**
`alpha in [0,1]^(V_r)` must be tested.  Indicator-set tests are not
sufficient.  The multidepth version gives an exact dual for `PCap_H` and
forces the same local factor choice to serve every depth.

The dual condition is necessary for every integral construction and
sufficient for a fractional one.  An integral factor follows if the
joint atoms also have small centered square mass.  At the fatal parent
scale, a pointwise affected-window bound `O(p)` for **each entire
independently rounded additive atom** is enough for the one-depth rounding
error to be `o(W)`; no such bound follows from port-transversality.  In
particular, a one-parent `O(p)` bound does not control an overlap-connected
atom containing many parents.

Finally, cap-`p` dispersion does not control actual missing shadows.  It
only removes the `PCap` obstruction.  Actual holes are the cap-one
problem and require a separate, much stronger dispersion or orbit-cover
theorem.

---

## 1. Full affected-window histograms

Fix an exact ambient middle factor `F`.  At depth `q`, let

\[
 \mathcal V_q=\binom{[2m+1]}{m-q},\qquad
 N_q=|\mathcal V_q|,
\]

and let

\[
 \mu_q^F(S)=\#\{\text{rooted depth-`q` windows of `F` with target }S\}.
\]

Every factor has exactly `W` such rooted windows, so

\[
                         \sum_{S\in\mathcal V_q}\mu_q^F(S)=W.       \tag{1.1}
\]

For an integer cap `b>=1`, put

\[
 K_{q,b}(F)=\sum_{S\in\mathcal V_q}(\mu_q^F(S)-b)_+.                \tag{1.2}
\]

The `PCap` overload is `K_q=K_(q,p)`, where `p=2m+1` is the row-power
orbit length.

Let `C` be an aligned size-`r+1` parent context.  Write `G_0` for the
canonical local factor and let `G` be another `D_(r+1)`-port-transversal exact
local factor.  Rooting every wreath at its unique member of `D_(r+1)`
fixes its two parent boundary states row by row.  The port-transversal
context-substitution theorem therefore gives another exact ambient
factor, denoted

\[
                         F'=F[C\leftarrow G].                       \tag{1.3}
\]

Let `I_(C,q)` be the set of rooted depth-`q` windows which contain an
interior phase of `C`.  Boundary states are fixed, so every window outside
`I_(C,q)` is unchanged.  Define the full local histograms

\[
 u_{C,G,q}(S)
 =\#\{I\in I_{C,q}:\text{ the target of `I` after installing `G` is }S\}
                                                                    \tag{1.4}
\]

and

\[
 \delta_{C,G,q}=u_{C,G,q}-u_{C,G_0,q}.                              \tag{1.5}
\]

Then

\[
 \mu_q^{F'}=\mu_q^F+\delta_{C,G,q},
 \qquad \sum_S\delta_{C,G,q}(S)=0.                                 \tag{1.6}
\]

The definition includes the two crossing-window collars.  In particular,
it is generally larger than the histogram of the distinguished nested
child windows.  Those distinguished windows prove that a parent
substitution can split a canonical Catalan fibre; they do not determine
the full vector (1.5).

---

## 2. Exact change under one parent replacement

### Theorem 2.1 (exact hinge identity)

Let `mu=mu_q^F`, `delta=delta_(C,G,q)`, and assume, as follows from the
replacement construction, that `mu+delta>=0`.  Define

\[
\begin{aligned}
 R_b(\delta;\mu)
   &=\sum_{\delta(S)<0}
       \min\{-\delta(S),(\mu(S)-b)_+\},\\
 G_b(\delta;\mu)
   &=\sum_{\delta(S)>0}
       \bigl(\delta(S)-(b-\mu(S))_+\bigr)_+ .             \tag{2.1}
\end{aligned}
\]

Then

\[
 \boxed{
 K_{q,b}(F[C\leftarrow G])-K_{q,b}(F)
   =G_b(\delta;\mu)-R_b(\delta;\mu).}                    \tag{2.2}
\]

Thus a parent replacement decreases overload precisely when the amount
removed from the old excess exceeds the amount of its positive collateral
which crosses the cap.

#### Proof

For `x>=0`, `x+d>=0`, a direct scalar calculation gives

\[
 (x+d-b)_+-(x-b)_+
 =\begin{cases}
   \bigl(d-(b-x)_+\bigr)_+,&d\ge0,\\
   -\min\{-d,(x-b)_+\},&d<0.
  \end{cases}                                             \tag{2.3}
\]

Apply (2.3) at every target and sum. \(\square\)

The identity is exact even when a positive and a negative arm lie on the
same side of the old overloaded set.  In particular, moving a marked
child occurrence away from a plateau does not imply a decrease: the
other affected windows are part of `G_b` and `R_b` with equal status.

For the depth-`q` summand of `PCap`, with `c_q=W-N_q`, (2.2) gives the
literal change

\[
 \boxed{
 \bigl[K_{q,p}(F)+G_p-R_p-c_q\bigr]_+
       -\bigl[K_{q,p}(F)-c_q\bigr]_+.}                   \tag{2.3a}
\]

Thus relief which merely lowers `K_(q,p)` toward the unavoidable budget
`c_q` is useful, while relief below that budget does not create a negative
credit at another depth.

### Theorem 2.2 (exact missing-shadow change)

Let

\[
 M_q(F)=|\{S\in\mathcal V_q:\mu_q^F(S)=0\}|.             \tag{2.4}
\]

Then

\[
\boxed{
\begin{aligned}
 M_q(F[C\leftarrow G])-M_q(F)
  ={}&|\{S:\mu(S)>0,\ \mu(S)+\delta(S)=0\}|\\
    &-|\{S:\mu(S)=0,\ \delta(S)>0\}|.                  \tag{2.5}
\end{aligned}}
\]

Equivalently,

\[
                         M_q(F)=K_{q,1}(F)-(W-N_q),        \tag{2.6}
\]

so the left side of (2.5) is also

\[
                         G_1(\delta;\mu)-R_1(\delta;\mu). \tag{2.7}
\]

#### Proof

Equation (2.5) lists the old positive targets which become zero and the
old zero targets which become positive.  For (2.6), an integral load
satisfies

\[
 K_{q,1}=\sum_S(\mu(S)-1)_+
        =W-|\{S:\mu(S)>0\}|=W-N_q+M_q.
\]

Now apply Theorem 2.1 with `b=1`. \(\square\)

### Corollary 2.3 (the row-power missing-shadow inequality)

Let `a` be any assignment of powers of a coordinate `p`-cycle to the
rows of the replaced seed; middle legality of the shifted family is not
needed.  If `H_q((F')_a)` is its number of missing depth-`q` targets, then

\[
\boxed{
 H_q((F')_a)
 \ge
 \left[
 K_{q,p}(F)+G_p(\delta;\mu)-R_p(\delta;\mu)
                 -(W-N_q)
 \right]_+.}                                             \tag{2.8}
\]

#### Proof

The `mu_q^(F')(S)` occurrences of one source target can occupy at most
`min{mu_q^(F')(S),p}` members of its coordinate-cycle orbit.  Taking the
union over source targets can only reduce coverage, so the number of
covered targets is at most

\[
 \sum_S\min\{\mu_q^{F'}(S),p\}=W-K_{q,p}(F').
\]

Hence

\[
 H_q((F')_a)\ge N_q-W+K_{q,p}(F').                        \tag{2.9}
\]

Combine (2.9) with (2.2), and use nonnegativity of `H_q`. \(\square\)

Equation (2.8) is a lower bound.  There is no converse from cap-`p`
overload alone.

---

## 3. Additive parent atoms

Suppose a family of parent contexts has been selected.  Call it
**`q`-influence-disjoint** when no rooted depth-`q` window meets the
interiors of two selected contexts.  In that case the depth-`q` load has
the exact form

\[
 \mu_q^{\mathbf G}
   =\lambda_q+\sum_{C\in\mathcal C}u_{C,G_C,q},           \tag{3.1}
\]

where `lambda_q` is the histogram of all unaffected windows and each
`G_C` may be chosen from a local library `mathscr L_C`.

Phase-disjointness is weaker than influence-disjointness.  Two adjacent
parent slabs have disjoint state and edge ledgers, and hence may be
substituted independently as exact factors, while one depth-`q` window
can still meet both interiors.  Its target is an intersection involving
both replacements and is not the sum of the two isolated changes.

There is an exact way to remove this qualification.  Join two parent
contexts when some depth-`q` window meets both.  Treat every connected
component `A` of this overlap graph as one **joint atom**.  Its library is
the collection of all jointly legal local-factor assignments inside
`A`, and `u_(A,G,q)` is their actual joint affected-window histogram.
No window meets two distinct atoms, so (3.1) holds with `A` in place of
`C`.  All results below apply to these joint atoms.  A giant overlap atom
is therefore not a formal problem, but it may destroy the fragmentation
needed for integral rounding.

---

## 4. The exact one-depth dispersion property

For each additive atom `C`, let `mathscr L_C` be a finite library of
`D_(r+1)`-port-transversal local factors, or a joint library as in Section 3.
Let `Delta(mathscr L_C)` be its probability simplex.  Define the least
fractional cap tail

\[
 \Phi_{q,b}
 =\min_{(\pi_C)}
 K_b\left(
   \lambda_q+
   \sum_C\sum_{G\in\mathscr L_C}\pi_C(G)u_{C,G,q}
       \right),
 \quad \pi_C\in\Delta(\mathscr L_C).                    \tag{4.1}
\]

Here `K_b(x)=sum_S(x(S)-b)_+` is defined for real nonnegative vectors.

### Theorem 4.1 (weighted parent-dispersion dual)

One has the exact identity

\[
\boxed{
 \Phi_{q,b}
 =\max_{0\le\alpha\le1}
 \left[
   \langle\alpha,\lambda_q-b\mathbf1\rangle
   +\sum_C\min_{G\in\mathscr L_C}
          \langle\alpha,u_{C,G,q}\rangle
 \right].}                                               \tag{4.2}
\]

Consequently a library has fractional residual at most `epsilon W` if
and only if, for every fractional target test

\[
                         \alpha:\mathcal V_q\to[0,1],
\]

one has

\[
\boxed{
 \langle\alpha,\lambda_q-b\mathbf1\rangle
 +\sum_C\min_{G\in\mathscr L_C}
       \langle\alpha,u_{C,G,q}\rangle
 \le\epsilon W.}                                        \tag{4.3}
\]

This is the exact averaged dispersion property at one depth.

#### Proof

Coordinatewise scalar duality gives

\[
 K_b(x)=\max_{0\le\alpha\le1}
                    \langle\alpha,x-b\mathbf1\rangle.   \tag{4.4}
\]

The product of the finite probability simplexes and the target-weight
cube are compact convex sets, and the expression after substituting
(4.4) into (4.1) is bilinear.  Finite-dimensional minimax therefore
allows the minimum and maximum to be interchanged.  For fixed `alpha`,
minimization over `pi_C` gives

\[
 \min_{\pi_C}\sum_G\pi_C(G)
       \langle\alpha,u_{C,G,q}\rangle
 =\min_G\langle\alpha,u_{C,G,q}\rangle.
\]

Summing over atoms proves (4.2), and (4.3) is equivalent to
`Phi_(q,b)<=epsilon W`. \(\square\)

The quantifier over all fractional `alpha` cannot in general be replaced
by indicator sets.  Here is an integral three-target example.  Take cap
`b=10`, fixed residual

\[
                         \lambda=(6,4,0),
\]

and one atom with two equal-mass choices

\[
                         u_1=(10,0,10),\qquad
                         u_2=(0,20,0).                    \tag{4.5}
\]

For every subset `A` of the three targets,

\[
 \langle\mathbf1_A,\lambda-10\mathbf1\rangle
       +\min_i\langle\mathbf1_A,u_i\rangle\le0.          \tag{4.6}
\]

Indeed the eight values, in the order
`emptyset,1,2,3,12,13,23,123`, are

\[
                         0,-4,-6,-10,0,-14,-6,0.
\]

But for `alpha=(1,1/2,0)` the left side of (4.3) is

\[
                         -7+\min\{10,10\}=3>0.           \tag{4.7}
\]

The reason is that one common local choice must serve all level sets of
`alpha`; the minimizing choice may be different for different indicator
sets.

Any integral selection with `K_(q,b)<=epsilon W` gives point-mass
distributions in (4.1), so (4.3) is necessary for every integral theorem.
It is only fractionally sufficient until a rounding estimate is supplied.

---

## 5. The exact multidepth `PCap` dual

Put

\[
                         c_q=W-N_q
\]

and recall

\[
 \operatorname {PCap}_H(F)
   =\sum_{q\le H}\bigl(K_{q,p}(F)-c_q\bigr)_+.           \tag{5.1}
\]

The same local factor `G_C` must be used at every depth.  Let
`lambda_q` and `u_(C,G,q)` be the simultaneous histograms in the additive
decomposition (3.1).  For this multidepth statement, the overlap graph in
Section 3 is formed by joining parents whenever a window at **any** depth
`q<=H` meets both; its connected components are the common atoms at all
depths.  Define

\[
 \Phi_H^{\rm PCap}
 =\min_{(\pi_C)}
 \sum_{q\le H}
 \left[
 K_p\left(\lambda_q+\sum_{C,G}\pi_C(G)u_{C,G,q}\right)
                 -c_q
 \right]_+.                                               \tag{5.2}
\]

### Theorem 5.1 (coherent multidepth dispersion dual)

For `gamma_q in [0,1]^(mathcal V_q)`, write
`||gamma_q||_infinity=max_S gamma_q(S)`.  Then

\[
\boxed{
\begin{aligned}
 \Phi_H^{\rm PCap}
 =\max_{(\gamma_q)}\Bigg\{
 &\sum_{q\le H}
   \left[
    \langle\gamma_q,\lambda_q-p\mathbf1\rangle
       -c_q\|\gamma_q\|_\infty
   \right]\\
 &+\sum_C\min_{G\in\mathscr L_C}
       \sum_{q\le H}\langle\gamma_q,u_{C,G,q}\rangle
 \Bigg\}.                                                \tag{5.3}
\end{aligned}}
\]

Hence the exact fractional `PCap_H=o(W)` dispersion requirement is that,
for **every** family of fractional depth-target tests `(gamma_q)`, the
quantity in braces in (5.3) be at most `o(W)`, with one error bound uniform
over that family.  No lower bound on a negative test value is intended.

#### Proof

For every real load `x` and `c>=0`,

\[
\begin{aligned}
 (K_p(x)-c)_+
 &=\max_{0\le\theta\le1}\theta(K_p(x)-c)\\
 &=\max_{0\le\gamma\le1}
   \left[
      \langle\gamma,x-p\mathbf1\rangle
       -c\|\gamma\|_\infty
   \right].                                              \tag{5.4}
\end{aligned}
\]

For the second equality, first put `gamma=theta alpha` in (4.4).  Conversely,
for fixed `gamma`, the least admissible `theta` is
`||gamma||_infinity`; this is optimal because `c>=0`.

Sum (5.4) over depths.  The resulting payoff is linear in each `pi_C`
and concave in `(gamma_q)`, since `-c_q||gamma_q||_infinity` is concave.
Minimax applies.  Minimizing one atom's common distribution gives

\[
 \min_{G\in\mathscr L_C}
       \sum_{q\le H}\langle\gamma_q,u_{C,G,q}\rangle,
\]

not a separate minimum at each depth.  This proves (5.3). \(\square\)

The final minimum in (5.3) is the precise chronology/coherence
requirement on a local-factor library: a single parent factor must
disperse the entire weighted multidepth test.  Good members chosen
separately for different depths do not prove (5.3).

---

## 6. Integral rounding and the required square fragmentation

Assume distributions `pi_C` have been chosen.  Select the atom states
independently and put

\[
\begin{aligned}
 \bar u_{C,q}(S)&=\mathbb E_{\pi_C}u_{C,G,q}(S),\\
 \bar\mu_q(S)&=\lambda_q(S)+\sum_C\bar u_{C,q}(S),\\
 V_q(S)&=\sum_C\operatorname {Var}_{\pi_C}
                         u_{C,G,q}(S).                    \tag{6.1}
\end{aligned}
\]

### Theorem 6.1 (integral `PCap` rounding)

Some integral choice of one library member per atom satisfies

\[
\boxed{
 \operatorname {PCap}_H(F_*)
 \le \operatorname {PCap}_H(\bar\mu)
      +{1\over2}\sum_{q\le H}\sum_{S\in\mathcal V_q}
                                \sqrt{V_q(S)}.}           \tag{6.2}
\]

Consequently the exact fractional dispersion condition (5.3), together
with

\[
             \sum_{q\le H}\sum_S\sqrt{V_q(S)}=o(W),      \tag{6.3}
\]

produces an integral exact factor with `PCap_H=o(W)`.

#### Proof

Let `Y_q=mu_q^(F_*)-bar(mu)_q`.  Since every local histogram has fixed
total mass, `sum_S Y_q(S)=0`.  The scalar inequality

\[
 (x+y-p)_+-(x-p)_+\le y_+
\]

gives

\[
 K_p(\bar\mu_q+Y_q)-K_p(\bar\mu_q)
 \le\sum_SY_q(S)_+={1\over2}\|Y_q\|_1.                  \tag{6.4}
\]

The positive-part map is one-Lipschitz, so (6.4) implies the analogous
bound after subtracting `c_q` and taking a positive part.  Independence
and Cauchy--Schwarz give

\[
 \mathbb E|Y_q(S)|\le\sqrt{V_q(S)}.
\]

Sum over depths.  The expectation of `PCap_H` obeys the right side of
(6.2), so one realization does also. \(\square\)

For one depth there is a sharper square-mass criterion.  Put

\[
                         \Sigma_q=\sum_SV_q(S).           \tag{6.5}
\]

### Proposition 6.2 (one-depth margin rounding)

For every `0<a<p`, some integral choice satisfies

\[
\boxed{
 K_{q,p}(F_*)
 \le K_p(\bar\mu_q)
 +{1\over2}\sqrt{\frac{W\Sigma_q}{p-a}}
 +{\Sigma_q\over4a}.}                                   \tag{6.6}
\]

In particular, with `a=p/2`,

\[
 K_{q,p}(F_*)
 \le K_p(\bar\mu_q)
       +\sqrt{\frac{W\Sigma_q}{2p}}
       +{\Sigma_q\over2p}.                              \tag{6.7}
\]

Thus

\[
             K_p(\bar\mu_q)=o(W),\qquad
             \Sigma_q=o(pW)                              \tag{6.8}
\]

are sufficient for an integral depth-`q` overload `o(W)`.

#### Proof

Let

\[
 D=\{S:\bar\mu_q(S)>p-a\}.
\]

Since the mean load has total mass `W`, `|D|<=W/(p-a)`.  On `D`,

\[
 \mathbb E(\bar\mu+Y-p)_+
 \le(\bar\mu-p)_++{1\over2}\sqrt{V_q(S)},               \tag{6.9}
\]

because a centered random variable has
`E(Y_+)=E|Y|/2`.  Off `D`, use the scalar inequality

\[
                         (y-a)_+\le {y^2\over4a}.         \tag{6.10}
\]

Summing (6.9), applying Cauchy--Schwarz on `D`, and summing (6.10)
outside `D` proves the expected version of (6.6).  Choose one realization
no worse than its expectation. \(\square\)

The square condition is not a consequence of port-transversality.  It is the
integral-fragmentation half of the required library property.

---

## 7. Exact parent-scale accounting

Let `r` be minimal with

\[
                         d=\operatorname {Cat}_r\ge4p.    \tag{7.1}
\]

Then `d<16p`, `r=Theta(log p)`, and

\[
                         \operatorname {Cat}_{r+1}<64p.  \tag{7.2}
\]

A rooted size-`r+1` local factor has `Cat_(r+1)` rows.  Its two boundary
states are fixed; only its `r` internal phases may change.  A depth-`r`
window has boundary phases separated by `r`, so in one row at most `2r`
window starts can meet an internal parent phase.  Therefore one full
parent substitution has affected-window mass at most

\[
                         w_C\le2r\operatorname {Cat}_{r+1}=O(rp).    \tag{7.3}
\]

There are

\[
 H_{m,r+1}={1\over2}\binom{2(m-r-1)}{m-r-1}              \tag{7.4}
\]

aligned size-`r+1` contexts, and, uniformly for `r^2/m=o(1)`,

\[
 {H_{m,r+1}\over W}
 ={1\over4\,4^{r+1}}
       \exp O\!\left({r^2\over m}+{1\over m}\right).    \tag{7.5}
\]

Since

\[
 \operatorname {Cat}_{r+1}
 =\Theta\!\left({4^{r+1}\over r^{3/2}}\right),
\]

(7.3)--(7.5) give the exact-scale bound

\[
 \boxed{
 \sum_Cw_C=O\!\left({W\over\sqrt r}\right).}            \tag{7.6}
\]

Here and below an influence-disjoint atlas may contain fewer contexts,
which only improves the upper bound.

Now let `A` index the objects which are actually rounded independently.
Thus `A` is either one parent in an influence-disjoint atlas or one whole
connected joint atom of the overlap graph from Section 3.  Write `w_A` for
the number of affected slots of `A`.  The affected slots of distinct
additive atoms are disjoint, while the union bound over their constituent
parents gives

\[
                         \sum_Aw_A=O(W/\sqrt r).          \tag{7.6a}
\]

Define the maximum **atomwise** affected-target multiplicity

\[
 L_{r,\mathcal A}^{\max}
   =\max_{A,\mathbf G,S}u_{A,\mathbf G,r}(S),            \tag{7.7}
\]

where `mathbf G` is a jointly legal assignment throughout `A`.  Then

\[
\begin{aligned}
 \Sigma_r
 &\le\sum_A\mathbb E_{\mathbf G}\sum_Su_{A,\mathbf G,r}(S)^2\\
 &\le L_{r,\mathcal A}^{\max}\sum_Aw_A
 =O\!\left({L_{r,\mathcal A}^{\max}W\over\sqrt r}\right). \tag{7.8}
\end{aligned}
\]

Thus the exact square condition `Sigma_r=o(pW)` follows from

\[
                  L_{r,\mathcal A}^{\max}=o(p\sqrt r).    \tag{7.9}
\]

In particular `L_(r,mathcal A)^{max}=O(p)` is more than sufficient.  In
that case (6.7) has rounding error

\[
                         O(Wr^{-1/4})+O(Wr^{-1/2})=o(W).  \tag{7.10}
\]

For one parent the crude consequence of port-transversality is only
`max_(G,S)u_(C,G,r)(S)<=w_C=O(rp)`, which does not imply (7.9).
Moreover, even a separately proved one-parent `O(p)` bound would not imply
(7.9) for a giant joined atom: adjacent pairwise interactions may form a
long overlap-connected chain.  One must either choose an
influence-disjoint atlas or prove (7.9) for every whole joint atom.
Therefore even at one matched depth the necessary library theorem has two
independent clauses:

1. weighted mean dispersion, namely (4.3), or its coherent multidepth
   form (5.3);
2. local square fragmentation, namely (6.3) for `PCap` rounding or
   (6.8) for one-depth overload.

---

## 8. Why cap dispersion is not hole dispersion

The `PCap` condition uses cap `p`; direct missing shadows use cap one.
There is no implication between them at the needed strength.  For
example, when `p>=2`, the load vectors

\[
 (1,1,\ldots,1)
 \quad\hbox{and}\quad
 (2,0,2,0,\ldots,2,0)                                    \tag{8.1}
\]

have the same total mass and both have cap-`p` overload zero, while the
second has half of all targets missing.

The exact fractional analogue of missing-shadow count is

\[
 \mathfrak H_q(x)
 :=K_1(x)-(W-N_q)
 =\sum_{S\in\mathcal V_q}(1-x(S))_+.                     \tag{8.2}
\]

For integral `x`, this is precisely `M_q`.  Theorem 4.1 with `b=1`
therefore gives the exact fractional parent-dispersion dual for direct
holes.  The corresponding independent-rounding scale is

\[
                         \Sigma_q=o(W),                   \tag{8.3}
\]

rather than `Sigma_q=o(pW)`.  Nothing in `D_(r+1)`-port-transversality or in
cap-`p` mean dispersion supplies (8.3).

Accordingly, a parent library satisfying (5.3) can remove the seed-level
`PCap_H` obstruction and still leave the actual missing-shadow problem
open.  To finish a row-power construction one additionally needs a legal
common phase assignment realizing near-complete target-orbit coverage.
Corollary 2.3 remains the only unconditional implication from `K_(q,p)`
to those holes, and it is one-sided.

---

## 9. Proved boundary

The following statements are now rigorous.

1. A single `D_(r+1)`-port-transversal replacement changes depth-`r`
   overload by the exact full-histogram formula (2.2), and changes direct
   missing shadows by (2.5).
2. Every row-power lift after that replacement obeys the exact lower
   bound (2.8).
3. For an additive or joint-atom parent library, (4.3) is the necessary
   and sufficient **fractional** one-depth dispersion property.
4. Formula (5.3) is the exact coherent fractional property for
   `PCap_H`; it keeps all depth and common-choice quantifiers.
5. Conditions (6.3) or (6.8) are rigorous integral-rounding hypotheses.
   The parent-scale accounting (7.6)--(7.10) shows exactly what local
   multiplicity estimate would suffice.

What is not proved is the existence of a noncanonical
`D_(r+1)`-port-transversal library satisfying the weighted dual and square
fragmentation.  Transversality alone admits the singleton canonical
library, for which no source fibre moves.  Nor is dispersion of the
distinguished nested child map enough: all crossing-window targets in
(1.4) enter the dual.  Finally, phase-disjoint substitutions must either
be thinned to an influence-disjoint atlas or analyzed through their joint
overlap atoms.

Thus the exact next finite/local theorem is:

> Construct `D_(r+1)`-port-transversal local factors whose full affected-window
> histograms satisfy (5.3) and whose joint overlap atoms satisfy (6.3),
> or exhibit a fractional weight family `(gamma_q)` violating (5.3) for
> every such library.

No constant-one conclusion follows without that theorem and the separate
phase/orbit realization gate.
