# Audit: canonical-frame contraction at the reciprocal-height scale

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Audited conclusion

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  Let \(\tau=\phi^2\) be the normalized
step-two PBBS map.  The theorem proved in
`MATH_ATTACK_HEIGHT_SATURATION_DIFFUSE_REFRAMING_20260725.md` is correct,
including its constants, floors, and little-oh quantifiers.

For a return interval \(I\), let \(s(I)\) be its step-two duration,
\(h(I)\) its invariant Dyck height, and \(R(I)\) the number of transitions
inside its step-two core at which the formally transported canonical first
deepest spine is no longer the canonical first deepest spine of the next
root.  For every fixed \(0<a<A\), every integer

\[
 1\le q\le \left\lfloor {\lceil a\sqrt m\rceil\over4}\right\rfloor,
\]

and every pairwise quotient-edge-disjoint nonwrapping family \(\mathcal P\)
of returns of duration at most \(H_A\), one has

\[
 \boxed{
 \#\left\{I\in\mathcal P:
   \lceil a\sqrt m\rceil\le h(I)\le\lfloor A\sqrt m\rfloor,
   \ R(I)\le\left\lfloor{s(I)\over4q}\right\rfloor
 \right\}
 \le C_{a,A}2^{-q}{B_m\over\sqrt m}.}
 \tag{0.1}
\]

Consequently every family satisfying \(R(I)=o(s(I))\) uniformly is

\[
 \boxed{o_{a,A}(B_m/\sqrt m)}                     \tag{0.2}
\]

on each fixed Gaussian height band.  Small heights have a uniformly
vanishing reciprocal-trace coefficient.  It follows that any family which
has positive critical mass \(\Theta(B_m/\sqrt m)\) must contain a positive
critical subfamily and a constant \(\varepsilon>0\) for which

\[
 \boxed{R(I)>\varepsilon s(I).}                  \tag{0.3}
\]

This is an actual vanishing improvement over critical height-stratum
saturation.  It applies to every winding.  It does not prove the full
packing gate: the exact residual is the linearly reframing class (0.3).
No implication from \(d(D)=1\) to a return is used.

The rest of this note independently checks the proof.

## 1. Exact finite-horizon canonical-frame conditions

For a height-\(h\) root, write the canonical first-deepest-spine
decomposition

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1
      0B_{h-1}0\cdots0B_1\,0B_0.                 \tag{1.1}
\]

The exact block rotation is

\[
 \tau D=B_0\,1A_0\,1A_1\cdots1A_{h-1}\,0
              0B_{h-1}0\cdots0B_1.              \tag{1.2}
\]

As long as the displayed spine stays canonical, after \(j\) rounds the
formal arrays are

\[
 A_i^{[j]}=
 \begin{cases}
 B_{j-1-i},&i<j,\\
 A_{i-j},&i\ge j,
 \end{cases}
 \qquad
 B_i^{[j]}=
 \begin{cases}
 B_{i+j},&i+j<h,\\
 \varnothing,&i+j\ge h.
 \end{cases}                                     \tag{1.3}
\]

An earlier forest at depth \(i\) must have relative height at most
\(h-i-1\); a later forest may have relative height \(h-i\), because the
chosen deepest leaf is the first one.  Therefore an original \(A_k\),
which is at earlier depth \(k+j\), obeys through rounds \(0\le j\le q\)

\[
 \operatorname {ht}(A_k)
 \le \max\{h-k-q-1,0\}.                          \tag{1.4}
\]

The zero on the right is exact: if the forest reaches the last earlier
slot before round \(q\), it must be empty there.

An original \(B_k\) remains later through round \(k\), giving the old cap
\(h-k\), and thereafter appears earlier at depth \(j-1-k\), giving cap
\(h-j+k\).  The strongest cap through round \(q\) is thus

\[
 \operatorname {ht}(B_k)
 \le \min\{h-k,h-q+k\}
 =h-\max\{k,q-k\}.                               \tag{1.5}
\]

Conditions (1.4)--(1.5) are sufficient as well as necessary: they keep
every earlier forest strictly below global height \(h\), every later
forest at or below height \(h\), and the displayed spine itself at height
\(h\).  Hence they preserve both maximality and the first-deepest
tie-breaking rule at every displayed round.

Let \(C_j(z)\) count ordered forests of height at most \(j\), with
\(C_0=1\), and put

