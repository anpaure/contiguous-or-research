# Rank-centre classification for contiguous equal-cube cores

Date: 2026-07-25

## 0. Verdict

Put

\[
Q_R=[0,R]^3,
\qquad
W_R=w(Q_R)=\left\lceil\frac{3(R+1)^2}{4}\right\rceil.
\]

Suppose a universal range-maximum word has the form

\[
U_R=P\,C\,S,
\]

and every letter of the contiguous core \(C\) lies in a translated equal
subcube

\[
B=\delta+Q_{R-k},
\qquad
0\le \delta_i\le k,
\qquad
s=\delta_1+\delta_2+\delta_3.
\]

For \(R\ge3k\), define

\[
f_R(q)=\frac q2(2R+3-q),
\qquad
q=\max\{s,3k-s\}.
\]

Then

\[
\boxed{|P|+|S|\ge f_R(q).}
\tag{0.1}
\]

The recursive width budget is

\[
\Delta_kW_R:=W_R-W_{R-k}
=\frac32kR-\frac34k^2+\frac32k+O(1).
\tag{0.2}
\]

Writing

\[
u=\left|s-\frac{3k}{2}\right|,
\]

the difference between (0.1) and (0.2) is

\[
uR+O_k(1).
\tag{0.3}
\]

Consequently, for fixed \(k\), an outside ledger

\[
|P|+|S|\le \Delta_kW_R+o(R)
\]

is possible only if

\[
\boxed{k\text{ is even and }s=3k/2.}
\tag{0.4}
\]

This completely closes every off-centre fixed-thickness contiguous-core
recurrence.  The centred case is also impossible, for a second
architecture-free reason.  Put

\[
M_s(R)=f_R(s),
\tag{0.5}
\]

and

\[
L_s(R)=\binom{R+2}{3}-\binom{R-s+2}{3}-1.
\tag{0.6}
\]

If \(s>0\), all targets having some coordinate below \(\delta_i\) avoid
the core.  Their rank-\(R\) antichain has size \(M_s(R)\), and their
nonzero lower ranks contain exactly \(L_s(R)\) targets.  The endpoint
capacity lemma gives the exact additional toll

\[
\boxed{
|P|+|S|\ge
M_s(R)+
\left\lceil\frac{L_s(R)}{M_s(R)+R-1}\right\rceil.}
\tag{0.7}
\]

For fixed \(s\), the second term is

\[
\left(\frac{s}{2(s+1)}+o(1)\right)R.
\tag{0.8}
\]

When \(s=3k/2\), the first term differs from the recursive width budget
by only \(O_k(1)\).  Hence (0.7) closes every centred fixed-thickness
recurrence as well.  Therefore:

\[
\boxed{\text{No fixed-thickness contiguous translated core can yield
coefficient one.}}
\tag{0.9}
\]

For example, the formerly surviving centred four-step candidate has
\(k=4,\delta=(2,2,2),s=6\).  Formula (0.7) gives

\[
|P|+|S|\ge
6R-9+
\left\lceil
\frac{\binom{R+2}{3}-\binom{R-4}{3}-1}{7R-10}
\right\rceil
=\left(\frac{45}{7}+o(1)\right)R,
\tag{0.10}
\]

strictly above

\[
W_R-W_{R-4}=6R-6.
\]

For centred \(2\le k=o(R)\), (0.7) contributes at least
\((3/8-o(1))R\); if also \(k\to\infty\), its sharper value is
\((1/2-o(1))R\).  Moreover

\[
M_{3k/2}(R)-\Delta_kW_R=\frac{3k(2-k)}8.
\tag{0.11}
\]

Hence a centred core with \(k/\sqrt R\to c\) is still impossible whenever

\[
c<\frac{2}{\sqrt3};
\tag{0.12}
\]

in particular all \(k=o(\sqrt R)\) are excluded.  The surviving local
lane must use a segmented core/cross-window braid, or a genuinely
mesoscopic core of at least \((2/\sqrt3-o(1))\sqrt R\) thickness with a
new fusion argument.

---

## 1. Exterior antichains inject into outside endpoints

### Lemma 1.1

Let \(W=P\,C\,S\) be a word in a finite product of chains.  Suppose all
letters of \(C\) lie in a join-closed set \(B\).  If \(\mathcal A\) is
an antichain disjoint from \(B\), and every member of \(\mathcal A\) is
represented by a contiguous factor of \(W\), then

\[
\boxed{|P|+|S|\ge|\mathcal A|.}
\tag{1.1}
\]

