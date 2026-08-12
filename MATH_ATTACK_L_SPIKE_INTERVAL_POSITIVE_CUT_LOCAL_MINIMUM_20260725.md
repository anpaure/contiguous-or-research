# Owner-fixed spike plus interval exchange graph: exact positive-cut stability and a literal null gadget

Date: 2026-07-25

## 0. Outcome

This note studies the exact penalized objective

\[
 \Psi_\lambda(M)=Q_w(M)+\lambda HJ(M),
\tag{0.1}
\]

where \(Q_w\) is the doubled, integer-floor-correct flag energy and
\(J(M)\) is the physical selected-row run count.  Put

\[
 \beta=\lambda H.
\tag{0.2}
\]

For every audited compatible owner-fixed spike or interval packet cube,
the restriction of \(Q_w\) to the cube is exactly a weighted positive-cut
polynomial:

\[
 Q_w(M_S)-Q_w(M)
 =\sum_{i\in S}h_i-\operatorname{cut}_g(S).
\tag{0.3}
\]

Here the edge weights are the nonnegative cross-Gram entries
\(g_{ij}=\langle d_i,d_j\rangle_w\), while \(h_i\) is an endpoint field.
Thus a penalized local minimum obeys, for every legal cut \(S\),

\[
 \boxed{
 \operatorname{cut}_g(S)
 \le \sum_{i\in S}h_i+\beta\Delta J(S)
 \le\sum_{i\in S}(h_i+2\beta).
 }
\tag{0.4}
\]

This is the requested positive-cut/local-minimum theorem, with the literal
run toll retained.

The theorem does **not** force high multiplicities to be small.  Summing
the singleton inequalities gives the sharp endpoint-barrier inequality

\[
 \boxed{
 Q_w(M_{\rm all})-Q_w(M)
 \ge \Gamma-2\lambda Ht,
 \qquad
 \Gamma=2\sum_{i<j}g_{ij}.
 }
\tag{0.5}
\]

For a common depth-\(q\) spike of load \(t\),

\[
 \Gamma\ge w_q^\pm t(t-1).
\tag{0.6}
\]

Thus local stability says that the coherent all-spike endpoint is expensive;
it does not bound \(t\).  Equivalently, it transfers old collision load to
the current loads of the spike images and to the run penalty.  No bounded
image-reuse theorem is presently available.

The low-multiplicity alternative also fails for the audited interval
family.  A common-partner owner-fixed interval has length at most \(q-1\).
Completely splitting \(P_{\le L,q}\) old collision pairs from load classes
at most \(L\) therefore requires at least

\[
 \boxed{
 K\ge \frac{2P_{\le L,q}}{L(q-1)}
 }
\tag{0.7}
\]

packets.  For fixed \(L\), \(P_{\le L,q}=\Omega(W)\), and \(q\le H\), this
is \(\Omega(W/H)\), not \(o(W/H)\).

Finally, there is an exact literal chart-null gadget.  A repeated first-upper
target of load two can be supplied with load-one owner-fixed image chains.
Every spike singleton is then energy-flat, the two-bit switch is
energy-increasing, \(J\) is unchanged, and the depth-one interval chart is
blind because the two collars are disjoint.  Hence the spike chart has a
genuine local minimum while the interval chart supplies no positive edge
for its surviving collision.  The gadget is exact and full-depth, but its
direct construction uses private singleton rows; it is not asserted to be
a local minimum against every other chart, or a positive-density low-run
global minimizer.

The precise remaining positive theorem is consequently stronger than a
positive-cut bound: it must show that the endpoint fields in (0.3) have
bounded global reuse and are carried by genuinely rewired long owner paths.
Neither owner-fixed spikes nor the present aligned interval packets prove
that statement.  No constant-one conclusion is claimed.

## 1. Exact floor normalization

Let \(\mathscr A\) be the finite set of signed depths being charged.  For
\(\alpha\in\mathscr A\), let \(\Omega_\alpha\) be its target layer, of
cardinality \(N_\alpha\), and let the forced total mass be

\[
 M_\alpha=N_\alpha c_\alpha+s_\alpha,
 \qquad 0\le s_\alpha<N_\alpha.
\tag{1.1}
\]

