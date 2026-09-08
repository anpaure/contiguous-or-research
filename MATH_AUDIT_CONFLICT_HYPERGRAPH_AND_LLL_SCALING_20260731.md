# Audit of the common-cap conflict hypergraph and LLL scaling

Date: 2026-07-31  
Scope: abstract depth-`d` common-cap selection; no finite K16 search.

## 1. Correct exact conflict clutter

Let the residual target parts be `L_S`, whose vertices are candidate
incidences `v=(S,C)`.  Cells are distinct physical intervals of length at
most `d`; middle rows have length at most `D` (normally `D=d+1`).  Let
`Ebar_p` already include every frozen prepin cap.

A complete conflict clutter must contain the following matching-compatible
minimal sets.

1. **Same cell:** every pair of vertices from distinct target parts using
   the same cell.
2. **Empty position:** a minimal family whose cells contain `p` and whose
   target masks have empty intersection with `Ebar_p`.
3. **Middle-bit cover:** a minimal family of targets omitting `b` whose cells
   cover
   \[
   H_{i,b}=\{p\in I_i:b\in\bar E_p\}.
   \]
4. **Assigned-lower-bit cover:** an anchor `v_0=(S_0,C_0)`, a bit
   `b in S_0`, and a minimal family of other selected targets omitting `b`
   whose cells cover
   \[
   H_{v_0,b}=\{p\in C_0:b\in\bar E_p\}.
   \]
5. **Protected-prepin-bit cover:** for every frozen multi-cell prepin
   `(P_alpha,J_alpha)` and `b in P_alpha`, a minimal family of residual
   targets omitting `b` whose cells cover
   \[
   H_{\alpha,b}=\{p\in J_\alpha:b\in\bar E_p\}.
   \]

Only sets with at most one vertex from each target part need be retained.
The fifth family is absent from the proposed clutter and is necessary unless
every residual incidence was defined to preserve every prepin row, or every
prepin has an immunity property.  A one-cell singleton is immune: any
nonempty later cap is the same singleton.  A general multi-cell pin is not.

If an owner `o_p in Ebar_p` is chosen and only candidates containing `o_p`
at every position of their cell are retained, empty-position conflicts
disappear.  None of the bit-cover families disappears.

After deleting unary conflicts, the ranks are:

| family | maximum size |
|---|---:|
| same cell | 2 |
| middle bit | `D` |
| assigned lower bit | `d+1` including the anchor |
| protected prepin bit | `d` |
| empty position | `min(|Ebar_p|,d(d+1)/2)` |

The cover bounds follow from private points in an inclusion-minimal cover.
The empty-position bound follows from private coordinates and from the fact
that only `d(d+1)/2` distinct length-at-most-`d` intervals contain a fixed
position.  Thus owner orientation gives rank at most `d+1`, but it does not
bound the number or dependency of conflicts.

## 2. Exact worst-case counts

Write

\[
m=\min_S|L_S|,\qquad M=\max_S|L_S|,
\]

and define the literal atlas loads

\[
\lambda_C=|\{S:(S,C)\in L_S\}|,
\quad \lambda=\max_C\lambda_C,
\]

\[
A^- =\max_{b,p}|\{(S,C):p\in C,\ b\notin S\}|,
\]

\[
A^+ =\max_{b,p}|\{(S,C):p\in C,\ b\in S\}|.
\]

For a vertex `v=(S,C)`, let `Pi(v)` be the number of protected-prepin
requirements `(alpha,b)` for which `b notin S` and
`C intersect H_(alpha,b)` is nonempty, and put `Pi=max_v Pi(v)`.

### 2.1 Global event counts

The same-cell pair count is exactly

\[
N_{cell}=\sum_C\binom{\lambda_C}{2}.                 \tag{2.1}
\]

For a fixed middle requirement with `h=|H_(i,b)|`, the number of minimal
size-`j` covers is at most

\[
(h)_j(A^-)^j\le(hA^-)^j,
\qquad j\le h\le D.                                 \tag{2.2}
\]

Indeed, assign every member a distinct private host, then choose a negative
candidate through that host.  The same bound with `h<=d` applies to a fixed
protected-prepin bit.  For a fixed lower anchor and bit, the blocker family
of size `t` has at most

