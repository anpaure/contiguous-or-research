# Complete-row blocker conjugation closes transported energy; switch normalization remains a literal gate

**Date:** 2026-08-06  
**Method:** full composite-row polarization, coordinate-conjugate
first-entry transport, exact density/rate calculation, and a scaling audit
of the auxiliary private-switch graph; no computation or search  
**Status:** proof-safe conditional closure plus an exact normalization
obstruction.  The complete-row involution pays all changed occurrences of
a full conjugate switch, including the constant-support lower queue
holonomy.  The present notes do not identify the auxiliary switch
conductance with the actual Bellman/Duhamel coefficient, so capacity
faithfulness is not yet unconditional.

## 1. The actual service and incidence scalars

The balanced-doublet clock has

\[
 p_{i+1}=p_i-\frac{2d}{M},
 \qquad
 \rho_i=\frac{p_{i+1}}{p_i},
\tag{1.1}
\]

and, on the global-rate bootstrap,

\[
 X_i=(1+o(1))\frac{p_iM}{2d}.
\tag{1.2}
\]

The service-damped Gramian uses

\[
                         a_i=\rho_i^2.
\tag{1.3}
\]

Consequently

\[
\begin{aligned}
 X_i(1-a_i)
 &=X_i(1-\rho_i)(1+\rho_i)\\
 &=\left((1+o(1))\frac{p_iM}{2d}\right)
   \left(\frac{2d}{p_iM}\right)(1+\rho_i)\\
 &=2+o(1).
\end{aligned}
\tag{1.4}
\]

Thus the original service scalar is already bounded above and below by
absolute positive constants.

For a resource type \(T\), the coefficient extracted in the joint
Lyapunov is exactly

\[
 \beta_T(i)=
 \frac{\sum_{x\in T_i}g_x^\circ(i)}
      {\sum_{x\in T_i}Y_x(i)},
\qquad
 g_x^\circ(i)=
 \sum_{\substack{A:\,x\in U_A^\circ}}
       \mu_i(A),
\tag{1.5}
\]

where

\[
                         \mu_i(A)=c_i(A)R_i(A)
\tag{1.6}
\]

is the actual hypothetical-next composite-row coefficient.  Under the
small potential cap, the authenticated incidence count gives

\[
                         \beta_T(i)
 \le \frac{C\varepsilon_P}{d^2}.
\tag{1.7}
\]

Equations (1.4)--(1.7) are definitions or already audited consequences;
no private-switch normalization enters them.

## 2. Full composite-row switch energy

Let \(A\) be an occurrence-labelled composite row, let \(\tau\) be a
coordinate transposition, and write

\[
 z_A=\sum_{x\in U_A^\circ\cap T}e_x,
 \qquad
 g_A=\langle z_A,f\rangle.
\tag{2.1}
\]

Suppose \(A\) survives the accepted blocker \(G\), while \(\tau A\) is
killed.  The resource-layer incidence of this full switch is

\[
                         b_{A,\tau}=z_A-z_{\tau A},
\tag{2.2}
\]

and its Dirichlet contribution is

\[
 \langle f,b_{A,\tau}b_{A,\tau}^*f\rangle
                         =(g_A-g_{\tau A})^2.
\tag{2.3}
\]

This formula is well typed: the resolvent acts on the resource vector
\(f\), while (2.3) is the ordinary positive birth form.  No resolvent is
applied to the scalar \(g_A\).

The elementary complete-row polarization is

\[
 \boxed{
 (g_A-g_{\tau A})^2
 \le 2g_A^2+2g_{\tau A}^2.}
\tag{2.4}
\]

Unlike a changed-occurrence expansion, (2.4) retains every hit and unhit
changed occurrence automatically.

## 3. Blocker conjugation

Choose any blocker-hit changed resource \(y\) on the killed shore and put

\[
                         x=\tau y,\qquad H=\tau G.
\tag{3.1}
\]

Since \(G\) misses the survivor \(A\), the conjugate blocker \(H\) misses
\(\tau A\).  Since \(G\) contains \(y\), \(H\) contains \(x\), a resource
of \(A\).  Hence

