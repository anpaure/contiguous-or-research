# Small-fixture audit for block-coherent Catalan/Pascal recursion

Date: 2026-07-31  
Status: exact, solver-free audit of the authenticated \(m=2,3\) fixtures;
scoped obstruction to one-coordinate simultaneous Pascal squares, not to
arbitrary rethreading

## 1. The inverse-square test

Let \(C\) be the canonical lower tight enumeration obtained from a cap-two
middle cycle \(P\) and a common lower/upper edge transversal \(T\): subdivide
the edges of \(T\) by their lower intersections and leave the other
\(K=\operatorname {Cat}_m\) middle edges direct.

Fix a proposed new coordinate \(z\).  A Pascal switch has the form

\[
 b0-x0, a1-b1
   \longmapsto
 b0-b1, x0-a1,
 \qquad x=a\cup b.
 \tag{1.1}
\]

Consequently, if \(C\) is the output of simultaneous switches at all \(K\)
direct child edges, then all of the following are necessary.

1. Every one of the \(K\) direct edges of \(C\) crosses \(z\).
2. Exactly \(K\) cube edges of \(C\) cross \(z\); they have the vertical form
   \(b0-b1\).
3. Form a bipartite occurrence graph between the direct edges \(x0-a1\) and
   the vertical edges \(b0-b1\), joining them exactly when \(x=a\cup b\).
   This graph has a perfect matching.

The third condition is literal: two switches cannot reuse one vertical
occurrence.  If the matching exists, inverse switching is still subject to
the stronger requirement that the restored edges form the two prescribed
sector cycles.  Thus failure of any of 1--3 is a proof-safe obstruction,
while passing them is not by itself a construction.

In the audited fixtures the common transversal is unique, so the direct-edge
bank used in this test is not a discretionary choice.

## 2. Complete \(m=2\) result

Fixing the first rank-three upper set leaves all \(3!=6\) rooted saturating
cycles.  Each has four common-refinement decorations, for 24 fixtures in
total.  Every one has the following exact properties.

* Its middle projection is one Hamilton cycle on the six rank-two sets, with
  degree histogram \(2^6\).
* Its upper load profile is \(1^2 2^2\).  In both doubled upper blocks the two
  occurrences are consecutive physical edges and share the inserted middle
  set.  Thus these are literal cap-two blocks, not merely equal labels.
* Its full colour-incidence graph is two balanced paths of three edges each.
  It has one perfect matching and is leaf-peelable.
* Its base lower word has profile \(1^4\), with no duplicate and no hole.
  Therefore it has no \(K\times K\times K\) floor repair core.  Its four
  solutions are all mixed-orientation; neither uniform direction occurs.

For each of the 24 fixtures exactly two coordinates pass conditions 1 and 2
of Section 1.  This gives 48 candidate split rows.  In every row the two
direct occurrences each have one compatible vertical occurrence, but it is
the **same** vertical occurrence for both.  The square-atlas matching number
is therefore

\[
                         1<K=2.                         \tag{2.1}
\]

Hence none of the 24 authenticated \(m=2\) common refinements is the output
of an all-\(K\) simultaneous Pascal-square splice across any coordinate.
This is a Hall obstruction internal to the enlarged two-square architecture,
strictly stronger on these fixtures than the published one-port count.

For example, for upper order

\[
                         7,11,13,14
\]

and the first solution, the direct middle edges are \(6-5\) and \(10-9\).
For \(z=0\), both require the vertical row \(2-3\), while the other available
vertical row is \(8-9\).  Thus the two left vertices have the identical
singleton neighbourhood.

## 3. Complete listed-\(m=3\) result

### 3.1 Positive directed fixture

For upper cycle

\[
60,53,23,15,29,30,54,46,43,45,39,51,58,27,57,
\]

the unique repair is uniformly outgoing.  Its five hosted blocks are

\[
 (i,X)=(1,49),(2,19),(7,14),(9,44),(13,11).
\]

The replay proves:

* one physical Johnson Hamilton cycle on all 20 rank-three sets, with degree
  histogram \(2^{20}\);
* upper profile \(1^{10}2^5\), with all five doubled labels realized by two
  consecutive edges sharing exactly \(X\);
* lower profile \(1^{10}2^5\);
* a full colour-incidence forest with component edge lengths
  
  \[
                         1^7,3^1,5^2,
  \]
  
  one perfect matching, and determinant \(-1\).

Its floor repair core has the seven occurrence-labelled edges

