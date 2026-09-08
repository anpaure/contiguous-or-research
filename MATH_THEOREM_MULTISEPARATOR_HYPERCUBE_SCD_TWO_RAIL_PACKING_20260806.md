# A hypercube matching spreads exact SCD two-rail charts over many separators

**Date:** 2026-08-06  
**Method:** tag-signature perfect matching, Vandermonde convolution, and
symmetric-chain decomposition on the bulk coordinates  
**Status:** unconditional all-depth marked-target packing with balanced
separator load, contained in one global saturated-chain decomposition with
the same top-aligned piece census as the symmetric-chain construction.  It
removes both the growing-uniformity target-matching gate and the
one-separator counting obstruction.  It does **not** yet realize the
required tag signatures and chart histories in one PBBS source trace.

## 1. Parameters and tag matching

Let the ground set be partitioned as

\[
 [n]=H\mathbin{\dot\cup}D\mathbin{\dot\cup}U,
 \qquad |H|=r,\quad |D|=p,\quad |U|=u=n-r-p.              \tag{1.1}
\]

The coordinates in \(H\) are selector tags, those in \(D\) are possible
separator coordinates, and \(U\) is the bulk.

Choose any map

\[
                         f:2^H\longrightarrow D.           \tag{1.2}
\]

For each selector signature \(\alpha\subseteq H\), match the two
\(D\)-signatures

\[
 S\longleftrightarrow S\cup\{f(\alpha)\}
 \qquad
 (S\subseteq D\setminus\{f(\alpha)\}).                    \tag{1.3}
\]

For fixed \(\alpha\), these edges form a perfect matching of the
\(p\)-cube.  Over all \(\alpha\), equation (1.3) is a perfect matching of
the complete \((r+p)\)-dimensional tag cube.  Its edge labels are the
separator coordinates \(f(\alpha)\).

## 2. Bulk SCD charts on every signature edge

Let cores have rank \(q\), and assume

\[
                         2q+d\le u.                         \tag{2.1}
\]

Fix **one** symmetric-chain decomposition of \(B(U)\), to be used for
every tag-signature edge below.

Fix one lower tag signature

\[
 E=\alpha\cup S,qquad b=f(\alpha)\notin E.                \tag{2.2}
\]

For every bulk set

\[
                         Q\in{U\choose q-|E|},              \tag{2.3}
\]

take the symmetric chain of this fixed SCD which contains \(Q\).
Condition (2.1) implies

\[
 2(q-|E|)+d\le u,                                          \tag{2.4}
\]

so this chain extends through a segment

\[
 Q=R_1\subset R_2\subset\cdots\subset R_{d+1}.             \tag{2.5}
\]

Define the two marked rails

\[
 \boxed{
 T_{0,j}=E\cup R_{j+1},
 \qquad
 T_{1,j}=E\cup R_j\cup\{b\}
 }
 \qquad(1\le j\le d).                                    \tag{2.6}
\]

They are the last two endpoint chains of the literal star word

\[
 E\cup Q\cup\{a_d\},\ldots,E\cup Q\cup\{a_1\},
 E\cup Q\cup\{b\},                                      \tag{2.7}
\]

where \(R_{j+1}=R_j\cup\{a_j\}\).

### Theorem 2.1 (multiseparator target packing)

All targets in (2.6), over every signature edge (1.3), every admissible
bulk core (2.3), and every depth \(1\le j\le d\), are pairwise distinct.

#### Proof

Different depths have different ranks.  Fix \(j\).

The intersection of \(T_{0,j}\) with the tag bank \(H\cup D\) is exactly
\(E\), while that of \(T_{1,j}\) is exactly \(E\cup\{b\}\).  Since (1.3)
is a matching of all tag signatures, targets belonging to different
signature edges cannot agree.

On one fixed signature edge, the \(T_{0,j}\)'s have distinct bulk parts
\(R_{j+1}\), and the \(T_{1,j}\)'s have distinct bulk parts \(R_j\),
because the truncated SCD chains are vertex-disjoint.  The two shores of
the edge have different tag signatures.  Thus no equality is possible.
\(\square\)

## 3. Exact census

For a fixed selector signature \(\alpha\), summing over the lower
\(D\)-signatures gives

\[
 \begin{aligned}
 N_\alpha
 &=\sum_{S\subseteq D\setminus\{f(\alpha)\}}
       {u\choose q-|\alpha|-|S|}\\
 &= {u+p-1\choose q-|\alpha|}.                            \tag{3.1}
 \end{aligned}
\]

The second line is Vandermonde's identity.  Summing over
\(\alpha\subseteq H\) gives another Vandermonde convolution:

\[
 \boxed{
 N_{\rm charts}
   =\sum_{\alpha\subseteq H}{u+p-1\choose q-|\alpha|}
   ={n-1\choose q}.}                                      \tag{3.2}
\]

