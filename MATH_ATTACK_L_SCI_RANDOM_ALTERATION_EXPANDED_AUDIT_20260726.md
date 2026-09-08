# Adversarial audit of the expanded SCI random-alteration report

Date: 2026-07-26

Audited source:
`MATH_ATTACK_L_SCI_RANDOM_ALTERATION_20260726.md`, including Sections 10--16.

Method: pure mathematics only.

## 0. Verdict

The mathematical core is sound. In particular, the exact dual, exact
collision decomposition, pair-codegree formula, corrected cutoff estimates,
crossing-grid construction, and capacity-nibble implication all agree with
Sections 0--9 after the corrections below.

There are two required mathematical edits:

1. Section 13 reuses \(\alpha\), which was already fixed as
   \(1+H/h>1\), for a cutoff exponent in \((1/2,1)\). Rename the cutoff
   exponent \(\beta\) everywhere in Sections 13 and 16.
2. Proposition 15.1 must assume \(I\ge W\). The displayed hypothesis
   \(I=W+o(W)\) permits \(I<W\), in which case a middle-layer floor quota is
   zero and the claim that every quota is at least one is false. It suffices
   to take the least multiple of \(2h\) not below \(W\).

There are also three required scope edits:

3. Rename Section 15 from “The exact positive successor” to “A precise
   sufficient successor.” Condition (15.2) is explicitly stronger than SCI
   and is not proved necessary for a successful correlated process.
4. Replace “the correct form of any capacity-respecting nibble” by “one
   sufficient aggregate form for a capacity-respecting nibble.” A family can
   have \(o(W)\) holes while having large \(L^1\) distance from a prescribed
   floor/ceiling quota vector.
5. In the final paragraph, replace “the only viable probabilistic successor”
   by “a viable probabilistic successor isolated by this audit,” and replace
   the generic-black-box closure by the precise statement that the audited
   criteria requiring vanishing rank times normalized pair codegree, or
   diverging full-codegree roots, do not apply. No theorem rules out every
   future generic correlated theorem, partial-resampling method, or
   deterministic construction.

With those edits, no aggregate \(o(W)\) assertion in Sections 10--16 is
incorrect.

## 1. Sections 10--11: valid

### Exact dual

The singleton columns give the dual caps \(y_S\le1\). Averaging is valid
because the coordinate group is transitive on the strip catalogue and on
each signed layer. An invariant strip constraint is

\[
 2h\left(a_0+\sum_{q=1}^H(a_q^-+a_q^+)\right)
 \le2h+2H.
\]

The residual capacity after putting weight one on the middle layer is
\(H/h<1\), and the largest remaining layer size is \(N_1\). Hence

\[
 \tau^*=W+(H/h)N_1
\]

globally, not only among invariant duals. The complementary-slackness ledger
is exact: the middle and both signed depth-one rows are tight under
\(x_C=1/D_1\), all deeper rows are strictly slack, and every strip constraint
is tight under (10.9).

### Collision decomposition

For a signed layer of size \(N\), total incidence \(I\), and support size
\(U\),

\[
 N-U=(N-I)_++\min(I,N)-U.
\]

Thus (11.3)--(11.5) are identities. The continuous baseline has its unique
minimum at \(I=N_1\): immediately below \(N_1\) its slope is
\((1+H/h)-3<0\), and immediately above it its slope is \(H/h>0\).
Restricting to the grid \(2h\mathbb Z\) costs at most
\(O(Hh)=o(W)\). Equation (11.9) is also exact:

\[
 F(W)-\tau^*=(H/h)(W-N_1).
\]

No hidden multiplication by the number of ranks occurs in these statements.

## 2. Section 12: valid, with one notation clarification

For signed indices, the report should explicitly declare

\[
 D_d:=D_{|d|}=\frac{(m+d)!(m-d)!}{2(m-h)!^2}.
\]

This is only a notation clarification; the formulas use this convention
correctly.

Fixing \(S\in V_d\), two active circular intervals of lengths \(h+d\) and
\(h+e\) have intersection range

\[
 \max(0,d+e)\le p\le h+\min(d,e).
\]

The number of relative phases is respectively \(|d-e|+1\) at maximum
overlap, \(|d+e|+1\) at minimum overlap, and two in the interior. There are

\[
 \binom{m+d}{u}\binom{m-d}{v}
\]

targets with the specified differences from \(S\). Double counting therefore
proves (12.6), and cancellation with the degree formula proves (12.7).

The same-rank and nested specializations (12.8)--(12.10) are correct. For a
nested gap \(r\), whichever endpoint has smaller degree supplies a binomial
denominator at least

\[
 \binom{m-H+r}{r}.
\]

This is maximized at \(r=1\), giving (12.11). In a nonnested pair both
difference binomials are nontrivial, so (12.12) follows. The adjacent-rank
sum (12.13) is exact: each occurrence has its two endpoint extensions.

