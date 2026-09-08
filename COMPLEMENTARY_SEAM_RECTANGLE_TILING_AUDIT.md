# Independent audit of the complementary seam-rectangle tiling

## 1. Verdict and scope

I audited `COMPLEMENTARY_SEAM_RECTANGLE_TILING.md` independently against
the displayed formulas and against
`scratch/verify_complementary_seam_rectangles.py`.

The main result, Theorem 1, is correct as stated.  In particular, for

\[
  1\le q\le \lfloor m/3\rfloor
\]

the construction really gives a word on (L_{2m-1}) of exact length

\[
  |L_{2m-1}|+4q(q-1)
\]

which covers every target of depth (1\le s\le q) missed by both
complementary complete-line systems.  Every selected hard-family witness
has exactly (s+1) letters, and no base-layer point occurs more than
twice.

The later balanced line-demand discussion has a more qualified verdict.
The reduction in Section 7 through the canonical maximum-degree-two demand
graph is correct.  Section 8 is not a proved tiling theorem, as the source
already says.  Moreover, its informal assertion that every odd demanded
seam necessarily collides with a *demanded* adjacent even seam has boundary
exceptions, and allowing the alternative odd baselines independently can
raise the demand-graph degree from two to three.  These issues do not affect
Theorem 1, but they matter for the proposed all-band continuation.

The audited source hashes are

```text
8647fc6b7d670161f9e4f986dab3fa82c7c467cf0c89a4f4db39fb2259be8c86  COMPLEMENTARY_SEAM_RECTANGLE_TILING.md
bd0d4ca6c3b21fc1e79d5abc9cf607445da746db10128bef9ca7d784cee8586d  scratch/verify_complementary_seam_rectangles.py
```

## 2. Complete lines and the hard-family normal form

Put (R=2m-1).  A coordinate-(\{1,2\}) line witness for
(y\in L_{R+s}) runs from

\[
  y-se_1\quad\hbox{to}\quad y-se_2.
\]

It is legal exactly when (y_1,y_2\ge s), and its coordinatewise maximum
is (y).  The complementary criterion is (y_3,y_4\ge s).  Thus

\[
  \min(y_1,y_2)<s,\qquad \min(y_3,y_4)<s
\]

is exactly the family missed by both complete-line directions.

Under (s\le q\le m/3), each coordinate pair has exactly one coordinate
below (s).  If both coordinates of one pair were below (s), one
coordinate of the other pair would also be below (s), and hence

\[
 |y|\le (2s-2)+(m+s-1)=m+3s-3<2m-1+s,
\]

a contradiction.  The low coordinate in each pair is therefore unique.
After the two independent coordinate swaps, write

\[
 y=(m-A,a,m-B,b).
\]

The rank equation gives

\[
 \delta:=A+B=a+b-s+1.
\]

Since (0\le a,b\le s-1), one has

\[
 0\le\delta\le s-1,
 \qquad A,B\le\delta\le a,b.
\]

All of these implications are valid; in particular the inequalities
(A,B\le a,b), needed for the nonnegative portal parameters, are not an
extra assumption.

For one orientation and a fixed depth (s), fixing
(delta\in\{0,\ldots,s-1\}) gives (delta+1) choices of ((A,B)) and
(s-\delta) choices of ((a,b)).  Therefore the exact number is

\[
 \sum_{\delta=0}^{s-1}(\delta+1)(s-\delta)
   =\binom{s+2}{3}
\]

per orientation and (4\binom{s+2}{3}) overall.  Summing over (s\le q)
gives (4\binom{q+3}{4}).  Equations (2.7)--(2.8) are correct.

## 3. Portal coordinates, physical order, and witness length

For (A+B\le q-1), the two arms are

\[
 X_u=(m-A-u,B+u,m-B-1,A),
 \qquad 0\le u\le q-1-B,
\]

and

\[
 Y_v=(m-A-1,B,m-B-v,A+v),
 \qquad 0\le v\le q-1-A.
\]

Their coordinate sums are exactly (2m-1).  Their designated low
coordinates are at most (q-1).  A designated high coordinate is at least
(m-2q+2); the other elementary high-coordinate bounds are stronger.
Thus every coordinate is in ([0,m]), and

\[
 m-2q+2>q-1
\]

under (q\le m/3).

In the physical order

\[
 X_{q-1-B},\ldots,X_0,Y_0,\ldots,Y_{q-1-A},
\]

the interval from (X_u) through (Y_v) contains

\[
 X_u,X_{u-1},\ldots,X_0,Y_0,Y_1,\ldots,Y_v.
\]

Its exact maximum is

\[
 (m-A,B+u,m-B,A+v).
\]