\[
 F_0=F_1=1,\qquad F_{j+1}=F_j-zF_{j-1},
 \qquad C_j={F_j\over F_{j+1}}.                  \tag{1.6}
\]

If \(c_{m,h}^{(q)}\) is the number of height-\(h\), \(q\)-stable roots,
independence of the spine forests gives the exact formula

\[
 c_{m,h}^{(q)}=[z^{m-h}]
 \prod_{k=0}^{h-1}
 C_{\max\{h-k-q-1,0\}}(z)
 C_{h-\max\{k,q-k\}}(z).                        \tag{1.7}
\]

Relax only the second cap to its original value \(h-k\).  Telescoping
(1.6) then gives the coefficientwise majorant

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(q)}z^m
 \preceq {z^h\over F_{h-q}(z)F_{h+1}(z)}.}       \tag{1.8}
\]

The indices in (1.8) are correct also at \(q=h-1,h\), with empty-product
conventions.  The later coefficient estimate uses only \(q\le h/2\).

## 2. The exact \(2^{-q}\) Gaussian loss

Define

\[
 A_j(x)={x^j\over F_j(x^2)},\qquad
 G_j(x)={x^j\over F_{j+1}(x^2)},                 \tag{2.1}
\]

and normalized coefficients

\[
 u_j(n)=2^{-n}[x^n]A_j(x),\qquad
 v_j(n)=2^{-n}[x^n]G_j(x).                       \tag{2.2}
\]

Finite-path diagonalization, with the short-time two-barrier reflection
bound, gives absolute \(c,C>0\) such that

\[
 \|u_j\|_1={1\over j+1},\qquad
 \|v_j\|_1={2\over j+2},                        \tag{2.3}
\]

and

\[
 u_j(n)\le {C\over(j+1)^3}e^{-cn/(j+1)^2},
 \qquad
 v_j(n)\le {C\over(j+2)^3}e^{-cn/(j+2)^2}.      \tag{2.4}
\]

The normalizations in (2.3) follow exactly from

\[
 F_j(1/4)={j+1\over2^j}.                         \tag{2.5}
\]

After \(z=x^2\), the right side of (1.8) becomes

\[
 {x^{2h}\over F_{h-q}(x^2)F_{h+1}(x^2)}
 =x^qA_{h-q}(x)G_h(x).                           \tag{2.6}
\]

Thus its \(x^{2m}\)-coefficient is exactly

\[
 2^{2m-q}(u_{h-q}*v_h)(2m-q).                   \tag{2.7}
\]

If \(a\sqrt m\le h\le A\sqrt m\) and \(q\le h/2\), both strip widths
are \(\Theta_{a,A}(\sqrt m)\).  In every convolution term one time is at
least \((2m-q)/2\).  Apply (2.4) to that factor and sum the other factor
with (2.3).  This proves

\[
 (u_{h-q}*v_h)(2m-q)\le C_{a,A}h^{-4},           \tag{2.8}
\]

and hence

\[
 \boxed{c_{m,h}^{(q)}
 \le C_{a,A}4^m2^{-q}h^{-4}.}                   \tag{2.9}
\]

Since

\[
 \sum_{h\ge a\sqrt m}h^{-4}=O_a(m^{-3/2}),
 \qquad B_m\asymp4^m m^{-3/2},                  \tag{2.10}
\]

we obtain the exact band estimate

\[
 \boxed{
 \sum_{\lceil a\sqrt m\rceil\le h\le\lfloor A\sqrt m\rfloor}
 c_{m,h}^{(q)}\le C_{a,A}2^{-q}B_m.}             \tag{2.11}
\]

The displacement factor \(2^{-q}\) in (2.9)--(2.11) is not hidden in an
implicit constant.

## 3. Edge-disjoint traces turn the root loss into packing loss

The step-two core of an interval \(I\) is

\[
 D_0(I),D_1(I),\ldots,D_{s(I)-1}(I).             \tag{3.1}
\]

There are exactly \(s-q\) possible windows of \(q\) successive core
transitions.  A frame-change transition lies in at most \(q\) such
windows.  Therefore the number of \(q\)-stable core roots is at least

\[
 s-q-qR(I).                                      \tag{3.2}
\]

The peak-deletion height-gap theorem gives \(s(I)\ge h(I)\), for every
winding.  Hence, under

\[
 q\le s(I)/4,\qquad R(I)\le s(I)/(4q),          \tag{3.3}
\]

