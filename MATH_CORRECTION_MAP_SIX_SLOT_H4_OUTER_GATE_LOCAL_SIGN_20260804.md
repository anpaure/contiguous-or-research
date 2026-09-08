# Correction map: six-slot `h=4` outer-gate local sign theorem

**Date:** 2026-08-04  
**Status:** exact two-row successor map responding to the independent
fail-closed audit.  No substantive gate constant, sign interval, endpoint
obstruction, or KKT branch has changed.

## 1. Lineage

| role | SHA-256 |
|---|---|
| failed predecessor theorem | `34057076744b82574ca5d93c87d29dea301c9b9a0edf9ee4232bc72e5b091315` |
| independent fail-closed audit | `5efa432687fbd7be14107ccdb1fded01ca6ec0db62db29ff681405d4f0742248` |
| corrected successor theorem | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |

The predecessor SHA is superseded and must not be cited as GO.

## 2. Exact correction 1: kernel derivative at zero

The predecessor displayed

\[
                         0<-K'(w)<3/10
 \qquad(0\le w\le A/2).
\]

Since `K'(0)=0`, the corrected successor displays

\[
 \boxed{0\le-K'(w)<3/10\qquad(0\le w\le A/2),}
\]

with strict positivity only for `0<w<=A/2`.  The proof text now uses the
weak comparison `arctanh(t)<=pi t/2`, with equality only at `t=0`.

## 3. Exact correction 2: diagonal displacement

The predecessor's single strict minimum bound gave `0<0` when `s=t`.
The corrected successor separates the two valid statements:

\[
 \boxed{
 F(s)-F(t)\le {3(t-s)\over10},
 \qquad
 F(s)-F(t)<{61\over1000}.}
\]

Equivalently, the minimum of the two upper bounds is weak, and the
displacement part is strict whenever `s<t`.

## 4. Downstream propagation

The active-envelope chain now ends with a weak displacement inequality;
the preceding Jacobi reflection comparison is strict, so (2.6) remains
strict.

In the inactive envelope, the moving loss is now stated to be **at most**
`D(delta)`, while the cap loss remains strictly below `eta`.  Again the
strict reflection comparison preserves the strict gate minorant.

The singleton and half-period estimates are unchanged: off the half-band
their displacement is nonzero, while at the half-band endpoint positivity
itself is strict.

The residual statement at `w=0` is also unchanged because

\[
 R_\tau(0)-T_\tau(0)
 =\sum_{q\ge2}(q-1)K'(q\tau)>0.
\]

Accordingly the certified interval

\[
 0\le\delta\le {43849\over643260},
\]

the two negative far-end bounds, continuity crossing, and the complete
residual KKT/subgradient list are byte-successor claims with exactly the
same constants.
