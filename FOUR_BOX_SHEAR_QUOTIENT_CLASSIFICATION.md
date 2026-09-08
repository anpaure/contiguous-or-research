# Exact classification of the four-box shear quotient

## 1. Outcome

Put

\[
P_m=[0,m]^4
\]

and let \(z=(z_1,z_2,z_3,z_4)\in P_m\) have rank

\[
|z|=2m+d,\qquad d\ge1.
\]

The sector shears from `SQUARE_RECTANGLE_EDGE_BARRIER.md` do identify many
apparently different rectangles.  They do **not**, however, move every upper
target to a bottom-anchored triangular rectangle.  This note gives the exact
classification.

For one fixed coordinate orientation, \(z\) has such a representative if and
only if

\[
 z_3<d
 \quad\hbox{and}\quad
 z_1+z_2>m+z_3.                                      \tag{1.1}
\]

For the two pair-transposed orientations used by the hook construction, the
criterion is

\[
\begin{split}
 &(z_3<d\ \hbox{and}\ z_1+z_2>m+z_3)\\
 &\qquad\qquad\text{or}\\
 &(z_1<d\ \hbox{and}\ z_3+z_4>m+z_1).                \tag{1.2}
\end{split}
\]

Even if one grants all \(24\) coordinate permutations, write the coordinates
of \(z\), with multiplicity, in increasing order as

\[
                         a\le b\le c\le e.
\]

Then a bottom-anchored triangular representative exists if and only if

\[
                         \boxed{a<d\quad\text{and}\quad c+e>m+a.}  \tag{1.3}
\]

Thus (1.3) supplies both a canonical transversal for every class that is
triangularizable and an exact description of the residual classes.  The
residual is not a surface error.  There are at least

\[
              {245\over1944}m^4+O(m^3)                         \tag{1.4}
\]

upper targets without such a representative, and equally many lower targets.
Consequently no ordering or transversal made only from bottom-anchored
triangular providers can solve the full four-box problem, regardless of its
allowed repetition overhead.  A central-square or other genuinely
non-bottom provider mechanism remains indispensable.

## 2. One oriented sector

In one nonnegative sector write

\[
 X_s(p,q)=(s+p,m-s-q,q,m-p),
 \qquad (p,q)\in[0,m-s]^2.                            \tag{2.1}
\]

For a rectangle \(Q=[A,B]\times[C,D]\), its join is

\[
 J(s,Q)=(s+B,m-s-C,D,m-A).                            \tag{2.2}
\]

A bottom-anchored triangular rectangle has the form

\[
 Q=[u,r]\times[0,x],
 \qquad 0\le u<r\le R=m-s,\quad 0\le x<r.             \tag{2.3}
\]

If \(J(s,Q)=z\), equation (2.2) forces every parameter:

\[
 s=m-z_2,\qquad R=z_2,\qquad
 u=m-z_4,\qquad r=z_1+z_2-m,\qquad x=z_3.              \tag{2.4}
\]

There is no remaining choice hidden in the shear class.

### Theorem 1 (one-orientation criterion)

The parameters in (2.4) satisfy (2.3) if and only if (1.1) holds.

### Proof

The box constraints \(0\le z_i\le m\) automatically give

\[
0\le s\le m,\qquad 0\le u,qquad r\le R.
\]

The strict height condition \(x<r\) is exactly

\[
 z_3<z_1+z_2-m,
\]

which is the second inequality in (1.1).  This inequality also implies
\(r>0\) and \(x<R\).  Finally,

\[
\begin{split}
u<r
&\iff m-z_4<z_1+z_2-m\\
&\iff z_1+z_2+z_4>2m\\
&\iff d>z_3,
\end{split}
\]

which is the first inequality.  These are all the conditions in (2.3).
QED.

Swapping the first coordinate pair with the second changes the role tuple
from \((z_1,z_2,z_3,z_4)\) to \((z_3,z_4,z_1,z_2)\).  Applying Theorem 1 in
the two orientations gives (1.2).

## 3. The full permutation quotient

It is useful to grant more symmetry than the actual two-orientation hook
construction.  Given a permutation of the four coordinates, place the
permuted target in the four roles in (2.1).  Theorem 1 says that an anchor
coordinate \(x\), placed in role three, works exactly when

\[
 x<d
 \quad\hbox{and}\quad
 y+z>m+x                                             \tag{3.1}
\]

for two of the other three coordinates \(y,z\), placed in roles one and two.

### Theorem 2 (all-orientation criterion)

Let \(a\le b\le c\le e\) be the sorted coordinates of \(z\).  Some coordinate
permutation gives a bottom-anchored triangular representative if and only if
(1.3) holds.

### Proof

If (1.3) holds, use the role assignment

\[
                         (z_1,z_2,z_3,z_4)=(c,e,a,b).  \tag{3.2}
\]

Then (3.1) is exactly (1.3), so Theorem 1 gives a representative.

