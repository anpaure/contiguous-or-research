# An explicit three-alpha fork portal at \(k=11\)

Date: 2026-07-27

Method: exact endpoint tables and strand tracing; no computational search.

## 0. Result

The lower bound of three formal alphas is sharp. There is an explicit
sequence

\[
A_1,\quad A_2,\quad A_0
\]

of legal alpha switches such that

- \(A_1\) and \(A_2\) are executable in the initial complemented PBBS factor;
- they insert the two missing negative diamonds of \(A_0\);
- \(A_0\) then becomes executable;
- \(A_0\) opens both ports of the alternating component and attaches them to
  outside strands.

The construction is a fork, not the monotone chain excluded in the
three-alpha normal-form note.

## 1. Alpha convention and marginal verification

For a rank-four core \(R\), spare \(\ell\), and directed triangle
\((i,j,k)\), write

\[
\begin{aligned}
A(R;\ell;i,j,k)
={}&
+z_{i\mid k\ell}+z_{j\mid i\ell}+z_{k\mid j\ell}\\
&-z_{i\mid j\ell}-z_{j\mid k\ell}-z_{k\mid i\ell}.
\end{aligned}
\tag{1.1}
\]

Thus the negative and positive endpoint pairs are

\[
\begin{array}{c|ccc}
\text{root}&i&j&k\\ \hline
-&\{\ell,j\}&\{\ell,k\}&\{\ell,i\}\\
+&\{\ell,k\}&\{\ell,i\}&\{\ell,j\}.
\end{array}
\tag{1.2}
\]

The lower multiset on both sides is

\[
\{R+i,R+j,R+k\}.
\tag{1.3}
\]

The middle-vertex multiset on both sides is

\[
\{R+\ell+i,R+\ell+j,R+\ell+k,
  R+i+j,R+j+k,R+k+i\}.
\tag{1.4}
\]

The upper multiset on both sides is

\[
\{R+\ell+i+j,R+\ell+j+k,R+\ell+k+i\}.
\tag{1.5}
\]

Equations (1.3)--(1.5) are the exact lower/middle/upper verification for
every switch below; there is no aggregate or asymptotic step.

## 2. The portal alpha \(A_0\)

Let

\[
R_0=\{1,5,7,9\},
\qquad
A_0=A(R_0;0;3,10,4).
\tag{2.1}
\]

Its negative side is

\[
\begin{array}{c|c|c}
\text{root}&\text{lower row}&\text{pair}\\ \hline
3&Z=R_0+3=\{1,3,5,7,9\}&\{0,10\}\\
10&Y_1=R_0+10=\{1,5,7,9,10\}&\{0,4\}\\
4&Y_2=R_0+4=\{1,4,5,7,9\}&\{0,3\}.
\end{array}
\tag{2.2}
\]

The first chord is the present alternating chord. The other two are absent
in the initial PBBS factor. Its positive side is

\[
Z:\{0,4\},\qquad
Y_1:\{0,3\},\qquad
Y_2:\{0,10\}.
\tag{2.3}
\]

Thus \(A_0\) has exactly the two-defect shape required by the fork normal
form.

## 3. First supply alpha \(A_1\)

Put

\[
R_1=\{5,7,9,10\},
\qquad
A_1=A(R_1;4;1,2,0).
\tag{3.1}
\]

Its negative endpoint table is

\[
\begin{array}{c|c|c}
\text{root}&\text{lower row}&\text{pair}\\ \hline
1&\{1,5,7,9,10\}=Y_1&\{4,2\}\\
2&\{2,5,7,9,10\}&\{4,0\}\\
0&\{0,5,7,9,10\}&\{4,1\}.
\end{array}
\tag{3.2}
\]

Direct cyclic reduction gives exactly these three PBBS endpoint pairs, so
\(A_1\) is initially executable. Its positive chord at root \(1\) is

\[
Y_1:\{4,0\},
\tag{3.3}
\]

which is the missing \(Y_1\)-diamond of \(A_0\).

For completeness, its other two positive pairs are

\[
\{2,5,7,9,10\}:\{4,1\},
\qquad
\{0,5,7,9,10\}:\{4,2\}.
\tag{3.4}
\]

## 4. Second supply alpha \(A_2\)

Put

\[
R_2=\{4,5,7,9\},
\qquad
A_2=A(R_2;3;1,10,0).
\tag{4.1}
\]

Its negative endpoint table is

\[
\begin{array}{c|c|c}
\text{root}&\text{lower row}&\text{pair}\\ \hline
1&\{1,4,5,7,9\}=Y_2&\{3,10\}\\
10&\{4,5,7,9,10\}&\{3,0\}\\
0&\{0,4,5,7,9\}&\{3,1\}.
\end{array}
\tag{4.2}
\]

Again these are the exact initial PBBS pairs, so \(A_2\) is executable. Its
positive chord at root \(1\) is

\[
Y_2:\{3,0\},
\tag{4.3}
\]

the second missing \(A_0\)-diamond. Its other positive pairs are

\[
\{4,5,7,9,10\}:\{3,1\},
\qquad
\{0,4,5,7,9\}:\{3,10\}.
\tag{4.4}
\]

