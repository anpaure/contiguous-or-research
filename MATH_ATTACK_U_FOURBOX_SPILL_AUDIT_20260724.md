# Adversarial audit: four-box spill report

Date: 2026-07-24

Audited source: `MATH_ATTACK_U_FOURBOX_SPILL_REPORT_RAW_20260724.md`

## Verdict

The spill-completed portal theorem is substantively correct.  The displayed
`X`- and `Y`-spill maxima are literal maxima of intervals already present in
the unchanged portal word; all receiving labels and arm parameters are
legal; the selected `X`-spill family is injective; the leading constant
`5/96`, the selected-family total `3/8`, the four-orientation separation, and
the exact word length all survive.

Four qualifications or corrections are required.

1. The report omits the literal stored interval proving the symmetric
   `Y`-spill.  The interval exists and is supplied below, so this is a
   presentational repair rather than a failed claim.
2. The term `4 C_X(q)` counts a deliberately selected `X`-spill subfamily.
   It is not the exact cardinality of the union of both displayed spill
   families: the `X`- and `Y`-families overlap but are not identical.  The
   stated `3/8` is therefore an exact leading constant for the selected
   certified subfamily, and a lower bound on total coverage.
3. The arithmetic formulas for `D_q` are correct, but the interpretation as
   an exact forced duplication count silently fixes both literal portal
   blocks in the same direction.  Reversing one block permits a one-point
   hairpin.  With arbitrary block orientations, the corrected robust count
   is `D'_q` below.  It is still `q^3/6+O(q^2)`, so the scoped cubic
   obstruction survives.
4. The triangular unique-provider lemma is correct, but it does not by
   itself prove an `Omega(R)` repetition cost.  Likewise, the inserted-corner
   argument is a local incompatibility, not a global lower bound.  The final
   hybrid-atlas statement is one sufficient construction target, not a
   necessary or exact characterization of every continuation.

No claim in the audited report proves `CB4`,
`g_4=w_4+o(R^3)`, or a new contiguous-OR coefficient.

## 1. Base portal identity

Put `R=2m-1`, let `1<=q<=floor(m/3)`, and define

\[
 X_t(A,B)=(m-A-t,B+t,m-B-1,A),
\]

\[
 Y_t(A,B)=(m-A-1,B,m-B-t,A+t).
\]

For nonnegative legal `u,z`, direct coordinatewise maximization gives

\[
\boxed{
 \bigvee[X_u,\ldots,X_0,Y_0,\ldots,Y_z]
 =(m-A,B+u,m-B,A+z).}
\tag{1}
\]

This must be proved directly: `X_0` and `Y_0` are different points, so the
block is not literally an instance of a one-common-vertex portal lemma.
Equation (1) is the corrected identity already established in the first-wave
four-box audit.

## 2. `X`-spill window

Assume

\[
 A+B\le q-1,qquad
 1\le h\le\min(A,B),qquad
 1\le u\le q-1-B.
\]

The formal extension is correct:

\[
 \bigvee_{t=-h}^{u}X_t(A,B)
 =(m-A+h,B+u,m-B-1,A)
 =Z^X_{A,B;h,u}.
\tag{2}
\]

More importantly, this is a literal interval in the stored neighboring
block.  Put

\[
 (A',B')=(A-h,B+1),qquad u'=u-1,qquad z'=h.
\]

Equation (1) gives

\[
\boxed{
 \bigvee[
 X_{u-1}(A-h,B+1),\ldots,X_0,
 Y_0,\ldots,Y_h]
 =Z^X_{A,B;h,u}.}
\tag{3}
\]

All receiver inequalities are exact:

\[
 A-h\ge0,qquad
 A-h+B+1\le q-1,
\]

\[
 0\le u-1\le q-2-B=q-1-(B+1),
\]

and

\[
 0\le h\le q-1-(A-h),
\]

the last inequality following from `A<=q-1`.  The interval has

\[
 u+(h+1)=h+u+1
\]

letters.  Its target depth is `s=h+u`, as required for an interval of
rank-`R` letters.

Also

