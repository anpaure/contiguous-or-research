# Independent audit of the DRAY obstruction

## Verdict

\[
\boxed{\textbf{PASS}}
\]

The finite inequality

\[
D\ge
\frac{M((r-\varepsilon)/2-q)-1}{h-1+2B}
\]

and its ray consequence

\[
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}
\]

are correct under the hypotheses stated in
`MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md`.  I found no hidden
common-pin assumption, no endpoint off-by-one error, and no congestion
leak in the block pairing.  The proof is architecture-free: it applies to
an arbitrary literal range-maximum word.

This audit was carried out independently from first principles.  I then
compared the result with `THREEBOX_CORRIDOR_NEWLINE_20260724.md`; the two
derivations agree, but no step below relies on that note.

There is one harmless wording ambiguity in Lemma 5: the selected maximal
plateau should explicitly be the maximal plateau **containing an occurrence
of the value (m_0) inside the original internal run**.  That is plainly the
intended choice and makes the proof literal.  No mathematical change is
needed.

---

## 1. Width and the exact low-rank count

Put

\[
M=(p+1)(q+1),\qquad
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,
\qquad
\varepsilon=p+q+r-2h.
\]

From (r>p+q),

\[
p+q\le h\le r.
\]

Consequently, for every ((x,y)\in[0,p]\times[0,q]), the point

\[
(x,y,h-x-y)
\]

lies in the box, and every rank-(h) point has this form.  Thus the
rank-(h) layer has exactly (M) points.  Projection to ((x,y)) is
injective on any antichain, because two points in the same fibre are
comparable.  Hence the width is exactly (M).

For fixed ((x,y)), the values below rank (h) are

\[
z=0,1,\ldots,h-x-y-1,
\]

exactly (h-x-y) choices.  Summation and deletion of the unique zero
point give

\[
\begin{aligned}
L_{<h}
&=\sum_{x=0}^{p}\sum_{y=0}^{q}(h-x-y)-1\\
&=M\left(h-\frac{p+q}{2}\right)-1\\
&=M\frac{r-\varepsilon}{2}-1.
\end{aligned}
\]

The parity correction and the final (-1) are both exact.

---

## 2. Ordered witnesses and slack coordinates

Choose one interval (I_i=[\ell_i,r_i]) witnessing each rank-(h)
point and order them by increasing left endpoint.

* Equal left endpoints are impossible: the two intervals would be nested,
  so their maxima would be comparable.
* If (\ell_i<\ell_j) but (r_i\ge r_j), then
  (I_j\subseteq I_i), giving the same contradiction.

Thus both endpoint sequences are strictly increasing.  In a word of length

\[
N=M+D,
\]

the (i)-th elements of two increasing (M)-subsets of ([N]) have the
forms

\[
\ell_i=i+\alpha_i,
\qquad
r_i=i+\beta_i,
\]

where

\[
0\le\alpha_1\le\cdots\le\alpha_M\le D,
\qquad
0\le\beta_1\le\cdots\le\beta_M\le D.
\]

Also (d_i=r_i-\ell_i=\beta_i-\alpha_i\ge0).  This parametrization
does not require shortest or canonical witnesses.

---

## 3. Rank-capped start capacity

Choose one witness for every nonzero target below rank (h).

At a selected start (\ell_i), such a witness must end before (r_i).
If it ended at or after (r_i), it would contain (I_i), hence its maximum
would dominate a rank-(h) point; a point of rank below (h) cannot do
that.  The allowed endpoints are exactly

\[
\ell_i,\ell_i+1,\ldots,r_i-1,
\]

so there are exactly (d_i) possible intervals.  This checks the
inclusive-endpoint off-by-one.

There are (N-M=D) unselected starts.  At any fixed start, interval
maxima obtained by moving the right endpoint form a chain.  Distinct
nonzero points below rank (h) in such a chain have distinct ranks among
(1,\ldots,h-1), so there are at most (h-1) of them.  Therefore

\[
L_{<h}\le\sum_{i=1}^{M}d_i+(h-1)D.
\]

No witness is omitted or counted twice in this partition by its start.

