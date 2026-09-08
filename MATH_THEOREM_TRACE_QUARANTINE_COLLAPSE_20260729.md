# A q1-perfect middle carrier is already a decorated quarantined enumeration

Date: 2026-07-29

Status: exact theorem.  This note collapses the four-level quarantine and
fixed-forest port conditions into one global middle-carrier condition.  It
does not prove existence of such a carrier for every parameter, nor does it
supply deeper shadows or the lower compiler.

## 1. Setup

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 M=\binom{k}{r},\qquad C=\operatorname{Cat}_m.
\]

Let

\[
 T=(T_i)_{i\in\mathbb Z_M}
\]

be a cyclic Hamilton cycle of the Johnson graph \(J(k,r)\): every rank-
\(r\) set occurs once and consecutive owners are distinct Johnson
neighbours.  Assume that

\[
 \{T_i\cap T_{i+1}:i\in\mathbb Z_M\}
   =\binom{[k]}{r-1}
\tag{1.1}
\]

as multisets.  Thus the lower first shadow is exact.

Fix a coordinate \(z\), put \(\Omega=[k]\setminus\{z\}\), and identify

\[
 A=\binom\Omega m
 \quad\text{with the owners }z+A,
 \qquad
 B=\binom\Omega{m+1}
 \quad\text{with the owners not containing }z.
\]

## 2. Forced channel census and trace structure

### Theorem 2.1 (trace--channel collapse)

Under (1.1), the edge types of the relabelled cyclic middle carrier are
forced:

\[
 \#AA=mC,\qquad \#AB=2C,\qquad \#BB=(m-1)C.          \tag{2.1}
\]

Moreover:

1. the \(AA\) intersection colours are every member of
   \(\binom\Omega{m-1}\) exactly once;
2. the cross and \(BB\) intersection colours together are every member of
   \(\binom\Omega m\) exactly once;
3. the cyclic membership trace of \(z\) has exactly \(C\) one-runs and
   \(C\) zero-runs, with average lengths \(m+1\) and \(m\), respectively;
4. a one-run cannot have length one.

#### Proof

An edge intersection contains \(z\) exactly when the edge is of type
\(AA\).  Exactness in (1.1) therefore bijects the \(AA\) edges with

\[
 z+\binom\Omega{m-1},
\]

so

\[
 \#AA=\binom{2m}{m-1}=mC.                              \tag{2.2}
\]

There are \(\binom{2m}{m}=(m+1)C\) A owners.  In a nonconstant cyclic
binary trace,

\[
 \#AA=\#\{1\text{-positions}\}-\#\{1\text{-runs}\}.
\]

Hence the number of one-runs is \(C\).  A cyclic binary trace has equally
many one-runs and zero-runs, so \(AB=2C\).  The B-owner count is
\(\binom{2m}{m+1}=mC\), whence

\[
 \#BB=mC-C=(m-1)C.
\]

The remaining colours in (1.1) do not contain \(z\), and they occur exactly
on cross and \(BB\) edges.  This proves assertions 1 and 2.  Dividing the A
and B owner counts by the common run count gives the two average lengths.

Finally, a one-run of length one has two incident cross edges with the same
rank-\(m\) intersection: the old part of its unique A owner.  This contradicts
the exactness in assertion 2.  \(\square\)

No simplicity assumption beyond the Hamilton cyclic listing is hidden in
the proof.  The wrap edge is included, all owners are distinct, and the
lower-colour exactness itself excludes the offending repeated incidences.

## 3. Upper q1 needs only adjacent unions

### Lemma 3.1

Let \(S\) have rank \(r+1\).  Then \(S\) is the union of a nontrivial
consecutive carrier interval if and only if

\[
                         S=T_i\cup T_{i+1}             \tag{3.1}
\]

for some adjacent edge.

#### Proof

The reverse implication is immediate.  Conversely, if a nontrivial carrier
interval has union \(S\), every one of its owners is contained in \(S\).
Any adjacent Johnson pair inside the interval has union of rank \(r+1\),
contained in \(S\), and hence equal to \(S\).  \(\square\)

This reduction is special to rank \(r+1\).  Targets of rank at least
\(r+2\) still require arbitrary-width union witnesses.

## 4. Exact quarantine collapse

Assume in addition that the adjacent unions cover the entire upper first
shadow:

\[
 \{T_i\cup T_{i+1}:i\in\mathbb Z_M\}
   \supseteq\binom{[k]}{r+1}.                           \tag{4.1}
\]