\[
                         (\tau A,G,y)
 \longmapsto (A,\tau G,\tau y)
\tag{3.2}
\]

is a counterfactual first-entry tuple on the opposite shore.

Coordinate covariance of the complete raw host gives

\[
 a_{\tau G}(i)=a_G(i),
\qquad
 \mu_i^+(\tau A;G)=\mu_i^+(A;\tau G).
\tag{3.3}
\]

The target blocker need not be dynamically live: the static rooted-overlap
ledger is a complete-host upper sum.

Retain the transposition label in (3.2).  The map is then an involution.
After forgetting the label, a target has at most
\(\binom{k}{2}\) preimages, cancelled by the uniform transposition factor

\[
                         \kappa_k=\binom{k}{2}^{-1}.
\tag{3.4}
\]

Occurrence repeats must be retained with their literal multiplicity.  On
the resource-simple private faces there is no further fibre.

## 4. Complete-row transported-ROc theorem

Let \(\mathcal B_i\) be a collection of full-conjugate first-kill
boundaries.  Let \(w_i(A,\tau,G)\) be their actual nonnegative
hypothetical-next coefficient, including the transition probability and
the factor \(\kappa_k\).

Assume the authenticated raw first-entry ledger bounds the complete
killed-row squares

\[
\begin{aligned}
 \mathbb E\sum_i \frac{\beta_T(i)d}{X_i}
 \sum_{(A,\tau,G)\in\mathcal B_i}
 w_i(A,\tau,G)\,g_{\tau A}^2
 \le C\mathsf A,
\end{aligned}
\tag{4.1}
\]

and the same complete-host ledger after coordinate relabelling.  Then

\[
\boxed{
 \mathbb E\sum_i \frac{\beta_T(i)d}{X_i}
 \sum_{(A,\tau,G)\in\mathcal B_i}
 w_i(A,\tau,G)\,(g_A-g_{\tau A})^2
 \le C\mathsf A.}
\tag{4.2}
\]

### Proof

The killed-row part \(g_{\tau A}^2\) is (4.1).  Map the survivor-row part
\(g_A^2\) by (3.2).  Equations (3.3)--(3.4) preserve its coefficient and
give total multiplicity at most one in the complete-host first-entry
ledger.  Apply (2.4) and add the two bounds.  \(\square\)

This theorem is stronger than endpoint transport.  It pays all changes in
one full conjugate switch, whether or not the accepted blocker meets the
individual changed resource.

### Marked aggregate

If the marked family fixes finitely many occurrence roles but sums every
coordinate labelling in its complete orbit, augment (3.2) by

\[
                         h\longmapsto\tau h.
\tag{4.3}
\]

This is a bijection of the marked complete-host sum.  Therefore (4.2)
holds for the raw orbit-summed marked family.  It need not hold in one
fixed non-covariant labelled cylinder.

## 5. Lower deletion holonomy is paid without a new cluster

An adjacent lower deletion-order swap changes one current lower state and
the order of the exported queue.  In the next block it changes exactly
one owner state in each of the \(h\in\{2,3\}\) owner copies.  The next
outgoing queue depends only on the next deletion order, so the global
transposition has closed support

\[
                         1+h\le4.
\tag{5.1}
\]

It is nevertheless one full coordinate conjugation
\(A\leftrightarrow\tau A\).  Its resource incidence is the sum of those
at most four changed Johnson incidences, and its entire energy is exactly
\((g_A-g_{\tau A})^2\).  Theorem 4.1 therefore pays the whole lower
holonomy switch.  No separate charge for the at most three unhit
companions, and no size-four marked-cluster theorem, is required.

This conclusion depends on keeping the complete row until after
polarization.  Expanding into individual changed edges and retaining only
the blocker-hit edge would recreate a false unhit-component gap.

## 6. The orbit scalar is not presently tied to \(\beta_T\)