Conversely, suppose the smallest coordinate \(a\) fails as an anchor.  If
\(a\ge d\), every other possible anchor also violates the first inequality
in (3.1).  If instead \(c+e\le m+a\), then for any anchor \(x\ge a\), the
sum of the two largest remaining coordinates is at most
\(c+e\le m+a\le m+x\).  Hence the second inequality in (3.1) fails for every role
assignment.  Therefore some assignment works precisely when the assignment
(3.2) works, proving (1.3).  QED.

The proof gives a canonical representative.  Break coordinate ties by their
original indices, use (3.2), and put

\[
 s=m-e,\qquad R=e,\qquad
 u=m-b,qquad r=c+e-m,qquad x=a.                     \tag{3.3}
\]

Then

\[
                         Q_z=[u,r]\times[0,x]          \tag{3.4}
\]

is legal precisely under (1.3), and its join is \(z\).  Since the target and
tie-breaking rule recover the role permutation and all parameters, (3.3)
selects one representative from every triangularizable shear/orientation
class without any Hall or choice issue.

Accordingly the upper target set has the exact canonical partition

\[
 \mathcal U_m=\mathcal U_m^{\rm tri}\ \dot\cup\
              \mathcal U_m^{\rm core},                \tag{3.5}
\]

where

\[
\begin{split}
\mathcal U_m^{\rm tri}
 &=\{z:a<d,\ c+e>m+a\},\\
\mathcal U_m^{\rm core}
 &=\{z:a\ge d\ \text{or}\ c+e\le m+a\}.            \tag{3.6}
\end{split}
\]

The second family is the exact residual class obstruction.

### Boundary-robust variant

The triangular tail family used in the four-box reduction has \(u<r\).
Suppose one enlarges it by permitting the degenerate vertical rectangles
\(u=r\).  Such rectangles really can be formed from triangular letters
when \(x<r\).  The same proof changes only

\[
                         a<d\quad\hbox{to}\quad a\le d. \tag{3.7}
\]

The condition \(c+e>m+a\) remains strict: \(x=r\) cannot be supplied by the
alphabet \(\mathcal T_R\), since every letter of height \(x\) has first
coordinate strictly greater than \(x\).  Thus even this enlarged convention
leaves every target with \(a>d\) uncovered.

## 4. The residual is volumetric

For \(1\le d\le\lfloor m/3\rfloor\), consider the simpler subfamily

\[
 \mathcal C_{m,d}=
 \{z\in[0,m]^4:|z|=2m+d,\ z_i\ge d\text{ for every }i\}. \tag{4.1}
\]

Every member has \(a\ge d\), so Theorem 2 places it in
\(\mathcal U_m^{\rm core}\), even after all coordinate permutations are
allowed.

On writing \(z_i=d+y_i\), one obtains

\[
0\le y_i\le m-d,\qquad \sum_i y_i=2m-3d.
\]

Inclusion-exclusion gives the exact count

\[
 |\mathcal C_{m,d}|
 =\binom{2m-3d+3}{3}
  -4\binom{m-2d+2}{3},                               \tag{4.2}
\]

with the usual convention that a binomial coefficient is zero when its top
argument is below three.  Two simultaneous upper-bound violations are
impossible because their shifted sum would be \(-d-2\).

Summing (4.2) for \(1\le d\le m/3\) and using Riemann sums gives

\[
\begin{split}
 \sum_{d\le m/3}|\mathcal C_{m,d}|
 &= {m^4\over6}
    \int_0^{1/3}\bigl((2-3t)^3-4(1-2t)^3\bigr)\,dt
    +O(m^3)\\
 &= {245\over1944}m^4+O(m^3),                        \tag{4.3}
\end{split}
\]

which proves (1.4).  Thus the failure is not confined to sector boundaries
or to \(O(m^3)\) exceptional targets.

The same leading bound survives the boundary enlargement (3.7).  Replace
\(\mathcal C_{m,d}\) by the subfamily \(z_i\ge d+1\).  Its exact size is

\[
 \binom{2m-3d-1}{3}-4\binom{m-2d-1}{3},              \tag{4.4}
\]

again with the zero convention.  Relative to (4.2), the change at each
depth is only \(O(m^2)\), and over \(O(m)\) depths it is \(O(m^3)\).
Therefore its sum is still

\[
                         {245\over1944}m^4+O(m^3).     \tag{4.5}
\]

In particular, the volumetric obstruction does not depend on whether the
zero-width boundary is assigned to the triangular or central family.

## 5. Lower targets

Let \(y\in P_m\) have rank \(2m-d\).  Coordinatewise complementation

\[
                         \bar y=(m-y_1,\ldots,m-y_4)   \tag{5.1}
\]

turns a lower meet provider into an upper join provider and gives
\(|\bar y|=2m+d\).  Hence Theorems 1 and 2 apply verbatim to \(\bar y\).

