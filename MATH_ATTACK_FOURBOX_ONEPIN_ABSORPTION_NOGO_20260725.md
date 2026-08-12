# Equal four-box: a one-pin middle-absorption no-go

Date: 2026-07-25

## 0. Result

Retain the notation of `MATH_ATTACK_U5_EQUAL_SURFACE_BRAID_20260725.md`.
Thus

\[
 \mathcal A_r=S_r\times H_r,\qquad
 \mathcal B_r=H_r\times I_r,
\]

the aligned packet-middle antichain has size

\[
 W_r=(r+1)^2+r^2=2r^2+2r+1,
\tag{0.1}
\]

and the literal \(\mathcal A_r\)-interface spine

\[
 F_A=\{a_{t,v}=(h_t;0,v):(t,v)\in J_r\}
\]

has size

\[
 N_r=(2r+1)r-1=2r^2+r-1=W_r-r-2.
\tag{0.2}
\]

Put

\[
 k=k_r=\left\lfloor\frac{r-1}{8}\right\rfloor
\]

and use the sloped interface points

\[
 X_{x,v}=((x,r);0,v),\qquad x+v=r+\sigma,
 \qquad -k\le \sigma\le k.
\tag{0.3}
\]

The common-lift braid keeps every point of \(F_A\) literal and uses the
points (0.3) as its shared child endpoints.  The most direct proposed
middle-queue repair is to let such a literal endpoint also be an endpoint
of an aligned middle witness, with the middle owner obtained by raising
only one coordinate of \(X_{x,v}\).  That repair is impossible at
subquadratic excess.

More precisely, let a packet word have length \(W_r+e\), retain one
designated literal occurrence of every point of \(F_A\), and choose the
sloped-band witnesses and all aligned-middle witnesses.  Let \(b\) be the
number of side-typed absorbed shared endpoints which are **not** of the
following form:

1. the physical endpoint is the designated occurrence of a point in
   (0.3); and
2. the aligned middle owner containing that endpoint differs from that
   point in at most one ambient coordinate.

Then

\[
 \boxed{6e+b\ge \Gamma_r-4r-4,}
\tag{0.4}
\]

where \(\Gamma_r\) is the exact two-child sloped-band toll from U5,

\[
 \Gamma_r=\frac{289}{1728}r^2+O(r).
\tag{0.5}
\]

Consequently, the pure one-pin repair \(b=0\) satisfies

\[
 \boxed{
 e\ge
 \max\left\{0,
 \left\lceil\frac{\Gamma_r-4r-4}{6}\right\rceil
 \right\}
 =\frac{289}{10368}r^2+O(r).}
\tag{0.6}
\]

Conversely, if \(e=o(r^2)\), then necessarily

\[
 \boxed{b\ge
 \left(\frac{289}{1728}-o(1)\right)r^2.}
\tag{0.7}
\]

Thus the existing common-lift surface cannot be completed by merely
attaching its literal portal bases to one-pin middle owners, even with
arbitrary global ordering, arbitrarily long witnesses, arbitrary inserted
letters, and both endpoint orientations.  A near-width completion must
perform a positive-density non-one-pin surgery: it must factor away
interface bases, use middle owners changing at least two coordinates, or
absorb through shared sites outside the displayed interface matching.

## 1. The endpoint absorption ledger

We reproduce the short part of the U5 middle-queue argument needed below.
For the selected sloped-band witnesses, let

\[
 L_A,R_A,L_B,R_B
\]

be their physical left- and right-endpoint sets, and put

\[
 S_L=L_A\cap L_B,\qquad S_R=R_A\cap R_B.
\tag{1.1}
\]

For independently selected witnesses of all \(W_r\) aligned packet-middle
targets, let their endpoint sets be \(Q_L,Q_R\).  Define the side-typed
absorption count

\[
 a=|S_L\cap Q_L|+|S_R\cap Q_R|.
\tag{1.2}
\]

The exact sloped-band endpoint inequalities give

\[
 |L_A|+|R_A|+|L_B|+|R_B|\ge 2W_r+\Gamma_r.
\tag{1.3}
\]

Since each left or right union uses at most \(W_r+e\) physical sites,

\[
 |S_L|+|S_R|\ge \Gamma_r-2e.
\tag{1.4}
\]

The aligned middle targets form an antichain.  Two distinct such targets
cannot have witnesses with a common left endpoint, because the two
intervals would be nested and their maxima comparable; the same is true
on the right.  Hence

\[
 |Q_L|=|Q_R|=W_r.
\tag{1.5}
\]

Only \(e\) physical sites lie outside either middle endpoint queue, so

