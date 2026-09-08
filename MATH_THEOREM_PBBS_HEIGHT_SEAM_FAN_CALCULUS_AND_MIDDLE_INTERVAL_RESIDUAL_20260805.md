# Exact PBBS height-seam fan calculus and the middle-interval residual family

**Date:** 2026-08-05  
**Method:** literal forward and reverse PBBS iterates of one mountain with a
unit tail; no search or computation  
**Status:** unconditional target-support classification for the forced
height-ladder edges.  The switched monotone height ladder repairs every
one-sided fan target, every terminal diagonal target, and the unique deep
left boundary target (except possibly at the top endpoint).  The remaining
two-sided targets form one explicit middle-interval family.  No path made
only from a positive PBBS prefix followed by the monotone height ladder can
realize that family.  Auxiliary/reflected rails remain to be analysed.

## 1. The mountain states

Put

\[
                         n=2r+1
\]

and index the ground set by `0,1,...,2r`.  For `1<=b<r`, let

\[
 A_b=0\,1^b0^b(10)^{r-b}
     =[1,b]\mathbin{\dot\cup}T_b,                       \tag{1.1}
\]

where

\[
 T_b=\{2b+1,2b+3,\ldots,2r-1\}.                        \tag{1.2}
\]

The corresponding physical owner is `U_b=[n]\setminus A_b`.  In the
height pentagon of height `h=b-1`, the forced selected old edge is

\[
                 U_{gA_b}\longrightarrow U_{A_b},       \tag{1.3}
\]

where `g=f^2` is the centered PBBS successor.  The monotone ladder switch
replaces its incoming shore by

\[
                         U_{A_{b-1}}\longrightarrow U_{A_b}. \tag{1.4}
\]

The next height switch, when present, continues with

\[
                         U_{A_b}\longrightarrow U_{A_{b+1}}. \tag{1.5}
\]

All set intersections below are complements of physical upper unions.

## 2. Exact forward iterates

### Lemma 2.1 (mountain peeling)

For `1<=t<=b`,

\[
 g^tA_b
   =[0,b-t]\mathbin{\dot\cup}[2b-t+2,2b]
      \mathbin{\dot\cup}T_b.                            \tag{2.1}
\]

Consequently, for `0<=q<=b`,

\[
 F_b(q):=\bigcap_{t=0}^{q}g^tA_b
       =[1,b-q]\mathbin{\dot\cup}T_b,                   \tag{2.2}
\]

where `[1,0]` is empty.

#### Proof

At `t=0`, the unmatched root zero is `0`, and the first maximum of
`1^b0^b(10)^(r-b)` is reached at coordinate `b`.  This gives (2.1) for
`t=1`.

Assume `1<=t<b` and (2.1).  Its unmatched root zero is

\[
                         \rho_t=2b-t+1.                  \tag{2.3}
\]

Cutting immediately after `rho_t` gives the Dyck word

\[
       1^{t-1}(10)^{r-b}1^{b-t+1}0^b.                   \tag{2.4}
\]

The initial part has height at most `t`, while the last up-run first
reaches the global height `b` at physical coordinate `b-t`.  Therefore

\[
 g(g^tA_b)=g^tA_b-\{b-t\}+\{2b-t+1\},                   \tag{2.5}
\]

which is (2.1) with `t+1`.  This proves (2.1) through `t=b`.

The coordinate `0` and the right-hand interval in (2.1) are absent from
`A_b`; the successive states delete `b,b-1,...,b-q+1` from its low block
and retain all of `T_b`.  Their intersection is (2.2). \(\square\)

The first two steps after this stable range will be needed at one endpoint.

### Lemma 2.2 (one final drop and then a stall)

Assume `b<r`.  Then

\[
 F_b(b+1)=T_{b+1},
 \qquad
 F_b(b+2)=T_{b+1}.                                     \tag{2.6}
\]

#### Proof

At `t=b`, (2.1) is

\[
 g^bA_b=\{0\}\cup[b+2,2b]\cup T_b.                    \tag{2.7}
\]

Its root is `b+1`, and the first maximum in

\[
 1^b0(10)^{r-b-1}1,0^b
\]

is reached at the first tail coordinate `2b+1`.  Hence the next state
deletes `2b+1`, so the running intersection becomes `T_(b+1)`.

The resulting state is

\[
 \{0\}\cup[b+1,2b]\cup T_{b+1}.                       \tag{2.8}
\]

Its root is `b`; after that root its normalized word begins with `1^b`, so
the next distinguished deletion is `2b`.  This coordinate was absent from
`A_b` and therefore from `T_(b+1)`.  The running intersection does not
change. \(\square\)

## 3. Exact reverse iterates in the stable range

### Lemma 3.1 (reverse peeling)