Thus distributing the separators over an arbitrary hypercube matching
costs **no chart capacity at all** relative to the fixed-coordinate SCD
construction.  The bank has

\[
                         2{n-1\choose q}                    \tag{3.3}
\]

pairwise target-disjoint marked full pieces.

## 3A. One global chain decomposition contains every paired rail

The tag-edge construction is compatible with a global chain partition; no
post hoc completion of the selected rails is needed.

Fix one matched tag edge

\[
                         E\longleftrightarrow E\cup\{b\},   \tag{3.3A}
\]

and one bulk symmetric chain

\[
 C=(C_a,C_{a+1},\ldots,C_{u-a}).                            \tag{3.4A}
\]

Partition the product of this chain with the two tag signatures into

\[
 \begin{aligned}
 C_E^0={}&(E\cup C_a,\ldots,E\cup C_{u-a},
                         E\cup\{b\}\cup C_{u-a}),\\
 C_E^1={}&(E\cup\{b\}\cup C_a,\ldots,
                         E\cup\{b\}\cup C_{u-a-1}).
 \end{aligned}                                             \tag{3.5A}
\]

The second chain is omitted when empty. These are saturated chains and
partition all sets whose tag signature is one endpoint of (3.3A) and whose
bulk part lies on \(C\). The tag edges partition all tag signatures and
the bulk SCD partitions \(B(U)\); hence all chains (3.5A), over every edge
and bulk chain, form a chain decomposition of \(B_n\).

Now suppose a bulk chain contains the core-level set

\[
                         R_1=C_{q-|E|}.                      \tag{3.6A}
\]

Then the two rank-\((q+1),\ldots,q+d\) segments of (3.5A) are exactly

\[
 E\cup R_2,\ldots,E\cup R_{d+1}                            \tag{3.7A}
\]

and

\[
 E\cup\{b\}\cup R_1,\ldots,E\cup\{b\}\cup R_d.          \tag{3.8A}
\]

These are the two rails (2.6). Thus every selected chart is already a pair
of pieces in this one global chain decomposition.

### Theorem 3A.1 (no piece-count penalty in the deep band)

Use the odd merged-PBBS notation

\[
 n=2m+1,\qquad t=m-d,                                      \tag{3.9A}
\]

and assume

\[
                         r+p\le2d+3.                        \tag{3.10A}
\]

Every chain in (3.5A) which meets a rank at most \(t-1\) reaches rank
\(t-1\). Consequently, splitting the deep-band intersections of these
chains from the top into pieces of length at most \(d\) gives exactly

\[
 \boxed{
 P_{n,d}=\sum_{\substack{h\ge0\\hd<t-d-1}}
                   {n\choose t-hd-1},}                     \tag{3.11A}
\]

the same piece census as an SCD. In particular, (3.7A)--(3.8A) are actual
full pieces of the top slab \(q+1,\ldots,q+d\).

#### Proof

The top rank of a nonempty \(C_E^1\) is

\[
                         u-a+|E|\ge\lceil u/2\rceil,        \tag{3.12A}
\]

and \(C_E^0\) ends one rank higher. Since

\[
 u=n-r-p,
 \qquad r+p\le2d+3,                                       \tag{3.13A}
\]

one has

\[
                         \lceil u/2\rceil\ge m-d-1=t-1.    \tag{3.14A}
\]

Thus every chain which begins at or below \(t-1\) crosses rank \(t-1\).

Split every deep-band chain intersection downward from rank \(t-1\) in
blocks of \(d\) ranks. For a fixed \(h\), a chain has an \(h\)-th block
exactly when it contains rank \(t-hd-1\). The chain decomposition has one
vertex per chain at that rank, so the number of such chains is exactly
\(\binom n{t-hd-1}\). Summing over the nonempty blocks proves (3.11A).

For the top slab, \(q=m-2d-1\), so its ranks are
\(q+1=m-2d\) through \(q+d=m-d-1=t-1\). Equations
(3.7A)--(3.8A) are precisely the top blocks of their chains. \(\square\)

## 4. Balanced separator loads

Take

\[
                         r=\lceil\log_2p\rceil             \tag{4.1}
\]

and choose \(f\) so that its fibre sizes differ by at most one.  Put

\[
 w_a={n-r-1\choose q-a},\qquad0\le a\le r.                \tag{4.2}
\]

The number of charts labelled by a fixed separator \(b\) is

\[
                         N_b=\sum_{\alpha:f(\alpha)=b}w_{|\alpha|}.
                                                                    \tag{4.3}
\]

Assume the top PBBS range, where \(q=n/2-O(d)\),
\(d=\Theta(\sqrt n)\), and \(r=O(\log d)\).  Uniformly for
\(0\le a\le r\),