(3.2) is at least

\[
 s(I)/2\ge h(I)/2\ge a\sqrt m/2.                \tag{3.4}
\]

Pairwise quotient-edge-disjointness makes all roots in (3.1), over all
selected intervals, globally distinct.  Counting the witnesses (3.4)
with (2.11) gives

\[
 {a\sqrt m\over2}|\mathcal P_{\rm slow}|
 \le C_{a,A}2^{-q}B_m,                           \tag{3.5}
\]

which is (0.1), after absorbing \(2/a\).  This is the essential joint
step: chronology and trace volume are coupled on the same actual core
roots.  No multiplication of unrelated marginal estimates occurs.

## 4. Floors, short quotient cycles, and the little-oh statement

Under the stated convention that the step-two core duration itself obeys
\(s(I)\le H_A\), use the integer definitions

\[
 h_-:=\lceil a\sqrt m\rceil,\qquad
 h_+:=\lfloor A\sqrt m\rfloor.                   \tag{4.1}
\]

\[
 1\le q\le\lfloor h_-/4\rfloor,\qquad
 R(I)\le\lfloor s(I)/(4q)\rfloor.               \tag{4.2}
\]

If instead one's residence convention includes the final odd edge and is
written \(s(I)+1\le H_A\), then and only then \(h_+\) in (4.1) is replaced
by \(\min\{\lfloor A\sqrt m\rfloor,H_A-1\}\).  If \(h_->h_+\), the
family is empty; otherwise the preceding proof is unchanged.  Quotient
cycles of length at most \(H_A+1\) contain at most

\[
 Z_{H_A}\le(2H_A+2)N^{2H_A+2}
 =\exp(O_A(\sqrt m\log m))                       \tag{4.3}
\]

roots.  Thus

\[
 Z_{H_A}=o_A(B_m/\sqrt m),                       \tag{4.4}
\]

so discarding them before applying the nonwrapping theorem costs nothing
at the corrected critical scale.

For the remaining small heights, if \(b_{m,h}\) is the exact height
spectrum, the path-graph estimate and a dyadic decomposition give a
function \(\eta(a)\downarrow0\) such that

\[
 \limsup_{m\to\infty}{\sqrt m\over B_m}
 \sum_{h<a\sqrt m}{b_{m,h}\over h+2}
 \le\eta(a).                                     \tag{4.5}
\]

Now let \(q_m\to\infty\), with \(q_m=o(\sqrt m)\).  If

\[
 R(I)\le s(I)/(4q_m),                            \tag{4.6}
\]

(0.1) gives \(o_{a,A}(B_m/\sqrt m)\).  Equivalently, for fixed
\(0<a<A\), choose \(q=\lfloor1/(8\varepsilon)\rfloor\).  Then

\[
 \limsup_{m\to\infty}{\sqrt m\over B_m}
 \#\{I:a\sqrt m\le h(I)\le A\sqrt m,
          R(I)\le\varepsilon s(I)\}
 \le C_{a,A}2^{-1/(8\varepsilon)+1},             \tag{4.7}
\]

which tends to zero as \(\varepsilon\downarrow0\).

Combining (4.5) and (4.7) proves the saturation contrapositive (0.3).
After the standard deck comparison, (0.2) is exactly

\[
 o_A(B_m\sqrt m)                                 \tag{4.8}
\]

in physical packing units, so the entire sublinearly reframing sector
meets the corrected linear-seam requirement.

## 5. Precise proved and unproved boundary

Proved:

1. the exact finite-horizon frame caps (1.4)--(1.5);
2. the exact forest product (1.7) and two-strip majorant (1.8);
3. the coefficient-correct \(2^{-q}\) contraction (2.9)--(2.11);
4. its conversion, on the same actual roots, to the packing estimate
   (0.1);
5. the negligible short-cycle term and the uniformly vanishing
   small-height trace; and
6. the corrected physical little-oh bound for every sublinearly
   reframing family, for all windings.

Unproved:

\[
 \boxed{
 \text{the bound }o_A(B_m/\sqrt m)
 \text{ for families with }R(I)\ge\varepsilon s(I).}
 \tag{5.1}
\]

A one-time frame change is not marginally rare: a transported earlier
forest may genuinely become first deepest.  Therefore (5.1) requires a
compatibility theorem for a linear sequence of canonical reframings, not
another static-spine count.  No constant-one conclusion is asserted
without that theorem.
