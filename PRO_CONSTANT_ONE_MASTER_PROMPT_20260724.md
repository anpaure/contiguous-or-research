# Prompt for Pro instances: prove the constant-one upper bound

You are working on the following extremal contiguous-OR problem.

For a positive integer \(k\), let \(\nu(k)\) be the minimum length of a word

\[
A_1,A_2,\ldots,A_n\in 2^{[k]}\setminus\{\varnothing\}
\]

such that every nonempty \(S\subseteq[k]\) is the union of some nonempty
contiguous interval:

\[
S=A_\ell\cup A_{\ell+1}\cup\cdots\cup A_r.
\]

Put

\[
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

The present unconditional asymptotic bracket is

\[
(1+o(1))W(k)\le \nu(k)\le(\sqrt2+o(1))W(k).
\]

The objective is to prove

\[
\boxed{\nu(k)\le(1+o(1))W(k)}.
\]

Do not merely restate this reduction or provide a research plan. Produce a
proof of the missing theorem below, a rigorous counterexample to one of its
premises, or a theorem-level partial result that strictly reduces the missing
gate. Clearly separate proved claims from conjectures.

## 1. The clean exact-factor sufficient theorem

Work first in odd dimension

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
B=W/n=\operatorname{Cat}_m.
\]

For a cyclic order \(\pi=(x_0,\ldots,x_{n-1})\), write

\[
I_\pi(j,r)=\{x_j,x_{j+1},\ldots,x_{j+r-1}\},
\qquad j\in\mathbb Z_n.
\]

The Mütze–Standke–Wiechert \(C_{2m+1}\)-factor theorem for the odd
graph supplies an exact factor

\[
\mathcal F=\{\pi_1,\ldots,\pi_B\}
\]

whose \(nB=W\) length-\(m\) cyclic intervals partition
\(\binom{[n]}m\). Thus the middle layer is already solved integrally. A
shortest odd-graph cycle is the same object as one such cyclic-interval
wreath; include this elementary conversion if you invoke the theorem.

For depth \(q\), define

\[
\mathcal C_q(\pi)=\{I_\pi(j,m-q):j\in\mathbb Z_n\},
\qquad
N_q=\binom n{m-q},
\]

and the lower-shadow defect

\[
M_q(\mathcal F)
=N_q-\left|\bigcup_{\pi\in\mathcal F}\mathcal C_q(\pi)\right|.
\]

Define the upper family analogously using intervals of length \(m+1+q\).
Its defect is exactly the same \(M_q(\mathcal F)\), because cyclic
complementation bijects the two families.

### Exact global-sharing transfer inequality

For every exact middle wreath factor and every \(1\le H<m\), there is a
literal nonzero contiguous-OR word with

\[
\boxed{
\nu(2m+1)\le
W+\frac{2H+1}{2m+1}W
+2\sum_{q=1}^{H}M_q(\mathcal F)
+2\sum_{r=0}^{m-H-1}\binom{2m+1}{r}-1.}
\tag{WT}
\]

For each wreath, emit the \(n\) entries

\[
E_j=I_\pi(j,m-H)
\]

followed by \(E_0,\ldots,E_{2H}\). For \(1\le t\le2H+2\), the union of
\(t\) consecutive entries is literally

\[
I_\pi(j,m-H+t-1).
\]

Append each missing band mask and then both literal tails. This proof is
already an actual OR word: linked bands, factorization, contamination, lower
cores, and coordinate pins are not separate obligations.

### Weak vertical wreath lemma

Construct exact middle wreath factors \(\mathcal F_m\) and choose, for any
fixed \(\varepsilon>0\),

\[
H=\left\lceil(1/2+\varepsilon)
\sqrt{(2m+1)\log(2m+1)}\right\rceil
\]

such that

\[
\boxed{\sum_{q=1}^{H}M_q(\mathcal F_m)=o(W).}
\tag{WV}
\]

This lemma is sufficient by (WT): \(HW/n=o(W)\), and a Chernoff bound gives

\[
\frac{2^n\exp(-2H^2/n)}{W}=o(1).
\]

The standard one-bit trimmed lift transfers the result to even dimensions.
Therefore a proof of (WV) proves the objective with no later factor-labeling
or pin-survival theorem.

### Current weakest isolated cyclic gate: shallow central traces

The full depth in (WV) is no longer necessary.  Fix

