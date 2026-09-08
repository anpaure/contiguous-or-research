# Odd upper-diamond synchronization is not half-integral, but has an exact constant-local rounding

Date: 2026-08-01  
Lane: odd upper-diamond synchronization / protected pivot owner gate  
Status: exact non-half-integral vertex and unconditional integral
constant-local rounding.  Neither result supplies the exact synchronized
selector or bounded *total* defect.

## 0. Outcome

Let \(\Omega=[2m-1]\), and let a diamond be a pair

\[
 L\in{\Omega\choose m-1},\qquad
 R\in{\Omega\choose m+1},\qquad L\subset R.
\]

Its two physical owners are the two rank-\(m\) sets strictly between
\(L\) and \(R\).  The natural synchronization relaxation asks for one
diamond at every upper colour, lower load at most one, and owner load at
most two.

Two exact facts sharpen this relaxation.

1. It is **not half-integral**.  Already at \(m=4\) it has a vertex whose
   nonintegral coordinates are \(1/3\) and \(2/3\).  The active matrix of
   that vertex has determinant \(-3\).  Therefore a proof based on
   half-integral odd circuits, or on neutralizing only graph-like odd cycles,
   cannot prove synchronization.
2. If the exact capacities are relaxed locally, an integral selector always
   exists: every upper colour can be selected once with lower load at most
   three and owner load at most four.  This is the column-frequency-three
   specialization of degree-bounded matroid-basis rounding.

The second statement is a per-resource bound.  It permits violations at
exponentially many resources and therefore does **not** imply
\(B(k)+O(1)\).  Exact or bounded-total synchronization remains open.

## 1. The synchronization polytope

For every diamond \((L,R)\), introduce \(x_{L,R}\ge0\).  If
\(R-L=\{a,b\}\), write

\[
                         \psi(L,R)=\{L+a,L+b\}.
\]

Define \(P_m\) by

\[
\begin{aligned}
 \sum_{L\subset R}x_{L,R}&=1
       &&\left(R\in{\Omega\choose m+1}\right),\\
 \sum_{R\supset L}x_{L,R}&\le1
       &&\left(L\in{\Omega\choose m-1}\right),\\
 \sum_{(L,R):\,T\in\psi(L,R)}x_{L,R}&\le2
       &&\left(T\in{\Omega\choose m}\right).
                                                               \tag{1.1}
\end{aligned}
\]

The uniform point

\[
                         x_{L,R}={1\over {m+1\choose2}}          \tag{1.2}
\]

is feasible.  Its lower and owner loads are respectively

\[
                         {m-1\over m+1},\qquad
                         {2(m-1)\over m+1}.                    \tag{1.3}
\]

Thus the fractional relaxation has strict slack in both capacity shores.

## 2. A literal one-third vertex at \(m=4\)

Use the ground set \([7]\), and abbreviate a set by its digits.  Set every
unlisted variable to zero, and give the following 29 diamonds the displayed
weights.  The two physical owners of a row are obtained by inserting either
element of \(R-L\) into \(L\).

\[
\begin{array}{c|c|c@{\qquad}c|c|c}
L&R&x&L&R&x\\ \hline
123&12346&1/3&123&12356&2/3\\
124&12345&1/3&124&12346&2/3\\
126&12567&1  &134&13456&1\\
135&12345&1/3&135&13567&2/3\\
145&12457&1/3&147&14567&1\\
156&12356&1/3&157&12357&1/3\\
157&12457&2/3&167&13467&1\\
234&23457&1  &235&12345&1/3\\
235&12357&2/3&236&23467&1\\
237&12347&1  &267&12467&1\\
345&23456&1/3&356&13567&1/3\\
356&23456&2/3&357&13457&1\\
367&12367&1  &456&12456&1\\
457&24567&1  &467&34567&1\\
567&23567&1  &&&
\end{array}                                                   \tag{2.1}
\]

### Theorem 2.1

The point (2.1) is a vertex of \(P_4\).  Its 15 fractional coordinates
consist of nine copies of \(1/3\) and six copies of \(2/3\).

#### Feasibility

Every one of the 21 upper colours has total load one.  The lower-load
multiset over the 35 lower colours is

\[
               \{1^{20},(1/3)^3,0^{12}\},                    \tag{2.2}
\]

and the owner-load multiset over the 35 middle owners is

\[
       \{2^9,(5/3)^1,(4/3)^5,1^{13},(2/3)^4,0^3\}.           \tag{2.3}
\]

Thus all inequalities in (1.1) hold.

#### Vertex certificate

Besides all 21 upper equalities, the following six lower rows are tight:

\[
                         123,124,135,157,235,356,             \tag{2.4}
\]

and the following two owner rows are tight:

\[
                         1235,1357.                           \tag{2.5}
\]

Restricted to the 29 positive columns, these 29 active rows are linearly
independent.  Here is a direct elimination, avoiding any numerical LP
claim.

The 14 integral columns are fixed immediately by their upper equations.
On the remaining 15 columns, use the seven nontrivial upper equations, the
six rows (2.4), and the two rows (2.5).  Put

\[
                         z=x_{135,12345}.
\]

The elimination which fixes \(z\) is short.  The
lower-\(135\) row gives

\[
 x_{135,13567}=1-z.
\]

After subtracting the integral column \((357,13457)\), the owner-\(1357\)
row gives \(x_{157,12357}=z\).  In turn the lower-\(157\),
upper-\(12457\), upper-\(12357\), and lower-\(235\) rows give

\[
 x_{157,12457}=1-z,\quad x_{145,12457}=z,\quad
 x_{235,12357}=1-z,\quad x_{235,12345}=z.             \tag{2.7}
\]

The upper-\(12345\), lower-\(124\), upper-\(12346\), and lower-\(123\)
rows now give successively

\[
 x_{124,12345}=1-2z,\quad x_{124,12346}=2z,\quad
 x_{123,12346}=1-2z,\quad x_{123,12356}=2z.           \tag{2.8}
\]

Finally the owner-\(1235\) row is

\[
 2z+z+z+(1-z)=2,
\]

and hence

\[
                              3z=1.                           \tag{2.9}
\]

The remaining upper and lower equations give

\[
\begin{aligned}
 x_{156,12356}&=1-2z,&
 x_{356,13567}&=z,\\
 x_{356,23456}&=1-z,&
 x_{345,23456}&=z.                                  \tag{2.10}
\end{aligned}
\]

At \(z=1/3\), equations (2.7)--(2.10) give exactly nine entries equal to
\(1/3\) and six equal to \(2/3\).

Thus the positive coordinates are uniquely determined by the active rows;
together with the zero-coordinate constraints, this proves extremality.
With the row and column orders just displayed, the active determinant has
absolute value three (and sign \(-3\) in lexicographic order).  In
particular, the point is not half-integral. \(\square\)

### Corollary 2.2 (no exchange confined to the active face)

There is no nonzero linear exchange supported entirely on the 29 positive
diamonds which preserves all active upper, lower and owner rows.

Indeed, such an exchange would lie in the kernel of the nonsingular active
matrix.  Consequently every repair of this one-third block must leave the
active face: it must either make at least one tight lower/owner inequality
slack or import a currently zero diamond.  In particular, an argument that
merely decomposes the positive support into half-integral odd circuits, or
applies Boolean \(C_6\) exchanges while keeping every active capacity row
equal, cannot be complete.

The statement does not say that \(P_4\) lacks integral points.  It says
that its fractional faces have genuinely higher-order torsion and that
integer synchronization requires an escape theorem, not only cycle
cancellation.

### Proposition 2.3 (this torsion block has a monotone integral forest escape)

The obstruction above is to active-face motion, not to integer feasibility.
Keep all 14 unit diamonds from (2.1), and from the fractional support keep
exactly

\[
\begin{gathered}
 (123,12346),\ (124,12345),\ (135,13567),\ (156,12356),\\
 (157,12457),\ (235,12357),\ (356,23456).              \tag{2.11}
\end{gathered}
\]

Give these 21 diamonds weight one and all others weight zero.  Then every
upper colour occurs once, the 21 lower colours are distinct, and the owner
degree multiset is

\[
                         \{2^{11},1^{20},0^4\}.               \tag{2.12}
\]

Moreover the physical owner graph is a forest.  Its 14 path components,
including isolates, are

\[
\begin{array}{lll}
1235-2357,&1236-1234-1245,&1237-2347-2345,\\
1246,&1247,&1257-1457-1467-1367-2367-2346,\\
1345-1346,&1347,&1456-2456,\\
1567,&2356-3456,&2457-4567-3467,\\
2467-1267-1256-1356-1357-3457,&2567-3567.&
\end{array}                                                   \tag{2.13}
\]

Thus the cubic torsion can be escaped at \(m=4\) without importing a zero
column.  More precisely, delete only the owner-\(1235\) equality from the
active system and retain every other active row.  Equations (2.7)--(2.10)
then parametrize one literal feasible segment

\[
                              0\le z\le {1\over3}.             \tag{2.14}
\]

The endpoint \(z=1/3\) is the fractional vertex, and \(z=0\) is exactly
the integral forest (2.11)--(2.13).  Along this segment every upper and
tight lower row remains equal, owner \(1357\) remains equal, and owner
\(1235\) decreases from load two to load one.  All other capacity loads stay
within their bounds.  Thus this is a monotone slack-releasing escape: no
capacity is violated at an intermediate point.