The exact minimum of the doubled factorial polynomial at this rank is

\[
 F_\alpha
 =(N_\alpha-s_\alpha)c_\alpha(c_\alpha-1)
  +s_\alpha c_\alpha(c_\alpha+1).
\tag{1.2}
\]

Define

\[
 Q_w(M)
 =\sum_{\alpha\in\mathscr A}w_\alpha
 \left[
   \sum_{Z\in\Omega_\alpha}
       \mu_\alpha^M(Z)(\mu_\alpha^M(Z)-1)
   -F_\alpha
 \right],
 \qquad w_\alpha\ge0.
\tag{1.3}
\]

Every \(F_\alpha\) is constant on the exact mass fibre.  Therefore no floor
term is lost in any energy-difference identity below.  The ordinary
factorial-floor excess is \(Q_w/2\); all displayed energy gains are then
divided by two, while the penalty \(\beta J\) is unchanged.

## 2. Compatible chart cubes and the positive-cut identity

Fix a literal lower-saturating, middle-simple token state \(M\).  Let
\(\mathcal C=\{1,\ldots,t\}\) be one audited compatible chart cube:

- one common-source-hub upper owner-fixed spike cube;
- one lower owner-fixed spike cube at a common target;
- one audited same-hub interval-packet cube with nonnegative joined Gram;
  or
- the commuting same-token upper/lower product, after treating each
  four-state token as its audited product block.

The word *compatible* is essential.  Several source hubs cannot be silently
combined, repeated leaf-pair orientations must be fixed, and different
distinguished depths on the same token are not independent unless an
audited commuting product is explicitly available.

For bit \(i\), let \(d_i\) be its complete signed-rank load innovation and
put

\[
 a_i=Q_w(M_{\{i\}})-Q_w(M),
 \qquad
 g_{ij}=\langle d_i,d_j\rangle_w.
\tag{2.1}
\]

The audited spike and positive interval charts satisfy

\[
 g_{ij}\ge0\qquad(i\ne j).
\tag{2.2}
\]

For \(S\subseteq[t]\), simultaneous additivity of the compatible token
innovations gives the exact quadratic expansion

\[
 \boxed{
 Q_w(M_S)-Q_w(M)
 =\sum_{i\in S}a_i
  +2\sum_{\substack{i<j\\i,j\in S}}g_{ij}.
 }
\tag{2.3}
\]

Define the Gram degree and endpoint field

\[
 d_i^g=\sum_{j\ne i}g_{ij},
 \qquad
 h_i=a_i+d_i^g,
\tag{2.4}
\]

and the positive cut

\[
 \operatorname{cut}_g(S)
 =\sum_{\substack{i\in S\\j\notin S}}g_{ij}.
\tag{2.5}
\]

Since

\[
 \sum_{i\in S}d_i^g
 =2\sum_{\substack{i<j\\i,j\in S}}g_{ij}
  +\operatorname{cut}_g(S),
\tag{2.6}
\]

(2.3) becomes (0.3):

\[
 \boxed{
 Q_w(M_S)-Q_w(M)
 =\sum_{i\in S}h_i-\operatorname{cut}_g(S).
 }
\tag{2.7}
\]

Thus the nonnegative spike Gram is literally positive cut curvature.  The
endpoint fields \(h_i\), not the cut algebra, are the unresolved term.

## 3. Penalized local-minimum theorem and literal toll

For every owner-fixed singleton or orientation-preserving interval packet,
the audited physical ledger gives

\[
 J(M_S)-J(M)\le2|S|.
\tag{3.1}
\]

More precisely, if packet \(i\) has a certified toll \(r_i\le2\), then

\[
 \Delta J(S):=J(M_S)-J(M)\le\sum_{i\in S}r_i.
\tag{3.2}
\]

The absolute change can be smaller or negative; (3.2) is the safe literal
upper bound.

### Theorem 3.1 (exact positive-cut stability)

Suppose \(M\) is a local minimum of \(\Psi_\lambda\) against every corner
of the compatible chart \(\mathcal C\).  Then, for every \(S\subseteq[t]\),

