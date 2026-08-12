# Hall 25 is not a compound minimum: an audited six-cut odd-turn portal reaches Hall 24

Date: 2026-07-28

Status: explicit exact candidate, independently reconstructed and audited.
It preserves the middle deck, depth-three residence, every upper support
through depth seven, and the complete lower support vector, while lowering
the depth-three compiler deficiency from \(25\) to \(24\).  It does not
solve the prefix-hole corridor or the one-common-word target assignment.

## 0. Exact result

Starting from `scratch/k15_segment_braid_hall25.json`, apply

\[
\operatorname{FR}(1512,2458,4103)
\quad\text{and then}\quad
\operatorname{FR}(2664,3491,6201).                        \tag{0.1}
\]

The exact score sequence is

\[
                         25\longrightarrow25\longrightarrow24.       \tag{0.2}
\]

The first braid is a plateau portal: it destroys the old canonical
defect-\(25\) shore but exposes another defect-\(25\) shore.  The second
opens that shore.  Thus the exhaustive one-move local minimum at Hall 25
is genuine but not a compound minimum.

The two sequential braids are equivalently one six-cut, seven-segment
reassembly of the original Hall-25 path.  Its port symmetric difference is
the disjoint union of two alternating \(C_6\)'s.  In rank-\((7,9)\)
odd-turn coordinates it preserves every lower turn centre exactly, changes
three upper turn colours after a three-colour transport, and retains all
upper supports.

## 1. Frozen artifacts and independent audit

The exact files are:

- `scratch/k15_segment_braid_hall25.json`;
- `scratch/k15_segment_braid_hall25_portal.json`;
- `scratch/k15_segment_braid_hall24.json`;
- `scratch/k15_segment_braid_hall24_portal_audit.json`.

Their SHA-256 values, in the last three cases, are

```text
83678f3fb928402b3e01f3de0553be0f1a60b30a50ee51d7979b8517abd99701
49eb1060ccbe86f056295f0b96fe409f275737b8b759f5b7ca0ee2fa7ca0416e
0c381981f90e7c7e251228d75593165534bc60a9b8f0bbae83fef247e1bbcdf1
```

The portal and Hall-24 comma-separated middle-path digests are

```text
be4674ab73f013d6ad7db2e424d670e291b3382e8aefa7f3b2ab2fc743a620b3
96e7640ebcf8e4c3e372e0e4654b7a7c3934ed5d38be2d13c1371a04eabc49f5
```

Running the independent reconstruction verifier as

```sh
python3 scratch/audit_k15_segment_braid_descent.py \
  --base scratch/k15_segment_braid_hall25.json \
  --step scratch/k15_segment_braid_hall25_portal.json \
  --step scratch/k15_segment_braid_hall24.json
```

returns `PASS` and independently obtains

\[
\begin{array}{c|ccc}
&H25&H25^{\rm portal}&H24\\ \hline
\text{matching}&16358&16358&16359\\
\text{deficiency}&25&25&24\\
\text{zero-candidate targets}&7&7&7.
\end{array}                                                \tag{1.1}
\]

The verifier does not trust the embedded Hall summaries: it rematerializes
both braids, rebuilds the maximal erosion, every compiler incidence, the
maximum matchings, all lower and upper consecutive-window supports, the DM
shores, and residence.

## 2. One literal six-cut chronology

Let \(T\) be the Hall-25 middle path and define the seven half-open retained
segments

\[
\begin{array}{c|c|c}
i&X_i&|X_i|\\ \hline
0&T[0:1512]&1512\\
1&T[1512:2125]&613\\
2&T[2125:2458]&333\\
3&T[2458:3610]&1152\\
4&T[3610:4104]&494\\
5&T[4104:6202]&2098\\
6&T[6202:6435]&233.
\end{array}                                                \tag{2.1}
\]

### Theorem 2.1 (composition normal form)

The final Hall-24 chronology is exactly

\[
\boxed{
T^{(24)}
=X_0\,X_3\,\overleftarrow{X_1}\,X_5\,X_2\,
 \overleftarrow{X_4}\,X_6.}                               \tag{2.2}
\]

