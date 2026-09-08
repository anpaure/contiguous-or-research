# Gate B: the exact `j=2` six-vertex rooted-core determinant

**Date:** 2026-08-22

**Status.**  This note closes the canonical finite rooted-core calculation
at the first harmonic depth.  In the punctured boundary graph, retain every
inclusion--exclusion blocker set with at most six incident cuts for which
every connected component contains one of the two event roots.  Two
puncture-side row differences of its middle/lower profile form a matrix
`M_r`.  For every `r>=23`,

\[
 \boxed{\det M_r={P(r)\over12Q(r)^2}>0,qquad
        \det M_r={4\over3}r^{-6}+O(r^{-7}),}                 \tag{0.1}
\]

with the explicit polynomial and denominator below.  In particular,

\[
                         \boxed{\det M_r\ge2^{-187}r^{-6}.} \tag{0.2}
\]

This is stronger than the sixteen-atom determinant at `j=2`.  It still
does **not** prove the fully dressed zero-avoidance determinant: components
which contain neither event root must be resummed, not inserted by a Weyl
bound.  The exact shore-difference theorem confines their fixed-depth
transverse current by one additional power of `r`, but their first common-
shore correction can alter the coefficient in (0.1).

## 1. The rooted six-vertex bank

Put

\[
 b=2r+1,
 \qquad B_r=\operatorname {Cay}(\mathbb Z_b,
              \{\mathord\pm1,\mathord\pm3\}),
 \qquad p=0,\ q=5,                                          \tag{1.1}
\]

and `D_M=2r r!(r+1)!`.  A blocker is an edge of `B_r`, tagged by
whether its original interval has length `r` or `r-1`.  At boundary-event
shift `t`, delete the two edges corresponding to the omitted start-zero
middle and lower intervals.

A blocker set `J` is **rooted** when

1. `{p,q}` is contained in its incident vertex set `V(J)`; and
2. every connected component of `J` contains `p` or `q`.

Let `L^(6)_(s,2)(t)` be the signed inclusion--exclusion profile obtained by
summing `(-1)^|J|` over all retained rooted `J` with `|V(J)|<=6`, on root
shore `s in {r,r-1}`.  Equivalently, restore the two punctures and let
`C^(6)_(s,2)(t)` be the sum of precisely those rooted terms using at least
one restored edge.  Translation invariance of the complete bank gives

\[
 L^{(6)}_{s,2}(u)-L^{(6)}_{s,2}(t)
 =C^{(6)}_{s,2}(t)-C^{(6)}_{s,2}(u).                         \tag{1.2}
\]

Define the normalized shore vectors

\[
 A_s={C^{(6)}_{s,2}(r)-C^{(6)}_{s,2}(r+1)\over D_M},
 \qquad
 B_s={C^{(6)}_{s,2}(r+2)-C^{(6)}_{s,2}(r+3)\over D_M},      \tag{1.3}
\]

and

\[
                         M_r=\begin{pmatrix}
                         A_r&A_{r-1}\\ B_r&B_{r-1}
                         \end{pmatrix}.                     \tag{1.4}
\]

All four entries in (1.3) are exact rational numbers.

## 2. Removing the factorial obstruction at `j=2`

Fix an ordered blocker tuple and index its Boolean label cells by `eta`.
Write `c_eta` for the cell size, `m_eta` for the number of the four event
boundary labels in that cell, and `u_eta` for the number of positions of a
positional root interval in the corresponding positional blocker cell.

For one choice `sigma` of one label from each event pair, let
`h_eta(sigma)` count its two selected labels in cell `eta`, and give
`sigma` the product sign `sgn(sigma) in {+1,-1}`.  Choosing the other root
labels cell by cell and then bijecting the label cells to the positional
cells gives the exact signed weight

