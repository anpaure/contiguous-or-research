# Independent audit of BALANCED_LINE_DEMAND_BRAID.md

## 1. Verdict

The architectural conclusion is correct, but Theorem 2 needs one exact
boundary correction.

The following parts check out:

* the demanded-seam characterizations (2.2)--(2.3);
* the canonical diagonal-path description and the arbitrary-choice
  degree-control formulas;
* the corner table (4.3);
* the fact that every odd seam has exactly one inward arm;
* Lemma 1's no-partial-sharing conclusion;
* the \(O(qm^2)\) bounded-copy construction.

The issue is in the count used in Theorem 2.  For the two extreme labels

\[
 (A,B)=(2r+1,0),\qquad (A,B)=(0,2r+1),
\]

one choice of odd baseline puts the inward defect on a physical line whose
formal \(p_0\) lies outside the box.  On that line the preferred segment
starts at \(p_1\), so the same \(p_1,\ldots,p_{q-1}\) occurrences can serve
the easy block and the portal block.  These seams cannot be charged
uniformly when odd baselines are arbitrary.

Deleting the two extreme labels at every level repairs the proof.  With

\[
 t=\left\lfloor {m-q-1\over3}\right\rfloor,
\]

the baseline-independent interior subcatalogue has

\[
 N_*=\sum_{r=1}^{t}2r=t(t+1)
\]

odd seams, rather than \(N=(t+1)(t+2)\).  The corrected lower bound is

\[
 \boxed{\#\text{ repeated base occurrences}\ge
        {t(t+1)(q-1)\over2}.}
\]

This remains \(\Omega(qm^2)\) uniformly for
\(2\le q\le m/3\), so the main asymptotic verdict and the matching
\(\Theta(qm^2)\) order statement survive unchanged.

The independent checker
scratch/verify_balanced_line_demand_braid_audit.py verifies the seam
conditions, component tables, corner identities, corrected interior
subcatalogue, and the extreme counterexample through (m=30), and checks
the component table through (m=90).

## 2. Demanded seams

Fix the displayed high/low orientation and write

\[
 y=(m-A,a,m-B,b),\qquad
 A+B=a+b-s+1,\qquad |a-b|<s.
\]

If \(A+B=2r\), the balanced lower bound gives \(a,b\ge r\).
The chosen orientation then forces

\[
 A+r\le m,\qquad B+r\le m.
\]

Conversely these inequalities make

\[
 s=1,\qquad a=b=r
\]

a legal tie target.  Thus (2.2) is exact.

If \(A+B=2r+1\), the balanced lower bound is
\(a,b\ge r+1\).  Hence a tie target requires

\[
 A+r+1\le m,\qquad B+r+1\le m.
\]

For \(q\ge2\), the converse uses

\[
 s=2,\qquad a=b=r+1.
\]

Thus (2.3) is also exact, and odd demand really is independent of \(q\)
once \(q\ge2\).  For \(q=1\), no odd label is demanded.

No hidden assumption about Johnson adjacency, factorability, or the word
order enters these two equivalences.

## 3. Demand graph and path formulas

For the canonical odd baseline \((c,d)=(r,r+1)\), direct equality of line
labels gives

\[
\begin{array}{lll}
 E(A,B)&\stackrel{X}{\sim}&O(A-1,B),\\
 E(A,B)&\stackrel{Y}{\sim}&O(A,B+1),\\
 O(A,B)&\stackrel{X}{\sim}&E(A+1,B),\\
 O(A,B)&\stackrel{Y}{\sim}&E(A,B-1).
\end{array}
\]

Therefore the exact component order is

\[
 \cdots-E(A-1,B-1)-O(A-1,B)-E(A,B)-O(A,B+1)
       -E(A+1,B+1)-\cdots .
\]

The even labels have constant \(A-B\); the odd labels have constant
\(A-B+1\).  The demanded inequalities cut a consecutive interval out of
each diagonal, so every nonempty canonical component is one path.  Direct
enumeration reproduces the three residue-class ranges in (3.7).

For arbitrary odd choices, formulas (3.9)--(3.10) are also correct.  After
contracting each even seam, the only two bridges between consecutive
vertices on one \(A-B\) diagonal are

