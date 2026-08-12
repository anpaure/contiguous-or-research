# Recursive complement transfer through omitted pairs

Date: 2026-07-25

Method: pure mathematics only. No search, solver, or finite computation is
used.

## 0. Outcome

Put

\[
N_m(d)=\binom{2m+1}{m+d},
\qquad
W_m=N_m(0)=N_m(1).
\]

This report derives the exact recursive transfer requested in the prompt.

1. Complementation on a child universe of size \(2r+1\) sends centre
   offset \(e\) to \(1-e\), signed depth \(q\) to \(-q\), and preserves
   physical path components exactly.
2. An unfused one-pair lift has the exact Pascal recurrences

   \[
   J'_{m,d}
   =J_{m-1,d+1}+2J_{m-1,d}+J_{m-1,d-1},
   \]

   and the identical recurrence for every signed hole ledger \(M(q)\).
   After normalization, the component recurrence at central offset has
   weights

   \[
   \frac14+\frac1{8m+4},\qquad
   \frac12+\frac1{4m+2},\qquad
   \frac14-\frac3{8m+4}.
   \]

   (the depth-\(q\) hole recurrence uses the same functions evaluated at
   offset \(q\)).
3. Exposing \(b\) pairs gives a binomial block operator

   \[
   (\mathsf P_bT)_{m,d}
   =\sum_{t=0}^{2b}\binom{2b}{t}
     T_{m-b,d+b-t},
   \]

   satisfying the exact semigroup law

   \[
   \mathsf P_b\mathsf P_c=\mathsf P_{b+c}.
   \]

   Thus every block-diagonal accelerated recursion is a Markov average of
   its leaf defect densities. It cannot turn a defect occupying
   nonvanishing exact fibre mass into \(o(1)\).
4. The concrete four-phase lift of one two-sided child path has an exact
   component and hole recurrence. The only negative terms are genuine
   collar-clean seams and the new targets represented across them.
   Complementation itself supplies neither term.
5. A macroscopic acceleration from residual dimension
   \(r\sim\beta m\), \(0<\beta<1\), has an unavoidable
   \(\Theta(W_m)\) cell-quota defect at every depth
   \(q\sim A\sqrt m\). It requires \(\Omega(W_m/\sqrt m)\) useful
   cross-cell seams; a block-diagonal jump cannot be coefficient one.
6. A uniform radius-\(H\), target-distinct physical path system has the
   unavoidable capacity bound

   \[
   HJ_{\rm lin}\ge M-N_r(-H).
   \]

   If \(M=(1-o(1))W_r\) and \(H=A\sqrt r\), this is

   \[
   HJ_{\rm lin}
   \ge(1-e^{-A^2}-o(1))W_r.
   \]

   At product-tail depth \(H=\alpha\sqrt{r\log r}\), the right side is
   \((1-o(1))W_r\). Hence a full-radius recursive path tower already has
   macroscopic reset cost. Variable radii are indispensable.

The verdict is therefore exact. A block size can make the component term
small only when the residual systems already have a vanishing component
density on almost all exact fibre mass. It does not shrink inherited
multidepth hole density. No accelerated block recursion proves
\(o(W_m)\) total defect using only these block-diagonal/complement
operations. The missing gain is a collar-clean endpoint
path-cover theorem together with crossing-window service of the inherited
holes.

---

## 1. Signed path ledgers and exact complementation

Let \(Q\) have size \(2r+1\). A signed physical path system
\(\mathcal P_{r,e}\) has centre vertices in

\[
\binom Q{r+e}.
\]

For \(q>0\), its signed-\(q\) targets are unions of \(q+1\)
consecutive centre vertices; for \(q<0\), they are intersections of
\(|q|+1\) consecutive centre vertices. Write

\[
J_{r,e}
\]

for the number of linear path components and

\[
M_{r,e}(q)
\]

for the number of rank-\((r+e+q)\) targets not represented by such a
window. We always take \(M_{r,e}(0)=0\) when every centre owner is used
once.

For a radius \(H\), define the literal reset/repair defect

\[
\mathcal L_{r,e,H}
=(2H+1)J_{r,e}
+\sum_{1\le |q|\le H}M_{r,e}(q).
\tag{1.1}
\]

Its centre-normalized value is

\[
\Lambda_{r,e,H}
=\frac{\mathcal L_{r,e,H}}{N_r(e)}.
\tag{1.1a}
\]

### Theorem 1.1 -- exact complement involution

Complement every centre vertex inside \(Q\). Then

\[
\boxed{
e\longmapsto 1-e,\qquad q\longmapsto-q,
}
\tag{1.2}
\]

and

\[
\boxed{
J^{\,c}_{r,1-e}=J_{r,e},
\qquad
M^{\,c}_{r,1-e}(q)=M_{r,e}(-q).
}
\tag{1.3}
\]

