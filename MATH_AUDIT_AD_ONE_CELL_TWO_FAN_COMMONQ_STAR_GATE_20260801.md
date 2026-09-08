# The inserted-star fan surplus is one address, not an automatic common-`Q` credit

Date: 2026-08-01  
Lane: AD, adversarial audit of the one-cell two-fan closure  
Status: exact common-`Q` criterion, exact canonical cap, exact
fan--crossing incompatibility for the proposed canonical new-chain bank,
and smallest scoped obstructions.  The result strengthens the fixed-state Hall normal form in
`MATH_THEOREM_AD_ONE_CELL_TWO_FAN_EXACT_EAR_HALL_CUT_20260801.md`.

## 0. Verdict

The scalar ledger is correct.  Moving the `d-1` destroyed crossing targets
to post-switch native cells and putting the `2(d-1)` old-chain targets on
the `2d-1` fan cells leaves one physical fan address.  This alone proves
only `alpha>=ell`, not `alpha=ell+1`.

For the literal two-sided coatom carving, both old chains must use the
non-singleton fan cells.  The unique spare is the inserted singleton `*`.
Before an ear is placed there, its maximal common-`Q` letter is

\[
 C_* =P_*\cap\bigcap_{(I,S):*\in I}S.                         \tag{0.1}
\]

In the source-private canonical face this is

\[
 C_*=K\cup\{\mathord\infty,c\}.                              \tag{0.2}
\]

Thus a target `h` has an edge to the spare only if it is a nonempty subset
of this cap and if capping the singleton to `h` does not delete a unique
positive witness.  This is the exact missing edge in the one-credit Hall
theorem.  In particular, the spare cannot automatically carry a native
`q1` target or any of the old/new packet-chain targets: their ranks exceed
the rank of (0.2).

There is a positive conditional conclusion.  If the prospective exposed
target is deliberately labelled inside (0.2), every coordinate which is
forced to use `*` belongs to it, and all other local pins satisfy the
source-private trace guard, then the ear is literal, common-`Q`, and
nonzero.  Under exactly these hypotheses the cardinal surplus becomes the
claimed one credit.

However, the new exact fan--crossing identity adds an earlier obstruction.
The two canonical **old** fan chains force every destroyed crossing target,
outside the typed star target, to contain both active labels and the entire
filler flag.  A canonical **new** prefix or suffix chain target does not
have that form.  Hence the proposed assignment "destroyed pins = one
canonical new chain" is impossible already at `d=2`.  The one-credit macro
must change the crossing bank or one of the fan chains before the
common-`Q` ear test is even reached.

## 1. Exact maximal-source formulation

Fix a final carrier `T`, its maximal envelopes `P_p`, and a pin table
`mathcal B`.  For each source position define

\[
 C_p(\mathcal B)=P_p\cap
       \bigcap_{(I,S)\in\mathcal B:\ p\in I}S.                \tag{1.1}
\]

This is precisely the maximal common-`Q` source letter at `p`: a coordinate
survives there iff it belongs to the envelope and no pin covering `p`
omits it.

Let `mathcal R(mathcal B)` contain all positive rows:

* `([i,i+d],x)` for `x in T_i`; and
* `(I,x)` for every pin `(I,S)` and `x in S`.

Assume `mathcal B` already passes common-`Q` and is nonzero.  At a fixed
position `*`, define its **unique-star load**

\[
 U_* =\{x:\text{some }(I,x)\in\mathcal R(\mathcal B)
       \text{ has }*\in I,
       \ x\notin C_p(\mathcal B)
       \text{ for all }p\in I-\{*\}\}.                      \tag{1.2}
\]

Every `x in U_*` necessarily lies in `C_*(mathcal B)`, because the old table
is feasible.

### Theorem 1.1 (exact singleton-ear criterion)

Add the singleton pin `({*},h)` for a previously exposed nonempty strict
lower target `h`.  The enlarged pin table passes the exact common-`Q` and
nonzero tests if and only if

\[
 \boxed{\qquad \varnothing\ne h\subseteq C_*(\mathcal B),
                    \qquad U_*\subseteq h.\qquad}             \tag{1.3}
\]

#### Proof

At every `p ne *`, adding the pin changes nothing.  At `*`, (1.1) becomes

\[
 C_*'=C_*(\mathcal B)\cap h.                                 \tag{1.4}
\]

The new positive rows `({*},x)`, `x in h`, hold exactly when
`h subseteq C_*(mathcal B)`; then `C_*'=h`.  Nonzeroness at the only changed
position is exactly `h ne emptyset`.