\[
\gamma(m)\to\infty,\qquad \gamma(m)=o(\log\log m),
\]

and put

\[
h=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil.
\]

An `o(W)`-length reservoir of independent cyclic orders covers every deeper
rank through the tail threshold.  Thus only depths `q<=h` need structured
control.

The strongest audited form uses one all-depth singleton block per auxiliary
cyclic order.  If `F` is an exact middle factor and `T>=1`, then

\[
\nu(2m+1)\le W+(2h+1)W/n+2\sum_{q=1}^hM_q(F)
 +(2n-2)T
 +2\sum_{q=h+1}^{m-1}N_q(1-n/N_q)^T.
\tag{AS}
\]

Take `T=ceil((W/n)/a_m)`, where `a_m->infinity` and
`log a_m=o(log log m)`, and let `h` be the least depth with
`W/N_h>=3a_m log m`.  Then

\[
h=(1+o(1))\sqrt{m\log\log m},
\]

and every term in (AS) beyond the exact-factor shallow defect is `o(W)`.
There is no condition on the exact factor beyond this depth.

There is a further trace-compression weakening.  Let `P_m` be a multiset of
`p_m` cyclic orders, let `H_q(P_m)` be its depth-`q` lower holes (including
`q=0`), and choose one marked set `Z_m` of size `t_m`, where

\[
t_m\to\infty,\qquad t_m=o(m).
\]

Choose `a_m<t_m/2` with

\[
2^{-t_m}\sum_{j=0}^{a_m}\binom{t_m}{j}=o(1),
\]

and define the balanced-trace defect

\[
G_m=\sum_{q=0}^{h}
\#\{S\in H_q(P_m):a_m<|S\cap Z_m|<t_m-a_m\}.
\]

There is an even weaker cutoff-free form.  If `c_R` is the number of
shallow holes with marked trace `R`, pair complementary traces
`Pi={R,Z_m minus R}` and put

\[
\Phi_m=\sum_{\Pi}
\min\{c_R+c_{Z_m\setminus R},\ \nu(n-t_m)+1\}.
\]

Then the following target is sufficient:

\[
\boxed{p_m(2m+1)=W+o(W),\qquad \Phi_m=o(W).}
\tag{SCT}
\]

Indeed, one universal word on the unmarked coordinates, lifted once for
each extreme marked trace, repairs all depths sharing that trace; only the
balanced-trace holes are appended literally.  One may take

\[
a_m=t_m/2-b_m,qquad \sqrt{t_m}\ll b_m=o(t_m),
\]

so only a narrow near-balanced trace window is charged.  Exact middle
ownership is optional.  Proving (SCT) proves coefficient one after the
reservoir and literal tails, with no later pinning theorem.

The easier condition `G_m=o(W)` implies (SCT): buy trace blocks for the two
extreme tails and append only the balanced holes.  The functional `Phi_m`
chooses optimally, trace pair by trace pair, between two shared trace blocks
and literal complementary repairs.

### Stronger exact resolution, if useful

Let \(\Omega=\{(\pi,j):\pi\in\mathcal F,j\in\mathbb Z_n\}\). An exact
cyclic-interval SCD resolution would be nested sets

\[
\Omega=A_0\supseteq A_1\supseteq\cdots\supseteq A_m,
\qquad |A_q|=\binom n{m-q},
\]

such that both maps

\[
(\pi,j)\mapsto I_\pi(j,m-q),\qquad
(\pi,j)\mapsto I_\pi(j,m+1+q)
\]

are bijections on \(A_q\). This would prove (WV), but it is strictly
stronger than needed: (WV) asks only near-surjectivity of the full shadow
maps through growing depth.

## 2. The exact collision ledger

Order the wreaths as \(\pi_1,\ldots,\pi_B\). Let

\[
U_{i,q}=\bigcup_{t\le i}\mathcal C_q(\pi_t),
\qquad
o_{i,q}=|\mathcal C_q(\pi_i)\cap U_{i-1,q}|.
\]

Then exactly

\[
\boxed{
M_q(\mathcal F)=\sum_{i=1}^{B}o_{i,q}-(W-N_q).
}
\tag{CL}
\]

The term \(W-N_q\) is unavoidable overlap and is not an error. Thus (WV) is
equivalent to

