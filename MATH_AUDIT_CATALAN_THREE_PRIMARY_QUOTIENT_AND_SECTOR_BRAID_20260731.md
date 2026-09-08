# Audit of the three-primary quotient and its sector-braid meaning

Date: 2026-07-31  
Status: the arithmetic, freeness, full-equivariance obstruction, quotient
matching, and voltage criteria are proved; the recursive sector braid below
is an exact conditional composition lemma, not an existence theorem

## 1. Verdict on the three-primary theorem

Let

\[
q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,
\qquad H=\langle s\rangle\leq \mathbb Z_q.
\]

The claims in
'MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md'
are correct, with one terminology qualification recorded in Section 4.

First,

\[
(m^2-1)\operatorname{Cat}_m
 =2q\binom{q-1}{m-2}.                                    \tag{1.1}
\]

Since

\[
\gcd(q,m^2-1)=\gcd(q,3)
\]

and \(h\) is coprime to \(3\), we have
\(\gcd(h,m^2-1)=1\).  Equation (1.1) therefore gives

\[
                         h\mid\operatorname{Cat}_m.        \tag{1.2}
\]

For a prime-power-explicit proof, if \(p^e\Vert h\), then \(p\ne3\),
\(p\nmid m^2-1\), and the right side of (1.1) has \(p\)-valuation at least
\(e\); hence so does the Catalan number.

Every nonidentity element of \(H\) has some order \(d>1\) dividing \(h\).
A fixed finite-coordinate subset must be a union of its \(d\)-cycles and
therefore have cardinality divisible by \(d\).  The possible finite parts
on ranks \(m-1,m,m+1\) are

\[
                         m-2,m-1,m,m+1.
\]

All four are coprime to \(h\).  Thus the \(H\)-action on all three ranks is
free.  Conversely, whenever \(3\mid q\), the order-three subgroup fixes an
explicit rank-\((m-1)\) colour and an explicit rank-\((m+1)\) colour.  Hence
\(H\) is the unique maximal-order subgroup of the cyclic rotation group
which is free on all three relevant ranks.

## 2. The full-rotation obstruction is exact

The phrase “full \(\mathbb Z_q\) directed repair is impossible” must mean
**fully \(\mathbb Z_q\)-invariant** directed repair.  It is not a no-go for
an unrestricted repair.

Assume \(3\mid q\), write \(q=6a+3\), and let \(T\) be \(\infty\) together
with \(a\) consecutive orbits of the order-three subgroup on the finite
coordinates.  Then

\[
|T|=3a+1=m-1,
\]

and its stabilizer has order exactly three.  Choose distinct finite
coordinates \(x,y\notin T\).  The Johnson edge

\[
                    \{T\cup\{x\},T\cup\{y\}\}             \tag{2.1}
\]

has lower colour \(T\).  Every rank-\(m\) vertex has a free full-rotation
orbit, and because \(q\) is odd no group element can exchange the two
endpoints of an invariant unordered edge.  Thus (2.1) has a free edge
orbit of size \(q\).

The equivariant map “edge \(\mapsto\) lower intersection” sends this free
edge orbit to the colour orbit of size \(q/3\).  Every colour in that orbit
is consequently hit exactly three times.  More generally, if a colour has
stabilizer of order \(d>1\), every free edge orbit over it hits each colour
exactly \(d\) times.  A union of complete edge orbits can therefore never
hit the short colour orbit once.  This proves the claimed obstruction to a
fully invariant exact lower rainbow, and hence to a fully invariant
diamond-normal directed repair.

This proof uses literal orbit multiplicity, not merely the congruence
\(q\nmid\operatorname{Cat}_m\).

## 3. Exact synchronized-track form of the quotient

The \(s\) cosets should be represented as synchronized coordinate tracks.
Write each finite coordinate uniquely as

\[
                         j+st,\qquad j\in\mathbb Z_s,
                         \quad t\in\mathbb Z_h.             \tag{3.1}
\]

For a subset \(A\subseteq\mathbb Z_q\sqcup\{\infty\}\), define its
\(s\)-track word