\[
(h)_t(A^-)^t\le(dA^-)^t,
\qquad h\le d,                                      \tag{2.3}
\]

choices; the resulting forbidden set has size `t+1`.

These are overcounts, but they are worst-case valid without any linearity or
codegree hypothesis.

### 2.2 Counts through one candidate

Assume middle starts are distinct integers.  A length-at-most-`d` cell meets
at most `D+d-1` middle intervals of length at most `D`.  For total conflict
size `j`, the number `B_j(v)` of bad sets containing a fixed vertex `v` is
bounded by

\[
\begin{split}
B_j(v)\le{}&
 \mathbf1_{j=2}(\lambda_C-1)\\
&+(D+d-1)r(DA^-)^{j-1}\\
&+r(dA^-)^{j-1}\\
&+\mathbf1_{j\ge2}\,k d A^+(dA^-)^{j-2}\\
&+\Pi(v)(dA^-)^{j-1},                               \tag{2.4}
\end{split}
\]

with terms omitted outside their possible ranks.  The lines respectively
count same-cell pairs, middle covers, the case where `v` is the lower
anchor, the case where `v` is a blocker for another lower anchor, and
protected-prepin covers.  Without owner orientation add

\[
d(rA^-)^{j-1}                                        \tag{2.5}
\]

for position conflicts.  If starts may repeat, replace `D+d-1` by the
literal maximum number of middle rows meeting a candidate cell.

For the part profile

\[
D_j(S)=|\{F:|F|=j,\ F\cap L_S\ne\varnothing\}|,
\]

one has

\[
D_j(S)\le\sum_{v\in L_S}B_j(v)\le M\max_vB_j(v).    \tag{2.6}
\]

Put `Gamma=max_S sum_j D_j(S)`.  A bad event using `j` target parts has
ordinary dependency degree at most

\[
\Delta(F)\le\sum_{S\in parts(F)}(\Gamma_S-1)
             \le j\Gamma.                           \tag{2.7}
\]

Thus the proposed symmetric hypothesis is valid only as a literal
candidate-specific assumption.  It does not follow from bounded depth or
bounded hyperedge rank.

### 2.3 Coarse Boolean bounds

Let

\[
u=\max_C\left|\bigcup_{p\in C}\bar E_p\right|.
\]

Each cell can support at most

\[
L_u=\sum_{q=1}^{r-1}\binom uq                         \tag{2.8}
\]

distinct lower labels.  Hence `lambda<=L_u`.  Since at most
`g_d=d(d+1)/2` cells contain a fixed position,

\[
A^-,A^+\le g_dL_u.                                  \tag{2.9}
\]

In the usual proper-prefix setting `u<=r`, so `L_u<=2^r-1`.  These bounds
are exponential and are far too coarse to imply an LLL without a separate
lower bound and distribution theorem for the candidate domains.

For example, after owner orientation the symmetric LLL can be certified from

\[
e\left((d+1)\Gamma+1\right)\le m^2.                 \tag{2.10}
\]

Using only (2.4), its high-arity contribution scales as

\[
\Gamma=O\left(Mr(dA^-)^d\right).                    \tag{2.11}
\]

The symmetric reduction charges every event at probability `m^-2` and thus
throws away the much smaller probability `m^{-(d+1)}` of a large cover.  An
arity-sensitive asymmetric test is therefore essential asymptotically.

## 3. What the LLL can and cannot prove

The conditional symmetric lemma is correct: after owner filtering and unary
closure, if every part has size at least `m`, every event has size at least
two, and its literal dependency degree is at most `Delta`, then

\[
e(\Delta+1)\le m^2                                  \tag{3.1}
\]

is sufficient.  The case `Delta=0` should be handled separately rather than
using the displayed witness `x=1/(Delta+1)=1`.

The exact uniform part-profile asymmetric condition is

\[
{1\over m}\le
a\prod_{j=2}^{\rho}(1-a^j)^{D_j}
\quad\text{for some }0<a<1,                         \tag{3.2}
\]

where `D_j=max_S D_j(S)`.  A candidate-specific atomic lopsided condition is

