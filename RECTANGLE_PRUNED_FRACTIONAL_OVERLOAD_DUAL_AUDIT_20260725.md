# Rectangle-pruned geodesic catalogues: exact fractional-overload dual and the horizontal flow

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The balanced independent-pruning lemma does not imply that the pruned
return-free geodesic catalogue has a tag-saturating fractional weighting
with total target overload \(o(W)\).

The obstruction is not a missing constant.  The overload problem has an
exact minimax dual over **all weighted target cuts**.  The pruning lemma
controls degrees of individual tag and target fibres, but does not control
the minimum weighted target cost of a path in each tag fibre.  An abstract
catalogue with empty bad graph and arbitrarily large tag and target fibre
degrees can still have \(\Theta(W)\) unavoidable overload.

For the actual geodesic catalogue there are two additional exact warnings.

1. Two pairwise rectangle-free singleton blockers can kill one path at
   depth one.
2. A globally exponentially small carrier shadow can kill an entire tag
   fibre.

Thus rectangle exclusion is not hereditary under the sequence of bites.
No tag-saturating fractional weighting with \(o(W)\) overload after every
bite is proved.

There is, however, no separate **fractional horizontal** obstruction.  A
weighting on length-\(\ell\) geodesic chunks already carries successor flow
along legal rotor paths.  Its total fractional path-start mass is \(R\)
and its state-column mass is \(\ell R\), so its fractional horizontal
deficiency is \(R=o(\ell R/Q)\) because \(Q=o(\ell)\).  The remaining
horizontal problem is integral: one must round the same path weights
without destroying target coverage or overload.

## 1. Correct coefficient weighting in the pruning lemma

Let

\[
W=\binom{2m}{m},\qquad
M=m+H,\qquad
N=\binom{2m}{M},\qquad MN=W-o(W).
\tag{1.1}
\]

In the balanced-pruning lemma, weights are arbitrary.  To use its
exceptional-fibre conclusion at coefficient one, a bad carrier-tag fibre
must be assigned the physical endpoint mass of its atom, not weight one.
For the return-free length-\(\ell\) chunk catalogue this weight is
\(\ell\).  For a full length-\(M\) carrier trajectory it is \(M\).

Indeed, if \(R_{\rm bad}\) length-\(\ell\) tags are lost, their owner/state
capacity is of order \(\ell R_{\rm bad}\).  Weight one would only show

\[
R_{\rm bad}=o(W),
\]

which is vacuous because the short-chunk tag family has

\[
T=(1+o(1))W/\ell=o(W).
\]

With weight \(\ell\), the pruning conclusion

\[
\ell R_{\rm bad}=o(W)
\tag{1.2}
\]

gives the required

\[
R_{\rm bad}=o(T).
\tag{1.3}
\]

Target fibres retain weight one.  The total weighted fibre mass remains
\(O(QW)\), so the abstract pruning theorem still applies with this
corrected ledger.

This correction makes the exceptional count meaningful.  It does not
solve the fractional overload problem on the good fibres.

## 2. The exact fractional-overload linear program

Let \({\cal T}\) be the retained good tag family.  For a tag
\(U\in{\cal T}\), let \({\cal I}_U\) be its pruned family of legal
decorated geodesic chunks.  Let \(V\) be the current available target
family, over all protected rows, and let \(C(P)\subseteq V\) be the claims
of a path \(P\).

We seek nonnegative weights \(x_P\) satisfying

\[
\sum_{P\in{\cal I}_U}x_P=1
\qquad(U\in{\cal T}).
\tag{2.1}
\]

The target load is

\[
\ell(v)=\sum_{P:v\in C(P)}x_P.
\tag{2.2}
\]

Define the minimum total capacity-one overload

\[
\operatorname{Ov}({\cal I})
=
\min_x
\sum_{v\in V}(\ell(v)-1)_+,
\tag{2.3}
\]

subject to (2.1).

### Theorem 2.1 (exact weighted-cut dual)