---

## 4. Valley characterization and the constant-sum bound

### Scalar characterization

Let (u_1,\ldots,u_m\) be nonnegative integers and choose a global-minimum
index (\tau).  If the prefix through (\tau) is not nonincreasing, some

\[
i<j<\tau
\]

satisfy (u_i<u_j), while (u_\tau\le u_i).  At threshold (u_j\ge1),
the component containing (j) is blocked on the left by (i) and on the
right by (\tau), hence is an internal positive threshold run.  The
suffix argument is symmetric.  Therefore absence of an internal positive
run forces a valley

\[
u_1\ge\cdots\ge u_\tau\le\cdots\le u_m.
\]

The inequalities (j<\tau) and (j>\tau) used in the two cases are
automatic because (\tau) is a global minimum.

### Three constant-sum coordinates

Suppose (T_1,\ldots,T_m\) are distinct rank-(h) points and all three
coordinate sequences are valleys.  Relabel the coordinates so their turn
indices satisfy

\[
\tau_X\le\tau_Y\le\tau_Z.
\]

Before (\tau_X), all coordinates are nonincreasing.  Constant sum then
forces every adjacent pair there to be equal, impossible; hence
(\tau_X=1).  Similarly (\tau_Z=m).

Between (\tau_X) and (\tau_Y), (X) is nondecreasing and the other
two coordinates are nonincreasing.  At every step (X) must increase by
at least one.  Between (\tau_Y) and (\tau_Z), (Z) must decrease by
at least one.  Hence

\[
\begin{aligned}
m-1
&\le X_{\tau_Y}-X_{\tau_X}
   +Z_{\tau_Y}-Z_{\tau_Z}\\
&=h-Y_{\tau_Y}-X_{\tau_X}-Z_{\tau_Z}.
\end{aligned}
\]

After relabeling, the three coordinatewise lower bounds are still the
multiset

\[
\{0,0,h-p-q\}.
\]

Their sum is (h-p-q), so the last display is at most (p+q).  Thus

\[
m\le p+q+1.
\]

This proves that any ordering of (p+q+2) middle points has an internal
positive threshold run in some coordinate.

---

## 5. The short-run mesh and its only wording repair

Start from an internal run and let (m_0) be the maximum coordinate value
on that run.  Choose a maximal consecutive (m_0)-plateau **containing an
occurrence in the original run**.  Both neighboring values are smaller:

* an adjacent value still in the original run is smaller by maximality and
  the choice of (m_0);
* an adjacent value outside the original run is below the old threshold,
  which is at most (m_0).

The plateau is therefore an internal positive run at threshold (m_0).
On the full middle rectangle:

* an (x)-level has (q+1) points;
* a (y)-level has (p+1) points;
* a (z)-level has at most (p+1) points, since (x+y) is fixed.

As (p<q), the plateau has at most (q+1) indices, hence edge length at
most (q).  This proves the mesh lemma exactly.

The source phrase “take a maximal consecutive plateau on which the
coordinate is equal to (m_0)” is unambiguous in context, but adding the
bolded clause above would prevent a reader from mistakenly selecting an
unrelated (m_0)-plateau elsewhere in the full sequence.

---

## 6. Literal pin gap: no common-pin assumption

Let ([u,v]) be an internal positive run at threshold (k), with
negative neighbors (u-1,v+1).  Because (T_u) has the relevant
coordinate at least (k), some physical word position

\[
s\in I_u
\]

has that coordinate at least (k).

Since (I_{u-1}) is negative and

\[
s\ge\ell_u>\ell_{u-1},
\]

one must have (s>r_{u-1}).  Since (I_{v+1}) is negative and

\[
s\le r_u<r_{v+1},
\]

one must have (s<\ell_{v+1}).  Therefore

\[
r_{u-1}+1\le s\le\ell_{v+1}-1,
\]

and the integral endpoints give

\[
r_{u-1}+2\le\ell_{v+1}.
\]

Substituting the slack coordinates yields

\[
\beta_{u-1}-\alpha_{v+1}\le v-u.
\]