In particular,

\[
\mathcal L^{\,c}_{r,1-e,H}=\mathcal L_{r,e,H}.
\tag{1.4}
\]

#### Proof

The complement of a set of size \(r+e\) has size

\[
(2r+1)-(r+e)=r+1-e.
\]

For consecutive centre vertices \(S_i\), De Morgan gives

\[
\bigcap_{h=0}^{q}(Q\setminus S_{i+h})
=Q\setminus\bigcup_{h=0}^{q}S_{i+h},
\]

\[
\bigcup_{h=0}^{q}(Q\setminus S_{i+h})
=Q\setminus\bigcap_{h=0}^{q}S_{i+h}.
\]

Complementation is a bijection on every Boolean rank and does not split or
join a path. This proves (1.2)--(1.4). \(\square\)

### Lemma 1.2 -- fixed-prefix transfer

Let \(K\) be a fixed set disjoint from \(Q\). Replacing every child vertex
\(S_i\) by \(K\cup S_i\) preserves all signed depths and all components.

#### Proof

For every family of child sets,

\[
\bigcap_i(K\cup S_i)=K\cup\bigcap_iS_i,
\qquad
\bigcup_i(K\cup S_i)=K\cup\bigcup_iS_i.
\]

Coordinates in \(K\) remain fixed throughout the lifted block, so they
create no short residence or nonresidence interval. \(\square\)

One important scope point follows already from (1.2). A centre system at
offset zero gives its complementary system at offset one. It does not give
the offset \(-1\) system: that system is complementary to offset two.
Thus one central child cannot silently be used for all three branches of a
one-pair Pascal lift.

---

## 2. The exact one-pair transfer and normalized weights

Expose a pair \(P=\{a,b\}\) from a parent universe of size \(2m+1\), and
put \(r=m-1\). A parent centre target of rank \(m+d\) has residual offsets

\[
d+1,\qquad d,\qquad d-1
\]

according as it contains zero, one, or two elements of \(P\). Therefore

\[
\boxed{
N_m(d)=N_r(d+1)+2N_r(d)+N_r(d-1).
}
\tag{2.1}
\]

### Theorem 2.1 -- unfused one-pair recurrences

Use independent child path systems in the four fixed-prefix cells, and
make no cross-cell seam. Then

\[
\boxed{
J^{\square}_{m,d}
=J_{r,d+1}+2J_{r,d}+J_{r,d-1},
}
\tag{2.2}
\]

\[
\boxed{
M^{\square}_{m,d}(q)
=M_{r,d+1}(q)+2M_{r,d}(q)+M_{r,d-1}(q),
}
\tag{2.3}
\]

and

\[
\boxed{
\mathcal L^{\square}_{m,d,H}
=\mathcal L_{r,d+1,H}
+2\mathcal L_{r,d,H}
+\mathcal L_{r,d-1,H}.
}
\tag{2.4}
\]

Equivalently, using only complemented child systems, the three offsets in
(2.2) are replaced by

\[
-d,\qquad1-d,\qquad2-d,
\]

and every \(q\) in (2.3) is replaced by \(-q\).

#### Proof

The four prefix cells are disjoint. Lemma 1.2 transports every signed
window literally inside its cell. Components and holes therefore add.
The complemented form is Theorem 1.1. \(\square\)

Define

\[
\gamma_{m,d}=\frac{J_{m,d}}{N_m(d)},
\qquad
\delta_{m,d}(q)=\frac{M_{m,d}(q)}{N_m(d+q)}.
\tag{2.5}
\]

For a ledger centred at offset \(x\), the exact one-pair weights are

\[
w_+(x)=
\frac{(m-x)(m+1-x)}{2m(2m+1)},
\]

\[
w_0(x)=
\frac{2(m+x)(m+1-x)}{2m(2m+1)},
\]

\[
w_-(x)=
\frac{(m+x)(m+x-1)}{2m(2m+1)}.
\tag{2.6}
\]

They are nonnegative in range and sum to one. Hence

\[
\boxed{
\gamma^{\square}_{m,d}
=w_+(d)\gamma_{r,d+1}
+w_0(d)\gamma_{r,d}
+w_-(d)\gamma_{r,d-1},
}
\tag{2.7}
\]

while

\[
\boxed{
\delta^{\square}_{m,d}(q)
=w_+(d+q)\delta_{r,d+1}(q)
+w_0(d+q)\delta_{r,d}(q)
+w_-(d+q)\delta_{r,d-1}(q).
}
\tag{2.8}
\]

At \(d=0\),

