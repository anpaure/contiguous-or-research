# All-radius selective triangular portal braid

## Theorem

Let

\[
\mathcal T_R=\{P_0\}\cup
\{E_{s,y}:1\le s\le R,\ 0\le y<s\},\qquad P_s=E_{s,0}.
\]

A target `(u,r,x)`, with `0<=u<r<=R` and `0<=x<r`, is represented by an
interval whose cells have extrema

```text
min s=u,  max s=r,  min y=0,  max y=x.
```

There is an explicit spanning word `W_R` representing every target and
satisfying

\[
 |W_{2t}|={7t^2+9t+2\over2},\qquad
 |W_{2t+1}|={7t^2+15t+4\over2}.
\]

Consequently

\[
 g_\triangle(R)\le {7\over8}R^2+O(R),\qquad
 \rho(R):=g_\triangle(R)-|\mathcal T_R|le {3\over8}R^2+O(R).
\]

## Typed invariant

Peak occurrences carry metadata type zero or one; both types have the same
cell value `P_s`.  A word is **braidable** when:

1. it spans `T_R` and has a selected witness for every target;
2. every selected witness contains a type-zero peak;
3. every selected height-zero witness contains a type-one peak as well;
4. every positive peak label has a type-one occurrence;
5. the word starts with

   ```text
   D_R=P_0^(0),P_1^(1),E_(2,1),E_(3,2),...,E_(R,R-1).
   ```

The bases are `W_0=[P_0^(0)]` and
`W_1=[P_0^(0),P_1^(1)]`.

## Selective lift

For a typed lower word define the letterwise lift

```text
P_0^(0)   -> P_1,
P_s^(0)   -> P_(s+1),
P_s^(1)   -> E_(s+1,1),
E_(s,y)   -> E_(s+1,y+1)       (y>0).
```

If a lower witness represents `(u,r,x)`, contains a type-zero peak, and also
a type-one peak when `x=0`, its lifted interval represents
`(u+1,r+1,x+1)`.  First coordinates all increase by one.  A type-zero peak
supplies height zero.  For positive old height, a highest nonpeak supplies
the new maximum; for old height zero, a type-one peak supplies height one.

## Recursion

Define

```text
B_R=E_(R,R-1),E_(R,R-2),...,E_(R,1),P_R,P_(R-1),...,P_0,
```

typing its peak block alternately by `s mod 2`, and put

```text
X_R=P_2^(1),P_4^(1),...,P_(2 floor(R/2))^(1).
```

Then

\[
 W_R=D_R\Vert B_R\Vert\sigma(W_{R-2})\Vert X_R.
\]

All peaks created by the lifted block are newly typed zero.

## Witnesses

The targets split exhaustively as follows.

1. `x=0`: use the consecutive peak interval `P_r,...,P_u` in `B_R`.
2. `r=R`, `x>0`: use `E_(R,x),...,P_R,...,P_u` in `B_R`.
3. `u=0`, `r<R`, `x>0`: start at `P_r` in `B_R`, pass through `P_0`, and
   stop at `E_(x+1,x)` in the initial lifted diagonal.
4. `u>=1`, `r<=R-1`, `x>=1`: lift the selected witness for
   `(u-1,r-1,x-1)`.

The outer scaffold supplies row `R` and all peaks.  Higher interior cells are
lifts of lower nonpeaks, and every height-one cell is the lift of a lower
type-one peak.  Odd scaffold peaks plus `X_R` restore a type-one occurrence
of every positive peak.  Hence braidability is preserved.

The exact recurrence is

\[
 n_R=n_{R-2}+3R+1+\lfloor R/2\rfloor.
\]

Solving it gives the displayed closed forms.

## Scope

This is an unconditional improvement for the triangular subproblem.  It is
not yet a four-box OR word: central-square intervals, reflected-meet
factorization, a linked interval band, coordinate pins, and uniform unequal
boxes remain open.  The independent audit and exhaustive verifier are
`ALL_RADIUS_TRIANGULAR_PORTAL_BRAID_AUDIT.md` and
`scratch/verify_all_radius_triangular_portal_braid.py`.
