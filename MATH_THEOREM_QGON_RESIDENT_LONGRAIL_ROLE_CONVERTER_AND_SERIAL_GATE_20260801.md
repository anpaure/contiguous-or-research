# Resident long-rail role conversion for every q-gon port

Date: 2026-08-01

Status: unconditional all-depth resident four-state role-conversion macro,
with exact resource, tail/head, topology, and serial-state ledgers.  All
four states have the same number of atoms and the same complete immediate
resource inventories.  Arbitrary-width interval ORs inside each rail are
preserved exactly, and the two endpoint states are global reversals.
Upper transparency across each q-gon toggle, ambient one-copy reservation,
and the common compiler remain open.

This note is an independent derivation of the same four-state construction
now frozen more completely in
MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md.  The latter
is authoritative for the retained-anchor/nonempty-antecedent statement and
the individual q-gon deeper-OR counteraudit.

## 0. Outcome

The depth-two square return can be stretched to a resident rail of length
\(2d+1\) at every q-gon port.  One common ordered \(d\)-set inside the
q-gon core and one common ordered \(d\)-set outside the q-gon support
suffice for all ports.

Under

\[
                         d\le m-2,\qquad q+d\le m+1,         \tag{0.1}
\]

the rails have pairwise distinct internal roots, lower colours, and
owners, and all of those resources avoid the original q-gon resources.
The two rail orientations have:

* identical complete root, immediate-lower, and immediate-upper palettes;
* strict depth-\(d\) residence internally, with only clipped endpoint
  runs;
* one head--owner alternating return path; and
* two tail--head parity return paths.

For the rolling-reset choice

\[
                              q=2(d+1),                     \tag{0.2}
\]

the coordinate condition (0.1) is

\[
                              m\ge3d+1.                     \tag{0.3}
\]

Since \(d=\Theta(\sqrt m)\), this holds in every sufficiently large
dimension.

The exact four-state atom count is

\[
                  q(2d+2)\longrightarrow q(2d+2)
                  \longrightarrow q(2d+2)
                  \longrightarrow q(2d+2).                 \tag{0.4}
\]

The topology is

\[
                              1\longrightarrow q
                               \longrightarrow q
                               \longrightarrow1.            \tag{0.5}
\]

The first and last transitions are respectively the reflected-reverse and
forward q-gon toggles with a rail bank held fixed.  The middle transition
reverses q complete direct-plus-rail cycles.  Thus no expansion or
contraction is needed.

## 1. Common q-port rail

Work on a \(2m\)-point ground.  Let \(S\) have rank \(m-2\), and choose
distinct coordinates

\[
                         z,a_0,\ldots,a_{q-1}\notin S.       \tag{1.1}
\]

The q-gon port endpoints are

\[
                 A_i=S+z+a_i,\qquad
                 B_i=S+a_i+a_{i+1},                         \tag{1.2}
\]

with indices modulo \(q\).  Their common facet is

\[
                              I_i=S+a_i.                    \tag{1.3}
\]

Choose ordered lists

\[
 X=(x_1,\ldots,x_d)\subset S,\qquad
 Y=(y_1,\ldots,y_d)
   \subseteq\overline{S\cup\{z,a_0,\ldots,a_{q-1}\}}.       \tag{1.4}
\]

Condition (0.1) is exactly what guarantees both choices: \(d\le|S|\),
and the exterior bank has size

\[
                  2m-(m-2+1+q)=m-q+1\ge d.                 \tag{1.5}
\]

Put \(X_j=\{x_1,\ldots,x_j\}\) and
\(Y_j=\{y_1,\ldots,y_j\}\).  For every port \(i\), define

\[
 P_{i,j}=I_i-X_j+Y_j+a_{i+1}
                       \qquad(0\le j\le d),                 \tag{1.6}
\]

\[
 Q_{i,0}=I_i-X_d+Y_d+z,                                    \tag{1.7}
\]

and

\[
 Q_{i,j}
 =I_i-\{x_{j+1},\ldots,x_d\}
      +\{y_{j+1},\ldots,y_d\}+z
                       \qquad(1\le j\le d).                 \tag{1.8}
\]

Then

\[
                         P_{i,0}=B_i,\qquad Q_{i,d}=A_i.    \tag{1.9}
\]

The reverse-side return rail is

\[
 {\cal R}_i^-:\quad
 B_i=P_{i,0}\to P_{i,1}\to\cdots\to P_{i,d}
 \to Q_{i,0}\to\cdots\to Q_{i,d}=A_i,                      \tag{1.10}
\]

and the forward-side rail \({\cal R}_i^+\) is (1.10) read backwards.

## 2. Exact resource inventory

The lower colours of (1.10) are