\[
 \boxed{
 \operatorname{cut}_g(S)
 \le
 \sum_{i\in S}h_i+\beta\Delta J(S)
 \le
 \sum_{i\in S}(h_i+\beta r_i).
 }
\tag{3.3}
\]

Conversely, a set \(S\) violating the first inequality gives the exact
penalized descent

\[
 \Psi_\lambda(M)-\Psi_\lambda(M_S)
 =
 \operatorname{cut}_g(S)
 -\sum_{i\in S}h_i-\beta\Delta J(S)>0.
\tag{3.4}
\]

#### Proof

Local minimality gives

\[
 0\le
 \Psi_\lambda(M_S)-\Psi_\lambda(M)
 =
 Q_w(M_S)-Q_w(M)+\beta\Delta J(S).
\]

Insert (2.7), then use (3.2).  This proves (3.3)--(3.4).  \(\square\)

There is a useful, but conditional, aggregate consequence.  Put

\[
 G(\mathcal C)=\sum_{i<j}g_{ij},
 \qquad
 H_+(\mathcal C)=\sum_i(h_i)_+,
 \qquad
 R(\mathcal C)=\sum_i r_i.
\tag{3.5}
\]

Choose \(S\) by independent fair bits.  Then

\[
 \mathbb E\operatorname{cut}_g(S)=\frac12G(\mathcal C),
 \qquad
 \mathbb E\sum_{i\in S}(h_i)_+=\frac12H_+(\mathcal C).
\tag{3.6}
\]

Hence some corner has penalized gain at least

\[
 \boxed{
 \frac12\bigl(
 G(\mathcal C)-H_+(\mathcal C)-\beta R(\mathcal C)
 \bigr).
 }
\tag{3.7}
\]

In particular, at a local minimum,

\[
 \boxed{
 G(\mathcal C)
 \le H_+(\mathcal C)+\beta R(\mathcal C).
 }
\tag{3.8}
\]

Equation (3.8) is a genuine quantitative descent criterion.  It would imply
that visible collision energy is \(o(W)\) if a global chart cover had

\[
 \sum H_+=o(W),
 \qquad
 \beta\sum R=o(W),
\tag{3.9}
\]

with bounded overlap.  The first assertion in (3.9) is exactly the missing
image-load/endpoint-field theorem.

## 4. The sharper small-density stability inequality

The positive-cut presentation is not the sharpest way to sum local
stability.  The singleton inequalities retain the exact endpoint barrier.

Let

\[
 \Gamma=2G(\mathcal C)=2\sum_{i<j}g_{ij},
\tag{4.1}
\]

and let \(M_{\rm all}=M_{[t]}\).  From (2.3),

\[
 Q_w(M_{\rm all})-Q_w(M)
 =\sum_i a_i+\Gamma.
\tag{4.2}
\]

For every singleton,

\[
 a_i+\beta\bigl(J(M_{\{i\}})-J(M)\bigr)\ge0.
\tag{4.3}
\]

Since each singleton toll is at most two,

\[
 \sum_i a_i\ge-2\beta t.
\tag{4.4}
\]

### Theorem 4.1 (summed endpoint barrier)

At a penalized local minimum,

\[
 \boxed{
 Q_w(M_{\rm all})-Q_w(M)
 \ge\Gamma-2\lambda Ht.
 }
\tag{4.5}
\]

For fair independent bits,

\[
 \boxed{
 \mathbb E Q_w(M_S)-Q_w(M)
 =
 \frac{Q_w(M_{\rm all})-Q_w(M)}2-\frac{\Gamma}{4}
 =
 \frac12\sum_i a_i+\frac{\Gamma}{4}.
 }
\tag{4.6}
\]

The fair expected run increase is at most \(t\).  Applying penalized
minimality only to (4.6) gives

\[
 Q_w(M_{\rm all})-Q_w(M)
 \ge\frac{\Gamma}{2}-2\lambda Ht,
\tag{4.7}
\]

which is weaker than (4.5).  Thus summing singleton stability is the sharp
available argument.

#### Proof

