# Independent audit of `LEX_FACTOR_ITERATION.md`

## 1. Verdict

The construction theorem is correct.  In particular:

* the regular erosion image in (3.5) and the exact deficit in (3.6) are
  correct;
* the pure-erosion obstruction is correctly scoped;
* the completed rank-shifted line word really covers every target satisfying
  the two-coordinate criterion;
* the slice fan covers every remaining target with nonzero entries; and
* the claimed (M_m+o(m^3)) length holds for every (q=o(m)).

There is one required quantitative repair.  Equation (3.7), as stated, is
not uniform over the advertised range because it fails at (q=0).  The
exact simplification is

\[
 D_q=(q+1)m^2-(q+1)^2m+\frac{q(q+1)(q+5)}6.          \tag{A.1}
\]

Thus a genuinely uniform version is, for example,

\[
 D_q=(q+1)m^2+O\bigl((q+1)^2m+(q+1)^3\bigr).         \tag{A.2}
\]

The original (O(q^2m+q^3)) remainder is valid when (q\ge1), but not when
(q=0): there (D_0=m^2-m), whereas the displayed formula would say
(D_0=m^2+O(0)).  This error does not affect Theorem 1 or its
(M_m+o(m^3)) corollary.

Two wording clarifications are also recommended:

1. the zero fixed-coordinate slice covers every **nonzero** slice target,
   not the global zero; and
2. what iterates is the regular line-fibre algebra.  The completed theorem
   reorders and enlarges those fibres, so it is not literally an iteration
   of the original global trail word from `LEX_THREE_LAYER_FACTOR.md`.

Neither clarification changes the theorem.

## 2. Regular core and erosion identities

For a regular colour (z), the first two positive coordinates are exactly
1 and 2, so its selected edge minimum is

\[
 b_z=z-e_1-e_2.
\]

This gives a bijection between regular colours and

\[
 C_0=\{x\in L_{2m-2}:x_1<m,\ x_2<m\}.
\]

After fixing ((x_3,x_4)=(c,d)), the remaining points form one consecutive
line

\[
 \beta_t=(t,K-t,c,d)
\]

over the legal integer range of (t).  Therefore

\[
 \bigwedge_{h=0}^q\beta_{t+h}=(t,K-t-q,c,d),
\]

and taking the maximum of consecutive eroded letters gives

\[
 \bigvee_{h=0}^s\gamma^{(q)}_{t+h}
   =(t+s,K-t-q,c,d).
\]

These are direct coordinate calculations; no unproved distributive
identity is being used.  Formula (3.4) follows by taking eroded starts from
(t-q) through (t), provided all involved original line points exist.

## 3. Exact erosion image and deficit

An eroded output has first coordinate at most (m-q-1), because the last
original point raises that coordinate by (q); the symmetric statement
holds for the second coordinate.  Conversely, if

\[
 x_1,x_2\le m-q-1,
\]

then

\[
 (x_1+h,x_2+q-h,x_3,x_4),\qquad 0\le h\le q,
\]

is a legal regular segment with coordinatewise minimum (x).  This proves
the equality in (3.5), not merely one inclusion.

For a point omitted because (x_1=m-q+j), the other coordinates sum to
(m-2-j), and hence give \(\binom{m-j}{2}\) choices.  The same applies to
(x_2).  If (x_1=m-i) and (x_2=m-j), the last two coordinates sum to
(i+j-q-2), giving ((i+j-q-1)_+) choices.  The upper box ceilings are
inactive throughout because (q\le m-2).  This verifies (3.6).

The two sums simplify as

\[
 2\sum_{j=0}^q\binom{m-q+j}{2}
   =2\sum_{h=0}^q\binom{m-h}{2},
\]

and

\[
 \sum_{i,j=0}^q(i+j-q-1)_+=\binom{q+1}{3}.
\]

Expanding gives (A.1), which both verifies the exact formula and exhibits
the defect in (3.7).

## 4. Pure-erosion obstruction

All literal erosion letters have rank

\[
 R=2m-q-2.
\]

