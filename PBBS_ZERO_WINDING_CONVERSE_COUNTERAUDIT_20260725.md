# Counteraudit: the proposed primitive zero-winding converse is false

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, or web search
is used.

## 0. Verdict

The converse asserted in
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md` is false.
In particular,

\[
 d(D)=1
 \quad\not\Longrightarrow\quad
 \text{a zero-winding return at gap }2\operatorname{ht}(D)+1.
\]

The sector shift in its Lemma 2.1 cannot in general be iterated through the
full height.  A forest transported from a \(B\)-sector into an \(A\)-sector
can reach the global height before the displayed spine.  The proof checks
its relative height at the root seam but omits the depth at which that
forest later sits.

Consequently the Catalan-positive family in its Section 4, the packing
lower bound in Section 5, and the claimed disproof of \((RP_A)\) do not
follow.

## 1. Exact counterexample

Take the semilength-five Dyck word

\[
 D_0=1110011000.
 \tag{1.1}
\]

It is primitive and has height three.  Therefore its canonical terminal
suffix is empty and

\[
 d(D_0)=1.
 \tag{1.2}
\]

Recall that, for the first-maximum factorization

\[
 D=P1R0S,
\]

one has

\[
 \delta(D)=|P|+1,
 \qquad d(D)=|S|+1,
 \qquad \tau D=S1P0R.
 \tag{1.3}
\]

For \(D_0\), the first maximum-reaching step is the third step and the
first subsequent return to zero is the final step.  Thus

\[
 D_0=(11)1(001100)0,
\]

and hence

\[
 (\delta(D_0),d(D_0))=(3,1),
 \qquad
 D_1:=\tau D_0=1110001100.
 \tag{1.4}
\]

For \(D_1\), the first maximum is again reached at step three, but its
first subsequent return is at step six.  Therefore

\[
 D_1=(11)1(00)0(1100),
\]

so

\[
 (\delta(D_1),d(D_1))=(3,5),
 \qquad
 D_2:=\tau D_1=1100111000.
 \tag{1.5}
\]

Finally, \(D_2\) first reaches its maximum at step seven and first returns
to zero at the final step:

\[
 D_2=(110011)1(00)0.
\]

Consequently

\[
 (\delta(D_2),d(D_2))=(7,1),
 \qquad
 D_3:=\tau D_2=1110011000=D_0.
 \tag{1.6}
\]

The zero-winding return equation at \(s=3=\operatorname{ht}(D_0)\) would
require

\[
 d(D_0)+d(D_1)+d(D_2)=\delta(D_3).
\]

Instead,

\[
 1+5+1=7\ne3=\delta(D_3),
 \tag{1.7}
\]

and the two sides are not congruent modulo \(N=11\).  At the two proper
times the corresponding comparisons are

\[
 1\ne3,
 \qquad
 1+5=6\ne7.
\]

Thus the primitive height-three root (1.1) has no zero-winding return at
gap seven, disproving the asserted converse.

## 2. Location of the sector-shift error

For (1.1), the first deepest spine has a later height-two forest in one of
its \(B\)-sectors.  During the successive formal shifts this forest is
transported into an \(A\)-sector at positive depth.  Its relative height is
strictly below three, as observed in the proposed proof, but after adding
the depth of its new attachment it reaches total height three.  It then
contains a deepest leaf before the displayed spine.

Thus the implication

\[
 \text{relative height}<h
 \quad\Longrightarrow\quad
 \text{does not pre-empt the height-}h\text{ spine}
\]

used in Lemma 2.1 is invalid away from the root.  The correct condition for
a forest attached at depth \(i\) is that its relative height be strictly
less than \(h-i\).  That stronger inequality is not supplied by the
hypothesis \(B_0=\varnothing\).

The failure is visible in (1.4)--(1.6): the displayed formal spine survives
the first shifts, but after the transported forest reaches the appropriate
positive-depth \(A\)-sector the canonical first deepest spine changes, and
the claimed sector recursion no longer describes the canonical
factorization.

## 3. Independent consistency check from the gap-seven classification

Simultaneous peak deletion of (1.1) removes the peaks in positions
\(3,4\) and \(7,8\), giving

\[
 \partial D_0=110100.
 \tag{3.1}
\]

The proved complete gap-seven classification in Theorem 18.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` requires

\[
 \partial D=(10)^{d-2}1100.
\]

