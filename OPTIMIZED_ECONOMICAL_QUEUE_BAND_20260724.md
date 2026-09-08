# Optimizing the economical queue-band parameters

Date: 2026-07-24

## 1. Quantitative improvement

The economical queue-cover theorem is usually stated with

\[
 H=\lfloor\sqrt{\log m}\rfloor.
\]

That convenient choice proves exact coverage through every
(h=o(\sqrt{\log m})), but it is not quantitatively optimal.  Choosing the
number of linked starts as a function of (h) improves the relative word
excess from roughly (h/\sqrt{\log m}) to

\[
 \boxed{
 O\!\left(
 {h^2\over\log m}
 \log {\log m\over h^2}
 \right).}
 \tag{1.1}
\]

The depth class is unchanged: this is still an
(h=o(\sqrt{\log m})) theorem.  For

\[
 h={\sqrt{\log m}\over\omega(m)},\qquad\omega\to\infty,
\]

the error improves from (O(1/\omega+e^{-\Theta(\omega)})) to

\[
 \boxed{O(\log\omega/\omega^2).}                  \tag{1.2}
\]

No coefficient-one conclusion for the full Boolean cube follows.

## 2. Parameterized cover estimate

Put (L=\log m).  The audited economical-cover proof works for any integer
parameters satisfying

\[
 H+h=o(m),\qquad {h\over H}\to0,qquad
 K=H(2h+1)=o(L).
 \tag{2.1}
\]

It gives a literal nonzero word covering every rank (m-h,\ldots,m+h),
with zero missing masks, and length

\[
 |A_m|\le
 W\left[1+O\left(
 {2h+1\over H}
 +\exp\left{-(1-o(1)){L\over H(2h+1)}\right}
 \right)\right].                                  \tag{2.2}
\]

This is exactly the argument in
`ECONOMICAL_QUEUE_COVER_AUDIT_20260724.md`; only the final specialization
of (H) is being changed.

## 3. Optimized choice

Assume

\[
 1\le h=o(\sqrt L)
\]

and define

\[
 t={L\over h^2}\longrightarrow\infty,
 \qquad
 H=\left\lfloor{L\over(2h+1)\log t}\right\rfloor.
 \tag{3.1}
\]

The expression before the floor tends to infinity.  Moreover,

\[
 {H\over h}
 =(1+o(1)){t\over2\log t}\longrightarrow\infty,   \tag{3.2}
\]

and

\[
 K=H(2h+1)=(1+o(1)){L\over\log t}=o(L).            \tag{3.3}
\]

Since (H+h\le O(L)=o(m)), every hypothesis in (2.1) holds.

The physical reset ratio becomes

\[
 {2h+1\over H}
 =(1+o(1)){(2h+1)^2\log t\over L}
 =O\left({\log t\over t}\right).                 \tag{3.4}
\]

For the cover error,

\[
 {L\over H(2h+1)}=(1+o(1))\log t.                 \tag{3.5}
\]

The lower-order term hidden in the ABKV exponent is harmless here.  In the
underlying proof it is (O(\log L)/K); with (3.3) this is

\[
 O\left({\log L\log t\over L}\right)=o(1).
\]

Therefore

\[
 \exp\left\{-(1-o(1)){L\over H(2h+1)}\right\}
 =(1+o(1))t^{-1}
 =O\left({\log t\over t}\right),                 \tag{3.6}
\]

where the last estimate is valid for all sufficiently large (m).  Putting
(3.4)--(3.6) into (2.2) proves

\[
 \boxed{
 |A_m|\le W\left[1+
 O\left({\log t\over t}\right)
 \right],
 \qquad t={\log m\over h^2}.}
 \tag{3.7}
\]

Equation (1.1) is just (3.7) rewritten in terms of (h).

## 4. Explicit near-boundary specialization

If (h=\lfloor\sqrt L/\omega\rfloor), then

\[
 t=(1+o(1))\omega^2,
 \qquad
 H=(1+o(1)){\sqrt L\,\omega\over4\log\omega}.
\]

Thus (H/h\sim\omega^2/(4\log\omega)), the atom uniformity is

\[
 K=(1+o(1)){L\over2\log\omega},
\]

and (3.7) becomes

\[
 \boxed{
 |A_m|\le W\left(1+O\left({\log\omega\over\omega^2}\right)\right).}
 \tag{4.1}
\]

The improvement comes from balancing the reset cost against the ABKV cover
error.  Taking (H=\sqrt L) overpays for resets when (h) is close to the
black-box boundary.

## 5. Scope

This optimization does not move the intrinsic one-stage ceiling.  Conditions
(H/h\to\infty) and (Hh=o(L)) still imply (h^2=o(L)).  What changes is
the convergence rate inside that admissible depth class, which matters when
the central word is later combined with any prospective multiscale
extension.

It is also order-optimal inside the two-error estimate (2.2).  Ignoring
integer and lower-order terms, put

\[
 a={L\over K}.
\]

Then the reset and cover errors are

\[
 {4a\over t}+e^{-a}.
\]

Their derivative vanishes at (a=\log(t/4)), and the minimum is

\[
 {4\over t}\left(1+\log{t\over4}\right)
 =\Theta\left({\log t\over t}\right).
\]

Thus improving (3.7) by more than a constant factor requires a stronger
cover theorem or a different atom/reset architecture, not merely another
choice of (H).