\[
\sum_{q=1}^{H}
\left(\sum_i o_{i,q}-(W-N_q)\right)=o(W).
\]

At the first shadow,

\[
N_1/W=m/(m+2),\qquad W-N_1=2W/(m+2).
\]

Even proving \(M_1(\mathcal F_m)=o(W)\) for a flexible family of exact
wreath factors would be a substantive first theorem, though not all depths.

### Strictly weaker near-factor target

Exact middle ownership is not required by the OR construction.  For any
multiset \(\mathcal P\) of \(p\) cyclic orders, let \(M_q(\mathcal P)\)
count the missing length-\(m-q\) masks, including \(q=0\).  The same literal
erosion blocks give

\[
\boxed{
\nu(2m+1)\le p(n+2H+1)
 +2\sum_{q=0}^{H}M_q(\mathcal P)
 +2\sum_{r=0}^{m-H-1}\binom nr-1.}
\tag{RWT}
\]

Consequently the still weaker integral target

\[
pn=W+o(W),\qquad \sum_{q=0}^{H}M_q(\mathcal P)=o(W)
\tag{RNF}
\]

also proves coefficient one.  It permits \(o(W)\) repeated and missing
middle masks and \(o(B)\) excess cyclic blocks.  If exact factor fibres are
too rigid, prove (RNF), not a needlessly exact replacement theorem.

### Fractional feasibility is completely settled

For every oriented cyclic order modulo rotation, the uniform weight

\[
x_\pi=\frac1{m!(m+1)!}
\]

gives each middle mask load one and each rank-\(r\) cyclic-interval target
load \(\binom nm/\binom nr\ge1\), simultaneously at all depths.  With
survival probabilities

\[
R_q=\binom n{m-q}/W,\qquad p_d=R_d-R_{d+1},
\]

it even gives an exact nested fractional cyclic-interval SCD.  This uniform
point lies in the convex hull of genuine exact middle factors: orient any
MSW factor and average its coordinate relabelings.  Therefore no ordinary
LP dual, nesting constraint, rank quota, or divisibility count can settle
the gate.  Holes are the nonlinear integral/Jensen gap.

For an exact factor the forced collision floor through
\(H/\sqrt m\to\infty\), \(H=o(m^{2/3})\), is

\[
\sum_{q=1}^{H}(W-N_q)
=W\left(H-\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m\right).
\]

Thus (WV) demands additive \(o(W)\) accuracy above a \(\Theta(WH)\)
unavoidable term, or relative uncovered mass \(o(m^{-1/2})\) across the
band.

### Exact legal-switch diagnostic

Overlay an exact factor \(F\) with a coordinate-transposed factor \(\tau F\).
Each interaction component may independently choose its left or right side.
For every component \(K\), the right incidence vector is exactly \(\tau\)
of its left incidence vector.  Hence every nonfixed target pair
\(\{S,\tau S\}\) is an exact not-all-equal clause on the component bits,
while \(\tau\)-fixed targets are immutable.  If \(h_p\) components carry a
pair, fair component switching has first-shadow drift

\[
\mathbb E\,[M(\mathrm{new})-M(F)]
=\sum_{p\text{ separated covered}}2^{1-h_p}
-\sum_{p\text{ hole--duplicate}}(1-2^{1-h_p}).
\tag{NAE}
\]

A useful switching proof must establish negative drift in (NAE), or solve
the simultaneous weighted Max-NAE instance through all depths.  Mean
smoothing alone is insufficient; a duplicate paired with a hole helps only
when its occurrences are split over at least two interaction components.

## 3. Valid alternative machinery: monotone-radius queue atoms

There is a second, stronger route which may be useful constructively.

On \(2m\) coordinates, take an injective queue and \(H\) consecutive
length-\(m\) windows. A genuine move-to-front OR word can expose at start
\(t\) a saturated symmetric chain of radius \(d_t\), provided

\[
d_0\ge d_1\ge\cdots\ge d_{H-1}.
\]

One such atom has literal word length \(H+2d_0+1\), and its exposed masks
are pairwise distinct. Factorability and coordinate pins are automatic.

The full coordinate/profile orbit has an exact fractional SCD cover. With

\[
W=\binom{2m}m,\qquad N_q=\binom{2m}{m-q},\qquad
\rho_q=N_q/W,
\]

the random integral monotone profile

