# Research note: the first shadow of an exact wreath factor

## 1. The exact (q=1) problem

Assume `m>=2`; the degenerate `m=1` case has length-zero cyclic intervals
and must be handled separately.

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn=\operatorname {Cat}_m,\qquad
 N=\binom n{m-1}=\frac m{m+2}W.
\tag{1.1}
\]

For a cyclic order (C) of ([n]), let (\mathcal W_r(C)) denote its
(n) cyclic intervals of length (r).  An exact middle wreath factor is a
family (\mathcal F) of (B) orders such that the families
(\mathcal W_m(C)), (C\in\mathcal F), partition
(\binom{[n]}m).  For (S\in\binom{[n]}{m-1}), write

\[
 \mu(S)=\#\{C\in\mathcal F:S\in\mathcal W_{m-1}(C)\},
 \qquad M_1=\#\{S:\mu(S)=0\}.
\tag{1.2}
\]

The exact slot identities are

\[
 \sum_S\mu(S)=W,
 \qquad
 M_1=\sum_S(\mu(S)-1)_+-(W-N),
 \qquad W-N=\frac{2W}{m+2}.
\tag{1.3}
\]

There is also a pointwise identity which any proposed multiplicity vector
must satisfy:

\[
 \boxed{\quad
 \sum_{S\ni x}\mu(S)=(m-1)B\qquad(x\in[n]).
 \quad}
\tag{1.4}
\]

Indeed, in one cyclic order a fixed point belongs to exactly (m-1) of the
length-((m-1)) intervals.

