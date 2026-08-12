# Audit of the sparse boundary and spine-recycling proposal

## Verdict

**PARTIAL PASS, WITH ONE FATAL PINNING ERROR AND TWO SCOPE ERRORS.**

The proposal contains several exact shadow-level lemmas.

* The two-step sparse section is correct, and its omitted alphabet is exactly
  the `2R-1` new cells of `T_R\T_(R-2)`.
* The three displayed boundary words cover every target with `u<2` or
  `x<3`.
* Both cross-`c` provider identities are exact coordinatewise-join
  identities.
* The alternating `L/U` band represents every advertised upper target.
* Conditional on a genuine word-level spine identification preserving all
  inherited and boundary witnesses, the local excess recurrence has the
  claimed arithmetic.

They do **not** prove the claimed factor or pin reduction.

1. The `E\vee E` formulas produce upper joins of middle points.  They do not
   construct lower meet cores of a central interval factor.
2. No monotone linked family of physical central witness intervals is
   supplied.  A linked interval in the *word of middle labels* is not the
   common core of physical intervals realizing those labels.
3. Most importantly, acyclicity of the band-junction graph does not imply
   pin survival.  A negative merge forest needs a negative assigned parent
   interval covering every linked hull.  A forest supplies no such parent.
   A three-position counterexample is given in Section 7 below.

Consequently the proposed spine-recycling lemma is a legitimate **open
upper-shadow sharing target**, but its forest clause is insufficient for an
OR-factor theorem.  The currently proved asymptotic coefficient does not
change.

## 1. The triangular chamber and recurrence arithmetic

The alphabet and target counts are the standard ones:

\[
 |\mathcal T_R|=1+\frac{R(R+1)}2,
 \qquad
 \#\{(u,r,x)\}=\sum_{r=1}^R r^2.
\]

For fixed `0<epsilon<=1`, the implication

\[
 \rho(R)\le \rho(R-2)+O(R^{1-\epsilon})
 \quad\Longrightarrow\quad
 \rho(R)=O(R^{2-\epsilon})
\]

is correct after summing separately over the two parities.  Summing the
fixed-`c` radii then gives `O(m^(3-epsilon))`.  If one had the corresponding
**actual factor construction uniformly for every unequal and degenerate
four-chain box**, the existing subcritical four-box aggregation theorem
would give

\[
 \nu(k)=W(k)+O(W(k)k^{-\epsilon/2}).
\]

This last sentence is conditional on the factor and uniform-box hypotheses;
the triangular shadow recurrence alone does not supply them.

## 2. The two-step sparse section

Define

\[
 \Sigma_R(P_a)=P_{a+2},\qquad
 \Sigma_R(E_{a,b})=E_{a+2,b+2}\quad(b\ge1).
\]

If a lower interval has box `[u,r]x[0,x]` with `x>=1`, its image has first
extrema `u+2,r+2`.  A peak preserves height zero, while a cell attaining
height `x` maps to one attaining `x+2`; no image cell has greater height.
Thus the image box is exactly

\[
 [u+2,r+2]\times[0,x+2].
\]

The image alphabet is

\[
 \{P_2,\ldots,P_R\}
 \cup\{E_{s,y}:3\le y<s\le R\}.
\]

Its complement is exactly

\[
 \mathcal S_R=\{P_0,P_1\}
 \cup\{E_{s,1}:2\le s\le R\}
 \cup\{E_{s,2}:3\le s\le R\},
\]

of size `2R-1`, equal to

\[
 |\mathcal T_R|-|\mathcal T_{R-2}|.
\]

The noninherited target regime is exactly `u<2 or x<3`.  This section
therefore passes.

### Novelty qualification

This is the twofold composition of the already proved one-step sparse
section `psi_R` in Section 6 of `CONSTRUCTIVE_CONSTANT_ONE_NEXT.md`:

\[
 \psi_R(P_a)=P_{a+1},\qquad
 \psi_R(E_{a,b})=E_{a+1,b+1}.
\]

That note already proves the one-step zero-overhead alphabet ledger.  The
two-step formulation is useful for matching the three-layer boundary, but
it is not a new elimination of a previously unresolved fibre tax.

## 3. The three-band boundary braid