\[
 |S_L|\le |S_L\cap Q_L|+e,
 \qquad
 |S_R|\le |S_R\cap Q_R|+e.
\]

Together with (1.4), this proves

\[
 \boxed{4e+a\ge\Gamma_r.}
\tag{1.6}
\]

All intersections here are side-typed: a physical site in both the left
and right intersections is counted twice.

## 2. Classification of one-pin owners

Fix a displayed interface point (0.3).  Its rank is

\[
 |X_{x,v}|=r+x+v=2r+\sigma.
\tag{2.1}
\]

If \(\sigma>0\), its designated literal occurrence cannot lie in an
aligned-middle witness: every letter of such a witness is at most its
rank-\(2r\) maximum, whereas \(X_{x,v}\) already has larger rank.

If \(\sigma=0\), then any aligned-middle target above the literal letter
\(X_{x,v}\) must equal \(X_{x,v}\).  The zero-slope points are

\[
 Z_u=((u,r);0,r-u),\qquad 1\le u\le r.
\tag{2.2}
\]

Now let \(\sigma=-d<0\).  Thus

\[
 x+v=r-d,
 \qquad
 X=(x,r,0,v).
\tag{2.3}
\]

If an aligned-middle owner \(M\ge X\) differs from \(X\) in exactly one
coordinate, the total increment is \(d\).  The second coordinate of \(X\)
is already \(r\), so the only possibilities are

\[
 \begin{aligned}
 M^{(1)}&=(x+d,r,0,v),\\
 M^{(3)}&=(x,r,d,v),\\
 M^{(4)}&=(x,r,0,v+d).
 \end{aligned}
\tag{2.4}
\]

The first and third lines of (2.4) after suppressing the superscript,
namely \(M^{(1)}\) and \(M^{(4)}\), both belong to the same size-\(r\)
family (2.2), because respectively

\[
 (x+d)+v=r,
 \qquad
 x+(v+d)=r.
\tag{2.5}
\]

The remaining owner

\[
 \widehat X=M^{(3)}=((x,r);d,v)
\tag{2.6}
\]

lies in \(\mathcal B_r\): its first square point is
\((x,r)=h_{r+x}\in H_r\), and \((d,v)\in I_r\).  Its rank is exactly
\(2r\).

Every selected witness of one target in (2.2) has only one left and one
right endpoint.  Therefore all zero-slope absorptions together with all
absorptions assigned to the lateral owners \(M^{(1)},M^{(4)}\) contribute
at most

\[
 2r
\tag{2.7}
\]

side-typed incidences.  Notice that (2.7) is \(2r\), not \(4r\): both
classes use endpoints of the same \(r\) selected middle witnesses.

## 3. A completion-position lemma for vertical owners

### Lemma 3.1

Suppose \(c\) side-typed absorbed incidences use a designated literal
point \(X\) as in (2.3) and use its vertical owner \(\widehat X\) from
(2.6).  Then the word has at least

\[
 \left\lceil\frac c2\right\rceil
\tag{3.1}
\]

physical positions outside the designated literal \(F_A\)-spine.

#### Proof

Consider first an incidence of left type.  Its selected
\(\widehat X\)-witness starts at the designated literal occurrence of
\(X=(x,r,0,v)\).  Traverse the witness to the right and stop at the first
position whose third coordinate is \(d\).  Such a position exists because
the interval maximum has third coordinate \(d\).

Every letter in the witness is at most

\[
 \widehat X=(x,r,d,v).
\]

The initial literal \(X\) already pins coordinates one, two, and four.
At the stopping position, coordinate three is pinned as well.  Hence the
truncated interval has maximum exactly \(\widehat X\).  Its stopping
position is therefore a right endpoint of an actual
\(\widehat X\)-witness.  For an incidence of right type, traverse left and
obtain analogously a left endpoint of an actual witness.

The stopping position is outside the designated \(F_A\)-spine because its
third coordinate is \(d>0\), while every designated \(F_A\) letter has
third coordinate zero.

One stopping position can serve at most one left-type incidence.  Indeed,
two resulting intervals would have a common right endpoint; they are
nested, so their maxima are comparable.  Both maxima have rank \(2r\), and
distinct vertical owners are distinct, a contradiction.  The same stopping
position can serve at most one right-type incidence, by the common-left
version of the argument.  It therefore serves at most two incidences in
total.  This proves (3.1). \(\square\)

The lemma permits the two incidences served by one stopping position to
come from different depths, and it makes no locality assumption on either
witness.  Thus neither long corridors nor a reordering of the surface
evades it.

## 4. Proof of the tradeoff

