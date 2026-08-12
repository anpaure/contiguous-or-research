# Long antipodal rings have a rigid core: the protected-collar quantifier gate

## Status

This note gives a sharp obstruction to the proposed theorem that an
arbitrary resource-disjoint bank of Boolean-`C6` collars can be extended to
an exact decomposition into near-maximal antipodal rings.

Every period-`ell` antipodal ring has a unique invariant core `K`, equal to
the intersection of its complete owner row.  A serially sealed width-`h`
collar containing at least `h+1` consecutive owner phases already determines
that core.  Consequently, two prescribed collars assigned to the same long
component must determine the same core.  Equivalently, the anchored lower
colours of any two prescribed ports on one component must have an
intersection of size at least `q-h`.  Pairwise resource-disjoint collars do
not imply this condition; in fact, for `h=o(q)`, an independently chosen
second central root satisfies it with exponentially small probability.

There is a second exact constraint.  In a decomposition using the two
near-maximal periods

\[
              L=q+h-1,\qquad L-1=q+h-2,
\]

the invariant cores of the period-`L` rings and the unused coordinates of
the period-`L-1` rings satisfy a coordinatewise affine balance law.  This
law follows from the pair-incidence moment of the two central Boolean
layers and is not visible in the scalar identity
`W=u(L-1)+vL`.

Thus the correct protected theorem cannot quantify over arbitrary disjoint
collars.  It must either:

1. construct the ring decomposition first and choose collars afterwards;
2. prescribe, for every intended component, one common core and compatible
   cyclic-order fragments; or
3. include the core/unused balance equations in the selector.

No exact one-copy ring decomposition is proved here.  The result is a
proof-safe obstruction and a corrected formulation of the integral packing
gate.  No computation or search is used.

## 1. Antipodal rings and their invariant core

Let the moving ground set `R` have size

\[
                            n=2q-1,
\]

and fix an owner width `h>=2`.  An antipodal ring of period `ell>=2h`
consists of disjoint sets

\[
             K,F\subseteq R,qquad |K|=q-h,quad |F|=\ell,
\]

together with a cyclic order

\[
                         F=(f_t)_{t\in\mathbb Z/\ell}.
\]

Its owners and immediate-lower roots are

\[
 \begin{aligned}
   O_t&=K\cup F[t,t+h),\\
   Q_t&=K\cup F[t+1,t+h),
 \end{aligned}                                           \tag{1.1}
\]

where cyclic intervals are taken modulo `ell`.

### Theorem 1.1 (the complete row determines the core)

For every antipodal ring of period `ell>=2h`,

\[
              \bigcap_{t\in\mathbb Z/\ell}O_t
       =      \bigcap_{t\in\mathbb Z/\ell}Q_t
       =K.                                                \tag{1.2}
\]

#### Proof

Every member of `K` belongs to every displayed set.  Conversely, fix
`x=f_s\in F`.  Since `ell>=2h`, there is a length-`h` cyclic interval and
a length-`(h-1)` cyclic interval avoiding `s`.  The corresponding owner and
root omit `x`.  Hence no member of `F` lies in either total intersection.
Coordinates outside `K\cup F` occur nowhere in the ring.  This proves
(1.2). \(\square\)

### Theorem 1.2 (a sealed collar already determines the core)

Let `I` be any interval of at least `h+1` consecutive owner phases in an
antipodal ring.  Then

\[
                         \bigcap_{t\in I}O_t=K.           \tag{1.3}
\]

In particular, the owner bank in a serially sealed Boolean-`C6` collar,
which contains the `h` left and `h` right phases around its cut, determines
the invariant core of the ambient ring.

#### Proof

It is enough to use `h+1` consecutive phases.  Their moving parts are the
`h`-windows

\[
                         F[t,t+h),\qquad 0\le t\le h.
\]

The first and last of these windows are disjoint because `ell>=2h` (when
`ell=2h` they are complementary).  Hence their intersection is empty, and
the intersection of all `h+1` owners is exactly `K`.  Adding further phases
cannot change it. \(\square\)

The theorem is deliberately literal.  A collar is not merely a list of
abstract lower and upper colours: once its consecutive owner occurrences
are fixed, its ambient long-ring core is fixed as well.

## 2. Core coherence is necessary for two ports on one component

Suppose an anchored port has a distinguished transition

\[
                O_x=Q+x \longrightarrow O_y=Q+y.         \tag{2.1}
\]