\[
\boxed{
\operatorname{Ov}({\cal I})
=
\max_{a\in[0,1]^V}
\left[
\sum_{U\in{\cal T}}
\min_{P\in{\cal I}_U}
\sum_{v\in C(P)}a_v
-
\sum_{v\in V}a_v
\right].}
\tag{2.4}
\]

If some retained tag fibre is empty, the primal is infeasible.

#### Proof

Introduce variables \(z_v\ge0\) and write the primal as

\[
\min\sum_vz_v
\tag{2.5}
\]

subject to (2.1),

\[
\sum_{P:v\in C(P)}x_P-z_v\le1
\qquad(v\in V),
\tag{2.6}
\]

and \(x_P,z_v\ge0\).

Give (2.6) multipliers \(a_v\ge0\), and give the tag equalities free
multipliers \(y_U\).  The Lagrangian is

\[
\sum_Uy_U-\sum_va_v
+
\sum_Px_P
\left(
\sum_{v\in C(P)}a_v-y_{\operatorname{tag}(P)}
\right)
+
\sum_vz_v(1-a_v).
\tag{2.7}
\]

Its infimum over \(x,z\ge0\) is finite exactly when

\[
0\le a_v\le1
\tag{2.8}
\]

and

\[
y_U\le\sum_{v\in C(P)}a_v
\qquad(P\in{\cal I}_U).
\tag{2.9}
\]

For fixed \(a\), the optimal value of \(y_U\) is the minimum in (2.4).
Finite-dimensional linear-programming duality proves the formula.
\(\square\)

### Exact sufficient and necessary cut

The pruned catalogue has overload \(o(W)\) if and only if, uniformly for
every \(a\in[0,1]^V\),

\[
\boxed{
\sum_{U\in{\cal T}}
\min_{P\in{\cal I}_U}a(C(P))
\le
\sum_{v\in V}a_v+o(W),}
\tag{2.10}
\]

where \(a(C)=\sum_{v\in C}a_v\).

For an indicator \(a=\mathbf1_A\), this reads

\[
\sum_U\min_{P\in{\cal I}_U}|C(P)\cap A|
\le |A|+o(W).
\tag{2.11}
\]

Thus the dual cuts measure unavoidable multi-target hitting sets in every
tag fibre.  Individual target-fibre degrees do not measure these minima.

### Corollary 2.2 (fractional overload implies low residual width)

Assume every length-\(\ell\) decorated chunk has claimed size \(K\), all
its claims lie in the current hole family \({\cal H}\), and

\[
|{\cal H}|=R K+\delta
\tag{2.12}
\]

for \(R=|{\cal T}|\).  For an overload-minimizing tag-saturating weighting,
put

\[
\Delta_-=\sum_{v\in{\cal H}}(1-\ell(v))_+.
\]

Then

\[
\boxed{
\operatorname{width}({\cal H})
\le \ell R+\Delta_-
=\ell R+\delta+\operatorname{Ov}({\cal I}).}
\tag{2.13}
\]

#### Proof

The claims of one geodesic chunk are the union of its \(\ell\) phase
columns.  Each phase column is an inclusion chain, so one chunk meets an
antichain in at most \(\ell\) targets.  For every antichain
\({\cal A}\subseteq{\cal H}\),

\[
\sum_{v\in{\cal A}}\ell(v)
\le\ell\sum_Px_P
=\ell R.
\]

Adding the lower-load deficiency gives

\[
|{\cal A}|\le\ell R+\Delta_-.
\]

Also \(\sum_v\ell(v)=RK\), so (2.12) gives

\[
\Delta_-=\delta+\sum_v(\ell(v)-1)_+.
\]

Minimize the last positive part over tag-saturating weights and maximize
over antichains. \(\square\)

Thus the desired fractional overload \(o(W)\), together with
\(\ell R=o(W)\) and \(\delta=o(W)\), would prove the residual low-width
gate from the preceding reserve audit.  Theorem 2.1 identifies exactly
what balanced pruning would have to prove to obtain it.

## 3. Why balanced fibre pruning does not imply the dual cuts

