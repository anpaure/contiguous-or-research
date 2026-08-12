# Independent audit of the multidepth boundary-signature circulation

Date: 2026-07-24

Audited source: `MULTIDEPTH_SAFE_SPLICE_THEOREM_20260724.md`, Section 9.

## Verdict

Section 9 is correct after two necessary premise clarifications, both of
which have been inserted into the audited source:

1. the old cycles are explicitly pairwise vertex-disjoint and their cut
   paths are `H`-run-valid; and
2. every retained old path has more than `2H` transitions, so distinct
   installed seams cannot interact inside a window or coordinate run of
   length at most `H`.

The soft splice theorem also now explicitly requires the new arc to join
two distinct current path components.  With these premises, formulas
(9.1)--(9.6), the exact component/hole ledger, and the depth-one mixed-flag
interpretation all check.  The new ambient mixed-flag count and its
geometric filtering estimate also check; there is no missing orientation
factor.

## 1. Lost-window indexing: (9.1)

Cut the cyclic edge from the tail `T^i_{-1}` to the head `T^i_0`.  A
depth-`q` cyclic shadow uses `q+1` vertices, hence `q` transitions.  It is
lost precisely when its start lies at one of

\[
 -q,-q+1,\ldots,-1.
\]

Writing the start as `-r`, with `1<=r<=q`, gives exactly

\[
 \{T^i_{-r},T^i_{-r+1},\ldots,T^i_{q-r}\}.
\]

This is the interval used in (9.1).  It contains

\[
 (q-r)-(-r)+1=q+1
\]

vertices and crosses the deleted edge exactly once.  Thus each of
`mathcal B_(i,q)^-` and `mathcal B_(i,q)^+` contains exactly the `q` lost
cyclic windows.  Joint global rainbowness makes these `q` colours distinct,
and makes the boundary-signature families for different old cycles
pairwise disjoint at each fixed signed depth.

## 2. Cross-window indexing: (9.2)

After joining the tail of path `i` to the head of path `j`, a crossing
depth-`q` window contains

* `r` vertices from the suffix of `i`, indexed `-r,...,-1`; and
* `q-r+1` vertices from the prefix of `j`, indexed `0,...,q-r`.

The total is

\[
 r+(q-r+1)=q+1.
\]

As `r` ranges from `1` to `q`, these are exactly the `q` new windows which
cross the seam.  Taking their intersections and unions gives precisely
(9.2); there is no off-by-one error.

## 3. Exact compatibility: (9.3)

The equality

\[
 \mathcal X_{ij,q}^-=\mathcal B_{i,q}^-,\qquad
 \mathcal X_{ij,q}^+=\mathcal B_{j,q}^+
\]

has the correct orientation.  An outgoing arc from `i` restores its lost
lower signature, while an incoming arc to `j` restores its lost upper
signature.  Equality as sets is sufficient; no indexed correspondence
between the `q` old and `q` new windows is needed.

The geometric seam condition supplies the correct shadow ranks and local
run validity.  Because every retained old path has more than `2H`
transitions, a block of at most `H` transitions meets at most one new seam.
Consequently independently checked seams cannot acquire an additional
short-run interaction through an intervening old component.

## 4. Exact path-forest ledger: Theorem 9.1 and (9.4)

An acyclic directed graph of indegree and outdegree at most one is a
directed path forest.  If it has `p` vertices and `s` arcs, it has

\[
 c=p-s
\]

components.  In each component:

* every non-sink old cycle has its lower boundary signature restored by
  its outgoing arc;
* the sink retains one unfilled lower boundary signature;
* every non-source old cycle has its upper boundary signature restored by
  its incoming arc; and
* the source retains one unfilled upper boundary signature.

Each signature contains `q` colours at depth `q`.  Hence the final family
has exactly `cq` unfilled lower cut colours and `cq` unfilled upper cut
colours at depth `q`, in addition to the original cyclic holes.

The endpoint-capped erosion charge is therefore

\[
 cH+2c\sum_{q=1}^Hq
 =cH+cH(H+1)
 =c(H^2+2H).
\]

Adding the original cyclic-band defect `U_m` gives exactly

\[
 \boxed{U_m+c(H^2+2H),}
\]

which is (9.4).  There is no extra factorability or pin charge: the
endpoint-capped erosion word is already a literal contiguous-OR word.

## 5. Depth-one mixed flag: (9.5)

At depth one,

