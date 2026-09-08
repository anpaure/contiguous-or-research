# The character-minimal q=3 three-by-three near-C atom has a centre-support hole

**Date:** 2026-08-14  
**Status:** exact named-owner obstruction.  It rules out every three-rail
per shore realization of the sharp q=3 centre-character bound, including
all placements of the one positive long rail.  A later companion theorem,
`MATH_THEOREM_Q3_FOUR_BY_FOUR_NEAR_C_ATOM_ON_ELEVEN_LABELS_20260814.md`,
constructs the sharp next atom.

## 0. Outcome

For `q=3`, the sharp centre-character theorem exhibits the net profile

\[
 3\times(-1,0),\qquad 1\times(2,1).                 \tag{0.1}
\]

Every realization attaining three physical rails per shore necessarily has

* two period-eight rails centred at one target label `z_0`;
* one period-nine rail centred at an arbitrary label `w`; and
* one period-eight rail centred at each of the other three target labels
  `z_1,z_2,z_3`.

No such positive named-owner trade exists.  The two positive period-eight
rails give point degree at least `16` at `z_0`.  Each of the three negative
period-eight rails is centred away from `z_0` and can contain `z_0` in at
most three cyclic windows, so the negative point degree at `z_0` is at most
`9`.  But a one-owner difference at the target `H` requires the two degrees
to differ by exactly one.  The arbitrary long-rail centre `w` can only
increase the positive degree and cannot repair the contradiction.

Thus the character lower bound of three rails per shore is sharp only in
the centre ledger, not in the cyclic-window named-owner semigroup.  Every
genuine q=3 trade using periods eight and nine has at least four rails per
shore.  The previously proposed q=3 three-by-three search is empty before
cyclic-order enumeration.

## 1. The general centre-support lemma

Fix a common core `C_0`, window width `q>=2`, and a reduced label `z`.
A rail centred at `w` and having period `N` has owners

\[
 C_0\cup\{w\}\cup I_i^q(\sigma),\qquad i\in\mathbb Z_N,       \tag{1.1}
\]

where `sigma` is a cyclic word of `N` distinct toggle labels avoiding `w`.

### Lemma 1.1

If `w!=z`, then a period-`N` rail centred at `w` has at most `q` owners
containing `z`.  Consequently it has at least `N-q` owners omitting `z`.

#### Proof

If `z` is absent from the toggle word, none of the owners contains it.  If
`z` occurs in the toggle word, then it lies in exactly the `q` cyclic
`q`-windows whose starting positions immediately precede its position.
The fixed centre `w` is not `z`, so there are no other occurrences.  This
proves both assertions. \(\square\)

### Corollary 1.2

Let every rail on a positive shore be centred at `z`, and let every rail
on a nonempty negative shore be centred away from `z`.  If the two complete
owner vectors differ only by owners containing `z`, then no such trade
exists.

#### Proof

Every positive owner contains `z`.  Each negative rail has `N>q` and,
by Lemma 1.1, contributes a negative owner omitting `z`.  In a genuine
positive shore decomposition that occurrence must be supplied with at
least the same multiplicity on the positive shore unless it is among the
declared positive differences.  Neither is possible: the positive shore
and every declared difference contain `z`. \(\square\)

The argument does not require owner simplicity.  Simplicity merely makes
the unmatched occurrences visibly distinct.

## 2. Classification of every three-rail q=3 centre ledger

Suppose a physical q=3 trade has exactly three rails on each shore.  The
sharp centre theorem gives net masses `P=N>=3`; hence equality holds and
there is no aggregate centre/period cancellation between the two shores.

For q=3 the pointwise supporting inequality used in that theorem is

\[
 {4\over3}h+{1\over3}a+b\le |a|+|b|,              \tag{2.1}
\]

where `h=1` on the four target centres and `h=0` elsewhere.  Equality in
the summed bound forces equality at every coordinate.  Multiplying the
slack by three gives

\[
             3|a|-a+3|b|-3b=4h.                  \tag{2.2}
\]

At a target centre the congruence is `a=-1 mod 3`.  Equality in `(2.2)`
therefore gives

\[
             a\in\{-1,2\},\qquad b\ge0.           \tag{2.3}
\]

At an exterior centre equality gives

\[
             a=0,\qquad b\ge0.                    \tag{2.4}
\]

