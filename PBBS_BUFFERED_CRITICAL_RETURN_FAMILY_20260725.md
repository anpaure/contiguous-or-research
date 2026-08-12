# A buffered Catalan family of genuine critical PBBS returns

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or external input.

## 0. Result

The previously known critical atom used the filler \(F=(10)^M\).  The
alternation is unnecessary.  A linear terminal buffer permits an arbitrary
height-bounded Dyck core, while preserving the entire canonical PBBS
first-return chronology.

Let \(n\ge4\), let

\[
 1\le h\le n-2,
\]

and let \(F\) be any Dyck word of semilength \(M\) and height at most \(h\).
Put

\[
 \boxed{
 D(F)=1^{3n+1}0^n1^{2n-1}0^{4n-h}F0^h.}          \tag{0.1}
\]

Its semilength is

\[
 R=M+5n.
\]

### Theorem A

Every \(D(F)\) starts a genuine first zero-winding quotient return of
duration \(4n\).  Its endpoint half-overlap is

\[
 \lambda=n.
\]

Its first mountain pruning depth is exactly

\[
 p=n,
\]

and the stopping mountain is \(M_{3n}=1^{3n}0^{3n}\), so

\[
 q=3n,
 \qquad p<2q.
\]

Thus, when \(M\asymp n^2\), every member lies in the actual critical lane

\[
 p,q,\lambda\asymp\sqrt R.
\]

Moreover, if \(h=\lfloor\alpha n\rfloor\) and
\(M=\lfloor c n^2\rfloor\), for fixed \(0<\alpha<1\) and \(c>0\), then
the number of admissible fillers is at least

\[
 c_{\alpha,c}\operatorname{Cat}_M
\]

for a constant \(c_{\alpha,c}>0\).  Hence the critical atom is robust under
a Catalan-positive family of internal PBBS cores.

This is not a critical aggregate packing lower bound.  Since
\(R-M=5n=\Theta(\sqrt R)\), the family still has relative size

\[
 \frac{\operatorname{Cat}_M}{\operatorname{Cat}_R}
 =\exp[-\Theta(\sqrt R)].
\]

Its significance is narrower: actual first-maximum chronology does not
force the filler to be rigid or alternating.  Any strict critical theorem
must still use global cross-phase/fibre incidence, not uniqueness of the
local return word.

## 1. Exact quotient trace

Write \(D_j=\tau^jD(F)\).  The following four formulas hold.

For \(0\le j\le h\),

\[
 \boxed{
 D_j=1^{3n+1+j}0^n1^{2n-1-j}
       0^{4n-h+j}F0^{h-j}.}                       \tag{1.1}
\]

For \(h+1\le j\le n-1\),

\[
 \boxed{
 D_j=1^{j-h-1}F1^{3n+2+h}0^n
       1^{2n-1-j}0^{4n}.}                         \tag{1.2}
\]

For \(n-1\le j\le4n-1\), write \(k=j-(n-1)\).  Then

\[
 \boxed{
 D_j=1^{n-h-2+k}F1^{3n+2+h-k}
       0^{n+k}1^n0^{4n-k}.}                       \tag{1.3}
\]

Finally,

\[
 \boxed{
 D_{4n}=1^n0^n1^{4n-h-1}F1^{h+1}0^{4n}.}         \tag{1.4}
\]

### Lemma 1.1

Equations (1.1)--(1.4) are the canonical quotient orbit formulas; in
particular \(D_{j+1}=\tau D_j\) at every displayed step.

#### Proof

Use the exact first-maximum block rotation

\[
 X=P1R0S,
 \qquad \tau X=S1P0R.                             \tag{1.5}
\]

The condition \(\operatorname{ht}(F)\le h\) keeps every copy of \(F\)
strictly below the main height \(4n\):

* in (1.1), its base height is \(h-j\);
* in (1.2), its maximum height is at most
  \((j-h-1)+h=j-1<4n\);
* in (1.3), its maximum height is at most
  \((n-h-2+k)+h=n-2+k\le4n-2\);
* in (1.4), it starts at height \(4n-h-1\), so it stays below \(4n\).

Thus the marked first maximum is always the end of the displayed main
up-run, never a step inside \(F\).

In (1.1), one application of (1.5) moves one of the terminal \(h-j\)
down-steps to the down-run before \(F\), giving the next value of \(j\).
At \(j=h\), \(F\) is the suffix \(S\), so the next application moves it
to the front and gives (1.2).  Within (1.2), block rotation transfers one
up-step from the main post-\(F\) run to the prefix before \(F\).  At
\(j=n-1\), the factorization changes to (1.3); each further update transfers
one step through the two displayed middle runs.  At \(k=3n\), the first
return after the maximum occurs before the suffix \(1^n0^n\), and (1.5)
gives (1.4).  Direct exponents agree at both regime boundaries. \(\square\)

## 2. First-return audit

For a Dyck root \(X\), let \(\delta(X)\) be its canonical first-maximum
position and let \(d(X)=|S|+1\) in (1.5).  Put