\[
w(A)=\bigl(\epsilon_\infty(A);w_0,\ldots,w_{s-1}\bigr),
\qquad
w_j(t)=\mathbf 1_{j+st\in A}.                              \tag{3.2}
\]

The generator \(s\in H\) shifts every track by one **simultaneously**.
The rank-freeness theorem says that every relevant word (3.2) has full
diagonal period \(h\).  Thus quotient vertices are aperiodic synchronized
\(s\)-track necklaces, and every relevant quotient shore has exactly its
literal cardinality divided by \(h\).

In particular, for a floor directed-repair core and common-transversal
forest, the quotient counts are

\[
\begin{array}{c|c}
\text{object}&\text{quotient cardinality}\\ \hline
\text{middle vertices}&M/h\\
\text{forest edges}&N/h\\
\text{forest paths}&K/h\\
\text{each repair-core shore}&K/h\\
\text{selected repair hyperedges}&K/h.
\end{array}                                                \tag{3.3}
\]

An oriented Johnson edge replaces a coordinate in one track by a
coordinate in another track, or exchanges a finite coordinate with the
fixed \(\infty\)-socket.  It therefore carries two independent labels:

1. a sector-transfer vector in the rank-zero lattice on
   \(\mathbb Z_s\sqcup\{\infty\}\); and
2. a phase voltage in \(\mathbb Z_h\).

The first describes how a quotient walk braids the tracks.  The second
determines how its lift connects the \(h\) physical fibres.

## 4. What “\(s\)-sector braid” can and cannot mean

The \(s\) coordinate cosets are not \(s\) independent equal packets.
Subsets normally occupy several tracks, and the quotient is by a common
phase shift, not by independent shifts of the tracks.  Accordingly an
\(s\)-sector braid is a quotient walk through synchronized track profiles,
with cross-track Johnson seams.  It is not a disjoint union of \(s\) copies
of a smaller fixture.

This has an equivalent residual-group formulation.  The quotient retains
the action

\[
                  \mathbb Z_q/H\cong\mathbb Z_s.          \tag{4.1}
\]

Middle-set and occurrence-edge \(H\)-orbits have residual orbit size
\(s\).  An exceptional outer colour has full-group stabilizer three, hence
its \(H\)-orbit has residual orbit size \(s/3\).  A complete residual orbit
of quotient edges therefore hits each colour in that shortened orbit three
times.  The sector braid must break this residual symmetry; a residual-
\(\mathbb Z_s\)-invariant quotient matching would simply lift back to the
already impossible fully \(\mathbb Z_q\)-invariant repair.

The count obstruction is already visible at \(m=8\):

\[
q=15,\qquad (h,s)=(5,3),\qquad K/h=1430/5=286,
\]

and \(286\not\equiv0\pmod3\).  Thus even the quotient path components
cannot be split into three equal sector packets.  At \(m=5\),

\[
q=9,\qquad (h,s)=(1,9).
\]

The previously observed three-copy identity \(K_5=3K_4\) is a separate
Pascal packet ledger; it is not the clean-group sector decomposition, which
has nine singleton coordinate tracks and no voltage compression.

These facts narrow, rather than invalidate, the theorem's construction
program: “\(s\)-sector” must refer to a coupled multi-track quotient.

This is a palette/carrier statement, not a claim about the literal K16
repair seams or compiler.  In the authenticated K16 optimum all three
residual sectors interlace inside each strict spiral.  Its four changed edge
classes do not service the four shortened outer-colour orbits one-for-one:
only one changed lower colour is shortened and no changed upper colour is.
Moreover, the final common-cap compiler breaks \(H\).  Thus neither the
four-filter name nor the exact word supplies an \(H\)-invariant realization
of four individual phase filters.

## 5. Conditional \(h\)-equivariant sector-braid lemma

Let an \(H\cong\mathbb Z_h\)-invariant saturating-cycle fixture be given.
Suppose the following quotient data exist.

