# Independent audit of the portal easy-line completion barrier

## 1. Verdict

The main claims of PORTAL_EASY_LINE_COMPLETION.md are correct under their
stated scope.

In particular:

* the physical line-family counts are correct;
* the crossing criterion and the factor of four from high/low orientations
  are correct and do not overcount physical crossings;
* the formulas for \(S_q\) and
  \[
  J_q=4S_{q-1}
  \]
  are correct for both parities, including \(q=1,2\);
* each of the \(J_q\) retained crossings really is interior in both line
  directions;
* the four required word adjacencies at such a crossing force a second
  occurrence of that crossing point;
* distinct crossings give distinct forced extra occurrences;
* the canonical balanced-demand graph is a union of monotone paths, but
  its shared arms are nested on the same ray, so the graph path order alone
  is not a physical arm braid.

Thus the proved lower bound

\[
 |W|-|L_{2m-1}|\ge J_q
 =
 \begin{cases}
 \displaystyle {q(2q+1)(q-2)\over3},&q\ {\rm even},\\[5pt]
 \displaystyle {q(2q+1)(q-2)+3\over3},&q\ {\rm odd}
 \end{cases}                                           \tag{1.1}
\]

is valid for every adjacency-preserving completion in the definition of
the source.  It gives

\[
                         J_q={2\over3}q^3+O(q^2).       \tag{1.2}
\]

The result is intentionally architectural.  It does not prove that the OR
targets themselves require this repetition after target-by-target witness
selection.

## 2. Audit of the line families

Let

\[
 {\cal N}_q=\{(A,B)\in{\mathbb Z}_{\ge0}^2:A+B\le q-1\}.
\]

It has \(q(q+1)/2\) elements.  In a fixed last-pair orientation an
\(X\)-line is determined by

\[
                         (x_3,x_4)=(m-B-1,A).          \tag{2.1}
\]

Swapping coordinates 3 and 4 produces a different physical line.  Indeed,
\(A\le q-1\), whereas

\[
 m-B-1\ge m-q\ >q-1
\]

under \(q\le m/3\).  Hence the two coordinates cannot be equal, and

\[
                         |{\cal X}_q|=q(q+1).          \tag{2.2}
\]

The identical argument gives \(|{\cal Y}_q|=q(q+1)\).  This also proves
that the two high/low orientations in each coordinate pair are recoverable
from the physical point, a fact needed later to justify the factor four.

## 3. Audit of the crossing count

Take the \(X\)-line indexed by \((A,B)\) and the \(Y\)-line indexed by
\((C,D)\), in fixed high/low orientations.  Their unique intersection
candidate is

\[
             (m-C-1,D,m-B-1,A).
\]

Its coordinate sum is

\[
 2m-2+(A-B)-(C-D).
\]

It lies in \(L_{2m-1}\) exactly when

\[
                         (A-B)-(C-D)=1.               \tag{3.1}
\]

Put

\[
 n_q(d)=\#\{(A,B)\in{\cal N}_q:A-B=d\}.
\]

Solving \(A=d+B\) gives

\[
 n_q(d)=
 \begin{cases}
 \left\lfloor(q+1-|d|)/2\right\rfloor,&|d|\le q-1,\\
 0,&|d|\ge q.
 \end{cases}                                           \tag{3.2}
\]

Therefore the number in one orientation is

\[
                         S_q=\sum_d n_q(d)n_q(d-1).    \tag{3.3}
\]

The two orientations of the first coordinate pair and the two
orientations of the second pair are independent.  They produce distinct
physical points because each fixed pair has one coordinate at most
\(q-1\) and the other at least \(m-q\).  Hence the unrestricted crossing
count is exactly \(4S_q\), not merely at most that number.

For the lower-bound argument the source keeps \(A\ge1\) and \(D\ge1\).
After writing \(A'=A-1,D'=D-1\), both index pairs lie in
\({\cal N}_{q-1}\), and (3.1) becomes

\[
                         (A'-B)-(C-D')=-1.
\]

By the symmetry \(n_{q-1}(-d)=n_{q-1}(d)\), or simply by reindexing the
sum, this count is \(S_{q-1}\).  Thus the exact number of retained
crossings is

\[
                         J_q=4S_{q-1}.                \tag{3.4}
\]

The sign change in this substitution is harmless; this is the only
algebraic detail which is slightly compressed in the source proof.

## 4. Independent evaluation of \(S_q\)

The symmetry of \(n_q\) gives

\[
 S_q=2\sum_{d\ge1}n_q(d)n_q(d-1).                    \tag{4.1}
\]

For \(q=2h\),

\[
 n_q(2j)=n_q(2j+1)=h-j\qquad(0\le j<h),
\]

so

\[
\begin{aligned}
S_{2h}
 &=2\left(\sum_{k=1}^{h}k^2+
           \sum_{k=1}^{h-1}k(k+1)\right)\\
 &={h(h+1)(4h-1)\over3}
  ={q(2q-1)(q+2)\over12}.                            \tag{4.2}
\end{aligned}
\]

For \(q=2h+1\),

\[
 n_q(2j)=h+1-j,\qquad n_q(2j+1)=h-j,
\]

and