\[
 I_i-X_j+Y_{j-1}+a_{i+1}
                       \qquad(1\le j\le d),                 \tag{2.1}
\]

\[
                         I_i-X_d+Y_d,                       \tag{2.2}
\]

and

\[
 I_i-\{x_j,\ldots,x_d\}
      +\{y_{j+1},\ldots,y_d\}+z
                       \qquad(1\le j\le d).                 \tag{2.3}
\]

Its owners are

\[
 I_i-X_{j-1}+Y_j+a_{i+1}
                       \qquad(1\le j\le d),                 \tag{2.4}
\]

\[
                    I_i-X_d+Y_d+a_{i+1}+z,                  \tag{2.5}
\]

and

\[
 I_i-\{x_{j+1},\ldots,x_d\}
      +\{y_j,\ldots,y_d\}+z
                       \qquad(1\le j\le d).                 \tag{2.6}
\]

### Theorem 2.1 (q-port resource disjointness)

Across all \(q\) rails:

1. the \(2dq\) internal roots are pairwise distinct;
2. the \((2d+1)q\) lower colours are pairwise distinct;
3. the \((2d+1)q\) owners are pairwise distinct;
4. every internal root avoids every original q-gon root;
5. every rail lower colour avoids every original q-gon lower colour; and
6. every rail owner avoids every original q-gon owner.

Consequently \(\{{\cal R}_i^-\}\) and
\(\{{\cal R}_i^+\}\) are two occurrence-level phase-paired open modules
with identical complete root, lower, and owner inventories.

#### Proof

Every internal rail root contains at least one coordinate of \(Y\) and
omits at least one coordinate of \(X\).  Every original q-gon root contains
all of \(S\), hence all of \(X\), and contains no coordinate of \(Y\).
This separates the two root banks.

Inside the rail bank, the number and prefix/suffix pattern of \(Y\)
recovers the index \(j\).  A \(P\)-root contains no \(z\) and contains the
adjacent q-gon labels \(a_i,a_{i+1}\); a nonendpoint \(Q\)-root contains
\(z\) and only the index label \(a_i\).  Adjacent unordered pairs
\(\{a_i,a_{i+1}\}\) are distinct for \(q\ge3\), and the single labels
\(a_i\) are distinct.  This proves root injectivity.

The same signatures prove lower-colour injectivity from (2.1)--(2.3):
the first family has the adjacent q-gon pair and no \(z\), the middle
family has the single label \(a_i\), all of \(Y\), and no \(z\), and the
last family has \(a_i,z\).  Each member omits at least one coordinate of
\(X\), whereas every original q-gon lower colour \(S+a_i\) contains all
of \(X\).

For owners, (2.4) has the adjacent q-gon pair and no \(z\), (2.5) has the
adjacent pair and \(z\), and (2.6) has only \(a_i,z\).  Their \(Y\)
prefix/suffix sizes recover \(j\).  Every owner in (2.4)--(2.6) contains
at least one coordinate of \(Y\), while every original q-gon owner
\(S+z+a_i+a_{i+1}\) contains none.  This proves all assertions.
\(\square\)

## 3. Exact residence

For one port, append the direct seam \(A_i\to B_i\) to
\({\cal R}_i^-\).  The resulting cycle has \(2d+2\) roots.

### Theorem 3.1 (resident long role-conversion rail)

On that cycle, every coordinate is constant or has one positive cyclic run
of length exactly \(d+1\).  On either open rail orientation, every
positive run avoiding both endpoints has length at least \(d+1\).

More precisely:

* \(a_{i+1}\) occupies \(P_{i,0},\ldots,P_{i,d}\);
* \(z\) occupies \(Q_{i,0},\ldots,Q_{i,d}\);
* \(y_j\) occupies
  \(P_{i,j},\ldots,P_{i,d},Q_{i,0},\ldots,Q_{i,j-1}\); and
* the complementary cyclic run of \(x_j\) is
  \(Q_{i,j},\ldots,Q_{i,d},P_{i,0},\ldots,P_{i,j-1}\).

Every displayed run has length \(d+1\).

#### Proof

The four trace descriptions follow directly from (1.6)--(1.8).
Their lengths are respectively

\[
       d+1,\qquad d+1,\qquad(d-j+1)+j,\qquad
       (d-j+1)+j.                                          \tag{3.1}
\]

Every coordinate of \(I_i-X\) is constant on the cycle.  All remaining
coordinates are absent.  Opening the seam clips the split \(x_j\) runs
and one endpoint-coordinate run; all positive runs which remain internal
retain length \(d+1\).  Reversing the path does not change which vertex
sets form a run or whether that run meets an endpoint. \(\square\)