\[
\boxed{
w_+(0)=\frac14+\frac1{8m+4},\quad
w_0(0)=\frac12+\frac1{4m+2},\quad
w_-(0)=\frac14-\frac3{8m+4}.
}
\tag{2.9}
\]

Thus the normalized constant mode is preserved exactly. Complementation
only reflects the child offsets and signed depths; it changes none of
these weights.

---

## 3. The concrete four-phase lift of one two-sided child system

The preceding theorem uses independent systems at three offsets. There is
a more economical but more constrained construction from one tight
two-sided child system.

Let \(\mathcal P\) be physical through radius \(H+1\), target-distinct at
every signed depth under discussion, and partition the \(r\)-sets of
\(Q\) into oriented literal coordinate-interval paths

\[
C=(S_0,S_1,\ldots,S_{\ell_C-1}).
\]

Put

\[
D_i=S_i\cap S_{i+1}
\qquad(0\le i<\ell_C-1).
\]

The four parent occupancy blocks are

\[
Q\setminus S_i,\qquad
\{a\}\cup S_i,\qquad
\{a,b\}\cup D_i,\qquad
\{b\}\cup S_i.
\tag{3.1}
\]

Let \(J\) be the number of child paths, let

\[
J^-=\#\{C:\ell_C\ge2\},
\]

and write \(M(q)\) for the child hole ledger. Add every missing
depth-\((-1)\) child target as an isolated full-prefix parent centre owner.

For \(q\ge1\), define

\[
B(q)=\sum_C\min\{2,(\ell_C-q+1)_+\},
\qquad
B(q)=0\quad(q\le0).
\tag{3.2}
\]

### Lemma 3.1 -- exact lower-carrier transfer

For \(-H\le q\le0\), the signed-\(q\) windows of the \(D\)-path are exactly the
signed-\((q-1)\) windows of the \(S\)-path. For \(1\le q\le H\), they are the
signed-\((q-1)\) windows with the two endpoint windows removed whenever
both exist. The total number removed is exactly \(B(q)\).

#### Proof

Write a tight child path locally as cyclic coordinate intervals

\[
S_i=I(i,r).
\]

Then

\[
D_i=I(i+1,r-1).
\]

For \(q\ge1\),

\[
\bigcup_{h=0}^{q}D_{i+h}
=\bigcup_{h=1}^{q}S_{i+h},
\]

which is a signed-\((q-1)\) child window missing the first and last
possible starting positions. For \(q=-h\le0\),

\[
\bigcap_{u=0}^{h}D_{i+u}
=\bigcap_{u=0}^{h+1}S_{i+u},
\]

with identical index range. Formula (3.2) handles short paths exactly.
\(\square\)

### Theorem 3.2 -- exact concrete component and hole recurrence

Before any cross-block seam, the repaired parent centre system has

\[
\boxed{
J^{\square}_m=3J+J^-+M(-1).
}
\tag{3.3}
\]

For every \(q\) with \(0<|q|\le H\),

\[
\boxed{
M^{\square}_m(q)
=M(-q)+2M(q)+M(q-1)+B(q).
}
\tag{3.4}
\]

In particular, parent depth \(-H\) uses the child ledger at depth
\(-(H+1)\); this is why the input was assumed physical through radius
\(H+1\).

Suppose \(S_*\) legal seams join distinct current components, and, for
\(0<|q|\le H\), their crossing windows represent \(G(q)\) distinct targets
counted in \(M^{\square}_m(q)\). Then

\[
\boxed{
J_m=3J+J^-+M(-1)-S_*,
}
\tag{3.5}
\]

\[
\boxed{
M_m(q)=M(-q)+2M(q)+M(q-1)+B(q)-G(q).
}
\tag{3.6}
\]

#### Proof

Complementation gives \(J\) no-pair components, and the two singleton
prefixes give \(2J\). The nonempty \(D\)-paths give \(J^-\) full-prefix
components. The missing full-prefix centre owners are exactly the
\(M(-1)\) missing child intersections and are inserted as isolated
components. This proves (3.3).

The no-pair branch is complementary to signed depth \(-q\), the two
singleton branches carry signed depth \(q\), and Lemma 3.1 gives the
full-prefix term. The four occupancy classes are disjoint, proving (3.4).
Every legal seam joining two components reduces the component count by one;
every useful distinct crossing target reduces the corresponding hole count
by one. This proves (3.5)--(3.6). \(\square\)

Let

\[
A=N_r(0)=\binom{2m-1}{m-1},
\qquad
C=N_r(-1)=\binom{2m-1}{m-2}.
\]

Then

\[
W_m=3A+C,\qquad \frac CA=\frac{m-1}{m+1}.
\tag{3.7}
\]

If

\[
\Delta(q)=\frac{M(q)}{N_r(q)},
\]

then, for \(0<|q|\le H\), (3.6) becomes the exact normalized recurrence

