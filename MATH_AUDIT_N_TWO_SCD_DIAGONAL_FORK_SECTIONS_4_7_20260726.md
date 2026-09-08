# Audit of Sections 4 and 7 of the two-SCD diagonal-fork report

Date: 2026-07-26

Scope: pure mathematical audit of Sections 4 and 7 and their numerical
constants in
`MATH_OBSTRUCTION_N_TWO_SCD_DIAGONAL_FORK_AND_HALF_SPLICE_20260726.md`.

## 1. Verdict

The isolated-diagonal construction in Proposition 4.1 is correct as a
**local partial-map construction**, after replacing the nonquantitative
condition `m>3H+O(1)` by an exact sufficient condition.  It does not assert,
and does not prove, extension to two global SCDs.

The one-SCD collapse bound

\[
                         p_1\le 3a+c
\]

is correct in the forward-\(\rho\) path model, provided the meaning of the
constant-orbit term is made explicit.  The point-margin inequality and all
constants through the lower bound on \(a+c\) are correct.

The claimed collar lower bound (7.7)--(7.8) is **not unconditional**.  It
requires the additional architectural hypotheses that every \(1\to0\) cut
and every constant track remains a separate hard start, that no within- or
cross-orbit endpoint fusion is allowed, and that the standard hard-start
compiler's \(2H\) charge is being booked per such start.  The preceding
lemmas alone do not prove a lower bound of \(2H(a+c)\) for an arbitrary
literal realization.

## 2. Proposition 4.1: exact local realization

Fix \(H\ge3\), \(2\le q<H\), and a prescribed set \(Q\) of size \(2H\).
The construction can be made with the exact sufficient hypothesis

\[
                              m\ge 3H+1.
\]

Indeed choose disjoint coordinates

\[
 Q,\quad r,\quad a_1,\ldots,a_H
\]

and enough filler coordinates to make

\[
 L\supset Q\mathbin{\dot\cup}\{r\},\qquad |L|=m-H,
 \qquad X=L\mathbin{\dot\cup}\{a_1,\ldots,a_H\}.
\]

Choose distinct \(b_1,\ldots,b_H\notin X\), put

\[
 \alpha_i(v)=a_i,\quad \beta_i(v)=b_i,\quad
 a=a_1,\quad b=b_{q+1},\quad c=a_{q+1},
\]

use promotion slot \(\ell=q+1\), and choose the appended reserve
\(x=r\in L_H(v)\).  Then

\[
 T=X-\{a_1,\ldots,a_q\},\qquad
 T'=T-a_{q+1}+b_{q+1},
\]

and, with

\[
 C=\{a_2,\ldots,a_{q-1},r\},\qquad
 S=X-(\{a_1\}\mathbin{\dot\cup}C),
\]

one has \(|C|=q-1\),

\[
 X-S=C\mathbin{\dot\cup}\{a_1\},\qquad
 (X-a_1+b_{q+1})-S=C\mathbin{\dot\cup}\{b_{q+1}\}.
\]

The roots \(T,S,T'\) are pairwise distinct: \(T'\) is the only one
containing \(b_{q+1}\), while \(T\) and \(S\) differ by exchanging
\(a_q\) and \(r\).  Every displayed root and owner, and in fact both
depth-\(H\) lower roots of the displayed promotion, contains \(Q\), since
\(Q\subseteq L-\{r\}\).

The local owner assignments