Equations (4.2) and (4.4) give (4.5).  The quadratic fair-cube identity
gives (4.6); averaging the literal toll gives (4.7).  \(\square\)

The importance of (4.5) is negative as well as positive: without an
independent upper bound on the coherent endpoint gap, it does not bound
\(\Gamma\).

## 5. Exact current-relative load-gradient form

For a nonzero unit transfer

\[
 U_{i,\alpha}\longrightarrow V_{i,\alpha}
\]

at signed depth \(\alpha\), the exact doubled-floor singleton change is

\[
 \boxed{
 a_i
 =2\sum_{\alpha:\,d_{i,\alpha}\ne0}
 w_\alpha\bigl(
   \mu_\alpha(V_{i,\alpha})
  -\mu_\alpha(U_{i,\alpha})+1
 \bigr).
 }
\tag{5.1}
\]

This follows directly from

\[
 (y+1)y-y(y-1)=2y,
 \qquad
 (x-1)(x-2)-x(x-1)=-2(x-1).
\]

At a penalized minimizer,

\[
 \boxed{
 \sum_{\alpha:\,d_{i,\alpha}\ne0}
 w_\alpha\bigl(
   \mu_\alpha(U_{i,\alpha})
  -\mu_\alpha(V_{i,\alpha})-1
 \bigr)
 \le\lambda H.
 }
\tag{5.2}
\]

The constant is \(\lambda H\), not \(2\lambda H\), because (5.1) has the
factor two while the run toll is at most two.

Summing (5.2) over \(t\) distinct occurrences gives

\[
 \boxed{
 \mathcal I\le\mathcal O+\lambda Ht,
 }
\tag{5.3}
\]

where

\[
 \mathcal I
 =\sum_{i,\alpha}w_\alpha
   \bigl(\mu_\alpha(U_{i,\alpha})-1\bigr),
 \qquad
 \mathcal O
 =\sum_{i,\alpha}w_\alpha\mu_\alpha(V_{i,\alpha}).
\tag{5.4}
\]

Thus local stability transfers old collision incidence to image load and
to the penalty.

For a common distinguished depth-\(q\) fibre of size \(t\), contained in a
phase-separated spike of total current load \(x_U\ge t\), (5.3) implies

\[
 \boxed{
 w_qt(x_U-1)
 \le
 \mathcal O+\lambda Ht.
 }
\tag{5.5}
\]

All later-depth image loads are included in \(\mathcal O\).  They cannot be
discarded merely because their cross-Grams are nonnegative.

### Conditional deepest-rank corollary

At \(q=H\), suppose a selected family of same-phase fibres has loads at
least \(K\), every spike image is charged at most \(\rho\) times, and the
total available image-target mass is \(M_H\).  Let

\[
 C=\sum_U\binom{t_U}{2},
 \qquad
 T_{\rm hi}=\sum_Ut_U.
\tag{5.6}
\]

Then

\[
 2w_HC\le\rho w_HM_H+\lambda HT_{\rm hi},
 \qquad
 T_{\rm hi}\le\frac{2C}{K-1}.
\tag{5.7}
\]

If

\[
 K-1>\frac{\lambda H}{w_H},
\tag{5.8}
\]

then

\[
 \boxed{
 C\le
 \frac{\rho M_H}
 {2\left(1-\dfrac{\lambda H}{w_H(K-1)}\right)},
 \qquad
 T_{\rm hi}\le\frac{2C}{K-1}.
 }
\tag{5.9}
\]

This condition can make the number of high-load occurrences small.  It
does not make their collision energy \(o(M_H)\), and no bounded \(\rho\)
has been proved for the owner-fixed image map.  Equation (5.9) is therefore
conditional, not a completed high-multiplicity theorem.

## 6. Specialization to audited spike curvature

For a legal one-hub upper owner-fixed common-\(U_q\) spike, or a lower
owner-fixed common-\(L_q\) spike,

\[
 \boxed{
 \Gamma\ge w_q^\pm t(t-1).
 }
\tag{6.1}
\]

For an owner-preserving upper interval packetization in one source phase,
proper equal \(U_q\)-targets occur in different physical rows.  Every
visible collision pair therefore lies in different packets, and the
audited aggregate Gram gives

