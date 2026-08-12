# Raw lead report: compact balanced three-box braid

Source thread: `019f946c-72e2-7fb1-9dfc-8045df59eaf0`

## Verdict

This route does **not** prove the contiguous-OR width conjecture. It does produce several unconditional theorems that substantially narrow the compact three-box gate:

1. The uniform compact theorem is equivalent to countably many pointwise homothetic-ray theorems.
2. A new rank-capped start lemma removes the former \(O(D^2)\) escape from all middle-band obstruction arguments.
3. Random middle orders, monotone slice sweeps, intact side braids, and the canonical recursively phased order all require \(\Omega(R^2)\) excess and therefore cannot prove the compact gate.
4. A literal Helly-core factor theorem identifies exactly what a surviving fragmented braid must supply.
5. A new coordinate-line stability theorem rules out asymptotically mixed, near-minimal line covers.

The surviving construction must be a genuinely fragmented, reset-free, strongly phase-separated braid. No such braid was constructed, and no order-independent quadratic obstruction was proved.

---

# 1. Exact raywise reduction

Let

\[
P(p,q,r)=[0,p]\times[0,q]\times[0,r],
\]

let \(g_3(p,q,r)\) be the minimum length of a range-maximum word covering all nonzero points, and let \(w(p,q,r)\) be the width.

### Theorem 1: exact face extension

If \(p_0\le p,\ q_0\le q,\ r_0\le r\), then

\[
\begin{aligned}
g_3(p,q,r)\le g_3(p_0,q_0,r_0)
&+(p-p_0)(q+r+1)\\
&+(q-q_0)(p_0+r+1)\\
&+(r-r_0)(p_0+q_0+1).
\end{aligned}
\tag{1}
\]

#### Proof

The two-dimensional word

\[
(a,0),(a-1,0),\ldots,(0,0),(0,1),\ldots,(0,b)
\]

has length \(a+b+1\), and the interval from \((x,0)\) to \((0,y)\) has maximum \((x,y)\).

Partition the outer shell into

\[
\begin{aligned}
&x>p_0,\\
&x\le p_0,\ y>q_0,\\
&x\le p_0,\ y\le q_0,\ z>r_0.
\end{aligned}
\]

For each new fixed \(x\)-level append the preceding rectangle word in the \(y,z\) coordinates, costing \(q+r+1\). Do the same for new \(y\)-levels and \(z\)-levels. Every witness stays inside its own appended face word. ∎

### Theorem 2: raywise equivalence

The compact estimate

\[
\sup_{\delta R\le p,q,r\le CR}
\frac{g_3(p,q,r)-w(p,q,r)}{R^2}\longrightarrow0
\tag{CB}
\]

for every fixed \(0<\delta<C\) is equivalent to the countable family

\[
\boxed{
g_3(at,bt,ct)=w(at,bt,ct)+o_{a,b,c}(t^2)
}
\tag{RAY}
\]

for every primitive positive integer triple \((a,b,c)\).

Only the nontrivial direction needs proof. Fix an integer \(L>2/\delta\), put

\[
h=\lfloor R/L\rfloor,\qquad
a=\lfloor p/h\rfloor,\quad b=\lfloor q/h\rfloor,\quad c=\lfloor r/h\rfloor.
\]

Then \(1\le a,b,c\le2CL\), and each coordinate gap is below \(h\). For fixed \(L\), only finitely many primitive rays occur, so (RAY) is uniform over this finite family:

\[
g_3(ah,bh,ch)=w(ah,bh,ch)+o_L(R^2).
\]

Width is coordinatewise monotone. By (1), the shell extension costs at most

\[
3h(2CR+1)\le \frac{6C}{L}R^2+O(R/L).
\]

Hence

\[
\limsup_{R\to\infty}\sup_{\delta R\le p,q,r\le CR}
\frac{g_3(p,q,r)-w(p,q,r)}{R^2}
\le\frac{6C}{L}.
\]

Let \(L\to\infty\). ∎

Thus **(RAY) is the smallest clean unproved local lemma**: it requires no rate uniformity between distinct aspect ratios.

---

# 2. New rank-capped start lemma

Choose witnesses

\[
I_i=[\ell_i,r_i],\qquad 1\le i\le M,
\]

for \(M\) distinct rank-\(h\) targets in a word of length \(M+D\), and put \(d_i=r_i-\ell_i\).

### Theorem 3

If \(L_{<h}\) distinct nonzero targets below rank \(h\) are represented, then

