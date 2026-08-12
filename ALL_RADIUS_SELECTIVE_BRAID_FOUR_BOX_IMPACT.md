# Impact of the all-radius selective triangular braid on the four-box programme

## 1. Scope

Assume the typed selective construction in the supplied note is valid.  Write

\[
 \mathcal T_R=\{P_0\}\cup\{E_{s,y}:1\le s\le R,\ 0\le y<s\},
 \qquad |\mathcal T_R|=1+\frac{R(R+1)}2,
\]

and let `rho(R)` be the repetition excess of the constructed spanning
triangular word.

This note records what follows for the four-box route, and what does not.
In particular, a triangular word supplies residual upper joins and, after
reflection and reversal, residual lower meets.  It is not automatically a
four-box max/OR word: central-square intervals, a linked factor band, and
coordinatewise pin survival remain separate requirements.

## 2. Exact recurrence ledger

The displayed construction has

\[
 n_R\le n_{R-2}+(R+1)+2R+\left\lfloor\frac R2\right\rfloor.
\]

Since

\[
 |\mathcal T_R|-|\mathcal T_{R-2}|=2R-1,
\]

its excess satisfies

\[
 \boxed{\rho(R)\le \rho(R-2)+R+\left\lfloor\frac R2\right\rfloor+2.}
 \tag{2.1}
\]

The three nonconstant contributions have distinct origins:

* `R`: the separately copied diagonal prefix, after subtracting the one
  genuinely new diagonal cell;
* `floor(R/2)`: the type-1 supplements for the even peaks;
* `2`: boundary bookkeeping left after subtracting the new alphabet.

Summing (2.1) gives

\[
 \rho(2t)\le\frac{3t^2+7t}{2},\qquad
 \rho(2t+1)\le\frac{3t^2+9t}{2}.
 \tag{2.2}
\]

Thus

\[
 \rho(R)\le\frac38R^2+O(R),\qquad
 n_R\le\frac78R^2+O(R).
 \tag{2.3}
\]

The proposed compression milestones have exact meanings:

| recurring cost retained | excess coefficient `c` in `rho(R)<=cR^2+O(R)` |
|---|---:|
| diagonal and supplements | `3/8` |
| diagonal only | `1/4` |
| supplements only | `1/8` |
| neither | `0` (hence `O(R)`) |

The last row still requires the constant increment in (2.1) to remain
bounded; it gives linear rather than zero excess.

### 2.1 Terminal metadata deletion

There is an immediate exact saving when the recursive word is used as a
finished triangular provider rather than as input to another lift.

#### Lemma 2.1 (terminal metadata deletion)

For `R>=2`, delete the initial `D_R` and the final `X_R` from the displayed
word `W_R`.  The remaining word is still spanning and represents every
triangular target.

#### Proof

The selected witnesses in the four cases of the construction lie,
respectively,

1. inside `B_R`;
2. inside `B_R`;
3. across the descending peaks in `B_R` and the initial lifted prefix of
   `sigma(W_(R-2))`; and
4. inside `sigma(W_(R-2))`.

None meets the leading `D_R` or trailing `X_R`, so all selected witnesses
survive.

The block `B_R` already contains every peak and every top-row cell.  The
lifted lower diagonal contains

\[
 P_1,E_{2,1},E_{3,2},\ldots,E_{R-1,R-2}.
\]

Thus every value occurring in `D_R` occurs later as well.  Every value in
`X_R` is a peak and already occurs in `B_R`.  Spanning also survives.  QED.

Consequently the actual finished triangular words obey the sharper finite
bounds

\[
 \bar\rho(2t)\le\frac{3t^2+t-2}{2}\quad(t\ge1),
\]

and

\[
 \bar\rho(2t+1)\le\frac{3t^2+3t-4}{2}\quad(t\ge1),
 \tag{2.4}
\]

with `bar rho(0)=bar rho(1)=0`.  This deletes only the outermost metadata;
the corresponding blocks at lower recursive radii remain physically
present.  Hence (2.4) retains the leading coefficient `3/8`.

## 3. Exact four-box tail-provider accounting