For `R>=3`, the displayed words have lengths

\[
 |F_R|=2R,\qquad |K_R|=3R-2,\qquad |J_R|=2R-3.
\]

Every proposed witness is exact.

* A peak segment in `F_R` covers `x=0`.
* From `P_r` through `P_0` and `D_x`, `F_R` covers `u=0,x>0`; the inequality
  `x+1<=r` prevents diagonal contamination.
* From `C_r` to `P_u`, `K_R` covers `x=1,u>=1`.
* From `C_r` through `P_1` to `D_x`, `K_R` covers `u=1,x>=1`.
* From `H_r` to `P_u`, `J_R` covers `x=2,u>=2`.

These classes exhaust `u<2 or x<3`.  Direct interval enumeration passes for
every `2<=R<=30`.

The three words collectively contain every cell of `S_R`.  They do not yet
contain those cells with exact multiplicity one.  Relative to one copy of
each new cell, there are five constant duplicates:

* one extra `P_1`;
* two extra occurrences of `C_2=D_1`; and
* two extra occurrences of `H_3=D_2`.

All remaining repeated boundary occurrences are old-image peaks or the
old-image diagonal cells `D_j`, `j>=3`.  Hence the proposal's later
`q_R+O(1)` ledger is arithmetically consistent if the claimed high-spine
identifications really exist.

This is a valid explicit boundary-shadow braid.  Boundary scaffolds and
standalone low-height corridors already existed in
`CONSTRUCTIVE_CONSTANT_ONE_NEXT.md` and the all-radius selective braid; the
particular clean three-word partition is a useful new presentation, not a
factor theorem.

## 4. The cross-threshold provider identity

With

\[
 E(c,r,x)=(c+r,m-c-x,x,m-r)
\]

and `0<=y<=min(c,x,u-1)`, direct coordinatewise maximization gives

\[
 E(c,r,x)\vee E(c-y,u,y)
   =(c+r,m-c,x,m-u)=Q(c,u,r,x).
\]

The identity and the deterministic choice

\[
 y=\min\{c,x,u-1\}
\]

are correct.

The terminology needs care.  `E(c-y,u,y)` is a provider from a lower
threshold sector, but the displayed equation is a **join of two middle
points producing an upper target**.  It is not a lower lattice meet and is
not a common physical core of central witness intervals.

## 5. The alternating linked band

The linked-band calculation is correct after stating the missing domains,
for example

\[
 0\le y\le\min(c,x),\qquad x<R=m-c.
\]

In

\[
 L_{y+1},U_{y+2},L_{y+2},U_{y+3},\ldots,L_{R-1},U_R,
\]

the interval from `L_u` to `U_r` contains `L_v` for `u<=v<r` and `U_s`
for `u<s<=r`.  Every such point lies coordinatewise below
`Q(c,u,r,x)`, while `L_u` supplies coordinates two and four and `U_r`
supplies coordinates one and three.  Its join is therefore exact.

There is an accounting qualification.  When `x>=s`, an internal
`U_s=E(c,s,x)` is not a cell of the fixed triangular alphabet `T_R`, whose
arm notation assumes `x<s`.  It is still a valid point of the full
four-box middle layer.  Thus this is a legitimate cross-sector middle-layer
band, but it cannot be inserted into a recurrence for `rho(R)` without
accounting for sharing with the other square sectors.

More importantly, the interval from `L_u` to `U_r` is an upper-join witness
in a word of middle labels.  It is not a physical central witness interval
`I_i=[i+alpha_i,i+beta_i]` realizing an individual middle label, and `L_u`
is not the intersection of such physical intervals.  The assertions
"factor-friendly" and "genuine meet core" therefore remain desiderata, not
consequences of this theorem.

## 6. The three-provider identity

Under `c>=x>=u>=1`, all three displayed providers are legal middle points,
and

\[
 \begin{split}
 &E(c,r,u)\vee E(c-u+1,u,u-1)\vee E(c-x,x+1,x)\\
 &\hspace{35mm}=(c+r,m-c,x,m-u).
 \end{split}
\]

The first point supplies coordinate one, the second supplies coordinates
two and four, and the third supplies coordinate three.  This algebraic
identity passes.  It is a useful noncanonical upper-provider formula, but,
again, it neither produces a lower-rank OR witness nor specifies physical
central intervals and pins.

