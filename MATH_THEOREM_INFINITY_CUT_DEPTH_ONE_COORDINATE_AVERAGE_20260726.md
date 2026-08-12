# Infinity-cut forced holes: exact coordinate identities and obstruction

Date: 2026-07-26

## 0. Statement

Let \(m\ge2\), let \(\Omega\) have size \(2m+1\), and let \(F\) be an exact middle wreath
factor on \(\Omega\), and put

\[
 W=\binom{2m}{m},\qquad B={W\over m+1}.
\]

For \(x\in\Omega\), cut every wreath at \(x\).  Denote by
\(h_1^-(x)\) and \(h_1^+(x)\) the numbers of lower and upper depth-one
targets missed by the forced interior flags of the resulting \(B\) owner
paths.

For \(S\in\binom{\Omega}{m-1}\), let \(\mu(S)\) be the number of wreaths
of \(F\) in which \(S\) is a cyclic interval, and let

\[
 \mathcal H=\{S:\mu(S)=0\},\qquad Z=|\mathcal H|.
\]

If \(S\notin\mathcal H\), every occurrence of \(S\) has two exterior
neighbours in its cyclic order.  Let

\[
 C(S)=\bigcap_{\substack{C\in F\\S\text{ is an interval of }C}}
       \{\text{the two exterior neighbours of }S\text{ in }C\},
 \qquad \kappa(S)=|C(S)|.
\tag{0.1}
\]

Then \(0\le\kappa(S)\le2\), and the following identities hold.

\[
\boxed{h_1^+(x)=0\quad\text{for every }x\in\Omega.}
\tag{0.2}
\]

If

\[
 d_x=|\{S\in\mathcal H:x\in S\}|,
 \qquad
 c_x=|\{S\notin\mathcal H:x\in C(S)\}|,
\tag{0.3}
\]

then

\[
\boxed{h_1^-(x)=Z-d_x+c_x.}
\tag{0.4}
\]

Consequently,

\[
\boxed{
 \sum_{x\in\Omega}\bigl(h_1^-(x)+h_1^+(x)\bigr)
  =(m+2)Z+\sum_{S\notin\mathcal H}\kappa(S).
}
\tag{0.5}
\]

In particular,

\[
 (m+2)Z
 \le \sum_x h_1^-(x)
 \le (m+2)Z+2\binom{2m+1}{m-1},
\tag{0.6}
\]

and therefore some coordinate satisfies

\[
\boxed{
 h_1^-(x)+h_1^+(x)
 \le {m+2\over2m+1}Z
      +{2m\over(m+1)(m+2)}W.
}
\tag{0.7}
\]

For critical \(H\asymp\sqrt{m\log m}\), the second term in (0.7) is
\(o(W/H)\).  Thus the coordinate average proves the general shallow
necessary bound \(h_1^-(x)+h_1^+(x)=o(W/H)\) if

\[
 Z=o(W/H).
\tag{0.8}
\]

This does not by itself clear the sharper intact-path capacity
\(h_1^-(x)\le B\), nor any proper endpoint-queue Hall cut.  It cannot
prove even the general shallow bound from a merely unquantified
\(Z=o(W)\), or from an arbitrary exact factor.  Indeed, whenever
\(Z\ge cW\), (0.5) gives an
average of order \(W\), not \(W/H\).  More exactly, (0.4) shows that a
good coordinate in that regime would have to be a non-averaging
phenomenon: it must lie in all but \(o(W/H)\) of the odd holes, while
simultaneously satisfying \(c_x=o(W/H)\).

For the canonical MSW factor, whose audited odd depth-one hole bound is

\[
 Z\ge(1/16-o(1))\binom{2m+1}{m},
\tag{0.9}
\]

every threshold \(t_m=o(W)\) is exceeded by at least

\[
\boxed{(1/8-o(1))m}
\tag{0.10}
\]

coordinates.  This includes \(t_m=o(W/H)\).  Coordinate averaging cannot
select a successful canonical cut, although (0.10) still does not rule out
the remaining coordinates.

## 1. Which lower occurrences survive the cut

Fix an occurrence of \(S\in\binom{\Omega}{m-1}\) in a cyclic order
\(C\), and let \(e_C(S)\) be the pair of vertices immediately before and
after that interval.  There are \(m+2\) choices of \(x\notin S\).

Rotate the cyclic order so that it begins at \(x\), then delete \(x\).
As \(x\) ranges over the \(m+2\) vertices outside this fixed occurrence,
the occurrence has linear start positions \(0,1,\ldots,m+1\) relative to
the cut.  Formula (3.1) of the
global infinity-cut reduction says that precisely start positions
\(1,\ldots,m\) are forced lower interior flags.  The excluded positions
\(0\) and \(m+1\) occur exactly when \(x\) is the predecessor or the
successor of \(S\).  Hence

\[
 \boxed{
 S\text{ is supplied by this forced occurrence after cutting at }x
 \iff x\notin e_C(S).
 }
\tag{1.1}
\]