The failure already occurs in an abstract catalogue with no bad pairs.

### Proposition 3.1 (large fibres with macroscopic unavoidable overload)

Let there be \(R\) tags and let every edge have size \(K\).  There is a
simple catalogue with:

1. an empty bad graph;
2. arbitrarily large tag degrees;
3. arbitrarily large degree in every nonempty target fibre;
4. unavoidable fractional overload at least
   \[
   \boxed{\left\lfloor\frac K2\right\rfloor(R-1).}
   \tag{3.1}
   \]

#### Proof

Choose a target set \(A\) of size

\[
a=\left\lfloor K/2\right\rfloor.
\]

For every tag, take arbitrarily many distinct \(K\)-sets which all contain
\(A\); use a sufficiently large auxiliary target pool for their remaining
\(K-a\) entries.  Duplicate degrees may be made as large and as balanced
as desired by a symmetric choice of the auxiliary parts.  Declare the bad
graph empty.

Every tag-saturating weighting gives load \(R\) to every member of \(A\).
Hence its overload is at least \(a(R-1)\).

Equivalently, insert \(a_v=1\) on \(A\) and zero elsewhere into (2.4).
Every tag minimum equals \(a\), so the dual value is

\[
Ra-a=a(R-1).
\]

\(\square\)

More generally, whenever \(K/\ell\to\infty\), take

\[
R=\Theta(W/K)=o(W/\ell).
\tag{3.2}
\]

the lower bound (3.1) is \(\Theta(W)\).  Therefore neither
\(R=o(N)\), large retained fibre degrees, nor absence of every bad pair
implies \(o(W)\) overload.

Proposition 3.1 is an abstract logical obstruction to deriving (2.10)
from the balanced-pruning lemma.  It is not asserted to be a geodesic
orbit subcatalogue.

## 4. Actual geodesic residual cuts not controlled by rectangle pruning

The return-free geodesic audit supplies two exact physical obstructions.

### 4.1 Two-source singleton obstruction

There are three geodesic grids

\[
{\cal G}_0,{\cal G}_1,{\cal G}_2
\]

such that

\[
{\cal G}_0\cap{\cal G}_i=\{v_i\}
\quad(i=1,2),
\qquad
{\cal G}_1\cap{\cal G}_2=\varnothing,
\tag{4.1}
\]

where \(v_1,v_2\) are depth-one targets in different phase columns of
\({\cal G}_0\).  Every pairwise intersection is rectangle-free.

For the length-\(g\) priority ladder,

\[
\bar d^{(g)}_1=1.
\tag{4.2}
\]

After \({\cal G}_1,{\cal G}_2\) claim \(v_1,v_2\), the path
\({\cal G}_0\) has two blocked depth-one phase columns and therefore zero
legal priority degree.

This shows that an independent set in the rectangle bad graph need not
remain inside the next residual catalogue.  Pairwise pruning controls one
source at a time; legal residual degree depends on cumulative blockers
from different selected paths.

### 4.2 Carrier-shadow tag cut

Fix one carrier \(U\), and forbid the lower depth-one shadow

\[
Z^-_1(U)=\binom U{m-1}.
\tag{4.3}
\]

Every geodesic chunk on \(U\) uses lower depth-one targets in this family,
so its residual priority degree is zero:

\[
{\cal I}_U=\varnothing.
\tag{4.4}
\]

Nevertheless

\[
\frac{|Z^-_1(U)|}{\binom{2m}{m-1}}
=
\frac{\binom M{m-1}}{\binom{2m}{m-1}}
=o(1),
\tag{4.5}
\]

indeed exponentially small.

Thus a vanishing global used-target density can violate the tag equality
(2.1).  Balanced global row degrees do not imply tag feasibility.

The residual (4.3) is a deterministic cut, not a claim that the random
bite process typically creates it.  Together with (4.1), it proves that
the rectangle-pruning lemma alone supplies neither hereditary tag
feasibility nor the weighted cuts (2.10).

## 5. The exact theorem still needed after pruning

A sufficient strengthening of balanced pruning is the following.