### Proof

Choose one witness \(I_x=[\ell_x,r_x]\) for every \(x\in\mathcal A\).
No witness lies wholly in \(C\), because the maximum of letters in the
join-closed set \(B\) again belongs to \(B\).

If \(r_x\) lies in \(S\), assign \(x\) to that right endpoint.  Otherwise
the witness does not end in \(S\); since it is not wholly in \(C\), it
must start in \(P\), and we assign \(x\) to its left endpoint.  A witness
meeting both outside pieces is assigned only to its suffix endpoint, so
the prefix and suffix image sets are disjoint.

Two witnesses assigned to one prefix position have the same left endpoint
and are nested.  Their maxima are comparable, contrary to the fact that
they are distinct members of an antichain.  The same argument with common
right endpoints applies in the suffix.  The assignment is injective into
the \(|P|+|S|\) outside positions, proving (1.1). \(\square\)

No old selected witness is assumed to survive.  A new witness may cross
the entire core; the endpoint assignment still applies.

---

## 2. Exact lower- and upper-shoulder counts

The rank generating polynomial of \(B\) is

\[
x^s(1+x+\cdots+x^{R-k})^3.
\]

Both ranks \(R\) and \(2R\) of \(Q_R\) have size

\[
\binom{R+2}{2}.
\tag{2.1}
\]

We use whichever shoulder lies farther from the centre of the translated
core.

### Lower shoulder

If \(s\ge k\), the coefficient of rank \(R\) in \(B\) is

\[
\binom{R-s+2}{2}.
\]

Indeed the untranslated rank is \(R-s\), which lies between \(0\) and
\(R-k\), so no coordinate cap is active.  Therefore the rank-\(R\)
antichain outside \(B\) has size

\[
\binom{R+2}{2}-\binom{R-s+2}{2}
=f_R(s).
\tag{2.2}
\]

### Upper shoulder

If \(s\le2k\), the coefficient of rank \(2R\) in \(B\) equals the rank

\[
3(R-k)-(2R-s)=R-(3k-s)
\]

coefficient of \(Q_{R-k}\), by complementation inside the core.  Since
\(R\ge3k\), this rank is nonnegative; since \(s\le2k\), it is at most
\(R-k\).  Hence the caps are again inactive and the core count is

\[
\binom{R-(3k-s)+2}{2}.
\]

The exterior rank-\(2R\) antichain consequently has size

\[
\binom{R+2}{2}
-\binom{R-(3k-s)+2}{2}
=f_R(3k-s).
\tag{2.3}
\]

If \(s<k\), then \(3k-s>s\), and (2.3) supplies (0.1).  If
\(k\le s\le2k\), both (2.2) and (2.3) apply, so their maximum supplies
(0.1).  If \(s>2k\), then \(s>3k-s\), and (2.2) supplies (0.1).
Lemma 1.1 converts these exterior antichains into the stated outside-word
bound.

---

## 3. Exact comparison with the width ledger

Write

\[
W_t=\frac34t^2+\frac32t+c_t,
\qquad
c_t=\begin{cases}1,&t\text{ even},\\[1mm]3/4,&t\text{ odd}.
\end{cases}
\tag{3.1}
\]

Then

\[
\Delta_kW_R
=\frac32kR-\frac34k^2+\frac32k+c_R-c_{R-k}.
\tag{3.2}
\]

Put

\[
q=\max\{s,3k-s\}=\frac{3k}{2}+u,
\qquad
u=\left|s-\frac{3k}{2}\right|.
\]

Since

\[
f_R(q)=qR+\frac32q-\frac12q^2,
\]

direct subtraction of (3.2) gives

\[
\begin{split}
f_R(q)-\Delta_kW_R
={}&u\left(R+\frac32-\frac{3k}{2}\right)-\frac{u^2}{2}\\
&+\frac{3k}{4}-\frac{3k^2}{8}-(c_R-c_{R-k}).
\end{split}
\tag{3.3}
\]

For fixed \(k\), the second line and every term except \(uR\) are
bounded independently of \(R\).  Thus any \(u>0\) forces an additional
\(uR+O_k(1)\) positions beyond the recursive width ledger.  Since \(s\)
is integral, \(u=0\) is possible exactly when \(k\) is even and
\(s=3k/2\).  This proves (0.3)--(0.4).

For the asymmetric shift \(k=2,s=1\), (2.3) specializes to

\[
|P|+|S|\ge f_R(5)=5R-5,
\]

so its proposed \(3R+o(R)\) outside ledger misses by \(2R-o(R)\).