The global sums `sum a=-1` and `sum b=1` now force exactly one target
centre `z_0` with `a=2`, the other three target centres with `a=-1`, and
exactly one centre `w` (target or exterior) with `b=1`.  All other `b`'s
vanish.  Consequently every three-rail shore pair has precisely the form
listed in Section 0; the displayed profile in the centre theorem is only
the special choice `w=z_0`.

## 3. Point-degree obstruction

Let

\[
 H=C_0\cup\{z_0,z_1,z_2,z_3\}.                    \tag{3.1}
\]

The proposed three-by-three atom asks for rail collections
`A^+,A^-` satisfying

\[
 \sum_{Q\in A^+} f(Q)=
 \sum_{Q\in A^-} f(Q)+e_H,                         \tag{3.2}
\]

where `A^+` consists of two period-eight rails centred at `z_0` and one
period-nine rail centred at `w`, while `A^-` consists of one period-eight
rail at each of `z_1,z_2,z_3`.

The two short positive rails already give

\[
       \deg_{A^+}(z_0)\ge 2\cdot8=16.              \tag{3.3}
\]

By Lemma 1.1, each negative rail contains `z_0` in at most three owners,
and hence

\[
       \deg_{A^-}(z_0)\le 3\cdot3=9.               \tag{3.4}
\]

Taking the `z_0` point degree in `(3.2)` requires

\[
       \deg_{A^+}(z_0)=\deg_{A^-}(z_0)+1\le10,     \tag{3.5}
\]

contradicting `(3.3)`.  The period-nine rail at `w` contributes a
nonnegative additional amount to the left and so cannot help.

### Theorem 3.1

No q=3 trade using only periods eight and nine attains three rails per
shore.  In particular, the finite search proposed as equation (4.2) of
`MATH_THEOREM_DISTANCE_ONE_NEAR_C_TWO_PERIOD_CENTRE_CHARACTER_MINIMUM_20260814.md`
has an empty feasible set for this structural reason, and the realizable
minimum is at least four.

## 4. The unique four-rail centre shape

The obstruction also identifies the first centre ledger that can possibly
be realized.

For a physical trade, let `t_z` be the positive-minus-negative number of
rails not centred at `z` whose toggle word contains `z`.  Exact point
degrees refine the centre congruence to

\[
             8a_z+9b_z+3t_z=h_z,                 \tag{4.1}
\]

where `h_z=1` on the four target labels and zero elsewhere.  With four
rails on each shore one has

\[
                         |t_z|\le4.               \tag{4.2}
\]

If the net centre masses were still `P=N=3`, the classification in
Section 2 would apply: its proof used only the net \(\ell^1\) mass six,
not equality between net and physical shore sizes.  The fourth physical
rail on each shore would give exactly one unit of aggregate centre/period
cancellation.  At the distinguished short centre `z_0`, equation `(4.1)`
would require `t_z0=-5` when the positive long centre is elsewhere and
`t_z0=-8` when it is `z_0`, contradicting the physical-shore bound
`|t_z0|<=4`.  Hence a four-rail realization must have net masses `P=N=4`,
no aggregate cancellation, and

\[
             \sum_z(|a_z|+|b_z|)=8.               \tag{4.3}
\]

At a target coordinate, the centre congruence gives
`a=-1 mod 3`.  Combining `(4.1)--(4.2)` yields the following minimum local
costs over the allowed choices of `b` and `t`:

\[
\begin{array}{c|ccc}
a&-4&-1&2\\ \hline
\min_b(|a|+|b|)&7&1&3,
\end{array}                                      \tag{4.4}
\]

Any other target value (`a>=5` or `a<=-7`) has local cost at least eight,
while at an exterior coordinate any nonzero `a` is a multiple of three
and has minimum local cost at least five.  Every target has local cost at
least one.  Thus `(4.3)` excludes `a=-4`, all more distant target values,
and every nonzero exterior `a`.  The sum `sum a=-1` then forces

\[
             a_{z_0}=2,\qquad
             a_{z_1}=a_{z_2}=a_{z_3}=-1.          \tag{4.5}
\]

For `a=2`, `(4.1)--(4.2)` requires `b` to be `-1,-2`, or `-3`; for
`a=-1` it requires `b` to be `0,1`, or `2`; and for exterior `a=0`
it permits only `b=-1,0,1`.  Since `(4.5)` already has \(\ell^1\) mass five,
equation `(4.3)` leaves \(\ell^1\) mass three for `b`.  Together with
`sum b=1`, this forces