\[
a_q=\lfloor H\rho_q+U\rfloor,\qquad
U\sim\operatorname{Unif}[0,1),
\]

has \(\mathbb E a_q=H\rho_q\). Total atom weight \(W/H\) covers every band
mask fractionally exactly once, with reset mass \(O(hW/H)=o(W)\).

For an integral atom family define, for each rank sign,

\[
T_q^\sigma=\sum_S\mu_q^\sigma(S),\quad
D_q^\sigma=\sum_S(\mu_q^\sigma(S)-1)_+,\quad
M_q^\sigma=\#\{S:\mu_q^\sigma(S)=0\}.
\]

The exact identity is

\[
M_q^\sigma=N_q+D_q^\sigma-T_q^\sigma.
\tag{DM}
\]

An approximate queue-compatible SCD with correct per-rank quotas and
\(\sum D_q=o(W)\) would prove the goal. However, this is stronger than
necessary. For OR coverage it suffices to construct \(W/H+o(W/H)\) atoms
with

\[
\boxed{\sum_{q,\sigma}M_q^\sigma=o(W),}
\tag{WQ}
\]

regardless of large nonmiddle duplicate counts. A fixed radius-\(h\) atom
already shares every shallower depth with the same physical updates;
monotone radii add exact SCD truncation, not cheaper weak OR coverage.

If you use the rotor route, target the weaker missing-only statement (WQ)
unless the near-SCD structure is essential to your proof.

### Two unconditional partial constructions already available

Do not return only another qualitative fixed-band result.

1. For every fixed `h,H`, dummy-completed monotone-profile queue atoms and
   Kahn's bounded-rank theorem give zero duplicates and only `o(W)` missing
   masks in the fixed band, with word length

   \[
   W+\frac{2h+1}{H}W+o_{h,H}(W).
   \]

   Diagonalization gives some unbounded band, but no quantitative depth.

   A quantitative sparsification plus the growing-uniformity ABKV matching
   theorem improves this to an explicit zero-collision queue band

   \[
   h=\sqrt{\frac{\log m}
    {\log\log m\,\omega(m)}},
   \qquad \omega(m)\to\infty,
   \]

   with word length `W+o(W)`.  Its natural ABKV matching ceiling is
   `h=o(sqrt(log m/log log m))`; it still does not approach the outer
   reservoir.  The Poisson proof can be made an ordinary simple hypergraph
   either by sampling distinct supports directly or by adding random label
   vertices and deleting the `poly(m)` old-vertex/label collisions.

   A cleaner fixed-radius queue orbit avoids both profiles and dummies.  For
   `d>=1`, `L>=2`,

   \[
   d/L\to0,\qquad K=(2d+1)L,\qquad K\log K=o(\log m),
   \]

   a simple atom matching has zero duplicates and only `o(W)` missing masks
   throughout ranks `m-d,...,m+d`; its completed literal word has length
   `W+(2d/L)W+o(W)`.  Hence every

   \[
   d=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right)
   \]

   is already unconditionally covered by a lossless queue packing.

   More strongly for raw OR coverage, round the same dummy-completed
   fractional queue system with ABKV's economical **cover** theorem instead
   of its matching theorem.  If `p` atoms are selected, the exact completed
   ledger is

   \[
   L_{\rm word}\le
   W+D_0+(2h+1)p+\sum_{r\ne0}M_r.
   \]

   A full augmented cover has every `M_r=0`, while its near-optimal edge
   count gives `D_0=pH-W=o(W)`.  With `H=ceil(sqrt(log m))`, simple
   Bernoulli support sparsification and ABKV Theorem 3.7 give

   \[
   p\le\frac WH(1+o(1))
   \]

   for every `h=o(sqrt(log m))`.  Concatenating the literal queue atoms
   therefore gives a zero-hole word of length `(1+o(1))W` throughout that
   range.  This removes the matching route's extra `sqrt(log log m)` loss,
   though it permits duplicate certified masks and still does not approach
   the reservoir scale.

2. Independently, a cyclic-strip hypergraph plus the growing-uniformity
   Alon--Bollobas--Kim--Vu economical-cover theorem gives an explicit
   zero-hole word of length `(1+o(1))W` through

   \[
   J=(\log m)^{1/2-o(1)}.
   \]

   The strip method itself cannot reach beyond `o(sqrt(log m))`: its word
   overhead needs `J/ell=o(1)` and its codegree condition needs
   `ell J=o(log m)`.