> **Weighted transversal dispersal (WTD).**  After every bite, discard
> tag fibres of total weight \(o(W)\), with tag weight \(\ell\), and retain a
> rectangle-free catalogue satisfying (2.10) for every
> \(a\in[0,1]^V\).

By Theorem 2.1, WTD is exactly equivalent to a tag-saturating fractional
weighting with total target overload \(o(W)\).

The balanced-pruning theorem proves lower degree in most coordinate
fibres.  WTD is a simultaneous hitting-set statement over a continuum of
weighted cuts.  It cannot be obtained from those coordinate degrees by
ordinary Hall: the minimum over paths in (2.10) couples all claimed
targets of one path.

The rectangle census would have to prove an inequality of the form

\[
\sum_U\min_{P\in{\cal I}_U}a(C(P))
\le(1+o(1))\sum_va_v+o(W)
\tag{5.1}
\]

uniformly in \(a\), or a multi-source blocker potential strong enough to
imply it dynamically.  No such estimate is presently proved.

## 6. Horizontal rotor flow of a fractional path weighting

Suppose, conditionally, that weights satisfying (2.1) and

\[
\operatorname{Ov}({\cal I})=o(W)
\tag{6.1}
\]

have been found.  Every atom \(P\) is a legal length-\(\ell\) geodesic
rotor chunk,

\[
P=(\omega_0,\ldots,\omega_{\ell-1}).
\]

Send \(x_P\) units of state mass through every \(\omega_j\) and
\(x_P\) units of successor flow through every arc

\[
\omega_j\longrightarrow\omega_{j+1}.
\]

The total fractional state-column mass is

\[
\boxed{B_{\rm frac}=\ell\sum_Px_P=\ell|{\cal T}|,}
\tag{6.2}
\]

while the total path-start, or horizontal deficiency, is

\[
\boxed{p_{\rm frac}=\sum_Px_P=|{\cal T}|.}
\tag{6.3}
\]

Therefore

\[
\frac{p_{\rm frac}}{B_{\rm frac}}=\frac1\ell.
\tag{6.4}
\]

For the geodesic pruning scale

\[
Q\ll\ell,
\tag{6.5}
\]

so

\[
\boxed{
p_{\rm frac}
=o(B_{\rm frac}/Q).}
\tag{6.6}
\]

Thus the same weighting automatically has more than enough **fractional**
horizontal successor flow.  No extra horizontal minimax condition is
needed before rounding.

### The remaining integral gap

Equations (6.2)--(6.6) do not select one integral path on every tag.
Rounding \(x\) independently preserves the legal horizontal path inside
each selected atom but typically gives Poisson-type target misses and
overloads.  Rounding the fractional target loads by a generic chain-cover
theorem preserves neither the path atoms nor their successor arcs.

The exact remaining assertion is a joint rounding theorem:

> Round the WTD weighting to integral geodesic chunks so that target
> overload and uncovered mass are \(o(W)\), while using only the already
> present path starts.

If such a rounding exists, its horizontal start count is the number of
selected chunk tags.  Since \(\ell\gg Q\), the reset contribution is
automatically \(o(W)\) at the calibrated endpoint mass.

The balanced-pruning lemma, by itself, proves neither WTD nor this joint
rounding.

## 7. Final status

The exact fractional overload gate is now

\[
\boxed{
\sup_{a\in[0,1]^V}
\left[
\sum_U\min_{P\in{\cal I}_U}a(C(P))
-\sum_va_v
\right]
=o(W).}
\tag{7.1}
\]

Rectangle-free balanced fibre degrees do not imply (7.1).  The abstract
common-hitting-set construction gives a \(\Theta(W)\) dual obstruction,
and the actual geodesic catalogue has explicit two-source and
carrier-shadow residual cuts which pairwise rectangle pruning does not
control.

Conditionally on (7.1), horizontal rotor flow is already present at the
strong ratio \(1/\ell=o(1/Q)\).  What remains is to preserve that flow
through an integral, target-efficient rounding.
