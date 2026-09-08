# Mathematical attack G: balanced three-box braids

## 0. Verdict and strongest result

Let

\[
P(p,q,r)=[0,p]\times[0,q]\times[0,r].
\]

In range-maximum normal form, a word is a sequence of nonzero triples in
this box, and it is universal if every nonzero triple is the componentwise
maximum of a contiguous interval. Write \(g_3(p,q,r)\) for the minimum
length of such a word and \(w_3(p,q,r)\) for the width of the product of the
three chains.

Throughout, the elementary width lower bound

\[
g_3(p,q,r)\ge w_3(p,q,r)
\tag{0.0}
\]

is used. To see it, choose witnesses for a largest antichain of targets. If
one witnessing interval contained another, its maximum would dominate the
other target, which is impossible inside an antichain. Thus the selected
physical intervals form a containment antichain. Such a family on an
\(n\)-position line has size at most \(n\): two members cannot have the same
left endpoint, since then one would contain the other.

**Post-audit correction.** The compact balanced three-box theorem is
**false**. An independently audited architecture-free lower bound from
MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md gives a positive quadratic
excess on every ray \(0<a<b,\ c>2b\). The earlier status “open” is
superseded. The structural reductions below remain correct, but their
cofinal axial branch is now proved impossible.

Precisely, for fixed \(0<a<b,\ c>2b\),

\[
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge\frac{ab(c-2b)}{c+5a+5b}>0.
\tag{0.A}
\]

For \(C\ge2\), let

\[
\mathrm{AX}_C:\qquad
g_3(t,t,Ct)=(t+1)^2+o_C(t^2).
\]

Let \(\mathrm{AX}_\infty\) mean that \(\mathrm{AX}_C\) holds for every \(C\)
in some unbounded set of positive integers. Let \(\mathrm{TRI}\) mean

\[
g_3(at,bt,ct)=w_3(at,bt,ct)+o_{a,b,c}(t^2)
\tag{TRI}
\]

for every primitive integer triple

\[
0<a\le b\le c<a+b.
\]

The main reduction proved below is

\[
\boxed{
\mathrm{CB}
\quad\Longleftrightarrow\quad
\mathrm{TRI}+\mathrm{AX}_\infty .
}
\tag{0.1}
\]

Moreover,

\[
\boxed{
\mathrm{AX}_\infty
\quad\Longleftrightarrow\quad
\exists\,L(t)\in\mathbb N,\ L(t)\to\infty:
g_3(t,t,L(t)t)=(t+1)^2+o(t^2).
}
\tag{0.2}
\]

Thus the entire plateau sector, and hence the inherited dominant-ray lemma
DRAY, compresses to one moving axial family. The compression is logically
equivalent to DRAY. The audited lower bound proves that both formulations
fail. The strict-triangle sector, including the cube, remains unresolved,
but the full compact statement already fails in the plateau sector.

The other unconditional advances are:

1. an exact width formula for every sorted three-box;
2. an exact width-additive plateau slab semigroup;
3. the transfer of (0.A) to sharp explicit axial lower bounds;
4. a proof that the same semigroup pays a quadratic reset toll in the
   strict-triangle interior;
5. a rectangular priority-shell braid improving the standard hook word near
   the diagonal; and
6. an exact corridor-overlap ledger showing that any near-width layer braid
   must reuse a quadratic amount of physical corridor across different max
   levels.

All lower obstructions below are stated with their scopes. Theorem 3.0 is
architecture-free in the dominant plateau cone; no corresponding
architecture-free quadratic bound is asserted for the cube.

---

## 1. Exact width and hereditary restriction

### Theorem 1.1 (exact width formula)

Suppose

\[
0\le p\le q\le r,
\qquad
d=(p+q-r)_+.
\]

Then

\[
\boxed{
w_3(p,q,r)
=(p+1)(q+1)-\left\lfloor\frac{(d+1)^2}{4}\right\rfloor .
}
\tag{1.1}
\]

#### Proof

A product of two finite chains has the standard hook symmetric-chain
decomposition. Taking the product of each hook with the third chain and
hook-decomposing that rectangle gives a symmetric-chain decomposition of
\(P(p,q,r)\). Hence its width is the size of a middle rank.

If \(d=0\), then \(r\ge p+q\). At a middle rank, every pair
\((x,y)\in[0,p]\times[0,q]\) determines a legal value of \(z\), so the width
is \((p+1)(q+1)\).

Now suppose \(d>0\). Since \(r\ge q\), one has \(d\le p\). Put

\[
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor
=p+q-\left\lceil\frac d2\right\rceil .
\]

Parametrize rank \(h\) by \((x,y)\), with \(z=h-x-y\). Begin with all
\((p+1)(q+1)\) pairs. The condition \(z<0\) deletes