For `0<=t<=b-1`,

\[
 g^{-t}A_b=[t+1,b+t]\mathbin{\dot\cup}T_b.              \tag{3.1}
\]

Consequently,

\[
 R_b(v):=\bigcap_{t=0}^{v}g^{-t}A_b
       =[v+1,b]\mathbin{\dot\cup}T_b
       \qquad(0<=v<=b-1).                               \tag{3.2}
\]

At the next step,

\[
                         R_b(b)=T_b.                     \tag{3.3}
\]

#### Proof

For `1<=t<=b-1`, root the state on the right side of (3.1) at the zero
`t`.  Its normalized Dyck word is

\[
                         1^b0^{b-t}(10)^{r-b}0^t.        \tag{3.4}
\]

The first maximum is reached at physical coordinate `b+t`, before the
unit tail.  Thus `g` deletes `b+t` and inserts `t`, carrying the `t`-th
state of (3.1) to the `(t-1)`-st.  Since the first predecessor is the
literal state

\[
 g^{-1}A_b=A_b-\{1\}+\{b+1\},                           \tag{3.5}
\]

induction proves (3.1), and intersection gives (3.2).

For `t=b-1`, (3.4) has one primitive factor and maximum `b`.  The reverse
distinguished deletion is its initial up-step, physical coordinate `b`,
while the down-step following the rightmost maximum is the final tail zero
`2r`.  Therefore the next inverse state deletes `b`.  This is the last low
coordinate in (3.2), proving (3.3). \(\square\)

## 4. The complete correct-rank inverse fan at the forced edge

Take `u` further old edges on the incoming side of (1.3) and `v` old edges
on its outgoing side.  The physical owner interval is

\[
 U_{g^{u+1}A_b},\ldots,U_{gA_b},U_{A_b},
 U_{g^{-1}A_b},\ldots,U_{g^{-v}A_b},                    \tag{4.1}
\]

with `q=u+v+1` edges.  Its upper target has complementary core

\[
 C_b(u,v)=
 \left(\bigcap_{t=0}^{u+1}g^tA_b\right)
 \cap
 \left(\bigcap_{t=1}^{v}g^{-t}A_b\right).               \tag{4.2}
\]

### Theorem 4.1 (exact target triangle and endpoint)

The correct-rank pairs are exactly

\[
 \boxed{u,v\ge0,\quad u+v\le b-1}                       \tag{4.3}
\]

together with the one endpoint `(u,v)=(b,0)`.

For (4.3),

\[
 \boxed{
 C_b(u,v)=[v+1,b-u-1]\mathbin{\dot\cup}T_b,
 }
                                                               \tag{4.4}
\]

where the displayed interval is empty when `u+v=b-1`.  At the extra
endpoint,

\[
                         C_b(b,0)=T_{b+1}.                \tag{4.5}
\]

#### Proof

For `u<=b-1` and `v<=b-1`, intersect (2.2) and (3.2).  This gives (4.4).
Its rank is `r-u-v-1=r-q` exactly when `u+v<=b-1`.  If the inequality is
violated, the low interval has already vanished and the rank is too large.

Lemma 2.2 gives (4.5), whose rank is `r-b-1`, correct for `q=b+1`.
Adding one outgoing state to this endpoint does not change the core,
because `g^(-1)A_b` contains `T_(b+1)`.  Adding the next incoming state
also does not change the core by Lemma 2.2.  Once one Johnson step fails to
lower an intersection rank, later states can lower it by at most one per
step and can never recover the correct-rank deficit.  Finally, at `v=b`,
the newly deleted coordinate is `b`, but every core in (4.2) already lost
`b` on the mandatory positive edge `A_b--gA_b`; this is again a stall.
These observations exclude every remaining pair. \(\square\)

## 5. What the monotone height seams repair

The height-window identity is

\[
 \bigcap_{j=c}^{b}A_j=[1,c]\mathbin{\dot\cup}T_b
                     \qquad(1<=c<=b).                   \tag{5.1}
\]

Combining it with Lemma 2.1 gives the history identity

\[
 \boxed{
 A_b\cap\bigcap_{t=0}^{u}g^tA_{b-1}
       =\bigcap_{t=0}^{u+1}g^tA_b
 }
 \qquad(0<=u<=b-1).                                    \tag{5.2}
\]

Thus an isolated incoming height seam transports every old right context.
In the **simultaneous** monotone ladder, however, the next seam replaces
the old right context by `A_(b+1),A_(b+2),...`.  The following statements
are the exact support that survives this second replacement.

### Theorem 5.1 (one-sided, diagonal, and deep-end repair)

In the switched height ladder:

1. every target `C_b(u,0)` with `0<=u<=b-1` occurs on the equal-width path
   \[
   U_{g^uA_{b-1}},\ldots,U_{A_{b-1}},U_{A_b};            \tag{5.3}
   \]
