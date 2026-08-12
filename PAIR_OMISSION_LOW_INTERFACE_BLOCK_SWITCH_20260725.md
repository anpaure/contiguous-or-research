# A low-interface block-switch theorem for clustered token matchings

Date: 2026-07-25

This note gives a rigorous positive theorem suggested by the clustered
barycenter identity.  It separates the remaining proof into two explicit
hypotheses:

1. a midpoint-plus-component-variance estimate in the weighted flag space;
2. a low-interface condition saying that the legal alternating components
   occur in long intervals of the physical source rows.

Under those hypotheses, one componentwise switch is simultaneously an
exact central matching, a low-run physical carrier, and an (o(W))-defect
multidepth object.

The note also proves a rigidity lemma: changing only the embedding of a
fixed long central owner block changes no interior flags.  Thus useful long
block switches must alter the central owner path itself; parallel row labels
can only make collar corrections.

## 1. Weighted flag space

Let \(\Omega\) be the disjoint union of all signed flag-target sets through
depth \(H\).  Give target coordinates at depth \(q\) a nonnegative weight
\(w_q\), for example the audited overload weight \(1/c_q\) or the
floor-corrected quadratic weight.

For a lower-saturating token matching \(M\), write \(\mu(M)\in
\mathbb R^\Omega\) for its complete flag-load vector and \(\lambda\) for
the forced uniform mean vector.  Put

\[
 \|z\|_w^2=\sum_{\omega\in\Omega}w(\omega)z(\omega)^2.
\tag{1.1}
\]

The raw quadratic energy is

\[
 Q(M)=\|\mu(M)-\lambda\|_w^2.
\tag{1.2}
\]

Let \(B\) be the sum of the exact integer floors in the same weights.  The
floor-corrected energy

\[
 \Phi(M)=Q(M)-B\ge0
\tag{1.3}
\]

dominates the required weighted overload, by the already proved scalar
floor identity.

## 2. Legal alternating components

Let \(M,N\) be two matchings of the token bipartite graph which saturate the
same lower vertex set.  Their symmetric difference is a disjoint union of
even alternating cycles and even alternating paths whose endpoints lie on
the middle side.  Denote these components by \(K\).

For each component, let

\[
 \Delta_K=\mu(N\cap K)-\mu(M\cap K).
\tag{2.1}
\]

Choose independently for every \(K\) either its \(M\)-side or its
\(N\)-side.  With signs \(\varepsilon_K\in\{-1,+1\}\), the resulting set
\(M_\varepsilon\) is again a lower-saturating middle-simple matching and

\[
 \boxed{
 \mu(M_\varepsilon)
 =\frac{\mu(M)+\mu(N)}2
 +\frac12\sum_K\varepsilon_K\Delta_K.}
\tag{2.2}
\]

This is an exact integral switch, not a fractional rounding.

## 3. A concrete row-interface parameter

For every physical source row \(R\), record the two binary membership
strings

\[
 x^M_R(i)={\bf1}_{\{e_{R,i}\in M\}},\qquad
 x^N_R(i)={\bf1}_{\{e_{R,i}\in N\}}.
\]

Linearly cut the cyclic row once.  Partition it into the minimum number
\(I_R(M,N)\) of consecutive intervals on each of which

1. the pair \((x^M_R(i),x^N_R(i))\) is constant; and
2. if this pair is \((1,0)\) or \((0,1)\), all tokens in the interval belong
   to the same alternating component \(K\).

Put

\[
 I(M,N)=\sum_R I_R(M,N).
\tag{3.1}
\]

### Lemma 3.1 (interface-to-runs)

For every component-side choice,

\[
 \boxed{J(M_\varepsilon)\le I(M,N).}
\tag{3.2}
\]

### Proof

On one interval of the defining partition, the chosen-child membership bit
is constant: it is constantly zero, constantly one, or is determined by one
fixed component sign.  Hence a selected run can begin only at the first
position of one of these intervals.  Sum over rows.  \(\square\)

The condition

\[
 I(M,N)=o(W/H)
\tag{3.3}
\]

is the exact long-block hypothesis.  It is stronger than merely requiring
\(J(M),J(N)=o(W/H)\): the alternating-component labels themselves must not
oscillate rapidly inside the old runs.

## 4. One-shot low-interface switching theorem

### Theorem 4.1

Suppose two lower-saturating token matchings \(M,N\) satisfy

\[
 I(M,N)=o(W/H)
\tag{4.1}
\]

and

\[
 \boxed{
 \left\|
 \frac{\mu(M)+\mu(N)}2-\lambda
 \right\|_w^2
 +\frac14\sum_K\|\Delta_K\|_w^2
 \le B+o(W).}
\tag{4.2}
\]

Then some legal componentwise child \(M_\varepsilon\) satisfies