More explicitly, if \(b_x(S)\) is the number of occurrences whose
boundary pair contains \(x\), and \(\nu_x(S)\) is the forced lower load
after cutting at \(x\), then

\[
 \boxed{\nu_x(S)=\mu(S)-b_x(S),\qquad
        \sum_{x\notin S}b_x(S)=2\mu(S),\qquad
        \sum_{x\notin S}\nu_x(S)=m\mu(S).}
\tag{1.2}
\]

There is also an exact pair-collision average.  If \(e_\alpha(S)\) is the
boundary pair of occurrence \(\alpha\), then

\[
 \sum_{x\notin S}\binom{\nu_x(S)}2
 =\sum_{\{\alpha,\beta\}}
   \bigl(m+2-|e_\alpha(S)\cup e_\beta(S)|\bigr),
\tag{1.3}
\]

so this lies between
\((m-2)\binom{\mu(S)}2\) and
\(m\binom{\mu(S)}2\).  Thus coordinate deletion also preserves, up to a
constant factor, any large odd depth-one collision mass; averaging does
not dissipate it.

If \(S\) is an odd-factor hole, it remains a forced hole for every
\(x\notin S\).  If \(S\) is not a hole, it is missed after cutting at
\(x\) exactly when \(x\in e_C(S)\) for every occurrence \(C\), which is
exactly \(x\in C(S)\).  This proves (0.4).

Notice also that \(\kappa(S)\le2\).  If \(\mu(S)=1\), then
\(\kappa(S)=2\); with several occurrences it is the size of the common
intersection of their boundary pairs.

## 2. The upper side is automatically perfect

Fix \(x\in\Omega\) and
\(T\in\binom{\Omega\setminus\{x\}}{m+1}\).  Its complement
\(A=\Omega\setminus T\) is an \(m\)-set containing \(x\).  Exact middle
ownership gives a unique wreath \(C\in F\) in which \(A\) is an
\(m\)-interval.  Therefore \(T\) is the complementary
\((m+1)\)-interval of that same wreath, uniquely.

Because \(x\notin T\), after cutting at \(x\) this is one of the \(m\)
non-wrapping \((m+1)\)-intervals.  Formula (3.2) of the infinity-cut
reduction lists exactly those \(m\) intervals as forced upper interior
flags.  Thus every upper target occurs exactly once, proving (0.2).

## 3. Double counting

Every hole \(S\in\mathcal H\) avoids exactly \(m+2\) coordinates.  Every
nonhole \(S\) contributes to exactly \(\kappa(S)\) coordinatewise forced
hole counts.  Summing (0.4) over \(x\) proves (0.5), because

\[
 \sum_x d_x=(m-1)Z,
 \qquad
 \sum_x c_x=\sum_{S\notin\mathcal H}\kappa(S).
\tag{3.1}
\]

The upper bound in (0.6) follows from \(\kappa(S)\le2\).  Dividing by
\(2m+1\), and using

\[
 {2\over2m+1}\binom{2m+1}{m-1}
 ={2m\over(m+1)(m+2)}\binom{2m}{m},
\tag{3.2}
\]

gives (0.7).  If \(H\asymp\sqrt{m\log m}\), then

\[
 {W/m\over W/H}={H\over m}=o(1),
\tag{3.3}
\]

so the common-endpoint correction is negligible at the required scale.

## 4. Sharp meaning of the obstruction

The pointwise identity (0.4), rather than just its average, gives the
exact alternative.  If \(Z\) is not already \(o(W/H)\), then a good cut
must satisfy

\[
 d_x=Z-o(W/H),\qquad c_x=o(W/H).
\tag{4.1}
\]

Thus almost the entire odd hole family must be a star at the selected
coordinate.  No first-moment coordinate average can establish this
concentration; it is additional global structure of the factor.

For completeness, let

\[
 K_t=|\{x:h_1^-(x)+h_1^+(x)>t\}|,
 \qquad N_1=\binom{2m}{m-1}=mB.
\]

Since every coordinatewise hole count is at most \(N_1\), (0.5) implies

\[
 K_t\ge{(m+2)Z-(2m+1)t\over N_1-t}
\tag{4.2}
\]

whenever the numerator is positive.  Substituting (0.9),
\(\binom{2m+1}{m}=(2m+1)B\), and any \(t=o(W)\) proves (0.10).

## 5. Consequence for the global MSW lane

The signed depth-one infinity-cut gate is one-sided:

* the forced upper side is solved exactly for every factor and every cut;
* the forced lower side is governed by the odd first-shadow holes, up to
  a total coordinate-average correction \(O(W/m)\);
* coordinate averaging clears the general shallow necessary bound only
  from the stronger input \(Z=o(W/H)\);
* absent that input, success requires an almost-star hole family at one
  coordinate, a genuinely non-averaging construction property.

