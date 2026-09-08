# Audit of `THREEBOX_CORRIDOR_NEWLINE_20260724.md`

## Verdict

**PASS, with one bookkeeping correction and six precision repairs.**

The construction-and-obstruction pair is mathematically sound. In
particular, the canonical atoms really give the advertised cylinders, the
plateau throughput and moment-conservation arguments have the correct
off-by-one constants, the surplus-endpoint turnover identities are exact,
the record-corridor lemma follows from monotonicity of suffix maxima, and the
maximum-load-three obstruction is valid in precisely the stated
certificate-preserving fusion architecture.

No unrestricted lower bound for arbitrary three-box words follows from
Section 8, and the source correctly disclaims one.

The only incorrect sentence is the role-type split immediately after (4.5):
after deleting the origin there are (N-1), not (N), displayed base-anchor
roles. The **total** role count used later is nevertheless correct.

---

## 1. Plateau width and throughput

For every (s\in[p+q,r]) and every base point
((x,y)\in[0,p]\times[0,q]), the third coordinate

\[
 z=s-x-y
\]

lies in ([0,r]). It is the unique third coordinate above that base point
having rank (s). Thus each plateau rank has exactly

\[
 N=(p+1)(q+1)
\]

points. Every rank has at most (N) points because fixing ((x,y)) fixes
at most one possible (z), so (N) is indeed the width.

At endpoint (j), there are (j) suffix intervals and their maxima form a
chain. A chain contains at most one point of any fixed rank. Hence endpoint
(j) carries at most (min(h,j)) of the (h=r-p-q+1) plateau points
assigned to it, and

\[
 Nh\le \sum_{j=1}^n\min(h,j).
\]

When (n\ge h),

\[
 \sum_{j=1}^n\min(h,j)
 =1+\cdots +(h-1)+h(n-h+1)
 =hn-\frac{h(h-1)}2.
\]

Therefore

\[
 n\ge N+\left\lceil\frac{h-1}{2}\right\rceil
   =N+\left\lceil\frac{r-p-q}{2}\right\rceil.
\]

The constant and endpoints in (2.6) are correct.

### Precision repair 1

As written, the boxed display (2.6) visually resembles an unconditional
finite bound, while its derivation assumes (n\ge h). For the positive
fixed rays used in the note this is automatic for sufficiently large (t),
because every universal word has (n\ge N\asymp t^2) whereas (h=O(t)).
The clean finite wording is:

> If (g_3(p,q,r)\ge h) (in particular, if (N\ge h)), then (2.6) holds.
> Hence it holds on every fixed positive ray for all sufficiently large
> (t).

This is a hypothesis-visibility repair, not a defect in the asymptotic use.

The claim that exact width is impossible when (h>1) is also correct. In
fact, if (n=N), saturation at the first plateau rank forces endpoint (1)
to carry a plateau point, but endpoint (1) has only one suffix and hence
cannot carry a second plateau rank.

---

## 2. Outer-hook partition

For (x+y\le p), the point ((x,y)) occurs on the horizontal part of
(C_y). For (x+y>p), it occurs on the vertical part of (C_{p-x}). At
(x+y=p), the adopted convention places the point only on the horizontal
part: the vertical part begins one step above its corner. Thus the chains
are disjoint and exhaustive.

The horizontal segment has (p-i) edges and the vertical segment has
(q-i) edges, so

\[
 s_i=(p-i)+(q-i)=p+q-2i.
\]

Consequently

\[
 \sum_{i=0}^{p}(s_i+1)
 =(p+1)(p+q+1)-p(p+1)
 =(p+1)(q+1)=N.
\]

All endpoint and repeated-corner conventions in Section 3 are correct.

---

## 3. Canonical corridor atom

The reverse base-chain prefix from (v_{i,k}) down to (b_i) has base
maximum (v_{i,k}). Appending ((b_i,1),\ldots,(b_i,z)) changes only the
third maximum, so the displayed interval has maximum exactly
((v_{i,k},z)). The (z=0) points are literal entries. Every remaining
entry is nonzero.

The lengths are