\[
\begin{array}{c|c|c|c}
X&D&Z&i\\ \hline
11&5&9&3\\
11&24&9&13\\
14&34&10&7\\
19&5&3&2\\
19&24&17&13\\
44&33&36&9\\
49&20&17&1.
\end{array}
\]

Every row is a literal Boolean repair diamond.  Degree-one peeling forces,
for example,

\[
(14,34,10), (44,33,36), (49,20,17),
(19,5,3), (11,24,9).
\tag{3.1}
\]

Thus this fixture is a genuine positive calibration for block contiguity,
physical degree two, and a leaf-peelable \(K=5\) repair core.

It is **not** a positive calibration for the proposed Pascal recursion.  The
numbers of direct edges crossing coordinates \(0,\ldots,5\) are

\[
                         3,1,3,1,1,1.                   \tag{3.2}
\]

Every coordinate has exactly five vertical cube edges, but no coordinate
has all five direct edges crossing it.  Condition 1 of Section 1 therefore
fails before the square atlas or sector topology is considered.

### 3.2 Mixed directed fixture

The authenticated mixed fixture is also one physical degree-\(2^{20}\)
Hamilton cycle with five literal contiguous double blocks.  Its full
colour-incidence graph is a balanced forest with edge lengths

\[
                            1^5,3^5
\]

and determinant \(+1\), hence its common transversal is unique and
leaf-peelable.  Its forced block signs are mixed, so it is not a uniform
directed repair.  Its base profile is not the floor core profile.  Its direct
crossing counts are

\[
                         3,1,1,1,3,1,                   \tag{3.3}
\]

again excluding every one-coordinate all-\(K\) Pascal decomposition.

### 3.3 Vendored GMM \(m=3\) fixture

The vendored GMM cycle has 165 injective host maps and 5,280
host/orientation decorations, but zero common transversals.  Its base profile
is \(0^4 1^7 2^4\), not the zero-slack \(0^5 1^5 2^5\) profile.  It therefore
does not calibrate block-coherent recursion either.

## 4. Reconciliation with the abstract colour forest

The abstract BTK-plus-cycle-broken-matching construction is correctly a
balanced colour forest with determinant \(\pm1\), but the small replay shows
why this does not settle the physical problem.

* At \(m=2\) its doubled upper rows are locally compatible, yet its Johnson
  lift has degree histogram \(1^1 2^4 3^1\), not \(2^6\).
* At \(m=3\) its Johnson lift has degree histogram \(1^5 2^{10}3^5\), two
  components, and two noncontiguous doubled-upper rows:

  \[
                       (U;L_0,L_1)=(27;9,18),(54;18,36).
  \tag{4.1}
  \]

  In each row the two lifted Johnson edges have no common middle endpoint.

Thus the exact hierarchy of gates is strict:

\[
\begin{split}
&\text{abstract squarefree palettes / balanced incidence forest}\\
&\not\Rightarrow\text{local cap-two endpoint sharing}\\
&\not\Rightarrow\text{spanning physical Johnson degree two}\\
&\not\Rightarrow\text{one cycle}\\
&\not\Rightarrow\text{uniform directed sign}\\
&\not\Rightarrow\text{one-coordinate all-}K\text{ Pascal ancestry}.
\end{split}
\tag{4.2}
\]

The Boolean-square ear ledger remains a valid abstract and local tool.  The
finite fixtures show that its ears must additionally be assembled into a
block-coherent, occurrence-disjoint Pascal atlas and then into one physical
cycle.  None of the authenticated \(m=2,3\) positive endpoint fixtures
supplies that recursive ancestry.

## 5. Scope and artifacts

The inverse-square no-go is confined to the literal simultaneous local
switch (1.1) and its canonical lower-tight decoration.  It does not rule out
a bulk rethreading which temporarily changes the direct bank or uses a larger
multi-coordinate gadget.

Artifacts:

* `scratch/audit_k_gmm_block_contiguity_m2_m3_20260731.py`, SHA-256
  `b91a1f0bba0c9fc639b310355e4860d39419cba5b99a5833abb0f379e7ad58c2`;
* `scratch/k_gmm_block_contiguity_m2_m3_20260731.audit.json`, SHA-256
  `638a00fd583984473d07ffd635769cd4f7d277d9f6a3579e20759313d49744f6`,
  canonical payload
  `b94274c26512c54e6a1eb5240acdc78595040a0827ad07e17a4ff4b728150393`.

The JSON binds every source fixture and prior audit by SHA-256 and contains
the occurrence-level rows for all 24 \(m=2\) solutions and both authenticated
common-refinement \(m=3\) fixtures.