\[
 S_{2h+1}
 =2\sum_{k=1}^{h}\bigl(k^2+k(k+1)\bigr)
 ={q(2q-1)(q+2)-3\over12}.                           \tag{4.3}
\]

Substituting \(q-1\) in (4.2)--(4.3) and multiplying by four yields
(1.1).  Direct boundary values are

\[
                         J_1=J_2=0,\quad J_3=8,\quad J_4=40,         \tag{4.4}
\]

consistent with both parity formulas.

I also ran scratch/verify_portal_easy_line_completion.py.  It
independently enumerates the diagonal fibers and physical crossing
quadruples for \(1\le q\le80\), and it reproduced every displayed formula
and the canonical path/nesting identities.

## 5. Interior legality

At a retained crossing the variable first pair is

\[
                         (m-C-1,D)
\]

and the variable last pair is

\[
                         (m-B-1,A).
\]

The restrictions \(A,D\ge1\) give a positive coordinate in each varying
pair.  The other two coordinates are at least \(m-q\ge1\), while all four
coordinates are at most \(m-1\).  Hence one may move one unit in either
direction along each of the two complementary physical lines.  The point
has exactly two distinct line-neighbors in the \(X\)-direction and two in
the \(Y\)-direction.

The four neighbors are mutually distinct: an \(X\)-move changes one of
coordinates 1,2, while a \(Y\)-move changes one of coordinates 3,4.
Therefore the source has not counted a boundary point or identified two
of the four required adjacencies.

## 6. Audit of the word lower bound

Fix one retained crossing \(p\).  Adjacency preservation requires four
different unordered word adjacencies

\[
 \{p,x^-\},\quad\{p,x^+\},\quad
 \{p,y^-\},\quad\{p,y^+\}.                            \tag{6.1}
\]

One occurrence of \(p\) in a linear word has at most two neighboring word
positions (only one if it is a word endpoint).  Since the four neighboring
values in (6.1) are distinct, one occurrence cannot realize all four
adjacencies.  Thus \(p\) occurs at least twice.

A physical point determines its \(X\)-line and \(Y\)-line uniquely.  The
orientation gap noted in Section 2 then determines the four oriented
indices uniquely.  Hence two different counted line-pairs cannot produce
the same crossing point.  The \(J_q\) points requiring a second occurrence
are distinct.

Condition 1 in the source definition already requires one occurrence of
every point of \(L_R\).  Adding the \(J_q\) forced second occurrences gives

\[
                         |W|\ge |L_R|+J_q.            \tag{6.2}
\]

No assumption about how the other letters are ordered is used.  In
particular, this remains valid if different line pieces are interleaved,
if lines are globally reversed, or if a crossing's two occurrences serve
different additional purposes.

## 7. Canonical demand paths and nesting

For the fixed floor/ceiling convention, direct comparison of the physical
line labels gives

\[
\begin{aligned}
E(A,B)&\leftrightarrow O(A-1,B),\\
E(A,B)&\leftrightarrow O(A,B+1).
\end{aligned}                                         \tag{7.1}
\]

Passing through those odd seams reaches respectively
\(E(A-1,B-1)\) and \(E(A+1,B+1)\).  Thus \(A-B\) is invariant on even
labels and every component lies on one finite monotone diagonal.  Boundary
deletions can shorten or split such a diagonal but cannot create a cycle.

On a shared canonical column line, suppressing the fixed coordinates, the
two requested rays are

\[
\begin{aligned}
E&:(m-B-v,r+v),&&v=0,1,2,\ldots,\\
O&:(m-B-1-v,r+1+v),&&v=0,1,2,\ldots .
\end{aligned}                                         \tag{7.2}
\]

The odd ray is exactly the even ray with its first point deleted.  The row
case is symmetric.  Therefore a demand-path turn at the odd seam preserves
only the first local adjacency of the longer preceding arm; it does not
magically retain both nested rays.

This confirms the source's central interpretation: degree two solves the
incidence branching problem, not the physical ordering problem.

## 8. Scope and minor presentation notes

The theorem proves a barrier only for words satisfying both conditions in
the source's definition of an adjacency-preserving completion.  It does
not apply after one chooses a single witness direction for each easy
target or replaces discarded line windows by mixed seams.  The final
open target in the source is therefore stated at the correct level.

Two presentation details are nonfatal:

1. in the substitution leading to \(S_{q-1}\), the difference changes
   from \(+1\) to \(-1\); symmetry of \(n_{q-1}\) should be mentioned
   explicitly;
2. equation labels in the proof of Lemma 1 jump from (3.6) to (3.9), but
   no mathematical equation is missing.

Neither affects the theorem.  The final audit ledger is:

| claim | verdict |
|---|---|
| \(|{\cal X}_q|=|{\cal Y}_q|=q(q+1)\) | proved |
| crossing criterion (3.2) | proved |
| four orientation classes are disjoint | proved |
| \(J_q=4S_{q-1}\) | proved |
| parity formulas for \(S_q,J_q\) | proved |
| retained crossings are interior in both lines | proved |
| four adjacencies force a repeated crossing | proved |
| all \(J_q\) forced crossings are distinct | proved |
| canonical demand components are paths | proved |
| canonical shared arms are nested | proved |
| arbitrary target-selective completion costs \(\Omega(q^3)\) | **not claimed** |

