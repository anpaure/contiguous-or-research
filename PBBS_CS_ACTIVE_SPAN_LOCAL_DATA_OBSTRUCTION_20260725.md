# An exact active-span obstruction to local simple-sector charging

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The fixed-core normal form of a simple PBBS return, projected-edge
disjointness, and the freedom to choose the cutting occurrence anywhere
inside the return do **not**, by themselves, imply the vanishing
clustered-span estimate required by \((CS_A)\).

There is an exact cyclic interval model in which

* every selected return support is simple and the supports are pairwise
  edge-disjoint;
* every return may be cut at an arbitrary one of its support edges;
* the return density is exactly \(1/H\), the marginal scale supplied by
  the current fan/fixed-core bounds; but
* every cut transversal, under every partition into clusters, has
  clustered cost \(\Omega(B)\).

The model can be decorated independently by the two-core simple-return
normal form and by any of its \(((r-s)!)^2\) ambient completions.  Those
decorations do not affect the lower bound.  Thus neither alternative
ambient occurrences nor a marginal \(1/H\) sector saving can close
\((CS_A)\).  A successful proof must use a common-base, cross-sector PBBS
chronology theorem which excludes the tiling pattern below.

This is a logical obstruction to the proposed local proof, not a
counterexample to the canonical PBBS statement \((CS_A)\).

## 1. The tiled simple-sector model

Let \(H\ge2\), let \(L\) be a multiple of \(H\), and let \(F\ge1\).
For a literal simple-return decoration take \(s=H-2\) (so its projected
trace has \(s+2=H\) edges) and assume \(H\le r+2\).
For each fibre \(v\in[F]\), take a cyclic edge set

\[
 C_v=\mathbb Z_L\times\{v\}.
\]

Partition it into the half-open length-\(H\) intervals

\[
 I_{a,v}=\{aH,aH+1,\ldots,(a+1)H-1\}\times\{v\},
 \qquad a\in\mathbb Z_{L/H}.
\tag{1.1}
\]

Let \(\mathcal I\) be the union of these intervals over all fibres.  Then

\[
 |\mathcal I|={LF\over H},
 \qquad
 \sum_{I\in\mathcal I}|I|=LF.
\tag{1.2}
\]

In particular the intervals are pairwise edge-disjoint.  Regard every
\(I\) as the projected trace of a simple return sector.  The local
fixed-core theorem places no compatibility condition between two
edge-disjoint sectors, so each interval may independently be decorated by
disjoint cores \(K,K'\), its active alternating label list, and any one of
the \(((r-s)!)^2\) ambient completions.  All conclusions below concern
only the projected supports and therefore survive every such decoration.

## 2. Exact cluster lower bound

A cut transversal is a set \(C\) of cyclic edges meeting every interval
in \(\mathcal I\).  On each fibre, partition the cuts into arbitrary
clusters.  If a cluster has leftmost and rightmost lifted cuts separated
by span \(S\ge0\), charge it the PBBS auxiliary cost

\[
 7H+3S-3.
\tag{2.1}
\]

This is precisely the cost appearing in the established clustered seam
ledger.  Allow cuts at shared block boundaries if desired; doing so can
only help the transversal and is included in the estimate below.

### Theorem 2.1 (tiled active-span obstruction)

Every cut transversal and every clustering satisfy

\[
 \boxed{
  \sum_{\text{clusters }J}(7H+3S_J-3)
  \ge (3-3/H)LF.
 }
\tag{2.2}
\]

In particular the clustered cost is \(\Theta(LF)\), not \(o(LF)\).

#### Proof

Work first on one fibre.  A cluster of span \(S\) can meet at most

\[
 {S\over H}+2
\tag{2.3}
\]

of the blocks in (1.1).  Indeed, except for the block containing the
leftmost cut and the block containing the rightmost cut, every met block
lies wholly between those two cuts and consumes \(H\) units of span.
The same assertion holds across the cyclic seam: lift immediately after a
largest cut-free cyclic gap.  A transversal has no cut-free gap longer
than \(2H\), and (2.3) remains valid even when the displayed cluster
contains every cut on the fibre.

Let \(t_J\) be the number of tiled intervals assigned to cluster \(J\).
Assign each block to one cluster containing one of its transversal cuts.
Equation (2.3) gives

\[
 S_J\ge H(t_J-2).
\tag{2.4}
\]

Consequently

\[
 \begin{aligned}
  7H+3S_J-3
  &\ge 7H+3H(t_J-2)-3\\
  &=3Ht_J+H-3\\
  &\ge (3H-3)t_J,
 \end{aligned}
\tag{2.5}
\]

because \(t_J\ge1\).  There are \(L/H\) blocks on the fibre, so summing
(2.5) gives at least

\[
 (3H-3){L\over H}=(3-3/H)L.
\tag{2.6}
\]

Summing independently over the \(F\) fibres proves (2.2). \(\square\)

The constants are inessential.  The same proof shows that every cost of
the form \(c_0H+c_1S\), with fixed positive \(c_0,c_1\), is
\(\Omega(LF)\).

## 3. Alternative occurrences do not help locally

The normal form gives two kinds of freedom.

1. The returned label occurs at both endpoints, so a cut may be placed at
   either endpoint or anywhere in the projected support.
2. The open sector admits \(((r-s)!)^2\) ambient wreath completions.

The proof of Theorem 2.1 already grants the stronger first freedom: every
edge of every interval is an admissible cut.  The second freedom changes
only the tail of the owner wreath, not the projected support that must be
hit.  It therefore leaves (2.2) unchanged.

Thus an argument which treats the sectors independently cannot convert a
\(1/H\) marginal sector density into an additional \(1/H\) active-span
saving.  This is the clustered-span version of the exact residue-class
non-tensorization phenomenon: interval length and marginal fibre density
combine by a minimum, not a product.

## 4. Exact consequence for the coefficient-one attack

The theorem rules out the implication

\[
 \boxed{
 \begin{gathered}
 \text{pairwise projected-edge-disjoint simple sectors}\\
 +\ \text{fixed-core normal form}\\
 +\ \text{independent alternative completions}\\
 +\ O(1/H)\ \text{marginal sector density}
 \end{gathered}
 \Longrightarrow (CS_A).
 }
\tag{4.1}
\]

It does not rule out \((CS_A)\) for the canonical PBBS factor.  It says
exactly what the missing theorem must add.  In quotient language, one
must prove that the actual PBBS short-return supports cannot approximate
the tiled pattern on a positive fraction of the \(B_r\) base edges.  Any
one of the following would suffice:

* a common-base two-time anticorrelation estimate for predecessor
  occurrences;
* a chronology theorem forcing the union of all Gaussian short-return
  supports to have \(o_A(B_r)\) measure;
* or an in-place baseline replacement which makes active span cease to be
  an additive cost.

The first two are genuinely global statements about the canonical PBBS
skew product.  They cannot be recovered from the local fixed-core sector
geometry, since the tiled model satisfies all of that local geometry and
still has linear clustered cost.

## 5. Status

Proved here:

\[
 \text{local simple-sector data plus alternative occurrences do not force
 vanishing active-span density.}
\]

Still open:

\[
 \mathfrak S_{\lceil A\sqrt r\rceil}=o_A(B_r)
\]

for the actual canonical PBBS quotient.  The remaining route is therefore
PBBS chronology/anticorrelation, not another local completion or cut-choice
argument.