\[
p_F\le {y_F\over\prod_{v\in F}c_v},
\qquad
\prod_{G\in\mathcal A(v)}(1-y_G)\ge c_v^{-1}.       \tag{3.3}
\]

Here `A(v)` consists of bad events using an alternative candidate in the
part of `v`.  Equations (3.2)--(3.3) are valid finite sufficient criteria,
but their profile/pressure bounds are additional atlas hypotheses.  Boolean
rank, Johnson adjacency, depth, and minimum list size alone do not supply
them.

### Counter-scaling

For integers `m,n`, take `n` target parts

\[
V_i=\{(i,c):c\in[m]\},
\]

and put a same-cell pair conflict between `(i,c)` and `(j,c)` for every
`i!=j`.  This is a rank-two, depth-one cell-conflict atlas with every domain
of size `m`.

If `n=m+1`, it has no independent transversal by the pigeonhole principle.
Thus no symmetric, asymmetric, or lopsided LLL conclusion can follow from
bounded depth/rank and growing candidate domains alone.

Even the Hall-feasible case `n=m` defeats the standard uniform numerical
tests.  A collision event has probability `m^-2` and ordinary dependency

\[
2m(m-1)-m-1=2m^2-3m-1,
\]

so the symmetric product tends to `2e`.  Its assignment-incompatible
lopsided degree is

\[
(m-1)(2m-3)\sim2m^2,
\]

so the symmetric lopsided test also fails.  The part profile is
`D_2=m(m-1)`, for which the maximum right side of (3.2) is asymptotically

\[
\max_a a(1-a^2)^{m(m-1)}
 \sim {e^{-1/2}\over\sqrt2\,m}<{1\over m}.           \tag{3.4}
\]

For a candidate `v`, the opposing lopsided pair count is `(m-1)^2`; the
uniform product condition tends to `exp(-c^2)>=1/c`, impossible for every
fixed `c>1` because `c^2>log c`.  Nevertheless a transversal exists (any
permutation).  This shows that failure of these canonical LLL inequalities
is not an obstruction theorem; nonuniform weights or deterministic
structure may still solve a specific atlas.

## 4. Exact finite cutwise criterion

Introduce one binary variable `x_(S,C)` per retained candidate.  After
reserving prepin cells and applying unary closure, impose

\[
\sum_{C:(S,C)\in L_S}x_{S,C}=1                       \tag{4.1}
\]

for every residual target,

\[
\sum_{S:(S,C)\in L_S}x_{S,C}\le1                     \tag{4.2}
\]

for every physical cell, and

\[
\sum_{v\in F}x_v\le|F|-1                             \tag{4.3}
\]

for every inclusion-minimal conflict of the four cap types: position,
middle-bit, assigned-lower-bit, and protected-prepin-bit.  Same-cell pairs
are already (4.2), though retaining them as two-edges is equivalent.

This finite system is exact.  Any integral solution is an injective
selection whose maximal common cap is nonempty and replays every middle,
residual-lower, and protected-prepin row.  Conversely, any simultaneous
common-cap matching violates none of (4.1)--(4.3).  Separation is cutwise:
an integral candidate matching either replays, or an empty position or a
missing bit supplies a minimal local cover of rank bounded in Section 1.

Accordingly, the reusable theorem should present (4.1)--(4.3) as the exact
finite gate, and the symmetric/asymmetric/lopsided conditions only as
candidate-specific sufficient certificates after owner filtering, prepin
protection, and unit closure.

## 5. Verdict on the proposed theorem

1. The conflict-transversal equivalence is correct after adding protected
   multi-cell prepin bit covers.
2. The rank bound `d+1` after owner orientation is correct; it is not a
   dependency bound.
3. The symmetric constant `e(Delta+1)<=m^2` is correct for literal
   post-closure `Delta`, apart from the trivial `Delta=0` witness detail.
4. No symmetric, asymmetric, or lopsided LLL hypothesis follows from generic
   Boolean/Johnson parameters alone.  Actual cell loads, coordinate-position
   loads, minimal-cover profiles, and post-owner domain sizes are required.
5. The exact fallback is the finite cutwise system (4.1)--(4.3), not a
   generic asymptotic LLL.