\[
 s=h+u\le B+(q-1-B)=q-1.
\tag{4}
\]

The target lies in `[0,m]^4`: `h<=A` gives `m-A+h<=m`,
`B+u<=q-1`, and the remaining bounds follow from `m>=3q`.

Finally,

\[
 (Z^X)_1-s=m-A-u\ge0,qquad
 (Z^X)_2-s=B-h\ge0.
\tag{5}
\]

Thus every selected `X`-spill has a complete coordinate-`{1,2}` line
witness and is disjoint from the previously counted doubly-missed family.

**Verdict:** valid.

## 3. `Y`-spill window

For

\[
 1\le v\le q-1-A,
\]

the formal identity is likewise correct:

\[
 \bigvee_{t=-h}^{v}Y_t(A,B)
 =(m-A-1,B,m-B+h,A+v)
 =Z^Y_{A,B;h,v}.
\tag{6}
\]

The audited source does not display the actual stored interval.  The missing
formula is

\[
\boxed{
 X_h(A+1,B-h),\ldots,X_0,
 Y_0,\ldots,Y_{v-1}(A+1,B-h).}
\tag{7}
\]

Indeed, use receiver

\[
 (A',B')=(A+1,B-h),qquad u'=h,qquad z'=v-1
\]

in (1).  Its maximum is exactly `Z^Y`, and it has `h+v+1` letters.
Legality is given by

\[
 B-h\ge0,qquad A+1+B-h\le q-1,
\]

\[
 0\le h\le q-1-(B-h),qquad
 0\le v-1\le q-2-A.
\]

Moreover,

\[
 h+v\le A+(q-1-A)=q-1,
\]

and

\[
 (Z^Y)_3-(h+v)=m-B-v\ge0,qquad
 (Z^Y)_4-(h+v)=A-h\ge0.
\]

Thus every `Y`-spill is easy in the complementary line direction.

**Verdict:** valid after inserting the omitted literal witness (7).

## 4. Injectivity and the exact `5/96` count

For `z=Z^X_{A,B;h,u}`, the parameters are recovered by

\[
 A=z_4,qquad B=m-1-z_3,qquad
 h=z_1-m+A,qquad u=z_2-B.
\tag{8}
\]

Hence the `X`-spill parametrization is injective.  Its exact parameter
count is

\[
 C_X(q)=
 \sum_{B=1}^{q-2}(q-1-B)
 \sum_{A=1}^{q-1-B}\min(A,B),
\tag{9}
\]

with the sum empty for `q<=2`.

Writing `q=2t` or `q=2t+1`, direct power-sum evaluation gives the exact
quasipolynomial

\[
\boxed{
 C_X(2t)=\frac{t(t-1)(5t^2-2t-1)}6
}
\tag{10}
\]

\[
\boxed{
 C_X(2t+1)=\frac{t^2(5t^2+3t-2)}6
}
\tag{11}
\]

Equivalently,

\[
 C_X(q)=
 \begin{cases}
 \dfrac{q(q-2)(5q^2-4q-4)}{96},&q\text{ even},\\[5pt]
 \dfrac{(q-1)^2(5q^2-4q-9)}{96},&q\text{ odd}.
 \end{cases}
\tag{12}
\]

In particular,

\[
\boxed{C_X(q)=\frac5{96}q^4-\frac7{48}q^3+O(q^2).}
\tag{13}
\]

The source's `5/96` leading constant is correct.

## 5. Which spill family is being counted

The four high/low orientations are disjoint.  For an `X`-spill the
designated low coordinates satisfy

\[
 B+u\le q-1,qquad A\le q-1,
\]

while the high coordinates are actually at least `m-q+1`.  The same is
true symmetrically for `Y`.  The source's weaker uniform bound

\[
 m-2q+1>q-1
\]

is safe, because

\[
 m-2q+1-(q-1)=m-3q+2\ge2.
\]

Thus the high position in each coordinate pair is recoverable from the
target, proving cross-orientation disjointness.

However, `X`- and `Y`-spills inside one orientation are not disjoint.  For
`q>=5`, for example,