For the balanced four-chain box, the already proved sector ledger is

\[
 L_m=M_m+2\rho(m)+4\sum_{R=0}^{m-1}\rho(R)+O(m),
 \tag{3.1}
\]

where

\[
 M_m=\frac{2m^3+6m^2+7m+3}{3}
     =\frac23m^3+O(m^2)
\]

is the four-box width.  More precisely, the unmerged-endpoint version has
the additive term `4m+2` in place of `O(m)`.

If

\[
 \rho(R)\le cR^2+O(R),
\]

then (3.1) gives

\[
 L_m\le\left(\frac23+\frac{4c}{3}\right)m^3+O(m^2)
     =(1+2c)M_m+O(m^2).
 \tag{3.2}
\]

For the actual selective braid, `c=3/8`, so

\[
 \boxed{L_m\le\frac74M_m+O(m^2).}
 \tag{3.3}
\]

Using the raw braidable bounds (2.2), the overload term

\[
 Q_m:=2\rho(m)+4\sum_{R<m}\rho(R)
\]

obeys

\[
 Q_{2t}\le4t^3+13t^2-7t,
 \qquad
 Q_{2t+1}\le4t^3+19t^2+9t.
 \tag{3.4}
\]

Including the explicit `4m+2` endpoint allowance, this gives

\[
 L_{2t}\le\frac{28t^3+63t^2+17t+9}{3},
\]

and

\[
 L_{2t+1}\le\frac{28t^3+105t^2+101t+36}{3}.
 \tag{3.5}
\]

Lemma 2.1 sharpens the finite provider ledger.  With `bar rho` from (2.4),

\[
 \bar Q_{2t}\le4t^3+t^2-13t+10,
 \qquad
 \bar Q_{2t+1}\le4t^3+7t^2-9t+4.
 \tag{3.6}
\]

After the explicit `4m+2` endpoint allowance,

\[
 \bar L_{2t}\le\frac{28t^3+27t^2-t+39}{3},
\]

and

\[
 \bar L_{2t+1}\le\frac{28t^3+69t^2+47t+48}{3}.
 \tag{3.7}
\]

These are `O(m^2)` improvements over (3.5), as expected; both still have
leading ratio `7/4`.

The compression milestones translate as follows:

| triangular achievement | conditional four-box ratio |
|---|---:|
| present braid, `c=3/8` | `7/4` |
| eliminate supplements only, `c=1/4` | `3/2` |
| reuse diagonal ladder, `c=1/8` | `5/4` |
| `rho(R)=O(R)` | `1+o(1)` |

The diagonal reuse is therefore the first listed milestone that would beat
the existing global `sqrt(2)` coefficient, **if** the missing factor/pin
theorem and a uniform thick unequal-box extension were also proved.

At present (3.3) is only a residual-tail occurrence ledger.  It does not
improve the known global upper bound.  Independently, the three-short-side
fusion already attains the same `7/4` leading coefficient in the equal
four-box by a different construction.

## 4. A prefix-ladder separation barrier

The copied diagonal is not an accidental arithmetic oversight in the
literal recursion.  The following barrier is scoped to the stated
witness-preserving architecture.

### Proposition 4.1 (prefix-ladder separation)

Assume a two-level fold recursion has all of the following properties.

1. The lower word has an exact initial diagonal ladder
   
   \[
   D_R=P_0,P_1,E_{2,1},\ldots,E_{R,R-1}.
   \]
2. The current targets `(0,r,x)`, `x>0`, are represented by starting in a
   fresh descending peak scaffold, passing its `P_0`, and stopping in the
   lifted diagonal ladder.
3. Selected lower witnesses are inherited as unchanged contiguous lifted
   spans; no new maximum-row letter may be inserted inside such a span.
4. At the next recursion, the same physical ladder is to be used after the
   next fresh peak scaffold.

Then the current ladder cannot simultaneously be the exact initial ladder
required for the next recursive call.  A second separated ladder occurrence,
or a violation of at least one of items 1--4, is necessary.

### Proof