\[
\boxed{
L_{<h}\le\sum_{i=1}^M d_i+(h-1)D.
}
\tag{2}
\]

#### Proof

The \(\ell_i\) are distinct: equal left endpoints would make two equal-rank witness intervals nested, hence their distinct targets comparable.

Fix one witness for every below-rank target and group them by their left endpoint.

- At a selected start \(\ell_i\), a lower witness must end before \(r_i\); otherwise it contains \(I_i\) and its maximum contains the rank-\(h\) target. There are at most \(d_i\) possible endpoints.
- Exactly \(D\) starts are not selected middle starts. At one fixed start, maxima obtained by moving the right endpoint form a chain. Below rank \(h\), a strict chain contains at most one point in each rank \(1,\ldots,h-1\).

Summing proves (2). ∎

This replaces the old \(3D^2+O(D)\) avoidance error by the linear term \((h-1)D\).

For the cube \([0,2s]^3\),

\[
M_s=3s^2+3s+1,\qquad
V_s=4s^3+\frac92s^2+\frac32s-1,
\]

and \(h=3s\). Consequently every universal word satisfies

\[
V_s\le\sum_i d_i+(3s-1)D.
\tag{3}
\]

In particular, \(D=o(s^2)\) forces

\[
\sum_i d_i\ge(4-o(1))s^3,
\]

so the selected middle witnesses must have average length at least

\[
\frac{\sum_i d_i}{M_s}\ge\left(\frac43-o(1)\right)s.
\tag{4}
\]

---

# 3. Short-run and random-order obstruction

Write

\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\]

where \(\alpha_i,\beta_i\) are nondecreasing in \([0,D]\).

Fix the coordinate increment corresponding, in centered coordinates, to \(x\ge1\). Suppose every zero-run and one-run in its incidence word on the ordered middle targets has length at most \(q\), and its support has more than \(2q\) elements.

### Theorem 4

\[
\boxed{
\sum_i d_i\le qM_s+6qD.
}
\tag{5}
\]

Hence

\[
\boxed{
V_s\le qM_s+(3s-1+6q)D.
}
\tag{6}
\]

#### Proof

For an internal positive run \([u,v]\), its neighboring middle intervals omit the increment. A legal pin must therefore lie strictly between them:

\[
r_{u-1}+2\le\ell_{v+1},
\qquad
\beta_{u-1}-\alpha_{v+1}\le v-u\le q.
\tag{7}
\]

Exclude the at most \(2q\) indices in boundary positive runs. Every other index can be assigned either its own internal positive run or an adjacent internal positive run. All relevant index spans are at most \(2q\).

For an index before its assigned run,

\[
d_i\le q+\alpha_{v+1}-\alpha_i;
\]

after the run,

\[
d_i\le q+\beta_i-\beta_{u-1};
\]

inside the run, both variation terms occur. Expanding into adjacent increments charges each \(\alpha\)- or \(\beta\)-increment at most \(2q\) times. Their total variations are each at most \(D\); the excluded boundary indices cost at most \(2qD\). This gives (5), and (6) follows from (3). ∎

For a uniformly random middle-target order, the support size is

\[
K=\frac{s(3s+1)}2,
\]

and both bit densities are at most \(3/4\). For \(q=\lceil10\log M_s\rceil\),

\[
\Pr(\text{some constant }q\text{-block})
\le2M_s(3/4)^q=o(1).
\]

Thus, with high probability, (6) gives

\[
\boxed{
D\ge\left(\frac43-o(1)\right)s^2.
}
\tag{8}
\]

Therefore random or pseudorandom low-run middle orders cannot satisfy the compact \(o(s^2)\) gate.

---

# 4. Upgraded deterministic obstructions

Combining (2) with previously audited run certificates upgrades several old \(s^{3/2}\)-scale obstructions to genuine quadratic ones.

### Aligned recursive phase order

Its audited certificate is

\[
\sum_i d_i\le s^3-s+(3s+1)D.
\]

Hence

\[
V_s\le s^3-s+6sD,
\]

so exactly

\[
\boxed{
D\ge
\frac12s^2+\frac34s+\frac5{12}-\frac1{6s}.
}
\tag{9}
\]

### Intact side-block braids

For any permutation and reversal of the intact forced side blocks, the audited assignment has \(4s+2\) omitted indices, run cost at most \(s+1\), and congestion at most \(4s+3\). Thus