\[
\boxed{
\begin{aligned}
\Delta_m(q)
={}&
\frac{N_r(-q)}{N_m(q)}\Delta(-q)
+\frac{2N_r(q)}{N_m(q)}\Delta(q)\\
&+\frac{N_r(q-1)}{N_m(q)}\Delta(q-1)
+\frac{B(q)-G(q)}{N_m(q)}.
\end{aligned}}
\tag{3.8}
\]

The first three coefficients sum to one. For \(|q|=o(m)\), they are
\(1/4+o(1),1/2+o(1),1/4+o(1)\). Thus even a perfectly fused component
ledger does not shrink inherited hole density unless the crossing-window
term \(G(q)\) does real work.

### Proposition 3.3 -- the automatic same-child braid is not physical

The natural attempt to join the full upper block to a reversed copy of the
same child path fails already at radius one.

#### Proof

Write

\[
S_{i+1}=S_i-p_i+q_i,
\qquad
U_i=S_i\cup S_{i+1}.
\]

At the right natural portal, the transitions are

\[
U_{\ell-2}\longrightarrow \{a\}\cup S_{\ell-1}
\longrightarrow \{a\}\cup S_{\ell-2}.
\]

The first transition removes \(p_{\ell-2}\), while the second immediately
reinserts it. Thus this residual coordinate is absent for one vertex and
the adjacent transition supports intersect. At the left portal the
analogous coordinate is removed and immediately reinserted. The alternative
facets that avoid the immediate toggle are not endpoints of the full
linear child block. A nonlocal endpoint with a clean collar may work, but
that is an additional matching theorem. \(\square\)

### Proposition 3.4 -- exact cut/seam topology

Start with \(J_{\rm in}\) linear block components. Cutting \(C_*\) interior
edges gives \(J_{\rm in}+C_*\) pieces. If \(S_*\) new seams join distinct
current pieces and no seam closes a cycle, then

\[
\boxed{
J_{\rm out}=J_{\rm in}+C_*-S_*.
}
\tag{3.9}
\]

At signed depth \(q\), let \(R_q\) be represented targets destroyed by the
cuts and let \(G_q\) be targets missing after those cuts and newly restored
by the seams. Then

\[
\boxed{
M_{\rm out}(q)=M_{\rm in}(q)+R_q-G_q,
}
\tag{3.10}
\]

with

\[
0\le R_{\pm q}\le qC_*,
\qquad
0\le G_{\pm q}\le qS_*.
\tag{3.11}
\]

Consequently

\[
\boxed{
\begin{aligned}
\mathcal L_{\rm out}
={}&\mathcal L_{\rm in}
+(2H+1)(C_*-S_*)\\
&+\sum_{1\le|q|\le H}(R_q-G_q).
\end{aligned}}
\tag{3.12}
\]

Thus an interior clip followed by one compensating splice has no component
gain. A net gain \(S_*-C_*\) requires that many surplus collar-clean seams.

---

## 4. Exact \(b\)-pair acceleration

Expose \(b\) pairs and put \(s=m-b\). A fixed prefix containing \(t\) of
the \(2b\) exposed coordinates leaves residual offset

\[
e=d+b-t.
\]

Vandermonde gives

\[
\boxed{
N_m(d)=\sum_{t=0}^{2b}\binom{2b}{t}N_s(d+b-t).
}
\tag{4.1}
\]

### Theorem 4.1 -- block operator and semigroup

For every additive block-diagonal ledger

\[
T\in\{N,J,M(q),\mathcal L\},
\]

one has

\[
\boxed{
T^{[b]}_{m,d}
=\sum_{t=0}^{2b}\binom{2b}{t}T_{s,d+b-t}.
}
\tag{4.2}
\]

With

\[
(\mathsf P_bT)_{m,d}
=\sum_{t=0}^{2b}\binom{2b}{t}T_{m-b,d+b-t},
\]

\[
\boxed{
\mathsf P_b\mathsf P_c=\mathsf P_{b+c}
\qquad(b,c\ge0,\ b+c\le m).
}
\tag{4.3}
\]

#### Proof

There are \(\binom{2b}{t}\) fixed prefixes of size \(t\). Lemma 1.2
proves literal transfer in every cell, and different cells cannot collide.
For composition, Vandermonde gives

\[
\sum_u\binom{2b}{u}\binom{2c}{t-u}
=\binom{2(b+c)}t.
\]

\(\square\)

Define

\[
\pi_t^{(m,d,b)}
=\binom{2b}{t}\frac{N_s(d+b-t)}{N_m(d)}.
\tag{4.4}
\]

Then \(\pi_t\ge0\), \(\sum_t\pi_t=1\), and

