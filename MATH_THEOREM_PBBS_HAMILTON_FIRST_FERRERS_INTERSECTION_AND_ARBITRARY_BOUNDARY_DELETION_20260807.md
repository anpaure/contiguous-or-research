# Hamilton-first Ferrers intersection: every optimal-size boundary deletion is capacity-safe

**Date:** 2026-08-07  
**Method:** pure mathematics; no computation or finite search  
**Status:** unconditional exact theorem.  At the ordinary containment level,
the Hamilton-first boundary targets may be chosen arbitrarily: deleting any
optimal-size boundary set leaves a capacity-\(d\) matching into the middle
owners.  Consequently the clean lag-two flags extracted from a middle-levels
Hamilton cycle are automatically compatible with an exact residual Ferrers
containment matching.  The theorem does **not** make the targets assigned to
one owner nested and does not construct one literal source chronology.

## 1. Parameters

Let

\[
 1\le r\le n,
 \qquad
 \mathcal O={ [n]\choose r},
 \qquad
 W=|\mathcal O|,
\]

and let

\[
 \mathcal L=\{S\subseteq[n]:1\le |S|<r\},
 \qquad
 \Lambda=|\mathcal L|=\sum_{s=1}^{r-1}{n\choose s}.
 \tag{1.1}
\]

Fix an integer \(d\) satisfying

\[
 0\le d\le r-1,
 \qquad
 h:=\Lambda-dW\ge0,
 \qquad
 h\le {d+1\choose2}.
 \tag{1.2}
\]

These are exactly the positive-Ferrers-residue parameters in the OR-word
application.  When \(h=0\), the already-known uniform fractional flow gives
a capacity-\(d\) matching of all of \(\mathcal L\).  The content below is the
case \(h>0\).

For a family \(\mathcal Q\subseteq\mathcal O\), write

\[
 \partial_s\mathcal Q
 =\{S\in{[n]\choose s}:S\subset T\text{ for some }T\in\mathcal Q\},
 \qquad
 D(\mathcal Q)=\sum_{s=1}^{r-1}|\partial_s\mathcal Q|.
 \tag{1.3}
\]

Thus \(D(\mathcal Q)\) is the number of nonempty proper subsets covered by
the owners in \(\mathcal Q\).

## 2. The total-shadow endpoint lemma

For \(0\le q\le {a\choose j}\), let \(\mathcal C_{a,j}(q)\) be the first
\(q\) rank-\(j\) sets in colex order.  Put

\[
 \widehat D_{a,j}(q)
 =\bigl|\{S:|S|<j,\ S\subset T
              \text{ for some }T\in\mathcal C_{a,j}(q)\}\bigr|,
 \tag{2.1}
\]

where the empty set is included when \(q>0\), and
\(\widehat D_{a,j}(0)=0\).

### Lemma 2.1 (endpoint minimum for the total colex shadow)

For all integers \(a\ge j\ge1\) and \(d\ge0\),

\[
 \boxed{
 \min_{1\le q\le {a\choose j}}
   \bigl(\widehat D_{a,j}(q)-dq\bigr)
 =
 \min\left\{2^j-1-d,
             \sum_{t=0}^{j-1}{a\choose t}-d{a\choose j}
      \right\}.}
 \tag{2.2}
\]

In other words, among all nonempty colex prefixes, the minimum of
``total proper shadow minus \(d\) times the top size'' occurs either at one
top set or at the complete top layer.

#### Proof

For fixed \(j,d\), define

\[
 G_j(x)=\sum_{t=0}^{j-1}{x\choose t}-d{x\choose j}.
 \tag{2.3}
\]

Pascal's identity gives

\[
 G_j(x+1)-G_j(x)=G_{j-1}(x).
 \tag{2.4}
\]

We prove (2.2) by induction on \(j\).  For \(j=1\), every nonempty
family of singletons has the empty set as its only proper face, so the
quantity is \(1-dq\).  Its minimum is at \(q=1\) or \(q=a\), exactly as
claimed.