\[
 Z^X_{3,1;1,2}
 =(m-2,3,m-2,3)
 =Z^Y_{1,3;1,2}.
\tag{14}
\]

They are not identical either.  For `q>=3`,

\[
 Z^Y_{1,1;1,1}=(m-2,1,m,2)
\tag{15}
\]

cannot be an `X`-spill, since every `X`-spill has third coordinate at most
`m-2`.

Consequently

\[
 T(q)=4\binom{q+3}{4}+4C_X(q)
\tag{16}
\]

is the exact size of the selected certified subfamily consisting of all
old hard targets and all `X`-spills in the four orientations.  It is a
lower bound on the total number of targets covered after including all
`Y`-spills; it is not the exact size of that larger union.

For completeness,

\[
 T(q)=
 \begin{cases}
 \dfrac{9q^4+10q^3+48q^2+32q}{24},&q\text{ even},\\[5pt]
 \dfrac{9q^4+10q^3+48q^2+38q-9}{24},&q\text{ odd}.
 \end{cases}
\tag{17}
\]

Therefore

\[
\boxed{T(q)=\frac38q^4+O(q^3).}
\tag{18}
\]

The comparison with the previous `q^4/6+O(q^3)` selected family is valid:
the certified leading volume increases by a factor `9/4` without changing
the word.

**Verdict:** valid when explicitly read as a selected-subfamily count;
unsupported if read as an exact census of both spill families.

## 6. Exact word length

For one label with `delta=A+B`, the portal block has

\[
 (q-B)+(q-A)=2q-\delta
\]

occurrences, and there are `delta+1` labels.  Thus all four orientations
contain

\[
 P_q=4\sum_{\delta=0}^{q-1}(\delta+1)(2q-\delta)
 =\frac{4q(q+1)(2q+1)}3
\tag{19}
\]

portal occurrences.

Within one orientation, `X`-letters and `Y`-letters are separately
injective.  A cross-type collision forces `u+v=1`, so only `(0,1)` and
`(1,0)` occur; each contributes `binom(q,2)` legal collisions.  Hence the
duplicate excess is exactly `q(q-1)` per orientation and `4q(q-1)` overall.
There are no cross-orientation collisions.

Appending every unused rank-`R` point once therefore gives

\[
\boxed{|W_{m,q}|=|L_{2m-1}|+4q(q-1).}
\tag{20}
\]

Also,

\[
 |L_{2m-1}|=\binom{2m+2}{3}-4\binom{m+1}{3},
\]

\[
 w_4(m,m,m,m)=\binom{2m+3}{3}-4\binom{m+2}{3},
\]

so

\[
\boxed{|L_{2m-1}|=w_4(m,m,m,m)-(m+1).}
\tag{21}
\]

The spill witnesses add no occurrence: they are intervals inside already
stored blocks.  Equations (20)--(21) are therefore unchanged and exact.

**Verdict:** valid.

## 7. Even/odd literal-portal obstruction

Fix `A+B=2r`.  Let `E(A,B)` use balanced baseline `(r,r)`, and let the
canonical odd seam `O(A,B+1)` use `(r,r+1)`.  On their shared `Y`-line put

\[
 p_j=(m-A-1,r,m-B-j,r+j).
\tag{22}
\]

The even ray is `p_0,p_1,...`; the odd ray is `p_1,p_2,...`.
For

\[
 0\le r\le\left\lfloor\frac{q-2}{2}\right\rfloor,
\]

take the legal depth-`q` targets

\[
 T_E=(m-A,2r,m-B,q-1),
\tag{23}
\]

with even parameters `(u,v)=(r,q-1-r)`, and

\[
 T_O=(m-A,2r+1,m-B-1,q-1),
\tag{24}
\]

with odd parameters `(u,v)=(r+1,q-2-r)`.  Both designated low coordinates
are below `q`, so both targets are doubly missed and already belong to the
swapped-baseline hard family.

Let

\[
 L=q-1-r.
\]

