# The exact one-rung square-corner splice theorem

Date: 2026-07-29

Status: proved, conditional on the stated odd-parent Hamilton cycle.  This
is an exact characterization of the one-cut-per-rail, one-rung carrier
class.  It does not assert that the required parent cycle exists, nor does
it settle higher shadows or `COMP_3`.

## 1. Complementary rails and notation

Let

\[
 |X|=2r-1,\qquad z\notin X,\qquad
 W=\binom{2r-1}{r}.
\]

Let `F` be one physical Hamilton cycle of `J(X,r)`.  For an edge
\(g=YY'\) of `F`, put

\[
 \lambda(g)=Y\cap Y',\qquad
 \upsilon(g)=Y\cup Y',
 \qquad
 \mu(U)=|\{g\in E(F):\upsilon(g)=U\}|.
\tag{1.1}
\]

Assume throughout that

1. \(\lambda:E(F)\to\binom X{r-1}\) is a bijection;
2. \(\upsilon(E(F))=\binom X{r+1}\);
3. every cyclic one-run and every cyclic zero-run of every coordinate of
   `X` on `F` has at least \(D\) vertices.

For the `15 -> 16` application, \(r=8\) and \(D=4\).

The child middle layer is the disjoint union of

\[
 A_P=P\quad(P\in\tbinom Xr),
 \qquad
 B_R=\{z\}\cup R\quad(R\in\tbinom X{r-1}).
\tag{1.2}
\]

The A rail is `F`.  The B copy of a parent vertex `Y` is
\(B_{\bar Y}\), where complements are in `X`.  The complementary B copy
of a parent edge `g` has the colour pair

\[
 \left(\{z\}\cup\overline{\upsilon(g)},
       \{z\}\cup\overline{\lambda(g)}\right),
\tag{1.3}
\]

whereas an incidence rung \(A_PB_R\), necessarily with \(R\subset P\),
has colour pair

\[
 (R,\{z\}\cup P).
\tag{1.4}
\]

Here and below, residence means that every internally bounded positive run
in the final linear middle chronology has at least \(D\) vertices.  Runs
meeting either global endpoint are exempt.

## 2. Exact one-rung characterization

### Theorem 2.1 (one-rung square-corner splice)

Choose parent edges \(e,f\in E(F)\), an endpoint \(P\) of `e`, and an
endpoint \(S\) of `f`.  Write

\[
 R=\bar S.
\]

Delete the A copy of `e` and the complementary B copy of `f`, and propose
to add the single rung \(A_PB_R\).  The result is a spanning Johnson
Hamilton path with both child q1 palettes complete and with depth-
\((D-1)\) residence if and only if all three conditions below hold.

**Square-corner identities**

\[
 R=\lambda(e),\qquad P=\overline{\lambda(f)}.
\tag{2.1}
\]

**Slack-colour survival**

\[
 \mu(\upsilon(e))\ge2,
 \qquad
 \mu(\upsilon(f))\ge2.
\tag{2.2}
\]

**Positive collar compatibility.**  Orient `F-e` toward `P`, and orient
the complementary path `bar(F-f)` away from `R`.  For \(x\in X\), let
\(\alpha_x\) and \(\beta_x\) be the positive terminal lengths at those
two endpoints, with value zero when the corresponding endpoint omits
`x`.  Then

\[
 \alpha_x+\beta_x\in\{0\}\cup[D,\infty)
 \qquad(x\in X).
\tag{2.3}
\]

The two global endpoints are the unused endpoint of `e` and the
complementary copy of the unused endpoint of `f`.

#### Proof

First suppose (2.1)--(2.3) hold.  Since
\(R=\lambda(e)\subset P\), the proposed rung is a Johnson edge.  Each
deleted rail edge opens a Hamilton cycle into a spanning path.  Joining
the chosen endpoints by one rung therefore gives one path through all

\[
 2W=\binom{2r}{r}
\]

child middle vertices, exactly once.

The deleted A edge and deleted B edge, followed by the added rung, have the
exact ledger

\[
\begin{array}{c|cc}
 &\text{lower colour}&\text{upper colour}\\ \hline
A_e&\lambda(e)&\upsilon(e)\\
B_f&\{z\}\cup\overline{\upsilon(f)}
   &\{z\}\cup\overline{\lambda(f)}\\
A_PB_R&R&\{z\}\cup P.
\end{array}
\tag{2.4}
\]

Thus (2.1) restores exactly the deleted no-`z` lower colour and the
deleted `z`-upper colour.  Bijection of `lambda` makes both of those
colours tight.  The only un-restored colours are
\(\upsilon(e)\) and \(\{z\}\cup\overline{\upsilon(f)}\); (2.2) says
precisely that another copy of each survives.  The original q1 hypotheses
then give both complete child palettes.  This remains true when
\(\upsilon(e)=\upsilon(f)\): after the two shore-specific deletions, the
A copy of `f` and the B copy of `e` remain.

Every positive run not meeting the rung is either a full cyclic one-run of
`F`, a full cyclic zero-run of `F` on the complementary B rail, or a run
meeting a global endpoint.  It is therefore safe by the parent
bi-residence or by the boundary convention.  At the unique internal seam,
the positive run of coordinate `x` has length
\(\alpha_x+\beta_x\), unless both endpoint bits are zero.  Hence (2.3) is
necessary and sufficient for residence.

Conversely, consider any construction in this class that is a spanning
path and has both q1 palettes.  Its rung must join endpoints exposed by the
two cuts.  Deleting `e` removes the unique no-`z` lower colour
\(\lambda(e)\); the only added edge has lower colour `R`, so completeness
forces \(R=\lambda(e)\).  Deleting the B copy of `f` removes the unique
`z`-upper colour \(\{z\}\cup\overline{\lambda(f)}\); the rung has upper
colour \(\{z\}\cup P\), so completeness forces
\(P=\overline{\lambda(f)}\).  No rung can supply a no-`z` upper colour or
a `z`-lower colour.  Their survival is therefore equivalent to (2.2).
Finally, the only new internally bounded positive run is at the rung, so
residence is equivalent to (2.3).  This proves all claimed necessities as
well as sufficiency.  \(\square\)

### Topological warning

The hypothesis that `F` is one Hamilton cycle is essential.  If `F` has
\(c>1\) physical components, one rung joins only one A component to one B
component and leaves \(2c-2\) untouched cycles.  A generic Hamilton
*factor* is therefore not enough for Theorem 2.1.

## 3. The square normal form and the six real collar rows

The apparent `2r-1` residence rows in (2.3) reduce almost completely.

### Lemma 3.1 (normal form)

Under (2.1), put

\[
 L=\lambda(e),\qquad K=\lambda(f).
\]

There are unique elements \(a\in X\setminus(L\cup K)\), \(u\in K\),
and \(v\in L\) such that

\[
 X=L\mathbin{\dot\cup}K\mathbin{\dot\cup}\{a\},
\tag{3.1}
\]

\[
 e=\{L\cup\{a\},L\cup\{u\}\},
 \qquad
 f=\{K\cup\{a\},K\cup\{v\}\},
\tag{3.2}
\]

and the rung is

\[
 A_{L\cup\{a\}}B_L.
\tag{3.3}
\]

The other B endpoint is \(B_{(L\setminus\{v\})\cup\{a\}}\).

#### Proof

Since \(L\subset P=\bar K\), the sets `L` and `K` are disjoint.  Their
two sizes are \(r-1\) in a ground set of size \(2r-1\), leaving the unique
element `a`.  Hence \(P=L\cup\{a\}\) and
\(S=\bar L=K\cup\{a\}\).  The other endpoint of `e` shares exactly `L`
with `P`, so it is \(L\cup\{u\}\) for a unique \(u\in K\).  The same
argument gives the other endpoint \(K\cup\{v\}\) of `f`, with
\(v\in L\).  Complementing that endpoint gives the displayed B endpoint.
\(\square\)

### Corollary 3.2 (exact reduced residence audit)

For \(x\in L\), let \(\alpha_x\) and \(\beta_x\) have the meaning in
Theorem 2.1.  Then (2.3) is equivalent to only

\[
 \boxed{\alpha_x+\beta_x\ge D
        \qquad(x\in L\setminus\{v\}).}
\tag{3.4}
\]

Indeed, every member of `K` is absent at both seam endpoints.  Coordinate
`a` is present only on the A side, and the cut edge `e` is a boundary edge
of its cyclic positive run, so \(\alpha_a\ge D\).  Coordinate `v` is
present on both sides, but the B copy of `f` is a boundary edge of its
complementary positive run, so \(\beta_v\ge D\).  These coordinates are
automatic.  At `k=15`, (3.4) consists of exactly six inequalities, each
decidable from a radius-three endpoint collar.

If one demanded child *bi*-residence rather than the positive residence
needed by the erosion carrier, there would also be the symmetric zero-run
rows on \(K\setminus\{u\}\).  Those are not part of Theorem 2.1.

## 4. Why parent bi-residence does not settle the seam

Cyclic bi-residence controls a whole cyclic run.  A cut through the
interior of that run can expose an arbitrarily short terminal fragment.
The square identities do not prevent this for the coordinates in
\(L\setminus\{v\}\).

The minimal binary model at \(D=4\) is the cyclic trace

\[
 11110000.
\tag{4.1}
\]

Cut the A copy between positions 0 and 1 and retain position 0 as the seam
endpoint.  Its terminal A-one fragment has length one.  On the
complementary trace \(00001111\), cut between positions 4 and 5 and retain
position 4 as the B seam endpoint.  Its initial B-one fragment also has
length one.  Concatenation creates the internally bounded seam motif

\[
 0\,1\mid1\,0,
\]

of length two.  In the square normal form this is exactly the allowed
coordinate pattern for an \(x\in L\setminus\{v\}\): `x` is constant one
across `e` and constant zero across the underlying `f`.

This binary projection is not, by itself, a full q1-exact Hamilton-cycle
counterexample.  It proves the narrower point needed here: the
coordinatewise bi-residence inequalities do not contain the collar
inequality, and the colour-aware square identities do not repair that
local loss.  Consequently bi-residence alone is not a proof certificate
for a proposed square.  One must either check (3.4) on the finite square
catalogue or prove an additional global theorem coupling q1-exact
Hamilton cycles, square positions, and run boundaries.  No such global
implication is presently proved (and existence of the parent input is
itself still open).

## 5. Exact finite reduction at `k=15`

Bijection of `lambda` makes the candidate catalogue deterministic.  For
each oriented edge incidence \((e,P)\), set

\[
 f=\lambda^{-1}(\bar P).
\tag{5.1}
\]

It gives a square-corner candidate if and only if

\[
 \overline{\lambda(e)}\text{ is an endpoint of }f.
\tag{5.2}
\]

There are at most \(2W=12{,}870\) oriented incidences.  The complete
one-rung audit is therefore:

1. test (5.2);
2. test the two multiplicities in (2.2);
3. test the six capped collar sums in (3.4).

Every passing row is already a rigorous carrier certificate after literal
replay of the resulting path.  The existing lightweight checker
`scratch/audit_k16_biresident_one_rung_splice_20260729.py` implements the
same test by reconstructing and auditing the whole child path.  Its emitted
field named `cycle` contains a **linear path**, so downstream readers must
respect its schema rather than treat that field as cyclic.

The exact square-graph duplicate count, profile-compressed collar bound,
and a checkable sufficient inequality forcing a passing row are proved in
`THREAD_A_K16_ONE_RUNG_SQUARE_COUNTING_AND_COLLAR_FORCING_20260729.md`.

No audited bi-resident parent PASS is presently available, and hence no
one-rung PASS is claimed here.

## 6. Exact scope relative to the general braid master

Theorem 2.1 can replace the large dual-rail master only after a parent
Hamilton cycle satisfying the three hypotheses in Section 1 has been
found, and only for the following carrier conclusions:

* all child middle owners occur exactly once in one Johnson path;
* both child q1 palettes are complete; and
* every internally bounded positive run has length at least `D`.

It does not by itself preserve or construct q2 and deeper upper shadows,
and it does not prove unrestricted `COMP_3` for the final chronology.  In
particular, the top trace \(0^W1^W\) is automatically residence-safe, but
the existence of a usable singleton-`z` compiler cell and the simultaneous
compiler antecedent remain separate finite gates.  A negative result for
the at-most-12,870 catalogue is likewise a no-go only for this one-rung
square-corner subclass, not for the unrestricted multi-rung braid.

Finally, this construction uses the unused incidence corner
\(A_PB_{\lambda(e)}\) of a colour-aware four-state cell.  It is not the
two-crossed-rung square switch used to merge two closed rail cycles into a
new cycle.  Calling it a **one-rung square-corner splice** avoids that
topological ambiguity.