\[
\sum_i d_i
\le (s+1)(M_s-4s-2)+(8s+5)D.
\]

Consequently

\[
\boxed{
D\ge
\frac{s^3+\frac52s^2+\frac72s}{11s+4}
=\left(\frac1{11}+o(1)\right)s^2.
}
\tag{10}
\]

So neither intact side braids nor maximally nested recursive phases can prove (CB).

---

# 5. Coordinate-line stability

Let \(I_s=[-s,s]\), \(n=2s+1\). Select coordinate-line levels

\[
X,Y,Z\subseteq I_s
\]

with sizes \(x,y,z\), and suppose

\[
x+y+z=n+k.
\]

Let \(U\) be the number of points of \(H_s\) uncovered by those lines.

### Theorem 5

If \(k=o(s)\) and \(U=o(s^2)\), then, after permuting coordinates,

\[
\boxed{
x=n-o(s),\qquad y+z=o(s).
}
\tag{11}
\]

#### Proof

Let \(A=I_s\setminus X\), and similarly \(B,C\). Fix \(a\in A\). Among \(b\in B\), at most \(|a|\) choices place \(-a-b\) outside \(I_s\), and at most \(z\) further choices land on a selected \(Z\)-line. Therefore

\[
U\ge\sum_{a\in A}(x-k-|a|)_+.
\tag{12}
\]

Put \(h=x-k\).

If \(1\le h\le s\), the positive weights are

\[
1,1,2,2,\ldots,h-1,h-1,h.
\]

After deleting at most \(x\) of them, at least

\[
r=(2h-1-x)_+=(x-2k-1)_+
\]

remain. Their sum is at least \(r^2/4\). Hence either \(x=o(s)\), or this case is impossible.

If \(h>s\), all \(m=n-x\) unselected levels have positive weight. The \(m\) smallest weights have sum at least

\[
m(h-s)+\frac{m^2}{4}-\frac m2.
\]

Thus \(U=o(s^2)\) forces \(m=o(s)\), i.e. \(x=n-o(s)\).

The same dichotomy holds for \(y,z\). Since their sum is \(n+o(s)\), exactly one count is \(n-o(s)\), and the other two are \(o(s)\). ∎

Hence a near-minimal family of distinct coordinate lines covering almost all of \(H_s\) cannot have positive proportions in all three directions. This rules out a genuinely rotating saturated line profile in that scope. It does **not** cover repeated use of the same line or a family with a positive linear excess in its line count.

---

# 6. Literal Helly-core factor bridge

For monotone middle intervals \(I_i=[\ell_i,r_i]\), let \(R=[u,v]\) be a maximal positive run of one coordinate increment. Define

\[
C_R=[\ell_v,r_u]\cap[r_{u-1}+1,\ell_{v+1}-1],
\]

with the natural boundary conventions.

### Theorem 6

If every \(C_R\) is nonempty, choose \(p_R\in C_R\) and place that increment at \(p_R\). Doing this for every coordinate increment yields a literal word satisfying

\[
\max_{t\in I_i}A_t=T_i
\]

for every selected middle target.

Indeed, \(p_R\) belongs to all \(I_i\) with \(i\in R\), and endpoint monotonicity places it outside every \(I_i\) with \(i\notin R\).

In offset notation, core nonemptiness is exactly

\[
\boxed{
\beta_u-\alpha_v\ge v-u,\qquad
\beta_{u-1}-\alpha_{v+1}\le v-u.
}
\tag{13}
\]

Moreover:

- if \(\bigcup_{i=u}^v I_i\) is connected, the corresponding physical interval has maximum \(\max_{u\le i\le v}T_i\);
- if \(\bigcap_{i=u}^v I_i\neq\varnothing\), the common core has maximum \(\min_{u\le i\le v}T_i\).

Thus connected join shadows and common-core meet shadows become literal contiguous-max witnesses.

Applied to the audited closed hexagonal spiral with \(I_i=[i,i+\operatorname{radius}(i)]\), this gives a word of length

\[
M_s+2s
\]

covering the entire middle and upper half and

\[
\sum_{t=1}^s3t(t+1)
=\boxed{s(s+1)(s+2)}
\]

distinct lower targets from within-side ring arcs. Deep lower targets remain uncovered.

---

# 7. Reset/slab recursion obstruction

For \(0\le r\le R\),

\[
\boxed{
w(R,R,r)
=
Rr-\left\lfloor\frac{r^2}{4}\right\rfloor
+R+\left\lfloor\frac r2\right\rfloor+1.
}
\tag{14}
\]

