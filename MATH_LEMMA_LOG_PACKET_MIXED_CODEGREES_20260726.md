# Mixed codegrees for logarithmic pair-cube packets

Date: 2026-07-26

This note is purely mathematical.  It separates three operations which must
not be conflated:

1. a physical target is a face of a pair-cube packet;
2. a local directed cube factor actually traces that face;
3. an eligible trace is accepted as a mandatory target rather than sent to
   a labelled dump token.

The face census is exact.  Tracing and acceptance can only decrease the
target--target bounds below.  Owner--target ratios remain exact after full
symmetrization because every accepted target sees the whole owner packet.

## 1. Catalogue and notation

Let \(\Omega=[2m]\), let \(1\le H\le r\le m\), and put \(R=2^r\).  A
pair frame consists of a full core \(F\), an empty core \(G\), both of size
\(m-r\), and a perfect matching on the remaining \(2r\) points.  Its owner
packet is the set of the \(R\) middle sets which contain \(F\) and choose
one endpoint of each active pair.

A lower depth-\(q\) face has size \(m-q\): it contains \(F\), chooses one
endpoint on \(r-q\) active pairs, and chooses neither endpoint on the other
\(q\) pairs.  An upper depth-\(q\) face has size \(m+q\): it contains
\(F\), chooses one endpoint on \(r-q\) active pairs, and both endpoints on
the other \(q\) pairs.

Consider any indexed multiset \(\mathfrak C\) of augmented columns with the
following properties.

* It is invariant under the full permutation group of \(\Omega\).
* Every column lies over one pair frame and contains all \(R\) owners of
  that frame.
* Every mandatory signed depth-\(q\) target in a column is a physical
  depth-\(q\) face of that frame.  It must additionally be traced by the
  chosen local factor, and accepted targets in one signed part are distinct.
* The usual floor/ceiling mixture has been cleared to an integral indexed
  catalogue, so every owner and every mandatory physical target has one
  common degree \(D\).

The last normalization is precisely the hard-quota normalization: at signed
depth \(q\), a column accepts on average

\[
 R p_q,\qquad
 p_q={\binom{2m}{m-q}\over\binom{2m}{m}}.                \tag{1.1}
\]

All codegrees below count indexed columns, including their local-state and
marking indices.

## 2. Physical face degrees

The owner degree in the physical frame orbit is

\[
 D_r=\binom mr^2r!.                                      \tag{2.1}
\]

The number of physical frames in which a fixed lower depth-\(q\) target is
a face is

\[
 D^{\rm face}_{r,q}
 =\binom{m-q}{r-q}\binom{m+q}{r+q}
   {(r+q)!\over 2^q q!}.                                 \tag{2.2}
\]

Indeed, choose the full core inside the target.  The \(r-q\) remaining
target points are the selected endpoints of the fixed active pairs.  Choose
the \(r+q\) active points outside the target, pair \(r-q\) of them
bijectively with those fixed endpoints, and pair the remaining \(2q\)
points among themselves.  This gives

\[
 \binom{m-q}{r-q}\binom{m+q}{r+q}
 \binom{r+q}{r-q}(r-q)!{(2q)!\over2^q q!},
\]

which is (2.2).  Complementation gives the same degree for upper faces.
For \(q=0\), (2.2) reduces to (2.1).

## 3. Owner--owner and owner--target codegrees

If middle owners \(X,Y\) have Johnson distance \(d\), then

\[
 {d(X,Y)\over D}
 = {1\over\binom rd}
   \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2
 \quad(1\le d\le r),                                    \tag{3.1}
\]

and the codegree is zero for \(d>r\).  In particular,

\[
 \max_{X\ne Y}{d(X,Y)\over D}={r\over m^2}.             \tag{3.2}
\]

Now fix a lower target \(T\) of depth \(q\) and a middle owner \(X\), and
write \(j=|T\setminus X|\).  The number of middle sets in the ambient
relation class is

\[
 M^{OT}_{q,j}=\binom{m-q}{j}\binom{m+q}{q+j}.            \tag{3.3}
\]

In every frame in which \(T\) is a lower \(q\)-face, exactly

\[
 g^{OT}_{q,j}=2^q\binom{r-q}{j}                          \tag{3.4}
\]