\[
\begin{split}
 &\sum_\sigma\operatorname {sgn}(\sigma)
 \prod_\eta {c_\eta-m_\eta\choose
                    u_\eta-h_\eta(\sigma)}
             u_\eta!(c_\eta-u_\eta)!\\
 &\quad=\prod_\eta(c_\eta-m_\eta)!
 \sum_\sigma\operatorname {sgn}(\sigma)
 \prod_\eta (u_\eta)_{h_\eta(\sigma)}
 (c_\eta-u_\eta)_{m_\eta-h_\eta(\sigma)}.                \tag{2.1}
\end{split}
\]

The second line is the key simplification.  After the common cell
factorials are removed, the marked-label factor has total degree four.

There is also an exact cyclic quotient for the positional sum.  Fix the
first positional blocker at relative start zero.  If the other blocker
starts and the root start are `d_1,...,d_m,u`, the number of translates
for which every retained start is nonzero is

\[
 b-\left|\{0,-d_1,\ldots,-d_m,-u\}\right|.                 \tag{2.2}
\]

Thus no factor `b` is approximated: (2.2) counts every retained positional
tuple exactly once.

For a rooted set on at most six vertices, five steps of size `+/-1,+/-3`
from `{0,5}` have representatives in `[-15,20]`.  When `b>=47`, no two
such representatives collide modulo `b`, and modular adjacency is ordinary
adjacency.  More explicitly, the inverse of the cut relabelling sends a
bounded lifted cut `x` to

\[
 \phi_r(2h)=-h\pmod b,
 \qquad \phi_r(2h+1)=r-h\pmod b.                            \tag{2.3}
\]

Thus all even cuts lie in one bounded cluster and all odd cuts in a second
bounded cluster.  Every step `1` or `3` joins opposite parities, so every
blocker has one cut in each cluster.  Its membership value on the two long
complementary gaps is opposite; hence the two gaps have distinct Boolean
membership vectors.  The cyclic cells therefore contain exactly two
macroscopic cells of sizes `r+a,r+b`, while all other cells have bounded
size.  There are twenty resulting macroscopic-factor types in (1.3).

For each type, factor out

\[
                         (r+a)!(r+b)!                         \tag{2.4}
\]

and the factorials of its bounded cells.  The remaining positional sum is
a polynomial in `r` of degree at most six.  Indeed, (2.1) has degree four,
the translate multiplicity (2.2) has degree one, and summing a piecewise
polynomial over the root start raises the degree by at most one.  All
breakpoints are among the fixed lifted endpoints above.  Hence seven exact
values determine each type polynomial; unused radii check the resulting
identities but are not an extrapolation premise.

## 3. Exact rational certificate

Collecting the twenty types gives the common denominator

\[
 Q(r)=(r-7)(r-6)\prod_{h=1}^{5}(r-h)^2\,r^3(r+1).           \tag{3.1}
\]

The determinant is exactly

\[
                         \det M_r={P(r)\over12Q(r)^2},       \tag{3.2}
\]

where, with `x=r-23`,

\[
                         P(r)=\sum_{i=0}^{26}a_ix^i         \tag{3.3}
\]

and the coefficients `a_i`, in increasing order, are

\[
\begin{array}{r|r}
i&a_i\\ \hline
0&62981083599956614478115107174154240\\
1&83731019301859283369193624773455872\\
2&53503167323082065050576460728060416\\
3&21874508927965046394283771602943488\\
4&6426381234586609560264944170832256\\
5&1444365103196196379308996566942592\\
6&258170481804935360887224705464448\\
7&37662599276106501292922749610480\\
8&4566280031383604538889761516544\\
9&466127777416902336699609774388\\
10&40438710544492245034672425456\\
11&3001278408729229165219406704\\
12&191400833973788705746237666\\
13&10515008159209256633718591\\
14&498043778207751522889761\\
15&20322149467297451253335\\
16&712577696918492023585\\
17&21377614697429068690\\
18&545129461736876970\\
19&11706023019295518\\
20&208959527775844\\
21&3045080777091\\
22&35300366213\\
23&313170763\\
24&1997129\\
25&8152\\
26&16
\end{array}                                                  \tag{3.4}
\]