For the current target `(0,r,x)`, the chosen interval crosses the cut from
the fresh peak scaffold into the ladder.  After lifting one level, its
maximum first coordinate is at most the old maximum plus one.

To use that same ladder after the next fresh scaffold, the new scaffold has
to be placed on the scaffold side of this cut.  The old crossing interval
then contains an inserted letter from the new maximum row.  That row is one
above the desired lifted maximum, so the old selected witness is destroyed.
Thus the cut cannot both remain insertion-free for inherited witnesses and
receive the next scaffold.  QED.

There is also a static reason the exact initial `D_R` cannot itself replace
the later boundary ladder.  The prefix ending at `E_(x+1,x)` has maximum
first coordinate only `x+1`.  Extending farther inside `D_R` meets
`E_(x+2,x+1)` and raises the maximum height above `x`.  Hence this exact
prefix cannot represent `(0,r,x)` when `r>=x+2`.

This proposition is not an unrestricted lower bound on `rho(R)`.  It says
that eliminating the `R` term requires a genuinely different invariant:
one must reselect old witnesses, permit controlled insertion through them,
replace the exact-prefix state by a distributed portal state, or fuse more
than one recursive level at once.

## 5. Exact status of the parity supplements

Inside the displayed descending peak block, the selected height-zero
targets use the exact intervals

\[
 P_r,P_{r-1},\ldots,P_u.
\]

In particular, each adjacent pair `P_(s+1),P_s` must contain both peak
types.  Therefore the types on the scaffold alternate.  With `P_0` of type
zero, every positive even scaffold peak is type zero.  If, as in the
displayed recursion, every peak created by the selective lift is also
declared type zero, then none of those even labels has a type-one occurrence
outside the supplement block.  Peak-fibre survival consequently forces
exactly

\[
 \left\lfloor\frac R2\right\rfloor
\]

additional type-one occurrences.  Thus `X_R` is optimal **under the stated
typing convention and the exact adjacent-pair witnesses**.

It is not yet proved optimal in an unrestricted typed braid.  Existing
lifted peak occurrences can in principle be recoloured.  The exact sharing
problem is a finite hypergraph problem.

Let `O` be the lifted peak occurrences, and for every selected lifted
witness `J` let `H_J \subseteq O` be the occurrences currently supplying its
type-zero hits.  Let `L` be the set of peak labels whose scaffold occurrence
is type zero.  A recolouring set `C \subseteq O` safely replaces the
supplement for every label in `pi(C)` precisely when

\[
 C\cap\pi^{-1}(s)\ne\varnothing\quad(s\in\pi(C)),
 \qquad
 H_J\setminus C\ne\varnothing\quad\text{for every }J.
 \tag{5.1}
\]

After such a recolouring, only the labels in `L \setminus \pi(C)` need literal
supplements.  Equation (5.1) is therefore the exact parity-sharing target.
It separates a potentially removable `R/2` cost from the genuinely harder
diagonal separation cost.

## 6. Safe conclusion

Assuming the selective construction, the unconditional triangular theorem
is a real all-radius improvement:

\[
 g_\triangle(R)\le\frac78R^2+O(R),
 \qquad
 \rho(R)\le\frac38R^2+O(R).
\]

Its proved effect on the four-box programme is to reduce the residual-tail
provider ledger from ratio `2` to ratio `7/4`.  It does not yet change the
best Boolean-cube upper bound, because:

1. `7/4>sqrt(2)`;
2. central-square intervals are not supplied by triangular universality;
3. reflected lower tails are meets, not OR witnesses;
4. no linked factor band or pin-survival theorem is supplied; and
5. equal-box triangular geometry has not been made uniform over the jointly
   thick unequal boxes required by aggregation.

The most valuable next theorem is not another verification of (2.1).  It is
either:

* a distributed portal invariant that evades Proposition 4.1 and reduces
  the diagonal contribution from `R` to `o(R)` per two-level lift; or
* a solution of the recolouring system (5.1) with `o(R)` uncovered labels,
  followed by such a diagonal theorem.

Only the diagonal result by itself reaches the conditional `5/4` regime;
both results together, with the factor/pin bridge, reopen the constant-one
four-box route.