\[
 |\mathcal A_0|=(s_0+1)+r-1=s_0+r,
\qquad
 |\mathcal A_i|=(s_i+1)+r\quad(i\ge1),
\]

and therefore

\[
 \sum_i|\mathcal A_i|=N+(p+1)r-1.
\]

### Precision repair 2

For (i=0,k>0,z>0), the proof says the physical interval contains
(v_{0,k},\ldots,v_{0,0}). The last of these entries was deleted. The
actual interval contains

\[
 v_{0,k},v_{0,k-1},\ldots,v_{0,1},
 (b_0,1),\ldots,(b_0,z).
\]

Its maximum is still exactly the claimed target, so the lemma is correct;
only that sentence should distinguish the (i=0) case.

### Required bookkeeping correction

The prose after (4.5) should read:

> exactly (N-1) displayed base-anchor roles and exactly
> ((p+1)r) positive vertical-reservoir roles,

or, equivalently,

> (N) formal base anchors with the unique zero anchor omitted, plus
> ((p+1)r) positive vertical-reservoir roles.

Under the Section 8 definition, a local role is a displayed position, so
the first formulation is the literal one. The later total

\[
 R=N+(p+1)r-1
\]

is already correct.

---

## 4. Exact-width owner conservation

At a fixed plateau rank, (N) targets and (N) endpoints force a bijection
between targets and endpoints. At two consecutive plateau ranks, the two
targets assigned to a common endpoint are comparable suffix maxima. Their
ranks differ by one, so exactly one coordinate increases by one.

Both rank assignments contain every base pair exactly once. Therefore their
total first-coordinate sums are equal, and every endpointwise first-coordinate
increment is nonnegative. Every such increment must be zero. The identical
argument applies to the second coordinate. Hence the third coordinate is the
one that increases, endpoint by endpoint, throughout the plateau.

Equation (5.3) is correct:

\[
 \sum_{(x,y)}x=(q+1)\sum_{x=0}^p x
 =(q+1)\frac{p(p+1)}2.
\]

The theorem is logically valid, though vacuous when (h>1) because exact
width is then impossible. The note explicitly presents it as an equality-
geometry statement, so this is not a hidden existence claim.

---

## 5. Surplus turnover

Two (N)-subsets of an ((N+d))-set have intersection of size at least
(N-d). Hence

\[
 k_s=|E_s\setminus E_{s+1}|
    =|E_{s+1}\setminus E_s|\le d.
\]

Equality of total first-coordinate mass at the two ranks gives

\[
 \sum_{j\in E_s\cap E_{s+1}}x_j(s)
 +\sum_{j\in D_s}x_j(s)
 =
 \sum_{j\in E_s\cap E_{s+1}}(x_j(s)+\Delta x_j)
 +\sum_{j\in B_s}x_j(s+1),
\]

which rearranges exactly to (6.4). The second-coordinate identity is
identical. Since the common-endpoint step is saturated,
(Delta x_j,\Delta y_j,\Delta z_j\in\{0,1\}) and their sum is one. Thus

\[
 0\le I_x(s)\le k_sp,
 \qquad
 0\le I_y(s)\le k_sq.
\]

The number of nonvertical common-endpoint steps is exactly
(I_x(s)+I_y(s)), hence at most (k_s(p+q)). All signs and constants are
correct.

### Precision repair 3

State explicitly that a plateau transition index satisfies

\[
 p+q\le s\le r-1,
\]

and in (6.7) that (J\subseteq\{p+q,\ldots,r-1\}) is a set (or interval)
of transition indices. This removes the only plateau-endpoint ambiguity.

---

## 6. Literal record corridor

For a fixed endpoint (j), suffix maxima are monotone as the start moves
left. If (ell_z) is the greatest start yielding ((x,y,z)), then distinct
consecutive vertical targets force

\[
 \ell_{z_1}<\ell_{z_1-1}<\cdots<\ell_{z_0}.
\]

The largest interval has maximum ((x,y,z_1)), so every entry in it has
first coordinate at most (x) and second coordinate at most (y). When
the start moves from (ell_{z-1}) to (ell_z), the third maximum changes
from (z-1) to (z). Therefore the newly admitted block contains a letter
of third coordinate exactly (z); and because the new full suffix has third
maximum (z), it contains no letter with third coordinate greater than
(z).