\[
\boxed{
\gamma^{[b]}_{m,d}
=\sum_t\pi_t^{(m,d,b)}\gamma_{s,d+b-t},
}
\tag{4.5}
\]

\[
\boxed{
\delta^{[b]}_{m,d}(q)
=\sum_t\pi_t^{(m,d+q,b)}
\delta_{s,d+b-t}(q).
}
\tag{4.6}
\]

The same central weights give

\[
\boxed{
\frac{\mathcal L^{[b]}_{m,d,H}}{N_m(d)}
=\sum_t\pi_t^{(m,d,b)}
\frac{\mathcal L_{s,d+b-t,H}}{N_s(d+b-t)}.
}
\tag{4.7}
\]

Equations (4.5)--(4.7) are exact Markov averages. The constant defect mode
is a fixed point for every \(b\).

The weights have a hypergeometric interpretation. If \(T\) is exposed
occupancy under (4.4), then

\[
\mathbb ET=\frac{2b(m+d)}{2m+1},
\]

\[
\operatorname {Var}T
=2b\,\frac{m+d}{2m+1}
\left(1-\frac{m+d}{2m+1}\right)
\frac{2m+1-2b}{2m}.
\tag{4.8}
\]

In particular, for \(d=o(m)\), writing \(s=m-b\),

\[
\operatorname {Var}T
=(1+o(1))\frac{b(2s+1)}{4m}.
\tag{4.9}
\]

If also \(s\to\infty\), this is
\((1+o(1))bs/(2m)\).

Therefore a defect bounded below on a fixed-multiple standard-deviation
band of nonvanishing exact weight survives with a positive normalized
size. A block can dilute a defect supported on a negligible offset fibre,
but only by routing almost all mass to other fibres already assumed good.

### Theorem 4.2 -- exact leaf-average no-contraction theorem

For any adaptive recursion tree made solely of fixed-prefix cells and no
cross-cell seams, there are leaf multiplicities \(a_\ell\) and residual
parameters \((s_\ell,e_\ell)\) such that

\[
N_m(d)=\sum_\ell a_\ell N_{s_\ell}(e_\ell),
\qquad
J_{m,d}=\sum_\ell a_\ell J_{s_\ell,e_\ell},
\tag{4.10}
\]

\[
N_m(d+q)=\sum_\ell a_\ell N_{s_\ell}(e_\ell+q),
\qquad
M_{m,d}(q)=\sum_\ell a_\ell M_{s_\ell,e_\ell}(q).
\tag{4.11}
\]

Hence every root density is exactly the corresponding exact-mass average
of the leaf densities. In particular:

* a homogeneous positive density is preserved exactly;
* a positive density on leaf mass at least \(\eta>0\) leaves root density
  at least its lower bound times \(\eta\);
* the root density is \(o(1)\) only if leaf density converges to zero in
  probability under the exact weights.

#### Proof

Induct on the recursion tree using (4.1)--(4.2). Division by the matching
mass identities gives the asserted probability averages. \(\square\)

This statement has a necessary qualification. A defect on one negligible
offset fibre can be averaged away. For example, take \(m=2s\), \(b=s\),
and put unit leaf density only at residual offset zero. Its root weight is

\[
\frac{\binom{2s}{s}W_s}{W_{2s}}
\sim\sqrt{\frac2{\pi s}}=o(1).
\tag{4.12}
\]

This is not a recursive improvement: all other leaf fibres were assumed
perfect.

---

## 5. First-deviation phases and exceptional sources

Scanning the first \(b\) pairs until the first nonsingleton pair gives the
exact truncated recurrence

\[
\boxed{
N_m(x)
=2^bN_{m-b}(x)
+\sum_{j=1}^{b}2^{j-1}
\bigl(N_{m-j}(x+1)+N_{m-j}(x-1)\bigr).
}
\tag{5.1}
\]

The same identity holds for every additive block-diagonal ledger. In
particular, when the scan runs through all \(m\) pairs,

\[
E_m(d)=2^m(\mathbf1_{d=0}+\mathbf1_{d=1}),
\tag{5.2}
\]

\[
\boxed{
J^{\rm fd}_{m,d}
=E_m(d)+\sum_{j=1}^{m}2^{j-1}
\bigl(J_{m-j,d+1}+J_{m-j,d-1}\bigr),
}
\tag{5.3}
\]

and, for \(q\ne0\),

\[
\boxed{
M^{\rm fd}_{m,d}(q)
=E_m(d+q)+\sum_{j=1}^{m}2^{j-1}
\bigl(M_{m-j,d+1}(q)+M_{m-j,d-1}(q)\bigr).
}
\tag{5.4}
\]

The exactly equivalent complemented form replaces the two child offsets
\(d+1,d-1\) by