An old positive row can fail only if its sole old witness was `*` and its
coordinate is deleted by (1.4).  The collection of precisely those
coordinates is `U_*`, so all old rows survive exactly when `U_* subseteq h`.
These are the two obstruction types of the bounded common-`Q` theorem, and
there are no other changed rows or positions.  \(\square\)

This theorem is statewise.  Taking the union of possible caps over several
terminal states is unsound.

## 2. Why the carved spare is forced to be the singleton

Put

\[
 G=K\cup\{\mathord\infty,c\}.
\]

The two old deep chains of one canonical packet can be written, for
`1<=s<=d-1`, as

\[
 A_s=G\cup\{b,f_1,\ldots,f_s\},\qquad
 B_s=G\cup\{a,f_{d-s+1},\ldots,f_d\}.                        \tag{2.1}
\]

They are strict chains on their own shores, while every `A_s` and `B_t`
are incomparable: `b in A_s-B_t` and `a in B_t-A_s`.

Let `L_1 subset ... subset L_d` and `R_1 subset ... subset R_d` be the two
fans, with `L_1=R_1={*}`.  Interval unions are monotone under inclusion, so
the `A` and `B` chains must appear in their displayed orders on their
respective fans.

### Lemma 2.1 (forced non-singleton carving)

No literal realization of both chains can assign `L_1=R_1` to a member of
either chain.  Consequently any injection of all `2(d-1)` targets into the
`2d-1` fan cells uses

\[
 A_s\longmapsto L_{s+1},\qquad
 B_s\longmapsto R_{s+1}                                    \tag{2.2}
\]

up to reversing both chain indices, and leaves `{*}` unused.

#### Proof

If the singleton had value `A_s`, then every right-fan union would contain
`A_s`, contradicting `b notin B_t`.  The symmetric argument excludes every
`B_t`.  The count now forces all non-singleton fan cells to be used, and
nestedness forces the order.  \(\square\)

Every fan pin covers `*`.  Hence, ignoring other retained pins through the
cut,

\[
 C_*\subseteq P_*\cap
       \bigcap_s A_s\cap\bigcap_s B_s=P_*\cap G.              \tag{2.3}
\]

Under the prepared endpoint envelopes `G subseteq P_*`, and with no other
pin through `*`, equality holds.  Since the packet rank is

\[
 r=|K|+d+4,
\]

the canonical spare cap has size

\[
 |G|=|K|+2=r-d-2.                                            \tag{2.4}
\]

The smallest old-chain target has rank `r-d`; the native `q1` targets have
rank `r-1`.  Therefore neither is a possible singleton ear target.  This is
already a zero-neighbour Hall cut at `d=2` for any proposed `q1` ear.

The word "spare" must therefore be read literally as **unused address**,
not as an automatically programmable `q1` address.

## 3. Exact interface with the crossing-cell telescope

For the `d-1` old length-`d` crossing cells, index the cut by
`1<=i<=d-1`.  Their old nonstar supports are

\[
 I_i=\{-i,\ldots,-1\}\cup\{1,\ldots,d-i\}.                  \tag{3.1}
\]

Thus a negative position `-t` has signature `1_(i>=t)` and a positive
position `+t` has signature `1_(i<=d-t)`.  After insertion their convex
hulls have length `d+1`, so these pins are destroyed and their targets are
paid on post-switch native cells.  They impose no negative constraint at
`*` in the final table.