\[
 \boxed{
 \Gamma
 \ge
 w_q^+\sum_U
   \mu_{A,q,U}\bigl(\mu_{A,q,U}-1\bigr).
 }
\tag{6.2}
\]

Combining (4.5) and (6.2),

\[
 \boxed{
 Q_w(M_{\rm all})-Q_w(M)
 \ge
 w_q^+\sum_U
   \mu_{A,q,U}\bigl(\mu_{A,q,U}-1\bigr)
 -2\lambda HK.
 }
\tag{6.3}
\]

This is the exact summed local-stability theorem for the audited
owner-fixed packets.  It is an endpoint lower bound, not a current-energy
upper bound.

There are three non-summability restrictions.

1. Different source hubs do not have an audited common nonnegative Gram:
   an image from one hub can equal an old target from another.
2. Lower spike fibres at different old targets can have negative cross
   products; for example
   \[
      d_1=\delta_{L_2}-\delta_{L_1},
      \qquad
      d_2=\delta_{L_3}-\delta_{L_2}
   \]
   have inner product \(-1\).
3. Distinct depths can reuse one token, and the corresponding
   transpositions need not commute.

Scalar singleton inequalities may always be summed with multiplicity, but
that repeatedly charges the same image load and the same run.  It does not
construct one legal global corner.

## 7. The low-multiplicity interval toll

Fix a depth \(2\le q\le H\).  In the audited owner-preserving
common-partner interval family, a packet of \(r\) consecutive starts needs
a pair contained in all future \(q\)-sets.  Their intersection has size

\[
 q-r+1.
\tag{7.1}
\]

Therefore

\[
 \boxed{r\le q-1.}
\tag{7.2}
\]

Let the old bounded-load collision census be

\[
 P_{\le L,q}
 =\sum_{\substack{U\\2\le\mu_q(U)\le L}}
   \binom{\mu_q(U)}2,
\qquad
 R_{\le L,q}
 =\sum_{\substack{U\\2\le\mu_q(U)\le L}}
   (\mu_q(U)-1).
\tag{7.3}
\]

Complete splitting requires at least \(R_{\le L,q}\) moved occurrences.
Since

\[
 R_{\le L,q}\ge\frac2L P_{\le L,q},
\tag{7.4}
\]

the packet count obeys

\[
 \boxed{
 K\ge
 \frac{R_{\le L,q}}{q-1}
 \ge
 \frac{2P_{\le L,q}}{L(q-1)}.
 }
\tag{7.5}
\]

Thus a fixed-\(L\), \(\Omega(W)\) diffuse sector requires
\(\Omega(W/H)\) packets.  This is a sharp physical capacity obstruction to
little-\(o\) boundary in this interval family.

There is an independent aligned-block obstruction valid also at \(q=1\).
If \(b\) common-owner block seams are available, at most \(qb\) upper
occurrences can change.  Hence

\[
 P_q^{\rm new}
 \ge
 P_{\le L,q}-(L-1)qb.
\tag{7.6}
\]

For \(b=o(W/H)\) and \(q\le H\), every linear bounded-load sector survives
with \(\Omega(W)\) collision pairs.

## 8. Exact depth-one blindness

Let two distinct occurrences in one exact source factor have the same
proper first-upper target \(U\).  Their two-point physical collars are
disjoint.  Indeed, if they shared a collar coordinate \(c\), then the
middle window \(U\setminus\{c\}\) would occur twice in the exact factor.
The two adjacent extensions of one proper middle window are distinct, so
the occurrences would have to be identical.

Consequently no common partner is active on both occurrences.  The
common-partner interval exchange graph has no positive edge joining this
collision pair.  Moreover the predecessor/successor orientation interval
atlas satisfies

\[
 z_{I,1}^-=z_{I,1}^+=0,
\tag{8.1}
\]

so its depth-one innovation is exactly zero.  Therefore the repeated
first-upper pair lies in the exact kernel of both audited aligned interval
mechanisms.  It can be touched only by occurrence-specific owner-fixed
spikes, which pay the singleton image field in Section 5.