\[
-d,\qquad2-d,
\]

and replaces \(q\) by \(-q\). Thus complementation pairs the empty and
full recursive towers but introduces no missing coefficient.

Define

\[
\beta_b(m,x)=2^b\frac{N_{m-b}(x)}{N_m(x)},
\]

\[
\alpha_{j,\pm}(m,x)
=2^{j-1}\frac{N_{m-j}(x\pm1)}{N_m(x)}.
\tag{5.5}
\]

These weights sum to one, so first-deviation batching is again an exact
convex average. Explicitly, the truncated normalized defect satisfies

\[
\boxed{
\begin{aligned}
\Lambda^{[b]}_{m,x,H}
={}&\beta_b(m,x)\Lambda_{m-b,x,H}\\
&+\sum_{j=1}^{b}\sum_{\sigma\in\{-1,+1\}}
\alpha_{j,\sigma}(m,x)
\Lambda_{m-j,x+\sigma,H}.
\end{aligned}}
\tag{5.5a}
\]

For fixed \(j\) and

\[
|x|\le A\sqrt{m\log m},
\]

\[
\alpha_{j,+}(m,x)
=\alpha_{j,-}(m,x)
=2^{-j-1}(1+o_A(1)).
\tag{5.6}
\]

Thus a proportion

\[
1-2^{-K}+o_A(1)
\]

of the mass exits in the first \(K\) deviation phases, independently of
how far the scan is batched, for fixed \(K\) and \(b\ge K\). At \(x=0\)
or \(1\), with \(s=m-b\to\infty\),

\[
\boxed{
\beta_b(m,x)
=(1+o(1))2^{-b}\sqrt{\frac ms}.
}
\tag{5.7}
\]

A large scan makes the all-singleton survivor negligible, but sends almost
all mass to early children of dimensions \(m-O(1)\). It therefore does not
accelerate the normalized defect.

If the scan is continued through all \(m\) pairs, this \(E_m(d)\) is the
terminal source.

Since

\[
W_m\sim\frac{2\cdot4^m}{\sqrt{\pi m}},
\]

\[
\frac{2^m}{W_m}
\sim\frac{\sqrt{\pi m}}2\,2^{-m}.
\tag{5.8}
\]

At \(d=0\) and \(H\ge1\), the normalized reset/repair source is exactly

\[
\frac{(2H+2)2^m}{W_m}
\sim(H+1)\sqrt{\pi m}\,2^{-m}.
\tag{5.9}
\]

More generally the full first-deviation normalized recurrence is

\[
\boxed{
\begin{aligned}
\Lambda^{\rm fd}_{m,d,H}
={}&
\sum_{j=1}^{m}\sum_{\sigma\in\{-1,+1\}}
\frac{2^{j-1}N_{m-j}(d+\sigma)}{N_m(d)}
\Lambda_{m-j,d+\sigma,H}\\
&+\frac{(2H+1)E_m(d)+
\sum_{1\le|q|\le H}E_m(d+q)}{N_m(d)}.
\end{aligned}}
\tag{5.10}
\]

This exponentially small source is not a contraction. If every terminal
exceptional owner is made an isolated path, induction through the same mass
recurrence gives

\[
J_{m,d}=N_m(d)
\]

exactly. Small sources at individual large nodes aggregate to full density
when the recursion is run to singleton leaves.

---

## 6. What block acceleration does to components

Suppose a residual tower on \(2s+1\) coordinates supplies exactly \(J_s\)
components in every relevant prefix fibre, and take one copy in every
fixed-prefix cell. An unfused lift through \(b=m-s\) pairs has

\[
J_m=4^bJ_s
\tag{6.1}
\]

components. Moreover,

\[
\boxed{
\frac{4^bW_s}{W_m}
=\prod_{u=s+1}^{m}\frac{2(u+1)}{2u+1}
=(1+o(1))\sqrt{\frac ms}.
}
\tag{6.2}
\]

The last asymptotic assumes \(s\to\infty\); the finite product identity is
exact for every \(1\le s<m\).

Thus copying one common absolute component count, measured against the
child central width, into every offset fibre incurs the factor
\(\Theta(\sqrt{m/s})\). This does not contradict the Markov theorem:
a density constant relative to each fibre's own mass is preserved exactly.

For the Catalan component scale

\[
J_s=\frac{W_s}{2s+1},
\]

\[
\boxed{
\frac{J_m}{W_m}
=(1+o(1))\frac{\sqrt m}{2s^{3/2}}.
}
\tag{6.3}
\]

The component count alone is \(o(W_m)\) when \(s\gg m^{1/3}\), and its
literal reset term is \(o(W_m)\) exactly when

\[
\boxed{
s^{3/2}\gg H\sqrt m.
}
\tag{6.4}
\]