If (v-u\le q), monotonicity then gives

\[
d_i\le q+\alpha_{v+1}-\alpha_i\quad(i<u)
\]

and

\[
d_i\le q+\beta_i-\beta_{u-1}\quad(i>v).
\]

Only the single position (s\in I_u) is used.  Different positive
witnesses may use different occurrences, and the threshold may occur at
arbitrarily many physical positions.  Thus the common-pin objection does
not apply.

---

## 7. Balanced blocks and telescoping congestion

Let

\[
s_0=p+q+2,
\qquad
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\qquad
R=M-Ks_0.
\]

When (K\ge2), it is positive and even, and maximality gives

\[
0\le R<2s_0.
\]

Partition the (M) indices into (K) consecutive blocks of sizes

\[
s_0+\left\lfloor\frac RK\right\rfloor
\quad\text{or}\quad
s_0+\left\lceil\frac RK\right\rceil.
\]

Thus every size lies in ([s_0,B]), where

\[
B=s_0+\left\lceil\frac RK\right\rceil.
\]

Apply the mesh lemma to the first (s_0) positions of every block.  Since
the resulting run is internal in that subblock, both negative neighbors
remain in the same full block.

Pair adjacent blocks (C=[a,b]) and (C'=[b+1,c]).  The run in (C')
lies strictly after all indices of (C), and the run in (C) lies
strictly before all indices of (C').  Therefore

\[
\sum_{i\in C}d_i
\le q|C|+B(\alpha_c-\alpha_a)
\]

and

\[
\sum_{i\in C'}d_i
\le q|C'|+B(\beta_c-\beta_a).
\]

The index-increment spans of distinct block pairs are disjoint.  Hence

\[
\sum_{\rm pairs}(\alpha_c-\alpha_a)
\le\alpha_M-\alpha_1\le D,
\]

and likewise for (\beta).  Notice that increments between consecutive
block pairs are not charged at all; no increment is charged twice.  Thus

\[
\sum_{i=1}^{M}d_i\le qM+2BD.
\]

All boundary indices are valid: the mesh run in the first (s_0) entries
has its left neighbor at least at the block start and its right neighbor
at most at the (s_0)-th block position.

---

## 8. Finite inequality

Combining the exact low-rank count, start capacity, and corridor bound gives

\[
M\frac{r-\varepsilon}{2}-1
\le qM+(h-1+2B)D.
\]

Therefore, whenever the numerator is positive,

\[
\boxed{
D\ge
\frac{M((r-\varepsilon)/2-q)-1}{h-1+2B}.
}
\]

The denominator is positive under the standing hypotheses.  The finite
statement correctly assumes (K\ge2); this is automatic eventually on
every fixed ray considered below.

---

## 9. Ray coefficient

Set

\[
p=at,\qquad q=bt,\qquad r=ct,
\]

with fixed integers (0<a<b) and (c>2b).  Then (r>p+q), and

\[
\frac{M}{t^2}\to ab,
\qquad
\frac ht\to\frac{a+b+c}{2}.
\]

Also (K=\Theta(t)), while

\[
0\le R<2s_0=O(t).
\]

Thus (R/K=O(1)) and

\[
\frac Bt\to a+b.
\]

The numerator of the finite bound divided by (t^3) tends to

\[
ab\left(\frac c2-b\right),
\]

while the denominator divided by (t) tends to

\[
\frac{a+b+c}{2}+2(a+b)
=\frac{c+5a+5b}{2}.
\]

Consequently

\[
\boxed{
\liminf_{t\to\infty}
\frac{D}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\]

For ((a,b,c)=(1,2,5)), the coefficient is

\[
\frac{1\cdot2\cdot(5-4)}{5+5+10}=\frac1{10},
\]

as claimed.

---

## 10. Scope

The proof disproves the proposed dominant-ray local theorem DRAY.  It does
not disprove the global Boolean contiguous-OR width conjecture, because
DRAY was only one sufficient product-box route to that conjecture.

No source repair is required for correctness.  The only recommended edit
is the clarifying phrase in Lemma 5 identified above.