1. The quotient directed-repair multihypergraph has a perfect matching.
   Parallel quotient edges are retained with their physical occurrence and
   voltage labels.
2. Its selected common-transversal edge orbits form a spanning quotient
   path forest \(\bar F\) with \(M/h\) vertices, \(N/h\) edges, and
   \(K/h\) path components, and the quotient lower and upper colour-orbits
   are each used exactly once.
3. Exactly \(K/h\) closure-edge orbits use every quotient path endpoint
   once and, after the paths are contracted, form one quotient cycle.
4. The total phase voltage \(v\in\mathbb Z_h\) around this cycle is a unit:
   \(\gcd(v,h)=1\).

Then the lifted repair is exact on both colour shores, its selected forest
has exactly \(K\) physical paths, and restoring the connectors produces one
Hamilton cycle on all \(M\) middle sets.

The proof is the quotient matching theorem followed by the standard
voltage lift: freeness makes every selected quotient hyperedge cover each
vertex of its incident orbit once; a quotient path gauges to voltage zero
and lifts to \(h\) disjoint paths; the closed quotient cycle has
\(\gcd(v,h)\) lifted components.

This is also the exact composition rule for recursive packets.  Packet
interiors may be inherited from smaller constructions, but their quotient
shore-orbits must be disjoint.  Boundary seams must complete the missing
lower and upper quotient palettes, use each path endpoint once, make the
contracted packet graph one cycle, and have unit total phase voltage.
Sector-transfer conservation and scalar counts alone do not imply any of
these palette or endpoint conditions.

The equivariance in this lemma is a sufficient organization of the
two-sided-rainbow carrier.  It is not a requirement on the later integral
compiler assignment; imposing it there would exclude the authenticated K16
optimum.

Because \(h\) is odd, voltage \(2\) is a unit for every clean group
\(\mathbb Z_h\).  Thus a dimension-uniform sufficient target is a coupled
\(s\)-track quotient braid of total voltage two.  This is a target, not a
proof that such a braid always exists.

## 6. The authenticated \(m=4\) seed as the one-sector base packet

For \(m=4\),

\[
(q,h,s)=(7,7,1),\qquad (M/h,N/h,K/h)=(10,8,2).             \tag{6.1}
\]

The authenticated complete repair core quotients to one forced-ear edge
and two parallel kernel edges.  Its two perfect matchings select the forced
edge and one of the kernel edges.  The common transversal quotients to two
paths of vertex sizes \(3\) and \(7\).  The two closure-edge orbits join
them into a ten-cycle of voltage \(2\).  Both kernel choices have the same
net voltage and therefore both lift to a connected 70-cycle.

Consequently the \(m=4\) object supplies all local primitives required by
the conditional lemma:

    one forced repair orbit + one binary kernel choice;
    two protected quotient paths + two closure seam orbits;
    exact lower/upper quotient palettes + primitive voltage 2.

It does not supply the cross-track part: \(s=1\), so its sector-transfer
graph is trivial.  In higher dimensions it is therefore a structural base
packet, not a literal automatically embeddable subfixture.  A recursive
proof still has to construct colour-disjoint quotient embeddings and the
cross-track seams satisfying Items 1--4 above.

## 7. Reproduction and hashes

Run

    python3 scratch/audit_catalan_three_primary_short_orbit_and_sector_braid_20260731.py

The audit constructs the explicit short colour and a free edge orbit above
it for every \(m\le50\) with \(3\mid(2m-1)\), checks the threefold incidence
multiplicity, and authenticates the frozen \(m=4\) quotient and voltage
payloads.  This finite replay supplements the symbolic all-\(m\) proof; it
does not establish a higher-dimensional braid.

Frozen hashes:

    audit script:
      846e39a28d084ea249d2cfa3e68f51147c179cb5891ce08a95e9b534b665a8c6
    audit JSON:
      5dfab3c04c1581e8953920a9bc7ba5af1a6a4734ea0e8f88ef247d4653e3a6cd
    canonical payload:
      0cfa075c6519fc9391e187efc74a107ba58166e5c672b0946f0f30873d92671c