\[
\binom{\lceil d/2\rceil+1}{2}
\]

pairs from the upper-right corner, after applying
\((x,y)\mapsto(p-x,q-y)\). The condition \(z>r\) deletes

\[
\binom{\lfloor d/2\rfloor+1}{2}
\]

pairs from the lower-left corner. The bound \(d\le p\le q\) ensures that
neither triangular count is truncated by a side of the rectangle. Finally,

\[
\binom{\lceil d/2\rceil+1}{2}
+\binom{\lfloor d/2\rfloor+1}{2}
=\left\lfloor\frac{(d+1)^2}{4}\right\rfloor .
\]

This proves (1.1). \(\square\)

The plateau \(r\ge p+q\) is therefore exactly the sector in which

\[
w_3(p,q,r)=(p+1)(q+1).
\tag{1.2}
\]

### Lemma 1.2 (exact clamping)

If \(p'\le p,\ q'\le q,\ r'\le r\), then

\[
\boxed{g_3(p',q',r')\le g_3(p,q,r).}
\tag{1.3}
\]

#### Proof

Clamp every word entry coordinatewise to the smaller box. If an interval
originally witnesses a target \(T\in P(p',q',r')\), every entry of that
interval is coordinatewise at most \(T\). Thus clamping fixes the entire
witness interval. Delete any entries that clamp to zero. No such entry can
lie in a nonzero target's fixed witness, so the surviving witness remains
contiguous. \(\square\)

This hereditary fact is stronger than face extension in the direction in
which it applies: a large-box word supplies every coordinatewise smaller
box without any added positions.

### Corollary 1.3 (the exact plateau collar)

For \(p\le q\le r\le p+q\), put \(d=p+q-r\). Then

\[
\begin{aligned}
g_3(p,q,r)-w_3(p,q,r)
\le{}&g_3(p,q,p+q)-(p+1)(q+1)\\
&+\left\lfloor\frac{(d+1)^2}{4}\right\rfloor .
\end{aligned}
\tag{1.4}
\]

Indeed, clamp a word for \((p,q,p+q)\) and use (1.1). Consequently, a
near-width plateau construction automatically settles every collar with
\(d=o(R)\). Uniformly for \(d\le\varepsilon R\), the additional normalized
loss is at most \(\varepsilon^2/4+o(1)\).

---

## 2. Exact plateau slabs

The next lemma is the central positive fusion statement.

### Lemma 2.1 (translated slab concatenation)

Partition the integer \(x\)-levels into consecutive intervals
\(I_1,\ldots,I_I\) of heights \(p_1,\ldots,p_I\), and the \(y\)-levels into
consecutive intervals \(J_1,\ldots,J_J\) of heights \(q_1,\ldots,q_J\).
Thus

\[
\sum_i(p_i+1)=p+1,
\qquad
\sum_j(q_j+1)=q+1.
\]

Then

\[
\boxed{
g_3(p,q,r)
\le IJ-1+\sum_{i=1}^{I}\sum_{j=1}^{J}g_3(p_i,q_j,r).
}
\tag{2.1}
\]

If \(r\ge p+q\), this partition is exactly width-additive:

\[
\boxed{
\sum_{i,j}w_3(p_i,q_j,r)=w_3(p,q,r).
}
\tag{2.2}
\]

#### Proof

The translated boxes

\[
I_i\times J_j\times[0,r]
\]

partition the parent box. Coordinatewise translation preserves every local
maximum witness. A local word omits its local zero; after translation that
point is the child origin. Prepend that origin once for every child except
the child containing the global origin. Concatenate the child blocks.
Every parent target is covered inside its unique child block, proving (2.1).

If \(r\ge p+q\), then every child is also plateau. By (1.2),

\[
\sum_{i,j}w_3(p_i,q_j,r)
=\sum_{i,j}(p_i+1)(q_j+1)
=(p+1)(q+1)=w_3(p,q,r).
\]

The only concatenation charge is the displayed \(IJ-1\) literal origins;
there is no hidden separator. \(\square\)

### Theorem 2.2 (axial compression of every plateau ray)

Fix \(C\ge2\), and assume \(\mathrm{AX}_C\). For every fixed pair of positive
integers \(a,b\) satisfying \(C\ge a+b\),

\[
\boxed{
g_3(at,bt,Ct)=(at+1)(bt+1)+o_{a,b,C}(t^2).
}
\tag{2.3}
\]

#### Proof

Partition the \(at+1\) \(x\)-levels into \(a\) consecutive slabs: one has
height \(t\), and the other \(a-1\) have height \(t-1\), since

\[
(t+1)+(a-1)t=at+1.
\]

Do the same for the \(bt+1\) \(y\)-levels. The \(ab\) children have shapes

\[
(t-\varepsilon_i,t-\delta_j,Ct),
\qquad
\varepsilon_i,\delta_j\in\{0,1\}.
\]

Clamp an \(\mathrm{AX}_C\) word in one or both short coordinates. For each
of the four child types,

\[
\begin{aligned}
g_3(t-\varepsilon_i,t-\delta_j,Ct)
&\le (t+1)^2+o_C(t^2)\\
&=(t+1-\varepsilon_i)(t+1-\delta_j)+o_C(t^2),
\end{aligned}
\]

because the omitted difference is only \(O(t)\). Lemma 2.1 and exact width
additivity now give

\[
g_3(at,bt,Ct)
\le (at+1)(bt+1)+o_{a,b,C}(t^2).
\]

The width lower bound gives the reverse inequality. \(\square\)

### Theorem 2.3 (cofinal axial equivalence)

The following are equivalent.

1. RAY holds on every primitive plateau ray \(0<a\le b\le c\) with
   \(c\ge a+b\).
2. \(\mathrm{AX}_C\) holds for \(C\) in some unbounded set
   \(\mathcal C\subseteq\{2,3,\ldots\}\).
3. There is an integer function \(L(t)\to\infty\) such that

   \[
   g_3(t,t,L(t)t)=(t+1)^2+o(t^2).
   \tag{2.4}
   \]

#### Proof

The first statement trivially implies \(\mathrm{AX}_C\) for every fixed
\(C\ge2\).

Assume the second statement, and fix a plateau ray \((a,b,c)\). Choose one
fixed

\[
C\in\mathcal C,
\qquad
C\ge\max\{c,a+b\}.
\]

Theorem 2.2 settles \((a,b,C)\). Clamp its long coordinate to \(ct\). The
two widths are both \((at+1)(bt+1)\), so RAY holds for \((a,b,c)\). Notice
that \(C\) is fixed before \(t\to\infty\); no uniformity across \(C\) is used.

For the equivalence with (2.4), choose an increasing sequence
\(C_j\in\mathcal C\). For each \(j\), the fixed-\(C_j\) error is eventually
at most \(t^2/j\). Choose increasing thresholds and set \(L(t)=C_j\) between
successive thresholds. This slow diagonalization proves (2.4).

Conversely, fix \(C\). For all sufficiently large \(t\), \(L(t)\ge C\).
Clamp (2.4) to \((t,t,Ct)\). Both widths equal \((t+1)^2\), proving
\(\mathrm{AX}_C\). \(\square\)

This is an exact structural compression: all two-parameter plateau aspect
ratios reduce to a single slowly moving long-axis family. Theorem 3.0 below
shows that this formerly positive target is quantitatively impossible.

---

## 3. Relation to DRAY and to the full compact theorem

### Theorem 3.0 (audited architecture-free plateau obstruction)

Let \(0<p<q\), \(r>p+q\), and put

\[
M=(p+1)(q+1),\qquad
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,\qquad
\epsilon=p+q+r-2h,
\]

\[
s_0=p+q+2,\qquad
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\]

and, when \(K\ge2\),

\[
B=s_0+\left\lceil\frac{M-Ks_0}{K}\right\rceil .
\]

Every range-maximum word of length \(N=M+D\) satisfies

\[
\boxed{
D\ge
\frac{M\bigl((r-\epsilon)/2-q\bigr)-1}
     {h-1+2B}
}
\tag{3.0}
\]

whenever the numerator is positive.

Consequently, for every fixed \(0<a<b,\ c>2b\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\tag{3.0a}
\]

#### Independent audit

The four vulnerable implications all pass.

1. Choose one witness \(I_i=[\ell_i,r_i]\) for each of the \(M\) targets
   in the full middle rank and order by increasing \(\ell_i\). Equal starts,
   or a later start with an earlier end, would make two same-rank maxima
   comparable. Hence

   \[
   \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
   \]

   with nondecreasing \(\alpha_i,\beta_i\in[0,D]\). If
   \(d_i=r_i-\ell_i\), the exact lower-rank count and start-capacity bound
   are

   \[
   L_{<h}=M\frac{r-\epsilon}{2}-1,
   \qquad
   L_{<h}\le\sum_i d_i+(h-1)D.
   \tag{3.0b}
   \]

2. Every order of \(p+q+2\) distinct middle-rank points has an internal
   positive coordinate-threshold run \([u,v]\) with \(v-u\le q\).
   Otherwise all three coordinate sequences are valleys. Ordering their
   turn positions and using constant sum forces at most \(p+q+1\) points.
   Taking a maximum-level plateau inside a forced run makes it short while
   preserving both negative neighbors.

3. For such a run, choose one physical occurrence in \(I_u\) attaining the
   positive threshold. It lies in neither negative-neighbor witness.
   Strict endpoint order therefore gives

   \[
   r_{u-1}+2\le\ell_{v+1},
   \qquad
   \beta_{u-1}-\alpha_{v+1}\le v-u\le q.
   \tag{3.0c}
   \]

   This uses one literal pin only; repeated occurrences and different pins
   for different positive witnesses do not affect it.

4. Partition the middle order into the \(K\) balanced blocks and pair
   consecutive blocks. Cross-assign the indices of each block to the short
   run in its partner. Monotonicity gives

   \[
   \sum_i d_i\le qM+2BD.
   \tag{3.0d}
   \]

   The \(\alpha\)- and \(\beta\)-increments charged by different block pairs
   lie on disjoint index spans, so each total charge is at most \(D\).

Combining (3.0b) and (3.0d) proves (3.0). On
\((p,q,r)=(at,bt,ct)\), one has

\[
\frac{M}{t^2}\to ab,\qquad
\frac ht\to\frac{a+b+c}{2},\qquad
\frac Bt\to a+b,
\]

which proves (3.0a). No ordered-factor, common-pin, or special braid
assumption occurs.

### Corollary 3.0A (the axial replacement is quantitatively impossible)

For every fixed integer \(C>4\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(t,t,Ct)-(t+1)^2}{t^2}
\ge\frac{C-4}{C+15}>0.
}
\tag{3.0e}
\]

More strongly, for every integer function \(L(t)\to\infty\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(t,t,L(t)t)-(t+1)^2}{t^2}\ge1.
}
\tag{3.0f}
\]

#### Proof

Apply Lemma 2.1 to split the \(2t+1\) \(y\)-levels of
\(P(t,2t,r)\) into slabs of heights \(t\) and \(t-1\), and clamp the
second child:

\[
g_3(t,2t,r)\le1+g_3(t,t,r)+g_3(t,t-1,r)
\le1+2g_3(t,t,r).
\tag{3.0g}
\]

Let

\[
E(t,r)=g_3(t,t,r)-(t+1)^2.
\]

If \(D_2=g_3(t,2t,r)-(t+1)(2t+1)\), then (3.0g) gives

\[
D_2\le2E(t,r)+t+2.
\tag{3.0h}
\]

Use (3.0) with \(p=t,q=2t\). For fixed \(r=Ct\),

\[
\liminf\frac{D_2}{t^2}\ge\frac{2(C-4)}{C+15},
\]

and (3.0e) follows from (3.0h).

For \(r=L(t)t\), the finite bound is uniform in the changing long side:

\[
M=2t^2+O(t),\qquad B=3t+O(1),
\]

while

\[
h=\frac{(L(t)+3)t}{2}+O(1).
\]

Substitution in (3.0) gives

\[
\frac{D_2}{t^2}
\ge
2\,\frac{L(t)-4-O(1/t)}{L(t)+15+O(1/t)}
=2-o(1).
\]

Here the one-sided estimate uses \(M/t^2\ge2\); this avoids introducing an
artificial \(O(L(t)/t)\) error by expanding that multiplicative factor.
Equation (3.0h) proves (3.0f). \(\square\)

The inherited dominant-ray lemma DRAY asks for RAY on every primitive

\[
0<a<b,
\qquad
c>2b.
\]

### Proposition 3.1

DRAY is equivalent to \(\mathrm{AX}_\infty\).

#### Proof

By Theorem 2.3, \(\mathrm{AX}_\infty\) gives every plateau ray and therefore
DRAY.

Conversely, fix an integer \(C\ge3\) and an integer \(L\ge2\). The triple

\[
(L-1,L,CL)
\]

is primitive and belongs to DRAY. At scale \(s\), extend the first side by
\(s\). The exact face-extension bound gives

\[
\begin{aligned}
g_3(Ls,Ls,CLs)
\le{}&g_3((L-1)s,Ls,CLs)\\
&+s\bigl((C+1)Ls+1\bigr).
\end{aligned}
\]

The small and large plateau widths differ by

\[
((L-1)s+1)(Ls+1)-(Ls+1)^2=-Ls^2-s.
\]

Hence, with \(T=Ls\),

\[
\limsup_{s\to\infty}
\frac{g_3(T,T,CT)-(T+1)^2}{T^2}
\le\frac CL.
\tag{3.1}
\]

The multiples of \(L\) have successive ratio tending to one. Extending a
multiple \(T_0\le T<T_0+L\) to \(T\) in all three coordinates costs only
\(O_{C,L}(T)\), so (3.1) holds for the full limsup over \(T\). Letting
\(L\to\infty\) proves \(\mathrm{AX}_C\). Thus DRAY gives
\(\mathrm{AX}_C\) for every \(C\ge3\). \(\square\)

The equivalence is a genuine compression of the family of shapes, but it is
not a logical weakening of DRAY. Theorem 3.0 and Corollary 3.0A now show
that both equivalent statements are false.

For completeness, the face-extension inequality used above is

\[
\begin{aligned}
g_3(p,q,r)\le g_3(p_0,q_0,r_0)
&+(p-p_0)(q+r+1)\\
&+(q-q_0)(p_0+r+1)\\
&+(r-r_0)(p_0+q_0+1).
\end{aligned}
\tag{3.2}
\]

It follows by appending, on every new coordinate face, the two-dimensional
L-shaped word

\[
(a,0),(a-1,0),\ldots,(0,0),(0,1),\ldots,(0,b).
\]

### Theorem 3.2 (exact ray decomposition)

The compact estimate

\[
\sup_{\delta R\le p,q,r\le CR}
\frac{g_3(p,q,r)-w_3(p,q,r)}{R^2}\longrightarrow0
\tag{CB}
\]

for every fixed \(0<\delta<C\) is equivalent to

\[
\boxed{\mathrm{TRI}+\mathrm{AX}_\infty.}
\tag{3.3}
\]

#### Proof

The audited raywise reduction is recalled briefly. CB immediately implies
RAY on each fixed primitive positive integer ray. Conversely, fix a mesh
parameter \(L>2/\delta\), put \(h=\lfloor R/L\rfloor\), and round each side down
to an integral multiple of \(h\). For fixed \(L\), only finitely many
primitive aspect ratios occur. Divide each rounded triple by its gcd and
absorb that gcd into the scale. RAY is therefore uniform over this finite
set. Equation (3.2) restores the discarded faces at cost
\(O_C(R^2/L)\). Width is coordinatewise monotone, so first
\(R\to\infty\) and then \(L\to\infty\) gives CB.

After sorting a primitive ray, exactly one of \(c<a+b\) and \(c\ge a+b\)
holds. TRI covers the first class, while Theorem 2.3 says that
\(\mathrm{AX}_\infty\) is equivalent to RAY on the second class. \(\square\)

Before Theorem 3.0 was available, the exact positive target was the pair

\[
\boxed{
\begin{array}{l}
\text{TRI on every primitive strict-triangle ray, and}\\[2mm]
\text{one moving axial construction (2.4).}
\end{array}}
\tag{3.4}
\]

The second line is now rigorously impossible by (3.0f). Therefore CB is
false, independently of the unresolved status of TRI. The former
four-block dominant-ray route to the Boolean conjecture is also closed.
This does **not** refute the Boolean contiguous-OR conjecture; it removes
that sufficient local route.

---

## 4. Why the plateau semigroup stops at the triangle sector

The width additivity in Lemma 2.1 is special to \(p+q\le r\).

### Proposition 4.1 (exact two-slab reset ledger)

Suppose \(p\le q\le r<p+q\). Put

\[
u=p+q-r>0,
\qquad
D=r-q,
\]

so \(u=p-D\). Split the \(p+1\) \(x\)-levels into two consecutive slabs of
heights \(p_1,p_2\), where

\[
p_1+p_2=p-1.
\]

Then

\[
\boxed{
\begin{aligned}
&w_3(p_1,q,r)+w_3(p_2,q,r)-w_3(p,q,r)\\
&\quad=
\left\lfloor\frac{(u+1)^2}{4}\right\rfloor
-\sum_{i=1}^2
\left\lfloor
\frac{\bigl((p_i-D)_++1\bigr)^2}{4}
\right\rfloor .
\end{aligned}}
\tag{4.1}
\]

On any compact scale on which \(p,q,r\le CR\) and

\[
u\ge\eta R,
\qquad
p_i+1\ge\eta R
\quad(i=1,2),
\tag{4.2}
\]

the right side is at least

\[
\kappa_{\eta,C}R^2-O_C(R)
\tag{4.3}
\]

for some \(\kappa_{\eta,C}>0\).

#### Proof

The base terms \((p_i+1)(q+1)\) in (1.1) add exactly to the parent's base
term. The child defects are

\[
(p_i+q-r)_+=(p_i-D)_+,
\]

which proves (4.1).

Put \(\ell_i=p_i+1\). Then

\[
(p_1-D)_+=(u-\ell_2)_+,
\qquad
(p_2-D)_+=(u-\ell_1)_+.
\]

Ignoring \(O(R)\) parity terms, four times the width reset is

\[
F=u^2-(u-\ell_1)_+^2-(u-\ell_2)_+^2.
\tag{4.4}
\]

This is positive whenever \(u,\ell_1,\ell_2>0\) and
\(u\le\ell_1+\ell_2\). If neither positive part occurs this is immediate;
if exactly one occurs, \(F=2u\ell-\ell^2>0\); if both occur, their sum is
strictly below \(u\), so the sum of their squares is below \(u^2\). Under
(4.2) and compact upper bounds, normalization by \(R\) leaves a compact set
away from the zero cases. Its minimum is a positive
\(\kappa_{\eta,C}\). Restoring the floors changes the result by \(O_C(R)\).
\(\square\)

Thus an independent macroscopic slab reset pays \(\Omega(R^2)\) throughout
the strict-triangle interior. The toll can disappear only as the triangle
defect tends to zero or one slab becomes negligible. This exactly matches
the positive collar in Corollary 1.3. A successful strict-triangle proof
must fuse witnesses across slab boundaries; independent child resets cannot
prove CB.

---

## 5. A rectangular priority-shell braid

The next construction generalizes the literal cubic triangular-shell word.

### Theorem 5.1

For \(1\le p\le q\le r\),

\[
\boxed{
g_3(p,q,r)
\le pq+pr+qr-p^2-\binom q2+p+r-\mathbf 1_{\{q\ge2\}}.
}
\tag{5.1}
\]

#### Construction

For \(1\le t\le p\), use the closed block

\[
\begin{aligned}
C_t={}&(t,0,0),(t-1,1,0),\ldots,(0,t,0),\\
 &(0,t-1,1),\ldots,(0,0,t),\\
 &(1,0,t-1),\ldots,(t,0,0).
\end{aligned}
\tag{5.2}
\]

It has length \(3t+1\). For \(p<t\le q\), use

\[
\begin{aligned}
D_t={}&(p,t-p,0),(p-1,t-p+1,0),\ldots,(0,t,0),\\
 &(0,t-1,1),\ldots,(0,0,t),\\
 &(1,0,t-1),\ldots,(p,0,t-p),
\end{aligned}
\tag{5.3}
\]

of length \(t+2p+1\). For \(q<t\le r\), use

\[
\begin{aligned}
E_t={}&(0,q,t-q),(0,q-1,t-q+1),\ldots,(0,0,t),\\
 &(1,0,t-1),\ldots,(p,0,t-p),
\end{aligned}
\tag{5.4}
\]

of length \(p+q+1\). Concatenate the blocks in increasing \(t\).

#### Coverage proof

Given \((x,y,z)\ne0\), put \(t=\max(x,y,z)\), and resolve ties in the
following order.

If \(y=t\), the interval from

\[
(x,t-x,0)
\quad\text{through }(0,t,0)\quad\text{to}\quad
(0,t-z,z)
\]

lies in \(C_t\) or \(D_t\) and has maximum \((x,t,z)\).

If \(y<t\) and \(z=t\), the interval from

\[
(0,y,t-y)
\quad\text{through }(0,0,t)\quad\text{to}\quad
(x,0,t-x)
\]

lies in \(C_t,D_t\), or \(E_t\) and has maximum \((x,y,t)\).

Otherwise \(x=t\) and \(y,z<t\), so \(t\le p\). For \(t\ge2\), begin in
the suffix of \(C_{t-1}\) at

\[
(t-1-z,0,z),
\]

cross the seam from the terminal \((t-1,0,0)\) to the initial
\((t,0,0)\) of \(C_t\), and stop at

\[
(t-y,y,0).
\]

The maximum is \((t,y,z)\). For \(t=1\), the only remaining target is
\((1,0,0)\), which occurs literally.

The unshortened length is

\[
\begin{aligned}
&\sum_{t=1}^{p}(3t+1)
+\sum_{t=p+1}^{q}(t+2p+1)
+\sum_{t=q+1}^{r}(p+q+1)\\
&\qquad=pq+pr+qr-p^2-\binom q2+p+r.
\end{aligned}
\tag{5.5}
\]

When \(q\ge2\), replace \(C_1\) by

\[
(0,1,0),(0,0,1),(1,0,0).
\]

Its contiguous intervals cover every max-one target except \((1,1,0)\).
That missing target occurs literally in \(C_2\) if \(p\ge2\), and at the
initial point of \(D_2\) if \(p=1\). This saves one position and proves
(5.1). \(\square\)

On the cube, for \(R\ge2\), this gives

\[
g_3(R,R,R)
\le\frac{3R(R+1)}2+R-1
=2w_3(R,R,R)-\left\lfloor\frac R2\right\rfloor-3.
\tag{5.6}
\]

Thus the braid is reset-free and is a strict quadratic improvement over the
standard hook word near the diagonal, but it is still asymptotically twice
the width on the cube. In the long-axis sector it should be compared with
the minimum of this bound and the hook bound; (5.1) by itself is not an
axial near-width construction.

---

## 6. Exact boundary-corridor overlap forced on any layer braid

The factor two in the literal shell word is not merely an inefficient tour
inside disjoint max-level corridors.

### Theorem 6.1 (arm-corridor overlap ledger)

Let \(W=(v_1,\ldots,v_n)\) be any universal word for \([0,R]^3\). For each
\(1\le t\le R\), select witnesses for the \(3t\) targets

\[
\begin{aligned}
A_{t,i}&=(i,t,0),&1\le i\le t,\\
B_{t,j}&=(0,j,t),&1\le j\le t,\\
C_{t,k}&=(t,0,k),&1\le k\le t.
\end{aligned}
\tag{6.1}
\]

Let \(J_t\) be any physical interval containing all these selected witness
intervals. Then

\[
\boxed{|J_t|\ge3t.}
\tag{6.2}
\]

If

\[
d(s)=|\{t:s\in J_t\}|,
\]

then

\[
\boxed{
\sum_{s=1}^{n}d(s)=\sum_{t=1}^{R}|J_t|
\ge\frac{3R(R+1)}2.
}
\tag{6.3}
\]

#### Proof

An \(A_{t,i}\)-witness contains a position whose first coordinate is \(i>0\);
because the target's third coordinate is zero, that position has third
coordinate zero. Call it \(u_{t,i}\). A \(B_{t,j}\)-witness contains a
position \(v_{t,j}\) with second coordinate \(j>0\) and first coordinate
zero. A \(C_{t,k}\)-witness contains a position \(w_{t,k}\) with third
coordinate \(k>0\) and second coordinate zero.

Positions inside each family are distinct because their pinned positive
levels differ. The three families are pairwise disjoint: \(u\ne v\) by the
first coordinate, \(v\ne w\) by the second, and \(w\ne u\) by the third.
All \(3t\) positions lie in \(J_t\), proving (6.2). Summing interval lengths
proves (6.3). \(\square\)

Two consequences are immediate.

1. If the corridors \(J_t\) are pairwise disjoint, then

   \[
   n\ge\frac{3R(R+1)}2=2w_3(R,R,R)-O(R).
   \tag{6.4}
   \]

2. If \(n=w_3(R,R,R)+o(R^2)\), then

   \[
   \frac1n\sum_s d(s)\ge2-o(1),
   \tag{6.5}
   \]

   and

   \[
   \sum_s(d(s)-1)_+
   \ge\frac{3R(R+1)}2-n
   =\left(\frac34-o(1)\right)R^2.
   \tag{6.6}
   \]

Thus every near-width layer braid must reuse a quadratic amount of physical
corridor across different max levels, already for these three elementary
boundary-arm families. The theorem does **not** prohibit such overlap; it
identifies it as the exact surviving escape.

---

## 7. Universal endpoint geometry and the dual obstruction audit

There is a useful universal gate on any proposed witness system, but it does
not yet force quadratic excess.

### Lemma 7.1 (ordered orthogonal endpoint gate)

Choose one witnessing interval \(I_X=[\ell_X,r_X]\) for every target \(X\).
Partition targets by common left endpoint into classes \(\mathcal L\), and by
common right endpoint into classes \(\mathcal R\). Then:

1. every class in \(\mathcal L\) and \(\mathcal R\) is a chain of targets;
2. an \(\mathcal L\)-class and an \(\mathcal R\)-class meet in at most one
   target; and
3. the precedence digraphs forced on the opposite endpoint classes are
   acyclic.

More explicitly, inside a fixed-left class, \(X<Y\) forces
\(r_X<r_Y\), so orient \(R(X)\to R(Y)\). Inside a fixed-right class,
\(X<Y\) forces \(\ell_Y<\ell_X\), so orient \(L(Y)\to L(X)\). Both digraphs
are acyclic.

#### Proof

With a fixed left endpoint, increasing the right endpoint can only increase
the interval maximum. With a fixed right endpoint, moving the left endpoint
left can only increase it. Thus both endpoint classes are chains. Two
opposite classes sharing two targets would give two targets represented by
the same physical interval, impossible. Finally, the first precedence
orientation strictly increases the numerical right endpoint, and the second
strictly increases the numerical left endpoint. Neither admits a directed
cycle. \(\square\)

This is the correct abstract form of the SCD-fusion compatibility problem:
one needs two orthogonal chain partitions with simultaneously acyclic
endpoint precedences. It does not supply a numerical contradiction. The
known hook pair develops quadratic precedence cycles only when one keeps its
particular endpoint families, and the audited ring, raster, intact-side, and
globally ordered shell obstructions likewise apply only to their stated
architectures. For the cube and the strict-triangle sector, arbitrary
simultaneous rechaining, nonmonotone crossing factors, and the corridor
overlap demanded by (6.6) remain open.

Theorem 3.0 supplies a universal \(\Omega(R^2)\) lower bound in the stated
dominant plateau cone. No such universal quadratic lower bound is known for
the cube: the rank-slack and endpoint estimates there still force only a
linear excess. A negative resolution of the cubic local problem would need
a new theorem coupling the two endpoint partitions, or a theorem showing
that the quadratic corridor overlap in (6.6) is incompatible with the
interior pins. Neither statement is proved here.

---

## 8. Cofinal scales on a fixed ray

The scale variable can also be thinned without loss.

### Lemma 8.1 (cofinal-scale interpolation)

Fix positive integers \(a,b,c\). Suppose \(t_j\to\infty\),

\[
\frac{t_{j+1}}{t_j}\to1,
\]

and

\[
g_3(at_j,bt_j,ct_j)
=w_3(at_j,bt_j,ct_j)+o(t_j^2).
\]

Then RAY holds for \((a,b,c)\) on every integer scale \(t\).

#### Proof

For \(t_j\le t<t_{j+1}\), use (3.2) to extend the word at scale \(t_j\).
All three side gaps are \(O_{a,b,c}(t-t_j)\), while all ambient sides are
\(O_{a,b,c}(t)\). Hence the extension cost is

\[
O_{a,b,c}((t-t_j)t)=o(t^2).
\]

Width is coordinatewise monotone, so subtracting the target width cannot
increase the resulting upper error. \(\square\)

As a reduction lemma this would permit sparsity in both parameters.
Corollary 3.0A shows that the proposed cofinal axial construction cannot
exist: on every moving long-axis family its normalized excess is at least
\(1-o(1)\).

---

## 9. Adversarial audit and exact obstruction

The strongest claims above were checked independently against the following
failure modes.

1. **Middle-rank parity.** Formula (1.1) counts the two deleted corner
   triangles separately. Their sizes differ when \(d\) is odd; the floor in
   (1.1) records exactly that difference.
2. **Clamping versus deletion.** A smaller target's old witness contains no
   entry outside the smaller box. Deleting newly zero entries therefore
   cannot puncture that witness.
3. **Translated origins.** A translated child word does not cover its local
   zero. Lemma 2.1 explicitly pays one literal origin for every non-global
   child, giving exactly \(IJ-1\) anchors.
4. **No hidden cross-\(C\) uniformity.** In Theorem 2.3 the cofinal \(C\) is
   chosen once for a fixed target ray and only then is \(t\to\infty\) taken.
   The moving formulation is obtained by an explicit slow diagonalization.
5. **The plateau/triangle boundary.** Axial slab widths add exactly only
   when the parent is plateau. Proposition 4.1 exhibits the missing
   quadratic term in the strict-triangle interior, so the axial compression
   is not being silently applied to the cube.
6. **Shell ties and the shortened first block.** The priority order
   \(y=t\), then \(z=t\), then \(x=t\) exhausts all ties. After shortening
   \(C_1\), the sole missing max-one target is supplied at level two, which
   is why the saving is claimed only for \(q\ge2\).
7. **Corridor scope.** The intervals \(J_t\) in Theorem 6.1 may overlap
   arbitrarily. Equations (6.5)--(6.6) are requirements on a successful
   construction, not a global lower bound excluding one.
8. **Endpoint scope.** Lemma 7.1 proves acyclicity only after endpoint
   classes have been chosen. It does not show that suitable orthogonal
   classes fail to exist.
9. **Ordered middle witnesses.** Equal left endpoints or reversed right
   endpoints force containment and comparable same-rank maxima. Thus the
   two monotone slack sequences in Theorem 3.0 require no canonical choice
   of witnesses.
10. **Literal multipin gap.** Equation (3.0c) uses one occurrence in one
    positive witness. It does not assume that a threshold run shares a
    common physical pin.
11. **Block congestion.** Consecutive block pairs charge disjoint
    \(\alpha\)- and \(\beta\)-increment spans. The two total charges are
    separately at most \(D\), exactly as required in (3.0d).
12. **Axial transfer direction.** Lemma 2.1 gives
    \(g_3(t,2t,r)\le1+2g_3(t,t,r)\). Combining an upper bound of the large
    box by the axial box with a lower bound for the large box correctly
    yields the axial lower bounds (3.0e)--(3.0f).

Accordingly, the full compact theorem is false. Line G is retargeted from
proving coefficient one to determining the sharp quadratic excess

\[
\gamma(a,b,c)=
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-w_3(at,bt,ct)}{t^2},
\]

constructing words that approach the new lower bounds, and deciding whether
any non-CB local architecture can still support the global Boolean
conjecture. In particular, the axial targets now obey (3.0e), and their
cofinal long-axis excess obeys (3.0f).

The strict-triangle and cubic construction problem remains meaningful:

> A strict-triangle proof must braid macroscopic child slabs without paying
> the quadratic reset in (4.1), and on the cube it must realize the
> quadratic cross-level corridor overlap (6.6) while preserving all
> interior target pins and an acyclic pair of endpoint precedence systems.

No such cubic braid was constructed, and no theorem here rules it out. It
can no longer prove CB, because CB already fails on dominant plateau rays.
