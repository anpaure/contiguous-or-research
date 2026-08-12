# Audit of the exact simplex-perimeter braid

## Verdict

**PASS after a minor degenerate-base repair.**

The recursive perimeter word is a permutation of the truncated simplex and
represents every stated `(min d,min a,max(d+a))` triple.  Its four-box image
is an exact-once word for the complete sector `z_2+z_3<=m` and covers every
advertised target with `c>=x`.

This is a valid partial upper-shadow theorem.  It is not a new factor theorem
and does not finish full upper sharing: the dual complementary-sector braid
is still unproved.  Moreover, the same sector result already follows from
fixed-`d` row words.  For every feasible `(ell,u,h)`, the row segment

\[
 (\ell,u),(\ell,u+1),\ldots,(\ell,h-\ell)
\]

has exactly the required extrema.  Thus the perimeter recursion is an
alternative exact-once ordering, not a stronger abstract target theorem; in
the four-box image these fixed rows are precisely the cross-diagonal lines.

## 1. Recursive simplex theorem

Let

\[
 D(P,N)=\{(d,a)\in\mathbb Z_{\ge0}^2:d\le P,\ d+a\le N\}.
\]

The strict interior

\[
 1\le d\le P-1,\qquad a\ge1,\qquad d+a\le N-1
\]

translates by `(-1,-1)` to

\[
 D(\min(P-2,N-3),N-3).
\]

Translation sends

\[
 (\min d,\min a,\max(d+a))
\]

to the same triple plus `(1,1,2)`, so the induction step is exact.

The top, right, bottom, and left perimeter order handles respectively

* `h=N`;
* `u=0`;
* `ell=0`; and
* `ell=P`.

Those conditions exhaust every target not lying in the translated strict
interior.  Every displayed interval has the claimed extrema.

### Degenerate repair

The recursion must explicitly stop whenever the strict interior is empty,
in particular when `N<3` or `P<2`.  Also `P=0` needs one copy of its single
vertical side, for example

\[
 (0,N),(0,N-1),\ldots,(0,0),
\]

rather than interpreting both the right and left side lists literally.
“Repeated corner descriptions are omitted” does not by itself remove all
duplicate side points when `P=0`.

With this repair, exhaustive construction and interval enumeration pass for
every `0<=P<=N<=12`.

The independent checker is
`scratch/audit_simplex_perimeter_braid.py`, SHA-256
`e81f40093298d9a72b68370ab0a8b731ebbf426e1c03b5ee7e222b3e15467624`.

## 2. Four-box image

For fixed `x`, put `P=m-x`, `N=m` and

\[
 \Phi_x(d,a)=(d+a,m-d-x,x,m-a).
\]

Every image point lies in `[0,m]^4` and has sum `2m`.  The images over all
`x` bijectively partition

\[
 M_m^- =\{z:|z|=2m,\ z_2+z_3\le m\}
\]

with inverse

\[
 x=z_3,\qquad d=m-z_2-z_3,\qquad a=m-z_4.
\]

Consequently

\[
 |M_m^-|=\sum_{j=0}^{m}(j+1)^2
 =\frac{(m+1)(m+2)(2m+3)}6
 =\frac12|M_m|+\frac{(m+1)^2}{2}.
\]

For `c>=x`, set

\[
 \ell=c-x,\qquad h=c+r.
\]

The simplex theorem supplies an interval with

\[
 \min d=c-x,\quad\min a=u,\quad\max(d+a)=c+r.
\]

Its image maximum is exactly

\[
 (c+r,m-c,x,m-u)=U_{c,u,r,x}.
\]

Thus the exact-once sector claim passes.
The same checker verifies the point bijection and every advertised target
through `m=10`.

### Relation to fixed rows and the cross-diagonal word

For every feasible triple, the fixed-`d` row

\[
 (d,u),(d,u+1),\ldots,(d,r+x),\qquad d=c-x,
\]

already has the required three extrema.  More abstractly, take `d=ell` and
end at `a=h-ell`.  Conversely, every interval triple satisfies the stated
feasibility inequalities, so the fixed rows and the recursive perimeter word
guarantee exactly the same target set.  Under `Phi_x` the displayed row is
the cross-diagonal line from `CROSS_DIAGONAL_CENTRAL_LINE_AUDIT.md`.

## 3. Complementary dual sector

The map

\[
 \Psi_c(d,a)=(a,m-c,c+d,m-d-a)
\]

bijectively parametrizes the complementary chamber

\[
 \{z:|z|=2m,\ z_2+z_3\ge m\}
\]

with inverse

\[
 c=m-z_2,\qquad d=z_2+z_3-m,\qquad a=z_1.
\]

For an interval its maximum is

\[
 (\max a,m-c,c+\max d,m-\min(d+a)).
\]

Hence the remaining `c<x` target asks for

\[
 \max d=x-c,\qquad\max a=c+r,\qquad\min(d+a)=u.
\]

This dual formulation is correct.  No word meeting it at exact-once or
subquadratic excess is supplied.  The dual upper-shadow ordering is
therefore still a genuine missing theorem.

Exact-once duality is already impossible for `D(1,1)`.  Its three points are
`(0,0),(1,0),(0,1)`.  The dual targets

\[
 (1,0,0),\qquad(0,1,0),\qquad(1,1,1)
\]

force each of the three point-pairs to be a contiguous two-letter interval:
including the third point respectively raises `max a`, raises `max d`, or
lowers `min(d+a)`.  A linear permutation of three letters has only two
adjacent pairs.  Thus any dual theorem must permit repetitions; the proposed
`O(N)` excess remains a meaningful open target.

If a uniform dual word had excess `O(N^(2-epsilon))` for every slice, its
sum over `O(m)` values of `c` would be `O(m^(3-epsilon))`.  An `O(N)` slice
error would give `O(m^2)` total excess.  These implications are conditional.

## 4. Factor and pin scope

A literal sector word is already an actual max/OR word for its displayed
upper targets.  It contains only central-rank entries, however, so no
interval can represent a genuinely lower-rank target.

Taking the physical realization intervals to be singletons transfers upper
segments but makes every nontrivial common core empty.  The proposal
correctly identifies the additional requirements:

* linked physical central intervals;
* nonempty common cores for lower targets; and
* coordinatewise pin survival in both central and lower intervals.

Thus two independent gates remain: the complementary dual upper braid and
the lower/factor/pin realization.  The currently justified asymptotic upper
constant does not change.