The theorem is componentwise.  If the q rails are subsequently joined to
an exterior chronology, their clipped boundary runs still require an
endpoint-compatible collar.  No global residence assertion is made before
that gluing is specified.

## 4. Functional return signature

Write the vertices of one reverse-side rail as

\[
                         R_0,R_1,\ldots,R_\ell,
            \qquad \ell=2d+1,                              \tag{4.1}
\]

where \(R_0=B_i\) and \(R_\ell=A_i\), and put
\(W_j=R_j\cup R_{j+1}\).

### Theorem 4.1 (one attachment return and two predecessor returns)

Comparing the rail with its reversal, the head--owner symmetric difference
is the alternating path

\[
 R_0-W_0-R_1-W_1-\cdots-W_{\ell-1}-R_\ell.                 \tag{4.2}
\]

The tail--head symmetric difference is the union of

\[
 R_0^- -R_1^+ -R_2^- -R_3^+ -\cdots-R_\ell^+,             \tag{4.3}
\]

and

\[
 R_0^+ -R_1^- -R_2^+ -R_3^- -\cdots-R_\ell^-.             \tag{4.4}
\]

Thus every rail supplies exactly the support-four square's one attachment
and two predecessor boundary returns, now with depth-\(d\) residence.

#### Proof

In the forward rail, owner \(W_j\) is attached to head \(R_{j+1}\); in the
reversed rail it is attached to head \(R_j\).  Alternation gives (4.2).

The two tail--head atoms on edge \(j\) are
\(R_j^-R_{j+1}^+\) and \(R_{j+1}^-R_j^+\).  Alternating them changes the
root index by two.  Since \(\ell\) is odd, the two components have the
opposite-shore endpoints displayed in (4.3)--(4.4). \(\square\)

## 5. Internal arbitrary-width OR deck

### Theorem 5.1 (exact internal reversal)

For every interval of rail vertices

\[
                         R_a,R_{a+1},\ldots,R_b,             \tag{5.1}
\]

the reversed rail has the interval

\[
                 R_b,R_{b-1},\ldots,R_a                    \tag{5.2}
\]

with exactly the same union.  Therefore the complete arbitrary-width OR
deck of intervals contained wholly in one rail is identical in the two
phases.

#### Proof

Equations (5.1) and (5.2) contain exactly the same family of root sets.
Set union is commutative. \(\square\)

This does not compare intervals which include exterior roots on one or
both sides of a rail.  It also does not compare an interval spanning two
different rails after a global ordering is chosen.  Those cross-boundary
and cross-rail witnesses are an explicit remaining upper-deck gate.

## 6. Exact four-state serial composition

Under the reflected indexing of the q-gon theorem, the two direct phases
of the reflected reverse block are

\[
\begin{aligned}
 D_R^0&=\{B_{i-1}\to A_i:i\in\mathbb Z_q\},\\
 D_R^1&=\{B_i\to A_i:i\in\mathbb Z_q\},
\end{aligned}                                               \tag{6.1}
\]

and the forward direct phases are

\[
\begin{aligned}
 D_F^0&=\{A_i\to B_i:i\in\mathbb Z_q\},\\
 D_F^1&=\{A_i\to B_{i-1}:i\in\mathbb Z_q\}.
\end{aligned}                                               \tag{6.2}
\]

Keep the direct q-gon matching in every state.  Pair a reverse-directed
q-gon matching with the oppositely directed rail bank, and vice versa:

\[
\begin{aligned}
 H_0&=D_R^0\cup\bigcup_i{\cal R}_i^+,\\
 H_1&=D_R^1\cup\bigcup_i{\cal R}_i^+,\\
 H_2&=D_F^0\cup\bigcup_i{\cal R}_i^-,\\
 H_3&=D_F^1\cup\bigcup_i{\cal R}_i^-.
\end{aligned}                                               \tag{6.3}
\]

### Theorem 6.1 (exact four-state role conversion)

Every \(H_j\) is a directed cycle cover on the same root set.  Every state
has exactly

\[
                              q(2d+2)                       \tag{6.4}
\]

atoms and the same complete lower and owner palettes.  The transitions
have the following literal meanings:

1. \(H_0\to H_1\) is the reflected-reverse q-gon toggle with
   \(\bigcup_i{\cal R}_i^+\) fixed;
2. \(H_1\to H_2\) reverses the q disjoint direct-plus-rail cycles;
3. \(H_2\to H_3\) is the forward q-gon toggle with
   \(\bigcup_i{\cal R}_i^-\) fixed.

Their component counts are

\[
                              1,\ q,\ q,\ 1.                \tag{6.5}
\]

Moreover,

\[
                              H_3=H_0^{\rm rev}             \tag{6.6}
\]