The Johnson-graph form is useful.  Consecutive middle intervals in one
wreath are adjacent vertices of (J(n,m)), and color the edge (AA') by
(A\cap A').  Thus an exact wreath factor is a special (2)-factor on all
middle vertices, and (\mu(S)) is the number of its edges of color (S).
For a fixed (S), those edges form a matching on the (m+2) supersets of
(S): at a middle interval the two incident wreath edges use its two
different boundary facets.  Consequently

\[
 0\leq\mu(S)\leq\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{1.5}
\]

This makes the rigidity transparent.  A zero-defect factor with no
multiplicity above two would have exactly (W-N) double colors and all
other colors single.  Its double-color family would have to obey the regular
point margins forced by (1.4).

## 2. Exact first-shadow coverage is genuinely feasible

The canonical MSW factor misses four triples when (m=4), but this is a
property of that factor, not an obstruction to the exact-factor fibre.  The
following fourteen cyclic orders form an exact factor of
(\binom{[9]}4):

```text
1 2 4 8 5 9 6 7 3
1 2 9 5 7 3 8 4 6
1 2 9 8 6 3 7 5 4
1 3 4 6 9 7 8 2 5
1 3 4 7 6 2 9 5 8
1 3 6 2 4 9 8 7 5
1 3 7 9 4 5 2 6 8
1 4 5 8 6 7 2 3 9
1 5 2 7 3 8 9 4 6
1 6 9 5 3 8 4 2 7
1 7 4 6 8 2 3 5 9
1 7 6 5 4 9 3 2 8
1 8 4 7 5 2 6 3 9
1 8 6 5 3 4 2 7 9
```

Direct cyclic-window enumeration gives

\[
 \#\{A:|A|=4,\mu_4(A)=1\}=126
\tag{2.1}
\]

and, at the first shadow,

\[
 \#\{S:\mu(S)=1\}=42,
 \qquad
 \#\{S:\mu(S)=2\}=42.
\tag{2.2}
\]

Thus every one of the (84) triples is covered, no triple occurs three
times, and the unavoidable (126-84=42) duplicates are attained exactly.
The list is a compact finite certificate: for each row and each cyclic start,
sort the next four entries (respectively the next three); (2.1)--(2.2) are
then literal equality tests.  In particular, no universal parity, point-
margin, or matching obstruction can force positive first-shadow defect.

This does not give an all-(m) construction.  It does show that the right
question is global re-bundling, not repair of a logically unavoidable hole.
It also does not imply the stronger rainbow-cut property below: for the nine
coordinate cuts of this certificate, the numbers of distinct internal path
intersections are

\[
 46,47,47,46,46,48,45,52,43
\]

out of the required `56`.  Thus perfect global first-shadow coverage and
even one rainbow coordinate cut are logically independent conditions.

## 3. A stronger sufficient target: many rainbow coordinate cuts

Fix a coordinate (z).  In each wreath, the (m+1) middle intervals which
avoid (z) occur consecutively.  Write the resulting complementary Johnson
path on ([n]\setminus\{z\}) as

\[
 X_0^z,X_1^z,\ldots,X_m^z,
 \qquad X_m^z=([n]\setminus\{z\})\setminus X_0^z.
\tag{3.1}
\]

Call (z) a **rainbow cut** of (\mathcal F) if the (mB) internal
intersections

\[
 X_{i-1}^z\cap X_i^z,
 \qquad C\in\mathcal F,\quad 1\leq i\leq m,
\tag{3.2}
\]

are pairwise distinct.  The count is exact:

\[
 mB=\binom{2m}{m-1}.
\tag{3.3}
\]

Hence a rainbow cut covers every ((m-1))-set avoiding (z), exactly once.
This gives a clean amplification lemma.

### Lemma 3.1 (several rainbow cuts force small defect)

If every coordinate in a set (Z\subseteq[n]), (|Z|=t), is a rainbow
cut, then

\[
 \boxed{\quad
 M_1(\mathcal F)\leq\binom{n-t}{m-1-t}.
 \quad}
\tag{3.4}
\]

In particular, for (t=o(\sqrt m)),

\[
 \frac{M_1(\mathcal F)}W
 \leq
 \frac{(m)_{t+1}}{(m+2)(2m+1)_t}
 =2^{-t}\exp\!\bigl(O(t^2/m)\bigr),
\tag{3.5}
\]

so any (t=t(m)\to\infty) proves (M_1=o(W)).

#### Proof

If a target (S) avoids some (z\in Z), the rainbow-cut property for (z)
places (S) among (3.2).  A missing target must therefore contain all of
(Z), and there are exactly the number in (3.4).  Dividing by (W) gives
the falling-factorial expression in (3.5); its estimate follows by taking
logarithms.  □

This is stronger than necessary, but it replaces the amorphous condition
"few holes" by (t) exact bijections, each on an ordinary complementary
Johnson path factor.  The canonical distinguished MSW cut is not rainbow in
general, so a new factor or a positive-density re-bundling is still required.

## 4. The square-resolved four-level bridge

There is an exact way to obtain a two-sided rainbow **path cover** from a
Hamilton cycle in four Boolean levels.  It is useful, but Section 6 records
why it is not yet a wreath theorem.

Let (Q=[2m-1]), let (z\notin Q), and let (H) be a Hamilton cycle through
the four levels

\[
 \binom Q{m-2},\quad\binom Q{m-1},\quad
 \binom Qm,\quad\binom Q{m+1}.
\tag{4.1}
\]

Put

\[
 V=\binom{2m-1}{m-1},\qquad
 L=\binom{2m-1}{m-2},\qquad
 B=V-L=\operatorname {Cat}_m.
\tag{4.2}
\]

Suppress every outer vertex of (H).  A lower outer vertex
(T\in\binom Q{m-2}) has two neighbors

\[
 S_T=T\cup\{a_T\},\qquad S'_T=T\cup\{b_T\}.
\]

After mapping an inner lower vertex (S) to (S\cup\{z\}), this outer
two-path becomes a Johnson edge whose meet and join are

\[
 \{z\}\cup T,
 \qquad
 \{z\}\cup\alpha(T),
 \qquad
 \alpha(T):=T\cup\{a_T,b_T\}\in\binom Qm.
\tag{4.3}
\]

Similarly, an upper outer vertex (U\in\binom Q{m+1}) has neighbors

\[
 A_U=U\setminus\{a_U\},\qquad A'_U=U\setminus\{b_U\}.
\]

Its suppressed Johnson edge has

\[
 \text{meet }\sigma(U):=U\setminus\{a_U,b_U\}
       \in\binom Q{m-1},
 \qquad
 \text{join }U.
\tag{4.4}
\]

A central edge (S\subset A), with (|S|=m-1) and (|A|=m),
maps to the Johnson edge between (S\cup\{z\}) and (A), with colors

\[
 \text{meet }S,qquad \text{join }A\cup\{z\}.
\tag{4.5}
\]

Suppressing all outer vertices turns (H) into a cyclic traversal (G) of
the (2V=\binom{2m}m) middle (m)-sets.  It has (2L) outer-derived
edges and exactly

\[
 (2V+2L)-4L=2(V-L)=2B
\tag{4.6}
\]

central edges.

### Theorem 4.1 (square-resolved Hamilton bridge)

Assume:

1. the completion map (\alpha:\binom Q{m-2}\to\binom Qm) is
   injective;
2. the completion map (\sigma:\binom Q{m+1}\to\binom Q{m-1}) is
   injective; and
3. among the (2B) central edges of (H), there are (B) edges (S\subset A)
   forming a perfect matching between

   \[
    R_-:=\binom Q{m-1}\setminus\sigma\!\left(\binom Q{m+1}\right)
    \quad\text{and}\quad
    R_+:=\binom Qm\setminus\alpha\!\left(\binom Q{m-2}\right).
   \tag{4.7}
   \]

Keep all (2L) outer-derived edges of (G) and precisely those (B)
central edges.  The result is a spanning cover of (J(2m,m)) by exactly
(B=\operatorname {Cat}_m) paths, and every rank-((m-1)) meet color and
every rank-((m+1)) join color occurs exactly once.

#### Proof

Both residual sets in (4.7) have size (V-L=B).  Delete from the cycle (G)
the other (B) central edges.  Deleting (B) distinct edges from one cycle
gives exactly (B) path components (isolated vertices are allowed as
length-zero paths), and it retains

\[
 2L+B=2V-B
\]

edges, the forced size of such a path cover.

The colors split into four disjoint sectors.  Formula (4.3) enumerates all
(z)-containing lower colors by (T), and all (z)-containing upper colors
in the image of (\alpha).  Formula (4.4) enumerates all (z)-free upper
colors by (U), and all (z)-free lower colors in the image of
(\sigma).  Finally, the matching in (4.7), via (4.5), supplies each
missing (z)-free lower color and each missing (z)-containing upper color
once.  Injectivity and the residual matching show that no color is repeated.
□

The existence of (H) itself is not a problem: the four levels in (4.1)
have equal bipartition sizes, and the central-level Hamilton-cycle theorem
supplies such cycles.  The substantive new conditions are exactly the two
square-completion injections and the residual central matching.

## 5. The published lexical Hamilton cycle fails the bridge

Set (r=m-1) in the GJM middle-four-level construction.  Its contracted
lower lexical forest is precisely the family of lower outer two-paths used
in (4.3).  The symbolic collision from
`GJM_FOUR_LEVEL_AUDIT.md` applies to every pair of Dyck words (w,v) whose
semilengths sum to (r-2=m-3): the two lower words

```text
w 00010 v,          w 00001 v
```

give distinct contracted edges with the same square-completion/union color

```text
w 00111 v.
```

There are

\[
 \sum_{a+b=m-3}\operatorname {Cat}_a\operatorname {Cat}_b
 =\operatorname {Cat}_{m-2}
\tag{5.1}
\]

edge-disjoint collision pairs, with distinct common colors.  Hence
(\alpha) is not injective for every (m\geq3).

This obstruction survives the passage from the lexical cycle factor to the
published lexical Hamilton cycle.  The joining operation takes symmetric
differences with six-cycles lying entirely between the two **upper** levels;
the paper explicitly emphasizes that all modifications happen there.  The
lower outer paths, and therefore all collisions in (5.1), remain unchanged.
Thus the known lexical Hamilton cycle cannot instantiate Theorem 4.1.  A
different four-level Hamilton cycle, or a rewiring which changes a
Catalan-sized family of lower outer paths, is necessary.

## 6. Exact scope and remaining gate

Theorem 4.1 is a first-shadow/path-cover bridge, not a completed wreath
factor theorem.

1. Its (B) paths may have unequal lengths and arbitrary endpoint pairs.
   To reconstruct an odd-dimensional wreath factor by the distinguished-
   coordinate normal form, every component would have to be

   \[
    X_0,X_1,\ldots,X_m,qquad X_m=\overline{X_0}.
   \tag{6.1}
   \]

   The bridge does not force either condition.

2. Even if (6.1) were added, the two-sided edge colors cover the internal
   (z)-free first-shadow sector.  The (z)-containing first-shadow colors
   of the reconstructed odd wreaths are

   \[
    \{z\}\cup\bigl([2m]\setminus(Y_{i-1}\cup Y_i)\bigr),
    \qquad Y_i=X_i\cup X_{i+1},
   \tag{6.2}
   \]

   and their coverage is a further consecutive-pair condition, not a
   consequence of the individual meet/join rainbow property.

3. Nothing here controls depths (q\geq2).

The rigorous status after this audit is therefore:

* exact zero first-shadow defect exists at (m=4), so the canonical MSW
  holes are not universal;
* (t\to\infty) simultaneous rainbow coordinate cuts would prove the
  desired general (M_1=o(W)) estimate by (3.4)--(3.5);
* square-resolved four-level Hamilton cycles would give an exact two-sided
  Catalan path cover, a strong input toward such cuts; but
* the published GJM lexical Hamilton cycle provably fails the first square-
  completion injection by the Catalan-sized family (5.1).

The next honest theorem target is thus one of the following:

1. construct exact wreath factors with (t(m)\to\infty) rainbow cuts; or
2. construct a nonlexical four-level Hamilton cycle satisfying Theorem 4.1,
   then add complementary length-(m) endpoint control and the consecutive
   condition (6.2).

Neither target is a generic fixed-uniformity nibble statement.  Both are
exact, checkable structural conditions at the first shadow.