For a hard target, set (u=a-B) and (v=b-A).  The normal-form
inequalities make both parameters legal, and

\[
 u+v=a+b-(A+B)=s-1.
\]

The interval therefore has exactly

\[
 (u+1)+(v+1)=s+1
\]

letters.  This verifies the physical contiguity and the exact witness
length, rather than merely the Cartesian set of available maxima.

The internal line formulas in Section 6 are also correct.  A block of
(ell) consecutive letters internal to either arm has maximum rank
(R+\ell-1).

## 4. Collision classification and exact length

Within one orientation, the (X)-letters are injectively indexed by
((A,B,u)): coordinates 4 and 3 recover (A,B), after which coordinate 2
recovers (u).  The analogous statement holds for the (Y)-letters.

Solving a cross-type equality gives exactly

\[
 A'=A+u-1,qquad B'=B+u,qquad u+v=1.
\]

Thus only ((u,v)=(0,1)) and ((1,0)) occur.  The legal instances of each
type number (inom q2), so one orientation has exactly
(q(q-1)) repeated points.  Since each type is separately injective, no
point has multiplicity greater than two.

The four coordinate orientations are disjoint.  In each pair the
designated low coordinate is at most (q-1), while the designated high
coordinate is at least (m-2q+2>q-1).  Hence the locations of the two high
coordinates can be recovered from the physical point itself.

For a fixed (delta=A+B), one block has

\[
 (q-B)+(q-A)=2q-\delta
\]

occurrences, and there are (delta+1) pairs ((A,B)).  Consequently the
four orientations use

\[
 P_q=4\sum_{\delta=0}^{q-1}(\delta+1)(2q-\delta)
     ={4q(q+1)(2q+1)\over3}
\]

portal occurrences.  Their number of distinct physical points is

\[
 P_q-4q(q-1).
\]

Appending each unused point of (L_R) once therefore gives exact total
length

\[
 P_q+\bigl(|L_R|-(P_q-4q(q-1))\bigr)
   =|L_R|+4q(q-1).
\]

It also proves that every base-layer point occurs at least once and at most
twice.  Direct inclusion--exclusion gives

\[
 |L_{2m-1}|=\binom{2m+2}{3}-4\binom{m+1}{3}
            ={2m^3+6m^2+4m\over3}
            =M_m-(m+1),
\]

so (1.4) and the (M_m+O(m^2)) conclusion are correct.

Concatenating the portal blocks cannot destroy any selected witness,
because every selected hard witness is internal to its own block.  The
unused singleton appendices can indeed be viewed as alternating degenerate
segments.  Nothing in this step asserts that an easy complete-line witness
survives, and the source correctly avoids that assertion.

## 5. The role of (q\le m/3)

The stated bound is a sufficient, not sharp, range.  It is used in two
separate places:

1. to rule out two low coordinates in the same pair in the hard-target
   normal form;
2. to make the designated high/low gap strict and hence separate the four
   portal orientations.

Both uses are valid at the endpoint (q=\lfloor m/3\rfloor).  The local
suffix--prefix maximum formula can remain legal beyond this range for
individual parameters, but the proved global orientation-disjoint packing
does not automatically extend.

## 6. Audit of the finite verifier

The supplied script exhausts all (3\le m\le30) and all
(1\le q\le\lfloor m/3\rfloor), a total of 145 parameter pairs.  It checks

* the portal occurrence formula;
* rank and box membership of every portal letter;
* maximum multiplicity two and exact duplicate excess (4q(q-1));
* exhaustive coverage and exact count of every hard target.

It passes all 145 cases.

The script does not explicitly append the unused base-layer points, check
the designated (s+1)-letter witness rather than some possibly different
crossing witness, test the internal sliding equations, or test Sections
7--8.  Those claims require the algebra above.  I also independently
enumerated the formula-selected witnesses through (m=19), checking their
legality, exact maximum, and exact length; all cases passed.

## 7. What is proved in the balanced-demand reduction

Let

\[
 a=\min(y_1,y_2),\qquad b=\min(y_3,y_4).
\]

On the complete coordinate-(\{1,2\}) witness, the minimum value of the
first-pair minimum is (a-s), while (b) is fixed.  Hence the entire
witness lies in the preferred (\{1,2\}) region exactly when

\[
 b\le a-s.
\]

The complementary statement is (a\le b-s).  Failure of both is exactly
(|a-b|<s).  The equality surface in the base layer contains only
(O(m^2)) points: after fixing the common minimum and the choices of which
coordinate attains it, the rank equation leaves only (O(m)) possibilities.

For one chosen high/low orientation write

\[
 y=(m-A,a,m-B,b),\qquad \delta=A+B=a+b-s+1.
\]