\[
 \mu_0(T)=X=\mu_1(S),\qquad
 \mu_0(S)=X-a_1+b_{q+1}=\mu_1(T')
\]

are injective on their displayed domains and force locally
\(S=\rho T\), \(T'=\rho^2T\).  Direct substitution in the promotion
normal form proves (4.5)--(4.13), including

\[
 A_1(T')=A_0(T)-a_1+a_{q+1},
\]

\[
 B_1(T')=B_0(T)-b_q+a_1,
\]

and

\[
 U_q(w)=U_q(v)-b_q+b_{q+1},\qquad U_H(w)=U_H(v).
\]

Thus the local claim is sound.  If one insists that the two auxiliary
coordinates \(r,x\) be distinct, the proof as phrased has the exact
sufficient hypothesis \(m\ge3H+2\).  Taking \(x=r\) sharpens this to
\(m\ge3H+1\).  In either form, `m>3H+O(1)` should not appear in a theorem
whose constants and quantifiers are meant to be exact.

Nothing here supplies extensions of the two partial owner bijections to
global SCD owner maps, and nothing supplies the intermediate old
head-to-successor edge.  This is precisely the intended local scope.

## 3. The one-SCD collapse

On a mixed cyclic \(\rho\)-orbit, Proposition 2.1 forbids every forward
edge joining two consecutive zeros.  Under the weakened retained-run
hypothesis, every zero is therefore isolated.  The number of zeros equals
the number \(a_K\) of \(0\to1\) transitions on that orbit.

For each colour-one run with head \(h\), make a pure-colour-one cover by:

1. retaining the suffix strictly after \(h\), if it is nonempty;
2. adding the colour-one state at \(h\) as a singleton; and
3. adding the colour-one state at the unique preceding zero as a
   singleton.

The first item is at most one component, not necessarily one component
when the one-run has length one.  Hence the contribution is at most three
components per \(0\to1\) transition.  These pieces cover every root of a
mixed orbit exactly once in colour one.

For the term \(c\), one must use one of the following equivalent precise
conventions.

* Each constant orbit is required to have a one-component pure-colour-one
  forward track; or
* \(c\) denotes the number of components in an independently supplied
  pure-colour-one cover of all constant-orbit roots.

Under the original forward-track convention, no nontrivial all-zero
constant orbit can occur: after cutting a cycle once, any remaining
forward edge is forbidden by Proposition 2.1.  Thus a permissible
all-zero constant orbit is a \(\rho\)-fixed root and becomes one
colour-one singleton.  An all-one constant track is already a
colour-one track.  With this convention the stated \(c\) is valid and

\[
                              p_1\le3a+c
\]

follows.

If “constant track” is allowed to mean an arbitrarily reordered or
reverse-colour-zero path, its replacement by one colour-one path does not
follow, and the theorem needs the explicit pure-colour-one convention
above.

Because every lower root is now used once in \(\mathscr D_1\), the middle
owners are distinct, and the lower and upper depth-\(q_0\) native targets
are the complete ranks.  Therefore Theorem 6.2 of the partial-annulus
queue report applies exactly:

\[
 p_1\ge {1\over2q_0^2}
 \sum_x|2M_x(\Omega)-|\Omega||.
\]

Consequently

\[
 \sum_x|2M_x(\Omega)-|\Omega||
 \le2q_0^2(3a+c)\le6q_0^2(a+c).
\]

There is no missing factor of two in these inequalities.

## 4. BTK and scale constants

The audited BTK calculation proves the lower bound

\[
 \sum_x|2M_x(\Omega_{\rm BTK})-N_{q_0}|
 \ge\left({4\over\sqrt\pi}+o(1)\right)W.
\]

It does not, as presently written, prove asymptotic equality of this
\(\ell^1\) point skew.  Thus the phrase “\(\kappa=4/\sqrt\pi+o(1)\)” is
safe only when \(\kappa\) is explicitly an admissible lower-bound
coefficient; the displayed statement should retain `\(\ge\)`.

Combining this lower bound with the collapse gives

\[
 a+c\ge
 \left({2\over3\sqrt\pi}+o(1)\right){W\over q_0^2}.
\]

Since

\[
 q_0^2=(1+o(1))\sqrt m,qquad
 {H\over q_0^2}=(1+o(1))\sqrt{\log m},
\]

the numerical coefficient obtained after multiplying by a separate
\(2H\) hard-start charge is correctly

\[
 \left({4\over3\sqrt\pi}+o(1)\right)W\sqrt{\log m}.
\]

## 5. Exact scope of the collar statement

The last multiplication is not a consequence of the point-margin theorem
alone.  That theorem lower-bounds the number \(p_1\) of components in the
constructed **pure-\(\mathscr D_1\)** cover.  The relation
\(p_1\le3a+c\) then lower-bounds \(a+c\), but it does not lower-bound the
number of components in an arbitrary two-colour realization.

To infer a collar term \(2H(a+c)\), one must additionally assume:

1. every \(1\to0\) seam is left open;
2. every constant track is cut once;
3. endpoints from different \(\rho\)-orbits, and different open pieces
   of one orbit, are not subsequently fused by other legal connectors;
4. each resulting component is compiled separately by the standard
   hard-start construction, whose booked collar term is \(2H\).

Under these assumptions the architecture has exactly \(a+c\) separately
compiled starts, and (7.7)--(7.8) are correct statements about that
compiler.  If \(f\) legal endpoint fusions are admitted, the corresponding
component count can fall to \(a+c-f\), so the only immediate booked term
is \(2H(a+c-f)\).  With unrestricted fusion no positive lower bound follows
from \(a+c\) alone.

Moreover, Proposition 1.1 in the partial-annulus report establishes
\(s+2H\) as a sufficient hard-started realization length.  It is not a
universal lower bound on all literal OR realizations.  Accordingly,
“would pay at least” should be replaced by “the separate hard-start
implementation books” unless an independent collar-minimality theorem is
added.

