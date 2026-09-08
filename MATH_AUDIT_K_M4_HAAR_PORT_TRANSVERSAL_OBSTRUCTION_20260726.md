# Independent audit of the rank-four Haar port-transversal obstruction

Date: 2026-07-26

Audited source:
`MATH_ATTACK_K_M4_HAAR_PORT_TRANSVERSAL_OBSTRUCTION_20260726.md`.

## 0. Verdict

The obstruction is correct for both completed factors in
`NONLOCAL_HAAR_M4.md`.

The proof uses the corrected interface from Section 17 of
`MATH_AUDIT_PLATEAU_TRUNCATION_20260726.md`: ordinary
\(\mathcal D_4\)-transversality is not sufficient; the selected boundary
set must be one of the two core windows adjacent to infinity.

All choices of infinity and all label relabelings are exhausted.  The two
surviving coarse separator frames fail an invariant necessary condition,
namely the point-degree multiset of a canonical \(\mathcal D_4\) family.
Rooting and reversal introduce no omitted freedom.

## 1. Audit of the canonical invariant

For an ordered core \(x_1,\ldots,x_8\), a Dyck four-subset has ordered
positions \(i_j\le2j-1\).  Hence it contains \(x_1\), avoids \(x_8\), and
after grouping

\[
 E_1=\{x_2,x_3\},\quad E_2=\{x_4,x_5\},\quad
 E_3=\{x_6,x_7\},
\]

its other three points have types \(111,120,201,210\).  Direct incidence
counting gives degrees

\[
 14;\quad9,9;\quad7,7;\quad5,5;\quad0;\quad0,
\]

where the last zero is infinity.  This independently verifies the target
multiset

\[
                         (14,9,9,7,7,5,5,0,0).             \tag{1.1}
\]

No assumption about the internal order of the three pairs enters this
count.

The stronger rigidity statement is also correct.  After deleting the
universal point, the complementary six triples have degrees
\(5,5,3,3,1,1\).  The two degree-five vertices miss distinct edges, so the
four edges containing both are all four possible triples through their
pair.  The remaining two edges must both use the degree-three pair.  This
uniquely recovers the canonical forbidden family.  Thus, under the forced
universal and zero labels, the degree test is sufficient as well as
necessary at \(r=4\).

## 2. Audit of the port reduction

For a displayed omitted-label row \(q\), the physical cycle is

\[
                         p_j=q_{2j\bmod9}.                  \tag{2.1}
\]

Thus the four successors and four predecessors of infinity in \(p\) are
exactly its two core ports.  If \(a=x_1\) and \(b=x_8\), every canonical
boundary contains \(a\) and avoids \(b,\infty\).  Therefore every row must
place \(a,b\) on opposite port sides, and the selected port is forced to be
the side containing \(a\).

This proves that complementary row-signatures are necessary.  Because the
factor is exact, the fourteen forced ports are distinct.  Hence, were the
factor port-transversal, these fourteen sets would have to equal the entire
fourteen-set Dyck family.  Comparing their degree multiset with (1.1) is
therefore legitimate.

Rotation preserves the unordered port pair.  Reversal swaps its two sides;
that is exactly the already-audited interchange of \(a,b\).  Relabeling
only permutes point degrees.

## 3. Audit of exhaustive separator reduction

The six-bit table in the source was re-read directly from the first six
common physical cycles.  Its complementary pairs are exactly

\[
\begin{array}{c|ccccccccc}
\infty&1&2&3&4&5&6&7&8&9\\ \hline
\{a,b\}&-&59&69&16&-&78&89&57&58.
\end{array}                                                \tag{3.1}
\]

There cannot be an additional candidate: for fixed infinity every possible
ordered choice of the universal and terminal labels is an unordered pair
in (3.1), with its two orientations audited later.

The physical cycles

\[
 p(C_7)=(1,6,5,2,4,8,7,9,3),\qquad
 p(C_8)=(1,7,4,5,6,8,9,2,3)
\]

eliminate respectively the \(16\) candidate and the \(59,69,57,58\)
candidates.  The pairs \((6,78)\) and \((7,89)\) remain separated through
the other common rows and through both four-row trade sides.  This confirms
that the same two coarse frames, and no others, must be tested for both
completed factors.

## 4. Audit of the degree obstruction

For \((\infty,a,b)=(6,7,8)\), the forced port family is the same on both
trade sides.  Its degree vector is

\[
                         (6,7,6,7,7,0,14,0,9),             \tag{4.1}
\]

so its sorted multiset is

\[
                         (14,9,7,7,7,6,6,0,0).             \tag{4.2}
\]

Complementing every port in the eight-point core gives

\[
                         (14,8,8,7,7,7,5,0,0).             \tag{4.3}
\]

For \((\infty,a,b)=(7,8,9)\), the residual degree vectors on labels
\(1,\ldots,6\) are

\[
 (7,8,5,8,5,9)\quad(F^-),\qquad
 (8,7,5,8,5,9)\quad(F^+).                                 \tag{4.4}
\]

They have the same sorted multiset, so both full families have

\[
                         (14,9,8,8,7,5,5,0,0).             \tag{4.5}
\]

Their complementary orientations both have

\[
                         (14,9,9,7,6,6,5,0,0).             \tag{4.6}
\]

Each of (4.2), (4.3), (4.5), and (4.6) differs from (1.1).  The mismatch is
not an ordering artifact: a multiset is being compared with a multiset.
This independently verifies the no-go theorem.

## 5. Audit of the ordinary-transversal caveat

The positive factor's claimed ordinary frame has

\[
 (x_1,\ldots,x_8)=(1,8,9,2,3,5,7,4),\qquad\infty=6.
\]

Its fourteen listed sets occur once each in the fourteen owner rows, so the
ordinary transversal statement is correct.  But in common row \(C_2\) the
selected set is 1358, while the two 6-ports are 2358 and 1479.  Hence the
selected set is interior.  If the two zero-degree labels are exchanged, in
common row \(C_7\) the selected set is 1379, while the two 4-ports are 1256
and 3789.  This independently confirms that the explicit ordinary
transversal cannot be promoted merely by choosing the other zero-degree
label as infinity.

## 6. Scope audit

The proved conclusion is exactly:

> Neither finished rank-four Haar factor can be inserted unchanged into a
> canonical aligned hole through the corrected port-transversal
> context-substitution theorem, under any relabeling, infinity choice, or
> row rooting/reversal.

The proof does not exclude a different rank-four factor, an auxiliary-path
port correction, a parent-context construction, or a state-level suspension
which changes the local completion.  It also leaves the certified
unrooted identities \(B_4w=B_3w=0\), \(B_2w\ne0\) untouched.  These caveats
are necessary and are stated correctly in the source report.
