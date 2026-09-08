# Opposite seam Cartesian ears cannot share one literal old-pair support

Date: 2026-08-01  
Status: corrected scoped typed-resource obstruction.  The two orientations
never have the same typed old-pair tail set.  This rules out the
literal-common-support/no-quarantine specialization.  It does **not** rule
out the general phase-paired reset-completion criterion, which permits
different phase-private packet resources provided contraction (and any
declared common deletion) leaves one identified residual exterior.

## 0. Outcome

Let

\[
 e_{\to}=(L,U,E,F),\qquad e_{\leftarrow}=(L,U,F,E)
 \tag{0.1}
\]

be the two orientations of one Boolean seam, where

\[
 E=L\cup\{d\},\qquad F=L\cup\{a\},\qquad
 U=L\cup\{a,d\},\qquad a\ne d.                      \tag{0.2}
\]

For either target, the ternary Boolean Cartesian fan replaces an old pair
`O^-` by a new triple and fills exactly the four resources of the target.
There are `(m-1)^2` choices in each orientation.

No forward fan option and reverse fan option have the same typed resource
set on their two old atoms.  In fact their **tail sets alone** can never
agree.  Consequently a pair consisting of one standard Cartesian gain ear
for each opened-reset phase cannot use one identical literal old-pair
support.

This does not by itself refute two independent phase-private ears.  If the
two unequal tail banks are private (or all atoms meeting their union are
deleted from both phase exteriors), contracting either packet can still
leave the same common residual system.  The remaining exact requirement is
therefore privacy/common-minor equality, not equality of packet supports.

## 1. The two old-pair tail sets

For the forward target `e_to`, choose

\[
                         b\in L,\qquad c\notin U.       \tag{1.1}
\]

The exact Cartesian-fan formula gives the two old-pair tails

\[
 \mathcal T_{\to}(b,c)
   =\{\,U-b,\ L-b+c+d\,\}.                            \tag{1.2}
\]

For the reverse target `e_left`, the roles of `a,d` are exchanged.  With

\[
                         b'\in L,\qquad c'\notin U,     \tag{1.3}
\]

its old-pair tails are

\[
 \mathcal T_{\leftarrow}(b',c')
   =\{\,U-b',\ L-b'+c'+a\,\}.                         \tag{1.4}
\]

All displayed sets have middle rank.  The first member in either pair has
outside-`L` part `{a,d}`.  The second member of (1.2) has outside-`L` part
`{c,d}`, while the second member of (1.4) has outside-`L` part `{c',a}`.

### Theorem 1.1 (tail-set obstruction)

For all choices satisfying (1.1) and (1.3),

\[
             \mathcal T_{\to}(b,c)
             \ne
             \mathcal T_{\leftarrow}(b',c').         \tag{1.5}
\]

#### Proof

The set `U-b` cannot equal the second member of (1.4).  Its two elements
outside `L` are `a,d`, whereas the latter's are `a,c'`; equality would force
`c'=d`, contrary to `c' notin U` and `d in U`.

Likewise, the second member of (1.2) cannot equal `U-b'`: equality would
force `c=a`, contrary to `c notin U` and `a in U`.

Hence equality of the two unordered pairs would have to match first member
to first member.  This forces

\[
                         U-b=U-b',
\]

and therefore `b=b'`.  Equality of the remaining members would then give

\[
                    L-b+c+d=L-b+c'+a.                \tag{1.6}
\]

Comparing their outside-`L` parts gives `{c,d}={c',a}`.  The unique member
of the left pair lying in `U-L` is `d`, while the unique such member of the
right pair is `a`; since `a!=d`, equality is impossible.  This proves
(1.5).  \(\square\)

The argument uses only typed tail resources.  No lower, owner, flag,
residence or compiler condition is needed.

## 2. Exact consequence and the contraction correction

Open the forward and reverse rolling-reset phases at their opposite seam
atoms (0.1).  In either phase, adjoining its missing seam atom restores the
same complete reset resource inventories.  A Cartesian gain ear has

\[
        \operatorname{res}(N_e)
        =\operatorname{res}(O^-_e)\mathbin{\dot\cup}
          \operatorname{res}(e).                       \tag{2.1}
\]

Therefore, after the reset interior and its phase-specific seam atom are
contracted, **equality of the consumed literal packet supports** would
require the two old-pair typed resource sets to agree.  In particular it
would require

\[
             \mathcal T_{\to}(b,c)
             =
             \mathcal T_{\leftarrow}(b',c'),           \tag{2.2}
\]

which Theorem 1.1 forbids.

### Corollary 2.1 (literal-common-support no-go)

No pair of independent standard Cartesian gain ears, one centred at
`e_to` and one at `e_left`, satisfies the common occurrence-labelled
**packet-support equality** condition.

This remains true if the non-tail resources happen to be collision-free or
both individual ears admit lossless depth-three flag lifts: the typed tail
systems already differ.

It is not a no-go for the general phase-paired Boolean-hex reset-completion
theorem.  To see the quantifier exactly, let `R` be any common exterior on
resources disjoint from both old-pair tail banks.  Adjoin the forward ear as
a private direct summand in the forward phase and the reverse ear as a
private direct summand in the reverse phase.  Contract the respective
private summand.  Both residuals are literally `R`, although (2.2) fails.
The same conclusion holds when all atoms meeting the union of the two
phase-private banks are explicitly deleted before comparing residuals.

Hence equality in (2.2) is necessary only on a face which forbids extra
quarantine and insists that both phases consume the same occurrence-labelled
packet resources.  In the actual phase-paired theorem, one must instead
prove that the unequal resources are private and that the contracted
residual matroids/caps agree.

## 3. Correct next search space

This no-go removes the complete `(m-1)^4` product only from the
literal-common-support search.  The live alternatives are:

1. one phase-private ear per orientation, with the unequal tail banks
   quarantined and an independently proved common residual contraction;
2. two or more ears in at least one phase, with their private tail
   differences cancelling as one coupled trade;
3. a non-Cartesian owner-changing path whose contracted module has the same
   typed resource support in both phases; or
4. a larger phase module allowing a literal bijection of residual resources
   only after internal alternating cancellation.

The closed-toggle parity theorem still applies: a purely matching-closed
composition of Boolean hex cycles has even attachment sign, whereas the
rolling reset requires odd attachment sign.  Hence any coupled solution
must retain a genuine gain/loss or open-boundary state during the
composition.