Together with the outer reservoir, the unresolved rank interval is now

\[
(\log m)^{1/2-o(1)}<|r-m|<\Theta(\sqrt{m\log\log m}).
\]

## 3A. Multidepth Johnson-path gate

There is now a third literal-factor route.  Let
`T_0,...,T_(L-1)` be a path in `J(2m,m)`.  If no coordinate has an internal
one-run of length at most `H`, define

\[
A_j=\bigcap_{i=\max(0,j-H)}^{\min(L-1,j)}T_i,
\qquad 0\le j<L+H.
\]

Then, literally,

\[
T_i=\bigcup_{j=i}^{i+H}A_j,
\]

\[
\bigcap_{s=0}^{q}T_{i+s}=\bigcup_{j=i+q}^{i+H}A_j,
\qquad
\bigcup_{s=0}^{q}T_{i+s}=\bigcup_{j=i}^{i+H+q}A_j.
\]

Only shadows of the correct ranks `m-q` and `m+q` are credited.  For
vertex-disjoint path families, let `p` be the number of components,
`M_q^-`, `M_q^+` the correct-rank shadow defects, and `rho_H` the number of
internal coordinate one-runs of length at most `H`.  Cutting before all
short runs gives the exact completed-word bound

\[
\boxed{
W+Hp+\sum_{q=1}^{H}(M_q^-+M_q^+)
 +(H^2+2H)\rho_H.}
\tag{JP}
\]

Thus it is sufficient to make every term after `W` in (JP) `o(W)` at a
tail-compatible depth.  Pin survival is not an additional condition: the
erosion entries themselves are the physical OR word.

At depth one this is already unconditional.  If a two-sided-rainbow Johnson
linear forest has `e` edges and `c` nontrivial components, the path word

\[
T_0,S_1,\ldots,S_\ell,T_\ell,
\qquad S_i=T_{i-1}\cap T_i,
\]

completes the three ranks at exact length

\[
W+2\left(\binom{2m}{m-1}-e\right)+c.
\]

The existing near-rainbow forest has `e=binom(2m,m-1)-o(W)` and `c=o(W)`.
Therefore ranks `m-1,m,m+1` have an unconditional literal `W+o(W)` word.

The erosion gate can absorb all outer ranks directly.  Append `T`
all-depth singleton cyclic-order blocks, each of length `4m-2`.  For every
path forest and every `T>=1`,

\[
\begin{aligned}
\nu(2m)\le{}&W+Hc+\sum_{q=1}^H(M_q^-+M_q^+)
 +(H^2+2H)\rho_H\\
&+(4m-2)T
 +2\sum_{q=H+1}^{m-1}N_q(1-2m/N_q)^T.
\end{aligned}
\tag{JPS}
\]

Taking `T=ceil(W/(2ma_m))`, where `a_m->infinity` and
`log a_m=o(log log m)`, makes the second line `o(W)` at

\[
H=(1+o(1))\sqrt{m\log\log m}.
\]

This yields one exact sufficient ledger:

\[
Hc+\sum_{q\le H}(M_q^-+M_q^+)+(H^2+2H)\rho_H=o(W).
\]

Do not try to meet it by merely appending the singleton blocks to the
existing strip, depth-one, or fixed-radius queue word.  Each such word has
no value in its first uncontrolled lower rank, and intact singleton blocks
plus literals then cost at least `(1-o(1))W`.  Cross-seam windows are the
missing operation.  Exactly `q` lower and `q` upper windows cross one splice
at depth `q`, recovering `d(d+1)` endpoint slots through depth `d`; their
labels must be made multidepth-rainbow.

Unconstrained endpoint scarcity is already solved.  Greedily splice
Johnson-adjacent endpoints of different components.  At maximality, spectral
supersaturation in `J(2m,m)` (degree `m^2`, least eigenvalue `-m`) gives

\[
c\le W/(2m),
\]

so `Hc=o(W)` at every `H=o(m)`.  This estimate need not survive after
restricting to short-run-safe and multidepth-rainbow splice edges.  In the
ideal independent queue-segment model with `L_0=o(sqrt(m))`, one-step safe
endpoint edges have density

\[
\frac{m^2}{W}\left(1-O(L_0^2/m)\right),
\]