\[
 b_{z_0}=-1,
 \qquad b_z\ge0\ (z\ne z_0),
 \qquad \sum_{z\ne z_0}b_z=2.                    \tag{4.6}
\]

### Proposition 4.1

Every possible four-rail q=3 trade has the following centre multiset:

* positive: two period-eight rails at `z_0` and two period-nine rails
  whose centres, with repetition, have total multiplicity two away from
  `z_0`;
* negative: one period-nine rail at `z_0` and one period-eight rail at
  each of `z_1,z_2,z_3`.

The two positive long centres may be target or exterior labels, but a
repeated centre can only be a target.  Indeed, two positive long rails at
one exterior `x` would have `a_x=0,b_x=2`, forcing `t_x=-6` in `(4.1)` and
contradicting `(4.2)`.  This is only a necessary centre/point-degree shape;
cyclic-window owner equality is supplied separately by the companion
eleven-label theorem.

### Corollary 4.2 (the minimal ten-label ground is impossible)

At `z_0`, equations `(4.1)` and `(4.5)--(4.6)` give

\[
              8(2)+9(-1)+3t_{z_0}=1,qquad
              t_{z_0}=-2.                         \tag{4.7}
\]

Suppose the reduced label ground has its minimum possible size ten.  A
period-nine rail then toggles all nine labels other than its centre.  Both
positive long rails are centred away from `z_0` by Proposition 4.1, so
both toggle `z_0` and contribute `+2` to `t_{z_0}`.  The three negative
period-eight rails centred at `z_1,z_2,z_3` can contribute at worst `-3`;
the negative long rail is centred at `z_0` and is not counted in
`t_{z_0}`.  Hence

\[
                         t_{z_0}\ge2-3=-1,          \tag{4.8}
\]

contradicting `(4.7)`.  Therefore no four-by-four atom exists on ten
reduced labels.  Every possible four-by-four realization needs at least
eleven reduced labels and, more precisely, at least one of its two positive
period-nine toggle supports must omit `z_0`.

## 5. Corrected next gate (subsequently resolved at the owner level)

The next q=3 search must change the centre support before choosing cyclic
orders.  At least one of the following is necessary:

1. search the unique four-by-four centre shape of Proposition 4.1 on at
   least eleven reduced labels, forcing a positive long support to omit
   `z_0`;
2. add a larger common reserve whose toggle-support degrees satisfy
   `(4.1)`; or
3. enlarge the allowed core catalogue beyond the distance-one
   `C_0+z` model.

The centre congruences remain necessary, but they are not sufficient even
at their sharp \(\ell^1\) value.  The first additional feasibility test for
any proposed profile is therefore the binary centre-support incidence
test furnished by Lemma 1.1, before any cyclic-order exact cover is run.
The companion eleven-label theorem passes both tests for two distinct
target centres and gives a simple exact 34-versus-33 owner certificate.

## 6. Independent finite replay

The proof is symbolic.  The companion verifier

`scratch/verify_q3_near_c_centre_support_hole_20260814.py`

independently enumerates the relaxed product of all local integer centre
states compatible with the exact point equation `(4.1)` and
`|t_z|<=s`, using four target slots and eight exterior slots (enough
because every nonzero exterior state consumes at least one of the at most
eight units of net \(\ell^1\) mass).  The bound on `t_z` is necessary but
not sufficient for a common toggle-word realization, so the enumeration
is deliberately a superset.  It finds no net-mass-three relaxed state at
physical shore three **or** four, and every net-mass-four relaxed state at
shore four has the normal form of Proposition 4.1.

The verifier was copied to and run only on `ssh h100`.  Frozen SHA-256:

* verifier: `a8ce9583f1f00ede02f3237db6f808a4e38c977d9b5039849adf9b8e0dcb6a8b`;
* H100 output: `11a2d34661a0e028ff8061f7bdf61b1f5a776e498025a3d1c9ddd2fa63f03069`.

The exact output is

```text
PASS shore=3 net_mass=3 feasible_relaxed_states=0
PASS shore=4 net_mass=3 feasible_relaxed_states=0
PASS shore=4 net_mass=4 relaxed_states=40 centre_distribution_types=4
```

An independent named-owner CP-SAT over the four centre-placement types on
the ten-label ground also returned `INFEASIBLE` in every case.  Corollary
4.2 now subsumes those finite results, so the solver is supporting audit
material rather than part of the proof.