## 9. A literal full-depth null gadget

The endpoint field obstruction is not merely an abstract load vector.

### Theorem 9.1 (load-one image reservoir)

Assume \(m\ge6\) and \(1\le H\le m-5\).  There is a literal,
lower-saturating, middle-simple token state containing two occurrences
\(e_1,e_2\) with

\[
 U_1(e_1)=U_1(e_2)=U,
\qquad
 \mu_1(U)=2,
\tag{9.1}
\]

and one fixed shadow occurrence on every owner-fixed image chain, such
that:

1. every corner of the two-bit owner-fixed spike cube has
   \(Q_w\) at least that of the all-old corner, for every choice of
   nonnegative signed-depth weights through \(H\);
2. the all-old corner and each singleton corner have equal depth-one
   energy;
3. the two-bit corner has depth-one doubled energy larger by \(2w_1^+\);
4. the spike switches have \(\Delta J=0\);
5. the collision pair in (9.1) is invisible to the two audited aligned
   depth-one interval charts.

Hence the all-old state is a local minimum of \(Q_w+\lambda HJ\) on this
exact owner-fixed spike cube for every \(\lambda\ge0\), while retaining a
genuine load-two collision.  The interval chart has zero positive
visibility on that collision; no assertion is made about unrelated
interval moves elsewhere in the state.

#### Construction

Take two occurrences of a repeated proper first-upper target \(U\) in one
exact omitted-\(A\) factor.  Such a target exists because that factor has

\[
 \binom{2m-1}{m-1}
 >
 \binom{2m-1}{m+1}
\tag{9.2}
\]

starts and possible first-upper targets.  Write

\[
 Y_i=U\setminus\{b_i\}.
\tag{9.3}
\]

Exactness gives \(b_1\ne b_2\) and disjoint physical collars.  Choose a
helper

\[
 z_i\notin U_H(e_i)\cup A,
\tag{9.4}
\]

and freeze one coordinatewise bijection between
\(B_i=\{b_i,z_i\}\) and \(A\).  If \(\alpha_i\in A\) is paired with
\(b_i\), the owner-fixed image chain is

\[
 V_{i,p}
 =\bigl(U_p(e_i)\setminus\{b_i\}\bigr)\cup\{\alpha_i\},
 \qquad 1\le p\le H.
\tag{9.5}
\]

The two image chains are distinct at every depth: the first contains
\(b_2\) and omits \(b_1\), while the second contains \(b_1\) and omits
\(b_2\).  Every image meets \(A\), while every old target avoids \(A\).

For each \(i\), prescribe one additional literal shadow token whose upper
chain is exactly \(V_{i,1}\subset\cdots\subset V_{i,H}\).  Choose its
middle owner as an \(m\)-subset of \(V_{i,1}\), then order the successive
added coordinates according to (9.5).  The four prescribed central edges
can be chosen pairwise disjoint and extended to a full lower-saturating
central matching by the robust middle-level extension lemma, since four
prescribed edges are at most \(m+1\).

Lift every residual central edge to a literal chain avoiding the at most
four special old/image targets at each depth.  At extension step \(p\)
there are

\[
 m+2-p\ge7
\tag{9.6}
\]

available next coordinates, so one can avoid all special targets.  At the
end at least two coordinates remain for an omitted pair.  This gives the
claimed full literal token state.

Render each old \(e_i\) segment and its alternate conjugate segment as a
private singleton labelled row.  Replacing one by the other removes one
run and inserts one run, so \(\Delta J=0\).

#### Energy audit

Every image target \(V_{i,p}\) has current load one.  The two old targets
\(U_p(e_1),U_p(e_2)\) have no residual occurrences.  At a depth where the
old targets are distinct, switching one occurrence removes a load-one bin
and changes an image load from one to two; the doubled factorial polynomial
increases by \(2\).  At a depth where the old targets coincide, their old
load is two.  Switching \(r=0,1,2\) occurrences changes the doubled
factorial polynomial by respectively

\[
 0,\quad0,\quad2.
\tag{9.7}
\]