and expected degree `~m^2/L_0`.  Static pairwise safety does not compose
under repeated splicing.  The missing theorem is a dynamic Hall/quasirandom
endpoint invariant for the actual integral atom selection, together with
control of the crossing-window labels and updated boundary-run histories.

## 4. Quantitative barriers that your proof must overcome

The following shortcuts have been audited and do not prove the theorem.

1. **Independent random wreaths or queues.** At mean load one they are
   Poisson-collision dominated. For monotone queue atoms,

   \[
   \mathbb E\sum D_q
   =(\sqrt\pi/e+o(1))W\sqrt m,
   \]

   and already the middle row has \((e^{-1}+o(1))W\) duplicates with
   exponentially high probability.

2. **A routine fixed-uniformity matching nibble.** A full band atom contains
   \(\Theta(m^{3/2})\) masks. Same-rank normalized pair codegree is
   \(\Theta(m^{-2})\), but adjacent nested depths have normalized codegree
   \((2+o(1))/m\). The required leftover is \(o(W)\) among
   \(\Theta(W\sqrt m)\) band masks, namely relative \(o(m^{-1/2})\). An
   unspecified \(o(1)\) matching error is insufficient.  This obstruction
   does not apply to an economical edge cover: that is precisely why the
   queue-cover theorem above reaches every `o(sqrt(log m))` depth while
   permitting duplicate certified masks.

3. **Fractional feasibility or LP duality alone.** The exact all-depth
   wreath LP, its nested SCD strengthening, the queue system, and earlier
   chain systems all have exact symmetric fractional covers.  The wreath
   point is even a convex combination of genuine exact factors.  The
   unsolved content is nonlinear correlated integral selection with the
   lossless ledger (CL), (NAE), or (DM).

4. **Per-rank counts without compatibility.** Marginally correct matchings
   at each depth need not arise from one common family of wreaths or queues.
   Preserve common ownership across every depth.

5. **Scalar blocker or antichain improvements.** The complete antichain
   barrier/Hall relaxation is already exhausted at the rank-count bound. It
   contains no missing upper-construction information.

6. **Atomic-square plus ordinary alpha-switch endpoint repair.** These moves
   satisfy

   \[
   \operatorname{sgn}(\pi)=(-1)^{\text{tag transfer}},
   \]

   so a ledger-neutral word is endpoint-even. The natural four-boundary plus
   inverse-atomic composite reduces to a one-tag Johnson square that
   preserves individual colours only by consuming two occurrences of the
   same colour. It is unavailable in a colour-perfect factor without a
   duplicate-colour reservoir.

7. **Overbroad tail parameters.** The recorded moderate-deviation theorem is
   uniform for \(h=\sqrt{m\omega}\) with \(\omega=o(m^{1/3})\). The clean
   choice \(\omega=\log m\) is sufficient.

8. **Charging every hole separately.** Extreme marked traces can be repaired
   once across all depths.  Any argument that insists on
   `sum_q M_q=o(W)` is solving a stronger problem than (SCT).

## 5. Productive proof lanes

If several instances receive this prompt, assign one lane per instance.

### Lane A — flexible exact wreath factor

Construct or modify an exact middle wreath factor while controlling the
incremental overlap excess in (CL). Prove (WV), or first prove \(M_1=o(W)\).
Switches must preserve exact middle ownership.

### Lane A2 — relaxed cyclic near-factor

Exploit the weaker target (RNF).  Construct \(W/n+o(W/n)\) cyclic orders
whose aggregate missing mass, *including the middle layer*, is \(o(W)\).
Exact middle ownership is optional.  Quantify the loss at the required
relative \(o(m^{-1/2})\) scale; a generic near-perfect matching estimate is
not enough.

### Lane A3 — shallow soft trace factor

Target (SCT), the weakest current cyclic gate.  Choose the cyclic family and
one marked coordinate set jointly.  Control only holes with near-balanced
marked trace through depth `(1+o(1))sqrt(m log log m)`; all extreme traces
and all deeper ranks already have `o(W)` repairs.  A proof must retain the
same marked set and same cyclic family across every shallow depth.

### Lane B — lossless correlated random greedy/absorption

Design a process whose state variable is the excess above unavoidable
overlap, not raw overlap. Prove all concentration estimates uniformly for
growing edge size and obtain total residual \(o(W)\), not merely
\(o(\text{total band size})\).