If rank-(R) letters (x^{(1)},\ldots,x^{(h)}) have a maximum (y) of
rank (R), then every (x^{(j)}\le y) coordinatewise.  Equality of their
coordinate sums forces (x^{(j)}=y) for every (j).  Hence a missing
rank-(R) point cannot be synthesized by an interval of other erosion
letters.  This proves exactly the stated no-go for the pure (C_q) word;
it says nothing against the subsequent fibre completion or a variable-rank
factor.

## 5. Completed line spine

For fixed ((c,d)), equations (4.1)--(4.2) list every solution of

\[
 x_1+x_2=R-c-d,qquad 0\le x_1,x_2\le m,
\]

once and in increasing (x_1)-order.  The blocks over distinct ((c,d))
are disjoint, so (W_R) is a permutation of (L_R).  Since
(q\le m-2), one has (R\ge m>0), and every letter is nonzero.

If (y\in L_{R+s}) and (y_1,y_2\ge s), then

\[
 y-se_1, y-se_2\in L_R
\]

are the endpoints of one contiguous block segment.  Its intermediate
points are

\[
 (y_1-s+h,y_2-h,y_3,y_4),\qquad 0\le h\le s,
\]

and their maximum is (y).  This verifies Lemma 3, including (s=0) and
the endpoint case (s=m).  Symmetry and unimodality of the four equal
chains give (|L_R|\le |L_{2m}|=M_m).

## 6. Slice completion and the nonzero issue

The audited hook construction for a three-chain box gives a nonzero word
for ([0,m]^3) of length

\[
 H_m=(m+1)(2m+1)-1.
\]

Embed it in the slice (x_i=a).

* If (a=0), all embedded letters are nonzero and all nonzero local
  targets are covered.  The omitted local origin is the omitted global
  zero and must not be inserted.
* If (a>0) and the whole slice is desired, insert the literal slice
  origin.  It is globally nonzero, and the resulting length is
  (H_m+1=(m+1)(2m+1)=G_m).

For Theorem 1, even the positive slice origins are unnecessary.  Indeed,
every requested target in a used slice has rank at least (R), whereas
(a\le q+1), and

\[
 R-a\ge 2m-2q-3\ge1.
\]

Thus its other three coordinates are not all zero.  One could consequently
replace every (G_m) in (1.3) by (G_m-1).  The stated, slightly looser,
bound remains correct and has the advantage that each positive slice block
covers its entire slice.

For a target of excess (s\le q+2), failure of the line condition means
that one of (y_1,y_2) equals an integer

\[
 a<s\le q+2,
\]

so (a\in\{0,\ldots,q+1\}).  The corresponding appended slice word gives
an internal witness.  No witness has to cross a concatenation seam.

There are (2(q+2)) slice blocks, and hence the claimed length is valid.
Since (G_m=\Theta(m^2)), the excess is

\[
 O((q+1)m^2)=o(m^3)
\]

whenever (q=o(m)).  This includes bounded (q), including (q=0).

## 7. Audit of the supplied checker

`scratch/verify_lex_factor_iteration.py` correctly checks, for its tested
finite range:

* the erosion rank;
* equation (3.3) on every legal regular line window;
* equality of the computed erosion image with (3.5);
* the exact inclusion-exclusion formula (3.6); and
* the exhaustive line-or-slice dichotomy for every target in the band.

The checker intentionally does not build the three-chain hook word.  It
also does not test the asymptotic statement (3.7), so it cannot detect the
(q=0) error above.  These are limitations of coverage, not errors in its
implemented checks.

As an additional independent test, I generated the actual hook words,
embedded all positive and zero slices with the correct origin treatment,
concatenated them after (W_R), and enumerated all contiguous maxima.  Every
required band target was covered for every admissible pair

\[
 2\le m\le5,qquad 0\le q\le m-2.
\]

The generated words contained no zero entry.  This directly checks the
construction step which the supplied verifier deliberately abstracts away.

## 8. Required and recommended edits

**Required:** replace (3.7) by (A.1), or by the uniform estimate (A.2).

**Recommended:** state explicitly in Section 5 that the (a=0) block omits
the global zero, and that all band targets in every used slice have a
nonzero local part.  Also replace the unqualified phrase “the
edge-minimum construction really does iterate” by “the regular line-fibre
algebra of the edge-minimum construction iterates.”  The global theorem
uses a reordered, surface-completed line spine and should not be read as a
factorization of the original lexicographic trail order.

With those changes, the note is mathematically sound.
