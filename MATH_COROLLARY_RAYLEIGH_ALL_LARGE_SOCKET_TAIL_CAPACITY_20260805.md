# Every Rayleigh large-socket tail-capacity cut has uniform slack

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or search  
**Status:** unconditional corollary of the independently audited all-mesh
arithmetic-comb theorem.  It closes the complete one-threshold family of
configuration cuts which says that a job of size `x` can contain at most
`ceil(x/t)-1` sockets strictly larger than `t`.  This family is necessary,
but is not by itself the full increasing-subadditive/all-price cone.

## 1. Rayleigh notation

Put

\[
             A={\sqrt\pi\over2},\qquad p=e^{-A^2}=e^{-\pi/4},
\tag{1.1}
\]

and let

\[
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A.
 \end{cases}
\tag{1.2}
\]

For `t>0`, write

\[
                         C(t)=\sum_{n\ge0}K(nt).
\tag{1.3}
\]

The centered-phase theorem proves, for `0<t<=A`,

\[
 C(t)=\mathbb E\left\{{R-(A\bmod t)\over t}\right\}-p,
\tag{1.4}
\]

where `R` is Rayleigh with density `2r e^(-r^2)`, together with the
uniform estimate

\[
 \mathbb E\left\{{R-(A\bmod t)\over t}\right\}
 \le {1\over2}+{35\over864}={467\over864}.
\tag{1.5}
\]

The same theorem uses the rational Gaussian bound

\[
                         p<{57\over125}.
\tag{1.6}
\]

Consequently

\[
 \boxed{
 K(0)-C(t)>
 1-{57\over125}-{467\over864}
 ={377\over108000}=:c_* .}
\tag{1.7}
\]

## 2. The complete tail-capacity family

Let the socket and job measures be

\[
 \nu(dy)=2(A-y)e^{-(A-y)^2}{\bf1}_{(0,A)}(y)\,dy,
\tag{2.1}
\]

\[
 \mu(dx)=2(A+x)e^{-(A+x)^2}{\bf1}_{(0,\infty)}(x)\,dx.
\tag{2.2}
\]

For a threshold `0<t<A`, any finite configuration of sockets summing to a
job of size `x` contains at most

\[
                         \left\lceil{x\over t}\right\rceil-1
\tag{2.3}
\]

sockets strictly larger than `t`.  Therefore every coagulation must obey

\[
 \nu((t,A))\le
 \int\left(\left\lceil{x\over t}\right\rceil-1\right)d\mu(x).
\tag{2.4}
\]

### Theorem 2.1 (uniform strict tail capacity)

For every `0<t<A`, inequality (2.4) holds with slack greater than `c_*`:

\[
 \boxed{
 \sum_{n\ge1}e^{-(A+nt)^2}
 -\left(1-e^{-(A-t)^2}\right)
 > {377\over108000}.}
\tag{2.5}
\]

### Proof

The socket tail is

\[
                         \nu((t,A))=1-e^{-(A-t)^2}.
\tag{2.6}
\]

Layer cake for the integer variable in (2.3) gives

\[
 \int\left(\left\lceil{x\over t}\right\rceil-1\right)d\mu(x)
 =\sum_{n\ge1}\mu((nt,\infty))
 =\sum_{n\ge1}e^{-(A+nt)^2}.
\tag{2.7}
\]

Put `q=floor(A/t)>=1` and abbreviate

\[
 L_n=e^{-(A-nt)^2}\quad(0\le n\le q),
 \qquad R_n=e^{-(A+nt)^2}\quad(n\ge0).
\tag{2.8}
\]

Expanding (1.3) at the last lattice point not exceeding `A` gives

\[
 C(t)=q+1-\sum_{n=0}^{q}L_n-\sum_{n=0}^{\infty}R_n.
\tag{2.9}
\]

Since `L_0=R_0=p`, rearrangement yields the exact identity

\[
 \begin{aligned}
 &\sum_{n\ge1}R_n-(1-L_1)\\
 &\qquad=q-2p-\sum_{n=2}^{q}L_n-C(t).
 \end{aligned}
\tag{2.10}
\]

The sum in (2.10) is empty when `q=1`.  Since every `L_n<=1`,

\[
 q-\sum_{n=2}^{q}L_n\ge1.
\tag{2.11}
\]

Thus the left side of (2.10) is at least

\[
                         1-2p-C(t)=K(0)-C(t),
\tag{2.12}
\]

which is greater than `c_*` by (1.7).  This proves (2.5). `square`

## 3. Exact scope

The theorem rules out every separator which prices only the number of
sockets above one threshold.  Equivalently, the Rayleigh pair has uniform
slack against all cuts obtained from the pointwise capacity
`#\{pieces>t\}<=ceil(x/t)-1`.

These cuts do not characterize finite coagulation.  Intersections of
several threshold constraints and genuinely nonarithmetic covering prices
remain possible separators.  Therefore this corollary strengthens the
all-price evidence but does not prove the Rayleigh coagulation theorem or
`nu(k)<=B(k)+O(1)`.

## 4. Dependencies

1. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`;
2. `MATH_AUDIT_RAYLEIGH_ARITHMETIC_COMB_AND_GLOBAL_APERY_TUBE_INDEPENDENT_20260805.md`;
3. `MATH_THEOREM_ATOMLESS_COMPACT_COAGULATION_COUNTEREXAMPLE_AND_EXACT_DUAL_20260805.md`.