---

## 4. Lower-boundary endpoint toll

Assume \(s>0\), and define the lower-boundary down-set

\[
\mathcal L_\delta
=\{x\in Q_R:x_i<\delta_i\text{ for at least one }i\}\setminus\{0\}.
\tag{4.1}
\]

Every target in \(\mathcal L_\delta\) has every witness disjoint from
the core: a core letter is at least \(\delta\), while the target is
strictly below \(\delta\) in some coordinate.  Such a witness lies wholly
in \(P\) or wholly in \(S\).  After deleting \(C\) and concatenating
\(P,S\), all selected witnesses remain contiguous.  Thus the outside word
itself covers \(\mathcal L_\delta\).

The rank-\(R\) part of this family has exact size

\[
M_s(R)
=\binom{R+2}{2}-\binom{R-s+2}{2}
=f_R(s).
\tag{4.2}
\]

Indeed, after translating by \(\delta\), the complementary inner family
has rank \(R-s\); its coordinate caps \(R-\delta_i\) are inactive because
\(R-s\le R-\delta_i\) for every \(i\).

The number of nonzero lower-rank targets in \(\mathcal L_\delta\) is

\[
L_s(R)
=\binom{R+2}{3}-\binom{R-s+2}{3}-1.
\tag{4.3}
\]

Here \(\binom{R+2}{3}\) counts all triples of rank at most \(R-1\),
including zero.  Translating the inner family changes the rank cutoff to
\(R-s-1\), giving \(\binom{R-s+2}{3}\); the same cap check applies.
The final minus one deletes the global zero.

### Lemma 4.1 (rank-capped outside starts)

If a word of length \(N=M+D\) covers \(\mathcal L_\delta\), where
\(M=M_s(R)\), then

\[
\boxed{L_s(R)\le(M+R-1)D.}
\tag{4.4}
\]

### Proof

Choose one witness for every rank-\(R\) target and order them by left
endpoint.  Their left endpoints and right endpoints are both strict and
in the same order, because containment would make two distinct equal-rank
maxima comparable.  Thus

\[
I_i=[i+\alpha_i,i+\beta_i],
\qquad
0\le\alpha_i\le\beta_i\le D,
\]

with both offset sequences nondecreasing.  If
\(d_i=\beta_i-\alpha_i\), then

\[
\sum_i d_i\le MD.
\tag{4.5}
\]

Group selected witnesses of the lower-rank targets by their left endpoint.
At a selected rank-\(R\) start, a lower witness must end before the
corresponding rank-\(R\) witness ends; otherwise it contains that witness.
The selected starts therefore supply at most \(\sum_i d_i\) lower targets.
There are exactly \(D\) unused starts.  At one fixed start, maxima obtained
by extending the right endpoint form a chain and contain at most one target
in each rank \(1,\ldots,R-1\).  Hence an unused start supplies at most
\(R-1\) lower targets.  Combining this with (4.5) proves (4.4). \(\square\)

Taking the integer ceiling in (4.4) proves (0.7).  For fixed \(s\),

\[
L_s(R)=\frac s2R^2+O_s(R),
\qquad
M_s(R)+R-1=(s+1)R+O_s(1),
\]

so the additional term is exactly (0.8).  More uniformly, if
\(s=o(R)\), it equals

\[
\frac{s}{2(s+1)}R+O(s).
\tag{4.6}
\]

If the shoulder classification leaves the centred case
\(s=3k/2\), then \(k\) is even, the parity constants cancel, and
formula (3.3) gives the exact identity

\[
M_s(R)-\Delta_kW_R=\frac{3k(2-k)}8.
\]

Equations (0.7) and (4.6) therefore exclude every fixed \(k\).  Uniformly
for centred \(2\le k=o(R)\), the endpoint term is at least
\((3/8-o(1))R\), which excludes \(k=o(\sqrt R)\).  If
\(k/\sqrt R\to c>0\), then \(k\to\infty\), \(s=3k/2\), and (3.3) with
\(u=0\) gives

\[
M_s(R)-\Delta_kW_R=-\frac38c^2R+o(R),
\]

and (4.6) gives an additional \((1/2-o(1))R\).  Their sum is positive
for \(c<2/\sqrt3\), proving (0.11)--(0.12).

---

## 5. A sharper centred thickness-two bound

The general endpoint toll already excludes \(k=2,s=3\).  The exact
two-zero-face theorem gives a stronger value in this smallest case.