### Lane C — weak queue packing

First create a near-disjoint packing of the middle queue paths, then steer or
absorb only the missing nonmiddle shadows. Prove (WQ). Do not insist on
near-disjointness outside the middle unless used essentially.

The economical queue cover already settles every
`h=o(sqrt(log m))`, so a new theorem in this lane must either pass that
depth, exploit its duplicate freedom in a multiscale absorber, or connect it
to the outer reservoir; reproving a shallower band is not progress.

### Lane C2 — rainbow Johnson erosion

Construct vertex-disjoint Johnson paths satisfying the multidepth bound
(JP).  Global duplicates away from adjacent windows are irrelevant.  The
new local obstruction is only the short-run charge `rho_H`; exact path
cycles, exact SCDs, and a separate pin assignment are unnecessary.

### Lane D — explicit algebraic/design construction

Seek a group-orbit, resolvable-design, universal-cycle, or recursive Catalan
construction giving exact middle ownership and lossless shallow shadows.
Check all divisibility conditions and quantify seams through depth \(H\).

### Lane E — obstruction with a replacement target

If a proposed atom/factor class cannot satisfy (WV) or (WQ), prove a lower
bound on its summed defect. Then identify a strictly more flexible class;
do not present failure of one ansatz as failure of the original OR problem.

## 6. Required output standard

Your response must contain:

1. a precise theorem statement;
2. a complete proof, with every asymptotic uniformity range stated;
3. exact accounting showing how it changes \(\sum_q M_q\) or the OR-word
   length;
4. verification on the smallest nontrivial dimensions, preferably with
   executable pseudocode or a compact checker;
5. an explicit list of anything still conditional.

Do not claim

\[
\nu(k)\le(1+o(1))W(k)
\]

unless the same integral construction simultaneously supplies either exact
middle ownership or only \(o(W)\) middle repair, total central-band defect
\(o(W)\), a genuine contiguous-OR word, and the \(o(W)\) tail completion.

The cleanest exact target is (WV), but the logically weakest isolated cyclic
target is now (SCT).  The rotor theorem, the fixed-band queue rounding, and
the explicit cyclic-strip cover are valid supporting machinery; none alone
reaches the reservoir threshold.

If the instance has access to the project workspace, it should read these
proof audits before beginning:

- GLOBAL_WREATH_SHADOW_TRANSFER_AUDIT_20260724.md
- WREATH_LP_DUAL_AND_RELAXED_TRANSFER_20260724.md
- WREATH_FIRST_SHADOW_COMPONENT_NAE_THEOREM_20260724.md
- WREATH_VERTICAL_PROPAGATION_GATE_20260724.md
- SHALLOW_RESERVOIR_DEFECT_DAMPING_20260724.md
- SOFT_TRACE_COMPRESSION_AND_SHALLOW_GATE_20260724.md
- BOUNDED_PARAMETER_QUEUE_ROUNDING_AUDIT_20260724.md
- QUANTITATIVE_GROWING_QUEUE_ROUNDING_AUDIT_20260724.md
- ECONOMICAL_QUEUE_COVER_AUDIT_20260724.md
- GROWING_BAND_LOSSLESS_QUEUE_PACKING_AUDIT_20260724.md
- CYCLIC_STRIP_GROWING_BAND_AUDIT_20260724.md
- ALL_DEPTH_WREATH_SPRINKLING_AUDIT_20260724.md
- RAINBOW_PATH_EROSION_TRANSFER_AUDIT_20260724.md
- SPRINKLED_EROSION_FOREST_AND_SPLICE_BARRIER_20260724.md
- JOHNSON_ENDPOINT_SPLICE_THEOREM_20260724.md
- GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT.md
- ODD_GRAPH_EXACT_WREATH_FACTOR.md
- WREATH_FIRST_SHADOW_AUDIT.md
- MULTIDEPTH_WREATH_CUT_AUDIT.md
- MONOTONE_PROFILE_ROTOR_PACKING_FINAL_AUDIT.md
- MONOTONE_RADIUS_ROTOR_BRAIDS_AUDIT.md
- MONOTONE_QUEUE_PACKING_CODEGREES.md
- TRUNCATED_TAIL_CONSTRUCTION.md
- ATOMIC_ALPHA_PARITY_LOCK.md
- NEUTRAL_ODD_COMPOSITE_COLLAPSE.md
