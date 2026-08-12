# Independent audit: K10 positive multidepth orbit menu

Date: 2026-07-25

Audited file:
MATH_ATTACK_K10_POSITIVE_MULTIDEPTH_ORBIT_MENU_20260725.md.

Method: pure mathematics only. No web search, finite search, solver, or
computer experiment was used.

## Verdict

PASS after the corrections incorporated in the audited file.

The unconditional literal theorem is the laminar half-packet preparation.
The all-depth orbit-capacity theorem and its coherent packet allocation are
also unconditional. Their realization by a common sequence of freshly
recomputed complete-component cuts remains conditional on the explicit
component-monochromatic/TU lift. The report does not claim \(J_A=o(W)\) or
the constant-one theorem.

## 1. Laminar selector

For \(M=m-2\), the cylinders

\[
 \mathscr C(q,V)=\{UV:U\in\mathcal D_q\}
\]

are laminar. If \(q\le q'\) and \(UV=U'V'\), then \(U'=UA\),
\(V=AV'\), and the intervening word \(A\) is Dyck. Hence the first
cylinder is contained in the second.

For every selected subfamily of laminar rows, alternating signs by inclusion
depth gives column sums in \(\{-1,0,1\}\). The Ghouila--Houri criterion
therefore proves TU. The half-vector polytope has an integral vertex, giving

\[
 \left|x(\mathscr C(q,V))-\frac12C_q\right|\le\frac12
\]

simultaneously for all \(q\le H,V\), and

\[
 x(\mathcal D_M)\in
 \left\{\left\lfloor\frac{C_M}{2}\right\rfloor,
       \left\lceil\frac{C_M}{2}\right\rceil\right\}.
\]

The audited \(q>s\) marker identity certifies one tagged even-suffix dipole
per packet: its positive arm contains \(n\), while the other three arms omit
\(n\). Thus the common signing balances the tagged dipoles. It does not
balance the full private-pair total or exclude additional same-sign
occurrences.

The switched-row density is

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 \longrightarrow\frac1{16}.
\]

The piecewise root map is nontrivial on

\[
 (2n-4)x(\mathcal D_M)
 =\left(\frac1{16}+o(1)\right)W
\]

middle roots. Finally,

\[
 \sum_{q\le H}C_qC_{m-q-2}\le C_{m-1},
\]

so both complementary tagged ledgers have total \(o(W)\).

## 2. All-depth orbit capacity

For \(s=\lceil3H/4\rceil\), the common coordinate block has

\[
 a=s+2,\qquad u=2s+2H+5.
\]

At depth \(q\),

\[
 |\mathcal B_q|=2(H-q).
\]

Fixing the trace outside \(\mathcal U\cup E_s\) and the
\(\mathcal B_q\)-occupancy \(k\), at most

\[
 \binom{2(H-q)}k
\]

Dyck indices share the orbit. The orbit has exactly

\[
 2\binom u{a+k}
\]

targets. Vandermonde gives

\[
 \binom u{a+k}\ge
 \binom{2s+2q+5}{s+2}\binom{2(H-q)}k.
\]

With \(\alpha=s/H\) and \(x=q/H\), the entropy exponent after removing
\(q\log4\) is

\[
 f_\alpha(x)=
 (2\alpha+2x)\log(2\alpha+2x)
 -\alpha\log\alpha-(\alpha+2x)\log(\alpha+2x)-x\log4.
\]

It decreases in \(x\) and increases in \(\alpha\). Its minimum is

\[
 \delta_0=f_{3/4}(1)>0.
\]

The binomial prefactor costs only \(O(\log H)\), so the uniform
\(\exp(\delta_0H/2)4^q\) bound is valid for large \(m\).

The coherent allocation is not inferred from independent rankwise
matchings. When packets are assigned greedily, each tag forbids at most
\(\frac12e^{-\delta_0H/2}\) of \(G\); a packet has at most \(2H\) lower and
upper tags. The union bound is below one. Hence one group element per packet
works at every depth.

The result concerns certified tags. It proves pointwise quota-capacity
extendability and no tagged self-collision, not balance of the complete
unlabelled factor histogram.

## 3. Spectral seam normalization

For the selected root set \(\mathcal E\), let

\[
 p=\frac{|\mathcal E|}{W}\longrightarrow\frac1{16}.
\]

Every selected two-wreath cell is a \(1\)-design. The first nonzero Johnson
harmonic available to its centered indicator has Laplacian eigenvalue
\(2(n-1)\), giving

\[
 |\partial\mathcal E|\ge2(n-1)Wp(1-p).
\]

There are four \((2\ 3)\)-fixed roots per selected packet. Deleting all
boundary edges incident with them costs at most

\[
 4k\,m(m+1)=\frac{pW(n^2-1)}{2n}.
\]

At \(p=1/16+o(1)\), the residual is

\[
 \left(\frac{11}{128}-o(1)\right)nW.
\]

Every residual boundary edge is a genuine loopless commutator seam. The
odd complete coordinate graph decomposes into \(n\) near-perfect matchings,
so one matching of colours carries

\[
 \left(\frac{11}{128}-o(1)\right)W
\]

seams. These are separate fresh overlays at one prepared factor; sequential
persistence and distinct-component dispersion are not asserted.

The carrier forest is a linear forest and extends to a Hamilton path.
Union with the seam-colour matching has at most \(3m\) edges, maximum degree
three, and generates \(S_n\).

## 4. Literal lift and charged TU theorem

The longest-word subword construction on the path through \(\mathcal U\)
correctly supplies one common \(O(H^2)\)-stage word representing every
packet permutation by apply/skip bits. If each freshly recomputed ownership
component is monochromatic in the prescribed bits, whole-component cuts
realize all routes. Components containing no routed row are retained.

For the charged theorem, the retained TU signing gives a
\(c_q/c_q+1\) vector with

\[
 g_q=\rho_q-M_q+c_qu_q
\]

ceilings. If a global quota puts \(h\) ceilings on the invariant bad set,
the retained half-\(\ell^1\) cost is

\[
 \frac12|M_q-c_qu_q-h|,
\]

and the bad-set cost is at most

\[
 \frac12(M_q+c_qu_q+h).
\]

Thus

\[
 O_q\le
 \min_{h\in I_q\cap\mathbb Z}
 \frac{M_q+c_qu_q+h+|M_q-c_qu_q-h|}{2}
 \le M_q+(c_q+1)u_q.
\]

There is no missing factor of two and no hidden fractional relaxation.

## 5. Final scope

The report proves:

1. an actual positive-density integral multidepth component rebundling;
2. an explicit \(O(H)\)-colour tree escaping the divergent tagged private
   cage simultaneously at all depths;
3. a coherent integral packet-level orbit allocation;
4. a connected degree-three \(S_n\)-menu with a linear genuine-seam
   reservoir; and
5. an exact charged near-TU component signing theorem.

It leaves one physical gate: prove component-bit coherence, or the augmented
near-TU property with a weighted \(o(W)\) actual bad-target residue, for one
fresh overlay or recomputed menu path.