Thus every nonnegative weighted full-depth energy is nondecreasing.  At
depth one the old targets coincide, proving items 1--3.  Lower flags are
fixed by the owner-fixed switches.  Item 4 was proved by the private-row
rendering, and item 5 follows from Section 8.  \(\square\)

### Positive-cut form of the null

At depth one the two spike vertices have

\[
 a_1=a_2=0,\qquad
 g_{12}=w_1^+,\qquad
 h_1=h_2=w_1^+.
\tag{9.8}
\]

For \(S\subseteq\{1,2\}\),

\[
 Q_1(M_S)-Q_1(M)
 =w_1^+|S|-\operatorname{cut}_g(S)
 \in\{0,2w_1^+\}.
\tag{9.9}
\]

More explicitly, the right side is zero for \(|S|=0,1\) and
\(2w_1^+\) for \(|S|=2\).  The positive cut is exactly cancelled by the
two endpoint fields.  There is no interval edge to supply another
direction.

The gadget is an exact chart-null obstruction to any theorem which attempts
to deduce a charge for every collision pair from the audited local cut
inequalities alone.
Its private-row construction has \(\Theta(W)\) runs after arbitrary
singleton completion.  Therefore it is not, by itself, an obstruction to a
future theorem exploiting the special low-run first-avoided trace.  A
positive-density low-run packing of these null gadgets is neither proved
nor used here.

## 10. Conditional global composition and the missing theorem

For completeness, suppose a family of compatible positive charts
\(\{\mathcal C_\gamma\}\) comes with nonnegative coefficients
\(\theta_\gamma\) such that:

1. every collision pair being charged is represented in the Gram edge
   mass with total coefficient at least \(\kappa>0\);
2. endpoint-field and packet incidences have overlap at most \(D\);
3. the total literal toll is
   \[
      \sum_\gamma\theta_\gamma R(\mathcal C_\gamma)=o(W/H).
   \]

Summing (3.8) gives

\[
 \boxed{
 \kappa E_{\rm vis}
 \le
 D\,B_{\rm field}
 +\lambda H\,o(W/H).
 }
\tag{10.1}
\]

Therefore, if \(\lambda=O(1)\),
\(B_{\rm field}=o(W)\), and the collision energy outside the visible chart
cover is \(o(W)\), then

\[
 E_{\rm vis}=o(W)
\tag{10.2}
\]

at every penalized local minimum.  This is an exact route to the desired
conclusion.

The hypotheses fail at precisely the two points proved above:

- image loads can make \(B_{\rm field}\) of the same order as the old
  collision charge, with equality in the null gadget;
- a fixed positive density of bounded-load collisions needs
  \(\Omega(W/H)\) owner-preserving packets, and depth-one collision pairs
  can be completely invisible to the aligned interval graph.

Thus the owner-fixed spike plus audited interval exchange graph does not
prove a quantitative descent unless energy is \(o(W)\).  Its exact
alternative is a load reservoir / blind-collar null component.  Eliminating
that alternative requires a new global theorem: image-load charges must be
transported along positive-density changes of the central owner path, with
total physical seam count \(o(W/H)\).

## 11. Independently checkable boundary

The following are proved in this report.

1. The exact positive-cut identity (2.7), with all integer floors retained.
2. The penalized local-minimum inequalities (3.3), including the constant
   \(2\lambda H\) per packet in doubled energy.
3. The sharper summed endpoint barrier (4.5).
4. The current-relative image-load inequality (5.2), with the exact
   \(\lambda H\) constant after dividing the doubled singleton change by
   two.
5. The conditional high-load estimate (5.9).
6. The sharp \(q-1\) interval length and packet lower bounds (7.2)--(7.5).
7. Exact depth-one interval blindness.
8. The literal full-depth null gadget in Theorem 9.1.

The following are not proved.

1. A bounded-reuse estimate for owner-fixed image targets.
2. A compatible simultaneous positive cube across different source hubs.
3. A global low-run packing of the null gadgets.
4. A recentered positive-Gram interval atlas at an arbitrary mixed
   penalized minimizer.
5. A theorem coupling the image fields to long genuine owner-path
   rewiring.

No signed relaxation, fractional factor, web search, or finite search is
used.