\[
 \mathcal B_{i,1}^-=\{L_i\},\qquad
 \mathcal B_{j,1}^+=\{U_j\},
\]

where

\[
 L_i=T^i_{-1}\cap T^i_0,\qquad
 U_j=T^j_{-1}\cup T^j_0.
\]

The single new cross edge has endpoints `T^i_{-1}` and `T^j_0`.  Therefore
the depth-one instance of (9.3) is exactly

\[
 T^i_{-1}\cap T^j_0=L_i,\qquad
 T^i_{-1}\cup T^j_0=U_j,
\]

which is (9.5).

Since `|L_i|=m-1` and `|U_j|=m+1`, these equalities are equivalent to
`L_i subset U_j` together with the assertion that the tail of `i` and the
head of `j` are the two distinct middle-rank members of the interval
`[L_i,U_j]`.  Thus an internal forest vertex uses its upper cut colour on
its incoming arc and its lower cut colour on its outgoing arc.  The stated
endpoint-neutral mixed-flag circulation law is exact.

## 6. Ambient mixed-flag degree: Proposition 9.3

Fix the source cut occurrence

\[
 T_{-1}=L+a,\qquad T_0=L+b.
\]

For a mixed-flag target choose

\[
 c\in L,\qquad d\notin L\cup\{a,b\},
\]

and set

\[
 U_j=L+a+d,\quad T^j_0=L+d,\quad
 T^j_{-1}=L-c+a+d.
\]

There are `(m-1)` choices for each of `c` and `d`.  The target endpoints
are distinct from the two source endpoints, and the target edge is a
Johnson edge.  Each such target edge lies in exactly `D_E` cyclic-strip
cycles.  Its orientation is forced by the displayed tail and head, so no
factor two is missing.  Conversely, (9.5) recovers `d` from the target head
`L+d`; the other endpoint of the target cut edge is `U_j-c`, and endpoint
distinctness excludes `c=d`, leaving uniquely `c in L`.  Thus the exact
ambient count is

\[
 \boxed{(m-1)^2D_E.}
\]

The filtered estimate

\[
 \left(1-O\!\left(\frac{H^2+\ell^2}{m}\right)\right)
 (m-1)^2D_E
\]

is also supported by the estimates used in Theorems 5.1--5.2:

* avoiding the fixed source seam neighbourhood and requiring the oriented
  target neighbourhood to avoid it rejects `O(H^2/m)` of the occurrences;
* the stabilizer of the target edge is transitive on each of its two
  `(m-1)`-coordinate classes, so a union bound over the `2ell` source-cycle
  vertices rejects `O(ell^2/m)` for vertex intersection; and
* the only small-orbit endpoint which could be the source predecessor
  shares coordinate `d` with the new seam label and is already rejected by
  seam safety.  Complementary endpoints cannot lie in a strip cycle through
  the target edge because its nonempty core is contained in every cycle
  vertex.

This proposition is only an ambient count.  It correctly makes no claim
that a particular selected strip matching retains any of those partners,
or that depth-`q` compatibility holds for `q>=2`.

## 7. Soft repeated-join ledger: (9.6)

For a geometrically valid arc joining two distinct current path components,
no old path window is deleted.  The component count drops by one, so the
endpoint-cap part changes by `-H`.  At signed depth `q`, if `R_q^pm` is the
current set of distinct colours, the missing count drops by exactly

\[
 |\mathcal X_{ij,q}^\pm\setminus R_q^\pm|.
\]

Internal repetitions inside the cross signature are handled correctly by
taking `mathcal X` as a set.  Therefore

\[
 \boxed{
 \Delta G=-H-
 \sum_{q=1}^H\left(
 |\mathcal X_{ij,q}^-\setminus R_q^-|
 +|\mathcal X_{ij,q}^+\setminus R_q^+|
 \right),
 }
\]

which is (9.6).  Its maximum possible saving is

\[
 H+2\sum_{q=1}^Hq=H^2+2H.
\]

For repeated joins, `R_q^pm` must be updated after every accepted arc and
each arc must join two distinct current components.  Under exactly those
conditions, the changes in distinct-colour counts and component counts
telescope, so (9.6) remains exact for an arbitrary sequence of accepted
splices.

## Final status

No flaw remains in the Section 9 boundary-signature theorem or ledger.
The unresolved issue is constructive: obtaining a sufficiently long path
forest of geometrically valid arcs with good exact or soft multidepth
signature gain inside the selected strip matching.