as complete occurrence-labelled directed graphs.

#### Proof

In \(H_0,H_1\), the direct matching uses every \(B_i\) once as a tail and
every \(A_i\) once as a head.  The rail bank
\({\cal R}_i^+\) runs from \(A_i\) to \(B_i\), so it supplies the opposite
endpoint roles.  Every internal rail root has one incoming and one outgoing
atom.  Hence both states are cycle covers.  The \(H_2,H_3\) argument is
the orientation reversal.

Every direct q-gon phase uses the same q lower and owner colours.  Theorem
2.1 makes those resources disjoint from the common rail palettes, and rail
reversal preserves every rail resource.  Thus all four states have the
same typed inventory and count (6.4).

In \(H_0\), following rail \(i\) from \(A_i\) to \(B_i\), then the direct
edge \(B_i\to A_{i+1}\), advances the port index by one.  This is one
cycle.  In \(H_1\), \(B_i\to A_i\) closes each rail separately, giving q
cycles.  The same argument reversed gives q cycles in \(H_2\) and one in
\(H_3\).  Finally the reverse of \(B_i\to A_{i+1}\) is
\(A_{i+1}\to B_i\), exactly the reindexed edge of \(D_F^1\), and every
\({\cal R}_i^+\) reverses to \({\cal R}_i^-\).  This proves (6.6).
\(\square\)

### Theorem 6.2 (residence in all four states)

Every component of every \(H_j\) has depth-\(d\) residence.  In \(H_1\)
and \(H_2\), every nonconstant cyclic run has length exactly \(d+1\) or is
longer by merging.  The global cycles \(H_0,H_3\) are resident as well.

#### Proof

The \(H_1,H_2\) components are exactly the direct-seam-plus-rail cycles of
Theorem 3.1.

Traverse \(H_0\) as

\[
 A_i,\ {\cal R}_i^+\setminus\{A_i\},\ A_{i+1},\ldots .      \tag{6.7}
\]

Within each rail, every \(y_j\)-run is internal of length \(d+1\), and
every \(z\)-run has length \(d+1\) at the \(A_i\) end.  The two clipped
pieces of an \(x_j\)-run at \(B_i,A_{i+1}\) concatenate across the direct
edge to length \(d+1\), because the same ordered \(X\) is used at every
port.  Each port label \(a_i\) is the constant anchor throughout rail i
and the endpoint label on the adjacent rail, so its positive run only
becomes longer.  Coordinates in \(S-X\) are constant.  These exhaust the
coordinates.  Hence \(H_0\) is resident.  Equation (6.6) gives the same
for \(H_3\). \(\square\)

### Corollary 6.3 (endpoint upper-deck equality)

The complete arbitrary-width interval-OR decks of \(H_0\) and \(H_3\)
are identical, including intervals crossing rail boundaries.

Indeed, (6.6) reverses the complete cyclic chronology, and every interval
has the same vertex family in reversed order.

## 7. Current gate

For \(q=2(d+1)\) and \(m\ge3d+1\), the local resident role-conversion
problem is solved at all q ports:

* coordinate supply is explicit;
* internal roots and immediate palettes are collision-free;
* all four serial states are resident;
* the functional boundary signature is exact; and
* the two endpoint chronologies have exactly the same full upper deck.

The remaining theorem is a protected common-host statement which reserves
the \(2dq\) internal rail roots and all direct/rail resources in one
coefficient-one ambient ordered-diamond factor.  It must also prove upper
transparency across the two q-gon transitions \(H_0\to H_1\) and
\(H_2\to H_3\), and retain the common compiler.  There is no longer an
edge-count or expansion/contraction discrepancy.

## 8. Independent H100 replay

The C++ replay

    scratch/audit_qgon_resident_longrail_role_converter_20260801.cpp

was compiled and run on H100 with C++20, O3, and NDEBUG.  It checks every
parameter triple in the range

    m <= 24, d <= 7, 3 <= q, q+d <= m+1.

For every instance it verifies:

* all root, lower, and owner ranks;
* every endpoint identity;
* within-rail and cross-rail resource injectivity;
* disjointness from the q-gon resource bank;
* cyclic and clipped-path residence;
* equality of every within-rail interval OR under reversal; and
* the direct/rail serial inventory.

The retained output is

    scratch/audit_qgon_resident_longrail_role_converter_20260801.out

with SHA-256 values

    source  3cd71291ee4c7df1574837b762487a91b24dcc8b4768f6fbd5b93de660c4d90f
    output  a9c89af811f4fd79b9dd05428fe7d9fe22e2c63044037aa1aa75c3a0fe6264bc

Its final scope line is

    H3 is the global reverse of H0; all four states resident