For \(H=\sqrt m\,\omega(m)\), this requires

\[
s\gg(m\omega(m))^{2/3}.
\tag{6.5}
\]

This is a genuine component calculation but not a total-defect theorem.
It starts from a component density already tending to zero, requires the
same bound in every relevant offset fibre, and leaves every hole density as
the Markov average (4.6).

---

## 7. A macroscopic Gaussian block-defect theorem

The Markov-averaging statement has a concrete capacity consequence for a
macroscopic accelerated jump.

Let

\[
b=m-r,
\qquad q>0.
\]

In a fixed-prefix cell containing \(t=b-c\) exposed coordinates, the
parent centre owners are residual rank-\((r+c)\) sets, while the signed
depth-\(q\) targets are residual rank-\((r+c+q)\) sets. Even a cyclic
path system produces at most one signed-\(q\) target per centre owner.
Therefore the number of missed targets is at least

\[
\boxed{
D_{m,r}(q)
=\sum_{c=-b}^{b}\binom{2b}{b-c}
\bigl[N_r(c+q)-N_r(c)\bigr]_+.
}
\tag{7.1}
\]

### Theorem 7.1 -- a fixed-fraction jump has linear Gaussian defect

Suppose

\[
\frac rm\longrightarrow\beta\in(0,1),
\qquad
\frac q{\sqrt m}\longrightarrow A>0.
\tag{7.2}
\]

Then

\[
\boxed{
\frac{D_{m,r}(q)}{N_m(q)}
\longrightarrow\delta(A,\beta)>0,
}
\tag{7.3}
\]

where, for

\[
X\sim N\!\left(
-A(1-\beta),\frac{\beta(1-\beta)}2
\right),
\]

\[
\boxed{
\delta(A,\beta)
=\mathbb E\!\left[
\left(1-\exp\!\frac{2AX+A^2}{\beta}\right)
\mathbf1_{\{X<-A/2\}}
\right].
}
\tag{7.4}
\]

Consequently

\[
\boxed{
D_{m,r}(q)=\Theta(W_m).
}
\tag{7.5}
\]

#### Proof

Divide (7.1) by \(N_m(q)\). Under a uniformly chosen rank-\((m+q)\)
parent target, the exposed occupancy \(t\) is hypergeometric, and

\[
\frac{D_{m,r}(q)}{N_m(q)}
=\mathbb E\left[
\left(1-\frac{N_r(c)}{N_r(c+q)}\right)_+
\right],
\qquad c=b-t.
\tag{7.6}
\]

Its exact mean and variance are

\[
\mathbb Ec=\frac{b(1-2q)}{2m+1},
\]

\[
\operatorname {Var}c
=2b\,\frac{m+q}{2m+1}
\frac{m+1-q}{2m+1}
\frac{2r+1}{2m},
\]

Stirling's formula for the hypergeometric mass, uniformly for
\(c=x\sqrt m\) on compact \(x\)-intervals, gives the local Gaussian
limit and hence

\[
\frac c{\sqrt m}\Longrightarrow
X\sim N\!\left(
-A(1-\beta),\frac{\beta(1-\beta)}2
\right).
\tag{7.7}
\]

The same uniform Stirling expansion gives

\[
\log\frac{N_r(c)}{N_r(c+q)}
=\frac{2cq+q^2-q}{r}+o(1)
\longrightarrow\frac{2Ax+A^2}{\beta}.
\tag{7.8}
\]

Unimodality gives

\[
N_r(c+q)>N_r(c)
\quad\Longleftrightarrow\quad
2c+q<1.
\tag{7.9}
\]

Here the equivalence is asserted on the support
\(N_r(c+q)>0\), which is the support seen in (7.6); out-of-range
binomials carry zero target mass.

Gaussian tail bounds make the compact restriction harmless, and the
integrand in (7.6) is bounded by one. Dominated convergence therefore
gives (7.3)--(7.4). The normal law gives positive probability to every
nonempty interval below \(-A/2\), where the integrand is strictly
positive, so \(\delta(A,\beta)>0\).

Finally

\[
\frac{N_m(q)}{W_m}\longrightarrow e^{-A^2}>0,
\]

which proves (7.5). \(\square\)

Each cross-cell seam creates at most \(q\) new signed-\(q\) windows.
Thus every lift with \(S\) such seams satisfies the robust bound

\[
M_m(q)\ge D_{m,r}(q)-qS.
\]

Therefore repairing the compulsory defect (7.5) to \(o(W_m)\) requires

\[
\boxed{
\Omega(W_m/q)=\Omega(W_m/\sqrt m)
}
\tag{7.10}
\]

useful, target-distinct seams. This is numerically compatible with a
constant-one proof, but it is a new endpoint-matching theorem; no choice of
block size supplies the seams.