If the coordinates of \(y\) are \(a\le b\le c\le e\), the all-orientation
criterion becomes

\[
                         \boxed{e>m-d\quad\text{and}\quad e>a+b.} \tag{5.2}
\]

Indeed the sorted complement is
\(m-e\le m-c\le m-b\le m-a\).  The residual lower family includes all
targets with every coordinate at most \(m-d\), and it has the same count as
(4.3).

## 6. Consequence for the positive four-box route

The shear quotient does remove the false requirement that every rectangle
be represented independently in every sector.  It also gives the explicit
canonical provider map (3.3) for every target in
\(\mathcal U_m^{\rm tri}\).  What it cannot do is eliminate central-square
compatibility.

In fact, even the artificially enlarged provider system using all \(24\)
coordinate orientations leaves the volumetric family (4.1) uncovered.
Therefore:

* there is no full target transversal consisting only of bottom-anchored
  triangular representatives;
* no ordering theorem for those representatives, even with unlimited
  repetition, can cover the complete four-box by itself;
* a valid near-width construction must superpose the triangular quotient
  word with intervals realizing \(\mathcal U_m^{\rm core}\) and its lower
  complement;
* the natural central diagonals remain one valid provider system for that
  core, but another non-bottom rectangle system could replace them;
* the outstanding subcubic problem is consequently a **hybrid** ordering and
  factor theorem, not a pure quotient-triangular transversal theorem.

This precisely justifies the central-square guardrail in
`FOUR_BOX_POSITIVE_ROUTE_AUDIT.md`: preserving those intervals is not merely
an artifact of the first construction.  Some non-bottom mechanism is forced
for a positive-density part of the target space.

## 7. Exact hybrid provider partition

For completeness, the residual family is not providerless.  The standard
hook decomposition gives it natural non-bottom intervals.  The following
formulas make the hybrid partition explicit.

In the fixed orientation, besides the bottom-tail condition

\[
\mathrm T:\qquad z_3<d,\qquad z_1+z_2>m+z_3,          \tag{7.1}
\]

there are three kinds of natural hook interval:

\[
\begin{array}{c|l}
\mathrm H&
 z_1+z_2\le m,\quad z_2+z_3\le m,\\[2mm]
\mathrm V&
 z_1+z_4\ge m,\quad z_3+z_4\le m,\quad z_3\ge d,\\[2mm]
\mathrm C&
 z_1\ge z_3,\quad z_3+z_4\ge m,\quad
 m\le z_1+z_2\le m+z_3.
\end{array}                                           \tag{7.2}
\]

Here \(\mathrm H\) is a horizontal subinterval of one square hook,
\(\mathrm V\) is a vertical subinterval, and \(\mathrm C\) crosses its
corner.  Their forced provider rectangles are respectively

\[
\begin{array}{c|c|c}
 &s&Q\\ \hline
\mathrm H&
 m-z_2-z_3&
 [m-z_4,\ z_1+z_2+z_3-m]\times\{z_3\},\\[1mm]
\mathrm V&
 z_1+z_4-m&
 \{m-z_4\}\times[z_3-d,\ z_3],\\[1mm]
\mathrm C&
 z_1-z_3&
 [m-z_4,\ z_3]\times[m-z_1+z_3-z_2,\ z_3].
\end{array}                                           \tag{7.3}
\]

Every entry in (7.3) is obtained directly by solving (2.2).  The
inequalities in (7.2) are exactly the conditions that the displayed sector
and hook interval are legal.

To see exhaustivity without a case search, give \(z\) its unique hook
coordinates

\[
\begin{split}
 H&=\max(z_1,m-z_2),&p&=z_1+z_2-m,\\
 K&=\max(z_3,m-z_4),&q&=z_3+z_4-m.
\end{split}                                           \tag{7.4}
\]

Then \(p+q=d>0\).  If \(H\ge K\), the case \(p>K\) is exactly
\(\mathrm T\).  The case \(p<-K\) is impossible because \(q\le K\) would
give \(p+q<0\).  Hence the remaining case is \(|p|\le K\), exactly the
central interval of the \((H,K)\) hook block; according to which leg or
corner it uses, one of \(\mathrm H,\mathrm V,\mathrm C\) holds.  If
\(H<K\), apply the pair transpose

\[
                         (z_1,z_2,z_3,z_4)
                         \longmapsto(z_3,z_4,z_1,z_2). \tag{7.5}
\]

Thus (7.1)--(7.5) give an exact deterministic provider assignment for every
upper target:

* choose the orientation by comparing \(H,K\);
* use a bottom triangular provider precisely in the tail case;
* otherwise use the corresponding natural hook interval.

Lower targets receive the complementary meet assignment.  This is the
correct target-level transversal.  The unresolved issue is physical
superposition: one near-once row must retain the hook intervals while also
realizing the triangular tail rectangles, and its lower providers must
survive one common linked factor band.  The classification proves that no
choice of shear representatives can remove that hybrid requirement.