\[
 {w_a\over w_0}
 =\prod_{i=0}^{a-1}{q-i\over n-r-q+i}
 =\exp(O(r/d))=1+o(1).                                    \tag{4.4}
\]

Since every fibre of \(f\) has either
\(\lfloor2^r/p\rfloor\) or \(\lceil2^r/p\rceil\) members and
\(p\le2^r<2p\), every fibre is nonempty.  Equations (4.3)--(4.4) give the
proof-safe uniform lower bound

\[
 \boxed{
 N_b\ge(1-o(1)){N_{\rm charts}\over2p}
 }
 \qquad(b\in D).                                           \tag{4.5}
\]

The factor two is real when \(p\) is not a power of two: some fibres have
one selector signature and others have two.  Exact
\((1+o(1))/p\)-balance is therefore not claimed.  The lower bound (4.5)
is all that the theta subbank needs.

## 5. Top-slab theta subbank

Use

\[
 n=2m+1,qquad q=m-2d-1.                                  \tag{5.1}
\]

Then

\[
                         2q+d=n-3d-3.                       \tag{5.2}
\]

Condition (2.1) alone holds whenever \(p+r\le3d+3\).  To retain also the
global deep-band piece-census conclusion of Theorem 3A.1, impose the
slightly stronger hypothesis

\[
                         p+r\le2d+3.                        \tag{5.3}
\]

Let

\[
 \eta=4\sum_{a\ge1}e^{-4\pi a^2},                         \tag{5.4}
\]

fix any constant \(\varepsilon>0\), and take

\[
 p=\left\lceil(1+\varepsilon)\eta(d+1)\right\rceil,
 \qquad r=\lceil\log_2p\rceil.                            \tag{5.5}
\]

For all sufficiently large parameters, (5.3) holds.  Moreover

\[
 {N_{\rm charts}\over W}\longrightarrow{e^{-\pi}\over2},             \tag{5.6}
\]

so even the factor-two lower bound (4.5) supplies more than

\[
 {e^{-\pi}/4+o(1)\over p}W                                \tag{5.7a}
\]

charts for every separator.  Since \(e^{-\pi}/4>700\eta\), choose exactly
\(\lfloor\eta W/p\rfloor\) or \(\lceil\eta W/p\rceil\) charts from each
separator shore, for a total of

\[
                         (\eta+o(1))W                       \tag{5.7}
\]

charts, with the counts per separator differing by at most one.  Then

\[
 {\#\text{ chosen charts labelled }b\over W}
 \le {1+o(1)\over(1+\varepsilon)(d+1)}.                    \tag{5.8}
\]

Equation (5.8) is strictly below the fixed-separator spacing capacity of a
word of length \((1+o(1))W\).  Thus the same construction simultaneously
has:

1. enough charts to pay the complete theta reset deficit;
2. exact marked-target disjointness at all depths;
3. separator diversity \(p=\Theta(d)\); and
4. per-separator load below the literal spacing upper bound.

This is an integral theorem; no nibble, LLL, or growing-uniformity matching
result is used.

## 6. What remains physical

Theorem 2.1 chooses target chains and separator labels.  It does not yet
give one global source word.  A word realizing a selected chart at terminal
position \(e\) must satisfy, for its separator \(b\),

\[
 b\notin A_{e-d},\ldots,A_{e-1},qquad b\in A_e,            \tag{6.1}
\]

and must simultaneously realize the complete bulk/tag unions (2.6).
Different separators can interleave without violating the one-coordinate
spacing count, but their \(d\)-histories overlap.  The independently chosen
SCD segments need not agree on those shared source letters.

Therefore (5.8) removes a necessary counting obstruction but is not a
history-gluing theorem.  The exact next statement is:

> **Multiseparator common-history Euler theorem.**  Choose the balanced
> subbank (5.7) together with physical endpoint positions and antecedent
> letters so that every prescribed rail (2.6) is realized, all overlapping
> histories agree, and the resulting trace belongs to the PBBS owner
> envelope and one connected Euler component.

## 7. Scope

Proved here:

* exact all-depth target disjointness across \(\Theta(d)\) separator shores;
* exact total chart count \(\binom{n-1}{q}\);
* asymptotically balanced per-separator chart counts;
* a theta-sized subbank below every one-coordinate spacing capacity.

Not proved here:

* simultaneous realization of overlapping chart histories;
* compatibility with the fixed PBBS maximal envelope;
* owner/q1 palettes or connected Euler ordering;
* the short-piece/global compiler interface; or
* \(\nu(k)\le B(k)+O(1)\).

The former random all-depth matching gate is therefore replaced by one
much more structured physical problem: glue a balanced family of already
disjoint recursive-SCD rail pairs into the PBBS trace.