Consequently it is one integral six-cut segment braid of one common
physical middle word, not two independent rankwise choices.

#### Proof

The first move in (0.1) gives

\[
T^{(1)}
=X_0\,X_3\,X_4\,\overleftarrow{X_2}\,
 \overleftarrow{X_1}\,X_5\,X_6.                          \tag{2.3}
\]

In \(T^{(1)}\), the second move's cut positions \(2664,3491,6202\)
fall exactly after \(X_3,\overleftarrow{X_2},X_5\).  Its four pieces are

\[
A=X_0X_3,\quad
B=X_4\overleftarrow{X_2},\quad
C=\overleftarrow{X_1}X_5,\quad
D=X_6.
\]

The `FR` rule is \(ABCD\mapsto AC\overleftarrow B D\).  Since
\(\overleftarrow{X_4\overleftarrow{X_2}}
=X_2\overleftarrow{X_4}\), equation (2.2) follows.  Direct comparison with
the frozen Hall-24 array agrees at all \(6435\) positions.  \(\square\)

## 3. Alternating port circuits

Write \(L_i,R_i\) for the original left and right ports of \(X_i\).
The old seam matching is

\[
\begin{aligned}
M^-=\{&
R_0L_1,R_1L_2,R_2L_3,\\
&R_3L_4,R_4L_5,R_5L_6\},
\end{aligned}                                             \tag{3.1}
\]

while (2.2) has

\[
\begin{aligned}
M^+=\{&
R_0L_3,R_3R_1,L_1L_5,\\
&R_5L_2,R_2R_4,L_4L_6\}.
\end{aligned}                                             \tag{3.2}
\]

### Proposition 3.1

The port symmetric difference \(M^-\triangle M^+\) is exactly the two
alternating circuits

\[
R_0-L_1-L_5-R_4-R_2-L_3-R_0,                              \tag{3.3}
\]

\[
R_1-L_2-R_5-L_6-L_4-R_3-R_1,                              \tag{3.4}
\]

where edges alternate old and new.

#### Proof

Every displayed port has one old and one new incident seam.  Following
these alternately gives (3.3)--(3.4), which exhaust the twelve ports.
\(\square\)

This is the exact PBBS-style multi-collar circulation underlying the
plateau escape.  Port balance alone would not have sufficed; the explicit
order (2.2) proves the one-path topology.

## 4. Odd-turn seam table

For a Johnson edge \(XY\), put

\[
L(XY)=X\cap Y,\qquad U(XY)=X\cup Y.                        \tag{4.1}
\]

The six old and new seams of the direct H25-to-H24 compound are

\[
\begin{array}{c|c|c|c}
&\text{edge}&L&U\\ \hline
\text{old}&3029-3045&3013&3061\\
&21845-21621&21589&21877\\
&2005-4037&1989&4053\\
&20823-20829&20821&20831\\
&2021-1013&997&2037\\
&21597-21085&20573&22109\\ \hline
\text{new}&3029-4037&3013&4053\\
&20823-21845&20821&21847\\
&3045-1013&997&3061\\
&21597-21621&21589&21629\\
&2005-2021&1989&2037\\
&20829-21085&20573&21341.
\end{array}                                                \tag{4.2}
\]

Every new pair is a Johnson edge.  The lower rows are fixed pointwise as a
multiset:

\[
\{3013,21589,1989,20821,997,20573\}.                       \tag{4.3}
\]

The upper columns satisfy

\[
\begin{aligned}
\text{transported common columns}&=\{3061,4053,2037\},\\
\text{lost columns}&=\{21877,20831,22109\},\\
\text{gained columns}&=\{21847,21629,21341\}.
\end{aligned}                                             \tag{4.4}
\]

Thus the immediate lower multiset is exact.  The immediate upper multiset
is not exact, but all three lost upper colours have other witnesses, so
upper support remains complete.  By Lemma 2.1 of the companion strong-\(C_8\)
note, each row-column pair in (4.2) is one complete turn in \(O_7\).
Equation (4.2) therefore gives an explicit odd-turn transport, not merely a
support count.

