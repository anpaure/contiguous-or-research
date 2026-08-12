# No scalar all-order profile energy: the consecutive-spine obstruction

Date: 2026-07-27

Scope: the attempted boundary-free absorption of
PFS$_3\to$PFS$_4\to\cdots$ in the vertex-induced promotion-frame
process.

## 0. Verdict

Let $E_k$ be a nonnegative order-$k$ profile energy and suppose its
positive predictable-variation boundary is paid by one child level,

\[
                         \dot E_k^+\le c_kE_{k+1}.         \tag{0.1}
\]

For the exact consecutive profile spine, the aggregate child kernel has
two regimes:

\[
                         c_k=\Theta(1/m),\qquad k<H,       \tag{0.2}
\]

but

\[
                         \boxed{c_k=\Theta(1),\qquad H\le k<m.}
                                                                    \tag{0.3}
\]

Thus the first physical order at which the kernel ceases to contract is

\[
                         \boxed{k=H=\Theta(\sqrt{m\log m}).} \tag{0.4}
\]

This is not the earlier polynomial-envelope threshold
$k\asymp (mu)^{1/4}$.  That threshold comes from the loose $k^4$
endpoint count.  The exact spine shows that the true low-order
contraction persists to $H$, and also shows that it genuinely disappears
there.

Let

\[
                         \Phi(t)=\sum_{k=2}^{m}a_kE_k(t),
                         \qquad a_k>0.                      \tag{0.5}
\]

If the time-integrated upward branching of every level is required to
be at most a fixed $\rho<1$, then necessarily

\[
                         T_*c_k{a_k\over a_{k+1}}\le\rho. \tag{0.6}
\]

On the requested interval

\[
 z_*=m^{-1/2}(\log m)^B,qquad
 T_*=r\log(1/z_*)=(1/2+o(1))m\log m,                       \tag{0.7}
\]

equations (0.3) and (0.6) force

\[
                         a_{k+1}\ge cT_*a_k
                         \qquad(H\le k<m).                 \tag{0.8}
\]

The actual time-zero catalogue contains a consecutive spine through all
these orders.  Its terminal normalized mass is

\[
                         \Gamma_m=exp[-m\log m+O(m)].      \tag{0.9}
\]

Consequently

\[
 \log(a_m\Gamma_m)
 \ge (1+o(1))m\log\log m+log a_H,                         \tag{0.10}
\]

and the initial weighted energy diverges whenever $a_H$ is normalized
at any subexponentially small scale.  The low-order absorption
inequalities themselves force $a_H\ge a_2\exp[\Omega(H\log\log m)]$,
so choosing $a_H$ tiny is not compatible with retaining the pair/triple
energies.

Therefore:

\[
 \boxed{
 \begin{array}{c}
 \text{No positive scalar weight sequence }(a_k)\text{ can both}\\
 \text{absorb every }+1\text{ profile shift over }T_*
 \text{ and have a finite initialized spine norm.}
 \end{array}}                                             \tag{0.11}
\]

This is a real physical-catalogue obstruction, not an arbitrary
edge-deletion residual.  It is already present at time zero, hence in
the genuine vertex-induced process.

It does **not** prove that PFS$_3$ itself has nonnegligible stopped
incidence.  It proves that the requested all-order one-index weighted
energy cannot establish the contrary.  A successful proof must exploit
one of:

1. compensation which removes the $+1$ shift so the positive remainder
   starts at $+2$;
2. a multidimensional energy retaining the two-shore/gap geometry past
   $H$; or
3. a direct trajectory theorem for PFS$_3$ which never propagates a
   scalar profile through the post-$H$ spine.

## 1. Exact consecutive profile masses

Let $\Gamma_k$ be the normalized number of catalogue frames through a
fixed owner and $k$ further consecutive profile resources.  The exact
rooted frame formulas are

\[
 \Gamma_k
 ={2(r-k)\over r}
 \left({(m-k)!\over m!}\right)^2,
 \qquad 1\le k\le H,                                     \tag{1.1}
\]

and

\[
 \Gamma_k
 ={2(r-k)(m-k)!(m-H)!\over r(m!)^2},
 \qquad H\le k\le m.                                    \tag{1.2}
\]

These are literal physical profiles in the initial catalogue.  No
formal envelope or marginal product is involved.