### Theorem 4.1 (q1-perfect carrier to decorated quarantine)

For every \(H\in\binom\Omega{m+2}\), choose one \(BB\) edge whose union is
\(H\).  Call these edges protected.  Expand every \(AA\) edge through its
unique rank-\((m-1)\) intersection, and every protected \(BB\) edge through
its rank-\((m+2)\) union.  Leave all cross edges and the remaining \(BB\)
edges unexpanded.

The resulting cyclic listing is a B-quarantined tight enumeration of the
four levels

\[
 \binom\Omega{m-1},\quad\binom\Omega m,
 \quad\binom\Omega{m+1},\quad\binom\Omega{m+2}.         \tag{4.2}
\]

Its channel counts are

\[
 \begin{aligned}
 AA&=mC,\\
 AB&=2C,\\
 BB_{\rm protected}&=N_2
       =\frac{m(m-1)}{m+2}C,\\
 BB_{\rm merge}&=t
       =\frac{2(m-1)}{m+2}C.
 \end{aligned}                                         \tag{4.3}
\]

The quarantine is already decorated by both opposite first-shadow
conditions: cross plus \(BB\) intersections are exact, and \(AA\) unions
plus cross B-endpoints cover every \(z\)-containing upper target.

#### Proof

A no-\(z\) upper target can only be the union of a \(BB\) edge.  Therefore
(4.1) supplies at least one such edge for every
\(H\in\binom\Omega{m+2}\).  Edges chosen for distinct \(H\) are distinct,
because an edge has one union label.  Thus upper multiplicity is harmless.

Likewise, a \(z\)-containing upper target \(z+U\), with
\(U\in\binom\Omega{m+1}\), is witnessed either by an \(AA\) union or by a
cross edge ending at \(U\).  This proves the second opposite decoration,
while Theorem 2.1 supplies the exact opposite lower deck.

Every rank-\((m-1)\) vertex is inserted once by the exact \(AA\) colours,
and every rank-\((m+2)\) vertex is inserted once by the chosen protected
edges.  These ranks are disjoint from the middle owners, so the expansion is
a cyclic enumeration with no repeated vertex.  Its only unexpanded
same-parity steps are the unprotected \(BB\) edges, hence it is
B-quarantined.  The protected count is \(N_2\), and Theorem 2.1 gives

\[
 \#BB_{\rm merge}=(m-1)C-N_2
                  =\frac{2(m-1)}{m+2}C.
\]

The standard parity census then gives the tight flip length.  \(\square\)

### Converse and scope

Contracting a B-quarantined enumeration recovers a q1-perfect carrier only
when the quarantine has the two opposite decorations just used: exact
cross-plus-BB lower colours and complete AA-plus-cross upper colours.  Bare
quarantine does not imply either condition.

If the global carrier was produced by the direct-jump two-GMM-forest splice,
its actual cross edges already form a perfect matching of the port copies.
Consequently the fixed-forest deletion equations, upper-hole exposure, Hall
inequalities, connectivity, and chosen orientations all hold automatically.
Those conditions are separate gates only when the two forests are selected
independently.  This implication is one-way: an arbitrary global carrier
need not extend either forest to a preselected GMM Hamilton cycle.

The distinguished coordinate was arbitrary.  Hence one doubly-rainbow q1
Hamilton carrier supplies **simultaneously** one compatible decorated
quarantine decomposition for every coordinate.  In the unit-voltage binary-
trace subclass these `k` decompositions are translates of the same trace;
this is precisely why all-coordinate residence collapses to one minimum-run
predicate there.

## 5. The exact remaining target

The four-level and port formulations therefore collapse to one object:

> a coordinate-compatible q1-perfect Hamilton middle carrier.

For \(k=15\), fixing one coordinate forces

\[
 (AA,AB,BB)=(3003,858,2574),\qquad \#z\text{-runs}=429,
\]

with 2002 protected \(BB\) edges and 572 merge edges.  The strict
unit-voltage binary-trace lane asks for such a carrier with minimum run at
least four.  A positive carrier must still pass the rank-five protected
intersection gate, every deeper upper shadow, the exact one-core/compiler
Hall test, a safe cut, and literal verification.  A negative result in the
binary-trace lane concerns only that symmetric subclass; the natural fallback
is a small-component q1-perfect factor followed by shadow-safe seams.