Every entry in (3.4) is positive and every factor in `Q(r)` is positive
for `r>=23`; this proves the strict sign in (0.1).

For scale and for an independent check on the cancellations, the four
entries have Laurent expansions

\[
\begin{aligned}
 A_r&=-{2\over3}r^{-2}+{5\over6}r^{-3}
             -{13\over3}r^{-4}-{1\over3}r^{-5}+O(r^{-6}),\\
 A_{r-1}&=-{2\over3}r^{-2}+{17\over6}r^{-3}
             -{65\over6}r^{-4}+{55\over6}r^{-5}+O(r^{-6}),\\
 B_r&={2\over3}r^{-2}-{1\over6}r^{-3}
             +{38\over3}r^{-4}-{92\over3}r^{-5}+O(r^{-6}),\\
 B_{r-1}&={2\over3}r^{-2}-{13\over6}r^{-3}
             +{91\over6}r^{-4}-{164\over3}r^{-5}+O(r^{-6}).
                                                               \tag{3.5}
\end{aligned}
\]

The `r^-5` determinant coefficient cancels, while (3.5) gives

\[
 \det M_r={4\over3}r^{-6}-6r^{-7}
            +{1169\over12}r^{-8}+O(r^{-9}).                 \tag{3.6}
\]

Finally, `P(r)>=16(x^26+1)>=2^-21(x+1)^26` for `x>=0`.
Since `x+1=r-22>=r/23`, and every one of the sixteen linear factors in
`Q` is at most `2r`, (3.2) yields the deliberately crude uniform bound
(0.2).

## 4. Why this does not yet close the remote dressing

The component condition in Section 1 is essential.  If one augments the
bank by even a bounded collection of six-vertex terms consisting of a
four-vertex rooted atom plus a nearby component containing neither root,
the `r^-6` determinant coefficient can cancel.  For the radius-five
nearby bank used in the exact evaluator, the corresponding expansions are

\[
\begin{aligned}
 \widetilde A_r&=-{2\over3}r^{-2}+{13\over6}r^{-3}
                                      -{10\over3}r^{-4}+O(r^{-5}),\\
 \widetilde A_{r-1}&=-{2\over3}r^{-2}+{25\over6}r^{-3}
                                      -{59\over6}r^{-4}+O(r^{-5}),\\
 \widetilde B_r&={2\over3}r^{-2}-{5\over6}r^{-3}
                                      +{29\over3}r^{-4}+O(r^{-5}),\\
 \widetilde B_{r-1}&={2\over3}r^{-2}-{17\over6}r^{-3}
                                      +{73\over6}r^{-4}+O(r^{-5}),
                                                               \tag{4.1}
\end{aligned}
\]

and both the `r^-5` and `r^-6` determinant terms cancel:

\[
 \det\widetilde M_r=-3r^{-7}+{929\over12}r^{-8}+O(r^{-9}). \tag{4.2}
\]

This is not a counterexample to the fully dressed determinant; the nearby
bank is only one finite fragment of the remote expansion.  It is a rigorous
obstruction to claiming that an `O(1/r)` relative remote correction must
preserve the leading rooted-core determinant coefficient.  The next exact
subgate is a grouped resummation of **all** rootless components, or a second
functional whose determinant is stable under their common-shore action.

## 5. Scope

The theorem proves the first nonzero rooted-core determinant at `j=2`, with
an explicit all-`r>=23` sign and polynomial lower bound.  Together with the
shore-difference current theorem it shows precisely what remains:

\[
 \boxed{\text{control the common-shore cumulant of every rootless
 component without cancelling the transverse rooted-core signal.}}       \tag{5.1}
\]

It does not yet prove the full zero-avoidance residual, the uniform range
`2<=j<=r-2`, multidepth coinstantiation, or stopped-process stability.