Let \(\Gamma_i\) be an auxiliary private-switch graph with conductances
\(w_i(A,A')\), and let its projected full operator be

\[
 L_i^{\rm sw}
 =\sum_{\{A,A'\}\in E(\Gamma_i)}
 w_i(A,A')(z_A-z_{A'})(z_A-z_{A'})^*.
\tag{6.1}
\]

On a complete coordinate orbit, symmetry implies

\[
                         L_i^{\rm sw}=\alpha_iL_T
\tag{6.2}
\]

for some orbit scalar \(\alpha_i\), on a one-occurrence layer; a
constant-support switch gives the analogous domination after a fixed
Cauchy factor.

The current sources do not define the conductances in (6.1) from
\(\mu_i(A)\).  In fact the private-switch structural theorem explicitly
permits rescaling its switch measure to make the projected scalar one.
This produces a decisive scaling obstruction.

### Proposition 6.1 (normalization non-identifiability)

From the currently stated private-switch geometry, complete-orbit
symmetry, the definitions (1.1)--(1.7), and the static rooted ledgers, one
cannot deduce

\[
 \frac{X_i(1-a_i)\beta_T(i)}{\alpha_i}
                         =\Theta(1).
\tag{6.3}
\]

### Proof

Fix every macro-clock rate, composite coefficient, resource load, and
future potential.  Thus \(X_i,a_i,\mu_i,g_x^\circ\), and \(\beta_T(i)\)
are fixed.  Multiply every auxiliary private-switch conductance by an
arbitrary scalar \(t>0\).  All the listed quantities and every switch
adjacency are unchanged, while

\[
                         \alpha_i\longmapsto t\alpha_i.
\]

The left side of (6.3) is divided by \(t\).  Since \(t\) is arbitrary,
neither an upper nor a lower absolute bound follows.  \(\square\)

The obstruction is definitional, not probabilistic.  The symbol
\(\alpha_i\) does not occur in the authenticated Bellman construction,
and no theorem identifies an arbitrary Bellman prefactor with
\(\beta_T\).

There is an exact double count once a literal conductance is declared.
For a composite row \(A\), put

\[
 n_T(A)=|U_A^\circ\cap T|,
\tag{6.4}
\]

and let \(s_T(A)\) be the number of declared private switches incident to
\(A\) whose projected change has type \(T\), counted with the same
orientation convention used by the switch Laplacian.  Suppose

\[
                         w_i(A,A')\asymp\mu_i(A)=\mu_i(A')
\tag{6.5}
\]

on every declared switch edge.  Define the trace orbit scalar by

\[
 \alpha_i^{\rm tr}
 =\frac{\operatorname {tr}L_i^{\rm sw}}
        {\operatorname {tr}L_T}.
\tag{6.6}
\]

For the normalized Johnson Laplacian,
\(\operatorname {tr}L_T=N_T(i)\).  Since one Johnson incidence has squared
norm two, undirected-edge double counting gives

\[
 \alpha_i^{\rm tr}
 \asymp\frac{\sum_A\mu_i(A)s_T(A)}{N_T(i)}.
\tag{6.7}
\]

On the other hand, (1.5) gives exactly

\[
 \beta_T(i)
 =\frac{\sum_A\mu_i(A)n_T(A)}
        {\sum_{x\in T_i}Y_x(i)}.
\tag{6.8}
\]

### Proposition 6.2 (degree/incidence criterion)

Assume the good-load bounds

\[
 c_0N_T(i)\le\sum_{x\in T_i}Y_x(i)\le C_0N_T(i)
\tag{6.9}
\]

and the literal private-degree comparison

\[
                         c_1n_T(A)\le s_T(A)\le C_1n_T(A)
\tag{DEG}
\]

for every positive-weight row.  Under (6.5),

\[
                         \alpha_i^{\rm tr}\asymp\beta_T(i).
\tag{6.10}
\]

Consequently,

\[
 \frac{X_i(1-a_i)\beta_T(i)}
      {\alpha_i^{\rm tr}}
                         =\Theta(1).
\tag{6.11}
\]

#### Proof

Compare (6.7) and (6.8) using (6.9) and (DEG), then apply (1.4).
\(\square\)

For the complete unstopped owner-tail order fibre, (DEG) is structural:
each length-\(d+O(1)\) track has \(d-O(1)\) adjacent private switches.
The two-block lower holonomy has the same order of available adjacent
positions.  But the stopped live fibre need not retain those mates.

### Counterexample 6.3 (live-degree collapse)

Keep positive-weight live rows with \(n_T(A)>0\), but let every private
mate already be unavailable.  Then

\[
                         \beta_T(i)>0,
\qquad
                         s_T(A)=0,
\qquad
                         \alpha_i^{\rm tr}=0.
\tag{6.12}
\]

The resource good-load bounds constrain the incidence totals, not the
number of live switch mates, so they do not exclude this configuration.
Thus (DEG), or a weighted replacement of it, is a genuine stopped-fibre
condition.

Even (6.10) is only a trace comparison.  Capacity faithfulness needs the
stronger positive-operator domination

\[
 \boxed{
 L_{i,\partial}^{\rm sw}
 \le C\beta_T(i)L_T,}
\tag{CAP}
\]

or its normalized equivalent.  A trace bound does not imply (CAP): the
same total conductance can be concentrated on one Johnson star.  Hence
the exact coefficient theorem must supply both the scalar comparison and
the edge/operator aperture.

## 7. The exact missing normalization theorem

The required statement is a coefficient-faithful private-switch
realization:

\[
\boxed{
\begin{aligned}
 &K_T^*\Lambda_iK_T=L_{T,i}^{0},\\
 &K_T^*\Lambda_{i,\partial}K_T=A_{T,i},\\
 &0\le\Lambda_{i,\partial}\le\Lambda_i,\\
 &w_i(A,\tau A)
   =\text{the literal Duhamel/Bellman switch coefficient after the}\\
 &\hspace{35mm}\text{single declared external scalar is removed.}
\end{aligned}}
\tag{NORM}
\]

Here \(L_{T,i}^{0}\) is the pristine operator actually used in the
Gramian and \(A_{T,i}\) is its actual stopped deletion.  Under (NORM),

\[
                         0\le A_{T,i}\le L_{T,i}^{0}
\tag{7.1}
\]

is immediate, so capacity faithfulness is no longer an assumption.

If

\[
                         L_{T,i}^{0}=\alpha_iL_T,
\tag{7.2}
\]

the simultaneous normalization

\[
 (L_{T,i}^{0},B_{T,i}^{0},X_i)
 \longmapsto
 \left(L_T,\frac{B_{T,i}^{0}}{\alpha_i},
             \frac{X_i}{\alpha_i}\right)
\tag{7.3}
\]

leaves both \(P_i=I-L_{T,i}^{0}/X_i\) and
\(B_{T,i}^{0}/X_i\) unchanged.  Its effective service parameter is

\[
                         \overline\lambda_i
 =\frac{X_i(1-a_i)}{\alpha_i}.
\tag{7.4}
\]

If an external scalar \(\zeta_i\) was removed before defining the switch
operator, replace \(\alpha_i\) in (7.4) by
\(\alpha_i/\zeta_i\).  The exact uniform service condition is then

\[
\boxed{
 0<c\le
 \frac{X_i(1-a_i)\zeta_i}{\alpha_i}
 \le C.}
\tag{7.5}
\]

Equation (1.4) shows that this is equivalent to

\[
                         \alpha_i/\zeta_i=\Theta(1).
\tag{7.6}
\]

No current theorem proves (7.6), because \(\zeta_i\) and the conductances
in \(\Lambda_i\) have not been identified.  If (NORM) defines
\(\zeta_i=\alpha_i\), then (7.5) reduces immediately to (1.4) and the
capacity row closes.

## 8. Exact proof boundary

The analytic status is therefore:

1. the physical service scalar is already \(2+o(1)\);
2. full-row blocker conjugation closes the transported energy for every
   full conjugate switch, including the two-block lower holonomy and
   orbit-summed marked families;
3. the remaining capacity statement cannot be proved from the current
   symbols because the private-switch conductance scale is free.

The next proof must write (NORM) from the actual Bellman/Duhamel expansion.
It is not another concentration theorem, spectral estimate, or
large-cluster ledger.