Their canonical forward witnesses share the tail `p_1,...,p_L`, but attach
different predecessors at `p_1`.  If both blocks are frozen in the same
direction, none of those `L` occurrences can be shared.  Since there are
`2r+1` choices of `(A,B)`, the source's formal count

\[
 D_q=\sum_{r=0}^{\lfloor(q-2)/2\rfloor}
 (2r+1)(q-1-r)
\tag{25}
\]

is exact under that additional same-direction convention.  Its arithmetic
evaluation is correct:

\[
 D_{2t}=\frac{t(8t^2-3t+1)}6,
\qquad
 D_{2t+1}=\frac{t(8t^2+3t+1)}6.
\tag{26}
\]

The report does not, however, justify freezing the two directions.  A
literal OR witness may be read in reverse.  Reversing one block lets the two
strings hairpin at the terminal point `p_L`; only `p_1,...,p_{L-1}` must be
duplicated.  At `q=2,r=0`, this shares the sole point `p_1`, directly
contradicting the unqualified charge `D_2=1`.

With arbitrary orientations, the robust literal-block count is therefore

\[
 D'_q=\sum_{r=0}^{\lfloor(q-2)/2\rfloor}
 (2r+1)(q-2-r),
\tag{27}
\]

namely

\[
\boxed{
 D'_{2t}=\frac{t(8t^2-9t+1)}6,
\qquad
 D'_{2t+1}=\frac{t(8t^2-3t+1)}6
}
\tag{28}
\]

It still satisfies