This compound is not the common-core strong \(C_8\) of
`THREAD_R_K15_HALL25_STRONG_C8_FIVE_SEGMENT_BRAID_20260728.md`:
its port boundary is two \(C_6\)'s and its upper flag boundary is nonzero.

## 5. All shadows and residence

Direct comparison of H25 with H24 gives:

\[
\begin{array}{c|c|c|c|c}
q&
\text{lower holes}&\|\Delta_q^-\|_1&
\text{upper holes}&\|\Delta_q^+\|_1\\ \hline
1&4&0&0&6\\
2&19&4&0&9\\
3&4&8&0&15\\
4&1&14&0&14\\
5&0&17&0&16\\
6&0&16&0&4\\
7&0&8&0&4.
\end{array}                                                \tag{5.1}
\]

There is no lost or gained support at any displayed depth.  In particular,
every rank-\((8+q)\) upper target remains represented for
\(q=1,\ldots,7\).  Equation (5.1) states support and multiplicity separately:
only lower \(q=1\) is multiset-exact.

The independent run audit finds no internally bounded coordinate run of
length at most three in either intermediate or final path.  Hence both
braids are depth-three resident.  The compiler reconstruction also passes
the central carrier test at every owner-coordinate pair, so the final
maximal erosion is one common controller of the final middle chronology.

These statements do not mean that a final injective lower target assignment
has already been lifted to one literal OR word.

## 6. Exact DM-shore motion and Hall gain

Let \(G_0,G_1,G_2\) be the compiler graphs of H25, the portal, and H24, and
let \(S_0,S_1,S_2\) be their canonical alternating-reachable shores.  Their
cross-gap matrix is

\[
\left(|S_j|-|N_{G_i}(S_j)|\right)_{i,j=0}^2
=
\begin{pmatrix}
25&24&23\\
22&25&24\\
21&24&24
\end{pmatrix}.                                             \tag{6.1}
\]

Thus the first braid gives current \(+3\) on the old critical shore, but
the new shore \(S_1\) has defect \(25\).  The second lowers every defect to
at most \(24\).  This is precisely the DM-shore-changing behavior requested:
a fixed-shore greedy rule would miss it.

Cancelling complete target-neighbourhood profiles directly between H25 and
H24 gives

\[
|H|=19253,\qquad |B^-|=|B^+|=58,\qquad \nu(H)=16323,       \tag{6.2}
\]

and contracted boundary capacities

\[
\operatorname{cap}_H(B^-)=35,\qquad
\operatorname{cap}_H(B^+)=36.                             \tag{6.3}
\]

Therefore

\[
\nu(G_2)=16323+36=16359
          >16323+35=\nu(G_0),                             \tag{6.4}
\]

which is the exact one-unit compiler gain.  The two individual profile
exchanges have sizes \(18\) and \(40\); direct cancellation of the compound
is essential and leaves \(58\) profiles on each side.

Since \(h(G_2)=24\), every H25 shore \(X\) of defect \(25\) satisfies

\[
|N_{G_2}(X)|-|N_{G_0}(X)|\ge1.                            \tag{6.5}
\]

The seven zero-candidate targets and target \(6308\)'s degree \(14\) are
unchanged.  The gain is collision-capacity transport, not creation of a
candidate for a zero row.

## 7. Exact scope

This is an explicit audited answer to the Hall-25 local-minimum problem:
bounded correlated segment rethreading succeeds even though every single
resident upper-safe three-cut move is nonimproving.

It does not prove the \(k=15\) conjecture.  The Hall-24 endpoint still has

\[
(h_1,h_2)=(4,19),
\]

where a final flat-middle optimum needs \(h_1\le2\) and
\(h_2\le h_1+3\le5\).  It also retains all seven zero-candidate targets.
Finally, Hall matching is only the outer SDR.  The selected target/cell
assignment must still satisfy the simultaneous one-common-word interval
conditions.

The proved conclusion is therefore:

\[
\boxed{\text{Hall 25 is a one-braid local minimum but not a compound
minimum; the explicit six-cut odd-turn portal reaches Hall 24.}}
\]