In every antipodal lift of this transition, its invariant core satisfies

\[
                          K\subseteq Q,qquad |K|=q-h.    \tag{2.2}
\]

### Corollary 2.1 (two-anchor intersection obstruction)

If two anchored ports with lower colours `Q_1,Q_2` occur on the same
antipodal-ring component, then

\[
                          |Q_1\cap Q_2|\ge q-h.           \tag{2.3}
\]

If both ports are supplied as sealed literal collars, then their determined
cores must in fact be identical.

#### Proof

The common component has one invariant core `K` by Theorem 1.1.  Applying
(2.2) to both anchors gives `K subseteq Q_1 cap Q_2`, proving (2.3).  A
sealed collar determines `K` by Theorem 1.2, so two such determinations must
agree. \(\square\)

Resource disjointness is orthogonal to (2.3).  Two collars can use disjoint
owner, root and upper occurrences while their lower colours have
intersection smaller than `q-h`; such collars cannot lie on one long ring.

### Proposition 2.2 (core-compatible pairs are exponentially sparse)

Fix a rank-`(q-1)` set `Q_1`.  The proportion of rank-`(q-1)` sets `Q_2`
on `R` satisfying (2.3) is at most

\[
 {\displaystyle\sum_{j=0}^{h-1}
       \binom{q-1}{j}\binom qj
  \over
       \displaystyle\binom{2q-1}{q-1}}.                \tag{2.4}
\]

If `h=o(q)`, this is `exp(-Omega(q))`.

#### Proof

Write `j=|Q_1-Q_2|`.  Since both sets have size `q-1`, their intersection
has size `q-1-j`; condition (2.3) is exactly `j<=h-1`.  For fixed `j`, one
chooses the deleted `j`-set inside `Q_1` and the inserted `j`-set from its
`q`-element complement, giving the numerator of (2.4).

For `j<=h=o(q)`, the standard bound

\[
        \binom{q-1}{j}\binom qj\le (eq/j)^{2j}
\]

shows that the numerator is `exp(o(q))`.  The central binomial lower bound
`binom(2q-1,q-1)>=2^{2q-1}/(2q)` makes the denominator `exp(O(log q))4^q`.
Their ratio is `exp(-Omega(q))`. \(\square\)

Thus a loose connector path cannot first choose independent collars and
then ask an internal component to carry the two incident ports.  The two
collars on that component must be generated from one common core and one
compatible cyclic-order chart.

## 3. The exact first- and second-moment balance laws

Now specialize to the near-maximal periods

\[
                         L=q+h-1,
\]

so a period-`L` ring uses every coordinate outside its core, while a
period-`(L-1)` ring has exactly one unused coordinate.

Suppose an exact owner/root decomposition contains `v` rings of period
`L` and `u` rings of period `L-1`.  Necessarily

\[
                         W=u(L-1)+vL,qquad
                         W=\binom{2q-1}{q}.              \tag{3.1}
\]

Put

\[
                 C=\operatorname{Cat}_{q-1}
                  ={1\over q}\binom{2q-2}{q-1}
                  ={W\over 2q-1}.                       \tag{3.2}
\]

For a coordinate `z`, let

* `m_z` be the number of rings in which `z` is a moving coordinate;
* `a_z` be the number of period-`L` rings whose invariant core contains
  `z`;
* `u_z` be the number of period-`(L-1)` rings in which `z` is the unique
  unused coordinate.

### Theorem 3.1 (coordinate and pair-moment equations)

Every exact decomposition satisfies

\[
                           m_z=C                         \tag{3.3}
\]

for every coordinate `z`, and

\[
                 \boxed{a_z-(L-1)u_z=\kappa}            \tag{3.4}
\]

for every `z`, where the constant is

\[
       \kappa=(2q-2)C-(L-1)(u+v)
              ={v(q-h)-(L-1)u\over 2q-1}.              \tag{3.5}
\]

In particular the numerator on the right of (3.5) is divisible by
`2q-1`.  This divisibility follows from (3.1), but the coordinatewise law
(3.4) is an additional incidence condition.

#### Proof

Across the complete owner and root shores, the excess number of occurrences
of `z` is

\[
 \binom{2q-2}{q-1}-\binom{2q-2}{q-2}=C.                \tag{3.6}
\]