## 7. The forest-to-pinning claim is false

The negative merge-forest theorem in `PINNING_THEOREM.md` requires more than
an acyclic junction graph.  For every coordinate `b`, every linked negative
hull must be contained in an **actually assigned negative interval**, and
the complete assigned system must be containment-monotone.  A graph forest
does not manufacture the required negative parent.

Here is a minimal counterexample.  Use three positions and coordinates
`a,b,c`, and prescribe

\[
 I_X=[1,2],\quad X=\{a\},
 \qquad
 I_Y=[2,3],\quad Y=\{c\},
 \qquad
 I_S=[1,3],\quad S=\{a,b,c\}.
\]

This partial assignment is containment-monotone: `X subset S` and
`Y subset S`.  It also has the correct endpoint-chain behavior.  For the
coordinate `b`, the two negative intervals `I_X,I_Y` are linked and their
junction graph is the one-edge tree.  Each child band is locally trivial.
Nevertheless

\[
 U_b=I_X\cup I_Y=[1,3],\qquad Z_b=\varnothing,
\]

so the positive interval `I_S` has no surviving `b`-pin.

The hull of the two negative children is `[1,3]=I_S`, which is positive.
There is no negative assigned parent covering that hull.  In fact, adding
one while retaining containment monotonicity is impossible in this
three-position system: any containing interval is `[1,3]`, already assigned
to the positive target.

Thus the statements

> a forest-like linked-band superposition has pin survival

and

> one hull witness per junction suffices automatically

are false.  What is sufficient is the earlier, stronger condition:

* for every coordinate, an explicit sign-correct negative merge forest;
* every parent is an assigned negative target whose interval contains the
  linked child hull;
* distinct roots have clean integer separators; and
* containment monotonicity holds globally.

Those conditions have not been constructed for the proposed bands.

## 8. What the spine recurrence would actually prove

At the abstract triangular-word level, the length bookkeeping is exact.
Start with a spanning word of length

\[
 |T_{R-2}|+\rho(R-2).
\]

Its sparse image has the same length.  One copy of each cell in `S_R` pays
exactly the alphabet growth `2R-1`.  If all boundary witnesses can be
superposed with only `q_R` additional old-image occurrences and `O(1)`
new-cell duplicates/cuts, while every inherited witness stays contiguous,
then

\[
 \rho(R)\le\rho(R-2)+q_R+O(1).
\]

This is a correct sufficient shadow theorem.  It is also precisely the
unproved difficult step: identifying equal labels is not enough; their
orders must be simultaneously compatible with all inherited and boundary
witness intervals.

For the claimed global OR-factor consequence, the spine lemma must be
strengthened further.  It must explicitly supply

1. monotone linked physical central intervals realizing all middle labels;
2. nonempty common cores for every reflected lower target;
3. actual pin sets meeting every positive central and lower interval;
4. a sign-correct negative merge forest, or a direct verification of the
   pin inequalities, for every Boolean coordinate;
5. a count of every added physical factor position; and
6. a uniform version for unequal and degenerate four-chain boxes.

The proposed forest clause does not imply items 1--4.  Therefore the valid
new frontier is narrower than the original portal problem at the
upper-shadow level, but it is too strong to say that sublinear spine cutting
is the sole remaining obstruction to `nu(k)=(1+o(1))W(k)`.

## 9. Final ledger

| Claim | Verdict |
|---|---|
| Sparse two-step section | Pass; immediate iterate of known one-step section |
| Omitted strip equals alphabet growth | Pass |
| Three-band boundary coverage | Pass |
| Cross-`c` two-provider identity | Pass as an upper join |
| Alternating linked-band joins | Pass with domain/accounting qualifications |
| Three-provider identity | Pass as an upper join |
| Forest junctions imply pins | **Fail** |
| `q_R` shadow recurrence, conditional on exact recycling | Pass |
| Factor recurrence and coefficient-one consequence from the stated lemma | **Not proved** |

The proposal makes concrete progress on the upper-shadow superposition
problem.  It does not remove the independent central-factor, lower-core, or
pin-survival gates, and it establishes no new unconditional asymptotic bound.
