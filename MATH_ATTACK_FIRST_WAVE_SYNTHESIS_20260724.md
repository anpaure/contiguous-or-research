# First-wave audited synthesis (A--J)

Let
\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor ,
\]
and \(H_A=\lceil A\sqrt m\rceil\) for fixed \(A\).

## Shared exact calculus

Uniformly for \(q\le H_A\),
\[
\log\frac{W}{N_q}=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]
so the capacities \(c_q\) are bounded in every fixed Gaussian window.
Writing \(W=c_qN_q+r_q\), define
\[
Q_q(F)=\sum_S
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]
Then
\[
Q_q\ge2O_q,\qquad
M_q\le\frac{O_q}{c_q}.
\]

For every fixed \(A\), the existence of exact factors with
\[
\sum_{q\le H_A}\frac{O_q}{c_q}=o(W)
\]
is equivalent by diagonalization to MWB on some growing window
\(H=\sqrt m\,\omega(m)\), \(\omega(m)\to\infty\).  The labelled
common-owner statement is strictly stronger and only sufficient.

## Exact implication structure

\[
\begin{array}{c}
\text{fair component heat}\\
\Downarrow\\
\text{signed component heat}\\
\Downarrow\\
\text{positive-cut/local-minimum lemma}\\
\Downarrow\\
\text{fixed-window overload}\\
\Downarrow\\
\text{MWB}\\
\Downarrow\\
\text{literal wreath word plus product tails}\\
\Downarrow\\
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\end{array}
\]

Separately,
\[
\text{adaptive adjacent-deletion orientations}
\Longrightarrow
\text{labelled synchronization}
\Longrightarrow
\text{fixed-window overload}.
\]
There is no proved reverse implication from overload to labelled
synchronization.

Three direct routes bypass MWB:

1. the compact balanced three-box theorem;
2. the compact balanced four-box theorem;
3. the corrected rotor path-forest theorem for one full SCD.

## Unconditional advances

### Exact-factor algebra and heat

The rectangle/octahedral moves generate the full signed lattice
\(\ker_{\mathbb Z}U_r\), and coefficient-one selectors make the common
lower-rank signed map onto.  This removes signed index and congruence
obstructions only; it supplies no positivity, packing support, quota, or
nesting theorem.

For a transposition and ownership-component effects \(\Delta_K\), put
\[
A=\left\|\sum_K\Delta_K\right\|_A^2,\qquad
R(\varepsilon)=\left\|\sum_K\varepsilon_K\Delta_K\right\|_A^2 .
\]
The exact antipodal identity is
\[
\mathcal Q(F_\varepsilon)+\mathcal Q(F_{-\varepsilon})
=2\mathcal Q(F)+\frac{R(\varepsilon)-A}{2}.
\]
Thus legal descent is a weighted component Max-Cut problem.  Spectral
smoothing controls only the coherent displacement; the component
correlation term is the unresolved positive-fibre geometry.

### Rank-isolated labelled swaps

Swapping deletion positions \(q,q+1\) changes only depth \(q\).
The two choices per owner form a sparse multigraph \(G_q\).  A prescribed
indegree vector \(b\) is orientable exactly when
\[
e_G(U)\le b(U)\le e_G(U)+|\delta_G(U)|
\]
for every \(U\).  The minimum supported toggle cost satisfies
\[
O_q(F)\le\frac12\|b-\mu_q\|_1\le\tau_q(b).
\]
The graphs evolve with earlier ownerwise choices, so independent rankwise
orientations do not yield one nested resolution.

### Absorption

Every normalized rooted four-label window has exactly
\((m-1)!(m-2)!\) profile-3 balanced \(C_8\) partners.  One such switch has
fixed-window cost \(O_A(m)\).  Therefore \(o(\operatorname{Cat}_m)\) local
switches can change a fixed-window objective by only \(o(W)\): a sparse
absorber cannot repair a linear defect.  Its viable role is cleanup after a
positive-density rebundling or another coarse construction.

### Product boxes

For three boxes, the compact theorem is equivalent to the primitive ray
statement
\[
g_3(at,bt,ct)=w(at,bt,ct)+o(t^2)
\]
for every primitive positive triple.  Existing random, intact-side,
short-run, and additive-slab architectures pay critical quadratic loss.

For four boxes, the uniform compact statement
\[
g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell)=o(R^3),
\qquad \ell_i\asymp R,
\]
implies coefficient one.  The proved lower bounds obstruct only reset-based
fixed-line architectures, not arbitrary surface braids.

### Rotor/SCD

For one full SCD \(\mathcal D\), define
\[
\Phi_{\min}(\mathcal D)
=\min\sum_{d\le H}(2d+1)p_d
\]
over spanning directed vertex-disjoint rotor path forests in its clipped
radius classes.  Exact orbit coloring and Euler routing give total toll at
most \(Q\Phi_{\min}\), with all resets charged.  Hence
\(\Phi_{\min}=o(W)\) is sufficient.  The canonical BTK/GK SCD has an empty
positive-radius rotor graph and fails at order \(W\sqrt m\).

## Five distinct remaining lemmas

1. Positive-cut/local-minimum lemma: every transposition-cut local minimum
   above \(C_AH_A\operatorname{Cat}_m\) admits a positive component cut.

2. Adaptive owner-orientation lemma: the evolving graphs
   \(G_1,\ldots,G_{H_A}\) admit balanced Hall-feasible orientations with
   total weighted toggle cost \(o(W)\).

3. Primitive three-box ray theorem:
   \(g_3(at,bt,ct)=w(at,bt,ct)+o(t^2)\).

4. Compact four-box theorem:
   \(g_4(\boldsymbol\ell)=w_4(\boldsymbol\ell)+o(R^3)\) uniformly on compact
   balanced aspect-ratio sectors.

5. Corrected rotor path-forest theorem:
   full SCDs exist with \(\Phi_{\min}=o(W)\) in every fixed window.

The first lemma is closest only in implication distance: it is qualitative,
support-feasible, and finite descent completes the argument.  No audited
lane currently has quantitative evidence that its missing lemma is true.