Inside one antipodal ring, a core coordinate occurs equally often in the
owner and root rows, a moving coordinate occurs `h` times in the owner row
and `h-1` times in the root row, and an unused coordinate occurs zero
times.  Hence the decomposition realizes (3.6) as exactly `m_z`, proving
(3.3).

For a fixed pair `{z,w}`, the corresponding global excess is also `C`:

\[
 \binom{2q-3}{q-2}-\binom{2q-3}{q-3}=C.                \tag{3.7}
\]

Sum (3.7) over the `2q-2` choices `w!=z`.  We evaluate the same sum ring by
ring.

In a period-`L` ring, a core coordinate `z` has excess one with every
moving coordinate, and hence contributes pair-degree `L`.  A moving
coordinate has excess one with every core coordinate and with the
`2(h-1)` moving coordinates at cyclic distance at most `h-1`.  Its
pair-degree is therefore

\[
                     (q-h)+2(h-1)=L-1.                 \tag{3.8}
\]

In a period-`(L-1)` ring, every nonunused coordinate, core or moving, has
pair-degree `L-1`, while the unused coordinate has degree zero.  Therefore
the total pair-degree of `z` over all rings is

\[
                  (L-1)(u+v-u_z)+a_z.                  \tag{3.9}
\]

Equating (3.9) with `(2q-2)C` gives (3.4) and the first expression in
(3.5).

Finally sum (3.4) over all coordinates.  Every period-`L` core has size
`q-h`, while every period-`(L-1)` ring contributes one unused coordinate.
Thus

\[
       (2q-1)\kappa=v(q-h)-(L-1)u,                     \tag{3.10}
\]

which proves the second expression in (3.5).  Reducing the numerator
modulo `2q-1` and using

\[
 q-h=(2q-1)-L,
\]

gives

\[
 v(q-h)-(L-1)u\equiv-[vL+u(L-1)]\equiv-W\equiv0
 \pmod{2q-1},
\]

because `W=(2q-1)C`. \(\square\)

Equation (3.4) is useful for protected planting.  A prescribed bank does
not merely consume distinct owner/root vertices; its invariant cores and
short-ring holes consume a coordinatewise affine budget which the residual
decomposition must complete exactly.

## 4. Corrected integral packing target

The scalar schedule in (3.1) and pairwise resource disjointness are
necessary but not sufficient data for a protected long-ring factor.  A
proof-safe formulation is the following.

### Core-coherent protected long-ring conjecture

For the critical width `h=Theta(sqrt q)`, choose nonnegative `u,v`
satisfying (3.1).  Suppose a protected partial bank of period-`L` and
period-`(L-1)` ring segments satisfies all of the following:

1. owner and root resources are pairwise disjoint;
2. all collars assigned to one intended component determine one common
   core and mutually compatible cyclic-order fragments;
3. the partial core and unused-coordinate loads extend to nonnegative
   integer vectors satisfying (3.3)--(3.4); and
4. every named upper and lower-ticket occurrence is protected at its
   literal phase.

Then the bank extends to an exact decomposition of both central shores
into `u+v=Theta(W/q)` antipodal rings of periods `L-1,L`.

This conjecture is strictly weaker than arbitrary protected-collar
extension and is the natural integral cover-down target left by the
present calculation.  Theorems 1.2 and 3.1 show that Conditions 2--3 cannot
be omitted.

For the loose Boolean-`C6` path, the safest order of quantifiers is now:

\[
 \boxed{
   \text{construct a core-balanced long-ring factor first, then choose
   two compatible cuts on each internal component.}
 }
\]

The local C6 tensor and the scalar collar budget remain valid under this
order.  What fails is only the stronger claim that an arbitrary disjoint
collar bank can be prescribed before the invariant cores are selected.

## 5. Exact scope

This note proves:

* uniqueness and literal recoverability of a long ring's invariant core;
* the exponential sparsity of core-compatible independent anchors;
* the exact coordinate and pair-moment balance laws for periods `L-1,L`;
* failure of the arbitrary-resource-disjoint protected-collar quantifier.

It does **not** prove:

* existence of an unprotected exact long-ring factor;
* extension of every core-coherent protected bank;
* upper-ticket or common-cap cover-down;
* `B(k)+O(1)` or exact equality.

The integral near-maximal ring packing remains open, but its protected
version now has the correct necessary state: one invariant core and one
cyclic-order chart per component, plus the affine coordinate budget
(3.4).