\[
 O(A,B+1)\quad(\varepsilon=0),\qquad
 O(A+1,B)\quad(\varepsilon=1).
\]

Under degree at most two, a component is a path or a doubled adjacent
edge.  Uncontracting the doubled edge gives exactly the four-cycle (3.13).
The XOR assertion \(\mu=1\) is a correct label calculation.  Calling it
monodromy is architectural terminology rather than an additional word
theorem; one incidence cut removes that doubled-edge cycle, but does not
resolve the physical arm overlap.

There is a presentation typo in (3.4): the first occurrence of
varepsilon contains a control character.  This does not affect the
mathematics.

## 4. Corner table and inward-arm formulas

On \(X_{B,d}\), the preferred points are

\[
 p^X_j=(m+B-2d-j,d+j,m-B-1,d).
\]

On \(Y_{A,c}\), they are

\[
 p^Y_j=(m-A-1,c,m+A-2c-j,c+j).
\]

Substitution of \(A+B=2r\) gives \(p^X_0,p^Y_0\) at an even seam.
For \(A+B=2r+1\):

* the canonical baseline \((r,r+1)\) gives
  \(p^X_{-1},p^Y_1\);
* the reversed baseline \((r+1,r)\) gives
  \(p^X_1,p^Y_{-1}\).

Thus (4.3) is exact.  The inward \(Y\)-arm in the canonical case is

\[
 p^Y_1,p^Y_2,\ldots,
\]

and the inward \(X\)-arm in the reversed case is

\[
 p^X_1,p^X_2,\ldots.
\]

Choosing \((u,v)=(1,q-2)\), or its reversal, gives \(s=q\) because
\(u+v=s-1\).  The inward part is precisely

\[
 p_1,p_2,\ldots,p_{q-1}.
\]

For the corrected interior labels used in Section 6 below, all these
points and the other arm stay in the box.

## 5. Lemma 1 and partial sharing

Lemma 1 is correct, including at \(q=2\).  Here is the explicit alignment
argument.

Let the distinguished easy occurrence be

\[
 p_0,p_1,\ldots,p_q
\]

or its reverse.  Suppose some distinguished occurrence \(p_j\),
\(1\le j\le q-1\), were also used by the portal string.  Its portal
neighbour in the direction of \(p_{j-1}\) must be the occurrence
\(p_{j-1}\).  A word position has only one neighbour on that side, so this
is the distinguished \(p_{j-1}\).  Induction reaches the distinguished
\(p_1\).  Its outward neighbour is \(p_0\), whereas the portal requires
the opposite seam corner, a distinct point on a different physical line.
This is impossible.

The same induction works if the first shared point is \(p_{q-1}\), if
only a proper suffix was proposed to be shared, or if either block is
reversed.  At \(q=2\), the point \(p_1\) is internal to the easy
three-point block and already has its two line neighbours, so the external
portal corner forces a second occurrence.

Thus every one of the \(q-1\) inward-arm points needs an occurrence
distinct from the specified preferred easy-block occurrence.

## 6. The boundary defect in Theorem 2

The source takes every \(A,B\ge0\) with

\[
 A+B=2r+1,\qquad 0\le r\le t.
\]

The inequality

\[
 3r+q+1\le m
\]

does imply the demand conditions and makes the literal depth-\(q\) portal
arms legal.  It does **not** make \(p_0\) legal on the inward line for
both baseline choices at the two extreme labels.

Take

\[
 (A,B)=(2r+1,0)
\]

and choose the canonical baseline.  The inward line is \(Y_{A,r}\), and

\[
 p^Y_0=(m-A-1,r,\underbrace{m+A-2r}_{m+1},r),
\]

which is outside \(P_m\).  The first legal preferred point is

\[
 p^Y_1=(m-A-1,r,m,r+1).
\]

The preferred line segment can begin at \(p_1\); its occurrence may have
the opposite seam corner as its exterior word neighbour while retaining
the rest of the easy line block.  Lemma 1 therefore supplies no duplicate.

Symmetrically, for