Here \(\partial D_0\) has semilength \(d=3\), for which the required word
would be

\[
 (10)1100=101100,
\]

not (3.1).  The exact block-rotation calculation above therefore agrees
with the existing gap-seven classification.

## 4. Consequence for the requested seam pivot

The proposed Catalan-dense primitive family is not established.  A
seam/fusion theorem cannot be required on the basis of that report until a
correct family of zero-winding roots with Catalan-positive Gaussian mass is
proved.  The authoritative status therefore reverts to the earlier
residence problem; neither \((RP_A)\) nor its negation follows from the
invalid primitive converse.

## 5. Audit of the two downstream counting steps

The failure occurs before the asymptotic and deck arguments.  Those two
arguments are correct as conditional statements.

First, if \(C_L(n)\) counts semilength-\(n\) Dyck paths of height at most
\(L\), then the path-graph spectral expansion is

\[
 C_L(n)=\frac{2}{L+2}\sum_{j=1}^{L+1}
 \sin^2\!\frac{\pi j}{L+2}
 \left(2\cos\frac{\pi j}{L+2}\right)^{2n}.
 \tag{5.1}
\]

For \(L=\lceil A\sqrt r\rceil-2\) and \(n=r-1\), retain the positive
\(j=1\) summand.  With \(x=\pi/(L+2)\), for all sufficiently large \(r\),

\[
 \sin x\ge \frac{2x}{\pi},
 \qquad \log\cos x\ge -x^2.
\]

Consequently

\[
 C_L(r-1)
 \ge \frac{8}{(L+2)^3}4^{r-1}
       \exp\!\left(-\frac{2\pi^2(r-1)}{(L+2)^2}\right)
 \ge c_A4^rr^{-3/2}
 \ge c_A'\operatorname{Cat}_r.
 \tag{5.2}
\]

Thus the asserted Gaussian Catalan mass of the *primitive words* is real;
what is false is that all those words start returns.

Second, suppose hypothetically that \(R\) quotient roots on \(\tau\)-cycles
longer than \(H+1\) did start return intervals of at most \(H+1\) quotient
edges.  A chosen oriented interval can meet only intervals whose starts lie
among the \(H\) preceding starts, its own start, and the \(H\) following
starts.  Greedy selection therefore gives at least

\[
 \frac{R}{2H+1}
 \tag{5.3}
\]

pairwise quotient-edge-disjoint intervals.  Each such interval uses distinct
quotient edges.  Its \(N\) deck translates use distinct lifts of every one
of those edges and hence are mutually edge-disjoint.  Quotient-edge-disjoint
intervals have disjoint lift families.  Therefore the physical packing is
at least

\[
 N\frac{R}{2H+1}.
 \tag{5.4}
\]

Hence the quotient-to-physical multiplication in the retracted report is
also valid conditional on its nonexistent Catalan family of return starts.
There is no independent defect in the coefficient or in the long-cycle
qualification that could rescue or further weaken the claim.

The exact proved boundary is therefore:

\[
 \boxed{
 \text{Gaussian-many primitive roots exist, but Gaussian-many
 zero-winding return roots have not been proved.}}
 \tag{5.5}
\]

## 6. The corrected no-preemption sector cone is negligible

There is a precise strengthening of \(d(D)=1\) under which the proposed
sector proof does work.  It also shows why merely repairing Lemma 2.1 by a
clearance hypothesis does not yield the claimed Catalan obstruction.

For an ordered forest \(F\), let \(\operatorname{fht}(F)\) be its maximum
height measured from its attachment vertex, with
\(\operatorname{fht}(\varnothing)=0\).  Retain the first-deepest-spine
sectors \(A_i,B_i\), \(0\le i<h\), from the retracted report.  Consider the
formal arrays

\[
 B_i^{(j)}=
 \begin{cases}B_{i+j},&i+j<h,\\ \varnothing,&i+j\ge h,\end{cases}
 \tag{6.1}
\]

and

\[
 A_i^{(j)}=
 \begin{cases}
 B_{j-1-i},&i<j,\\
 A_{i-j},&i\ge j.
 \end{cases}
 \tag{6.2}
\]

### Proposition 6.1 (exact full-transport criterion)

The displayed height-\(h\) spine remains the canonical first deepest spine
through every formal shift \(0\le j\le h\) if and only if

\[
 \boxed{
 A_i=\varnothing\quad(0\le i<h),
 \qquad
 \operatorname{fht}(B_i)\le i\quad(0\le i<h).
 }
 \tag{6.3}
\]