The fixed-\(\beta\) hypothesis is essential. A unit or sublinear jump has
only a smaller immediate quota residue. However the normalized transfer is
still the Markov average in Section 4, so iterating small nonnegative
residues is not a contraction argument. The theorem concerns a fixed
common \(2b\)-coordinate block partition; it does not rule out an adaptive
unequal-depth variable-radius construction equipped with cross-cell seams.

---

## 8. A uniform-radius Gaussian component obstruction

There is a separate obstruction to treating every centre owner as active
through one common radius.

### Theorem 8.1 -- component lower bound at a fixed lower depth

Let a target-distinct physical system contain \(M\) centre vertices in
linear paths and cycles. Let \(J_{\rm lin}\) be its number of linear path
components. If every component is physical through lower depth \(H\), then

\[
\boxed{
M-HJ_{\rm lin}\le N_r(-H).
}
\tag{8.1}
\]

Consequently

\[
\boxed{
HJ_{\rm lin}\ge M-N_r(-H).
}
\tag{8.2}
\]

#### Proof

A linear path with \(\ell\) centre vertices has
\((\ell-H)_+\) consecutive lower depth-\(H\) windows. A physical cycle
has one such window per centre vertex. Therefore the total number of
represented occurrences is at least

\[
M-HJ_{\rm lin}.
\]

Target-distinctness bounds this by the number \(N_r(-H)\) of available
rank-\((r-H)\) targets. This proves (8.1)--(8.2). \(\square\)

If

\[
M=(1-o(1))W_r
\]

and \(H=A\sqrt r+O(1)\), the central binomial ratio gives

\[
\frac{N_r(-H)}{W_r}=e^{-A^2+o(1)},
\]

so

\[
\boxed{
HJ_{\rm lin}
\ge(1-e^{-A^2}-o(1))W_r.
}
\tag{8.3}
\]

If

\[
H=\alpha\sqrt{r\log r}+O(1),
\]

then

\[
\frac{N_r(-H)}{W_r}=r^{-\alpha^2+o(1)}
\]

and

\[
\boxed{
HJ_{\rm lin}\ge(1-o(1))W_r.
}
\tag{8.4}
\]

Thus the reset term of a uniform full-radius path system is already
\(\Omega(W_r)\), independently of recursion or complementation. The
proportional quota \(N_r(-H)\), rather than all \(W_r\) centre owners,
may remain active at that depth. Any viable recursive construction must
therefore carry a variable-radius activity profile.

---

## 9. Exact boundary for a successful recursive lift

For an arbitrary block-diagonal lift, let \(J^{\rm block}\) and
\(M^{\rm block}(q)\) be the ledgers in Sections 2 or 4. If collar-clean
cross-cell seams are added, the only possible improved recurrence is

\[
\boxed{
J^{\rm new}=J^{\rm block}-S,
}
\tag{9.1}
\]

\[
\boxed{
M^{\rm new}(q)=M^{\rm block}(q)-G(q),
}
\tag{9.2}
\]

where every seam counted by \(S\) joins two distinct current components
and every target counted by \(G(q)\) is a previously missing, distinct
crossing window. Therefore

\[
\boxed{
\mathcal L^{\rm new}
=\mathcal L^{\rm block}
-(2H+1)S
-\sum_{1\le|q|\le H}G(q).
}
\tag{9.3}
\]

If interior clipping is needed, (3.9)--(3.12) must be used instead; a seam
which merely compensates for one cut gives no component gain.

The recursive route reaches total \(o(W_m)\) precisely if it supplies,
after all cuts,

\[
J^{\rm new}=o(W_m/H)
\tag{9.4}
\]

and

\[
\sum_{1\le|q|\le H}M^{\rm new}(q)=o(W_m).
\tag{9.5}
\]

Gray ordering of the exposed pair states ensures only that consecutive
prefix states differ in one coordinate. It does not produce the residual
endpoint containments or the \(H\)-clean collars needed for \(S\), and it
does not prove that the crossing windows counted by \(G(q)\) are useful and
distinct.

Hence:

* complementation is exact but neutral;
* first-deviation phases and larger block-diagonal lifts are exact but
  neutral after normalization;
* a fixed-fraction accelerated jump has the linear cell-quota defect
  (7.5), unless \(\Omega(W_m/\sqrt m)\) useful seams repair it;
* component acceleration can preserve an already good Catalan component
  scale, subject to (6.4), but cannot cure the multidepth holes;
* a uniform-radius tower is ruled out by (8.2);
* the only remaining positive mechanism is a variable-radius,
  collar-clean endpoint path cover with useful crossing-window service.

No such endpoint theorem is proved here, so no constant-one conclusion is
claimed.