\[
 J(M_\varepsilon)=o(W/H),
 \qquad
 \Phi(M_\varepsilon)=o(W).
\tag{4.3}

Consequently its physical pair-row word has length \(W+o(W)\) after the
audited literal repairs and tails.

### Proof

Choose the component signs independently and uniformly.  Orthogonality of
the signs in (2.2) gives

\[
 \mathbb E Q(M_\varepsilon)
 =left\|
 \frac{\mu(M)+\mu(N)}2-\lambda
 \right\|_w^2
 +\frac14\sum_K\|\Delta_K\|_w^2.
\tag{4.4}
\]

By (4.2), \(\mathbb E\Phi(M_\varepsilon)=o(W)\).  Since \(\Phi\ge0\),
some deterministic sign choice has \(\Phi=o(W)\).  Lemma 3.1 gives the run
bound for every sign choice.  The literal consequence is the clustered
token transfer theorem.  \(\square\)

This theorem is deliberately one-shot.  It avoids the accumulation of row
interfaces which occurs if a heat-bath contraction is iterated without a
separate laminarity theorem.

## 5. A checkable overlap form of the variance hypothesis

For a component \(K\) and depth \(q\), let \(A_{K,q}\) and \(B_{K,q}\)
be the two multisets of flag targets contributed by its two sides.  If both
are simple at that rank and their symmetric difference has size
\(r_{K,q}\), then

\[
 \|\Delta_{K,q}\|_2^2=r_{K,q}.
\tag{5.1}
\]

More generally, (5.1) is an upper bound with the right side replaced by the
squared multiplicity discrepancy.  Therefore the explicit sufficient
overlap condition

\[
 \sum_{K,q}w_q r_{K,q}=o(W)
\tag{5.2}
\]

reduces (4.2) to the midpoint estimate

\[
 \left\|
 \frac{\mu(M)+\mu(N)}2-\lambda
 \right\|_w^2\le B+o(W).
\tag{5.3}
\]

In words: the two matchings must have a nearly balanced average, and the
two sides of each legal long switch must agree on almost all weighted flag
targets.  This is stronger and more geometric than a maximum-codegree
condition.

## 6. Rigidity of a fixed central block

The most tempting way to force (5.2) is to use two different row embeddings
of the same long central token block.  Such a switch cannot alter the bulk
flags.

### Proposition 6.1 (central-block rigidity)

Let

\[
 Y_a,Y_{a+1},\ldots,Y_{a+\ell-1}
\]

be a support-separated tight path of \(m\)-sets.  The ordered central path
determines every lower and upper flag whose witness is contained at distance
at least \(H\) from the two ends.  Consequently two physical embeddings of
the same central block can differ only in the \(H\)-collars of the block.

### Proof

Every transition determines its departing and arriving coordinates:

\[
 d_i=Y_i\setminus Y_{i+1},\qquad
 a_i=Y_{i+1}\setminus Y_i.
\tag{6.1}
\]

Support separation says these are the successive symbols of the unique
tight coordinate word, up to the irrelevant ordering of coordinates which
never reach the observed block.  For an interior start,

\[
 L_q=\bigcap_{j=0}^qY_{i+j},
 \qquad
 U_q=\bigcup_{j=0}^qY_{i+j}
\tag{6.2}
\]

uses only central owners inside the displayed block when \(q\le H\).
Hence it is fixed by the central path.  \(\square\)

Thus a parallel-embedding switch has excellent component overlap, but its
total adjustable weighted flag mass is only in the collars.  With
\(W/\ell\) blocks it can change at most \(O(WH/\ell)\) start-depth
positions.  If \(\ell\gg H\), this is (o(W)) at each fixed depth and
cannot correct an initial \(\Theta(W)\) bulk defect.

Useful long switches must therefore change the central owner path on a
positive fraction of their interiors while arranging substantial *target*
overlap between the two flag multisets.  This is the concrete structural
content missing from a generic vector-balancing argument.

## 7. Status for pair-omission rows

Theorem 4.1 is fully applicable to pair-row tokens once a pair \(M,N\) with
(4.1)--(4.2) is constructed.  The current first-avoided orbit gives many
low-run matchings with the correct barycenter, but coordinate relabelling
preserves each individual load histogram.  For a generic relabelling, the
two component sides have essentially disjoint deeper flag targets, so the
sum in (5.2) is of order the full weighted flag mass rather than (o(W)).

No pair of first-avoided orbit matchings satisfying both the low-interface
condition and the component-overlap condition is presently proved.  The
positive remaining construction is now exact:

\[
 \boxed{
 \begin{array}{c}
 \text{find two structurally different clustered matchings with a balanced
 midpoint,}\\
 \text{whose alternating components are long row blocks and whose two
 sides}\\
 \text{have }o(W)\text{ total weighted flag symmetric difference.}
 \end{array}}
\tag{7.1}
\]

Under precisely those verifiable hypotheses, Theorem 4.1 completes the
constant-one construction.