\[
 C_j=\sum_{i<j}d(D_i).
\]

The orbit formulas give

\[
 d(D_j)=
 \begin{cases}
  2M+1,&j=h,\\
  2n+1,&j=4n-1,\\
  1,&\text{otherwise for }0\le j<4n.
 \end{cases}                                      \tag{2.1}
\]

Indeed, \(F\) is the suffix exactly at \(j=h\), and
\(1^n0^n\) is the suffix exactly at \(j=4n-1\).  Hence

\[
 C_j=
 \begin{cases}
  j,&0\le j\le h,\\
  2M+j,&h<j<4n,\\
  2M+6n,&j=4n.
 \end{cases}                                      \tag{2.2}
\]

The first-maximum positions are

\[
 \delta(D_j)=
 \begin{cases}
  6n,&0\le j\le h,\\
  2M+6n,&h<j<n-1,\\
  2M+4n,&n-1\le j<4n,\\
  2M+6n,&j=4n.
 \end{cases}                                      \tag{2.3}
\]

The formula at an empty second range is simply omitted.  Equations
(2.2)--(2.3) show

\[
 C_j<\delta(D_j)\quad(0<j<4n),
 \qquad C_{4n}=\delta(D_{4n})=2M+6n.              \tag{2.4}
\]

Since

\[
 2M+6n<2R+1=2M+10n+1,
\]

(2.4) is exactly the canonical first zero-winding return criterion.  This
proves the return assertion in Theorem A.

At the endpoints,

\[
 \delta(D_0)=6n,
 \qquad \delta(D_{4n})=2M+6n.
\]

Therefore the endpoint excess is

\[
 \Lambda=\delta(D_0)+\delta(D_{4n})-2R=2n,
\]

so \(\lambda=\Lambda/2=n\).

## 3. Exact first mountain depth

For \(j<n\), simultaneous peak deletion leaves both displayed macro peaks:
the first down-run has length \(n-j>0\), and the second main up-run has
length \(2n-1-j>0\).  Hence \(\partial^jD(F)\) is not a mountain.

The pruning depth of a plane tree equals its height.  Since
\(\operatorname{ht}(F)\le h<n\), one has \(\partial^nF=\varnothing\).
After \(n\) simultaneous peak deletions, the two adjacent surviving up-runs
merge, as do the two terminal down-runs, and give

\[
 \partial^nD(F)
 =1^{(3n+1-n)+(2n-1-n)}
  0^{(4n-h-n)+h}
 =1^{3n}0^{3n}.                                   \tag{3.1}
\]

Thus the first mountain depth is \(p=n\), with residual rank \(q=3n\).

## 4. Catalan-positive filler count

Let \(\mathcal D_M^{\le h}\) be the Dyck words of semilength \(M\) and
height at most \(h\).  Let \(A_h\) be the adjacency matrix of the path on
states \(0,1,\ldots,h\).  Then

\[
 |\mathcal D_M^{\le h}|=(A_h^{2M})_{0,0}.         \tag{4.1}
\]

The path eigenvalues are

\[
 2\cos\frac{k\pi}{h+2},\qquad1\le k\le h+1,
\]

and the squared first coordinate of the \(k\)-th normalized eigenvector is

\[
 \frac2{h+2}\sin^2\frac{k\pi}{h+2}.
\]

All eigenvalue contributions to (4.1) are nonnegative because the power is
even.  Keeping only \(k=1\) gives

\[
 |\mathcal D_M^{\le h}|
 \ge
 \frac2{h+2}\sin^2\!\frac{\pi}{h+2}
 \left(2\cos\frac{\pi}{h+2}\right)^{2M}.         \tag{4.2}
\]

Take \(h=\lfloor\alpha n\rfloor\) and
\(M=\lfloor c n^2\rfloor\).  The prefactor in (4.2) is
\(\Theta_{\alpha}(n^{-3})\), while

\[
 \left(2\cos\frac{\pi}{h+2}\right)^{2M}
 =4^M\exp\!\left(-\frac{\pi^2M}{(h+2)^2}+o(1)\right)
 =\Theta_{\alpha,c}(4^M).                         \tag{4.3}
\]

Since

\[
 \operatorname{Cat}_M=\Theta(4^M/M^{3/2})
 =\Theta_c(4^M/n^3),
\]

(4.2)--(4.3) prove

\[
 |\mathcal D_M^{\le h}|
 \ge c_{\alpha,c}\operatorname{Cat}_M.           \tag{4.4}
\]

Finally,

\[
 \frac{\operatorname{Cat}_M}{\operatorname{Cat}_{M+5n}}
 =4^{-5n}\left(1+\frac{5n}{M}\right)^{3/2}(1+o(1))
 =\exp[-\Theta(n)],                               \tag{4.5}
\]

which proves the stated limitation.

## 5. Implication boundary