packet owners have this relation to \(T\): choose freely on the \(q\)
missing pairs and reverse exactly \(j\) of the \(r-q\) fixed signs.
Double counting the pairs consisting of an accepted \(T\)-column and one
of its owners, and using coordinate transitivity, gives the exact augmented
ratio

\[
 \boxed{
 {d(T,X)\over D}
 ={2^q\binom{r-q}{j}\over
   \binom{m-q}{j}\binom{m+q}{q+j}}.}                    \tag{3.5}
\]

The same formula holds above the middle by complementation.  Consecutive
terms in \(j\) have ratio

\[
 {(r-q-j)(q+j+1)\over(m-q-j)(m-j)},                      \tag{3.6}
\]

so for \(r=o(m)\) the maximum is the incident case \(j=0\).  Moreover

\[
 {2^{q+1}/\binom{m+q+1}{q+1}\over
  2^q/\binom{m+q}{q}}
 ={2(q+1)\over m+q+1}<1.                                \tag{3.7}
\]

Consequently the maximum over all signed depths \(q\ge1\) is

\[
 \boxed{\max {d(T,X)\over D}={2\over m+1}.}              \tag{3.8}
\]

For comparison, before tracing and quota marking, the probability that a
uniform physical frame through a fixed \(X\) supports \(T\) as a lower
face is

\[
 {\binom{m-q-j}{r-q-j}\over\binom mr}
 {\binom{m-j}{r-j}\over\binom mr}
 {(q+j)_{\underline j}\over(r)_{\underline j}}
 ={(r)_{\underline{q+j}}\over(m)_{\underline{q+j}}}
  {(q+j)_{\underline j}\over(m)_{\underline j}}.        \tag{3.9}
\]

Thus physical packet containment, (3.9), is not the augmented mandatory
codegree, (3.5).  For example, in the incident depth-one case they are
respectively \(r/m\) and \(2/(m+1)\).

## 4. Same-sign target pairs

Let \(T\) be a lower depth-\(q\) target and \(S\) a lower depth-\(p\)
target.  Put

\[
 a=|T\setminus S|,\qquad b=|S\setminus T|=a+q-p.         \tag{4.1}
\]

The ambient relation shell about \(T\) has size

\[
 M^-_{q,p}(a)=\binom{m-q}{a}\binom{m+q}{b}.              \tag{4.2}
\]

The exact number of lower \(p\)-faces in one fixed pair frame having this
relation to a fixed lower \(q\)-face is

\[
 \boxed{
 f^-_{q,p}(a)
 =\sum_t
   \binom{r-q}{t}\binom q{t+q-p}2^{t+q-p}
   \binom{r-q-t}{a-t},}                                  \tag{4.3}
\]

where, as usual, an invalid binomial coefficient is zero.

To prove (4.3), encode a lower face by a missing-coordinate set and signs
on the other active coordinates.  If \(t\) formerly fixed coordinates
become missing, then \(s=t+q-p\) formerly missing coordinates become
fixed.  The latter have two possible signs.  If \(c=a-t\), reverse the
sign on exactly \(c\) of the coordinates fixed in both faces.  These
choices give (4.3), and every face is represented uniquely.

Full coordinate symmetrization therefore gives the exact physical-face
support ratio

\[
 {d_{\rm face}(T,S)\over D^{\rm face}_{r,q}}
 ={f^-_{q,p}(a)\over M^-_{q,p}(a)}.                      \tag{4.4}
\]

In the accepted catalogue, tracing and marking select only some of these
faces.  Every accepted \(T\)-column nevertheless contains at most
\(f^-_{q,p}(a)\) accepted \(S\)'s in this relation shell.  A second double
count consequently proves

\[
 \boxed{{d(T,S)\over D}\le {f^-_{q,p}(a)\over
 M^-_{q,p}(a)}.}                                        \tag{4.5}
\]

There is also a useful shell bound which avoids the sum.  Both faces share
the full core.  Hence the \(a\) deletions and \(b\) additions are confined
to the active \(2r\)-set, and

\[
 f^-_{q,p}(a)
 \le \binom{r-q}{a}\binom{r+q}{b}.                      \tag{4.6}
\]

If \(q,p\le r/4\) and \(m>2r\), (4.2), (4.5), and (4.6) imply

