# Depth-one drift of bounded exact wreath trades

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The effect of any exact-factor trade on the first-shadow hole count has a
pointwise formula.  For a universal two-for-two (C8) trade, its four-cell
first-shadow rectangle has two positive and two negative cells, and

\[
 \boxed{
 \Delta H_1
 =\#\{\text{negative corners of old load }1\}
  -\#\{\text{positive corners of old load }0\}.}
 \tag{0.1}
\]

Thus a C8 switch is maximally repairing exactly when both positive corners
are holes and both negative corners have load at least two.

The explicit all-\(m\) private C8 family in the canonical MSW factor has
the opposite behavior.  For every \(m\ge4\), it contains
\(\operatorname {Cat}_{m-4}\) pairwise disjoint supported components, and
switching any subset \(I\) gives

\[
 \boxed{
 H_1(F_I)=H_1(F_m^{\rm MSW})+|I|.}
 \tag{0.2}
\]

Every displayed switch creates one hole and fills none.  Hence the most
natural suspended/private C8 family is an exact anti-repair cube, not a
depth-one absorber.

There is also a dimension-free capacity obstruction for the universal
four-cell C8 atlas.  In one round of pairwise packet-disjoint universal
two-for-two trades, at most \(T/2\) trades can be used and each can fill at
most two holes.  Therefore one round improves
\(H_1\) by at most

\[
 T=W/(2m+1)=o(W).
\]

Since the canonical factor has \((1/16-o(1))W\) holes, any bounded C8
repair based on disjoint rounds needs \(\Omega(m)\) rounds and
\(\Omega(W)\) individual switches.  A one-round disjoint suspended family
cannot solve even depth one.

## 1. General exact trade drift

Let \(F\) be an exact middle wreath factor.  Write

\[
 \mu(S)=\mu_{F,1}(S),
 \qquad
 H_1(F)=\#\{S:\mu(S)=0\}.
\]

Let an exact trade replace an old packet family \(N\subseteq F\) by a new
packet family \(P\), with the same middle owners.  At depth one put

\[
 a(S)=\#\{\pi\in N:S\text{ is an }(m-1)\text{-interval of }\pi\},
\]

\[
 b(S)=\#\{\pi\in P:S\text{ is an }(m-1)\text{-interval of }\pi\},
 \qquad
 d(S)=b(S)-a(S).
 \tag{1.1}
\]

Then the new multiplicity is

\[
 \mu'(S)=\mu(S)+d(S)\ge0.
 \tag{1.2}
\]

Define the filled and opened sets

\[
 \mathcal F_0(d)=\{S:\mu(S)=0,\ d(S)>0\},
\]

\[
 \mathcal O_0(d)=\{S:\mu(S)>0,\ \mu(S)+d(S)=0\}.
 \tag{1.3}
\]

### Theorem 1.1 (exact first-shadow drift)

\[
 \boxed{
 H_1(F')-H_1(F)
 =|\mathcal O_0(d)|-|\mathcal F_0(d)|.}
 \tag{1.4}
\]

Moreover, for the endpoint statistic

\[
 e_F(S)=2\mu_{F,1}(S),
\]

the exact change is

\[
 \boxed{e_{F'}(S)-e_F(S)=2d(S).}
 \tag{1.5}
\]

#### Proof

For each target \(S\), the indicator of being a hole changes from
\(\mathbf1_{\mu(S)=0}\) to
\(\mathbf1_{\mu(S)+d(S)=0}\).  It decreases by one precisely on
\(\mathcal F_0(d)\), increases by one precisely on
\(\mathcal O_0(d)\), and is unchanged otherwise.  Summing gives (1.4).
Equation (1.5) follows from the exact endpoint identity
\(e_F=2\mu_{F,1}\). \(\square\)

This theorem is independent of the size of the trade.  It makes clear
that quadratic-energy descent and hole descent are different questions:
a transfer from load three to load one may lower energy without filling a
hole, while deleting the last copy of a singleton opens a hole.

## 2. Universal C8 rectangle

The universal two-for-two circuit has a common \((m-3)\)-set \(K\) and
four distinct labels \(u,v,\beta,\gamma\notin K\).  With one choice of
sign its complete depth-one action is

\[
 d=
 e_{K\cup\{v,\gamma\}}
 +e_{K\cup\{u,\beta\}}
 -e_{K\cup\{v,\beta\}}
 -e_{K\cup\{u,\gamma\}}.
 \tag{2.1}
\]

Put

\[
 P_1=K\cup\{v,\gamma\},\quad
 P_2=K\cup\{u,\beta\},
\]

\[
 M_1=K\cup\{v,\beta\},\quad
 M_2=K\cup\{u,\gamma\}.
 \tag{2.2}
\]

All four targets are distinct.  Since a supported trade has
\(\mu(M_i)\ge1\), Theorem 1.1 gives

\[
 \boxed{
 \Delta H_1
 =\mathbf1_{\mu(M_1)=1}
  +\mathbf1_{\mu(M_2)=1}
  -\mathbf1_{\mu(P_1)=0}
  -\mathbf1_{\mu(P_2)=0}.}
 \tag{2.3}
\]

Consequently:

* \(\Delta H_1=-2\) exactly when both positive corners are holes and both
  negative corners have load at least two;
* a strict repair requires more positive hole corners than negative
  singleton corners;
* the existence of a hole somewhere in the row says nothing about the
  sign of one supported C8 trade unless its rectangle meets that hole.

Algebraically, any prescribed hole can be made one positive corner of a
rectangle: choose two of its elements as \(v,\gamma\), use the rest as
\(K\), and choose \(u,\beta\) outside.  This does **not** make (2.1) an
applicable exact-factor trade.  Applicability additionally requires the
two negative cyclic rows to occur in the current factor and the positive
rows to replace exactly the same middle owners.

## 3. The canonical private C8 family is anti-repair

We use the proved canonical C8 theorem.  For every
\(V\in\mathcal D_{m-4}\), the canonical \((2\ 3)\)-overlay has a genuine
two-for-two ownership component \(\mathcal K_V\), and four pairwise
distinct depth-one targets

\[
 S_V,\quad \tau S_V,\quad T_V,\quad \tau T_V
\]

with old loads

\[
 (\mu(S_V),\mu(\tau S_V))=(3,1),
 \qquad
 (\mu(T_V),\mu(\tau T_V))=(1,1).
 \tag{3.1}
\]

The old-to-new action is

\[
 d_V=-e_{S_V}+e_{\tau S_V}-e_{T_V}+e_{\tau T_V}.
 \tag{3.2}
\]

The components and their four-cell target supports are pairwise disjoint
as \(V\) varies.

### Theorem 3.1 (exact all-\(m\) anti-repair cube)

For every \(I\subseteq\mathcal D_{m-4}\), simultaneous switching of
\(\{\mathcal K_V:V\in I\}\) gives an exact factor \(F_I\) satisfying

\[
 \boxed{H_1(F_I)=H_1(F_m^{\rm MSW})+|I|.}
 \tag{3.3}
\]

#### Proof

For one \(V\), neither positive cell in (3.2) is a hole: both have old
load one.  The negative cell \(S_V\) has load three and remains supported,
whereas the negative cell \(T_V\) has load one and becomes a hole.  Formula
(2.3) therefore gives \(\Delta H_1=1\).

The four-cell supports are disjoint for different \(V\), so the changes
do not alter the input loads of any other displayed component.  Their hole
drifts add exactly, proving (3.3). \(\square\)

The reverse switch from \(F_I\) back toward the canonical corner fills
exactly one of these newly created holes.  It does not touch the
positive-density family of holes already present at the canonical corner.

## 4. Relation to marked-gap certificates

The marked-gap theorem supplies

\[
 (2m-3)\operatorname {Cat}_{m-2}
\]

disjoint pairs of pointed occurrences with a common depth-one target.  It
therefore supplies a large pool of duplicate occurrences from which one
copy can be removed safely.

It does not label an equally large family of missing targets.  The holes
are inferred globally from

\[
 \text{duplicate excess}=W-(N_1-H_1),
\]

not paired canonically with the collision certificates.  Nor does one
safe negative occurrence determine the other three corners or the two
negative cyclic rows of an applicable C8 trade.

The explicit family in Section 3 exhibits the failure concretely: one
negative corner has abundant load three, but the forced companion negative
corner has load one, and neither positive corner is a hole.  Thus the
marked-gap collision supply alone cannot orient the supported rectangles
productively.

The exact missing incidence theorem is:

> Match actual holes to positive rectangle corners and marked-gap-safe
> duplicate occurrences to both negative corners, subject simultaneously
> to support by pairwise compatible exact ownership trades.

No such all-\(m\) matching theorem is presently proved.

## 5. One-round and multiround capacity obstruction

Let \(F\) be any exact factor with \(T=W/n\) packets.  Consider one family
of pairwise packet-disjoint supported universal C8 trades whose depth-one
action has the four-cell form (2.1).  If it contains \(r\) trades, then

\[
 2r\le T.
 \tag{5.1}
\]

Every trade has only two positive first-shadow cells, so by (1.4) it can
fill at most two old holes.  Therefore every simultaneous choice in this
one round satisfies

\[
 \boxed{H_1(F')\ge H_1(F)-2r\ge H_1(F)-T.}
 \tag{5.2}
\]

For the canonical factor,

\[
 H_1(F_m^{\rm MSW})\ge(1/16-o(1))W,
 \qquad T=W/n=o(W),
\]

so

\[
 \boxed{H_1(F')\ge(1/16-o(1))W}
 \tag{5.3}
\]

after every one-round packet-disjoint C8 correction, even under the
unrealistically favorable assumption that every chosen trade repairs two
holes and opens none.

More generally, after \(R\) such rounds,

\[
 H_1(F_R)\ge H_1(F_0)-RT.
 \tag{5.4}
\]

Hence reducing the canonical hole count to \(o(W)\) requires

\[
 R\ge(1/16-o(1))n=\Omega(m).
 \tag{5.5}
\]

Independently of how trades are grouped into rounds, (1.4) shows that at
least

\[
 \frac{H_1(F_0)-H_1(F_R)}2
\]

individual C8 switches are necessary.  Canonical-to-\(o(W)\) repair thus
requires \(\Omega(W)\) switch steps.

This does not rule out a long adaptive exact-factor path which reuses
packets.  It rules out a one-shot disjoint suspended universal-C8 family
and every bounded-number-of-rounds version of that strategy.  No
classification of arbitrary two-for-two wreath trades is known; a
bounded-row trade can in principle have \(\Theta(n)\) positive depth-one
cells, so (5.2) must not be applied beyond the four-cell atlas.

## 6. Owner-footprint obstruction for one bounded trade

For a cyclic row \(\pi\notin F\), define its owner footprint in \(F\) by

\[
 \omega_F(\pi)=
 \#\{\operatorname {owner}_F(X):X\in\mathcal W_m(\pi)\}.
 \tag{6.1}
\]

Thus \(\omega_F(\pi)\) is the number of old wreath rows which collectively
own the \(n\) middle sets of \(\pi\).

### Proposition 6.1 (bounded-trade accessibility)

If an exact \(s\)-for-\(s\) trade from \(F\) introduces \(\pi\), then

\[
 \boxed{\omega_F(\pi)\le s.}
 \tag{6.2}
\]

Consequently, if a hole \(R\) satisfies

\[
 \min\{\omega_F(\pi):R\in\mathcal W_{m-1}(\pi)\}>s,
 \tag{6.3}
\]

then no exact trade replacing at most \(s\) rows can fill \(R\).

#### Proof

Let \(N\subseteq F\) and \(P\) be the two signs of the trade, with
\(|N|=|P|=s\) and \(\pi\in P\).  Equality of the middle incidence of the
two signs says that every middle set of \(\pi\) is owned on the old side
by a row in \(N\).  Hence all owners counted by \(\omega_F(\pi)\) lie in
\(N\), proving (6.2).  If the trade fills \(R\), some newly introduced
row contains \(R\), so (6.3) gives a contradiction. \(\square\)

The footprint test is only necessary.  Even if
\(\omega_F(\pi)\le s\), the remaining old middle owners need not admit a
packing by the other \(s-1\) new rows.  Nevertheless it isolates a second
reason why a scalar hypothesis \(H_1(F)=\Theta(W)\) cannot force a bounded
repair: the hypothesis says nothing about the footprints of rows containing
the holes.

## 7. Sharp conditional positive gate

A sequence of supported C8 trades repairs the first shadow monotonically
if, at every step,

1. each positive corner selected for repair is currently a hole;
2. each negative corner currently has load at least two.

Under these two conditions every switch lowers \(H_1\) by exactly two.
It is enough to find

\[
 \frac12H_1(F_0)-o(W)
\]

such trades along one exact-factor path, allowing packet reuse across
\(\Omega(m)\) rounds.  Equivalently, one needs an adaptive alternating-
rectangle matching in the factor fibre whose positive side exhausts the
hole set and whose negative side stays inside the current duplicate set.

The scalar inequality \(H_1(F)=\Theta(W)\), the marked-gap collision
family, and the existence of individually realizable universal C8 circuits
do not prove this gate.  They control respectively the positive demand,
one part of the negative supply, and algebraic trade shape; the missing
content is their common support-feasible alignment inside one evolving
exact factor.