Every vector \(\delta\in\{0,1,2\}^3\) with coordinate sum three has at
least two positive coordinates.  Relabel them as coordinates one and two.
Every core letter is positive in both.  Therefore a witness for a target
with first or second coordinate zero avoids the core.  After deleting
\(C\) and concatenating \(P,S\), all such selected witnesses remain
contiguous.  The outside word consequently covers

\[
\mathcal F_R={(x,0,z):0\le x,z\le R\}
\cup\{(0,y,z):0\le y,z\le R\}\setminus\{0\}.
\tag{5.1}
\]

We prove that every word covering \(\mathcal F_R\) has length at least
\(4R-1\).  The \(2R\) nonzero pure \(x\)- and \(y\)-axis targets force
\(2R\) distinct literal axis positions.  Fix rows \(x=r\) and \(y=s\).
For each \(1\le z\le R\), choose a witness of \((r,0,z)\) and designate
one occurrence whose third coordinate is \(z\); call it \(P_z\).  Do the
same for \((0,s,z)\), obtaining \(Q_z\).  Each provider family has \(R\)
distinct positions and is disjoint from the pure \(x\)- and \(y\)-axis
positions.

If the chosen \(x\)-row witnesses use \(a_r\) distinct occurrences to
attain their first coordinate, and the \(y\)-row witnesses use \(b_s\)
distinct occurrences to attain their second coordinate, then

\[
|\{P_z\}\cap\{Q_z\}|\le a_rb_s.
\tag{5.2}
\]

To see this, charge a common provider to its ordered pair of designated
row-root occurrences.  For one fixed root pair, at most one provider is
common.  If the \(x\)-root precedes the \(y\)-root and two common providers
of heights \(z<w\) lie between them, the \(x\)-witness of height \(z\)
forces the \(z\)-provider to precede the \(w\)-provider, whereas the
\(y\)-witness of height \(z\), viewed from the opposite root, forces the
reverse order.  A common provider outside the two roots contaminates one
of the two witnesses.  The reversed root order is symmetric.  This proves
(5.2).

Let \(a=\min_r a_r\), \(b=\min_s b_s\).  The pure \(z\)-axis positions,
the row-root families for distinct rows, and the two coordinate types give

\[
N\ge R+\sum_ra_r+\sum_sb_s\ge R(1+a+b).
\]

If \(a+b\ge3\), then \(N\ge4R\).  Otherwise \(a=b=1\).  Choose rows
attaining these minima.  Equation (5.2) and the \(2R\) forced pure
\(x,y\)-axis positions give

\[
N\ge2R+(2R-1)=4R-1.
\]

This proves the sharper bound \(|P|+|S|\ge4R-1\).  (A matching
\(4R-1\) word exists for the two-face family, but only the lower
bound is needed here.)

---

## 6. Exact surviving statement

The contiguous-core recurrence is exhausted at every fixed thickness, and
through the centred mesoscopic range
\(k<(2/\sqrt3-o(1))\sqrt R\).  The smallest known sufficient replacement
is therefore genuinely segmented.

> **Separator-safe two-shell splice (unproved).**  Insert the two new
> height levels through the old word so that, after deleting them, the
> remaining old-letter runs collectively retain an internal witness for
> every old target, while the full word satisfies
> \[
> g_3(t+2)\le g_3(t)+3t+6+O(1).
> \tag{6.1}
> \]

Since \(W_{t+2}-W_t=3t+6\), summing (6.1) separately on the two parities
would give

\[
g_3(t)=W_t+O(t),
\]

and hence the required \(W_t+o(t^2)\) estimate.  Lemma 1.1 does not apply
to this splice because the old translated letters are no longer one
contiguous join-closed factor: new separators split them into several
physical runs.  A boundary witness may then start and end at old positions
while containing new letters between them.

The architecture-free alternative is the cross-window endpoint-reuse gate.
For the rank-\(2t\) antichains of consecutive three-shell windows, every
near-width word must reuse at least

\[
\left(\frac34-o(1)\right)R^2
\]

left endpoints across different windows, and independently the same
number of right endpoints.  This follows by summing the exact shell
antichain sizes and subtracting the \((3/4+o(1))R^2\) available physical
sites; the full calculation is in
`MATH_ATTACK_THREE_SHELL_ENDPOINT_NO_GO_20260725.md`.

Thus the next positive theorem must implement one of two resources which
the present no-go deliberately leaves open: separator-safe old-letter
segmentation, or quadratic two-sided cross-window endpoint sharing.  A
larger contiguous core is not a fixed-scale substitute.