For one prescribed continuation,

\[
 {\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over(m-k)^2},
 \qquad k<H,                                             \tag{1.3}
\]

whereas

\[
 {\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over m-k},
 \qquad H\le k<m.                                       \tag{1.4}
\]

At profile order $k$ there are $m-k$ admissible next coordinate
continuations.  Summing the prescribed-child ratios gives the aggregate
kernel

\[
 \begin{aligned}
 c_k^{\rm spine}
 &:=(m-k){\Gamma_{k+1}\over\Gamma_k}\\
 &= {r-k-1\over r-k}{1\over m-k},&&k<H,\\
 &= {r-k-1\over r-k},&&H\le k<m.
 \end{aligned}                                           \tag{1.5}
\]

Since $r=m+H+O(1)$, (1.5) proves (0.2)--(0.4).  In particular,
$c_k^{\rm spine}\ge1/3$ throughout
$H\le k\le m-1$ for all sufficiently large $m$.

## 2. Necessary weight recurrence

Multiply (0.1) by $a_k$ and sum.  The contribution entering the
$a_{k+1}E_{k+1}$ coefficient from level $k$ over a time interval of
length $T_*$ is

\[
                         T_*c_k{a_k\over a_{k+1}}.         \tag{2.1}
\]

Thus any positive-kernel argument whose total incoming branching is at
most $\rho<1$ must satisfy (0.6).  By (1.5), for
$H\le k<m$,

\[
                         a_{k+1}\ge {T_*\over3\rho}a_k.    \tag{2.2}
\]

Iteration yields

\[
                         a_m
 \ge a_H\left({T_*\over3\rho}\right)^{m-H}.              \tag{2.3}
\]

This argument allows arbitrary $m$-dependent weights.  It is not
restricted to powers of factorials.

For comparison, in the low-order regime (1.5) and (0.6) give

\[
                         a_{k+1}
 \ge {cT_*\over m-k}a_k.                                  \tag{2.4}
\]

For $k\le H$ the right side is
$(c+o(1))\log m\,a_k$, so even the pre-$H$ recurrence makes the weights
grow rather than permitting an exponentially small $a_H$.

The tempting choice $a_k=(k!)^4$ cancels the loose polynomial $k^4$
factor in the local endpoint envelope, but (2.2) is stronger after the
spine transition and is unaffected by that cancellation.

## 3. Initialization on the physical spine

At the terminal universally available order $m$ (or $m-1$ if the
chosen convention omits the final zero-length continuation), Stirling
applied to (1.2) gives

\[
                         \log\Gamma_m=-m\log m+O(m).       \tag{3.1}
\]

Combining (2.3), (3.1), and
$\log T_* =\log m+\log\log m+O(1)$ gives

\[
 \begin{aligned}
 \log(a_m\Gamma_m)
 &\ge\log a_H+(m-H)\log(T_*/(3\rho))
       -m\log m+O(m)\\
 &=\log a_H+(1+o(1))m\log\log m.                          \tag{3.2}
 \end{aligned}
\]

Equation (2.4) gives

\[
                         \log(a_H/a_2)
                         \ge\Omega(H\log\log m),          \tag{3.3}
\]

so a normalization with $a_2=1$ makes the right side of (3.2) diverge
even faster.  Conversely, forcing $a_m\Gamma_m=O(1)$ would require

\[
                         a_H\le\exp[-(1-o(1))m\log\log m],\tag{3.4}
\]

which contradicts (3.3) and removes the pair/triple levels the energy
was meant to control.

This proves (0.11).

## 4. Interpretation for the stopped hierarchy

The conditional result
`MATH_THEOREM_PAIR_PROFILE_STOP_UNDER_TRIPLE_FIBRE_AND_NEXT_BOUNDARY_20260727.md`
uses the order-three profile only to control pair-link jumps and theta
quadratic variation.  Iterating that argument one order at a time would
create the $+1$ chain (0.1).  The preceding theorem shows that summing
that chain in a scalar all-order norm cannot eliminate its boundary.

The obstruction occurs before any issue of random residual reachability:
the profiles (1.1)--(1.2) are present in the full initial catalogue.
Thus the next positive attack should not seek another scalar choice of
$a_k$; it must remove or geometrically split the post-$H$ unit kernel.