2. every diagonal target with `u+v=b-1` equals `T_b` and is repaired by
   (5.3) with `u=b-1`;
3. if the next seam exists, the endpoint `C_b(b,0)=T_(b+1)` occurs on the
   equal-width path
   \[
   U_{g^{b-1}A_{b-1}},\ldots,U_{A_{b-1}},U_{A_b},U_{A_{b+1}}.
                                                               \tag{5.4}
   \]

For `b>=5`, all positive PBBS prefixes displayed in (5.3)--(5.4) are
untouched by the other height-pentagon support states, so these are literal
paths in the fully switched pentagon ladder, not merely in the forced-seam
projection.

#### Proof

Item 1 is (5.2).  Item 2 follows from (4.4).  For item 3,

\[
 F_{b-1}(b-1)\cap A_b\cap A_{b+1}
   =T_{b-1}\cap A_b\cap A_{b+1}=T_{b+1},                \tag{5.5}
\]

and both old and new paths have `b+2` owners.

For the last assertion, the component-height census says that, on the
component of `A_c` with `c>=4`, the only possible pentagon support states
are

\[
 Z_c^0,\ Z_c^2,\ Z_{c-1}^1=A_c,\ Z_{c+1}^3,\ Z_{c+1}^4. \tag{5.6}
\]

Every `g^tA_c`, `1<=t<=c`, contains both `0` and `2c+1`.  The state
`Z_c^0` omits `0`; `Z_c^2` omits `2c+1`; and `Z_(c+1)^3,Z_(c+1)^4` omit
`0`.  Hence no positive-prefix interior state is switched.  Apply this
with `c=b-1>=4`. \(\square\)

At the top height there is no `A_(b+1)` seam, so item 3 leaves at most one
top endpoint target.  The finitely many paths with `b<5` are a bounded
bottom exception.

## 6. The sharp middle-interval residual

The unrepaired members of (4.3) after the main-ladder repairs are

\[
 \boxed{
 \mathcal R_b=
 \left\{
 [v+1,b-u-1]\cup T_b:
 v\ge1,\ u\ge0,\ u+v\le b-2
 \right\}.}                                             \tag{6.1}
\]

Every member has a nonempty low interval which omits coordinate `1`.

There is a useful exact no-go for the natural monotone-seam class.  Take a
positive PBBS prefix ending at `A_c`, followed by an ascending height
window to `A_(c+ell)`.  Its core is

\[
 \left(\bigcap_{t=0}^{a}g^tA_c\right)
 \cap
 \left(\bigcap_{j=c}^{c+\ell}A_j\right)
   =[1,c-a]\cup T_{c+\ell}.                              \tag{6.2}
\]

The low part in (6.2) is either empty or contains `1`.  Therefore:

### Theorem 6.1 (main-ladder obstruction)

No target in `mathcal R_b` has a target-equal replacement on a path made
from one positive PBBS prefix followed only by monotone ascending height
seams.

This does not prove that `mathcal R_b` is an actual hole family.  Its
targets may have unaffected old occurrences or replacements on the four
auxiliary pentagon rails.  It proves exactly that the successful rigid-`E1`
strategy needs its analogue here: a reflected/residual seam which can
delete an initial low prefix while retaining the terminal tail.  The main
height ladder supplies only the opposite, prefix-anchored rail.

## 7. Consequence and remaining target

The forced selected height cuts are no longer an unstructured all-width
problem.  Their correct-rank inverse fan splits into:

* one-sided rays: repaired;
* terminal diagonals: repaired;
* one deep endpoint per height: repaired by the next height seam, except
  possibly once at the top;
* the explicit middle-interval family (6.1).

The next exact PBBS question is whether one of the auxiliary role families
`Z_h^2,Z_h^3,Z_h^4,Z_h^0`, chained through its inherited PBBS arcs, has
core

\[
                         [v+1,b-u-1]\cup T_b             \tag{7.1}
\]

at the same width.  A positive answer is the desired height-seam analogue
of the rigid `E_1` residual-seam theorem.  A negative answer must also rule
out unaffected alternate occurrences; (6.2) alone does not do so.

## 8. Dependencies

Used:

* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_AH_PENTAGON_COMPONENT_LOAD_AND_REGENERATION_20260805.md`;
* `MATH_THEOREM_PBBS_HEIGHT_PENTAGON_FORCED_Q1_AND_RIGHT_RAY_REGENERATION_20260805.md`;
* `MATH_THEOREM_PBBS_Q_FAN_SUPPORT_Q2_AND_GAUSSIAN_MULTIPLICITY_20260726.md`.

No arbitrary exterior, multiplicity, or probabilistic assumption is used.