The theorem supplies an exponentially large and internally Catalan family
of *actual*, not formal-envelope, critical returns.  It eliminates a
possible rigidity shortcut: the canonical first-maximum itinerary tolerates
arbitrary Brownian-scale Dyck complexity behind a linear height buffer.

It does not saturate the ambient critical coefficient.  Recovering the
missing factor \(4^{5n}\) would require independent PBBS-safe decorations
of the macro skeleton, or a fibrewise theorem showing that a Catalan-order
fraction of the full inverse envelope embeds into canonical chronology.
That is precisely the global realization statement absent from the formal
joint-saturation construction.

## 6. General two-hill form

The ratio \(q/p=3\) above is not special.  Let

\[
 p\ge3,
 \qquad s\ge2p-1,
 \qquad 1\le h\le p-2,
\]

and let \(F\) be a Dyck word of height at most \(h\).  Define

\[
 \boxed{
 D_{s,p,h}(F)
 =1^{s-p+1}0^p1^{2p-1}0^{s-h}F0^h.}             \tag{6.1}
\]

The same proof, with the replacements \(n\mapsto p\) and
\(4n\mapsto s\), gives a first zero-winding return of duration \(s\),
endpoint half-overlap \(p\), first mountain depth \(p\), and stopping
mountain

\[
 M_{s-p}=1^{s-p}0^{s-p}.                          \tag{6.2}
\]

For completeness, its four orbit regimes are

\[
 \tau^jD=
 1^{s-p+1+j}0^p1^{2p-1-j}0^{s-h+j}F0^{h-j},
 \quad0\le j\le h,                                \tag{6.3}
\]

\[
 \tau^jD=
 1^{j-h-1}F1^{s-p+2+h}0^p1^{2p-1-j}0^s,
 \quad h+1\le j\le p-1,                          \tag{6.4}
\]

and, for \(j=p-1+k\), \(0\le k\le s-p\),

\[
 \tau^jD=
 1^{p-h-2+k}F1^{s-p+2+h-k}
 0^{p+k}1^p0^{s-k}.                               \tag{6.5}
\]

The terminal state is

\[
 \tau^sD
 =1^p0^p1^{s-h-1}F1^{h+1}0^s.                 \tag{6.6}
\]

The only nontrivial suffix charges before time \(s\) occur at times
\(h\) and \(s-1\), with values \(2|F|+1\) and \(2p+1\).  Hence the
terminal cumulative displacement and terminal first-maximum position both
equal

\[
 2|F|+s+2p.                                       \tag{6.7}
\]

At the endpoints,

\[
 \delta(D)=s+2p,
 \qquad
 \delta(\tau^sD)=2|F|+s+2p.
\]

Since the semilength is \(|F|+s+p\), the endpoint excess is \(2p\), as
claimed.  The inequalities at every intermediate time are respectively

\[
 j<s+2p,
 \qquad 2|F|+j<2|F|+s+2p,
 \qquad 2|F|+j<2|F|+s,
\]

in the three nonterminal regimes, and are strict.

Thus buffered Catalan fillers occur throughout the genuine critical sector

\[
 p\asymp s-p\asymp\sqrt R
\]

whenever \(s/p\) stays in a compact subset of \([2,\infty)\).  The lower
endpoint \(s\ge2p-1\) is a feature of this two-hill template, not a general
PBBS restriction.

## 7. The buffered starts are exact sliding-defect exits

The canonical sliding-defect reduction isolates a positive-boundary exit by

\[
 d(D)=1,
 \qquad d(\phi\tau^sD)\ge3.
\]

Every buffered start (6.1) satisfies the stronger exact identity

\[
 \boxed{d(\phi\tau^sD)=2p+1.}                     \tag{7.1}
\]

Indeed, (6.6) is

\[
 \tau^sD
 =1^p0^p1^{s-h-1}F1^{h+1}0^s.
\]

Its first maximum \(s\) is reached on the last up-step before \(0^s\).
Thus in the factorization \(P1R0S\),

\[
 P=1^p0^p1^{s-h-1}F1^h,
 \qquad R=0^{s-1},
 \qquad S=\varnothing.
\]

Writing \(\overline W\) for reverse-complement, the one-step map gives

\[
 \begin{aligned}
 \phi\tau^sD
 &=\overline R,1\,\overline S,0\,\overline P\\
 &=1^s0^{h+1}\overline F0^{s-h-1}1^p0^p.          \tag{7.2}
 \end{aligned}
\]

The first run reaches height \(s\).  Since
\(\operatorname{ht}(\overline F)=\operatorname{ht}(F)\le h\), the middle
excursion never regains height \(s\), and the word first returns to zero
immediately before the terminal suffix \(1^p0^p\).  Hence that suffix is
the canonical \(S\)-sector of (7.2), proving (7.1).

Therefore the new exit-incidence residual is genuinely nonempty even after
all terminal-rotor reductions.  The buffered family supplies
\(c_{\alpha,c}\operatorname{Cat}_M\) actual exit roots inside its template,
although its ambient proportion remains \(\exp[-\Theta(\sqrt R)]\).
