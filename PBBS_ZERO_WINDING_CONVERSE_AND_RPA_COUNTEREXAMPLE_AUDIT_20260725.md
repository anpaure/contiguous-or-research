# Audit of the proposed PBBS zero-winding converse and RP_A counterexample

Date: 2026-07-25

Method: pure symbolic PBBS/Dyck-word algebra.  No computation, finite
search, or external input is used.

Audited source:
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md`.

## 0. Verdict

The proposed converse and the resulting refutation of \((\mathrm{RP}_A)\)
are **false**.

There are two separate failures.

1.  Lemma 2.1's sector recurrences are false.  Under \(\tau\), a forest
    which was before the displayed deepest-spine child can become the forest
    after the new first deepest-spine child.  Thus the displayed transported
    spine need not remain the *first* deepest spine.

2.  This is not merely a defective proof of a true conclusion.  For every
    \(a,b\ge0\), the explicit primitive Dyck word

    \[
      D_{a,b}=11100\,(10)^a1100(10)^b\,0
    \]

    has height three and \(d(D_{a,b})=1\), but its omitted coordinate does
    not return at any positive time at most seven.  In particular it does
    not return at the asserted time
    \(2\operatorname{ht}(D_{a,b})+1=7\).

Consequently the following downstream claims in the audited source do not
follow and are in fact based on a false premise:

* the equivalence between zero winding and \(d(D)=1\);
* the assertion that every member of the primitive family
  \(\{1E0:\operatorname{ht}(E)\le H-2\}\) starts a short return;
* the Catalan-positive lower bound on short-return starts;
* the physical packing lower bound \(\Omega_A(B_r\sqrt r)\); and
* the claimed disproof of \((\mathrm{RP}_A)\).

The valid result remains one-way: an actual zero-winding return after
\(2s+1\) steps forces

\[
  s=\operatorname{ht}(D),\qquad d(D)=1.
\]

The converse is false.

## 1. The printed sector shift fails on the proposed test word

Take

\[
 D=101100.
\]

Its height is two.  Relative to its first deepest leaf, its sector data are

\[
 A_0=10,qquad A_1=B_1=B_0=\varnothing.
\]

The first maximum-reaching step is the fourth symbol, so

\[
 P=101,qquad R=0,qquad S=\varnothing.
\]

The exact two-step formula gives

\[
 \tau D=S1P0R=110100.
\]

In \(110100\), the first deepest leaf is reached at the second symbol.  Its
actual sectors are

\[
 A'_0=A'_1=B'_0=\varnothing,qquad B'_1=10.
\]

By contrast, formulas (2.1)--(2.2) of the audited source predict

\[
 A'_1=A_0=10,qquad B'_1=\varnothing.
\]

Thus those formulas interchange the side on which the forest \(10\)
actually lies.

The precise defect in the proof is the sentence asserting that the
displayed spine remains the first deepest spine.  An old \(A_i\)-forest is
moved one level farther from the root.  If its relative height is
\(h-i-1\), it now reaches global height \(h\) before the displayed spine.
That is exactly what happens here: the old root forest \(A_0=10\) is moved
from depth zero to depth one and supplies the new first deepest leaf.

The return conclusion happens to be true for this particular word.  Indeed,

\[
 D_0=101100,qquad D_1=110100,qquad D_2=110010,
\]

and

\[
 d(D_0)=d(D_1)=1,qquad \delta(D_2)=2.
\]

Hence \(1+1=2\), giving the gap-five zero-winding return.  This example
therefore refutes Lemma 2.1, but by itself does not refute Theorem 3.1.

## 2. An infinite counterfamily to Theorem 3.1

For integers \(a,b\ge0\), put

\[
 F_{a,b}=(10)^a1100(10)^b
\]

and

\[
 D_0=D_{a,b}=11100F_{a,b}0.
\]

Write

\[
 f=|F_{a,b}|=2a+2b+4,qquad
 r=a+b+5,qquad N=2r+1=2a+2b+11.
\]

### Proposition 2.1

Every \(D_{a,b}\) is a primitive Dyck word of semilength \(r\), has height
three, and satisfies \(d(D_{a,b})=1\).  Nevertheless its initial omitted
coordinate has no positive occurrence at any time at most seven.

### Proof

The prefix \(11100\) ends at height one.  The word \(F_{a,b}\) is Dyck of
height two, so, when read from height one, it stays positive and reaches
height three.  The final zero is the first return to height zero.  Thus
\(D_0\) is primitive of height three.  Its first maximum occurs at the
third symbol, and the distinguished maximum-height primitive component is
the whole word.  Hence the terminal suffix \(S_0\) is empty and

\[
 d(D_0)=|S_0|+1=1.
\]

The canonical first-maximum factorizations give the following exact
\(\tau\)-chain:

\[
 \begin{aligned}
 D_0&=11100F_{a,b}0,\\
 D_1=\tau D_0&=111000F_{a,b},\\
 D_2=\tau D_1&=F_{a,b}111000,\\
 D_3=\tau D_2&=1F_{a,b}11000.
 \end{aligned}
 \tag{2.1}
\]

Indeed:

* for \(D_0\), one has
  \(P_0=11\), \(R_0=00F_{a,b}\), and \(S_0=\varnothing\);
* for \(D_1\), the initial mountain \(111000\) is the first
  maximum-height primitive component, so
  \(P_1=11\), \(R_1=00\), and \(S_1=F_{a,b}\); and
* for \(D_2\), the prefix \(F_{a,b}\) has height only two, while the final
  mountain has height three, so
  \(P_2=F_{a,b}11\), \(R_2=00\), and
  \(S_2=\varnothing\).

Substitution in \(\tau D=S1P0R\) proves (2.1).  The three even-step
deficits are therefore

\[
 d(D_0)=1,qquad d(D_1)=f+1,qquad d(D_2)=1.
 \tag{2.2}
\]

Put \(C_j=\sum_{i<j}d(D_i)\).  Then

\[
 C_1=1,qquad C_2=f+2,qquad C_3=f+3.
 \tag{2.3}
\]

The first-maximum positions at the relevant endpoints are

\[
 \delta(D_0)=3,qquad
 \delta(D_1)=3,qquad
 \delta(D_2)=f+3.
 \tag{2.4}
\]

In \(D_3=1F_{a,b}11000\), the initial \((10)^a\) part of \(F_{a,b}\)
oscillates only between total heights one and two.  The second up-step in
the displayed \(1100\) is therefore the first step to total height three.
Consequently

\[
 \delta(D_3)=1+(2a+2)=2a+3.
 \tag{2.5}
\]

At the three possible positive odd endpoints the return differences are

\[
 \begin{aligned}
 C_1-\delta(D_1)&=-2,\\
 C_2-\delta(D_2)&=-1,\\
 C_3-\delta(D_3)&=2b+4.
 \end{aligned}
 \tag{2.6}
\]

All are nonzero modulo \(N\), since

\[
 0<2b+4<2a+2b+11=N.
\]

The gap-one endpoint also fails because
\(C_0-\delta(D_0)=-3\not\equiv0\pmod N\).  At the positive even
endpoints, a return would require \(C_j\equiv0\pmod N\).  But

\[
 0<C_1<C_2<C_3=f+3=2a+2b+7<N.
\]

Thus none of the times \(1,2,\ldots,7\) returns the initial omitted
coordinate.  In particular, time seven is not a return, although
\(d(D_0)=1\) and \(\operatorname{ht}(D_0)=3\).  This proves the
proposition. \(\square\)

The smallest member is

\[
 D_{0,0}=1110011000.
\]

Its chain is

\[
 1110011000\longmapsto1110001100
 \longmapsto1100111000\longmapsto1110011000,
\]

with deficits \((1,5,1)\).  Their sum is seven, while the terminal
first-maximum position is three; since the circumference is eleven, there
is no modular equality.

## 3. What remains valid

The exact two-step formulas

\[
 \tau D=S1P0R,qquad d(D)=|S|+1
\]

are unaffected.  So are the previously proved strict first-passage and
necessity statements: if a zero-winding return exists after \(2s+1\), then

\[
 s=\operatorname{ht}(D),\qquad d(D)=1.
\]

The correct implication is therefore

\[
 \boxed{
 \text{zero-winding return}
 \ \Longrightarrow\ 
 d(D)=1,}
\]

not an equivalence.

Lemma 4.1 of the audited source, which counts bounded-height primitive
Dyck paths, is a valid enumeration statement.  What fails is the preceding
claim that every such primitive path is a return start.  The counterfamily
above consists entirely of primitive paths and shows that primitivity is
not sufficient even at fixed height three.

Accordingly no positive-density statement for actual PBBS return starts is
established by Sections 4--5 of the audited source.  The lower bounds
\(R_H^{\rm long}=\Omega_A(B_r)\),
\(\overline\nu_H=\Omega_A(B_r/\sqrt r)\), and
\(\nu_H(P_r)=\Omega_A(B_r\sqrt r)\) must all be withdrawn.  The status of
\((\mathrm{RP}_A)\) returns to the pre-converse boundary: it is neither
proved nor refuted by this argument.

## 4. Exact repair to the sector statement

The word obtained by the printed sector transport is still a legitimate
height-\(h\) spine presentation, but it need not be the canonical
presentation using the *first* deepest leaf.  Re-canonicalization can move
whole forests from the displayed left side to the actual right side, as in
Section 1.

A one-step version of the printed recurrences is valid only under the
additional strict-clearance condition that no shifted old \(A_i\)-forest
reaches height \(h\); a sufficient form is

\[
 \operatorname{ht}(A_i)\le h-i-2
 \qquad(0\le i\le h-2).
\]

For an iterated statement this clearance must hold again after every
re-canonicalization.  The audited source assumes it automatically from the
first-deepest convention, but that convention gives only
\(\operatorname{ht}(A_i)\le h-i-1\); equality is allowed and is exactly
the missing case.  No unconditional converse follows from the repaired
conditional sector shift.