\[
\boxed{D'_q=\frac16q^3+O(q^2).}
\tag{29}
\]

Different selected seams use distinct shared `Y`-lines, so these corrected
tail requirements are disjoint.  Thus the qualitative cubic obstruction
survives for an architecture retaining all these literal balanced blocks.

If only target coverage is required, neither `D_q` nor `D'_q` is forced:
the targets (23)--(24) already have swapped-baseline witnesses.  This is not
an unrestricted lower bound or a hybrid-atlas obstruction.

The sentence asserting that an odd-seam inward prefix transfers to a
neighboring odd rectangle supplies no receiving label, parameter map,
stored interval, or legality range.  It is **unsupported as written** and
is not needed for (27)--(29).

## 8. Borrowed even rays and inserted corners

This local claim is repairable.  Let `A+B=2r`, take the canonical odd seam
`O(A,B+1)`, and put

\[
 E^+=E(A+1,B+1)
\]

with baseline `(r+1,r+1)`.  Let

\[
 C_1=(m-A,r,m-B-2,r+1),
\]

\[
 C_2=(m-A-1,r,m-B-1,r+1)
\]

be the two old odd corners.  For

\[
 1\le u\le q-1-r,qquad 0\le v\le q-2-r,
\]

the interval

\[
 X^+_{u-1},\ldots,X^+_0,C_1,C_2,
 Y^+_0,\ldots,Y^+_v
\tag{30}
\]

has maximum

\[
\boxed{(m-A,r+u,m-B-1,r+1+v),}
\tag{31}
\]

the intended odd-seam target.

But a direct `E^+` cross target has first-coordinate maximum `m-A-1`.
Every direct cross interval through the placement (30) contains `C_1`,
whose first coordinate is `m-A`; hence all such direct crosses in that
same placement are contaminated.

The necessary qualifications are:

- (30) requires `u>=1`; it does not supply the `u=0` edge;
- a reversed odd baseline has the symmetric qualification;
- this is only a local incompatibility in the stated placement.  It gives
  no global lower bound, since corners or rays may be duplicated, reversed,
  relocated, or rerouted.

**Verdict:** valid after adding the ranges and local scope.

## 9. Triangular-fold claim

In the triangular cell set, for `1<=x<=R-1`, the target

\[
 [0,x+1]\times[0,x]
\]

has the unique height-`x` provider

\[
\boxed{D_x=(x+1,x).}
\tag{32}
\]

Indeed, triangularity forces the first coordinate `s` of a height-`x` cell
to satisfy `s>x`, while containment in the target forces `s<=x+1`.
Therefore `s=x+1`.

Deleting every occurrence of `D_x` destroys that target.  This does not
establish an `Omega(R)` repetition cost or invalidate every
`o(R)`-repair-per-level recurrence:

- the `D_x` are compulsory distinct cell types already present in a lift;
- retaining or relocating one occurrence of each need not create repeats;
- another occurrence of the same `D_x` can support a rerouted interval;
- the audited fold scaffold is sufficient, not a proved necessary normal
  form.

The safe conclusion is only that one cannot erase the diagonal separators
from the canonical suffix fan while leaving its chosen suffix witnesses
unchanged.  Any relocation must reroute every affected suffix through an
occurrence of the same forced provider.

**Verdict:** unique-provider lemma valid; quantitative recurrence
obstruction unsupported outside that narrow deletion architecture.

## 10. Implication scope

A sufficient hybrid-atlas lemma must explicitly produce a rank-`R` word
which

1. retains every swapped-baseline portal block and its hard-family
   witnesses;
2. contains every base-layer point;
3. gives every remaining line-easy target through
   `q=floor(alpha m)`, `0<alpha<=1/3`, either an intact-line witness or a
   proved spill witness; and
4. has total length `|L_R|+o(m^3)`.

Then the hard and line-easy families exhaust the equal-box upper ranks
`R,...,R+q`, and

\[
 |L_R|+o(m^3)=w_4(m,m,m,m)+o(m^3).
\]

This still supplies none of:

- upper depths larger than `q`;
- lower ranks or the origin;
- an integral lower-factor/pinning construction;
- uniform extension to `delta R<=ell_i<=CR`.

It therefore does not imply `CB4`, an unrestricted
`g_4=w_4+o(R^3)` theorem, or a contiguous-OR coefficient.  The hybrid atlas
is one sufficient next construction target, not a proved necessary gate or
an exact localization of every possible continuation.

## 11. Final ledger

| Claim | Verdict |
|---|---|
| Base portal maximum (1) | **VALID** |
| `X` formal and stored spill identities | **VALID** |
| `Y` formal spill identity | **VALID** |
| Literal stored `Y` witness | **CORRECTED** by (7) |
| Receiver-label and arm legality | **VALID** |
| Spill depths at most `q-1` | **VALID** |
| Spill targets are line-easy and new relative to the hard family | **VALID** |
| `X` injectivity | **VALID** |
| `C_X(q)=5q^4/96+O(q^3)` | **VALID**, sharpened by (10)--(13) |
| Four high/low orientations are disjoint | **VALID** |
| `X` and `Y` spill families are disjoint | **FALSE**; not actually proved in the source |
| `4 binom(q+3,4)+4C_X(q)` | **VALID** as an exact selected-subfamily count and coverage lower bound |
| Same formula as exact total `X union Y` coverage | **UNSUPPORTED** |
| Exact word length `|L_R|+4q(q-1)` | **VALID** |
| Formal arithmetic formulas for `D_q` | **VALID** |
| `D_q` as exact forced count with arbitrary block orientations | **FALSE / CORRECTED** to `D'_q` |
| Cubic all-literal-balanced obstruction | **VALID** after the one-point correction and only in the stated architecture |
| Odd inward-prefix transfer sentence | **UNSUPPORTED AS WRITTEN** |
| Inserted-corner maximum identity | **VALID LOCALLY**, with `u>=1` and stated ranges |
| Inserted corners prove a global obstruction | **UNSUPPORTED** |
| Triangular `D_x` unique-provider lemma | **VALID** |
| Unique provider forces `Omega(R)` new repetitions | **UNSUPPORTED** |
| Hybrid atlas would finish the displayed equal-box upper band | **VALID** under the four explicit hypotheses above |
| Hybrid atlas implies `CB4` or coefficient one | **FALSE / NOT CLAIMED** |

The stable positive result is therefore the spill-completed reset-free
portal theorem with an exact selected-family leading constant `5/96` and
unchanged word length.  The stable negative result is only
architecture-specific: retaining all balanced literal portals costs cubic
repetition, with the orientation-robust exact local ledger `D'_q`, not the
unqualified `D_q` printed in the raw report.