\[
 {d(T,S)\over D}
 \le \left({2r\over m-r}\right)^{a+b}.                 \tag{4.7}
\]

The exponent is at least \(|p-q|\), and for two distinct targets at the
same depth it is at least two.  The two adjacent nested shells, which are
the only one-power cases, are exact at the physical-face level:

\[
 {f^-_{q,q+1}(1)\over M^-_{q,q+1}(1)}
 ={r-q\over m-q},                                       \tag{4.8}
\]

and

\[
 {f^-_{q,q-1}(0)\over M^-_{q,q-1}(0)}
 ={2q\over m+q}.                                        \tag{4.9}
\]

Upper--upper pairs obey the same formulas by complementation.

## 5. Opposite-sign target pairs

Let \(T\) be lower at depth \(q\), let \(U\) be upper at depth \(p\),
and put \(a=|T\setminus U|\).  Then

\[
 |U\setminus T|=p+q+a,
\]

and the ambient shell has size

\[
 M^{-+}_{q,p}(a)
 =\binom{m-q}{a}\binom{m+q}{p+q+a}.                     \tag{5.1}
\]

In a fixed pair frame, let \(u\) be the number of active coordinates which
are missing from the lower face and doubled in the upper face.  The exact
number of compatible upper faces is

\[
 \boxed{
 f^{-+}_{q,p}(a)
 =\sum_u \binom qu\binom{r-q}{p-u}2^{q-u}
   \binom{r-q-p+u}{a}.}                                  \tag{5.2}
\]

Indeed, on each of the \(q-u\) lower-missing but not upper-doubled
coordinates the upper face has either sign.  A point of \(T\) fails to lie
in \(U\) only through a sign reversal on a coordinate which is fixed in
both faces; choosing the \(a\) reversals gives the last factor.

Exactly as in Section 4,

\[
 {d(T,U)\over D}\le {f^{-+}_{q,p}(a)\over M^{-+}_{q,p}(a)}. \tag{5.3}
\]

The difference sets lie in the active coordinates, so

\[
 f^{-+}_{q,p}(a)
 \le\binom{r-q}{a}\binom{r+q}{p+q+a}.                   \tag{5.4}
\]

Therefore, for \(q,p\le r/4\),

\[
 \boxed{
 {d(T,U)\over D}
 \le\left({2r\over m-r}\right)^{p+q+2a}.}              \tag{5.5}
\]

Every opposite-sign pair pays at least two powers of \(r/m\).  The
upper--lower case is obtained by complementation and interchanging the two
depths.

## 6. Acceptance marking and dump labels

Fix a local state and one signed part.  If it has \(n\) distinct eligible
faces and the marking is uniform over its \(a\)-subsets, then

\[
 \Pr(T\text{ accepted}\mid T\text{ eligible})={a\over n},\qquad
 \Pr(T,S\text{ accepted}\mid T,S\text{ eligible})
 ={(a)_{\underline2}\over(n)_{\underline2}}.            \tag{6.1}
\]

For different signed parts, independent marking gives the product of the
two one-point factors.  Thus the conditional second-target factors are
\((a-1)/(n-1)\) in the same part and \(a'/n'\) in a different part.
These factors never enlarge (4.5) or (5.3).

In the logarithmic pilot,

\[
 r=\alpha\log_2m+O(1),\quad 0<\alpha<1,\qquad H\le r/4,
\]

and

\[
 p_q=\prod_{i=0}^{q-1}{m-i\over m+i+1}
 =1-{q^2\over m}+O\left({q^3+q^4\over m^2}\right).     \tag{6.2}
\]

Hence the marking factors are \(1-o(1)\), not a source of additional
codegree decay.  More sharply,

\[
 R(1-p_q)=O(m^{\alpha-1}\log^2m)=o(1),                  \tag{6.3}
\]

so the floor/ceiling quota is \(R-1\) or \(R\).  A nonempty regular
catalogue must therefore contain local states with \(R\) distinct traces
at every depth assigned quota \(R\).  The marking layer cannot repair a
repeated physical trace.

This requirement is simultaneous, not merely depthwise.  In any balanced
catalogue the mean total number of dumped occurrences in a column is

