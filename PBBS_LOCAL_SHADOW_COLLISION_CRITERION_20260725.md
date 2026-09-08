# Exact local-shadow criterion for a coefficient-one erosion compiler

Date: 2026-07-25

Method: exact mathematics only.

## 0. Outcome

For a cyclic Johnson walk, short positive coordinate residence is exactly
equivalent to an equality between two adjacent consecutive-intersection
shadows.  Consequently the weakest purely local hypothesis needed by the
ordinary cyclic erosion compiler is not global rainbowness: it is only
adjacent separation of the lower shadows at every requested depth.

More precisely, for a rank-\(r\) cyclic Johnson walk of length \(S>2H\),
the following are equivalent:

1. every proper positive coordinate run has length at least \(H+1\);
2. for every \(1\le q\le H\), adjacent depth-\(q\) lower shadows are
   different.

Under either condition, one explicit nonzero word of length \(S+2H\)
covers every consecutive lower intersection and upper union through depth
\(H\).  The arbitrary-depth suspension obstruction shows that this
criterion is sharp: all depths below \(H\) may be injective while a dense
set of equalities first appearing at depth \(H\) forces linear excess for
an arbitrary compiler.

## 1. Setup

Let

\[
 X_i\in\binom{[n]}r,\qquad i\in\mathbb Z_S,
\]

be a cyclic Johnson walk.  Thus for every \(i\) there are unique labels
\(a_i\in X_i\) and \(e_i\notin X_i\) such that

\[
 X_{i+1}=X_i-\{a_i\}+\{e_i\}.                    \tag{1.1}
\]

For \(q\ge0\), define the consecutive lower shadow

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}X_{i+h}.              \tag{1.2}
\]

A **proper positive run** of a coordinate is a maximal proper circular
interval of owner indices on which that coordinate is present.  Coordinates
present on the whole cycle are harmless fixed-core coordinates and are not
called proper runs.

## 2. Exact collision--residence equivalence

### Theorem 2.1

For every \(1\le H<S\), the following are equivalent.

* Every proper positive coordinate run has length at least \(H+1\).
* For every \(i\in\mathbb Z_S\) and \(1\le q\le H\),
  \[
   L_i^{(q)}\ne L_{i+1}^{(q)}.                    \tag{2.1}
  \]

#### Proof

Suppose first that

\[
 L_i^{(q)}=L_{i+1}^{(q)}.                         \tag{2.2}
\]

The entering coordinate \(e_i\) belongs to \(X_{i+1}\) but not to
\(X_i\), and hence it does not belong to \(L_i^{(q)}\).  By (2.2), it
does not belong to \(L_{i+1}^{(q)}\) either.  It is present at the first
owner \(X_{i+1}\) of that latter window, so it must disappear by one of
\(X_{i+2},\ldots,X_{i+q+1}\).  The positive run beginning at \(i+1\)
therefore has length at most \(q\le H\).

Conversely, let a coordinate \(x\) have a proper positive run

\[
 X_a,X_{a+1},\ldots,X_b
\]

of length \(\ell=b-a+1\le H\).  Put

\[
 C=\bigcap_{j=a}^{b}X_j.
\]

The transition into the run adds \(x\) and changes no other membership
among coordinates of \(C\).  Therefore

\[
 C\cap X_{a-1}=C-\{x\}.
\]

The transition out of the run removes \(x\) and likewise changes no other
membership among coordinates of \(C\), so

\[
 C\cap X_{b+1}=C-\{x\}.
\]

Consequently

\[
 L_{a-1}^{(\ell)}
 =\bigcap_{j=a-1}^{b}X_j
 =C-\{x\}
 =\bigcap_{j=a}^{b+1}X_j
 =L_a^{(\ell)}.                                  \tag{2.3}
\]

This is an adjacent collision at a depth at most \(H\). \(\square\)

No rank hypothesis is used in Theorem 2.1.  If one additionally chooses a
shortest proper run, both shadows in (2.3) are automatically floor-correct:
an internal return causing rank loss would contain a still shorter proper
positive run.