Every word satisfying (6.3) starts a consecutive zero-winding return at
gap \(2h+1\).

#### Proof

At depth \(i\), a forest before the displayed spine may not reach total
height \(h\), whereas a forest after it may tie the spine.  Thus the exact
first-deepest conditions for the formal arrays are

\[
 \operatorname{fht}(A_i^{(j)})<h-i,
 \qquad
 \operatorname{fht}(B_i^{(j)})\le h-i.
 \tag{6.4}
\]

The second inequality follows automatically from the original attachment
bound on \(B_{i+j}\).  In the second branch of (6.2), fix \(t=i-j\) and
let \(j\) increase to \(h-1-t\).  Then (6.4) becomes
\(\operatorname{fht}(A_t)<1\), which is equivalent to
\(A_t=\varnothing\).  In the first branch, write
\(t=j-1-i\) and let \(j\) increase to \(h\).  The last inequality is

\[
 \operatorname{fht}(B_t)<t+1,
\]

equivalently \(\operatorname{fht}(B_t)\le t\).  These terminal
inequalities imply all the earlier ones, because their right-hand sides are
larger.  This proves the equivalence in (6.3), and also inductively justifies
every formal sector update as the canonical update.

Under (6.3), the calculation in the proposed proof is now legitimate.  If
\(C_j=\sum_{t<j}d(D_t)\), then for \(j<h\),

\[
 \delta(D_j)-C_j=h-j>0,
 \tag{6.5}
\]

while \(\delta(D_h)=C_h\).  Both quantities lie strictly between \(0\)
and \(N\) at every proper time, so the same congruence check as in Theorem
3.1 gives a first zero-winding return at gap \(2h+1\).  \(\square\)

The cone (6.3) has an exact generating function.  Let \(G_{r,h}\) be the
number of its words of semilength \(r\) and height \(h\).  The spine uses
\(h\) edges, and \(B_i\) is an arbitrary Dyck forest of height at most
\(i\).  Hence

\[
 G_{r,h}=[z^{r-h}]\prod_{i=0}^{h-1}C_i(z).
 \tag{6.6}
\]

Write \(F_0=F_1=1\) and

\[
 F_{j+1}=F_j-zF_{j-1}.
\]

Since \(C_i=F_i/F_{i+1}\), (6.6) telescopes to

\[
 \boxed{G_{r,h}=[z^{r-h}]\frac1{F_h(z)}.}
 \tag{6.7}
\]

### Proposition 6.2 (the corrected cone has sub-Catalan mass)

For every fixed \(A>0\),

\[
 \boxed{
 \sum_{1\le h\le A\sqrt r}G_{r,h}=o_A(\operatorname{Cat}_r).
 }
 \tag{6.8}
\]

#### Proof

All coefficients in (6.6) are nonnegative.  The recurrence gives

\[
 F_h(1/4)=\frac{h+1}{2^h}.
\]

Evaluation at \(z=1/4\) therefore yields

\[
 G_{r,h}\le 4^{r-h}\frac{2^h}{h+1}
 =\frac{4^r}{2^h(h+1)}.
 \tag{6.9}
\]

On the other hand, these words are height-\(h\) Dyck paths, so
\(G_{r,h}\le C_h(r)\).  Formula (5.1), with the spectral weights summed,
gives the uniform bound

\[
 C_h(r)
 \le4^r\cos^{2r}\!\frac{\pi}{h+2}
 \le4^r\exp\!\left(-c\frac r{(h+2)^2}\right)
 \tag{6.10}
\]

for an absolute \(c>0\).  Put \(K=4\) and split at
\(h=K\log_2 r\).  By (6.10), the part below the split is at most

\[
 O(\log r)4^r
 \exp\!\left(-c'\frac r{\log^2r}\right)
 =o(\operatorname{Cat}_r).
\]

By (6.9), the remaining part, even if extended to all \(h\), is at most

\[
 4^r\sum_{h\ge4\log_2r}2^{-h}
 =O(4^rr^{-4})
 =o(\operatorname{Cat}_r).
\]

This proves (6.8).  \(\square\)

Thus the strongest direct repair of the erroneous sector iteration gives a
genuine return family, but one far too small to refute \((RP_A)\).  Any
counterexample to \((RP_A)\) must exploit canonical spine changes rather
than exclude them.