## 3. Section 13: valid estimates, but notation and one proof line must be fixed

Use \(\beta\in(1/2,1)\), not \(\alpha\), and set

\[
 H=\lceil\sqrt{\beta m\log m}\rceil.
\]

Then the claimed estimates are correct:

\[
 R_{m,H}/W=O(m^{1/2-\beta}),\qquad
 D_H/D_0=(1+o(1))m^\beta.
\]

The proof of the absolute maximum pair codegree should be written explicitly.
Corollary 12.2 gives

\[
 \frac{2D_{H-1}}{m-H+1}
 \le \Delta_2
 \le \frac{2D_H}{m-H+1}.                           \tag{A.1}
\]

Since

\[
 D_{H-1}/D_H=\exp(-(2H-1)/m+o(1))=1+o(1),
\]

(A.1) proves

\[
 \Delta_2/D_0=(2+o(1))m^{\beta-1}.
\]

The current sentence “Equations (13.1)--(13.2) prove the other assertions”
does not itself state this upper-bound argument. Adding (A.1) makes
Proposition 13.1 theorem-grade.

The compiler and random-alteration estimates survive the new cutoff:
\(H/\sqrt m\to\infty\), the Gaussian core remains far inside the cutoff,
\(H=o(m^{2/3})\), and \(H/h=o(1)\).

The growing-edge calculation is correct:

\[
 2h(2H+1)\frac2{m-H+1}\asymp hH/m.
\]

The crossing grid contains \((s+1)^2\) distinct targets. Its smallest and
largest members leave \(h-s\) freely ordered active coordinates inside and
outside, respectively. Dividing the resulting oriented descriptions by at
most \(4h\) proves (13.10). The falling-factorial cancellation in (13.11) is
correct, and for \(s=\lceil\log m\rceil\),

\[
 \frac{2s\log m+O(\log m)}{(s+1)^2-1}=2+o(1),
\]

which proves (13.12).

What (13.12) rigorously excludes is a criterion demanding divergence of all
quantities

\[
 (\Delta_1/\Delta_j)^{1/(j-1)}.
\]

It is not a no-go for every theorem that uses higher codegrees in some other
structured way.

## 4. Section 14: valid and appropriately qualified

A full-band matching uses at most \(N_H/(2h)\) strips because every strip
has \(2h\) outer-layer targets. It consequently covers at most \(N_H=o(W)\)
middle targets. The capacity identity

\[
 D_d/(W/N_{|d|})=D_0
\]

and the exact rank-one floor/ceiling count are correct. The middle same-rank
calculation

\[
 (2h)^2\Delta_2/D_0=8h^2/m^2=o(1)
\]

is also correct for \(h=m^{3/4+o(1)}\).

The qualification in (14.2), “do not presently compose,” is essential and
should be retained.

## 5. Section 15: sufficient after adding \(I\ge W\)

Replace its opening by, for example:

> Let \(I\) be the least multiple of \(2h\) satisfying \(I\ge W\). Then
> \(I=W+O(h)=W+o(W)\).

More generally, \(I\ge W\), \(2h\mid I\), and \(I=W+o(W)\) suffice. Then
every quotient \(I/N_{|d|}\) is at least one, so every quota in (15.1) is at
least one. Every hole contributes at least one to the aggregate deviation
in (15.2). Hence total holes are \(o(W)\), while

\[
 (1+H/h)I=W+o(W).
\]

The implication to SCI is valid.

Condition (15.2), however, is not equivalent to SCI. It controls overload
placement as well as holes and ties the family to one prescribed quota vector.
SCI only requires aggregate holes \(o(W)\). Therefore the heading and the
claim about the “correct form of any” capacity nibble must be weakened as in
the verdict.

## 6. Aggregate \(o(W)\) audit

The following conversions are valid:

1. \(O(Hh)=o(W)\) in (11.6), since \(Hh\) is polynomial and \(W\) is
   exponential.
2. The corrected Boolean tail is \(o(W)\) exactly when fixed
   \(\beta>1/2\).
3. In Proposition 15.1, (15.2) is already summed over every signed rank, so
   no missing factor \(H\) occurs.
4. The block toll is \((H/h)I=o(W)\).

The earlier stability result (6.21) remains deliberately only rankwise:
\(B_q=o(W)\) for each fixed signed rank. It must not be summed over all
\(2H+1\) ranks without an \(o(1/H)\) residual-mass bound. The report states
this caveat correctly.

## 7. Final corrected boundary

After the required edits, the report proves that the specifically audited
diffuse product measures, uniform fixed-size sampling, charged Poisson
schemes, ordinary full-band matching, and codegree criteria described in
Sections 13--14 do not yield SCI. It does not prove a generic probabilistic
no-go. Proposition 15.1 isolates a strong sufficient target for one possible
correlated capacity process; it is not the uniquely necessary successor.