The tie-strip inequality implies (delta\le2a) and (delta\le2b), so

\[
 c=\lfloor\delta/2\rfloor,qquad
 d=\lceil\delta/2\rceil
\]

satisfy (c,d\le a,b).  The displayed central endpoints are legal
rank-(R) points.  With (u=a-c), (v=b-d), their two arms have maximum
exactly (y) and (u+v=s-1).  Thus the balanced seam is an exact local
replacement for every tie-strip target.

Under this fixed floor/ceiling convention, a coordinate-(\{1,2\}) line
is labelled by ((m-B-1,d)).  Fixing this label fixes (B,d), and the only
possible values of (delta) are (2d) and (2d-1).  Hence at most two seam
labels demand the line.  The complementary line has the same property.
The resulting bipartite line-demand graph has maximum degree two and is a
union of paths and cycles.  This part of Section 7 is correct.

## 8. Necessary qualifications to the parity discussion

For odd (delta=2r+1), both balanced assignments

\[
 (c,d)=(r,r+1)\quad\hbox{and}\quad(c,d)=(r+1,r)
\]

are locally legal.  Algebraically, the first choice shares its two line
labels with the formal neighboring even levels (delta-1) and
(delta+1); the reversed choice swaps which neighboring even level is
met in each direction.  For interior catalogue points this explains the
nested-arm collision described in Section 8.

Two qualifications are essential.

First, a formal adjacent even seam need not itself be demanded by any
tie-strip target through depth (q).  For example, take

\[
 m=8,qquad q=2,qquad (A,B)=(0,5),qquad \delta=5.
\]

The target

\[
 y=(8,3,3,3)\in L_{17}
\]

has (s=2), (a=b=3), and belongs to the tie strip.  Choose the legal odd
baseline ((c,d)=(3,2)).  Its requested line labels are

\[
 (m-B-1,d)=(2,2),qquad (m-A-1,c)=(7,3).
\]

The first could only be shared with the lower even label having
((A',B')=(-1,5)), which is invalid.  The second could only be shared with
the upper even pair ((A',B')=(0,6)).  But that pair has no legal tie-strip
target through depth two: it would have (b\le m-B'=2), whereas the
balanced inequality for (delta'=6) requires (b\ge3).  Thus this odd
*demanded* seam has a balanced choice sharing neither of its physical lines
with a demanded even seam.  The word “whichever” in Section 8 is therefore
too strong if the catalogue means the actual demand catalogue.

Second, the degree-two statement is tied to the fixed floor/ceiling
convention.  If odd baselines are reversed independently, a line may have
three requests.  A smallest example is (m=6,q=2).  The demanded labels

\[
 (A,B)=(1,0),(2,0),(3,0)
\]

have (delta=1,2,3).  Use the canonical baseline on (delta=1), the
forced even baseline on (delta=2), and the reversed baseline on
(delta=3).  All three then request the same coordinate-(\{1,2\}) line
label

\[
 (m-B-1,d)=(5,1).
\]

Corresponding legal targets are, respectively,

\[
 (5,1,6,1)\ (s=2),\qquad
 (4,1,6,1)\ (s=1),\qquad
 (3,2,6,2)\ (s=2).
\]

Therefore a future parity-selection lemma must enforce degree control; it
cannot assume that arbitrary odd choices preserve the path/cycle graph.

Finally, the claimed (Theta(q)) arm overlap and
(Theta(qm^2)) naive total are plausible for a large interior subcatalogue,
but Section 8 does not define and sum the exact demanded arm radii.  They
should be treated as architectural motivation, not as an audited lower
bound.

## 9. Final ledger

| Claim | Audit status |
|---|---|
| Complete-line criterion | proved |
| Unique hard-family orientation for (q\le m/3) | proved |
| Hard-family counts (4\binom{s+2}{3}), (4\binom{q+3}{4}) | proved |
| Portal coordinate/rank legality | proved |
| Exact suffix--prefix maximum and (s+1) witness length | proved |
| Collision classification and multiplicity at most two | proved |
| Four-orientation disjointness | proved |
| Exact length (|L_R|+4q(q-1)) | proved |
| Coverage of every base-layer point after append | proved |
| Coverage of easy targets after extracting line arms | **not claimed / open** |
| Canonical balanced demand graph has maximum degree two | proved |
| Arbitrary odd baseline choices preserve degree two | false |
| Every odd demanded seam necessarily meets a demanded even seam | false at catalogue boundaries |
| Balanced line-demand braid | conjectural |

Accordingly, the main theorem is a sound positive result for precisely the
doubly-missed hard family.  It does not yet cover the whole upper band, and
the next step must solve a parity-sensitive ordered line-demand problem with
the extra degree-control and boundary qualifications above.