Thus a theorem clearing the general depth-one cut is not an upper-shadow
estimate.  It must either construct an odd factor with \(o(W/H)\) lower
first-shadow holes, or construct one whose much larger hole family is
almost entirely concentrated on a single coordinate while avoiding the
common-endpoint penalty.  The intact-path completion remains strictly
stronger.

## 6. All lower depths and the complementary upper identity

The preceding calculation has an exact all-depth extension.  Fix
\(1\le q<m\).  For
\(S\in\binom{\Omega}{m-q}\), let \(\mu_q(S)\) be its odd-factor interval
load, let

\[
 \mathcal H_q=\{S:\mu_q(S)=0\},\qquad Z_q=|\mathcal H_q|,
\tag{6.1}
\]

and put \(\mathcal H_0=\varnothing\), \(Z_0=0\), and \(d_{0,x}=0\), since
exact middle ownership has no depth-zero holes.
Let \(E_{C,q}(S)\) be the \(2q\)-set consisting of the \(q\) cyclic
vertices immediately before and the \(q\) vertices immediately after an
occurrence of \(S\) in \(C\).  Define

\[
 C_q(S)=\bigcap_{C:S\text{ interval in }C}E_{C,q}(S),
 \qquad \kappa_q(S)=|C_q(S)|\le2q,
\tag{6.2}
\]

and

\[
 d_{q,x}=|\{S\in\mathcal H_q:x\in S\}|,
 \qquad
 c_{q,x}=|\{S\notin\mathcal H_q:x\in C_q(S)\}|.
\tag{6.3}
\]

As \(x\) ranges over the \(m+q+1\) vertices outside a fixed occurrence,
its start relative to the cut ranges from \(0\) to \(m+q\).  Formula
(3.1) of the global reduction forces precisely starts \(q,\ldots,m\).
The other \(2q\) starts are exactly the choices
\(x\in E_{C,q}(S)\).  Therefore

\[
 \boxed{h_q^-(x)=Z_q-d_{q,x}+c_{q,x}.}
\tag{6.4}
\]

The upper side is complementary, with no boundary correction.  A target
\(T\in\binom{\Omega\setminus\{x\}}{m+q}\) has complement
\(A=\Omega\setminus T\) of size \(m+1-q\) and containing \(x\).  The
target \(T\) is a forced upper interior interval after cutting at \(x\)
if and only if \(A\) is an odd-factor interval: complementation takes one
cyclic interval to the other, and every \((m+q)\)-interval avoiding \(x\)
is one of the forced starts \(0,\ldots,m-q\) in (3.2).  Hence

\[
 \boxed{h_q^+(x)=d_{q-1,x}.}
\tag{6.5}
\]

For \(q=1\), this recovers \(h_1^+(x)=d_{0,x}=0\).  Summing (6.4)--(6.5)
over coordinates gives the exact signed-depth identity

\[
\boxed{
 \sum_x\bigl(h_q^-(x)+h_q^+(x)\bigr)
 =(m+q+1)Z_q+(m+1-q)Z_{q-1}
   +\sum_{S\notin\mathcal H_q}\kappa_q(S).
}
\tag{6.6}
\]

The last sum is at most

\[
 2q\binom{2m+1}{m-q}.
\tag{6.7}
\]

There is a particularly clean aggregate form.  For \(1\le H<m\), the
coefficient of every interior \(Z_r\), \(1\le r<H\), is

\[
 (m+r+1)+(m-r)=2m+1.
\]

Consequently

\[
\boxed{
 \sum_x\sum_{q=1}^{H}\bigl(h_q^-(x)+h_q^+(x)\bigr)
 =(2m+1)\sum_{r=1}^{H-1}Z_r+(m+H+1)Z_H
 +\sum_{q=1}^{H}\sum_{S\notin\mathcal H_q}\kappa_q(S).
}
\tag{6.8}
\]

Thus every odd hole at depth \(r<H\) contributes once for every deleted
coordinate across the adjacent signed depths: if the coordinate is
outside the hole it is a lower hole at depth \(r\), while if the
coordinate is inside it is an upper hole at depth \(r+1\).  Deletion
averaging cannot reduce aggregate odd-hole mass; it only moves that mass
between the two signs.

At critical \(H\asymp\sqrt{m\log m}\), the crude common-boundary average
over the whole band has order at most \(W\):

\[
 {1\over2m+1}\sum_{q\le H}2q\binom{2m+1}{m-q}=O(W).
\tag{6.9}
\]

The right side is asymptotic to \(W\) if the upper bounds
\(\kappa_q(S)=2q\) are saturated through the Gaussian core.  This is not
an \(o(W)\) error.  Hence the exact identities plus only the universal
bound \(\kappa_q(S)\le2q\) do not prove a simultaneous completion.  An
averaging proof additionally needs an actual small-common-boundary
estimate and sufficiently small aggregate \(Z_r\); alternatives are
strict endpoint-capacity slack or a non-averaging choice of coordinate.
The identities (6.6)--(6.8) isolate these requirements without any
MSW-specific input.