There are \(N_r\) distinct designated literal spine positions.  Since the
whole word has length \(W_r+e\), the number of positions outside that
spine is exactly at most

\[
 (W_r+e)-N_r=e+r+2.
\tag{4.1}
\]

Let \(c\) be the number of vertical one-pin absorbed incidences.  Lemma
3.1 and (4.1) give

\[
 c\le 2(e+r+2).
\tag{4.2}
\]

By definition, every absorbed incidence is either exceptional and counted
by \(b\), vertical and counted by \(c\), or belongs to the common
zero-slope/lateral-owner family bounded in (2.7).  Hence

\[
 a\le b+c+2r
 \le b+2e+4r+4.
\tag{4.3}
\]

Insert (4.3) into (1.6):

\[
 \Gamma_r\le4e+a
 \le6e+b+4r+4.
\]

This is (0.4), and (0.6)--(0.7) follow immediately.

For completeness, the exact U5 formulas use
\(k=\lfloor(r-1)/8\rfloor\) and give

\[
 \Gamma_r=\gamma_A(r)+\gamma_B(r),
\]

\[
 \gamma_A(r)=
 \max\left\{0,
 \left\lceil
 \frac{
 2k(r+1)^2+
 k(k+1)(k-12r-4)/3
 }{2r+2k}
 \right\rceil\right\},
\]

\[
 \gamma_B(r)=
 \max\left\{0,
 \left\lceil
 \frac{
 (2+2k)r^2+
 k(k+1)(k-12r+8)/3
 }{2r+2k}
 \right\rceil\right\}.
\]

Since \(k=r/8+O(1)\), each numerator has leading coefficient
\(289/1536\), while the denominator is \((9/4)r+O(1)\).  Thus

\[
 \gamma_A(r)=\gamma_B(r)
 =\frac{289}{3456}r^2+O(r),
\]

which proves (0.5) and the coefficient in (0.6).

## 5. Exact surviving statement

The direct interface-incidence question from U5 is settled positively by
the common-lift braid, but the present theorem closes its smallest literal
middle-absorption repair.  Keeping the entire literal \(F_A\) spine and
raising one pin at each absorbed endpoint cannot yield PACK.

The exact next positive statement is therefore the following genuinely
non-one-pin replacement.

> **Multipin interface replacement (still unproved).**  Replace or factor
> a quadratic number of the designated \(F_A\) literals, and construct
> \(\Gamma_r-o(r^2)\) side-typed shared band endpoints inside the aligned
> middle queues such that a quadratic number of their middle owners either
> differ from the endpoint letter in at least two coordinates or use shared
> sites outside the displayed matching, while preserving all packet
> witnesses in one word of length \(W_r+o(r^2)\).

Equation (0.7) shows that “a quadratic number” cannot be weakened to
\(o(r^2)\) within the retained-interface lane.  This is not an
unrestricted lower bound for PACK: a successful word may factor a positive
density of the interface itself or use multipin owners, and the proof above
does not prohibit either escape.

## 6. Final audit

Two possible ambiguities deserve explicit checks.

First, the zero-slope and lateral one-pin classes really use one common
owner family.  A zero-slope point is

\[
 ((u,r);0,r-u)=Z_u.
\]

For a negative-slope point \(X=(x,r,0,v)\) with
\(x+v=r-d\), raising coordinate one gives \(Z_{x+d}\), since
\(r-(x+d)=v\); raising coordinate four gives \(Z_x\), since
\(r-x=v+d\).  Thus every such owner is one of the same \(r\) targets
\(Z_1,\ldots,Z_r\).  The selected witness of each \(Z_u\) has only its
one left and one right endpoint, so the combined side-typed contribution is
at most \(2r\), even when many band targets use one endpoint site.

Second, the partition used in (4.3) does not assume that a shared band
endpoint is used by the matching target whose value is written at that
site.  An absorbed incidence is only a pair \((q,\mathrm L)\) or
\((q,\mathrm R)\) belonging to the corresponding set intersection in
(1.2).  Its middle owner is unique by (1.5).  If \(q\) is not one of the
designated occurrences (0.3), the incidence is exceptional and is counted
by \(b\), regardless of which child-band witnesses created the sharing.
If it is a designated occurrence, its physical letter is \(X_{x,v}\), so
that letter lies below the unique middle owner.  Positive slope is
impossible, zero slope gives the owner itself, and negative slope is
exhaustively split according to whether the owner changes one coordinate
or at least two.  Hence every term counted by \(a\) occurs exactly in one
of the three classes used in (4.3); no matching-target identification is
being smuggled into the argument.
