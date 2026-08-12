# Audit of `LEX_FACTOR_ITERATION.md`

## 1. Claims audited

The note makes four mathematical claims.

1. The regular lexicographic minima are coordinate-\(\{1,2\}\) lines.
2. Their repeated erosion has formulas (3.2)--(3.6).
3. The completed rank-\(R\) line spine has the exact witness equation in
   Lemma 3.
4. Appending the stated slice fan covers the whole band and has the length
   in Theorem 1.
5. The same proof with a shifted base gives the symmetric-band corollary.

Each is checked below independently of the heuristic discussion in the
last section.

## 2. Erosion algebra

On a line \(\beta_t=(t,K-t,c,d)\), the minimum of
\(\beta_t,\ldots,\beta_{t+q}\) takes its first coordinate at the left end,
its second coordinate at the right end, and leaves the last two coordinates
fixed.  This gives

\[
 (t,K-t-q,c,d).
\]

The maximum of the consecutive eroded letters starting at \(t\) and ending
at \(t+s\) takes its first coordinate at the right end and its second at
the left end.  This gives (3.3).  No distributive-lattice identity is being
assumed beyond this explicit coordinate calculation.

The regular-line bounds are also two-sided.  Existence of all \(q+1\)
original letters forces both output coordinates at most \(m-q-1\), and
those inequalities construct the preimage segment.  Hence (3.5) is an
equality, not only an inclusion.

## 3. Deficit count

At rank \(2m-q-2\), fixing \(x_1=m-q+j\), \(0\le j\le q\), leaves three
coordinates summing to \(m-2-j<m\).  Their box ceilings are inactive, so
the count is \(\binom{m-j}{2}\).  Reindexing gives the first term of
(3.6).

For the intersection, write \(x_1=m-i,x_2=m-j\).  The final two
coordinates sum to \(i+j-q-2\), and the number of nonnegative solutions is
\((i+j-q-1)_+\).  Their ceilings are again inactive for \(q\le m-2\).
This verifies inclusion-exclusion and the exact formula.

The overlap sum is \(\binom{q+1}{3}\), and expansion gives the exact
polynomial (3.7).  In particular the uniform error term must contain
\(q+1\): at \(q=0\), the defect is already \(m^2-m\).

The scoped impossibility statement uses equal ranks correctly: if
\(x^{(1)},\ldots,x^{(h)}\) all have rank \(R\) and their coordinatewise
maximum also has rank \(R\), then every \(x^{(j)}\) equals that maximum.
Thus a missing rank-\(R\) letter cannot be synthesized from distinct
rank-\(R\) erosion letters.

## 4. Completed line spine

For fixed \((c,d)\), equations (4.1)--(4.2) enumerate every legal solution
of \(x_1+x_2=R-c-d\) exactly once.  Different fixed pairs give disjoint
blocks, so the concatenation is a permutation of \(L_R\).

For \(y\in L_{R+s}\), both endpoints in (4.4) are legal precisely under
the stated inequalities \(y_1,y_2\ge s\).  Every intermediate line point
lies in the same block, and the coordinatewise maximum calculation is
exact.  Cross-block intervals are irrelevant and cannot destroy these
internal witnesses.

## 5. Slice fan and length

If Lemma 3 fails for a target at excess \(s\), one of its first two
coordinates is an integer in \([0,s-1]\subseteq[0,q+1]\).  Exactly one of
the appended full-slice words therefore covers it.  The proof does not
assume that the slice witnesses interact safely with neighbouring blocks;
each witness stays inside its own appended block.

There are \(2(q+2)\) such blocks, each of length at most
\((m+1)(2m+1)\).  The rank layer \(L_R\) has size at most the central rank
layer by symmetry and unimodality of the product of four equal chains.
This proves the displayed length without hidden seam padding.

For Corollary 4, the maximum excess is \(2q\), so the low-coordinate values
are exactly among \(0,\ldots,2q-1\).  The hypothesis \(2q\le m\) keeps
these as legal distinct slice values.  Hence the count is \(4q\) blocks,
and the same witness calculation applies without a new assumption.

## 6. Scope guardrails

- The theorem covers a lower-central band, not the whole four-box lattice.
- It proves a lower-order excess only for \(q=o(m)\).
- The completed line spine is a reordered enlargement of the regular lex
  fibres, not the untouched original transition-trail word.
- The exact deficit is for the regular coordinate-line erosion.  It is not
  asserted to be an obstruction to arbitrary variable-rank words.
- The multiscale fan fusion in Section 6 is a proposed next target, not a
  proved construction.
- Formula (7.3) is a direct suffix/prefix calculation.  The subsequent
  seam-rectangle tiling is explicitly conjectural; raw rectangle capacity
  is not being treated as a coverage theorem.
- No claim here resolves the original all-\(k\) exact formula.