This validates the scalar count, but the values on the crossing cells are
not free.  The exact identity in
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md` gives the following
additional gate.

### Theorem 3.1 (canonical old fans force the crossing bank)

Let the typed singleton be a target `Z subseteq G`, and realize the old fan
chains (2.1) by

\[
 L_{s+1}=A_s,\qquad R_{s+1}=B_s
       \qquad(1\le s\le d-1).                                \tag{3.2}
\]

Then every compatible old crossing target `C_i`, `1<=i<=d-1`, satisfies

\[
 \boxed{
 C_i\setminus Z=(G\setminus Z)\cup
                  \{a,b,f_1,\ldots,f_d\}.}                   \tag{3.3}
\]

The only remaining freedom is the membership of coordinates in `Z`; for
each `z in Z`, its zero set

\[
                 \{i:z\notin C_i\}                            \tag{3.4}
\]

must be an interval.  Conversely, every bank satisfying (3.3)--(3.4) is
realized by side copies of the star coordinates.

#### Proof

The star-hidden identity says, for every `x notin Z`,

\[
 x\in C_i\iff x\in L_{i+1}\ \hbox{or}\
                     x\in R_{d-i+1}.                         \tag{3.5}
\]

Using (2.1),

\[
 L_{i+1}\cup R_{d-i+1}
   =G\cup\{a,b,f_1,\ldots,f_d\},                            \tag{3.6}
\]

independently of `i`.  This proves (3.3).  The interval-zero statement and
its converse are exactly the star-coordinate part of the same theorem.
\(\square\)

A canonical phase-new prefix target has the form

\[
       G\cup\{a,f_1,\ldots,f_i\},                             \tag{3.7}
\]

and a canonical phase-new suffix target has the form

\[
       G\cup\{b,f_{i+1},\ldots,f_d\}.                         \tag{3.8}
\]

The first omits `b,f_(i+1),...,f_d`; the second omits
`a,f_1,...,f_i`.  Both contradict (3.3), for every
`1<=i<=d-1`.  At `d=2`, (3.3) already forces
`{a,b,f_1,f_2}` outside `Z`, whereas the sole target in (3.7) or (3.8)
misses two of these labels.  Thus `d=2` is the smallest obstruction.

Although the crossing pins disappear from the **terminal** table and hence
impose no terminal negative at `*`, their old target values must first be
realized by the same side sources.  This is why they cannot be chosen
independently of the fans.

Even after (3.3)--(3.4) is met, the terminal common-`Q` test does **not**
remove:

1. transported crossing pins of old length below `d`, whose new hulls do
   cover `*`;
2. any retained external pin through the seam; or
3. the positive rows which may have `*` as their unique source witness.

All such data enter (1.1)--(1.2).  In a source-private seam they are absent
or have already been certified compatible.  Without that privacy, the
endpoint transporter envelopes alone do not imply common-`Q`.

## 4. Two smallest mixed-cover obstructions

The first seam-specific interaction occurs at `d=3`, because an old
crossing interval of length two transports to a legal length-three hull.
Use source positions `-1,*,1`.

### 4.1 Empty-position core

Let

\[
 P_* =\{g,x\}.
\]

Take a left fan pin whose target contains `g` but omits `x`, and a
transported crossing pin whose target contains `x` but omits `g`.  Both
cover `*`.  They are separately feasible, but together their intersection
with `P_*` is empty.  This is a two-pin empty-position certificate.

### 4.2 Positive-cover core with nonzero star

Let the transported crossing target be `{g,x}`, and suppose `x` has only
one legal envelope position, `-1`.  Let the left fan pin cover `{-1,*}` and
omit `x`.  Then `g` survives at `*`, so the source word is locally nonzero,
but the crossing positive row for `x` has all legal positions covered by
one negative pin.  This is a one-negative-pin positive-cover certificate.

These examples do not refute the source-private carved face.  They prove
that envelope containment, separate fan carving, and marginal native-cell
assignment do not automatically compose.

## 5. Correct one-credit theorem

Let `O` be the `2(d-1)` old-chain targets, `N` the `d-1` destroyed crossing
targets, and `h` one exposed compiler target.  Suppose:

1. the old side sources realize `N` jointly with the fans, equivalently
   `N` satisfies (3.3)--(3.4), and post-switch native cells carry `N` in
   one literal terminal cap state;
2. the endpoint transporters realize (2.2) in that same state;
3. every retained pin meeting the carved source region contains the
   exhibited source letter at each point it covers (source privacy is a
   sufficient form of this condition);
4. the baseline unique-star load and cap satisfy

   \[
       \varnothing\ne h\subseteq C_*,\qquad U_*\subseteq h;  \tag{5.1}
   \]

5. `h` is still exposed and all named cells are distinct.

Then the native cells restore `N`, the non-singleton fans restore `O`, and
the singleton realizes `h`.  The complete assignment is literal and
common-`Q`, every source position remains nonzero, and the local matching
gain is exactly

\[
                            \alpha=\ell+1.                    \tag{5.2}
\]

If (5.1) fails, the exact residual obstruction is already the singleton
target cut `{h}` on this deterministic carved face.  In a larger fan
incidence graph it is the tight-set cut from the one-cell exact ear Hall
theorem.

Thus two decisive constructive tasks remain.  First replace the
incompatible canonical new-chain crossing bank by a bank satisfying
(3.3)--(3.4), or alter a fan chain.  Then expose or route one lower target
`h` into the common carved cap while preserving (5.1).  The canonical
packet makes neither step automatic.

## 6. Independent replay

The dependency-free audit checks `d=2,...,6`, the forced singleton spare,
the exact common intersection, and the two `d=3` cores:

```text
scratch/audit_ad_one_cell_two_fan_commonq_star_gate_20260801.py
scratch/ad_one_cell_two_fan_commonq_star_gate_20260801.audit.json
```

It reports

```text
PASS_ONE_CELL_TWO_FAN_COMMONQ_STAR_GATE
```

with payload SHA-256

```text
a00d1aa44cbf60cb0ac703cc7e89afe3b5fcd7e5e9f4073ae1f4bd1b56a3d156
```