\[
 (A,B)=(0,2r+1)
\]

and the reversed baseline, \(p^X_0\) has a coordinate \(m+1\), and the
same escape occurs.  Since the theorem permits arbitrary odd-baseline
choices, both extreme labels must be omitted from a uniform charge.

For

\[
 A,B\ge1,\qquad A+B=2r+1,
\]

one has \(A,B\le2r\).  Hence \(p_0\) is in the box for either inward
direction.  The source inequality also gives, for \(0\le j\le q\),

\[
\begin{aligned}
 0&\le m+A-2r-j\le m &&\text{on a canonical inward \(Y\)-line},\\
 0&\le m+B-2r-j\le m &&\text{on a reversed inward \(X\)-line},
\end{aligned}
\]

and all companion coordinates lie in \([0,m]\).  Thus the preferred block
\(p_0,\ldots,p_q\) and the entire portal target are legal.

At level \(r\ge1\), the number of positive solutions is \(2r\).
Consequently the corrected subcatalogue size is

\[
 N_*=\sum_{r=1}^{t}2r=t(t+1).
\]

## 7. Corrected charging

For a canonical inward arm, the line label \(Y_{A,r}\) determines \(A,r\)
and therefore

\[
 B=2r+1-A.
\]

For a reversed inward arm, \(X_{B,r}\) analogously determines the seam.
Thus two forced inward arms in the same direction never share a physical
line.

A base point lies on one \(X\)-line and one \(Y\)-line.  It is therefore
required by at most one selected \(X\)-arm and at most one selected
\(Y\)-arm.  Let \(R(p)\in\{0,1,2\}\) count these requirements.  Lemma 1
implies that \(R(p)>0\) forces multiplicity at least two, relative to the
one base occurrence.  Hence

\[
 \operatorname{mult}(p)-1\ge {R(p)\over2}.
\]

Summing over points gives

\[
 \sum_p(\operatorname{mult}(p)-1)
 \ge {1\over2}\sum_pR(p)
 ={t(t+1)(q-1)\over2}.
\]

This also handles equality-surface points which already have two preferred
system occurrences: one repeated occurrence can pay at most the two
directional requirements, exactly as the division by two allows.

Since \(q\le m/3\),

\[
 t=\left\lfloor{m-q-1\over3}\right\rfloor=\Theta(m),
\]

so the corrected result remains \(\Omega(qm^2)\).

## 8. Upper construction and final status

The source's upper construction is sound within its stated literal
architecture.

The strict min-comparison regions partition \(L_R\).  On each physical
line, its preferred points form one contiguous segment; equality points
are duplicated.  The equality surface has \(O(m^2)\) lattice points, so
the easy-system word has length

\[
 |L_R|+O(m^2).
\]

Appending one balanced two-arm block of at most \(2q\) letters for each
demanded seam in each orientation covers the complete tie strip.  There
are \(O(m^2)\) labels per orientation, giving

\[
 |L_R|+O(m^2)+O(qm^2).
\]

The multiplicity is uniformly bounded: a point belongs to one physical
line of each direction, each canonical line has demand degree at most two,
and there are four high/low orientations.  The displayed bound \(18\) is
conservative but valid.

Therefore the corrected ledger is:

| claim | audit status |
|---|---|
| demanded-seam iff conditions | proved |
| canonical demand components are paths | proved |
| arbitrary degree-controlled cycles are only four-cycles | proved |
| corner and inward-arm table | proved |
| no partial sharing in Lemma 1 | proved |
| exact count \(N=(t+1)(t+2)\) | **false at extreme labels** |
| corrected count \(N_*=t(t+1)\) | proved |
| lower repeat bound \(N_*(q-1)/2\) | proved |
| bounded-copy \(O(qm^2)\) repair | proved |
| literal balanced architecture costs \(\Theta(qm^2)\) repeats | proved |

The source's big-picture conclusion is unchanged: the balanced
line-demand paths do not yield a near-once word at linear depth while all
preferred easy line witnesses are kept literally.  A successful
width-plus-lower-order construction must let mixed seams replace some of
those easy witnesses, rather than requiring both copies.