## 3. Exact erosion compiler under local separation

Assume now that the equivalent conditions of Theorem 2.1 hold and that

\[
 r\ge H+1.                                       \tag{3.1}
\]

Define cyclic letters

\[
 D_i=\bigcap_{h=0}^{H}X_{i+h}.                   \tag{3.2}
\]

At most \(H\) coordinates of \(X_i\) can be removed in the following
\(H\) transitions, so

\[
 |D_i|\ge r-H\ge1.                               \tag{3.3}
\]

### Theorem 3.1

For every cyclic owner interval \([a,b]\) with
\(0\le b-a\le H\), one has

\[
 \boxed{
 \bigcap_{t=a}^{b}X_t
 =\bigcup_{i=b-H}^{a}D_i,}                       \tag{3.4}
\]

and

\[
 \boxed{
 \bigcup_{t=a}^{b}X_t
 =\bigcup_{i=a-H}^{b}D_i.}                       \tag{3.5}
\]

#### Proof

Fix a coordinate \(x\).  Its positive set on the owner cycle is a union
of proper circular intervals, each of length at least \(H+1\), together
possibly with the whole cycle.

The coordinate belongs to the left side of (3.4) exactly when one of its
positive intervals contains \([a,b]\).  Since that interval has length at
least \(H+1\), this is equivalent to containing an \((H+1)\)-owner
subinterval whose start lies in \([b-H,a]\).  By (3.2), that is exactly
membership in the right side of (3.4).

Similarly, \(x\) belongs to the left side of (3.5) exactly when one of its
positive intervals meets \([a,b]\).  Any point of such an intersection
lies in an \((H+1)\)-owner subinterval of the same positive run, and the
start of that subinterval lies in \([a-H,b]\).  This is exactly membership
in the right side of (3.5). \(\square\)

Emit

\[
 D_0,D_1,\ldots,D_{S-1},D_0,D_1,\ldots,D_{2H-1}.
                                                               \tag{3.6}
\]

Every interval on the right sides of (3.4)--(3.5) has at most \(2H+1\)
letters, so the repeated prefix linearizes it.  Equations (3.3)--(3.5)
give the following exact result.

### Corollary 3.2

If adjacent lower shadows are separated at every depth \(q\le H\), then
the cyclic owner walk has a nonzero literal contiguous-OR compiler of
length

\[
 \boxed{S+2H}                                    \tag{3.7}
\]

covering every consecutive lower intersection and upper union through
depth \(H\).

## 4. Defect form and the PBBS boundary

Let

\[
 \mathcal C_H
 =\{(i,q):1\le q\le H,\ L_i^{(q)}=L_{i+1}^{(q)}\}.
                                                               \tag{4.1}
\]

Mapping a proper positive run \([a,b]\) of length \(\ell\le H\) to
\((a-1,\ell)\) is injective and, by (2.3), lands in \(\mathcal C_H\).
Thus

\[
 \boxed{
 \#\{\text{proper positive runs of length at most }H\}
 \le |\mathcal C_H|.}                            \tag{4.2}
\]

Conversely, every element of \(\mathcal C_H\) certifies a proper positive
run of length at most its depth, by the first half of Theorem 2.1.

For the canonical PBBS factor, depth one has distinct intervening exact
middle owners, so \(\mathcal C_1=\varnothing\); this is the literal reason
the first-band rainbow forest compiler succeeds.  Gap-five PBBS returns
create residence-three runs, hence collisions first visible by depth
three.  The arbitrary-depth suspension construction proves that separation
at all smaller depths gives no control at the next depth.

Accordingly, a black-box universal \(S+O(H)\) theorem is impossible.  The
sharp PBBS-specific replacement target is one of the following equivalent
forms:

1. show that the collision-certified short residences admit only
   \(O(\operatorname{Cat}_m)\) cuts and use the already proved linear
   one-cut seam chart; or
2. construct a genuinely global rethreading which shares the letters of
   the dense collision set.

The theorem above proves the exact zero-collision case and identifies the
precise local defect.  It does not prove either positive PBBS estimate.
