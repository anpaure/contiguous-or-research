# The minimal biresident period ledger for the star--cycle singleton absorber

Date: 2026-08-13  
Status: exact necessary arithmetic and constructive reduction  
Source graph absorber:
`/Users/amir.nuriyev/.codex/attachments/92d98fcf-75a1-4de4-8d0b-3216490f0909/pasted-text.txt`  
Source SHA-256: `d1d1432d1c31c01103a90aa21daf7f2d6d6927b497b97ddf5075772c04f3f94f`

## 1. Exact period equation

The graph absorber has one shore consisting of `q+1` star components of
period `q+1`, and the other shore consisting of `q` cycle components of
period `q+2`.  Their total owner counts differ by one:

\[
 (q+1)^2-q(q+2)=1.                                \tag{1.1}
\]

Suppose a componentwise dilation replaces every star component by one
pure rail of a common period `a`, and every cycle component by one pure
rail of a common period `b`.  If the dilated signed owner current is still
a singleton, total owner count forces

\[
 (q+1)a-qb=1.                                     \tag{1.2}
\]

### Lemma 1.1 (complete integer solution)

All positive integer solutions of (1.2) are

\[
 a=1+qt,\qquad b=1+(q+1)t                         \tag{1.3}
\]

for an integer `t >= 0`.

### Proof

Reducing (1.2) modulo `q` gives `a=1 mod q`, so `a=1+qt`.
Substitution gives `b=1+(q+1)t`.  The converse is immediate. \(\square\)

## 2. Minimal biresident solution

A pure `q`-window rail of period `m` has positive run `q` and zero run
`m-q` on every active coordinate.  Literal positive-and-zero residence
therefore requires

\[
 m\ge2q.                                           \tag{2.1}
\]

For `q >= 2`, the solution `t=1` in (1.3) is the original short pair

\[
 (a,b)=(q+1,q+2),                                  \tag{2.2}
\]

which fails zero residence.  The next solution is

\[
 \boxed{(a,b)=(2q+1,,2q+3)}.                      \tag{2.3}
\]

It is the unique componentwise-uniform solution minimizing both periods
subject to biresidence.  In particular, a common-period tensor lift can
never preserve the singleton: setting `a=b=m` makes the signed owner count
equal to `m`, not one.

## 3. Balanced auxiliary census

At the minimal biresident pair, the number of new owner positions relative
to the original short components is

\[
 a-(q+1)=q,
 \qquad
 b-(q+2)=q+1.                                      \tag{3.1}
\]

Consequently the two shores require exactly the same number of auxiliary
owner positions:

\[
 (q+1)q=q(q+1).                                    \tag{3.2}
\]

Thus there is no scalar obstruction to a genuine singleton-preserving
dilation.  The exact remaining local theorem is the following.

> **Balanced rooted-dilation gate.**  Replace the `q+1` ordered star
> components by legal, owner-simple, biresident period-`2q+1` rails and
> the `q` ordered cycle components by legal, owner-simple, biresident
> period-`2q+3` rails so that their complete signed owner current is
> exactly `e_H`, and so that the same equality holds in every compulsory
> proper-deck, trace, socket, and cap row.

Equation (3.2) says that the auxiliary positions can in principle be
paired between the two shores.  It does not pair them.  A construction
must correlate the two decompositions; independently inserting fresh
labels in each component only matches counts and generally changes the
owner current.

## 4. Relation to the vertical whole-rail lift

The vertical complementary-fibre construction uses one common period on
every graph edge.  It therefore sends the one-edge graph difference to
one whole rail, whose owner count is that common period.  This is exactly
the common-period obstruction following (2.3), not a defect in the
vertical construction.

The balanced rooted-dilation gate is the smallest possible route that can
retain a literal singleton while repairing the zero-residence defect of
the short graph components.  Any proposed Cartesian-product Hamilton
lift, transition-clock lift, or blow-up which retains `q+1` components on
one shore and `q` on the other must realize the period ledger (1.3).  The
first period pair worth testing is therefore (2.3), not `(2q,2q)`.

No owner-current construction of this balanced dilation is claimed here.
The result is an exact reduction from an unrestricted tensor search to one
minimal asymmetric pair with perfectly matched auxiliary census.

## 5. Fixed-core insertion dilation is impossible

The most direct realization of (1.3) would keep every original star or
cycle core and insert fresh, distinct active labels into its toggle order.
This cannot preserve the singleton for any `t > 1` when `q >= 3`.

Let

\[
 \mathcal C_S=\sum_{i=1}^{q+1}\mathbf1_{C_i^S},
 \qquad
 \mathcal C_G=\sum_{j=1}^{q}\mathbf1_{C_j^G}        \tag{5.1}
\]

be the core-incidence vectors of the original star and cycle
decompositions.  Put `s=t-1`.  Relative to the original periods, each
star rail receives

\[
 a-(q+1)=qs
\]

new active labels, while each cycle rail receives

\[
 b-(q+2)=(q+1)s.                                   \tag{5.2}
\]

Let `Z_S,Z_G` be the resulting aggregate incidence vectors of inserted
labels on the two shores.  Because active labels are distinct within a
pure rail,

\[
 0\le Z_S(x)\le q+1,
 \qquad
 0\le Z_G(x)\le q                                 \tag{5.3}
\]

for every ground coordinate `x`.

Keeping the original singleton current requires the added point current
to vanish:

\[
 qs\,\mathcal C_S-(q+1)s\,\mathcal C_G
 +q(Z_S-Z_G)=0.                                    \tag{5.4}
\]

Modulo `q`, equation (5.4) says

\[
 s\,\mathcal C_G=0\pmod q.                         \tag{5.5}
\]

### Lemma 5.1

For both explicit graph decompositions, `C_G` has additive order exactly
`q` in `(Z/qZ)^[k]`.

### Proof

For odd `q`, a point of `A union B_0` lies in `(q-1)/2` cycle cores.
This number is coprime to `q`, so the order is `q`.

For even `q=2h`, a point of `B_0 union {u,v}` lies in `h` cycle cores,
giving an order-two coordinate, while a point of `A` lies in `h-1` cycle
cores.  The order of `h-1` modulo `2h` is `2h/gcd(2h,h-1)`; together with
the order-two coordinate its least common multiple is `2h=q`, whether
`h` is odd or even.  Core points in `D` occur `q` times and do not change
the order.  \(\square\)

It follows from (5.5) that

\[
 q\mid s.                                          \tag{5.6}
\]

Write `s=qr`, with `r >= 1`.  Dividing (5.4) by `q` gives

\[
 Z_S-Z_G
 =r\left((q+1)\mathcal C_G-q\mathcal C_S\right).  \tag{5.7}

For even `q`, the coordinate `v` lies in no star core and in `q/2` cycle
cores.  The right side of (5.7) at `v` is

\[
 r\,\frac{q(q+1)}2>q+1,                            \tag{5.8}
\]

contradicting (5.3) for every even `q >= 4`.

For odd `q`, a point `a in A` lies in `q` star cores and `(q-1)/2` cycle
cores.  The right side of (5.7) at `a` is

\[
 -r\,\frac{q^2+1}{2}<-q,                           \tag{5.9}
\]

again contradicting (5.3).  This includes `q=3`.

Therefore no fixed-core extension obtained only by inserting distinct
active labels into the original graph rails can realize any longer
singleton-preserving solution (1.3).  The balanced rooted-dilation gate
must use cross-core role changes, shared auxiliary owners between opposite
shores, or another genuinely compound operation.  Merely choosing the
correct periods is not enough.