What remains open is a uniform theorem guaranteeing such a slack-releasing
escape for every fractional face, with a protected pivot bank.

## 3. Exact constant-local integral rounding

The following theorem is unconditional but deliberately weaker than exact
synchronization.

### Theorem 3.1

For every \(m\ge2\), there is an integral diamond selection \(B\) such that

\[
\begin{aligned}
 |B\cap E_R|&=1 &&(R\in\mathcal U),\\
 |B\cap E_L|&\le3 &&(L\in\mathcal L),\\
 |B\cap E_T|&\le4 &&(T\in\mathcal M),                 \tag{3.1}
\end{aligned}
\]

where \(E_R,E_L,E_T\) are respectively the diamonds of upper colour
\(R\), lower colour \(L\), and physical incidence with owner \(T\).

#### Proof

Take the partition matroid whose parts are the upper-colour classes
\(E_R\), with one element required from each part.  Its bases are exactly
the unconstrained one-diamond-per-upper selections.

Regard the lower and owner classes as degree hyperedges, with upper bounds
one and two.  Every diamond lies in exactly three such hyperedges: its one
lower class and its two owner classes.  Hence the column frequency is

\[
                              \Delta=3.                         \tag{3.2}
\]

The uniform point (1.2) is a feasible fractional matroid base satisfying
all those upper bounds.  The upper-bound-only degree-bounded matroid-basis
rounding theorem of Király--Lau--Singh gives an integral base with additive
violation at most \(\Delta-1=2\) in every degree row.  Therefore lower load
is at most \(1+2=3\), owner load at most \(2+2=4\), and every upper part is
still used exactly once. \(\square\)

The cited result is Theorem 2 of T. Király, L. C. Lau and M. Singh,
*Degree bounded matroids and submodular flows*, Combinatorica 32 (2012),
703--720, DOI `10.1007/s00493-012-2760-6`.  Only its upper-bound case is
used here.

### Protected conditional form

Let \(P\) be a fixed protected diamond bank.  Contract its upper-colour
parts and subtract its incidences from the lower and owner capacities.  If
the resulting protected face of (1.1) is fractionally feasible, the same
theorem returns an integral selection containing \(P\) with the bounds
(3.1).  Fractional feasibility of that protected common face is not implied
by the two separate protected marginal extension theorems.

There is also an unconditional coarser protected statement.  Suppose the
protected diamonds have distinct upper and lower colours and physical owner
degree at most two.  Force them, and on every other upper colour use the
uniform distribution.  This has lower load below two and owner load below
four after adding the protected bank.  Applying the same rounding theorem
to the residual partition matroid gives an integral extension with

\[
                         d_L\le4,\qquad d_T\le6.               \tag{3.3}
\]

Thus a fixed tight-pivot bank can always be retained in a constant-local
approximate selector.  This still says nothing about acyclicity.

## 4. Why constant-local is not bounded-total

The theorem above controls the largest multiplicity at one resource.  It
does not bound

\[
 \sum_L(d_L-1)_+
 \quad\hbox{or}\quad
 \sum_T(d_T-2)_+.                                      \tag{4.1}
\]

Those sums may receive contributions from exponentially many lower colours
or owners.  No terminal \(O(1)\) sidecar follows from (3.1) or (3.3).

The distinction is already visible in independent rounding of the uniform
point.  A fixed lower load converges to a Poisson random variable of mean
one, and a fixed owner load to one of mean two.  The expected overloads per
resource converge respectively to

\[
                         e^{-1},\qquad 4e^{-2},                 \tag{4.2}
\]

so naive rounding has \(\Theta(W)\) total defect despite the strict
fractional slack (1.3).  Correlation, rather than concentration, is the
essential missing ingredient.

## 5. Revised synchronization target

The exact next theorem is not half-integral odd-circuit cleanup.  It is one
of the following genuinely stronger statements.

1. **Torsion escape:** every fractional face of (1.1) admits a sequence of
   Boolean exchanges which imports zero columns and reaches an integral
   point without violating any exact row.
2. **Bounded-total rounding:** an integral upper-exact selector exists with
   total lower-plus-owner overload \(O(1)\), preferably zero, while retaining
   the protected pivot bank.
3. **Direct synchronization:** (1.1) itself has an integral point containing
   the protected bank.

Even the third statement does not impose physical acyclicity.  After exact
synchronization, cycle elimination and the fixed-root tail/head Catalan
connector remain separate gates.

The one-third vertex proves that any successful exchange theorem must allow
higher-degree circuits or controlled excursions outside the current positive
support.  The constant-local rounding theorem proves that unbounded local
multiplicity is not the obstruction.  What remains is bounded **global**
correlation.