The six negative lower rows in (3.2) and (4.2) are pairwise distinct.
Therefore \(A_1\) and \(A_2\) delete disjoint PBBS chords. Their inserted
chords are also distinct, and neither switch changes a negative chord needed
by the other. They may be executed in either order.

After both switches, all three negative diamonds in (2.2) are present, so
\(A_0\) is executable.

## 5. Exact execution order and net support

Execute

\[
F_{\rm PBBS}
\xrightarrow{A_1}
F_1
\xrightarrow{A_2}
F_2
\xrightarrow{A_0}
F_3.
\tag{5.1}
\]

The two supplied chords (3.3) and (4.3) are inserted by \(A_1,A_2\) and
then deleted by \(A_0\). Hence the total move from \(F_{\rm PBBS}\) to
\(F_3\) is a simple \(7\leftrightarrow7\) trade:

- seven original PBBS chords are deleted—the six chords in (3.2), (4.2),
  plus the alternating chord in (2.2);
- seven final chords are inserted—the four non-supply positives in (3.4),
  (4.4), plus the three \(A_0\) positives in (2.3).

Every intermediate and final state is a 2-factor, and (1.3)--(1.5) show
that every lower load, middle degree, and upper load is preserved exactly at
each step.

## 6. Strand-pairing proof of the portal

Immediately before \(A_0\), remove the three negative edges (2.2). Name
their six ports

\[
\begin{array}{lll}
a=Z+0,&b=Z+10,\\
c=Y_1+0,&d=Y_1+4,\\
e=Y_2+0,&f=Y_2+3.
\end{array}
\tag{6.1}
\]

The edge \(ab\) lies on the alternating component. Since \(A_1,A_2\) are
initially executable alpha charts and no initial alpha chart contains an
alternating chord, their six deleted edges lie outside that component.
They therefore leave the alternating cycle unchanged.

The three positive edges of \(A_0\) have the exact port pairing

\[
a\!-\!f,\qquad c\!-\!b,\qquad e\!-\!d.
\tag{6.2}
\]

Indeed:

\[
\begin{aligned}
Z:\{0,4\}&\quad\Rightarrow\quad
Z+0=a,\quad Z+4=Y_2+3=f,\\
Y_1:\{0,3\}&\quad\Rightarrow\quad
Y_1+0=c,\quad Y_1+3=Z+10=b,\\
Y_2:\{0,10\}&\quad\Rightarrow\quad
Y_2+0=e,\quad Y_2+10=Y_1+4=d.
\end{aligned}
\]

Thus neither pair of alternating ports \(a,b\) is rejoined internally.
Each is attached to an outside strand, one through \(f\) and one through
\(c\). The alternating path obtained by deleting \(ab\) is therefore a
proper subpath of a component containing outside PBBS strands.

This proves that \(A_0\) is a genuine portal, not merely a relabelling or an
internal reorder of the alternating cycle.

## 7. Equivariance and higher-depth scope

The certificate above is a labelled local move. It does **not** by itself
preserve \(\mathbb Z_{11}\)-equivariance.

The seven changed lower rows have the following cyclic gap words:

\[
\begin{array}{c|c}
\text{row}&\text{cyclic gap word}\\ \hline
\{1,3,5,7,9\}&22223\\
\{1,5,7,9,10\}&42212\\
\{2,5,7,9,10\}&32213\\
\{0,5,7,9,10\}&52211\\
\{1,4,5,7,9\}&31223\\
\{4,5,7,9,10\}&12215\\
\{0,4,5,7,9\}&41222.
\end{array}
\tag{7.1}
\]

No two words in (7.1) are cyclic rotations. Hence the seven rows belong to
seven distinct free \(\mathbb Z_{11}\)-orbits. The supports of the eleven
translated \(7\leftrightarrow7\) trades are therefore pairwise lower-row
disjoint. In particular, the translated sequences commute and applying all
eleven translates is a well-defined equivariant trade.

Thus overlap is not an additional gate: the full orbit preserves the
lower/middle/upper marginals orbitwise. Component-merging and quotient
voltage still require a separate audit.

In the sigma-map formulation, the net \(7\leftrightarrow7\) trade changes
the values of \(\sigma\) on seven lower rows while preserving both the
degree-two constraints and the complete upper-image multiplicity vector.
Consequently it preserves surjectivity whenever the initial sigma map is
surjective. Its orbit of eleven translates is therefore a legitimate local
move inside the \(42\)-variable equivariant CSP. What is not automatic is
that this orbit move merges quotient components or gives nonzero lift
voltage.

At depth \(q=1\), the damage is exactly zero: all three alpha switches
preserve lower colours, middle degree two, and the complete upper-load
multiset. The move changes only seven final chords relative to PBBS.

No claim is made that it preserves:

- a wreath residence condition;
- an \(H\)-safe chronology;
- or any depth-\(q\) shadow profile for \(q\ge2\).

Those are the next compatibility gates. The present theorem solves the
local component-portal problem only.

## 8. Theorem

### Theorem 8.1

The alternating component of the \(k=11\) complemented PBBS factor admits a
three-alpha fork portal. Consequently the previously proved lower bound of
three formal alphas is sharp.