\[
 2R\sum_{q\le H}(1-p_q)
 =O\left({RH^3\over m}\right)=o(1).                      \tag{6.3a}
\]

Since this number is a nonnegative integer, all but an \(o(1)\) fraction
of the indexed columns have no dump at any signed depth.  Those columns
must have \(R\) distinct lower traces and \(R\) distinct upper traces
simultaneously for every \(q\le H\).  Thus an almost-everywhere exact
multidepth-rainbow local catalogue is a logically prior gate to any global
nibble in this logarithmic regime.

For completeness, add labelled dump tokens.  Let a signed part contain
\(Z_q=W-N_q\) dump labels and let a column use \(s_q=R-a_q\) of them.
Under full uniform injection of dumped occurrences into labels and the
balanced floor/ceiling mixture, mass transport gives

\[
 {d(z,X)\over D}={R\over W}                              \tag{6.4}
\]

for every dump token \(z\) and owner \(X\).  A dump--target codegree is at
most \(R/N_p=(1+o(1))R/W\).  For two dump tokens in one part it is at most

\[
 {s_q^{\max}-1\over Z_q-1},                              \tag{6.5}
\]

and for two independently symmetrized parts it is \(O(R/W)\).  In the
pilot (6.3) gives \(s_q^{\max}=1\), so the same-part dump--dump codegree is
zero.  All dump ratios are exponentially smaller than the physical mixed
ratios above.

## 7. The pilot codegree scale

The full lifted edge size is

\[
 K_{\rm full}=R(1+2H),                                   \tag{7.1}
\]

and, by (6.3), the mandatory projection satisfies

\[
 R(1+2H)-2H\le K_{\rm mand}\le R(1+2H).
\]

Equations (3.2), (3.8), (4.7)--(4.9),
(5.5), and (6.4)--(6.5) show

\[
 {\Delta_2\over D}
 \le (1+o(1)){r\over m}.                                \tag{7.2}
\]

The only first-order candidate is the same-sign, adjacent-depth nested
shell (4.8).  Owner--target codegrees are \(O(1/m)\), owner--owner
codegrees are \(O(r/m^2)\), and same-depth, nonnested cross-depth, and
opposite-sign target pairs are \(O(r^2/m^2)\) or smaller.

Consequently

\[
 \boxed{
 K_{\rm full}{\Delta_2\over D}
 =O\left({2^rHr\over m}\right)
 =O\left(m^{\alpha-1}\log^2m\right)=o(1).}              \tag{7.3}
\]

Thus the logarithmic pilot clears the natural growing-edge condition
\(K\Delta_2/D=o(1)\).  It does not by itself prove a matching theorem.
In particular, a theorem whose error requires \(K^2\Delta_2/D=o(1)\)
would only be certified by this census in the smaller range
\(\alpha<1/2\), up to logarithmic factors.  The other independent gate is
the existence of the simultaneous trace-injective local states forced by
(6.3).

## 8. Global packet survival is not hereditary link survival

There is one further distinction relevant to a multiround nibble.  Retain
owners independently with probability \(\varepsilon=m^{-\beta}\), where
\(\beta>0\) is fixed, and condition on retaining one owner \(X\).  There
are exactly \(D_r\) physical packet frames through \(X\).  A frame survives
only if its other \(R-1\) owners survive, so

\[
 \mathbb E[\#\{\text{surviving physical frames through }X\}\mid X]
 =D_r\varepsilon^{R-1}.                                  \tag{8.1}
\]

Here

\[
 \log D_r=O(r\log m)=O(\log^2m),
\]

whereas

\[
 -(R-1)\log\varepsilon
 =\Theta(m^\alpha\log m).
\]

Thus (8.1) is \(o(1)\), and Markov's inequality shows that a typical
retained owner has no surviving physical packet at all.  Adding local
factor states cannot create a column over a physical frame whose owners
did not survive.

On the other hand, the total number of physical frames is \(WD_r/R\), and

\[
 \log W=\Theta(m)\gg R\log m
\]

for \(\alpha<1\).  Hence the expected total number of surviving packets
can still be exponentially large.  The assertion that random residuals
retain many packets is therefore true globally but false as a hereditary
per-owner regeneration statement.  Any multiround argument must preserve
correlated packet links; (7.3) alone does not supply that invariant.