Assume the assertion for \(j-1\).  In one colex block write

\[
 q={x\choose j}+q',
 \qquad
 0\le q'\le{x\choose {j-1}},
 \qquad j\le x<a.
 \tag{2.5}
\]

The first \({x\choose j}\) top sets are all \(j\)-sets on \([x]\).
The next \(q'\) top sets are \(\{x+1\}\cup B\), where \(B\) runs through
the first \(q'\) rank-\((j-1)\) sets on \([x]\).  Proper faces not using
\(x+1\) give the complete \((j-1)\)-skeleton on \([x]\); proper faces
using \(x+1\) are in bijection with the proper faces, including the empty
face, of that rank-\((j-1)\) colex prefix.  Therefore

\[
 \widehat D_{a,j}(q)-dq
   =G_j(x)+\bigl(\widehat D_{x,j-1}(q')-dq'\bigr).
 \tag{2.6}
\]

By induction, the minimum of the second term over this block is one of

\[
 0,qquad A_{j-1}:=2^{j-1}-1-d,qquad G_{j-1}(x).
 \tag{2.7}
\]

The middle candidate never falls below both block endpoints.  If
\(A_{j-1}\ge0\), then
\(G_j(x)+A_{j-1}\ge G_j(x)\).  If \(A_{j-1}<0\), then
\(d>2^{j-1}-1\).  For every \(y\ge j-1\),

\[
 {\sum_{t=0}^{j-2}{y\choose t}\over {y\choose {j-1}}}
 \le 2^{j-1}-1<d.
 \tag{2.8}
\]

The displayed ratio is largest at \(y=j-1\), since each individual ratio
\({y\choose t}/{y\choose {j-1}}\), \(t<j-1\), decreases with \(y\).
Writing that ratio as \(H(y)\), we have
\(H(y)-d\le A_{j-1}<0\), while \(\binom y{j-1}\ge1\).  Hence directly

\[
 G_{j-1}(x)=\binom x{j-1}(H(x)-d)\le A_{j-1},
 \]

so

\[
 G_j(x)+A_{j-1}
 \ge G_j(x)+G_{j-1}(x)=G_j(x+1).
 \tag{2.9}
\]

Thus the minimum in every colex block is attained at one of its two
endpoints.  It remains to minimize \(G_j(x)\) over
\(j\le x\le a\).  The sign of its increment is the sign of

\[
 {\sum_{t=0}^{j-2}{x\choose t}\over{x\choose {j-1}}}-d.
 \tag{2.10}
\]

Again every summand in the ratio decreases with \(x\).  Hence the
increments of \(G_j\) change sign at most once, from nonnegative to
nonpositive.  The sequence first rises and then falls, so its minimum on
the interval occurs at \(x=j\) or \(x=a\).  These two values are precisely
the two expressions in (2.2).  This completes the induction. \(\square\)

## 3. A sharp total lower-shadow inequality

### Theorem 3.1 (\(d\)-line plus the full Ferrers residue)

Under (1.2), every nonempty family
\(\mathcal Q\subseteq\mathcal O\), with \(q=|\mathcal Q|\), satisfies

\[
 \boxed{D(\mathcal Q)\ge dq+h.}
 \tag{3.1}
\]

The inequality is sharp at \(\mathcal Q=\mathcal O\).

#### Proof

The iterated Kruskal--Katona theorem says that the colex prefix of size
\(q\) simultaneously minimizes every lower-rank shadow.  Hence

\[
 D(\mathcal Q)+1\ge \widehat D_{n,r}(q).
 \tag{3.2}
\]

Lemma 2.1 gives

\[
 D(\mathcal Q)-dq
 \ge
 \min\left\{2^r-2-d,\ \Lambda-dW\right\}.
 \tag{3.3}
\]

The second term is \(h\).  For the first, (1.2) and \(d\le r-1\) give

\[
 h\le {d+1\choose2}
 \le 2^r-2-d.
 \tag{3.4}
\]

For completeness, the last inequality is worst at \(d=r-1\), where it is

\[
 {r\choose2}\le2^r-r-1.
\]

It is equality at \(r=2\), and its right-minus-left difference increases
for \(r\ge2\); the case \(r=1\) is trivial.  Substitution in (3.3) proves
(3.1).  At the full owner layer,
\(D(\mathcal O)=\Lambda=dW+h\), so equality holds. \(\square\)

## 4. Arbitrary boundary deletion is safe

### Theorem 4.1 (uniform capacity matroid)

Let \(\mathcal B\subseteq\mathcal L\) be **any** family of exactly \(h\)
distinct lower targets.  Then every target of
\(\mathcal L\setminus\mathcal B\) can be assigned to a containing owner
in \(\mathcal O\), with no owner receiving more than \(d\) targets.

Equivalently, the transversal matroid obtained from \(d\) labelled copies
of every owner, on the ground set \(\mathcal L\), is the uniform matroid

\[
 U_{dW,\Lambda}.
 \tag{4.1}
\]

#### Proof

Apply Hall's theorem with \(d\) copies of every owner.  Let
\(\mathcal F\subseteq\mathcal L\setminus\mathcal B\), and let
\(\mathcal N(\mathcal F)\subseteq\mathcal O\) be its owner neighbourhood.

If \(\mathcal N(\mathcal F)=\mathcal O\), then

\[
 |\mathcal F|
 \le|\mathcal L\setminus\mathcal B|
 =\Lambda-h=dW.
 \tag{4.2}
\]

Otherwise put

\[
 \mathcal Q=\mathcal O\setminus\mathcal N(\mathcal F),
 \qquad q=|\mathcal Q|>0.
\]

No member of \(\mathcal F\) is a subset of an owner in \(\mathcal Q\).
Theorem 3.1 therefore gives

\[
 \begin{aligned}
 |\mathcal F|
 &\le \Lambda-D(\mathcal Q)\\
 &\le \Lambda-(dq+h)\\
 &=d(W-q)
 =d|\mathcal N(\mathcal F)|.
 \end{aligned}
 \tag{4.3}
\]

Every Hall row passes, proving the matching assertion.

The matching saturates every set of cardinality \(dW\).  Any smaller
family can be enlarged to cardinality \(dW\) and then restricted, proving
the uniform-matroid formulation. \(\square\)

### Corollary 4.2 (rank-profiled deletion)

The conclusion holds for every boundary rank profile
\((b_1,\ldots,b_{r-1})\) satisfying

\[
 \sum_s b_s=h,
\]

and for every choice of \(b_s\) distinct rank-\(s\) targets.  Ordinary
containment feasibility is completely independent of the names of the
boundary targets.

This is strictly stronger than the earlier joint boundary/owner-flow
theorem, which established the existence of some feasible named boundary.

## 5. Exact Hamilton-first Ferrers intersection

Now specialize to the notation of
`MATH_THEOREM_PBBS_HAMILTON_FIRST_GOOD_TURN_FLAG_EXTRACTION_20260807.md`.
Thus a middle-levels Hamilton cycle supplies well-spaced good turns with

\[
 R_j\in{[n]\choose {r-2}},
 \qquad
 M_j=R_j\setminus C_j,
 \qquad |C_j|=d,
 \tag{5.1}
\]

and a prescribed Ferrers rank list \(s_1,\ldots,s_h\).  The target
extraction theorem there chooses distinct

\[
 S_j\in{M_j\choose {s_j}}.
 \tag{5.2}
\]

Put \(\mathcal B=\{S_1,\ldots,S_h\}\).  Theorem 4.1 applies to this
boundary without any further correlation.  Hence:

### Corollary 5.1 (Hamilton-first Ferrers capacity intersection)

For every sufficiently large positive-residue parameter, the good turns,
flag bottoms, and distinct rank-profiled boundary targets may be chosen by
the Hamilton-first extraction theorem.  All complete clean lag-two
owner/lower/upper paths lie in that one Hamilton cycle, and the complement
of the chosen boundary targets has an exact capacity-\(d\) containment
matching to the middle owners.

No protected two-factor theorem and no joint Ferrers selector are needed
for this ordinary matching row.

## 6. Restricted-slot TU formulation (and why it is now redundant)

For completeness, before Theorem 4.1 the exact co-selection problem could
be written as one restricted bipartite network.  Give boundary slot \(j\)
the menu

\[
 \mathcal A_j={M_j\choose{s_j}},
\]

and retain \(d\) labelled copies of every owner.  Since the two shores
both have size \(\Lambda=dW+h\), a perfect matching exists exactly when

\[
 |\mathcal F|
 \le d|\mathcal N(\mathcal F)|
    +|\{j:\mathcal A_j\cap\mathcal F\ne\varnothing\}|
 \qquad(\mathcal F\subseteq\mathcal L).
 \tag{6.1}
\]

This is an ordinary TU/Hall system.  Theorem 4.1 proves something stronger:
once any distinct representatives have been chosen from the menus, the
residual owner matching exists.  Thus the menu slots may be solved first,
independently, and then discarded from the residual network.

## 7. Exact scope: nested flags remain open

Theorem 4.1 assigns residual targets to independent labelled slots of one
owner.  It does not ensure that the targets assigned to one owner are
comparable.  Therefore it does not solve any of the following:

1. partitioning the residual lower ideal into owner-anchored chains of
   length at most \(d\);
2. arranging those chains as suffix flags of one common width-\((d+2)\)
   literal source;
3. retaining the arbitrary-width upper OR deck and residence; or
4. the terminal common-cap/compiler incidence matching.

The capacity matroid being uniform gives no matroidal structure to the
ownerwise chain configurations: the family of chains available at one
owner is not a matroid.  The existing complete-owner counterexamples show
that a fixed perfect capacity matching need not admit owner-local
chainization, while the sharp complete-central chain theorem remains on
the one-sided equitable/uniform-chain frontier.

The gain is nevertheless exact and useful:

\[
 \boxed{
 \text{Hamilton boundary names and ordinary Ferrers capacity are now
 fully decoupled.}}
\]

Future work may choose the boundary entirely for the literal packet,
nested-flag, or compiler geometry without paying another ordinary Hall
condition.

## 8. Uniform capacity still does not imply nested flags

There is a sharp small Boolean warning inside the hypotheses of Theorem
4.1.  Take

\[
 n=4,\qquad r=3,\qquad d=2,
 \qquad W=4,\qquad\Lambda=10,\qquad h=2.
\]

Delete

\[
 \mathcal B=\bigl\{\{4\},\{3,4\}\bigr\}.
\]

The remaining eight targets have the capacity-two assignment

\[
\begin{array}{c|c}
123&1,12\\
124&2,24\\
134&13,14\\
234&3,23.
\end{array}
\tag{8.1}
\]

Thus Theorem 4.1 is visible directly.  Nevertheless no ownerwise
chain assignment exists.  All four owners would have to receive two
targets.  A two-target strict chain below a rank-three owner must contain
one singleton and one pair.  The residual family contains only the three
singletons \(1,2,3\), so four such chains are impossible.

This example is not at the intended largest owner rank and therefore is
not a no-go for the central PBBS problem.  It is an exact counterexample to
the black-box implication

\[
 \text{uniform capacity matroid}
 \Longrightarrow
 \text{ownerwise nested flag factor}.
\]

Accordingly, the arbitrary-deletion theorem removes the Ferrers
**capacity** correlation and nothing more.  The central nested-flag lift
still needs complete Boolean geometry and remains at the equitable-chain
frontier identified in the existing chainization notes.