Lemma 7.1 is correct, including the strict ordering and the closed/open
endpoint ([ell_z,ell_{z-1}-1]).

---

## 7. Architecture-scoped load obstruction

By definition, every displayed local position is mapped to one physical
position. If every physical position has load at most (kappa), double
counting roles gives

\[
 R=\sum_{w=1}^n\operatorname{load}(w)\le\kappa n.
\]

With

\[
 R=N+(p+1)r-1,
\]

this proves (8.1) without any further property of the interval
certificates. For (p=at,q=bt,r=ct),

\[
 \frac RN
 =1+\frac{(at+1)ct-1}{(at+1)(bt+1)}
 \longrightarrow 1+\frac cb.
\]

If (n=N+o(t^2)), then (n/N\to1), so (R/n\to1+c/b). Since the maximum
load is an integer, any such sequence of safe fusions satisfies

\[
 \liminf_{t\to\infty}\kappa_t
 \ge \left\lceil1+\frac cb\right\rceil.
\]

As (c>2b), this lower bound is at least (4). Thus maximum role load at
most (3) is impossible for all sufficiently large (t).

This conclusion is valid only for the explicitly defined safe-fusion
architecture. The definition is sufficiently narrow to make the role count
literal and sufficiently broad to allow quotienting, interleaving, and
physical letters different from their local antecedents. It does **not**
apply to arbitrary three-box words, and the source states this correctly.

### Precision repair 4

Replace the asymptotically ambiguous display

\[
 \kappa\ge\left\lceil1+\frac cb-o(1)\right\rceil
\]

by the exact integer consequence

\[
 \liminf_{t\to\infty}\kappa_t
 \ge\left\lceil1+\frac cb\right\rceil.
\]

The stated load-three corollary is unchanged.

### Precision repair 5

The sentence excluding “pairwise portal fusion, alternating two-arm fusion,
or a three-atom local patch” is justified only for implementations in which
those labels genuinely imply maximum **role** load at most (2) or (3).
Add “whose physical positions carry at most three canonical local roles” to
that sentence. A globally interleaved construction could be described
informally as pairwise while allowing a position to accumulate many roles;
Theorem 8.1 would not exclude it merely because of the informal label.

---

## 8. Ray integrality convention

The side lengths of (P(p,q,r)) are integers. “Primitive ray” normally
means a fixed primitive integer triple ((a,b,c)) and integer
(t\to\infty), but the note never states this explicitly.

### Precision repair 6

At (1.1), state (a,b,c\in\mathbb Z_{>0}) (usually
(\gcd(a,b,c)=1)) and (t\in\mathbb Z_{>0}), or say that (t) ranges over
values for which (at,bt,ct) are integers. This has no effect on any
asymptotic estimate.

---

## Final audit ledger

| Item | Verdict | Comment |
|---|---|---|
| Plateau size and width | PASS | Exact for (p+q\le s\le r). |
| Throughput bound | PASS | Correct under the stated (n\ge h) hypothesis; make the boxed finite scope explicit. |
| Outer-hook partition | PASS | Boundary (x+y=p) handled correctly. |
| Atom certificate | PASS | One proof sentence must omit the deleted origin in the (i=0) case. |
| Total isolated length | PASS | (N+(p+1)r-1). |
| Role-type split | **REPAIR** | (N-1) displayed base roles, not (N); total (R) remains correct. |
| Exact-width owner conservation | PASS | Correct equality geometry, vacuous for multi-rank plateaux. |
| Surplus turnover identities | PASS | Correct signs, (k_s\le d), and bounds (dp,dq). |
| Record-corridor lemma | PASS | Greatest-start and newly admitted-block claims are valid. |
| Safe-fusion load barrier | PASS | Exact double count; architecture-scoped only. |
| Maximum-load-three obstruction | PASS | Since (1+c/b>3), eventual load at least four is forced. |
| Primitive-ray theorem | NOT PROVED | Correctly left open. |

After the listed wording/bookkeeping repairs, the note is suitable for the
master handoff as a rigorous new reduction.