This follows by summing the triangular coefficients of
\((1+\cdots+z^R)^2\) over the central \(r+1\) positions.

If \(r_1+r_2=R\), then

\[
w(R,R,r_1)+w(R,R,r_2)-w(R,R,R)
=\frac12r_1r_2+O(R).
\tag{15}
\]

Therefore ordinary slab concatenation incurs \(\Theta(R^2)\) excess for every fixed-ratio split. Any recursion needs a literal seam fusion saving

\[
\frac12r_1r_2-o(R^2).
\]

This is the three-dimensional analogue of the newly reported four-box reset obstruction: both routes require a reset-free surface braid.

---

# 8. Verification of Boolean aggregation

Assume (CB). Split the Boolean coordinates into three balanced blocks and take arbitrary SCDs. A triple of chains gives a box with side heights \(p_1,p_2,p_3\). Their widths add exactly:

\[
\sum_{\text{boxes}}w(p_1,p_2,p_3)
=\binom{k}{\lfloor k/2\rfloor}=W(k).
\tag{16}
\]

Put \(R=\sqrt{k}\). The number of boxes is

\[
B=\Theta(W(k)/k)=\Theta(W(k)/R^2).
\tag{17}
\]

The SCD height distribution satisfies Gaussian moment and tail estimates

\[
\sum_C(1+p(C))^j=O(B_s s^{j/2}),\qquad j=0,1,2,
\]

and

\[
\sum_{p(C)>CR}(1+p(C))^j
=O(B_sR^j e^{-cC^2}).
\]

The explicit slice word gives

\[
g_3(p,q,r)+1\le(\min\{p,q,r\}+1)(1+p+q+r).
\]

Consequently:

- boxes with a side below \(\delta R\) have total full cost

  \[
  O(\delta W(k))+O(W(k)/R);
  \]

- boxes with a side above \(CR\) have total full cost

  \[
  O(e^{-cC^2}W(k));
  \]

- compact boxes contribute their widths plus

  \[
  o(R^2)B=o(W(k)).
  \]

One common-minimum anchor per box costs

\[
O(B)=O(W(k)/k).
\]

Thus

\[
\nu(k)\le W(k)
+O(\delta W(k))
+O(e^{-cC^2}W(k))
+o(W(k)).
\]

First let \(k\to\infty\) for fixed \(\delta,C\), then let \(\delta\downarrow0\) and \(C\uparrow\infty\). Together with \(\nu(k)\ge W(k)\), this proves the conjectured asymptotic **conditionally on (RAY)**.

---

# 9. Integration of the exact-factor fixed-window reduction

This remains a separate sufficient route.

For fixed \(A\), on \(q\le A\sqrt m\),

\[
\log\frac W{N_q}=\frac{q^2}{m}+O_A(m^{-1/2}),
\]

so

\[
1\le c_q\le C_A.
\]

It is sufficient to prove, using one exact factor and one common integral nested resolution,

\[
\sum_{q\le A\sqrt m}\frac{e_q(F_m,P_m)}{c_q}=o(W)
\tag{\(\mathrm{CA}_A\)}
\]

for every fixed \(A\). A slow diagonal \(A=A(m)\to\infty\) then gives the moving-window synchronization theorem. Independently selected depthwise quotas are invalid: the \(n=9\) example has demand \(8\cdot4=32\) on pairs containing one fixed point but only \(28\) parent triples of quota one.

The factor-independent deep tail is safe whenever

\[
\boxed{
\frac{Q^2}{m}
\ge\frac12\log m-\frac12\log\log m+\omega(1).
}
\tag{18}
\]

Indeed,

\[
\sum_{q\ge Q}\frac{O_q}{c_q}
\le
O\!\left(
W\frac mQ e^{-Q^2/m+o(1)}
\right)=o(W).
\]

In particular, \(Q=\alpha\sqrt{m\log m}\) is safe for every fixed \(\alpha>1/\sqrt2\). I do not use the ambiguous notation
\((1/\sqrt2+o(1))\sqrt{m\log m}\).

Nothing in the three-box argument constructs \((F_m,P_m)\), and no fractional or separate-depth substitute is being claimed.

---

# 10. Exact unresolved lemmas

The smallest positive local target is:

\[
\boxed{\text{(RAY) for every primitive positive integer triple.}}
\]

A more structural sufficient version is the following **unproved fragmented Helly-braid lemma**:

> Construct, on every compact ray, a middle order and monotone interval band with \(D=o(R^2)\), every coordinate-run core \(C_R\) nonempty, connected upper join shadows, common-core lower meet shadows, and literal witnesses for every target.

All intact, random, slice-sweep, and canonically phased versions are ruled out above.

The smallest negative-route lemma is also unproved:

> Every ordering of \(H_s\) admits an \(O(s)\)-congestion heterogeneous internal-run assignment of total cost at most
> \[
> (4-\varepsilon)s^3.
> \]

Together with (2), this would force \(D=\Omega(s^2)\) for every order and disprove the three-box route. The best universal mesh theorem only guarantees a nearby run within \(3s+O(1)\), producing leading cost \(9s^3\). A hypothetical \(4s^3\)-saturated fragmented profile remains at the exact barrier.

The exact-factor alternative remains the unproved common-ownership theorem \((\mathrm{CA}_A)\).

---

## Adversarial audit

- The face-extension and raywise reduction were independently checked, including floors, finite-ray uniformity, width monotonicity, and order of limits.
- The start-chain lemma was independently re-audited after one auditor initially used the obsolete \(3D^2\) ledger. The corrected random-order conclusion \(D\ge(4/3-o(1))s^2\) passed.
- The coordinate-line stability proof was independently checked in both regimes \(x-k\le s\) and \(x-k>s\).
- The Helly-core conditions are sufficient, not necessary; multiple pins can factor a run even when its single common core is empty.
- The line-cover stability theorem applies to distinct near-minimal line families. It does not by itself exclude repeated-line fragmented profiles.
- The architecture-specific quadratic bounds do not imply an order-independent quadratic lower bound.
- No finite or computational search was used.

Thus the stable advance is a sharper reduction and a broad family of rigorous compact-scale obstructions, not a proof of the conjecture.

---

## Audit correction: precise scope addendum

1. **RAY gcd reduction.** In the compact-mesh proof, write

   \[
   (a,b,c)=d(a',b',c'),\qquad \gcd(a',b',c')=1.
   \]

   The inner box is

   \[
   (a'hd,b'hd,c'hd).
   \]

   For fixed mesh parameter \(L\), only finitely many primitive triples and gcds occur, while \(hd\to\infty\). Thus RAY gives

   \[
   g_3(ah,bh,ch)-w(ah,bh,ch)=o_L(R^2).
   \]

   Also \(g_3\ge w\) by the width-antichain lower bound, so the normalized excess is nonnegative. This completes the stated equivalence between compact CB and primitive RAY.

2. **Random-order scope.** The random theorem uses one fixed threshold whose support and complement densities are at most \(\rho<1\). For \(B\) such thresholds,

   \[
   \Pr(\text{some monochromatic \(q\)-block})
   \le 2BM\rho^q.
   \]

   One balanced threshold already proves the quadratic random-order obstruction. The statement is not uniform over extreme increments, whose densities approach \(0\) or \(1\).

3. **Coordinate-line stability.** In its proof, with \(h=x-k\), the omitted trivial regime is:

   \[
   h\le0\quad\Longrightarrow\quad x\le k=o(s).
   \]

   The remaining cases \(1\le h\le s\) and \(h>s\) give respectively \(x=o(s)\) or \(x=n-o(s)\), as stated.

4. **Helly-core scope.** For a positive run \(R=[u,v]\),

   \[
   C_R=[\ell_v,r_u]\cap[r_{u-1}+1,\ell_{v+1}-1]
   \]

   is nonempty exactly when that entire run can be served by one common pin avoiding the neighboring negative intervals. Hence the Helly-core inequalities exactly characterize the **one-common-pin-per-run realization**. They are sufficient, but not necessary, for general factorability: multiple pins may serve different intervals in the same run even when \(C_R=\varnothing\).

   The spiral coverage claims additionally use the previously audited closed-spiral geometry and its factorable radius band; the new contribution is only the common-core-to-literal-maximum bridge.

5. **Slab obstruction scope.** The width identity and quadratic cross-term show that additive two-slab concatenation, or a recursion that resets independently in each child slab, pays

   \[
   \frac12r_1r_2+O(R).
   \]

   This does not obstruct arbitrary recursion. A recursion with cross-seam witnesses may recover that term; the exact missing ingredient is a literal fusion saving of

   \[
   \frac12r_1r_2-o(R^2).
   \]

Finally, the multipin short-run theorem remains unchanged and requires no common-pin hypothesis.
