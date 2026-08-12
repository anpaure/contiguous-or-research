# Audit of rainbow Johnson-path erosion transfer

## Verdict

The endpoint-capped erosion theorem, its cut-repair extension, and the
depth-one rainbow-forest OR word are correct.  In particular, the project's
already proved near-spanning two-sided-rainbow **linear** forest yields an
unconditional literal word of length `W+o(W)` covering the three central
ranks in every even dimension.

This removes the previously listed factorability and pin-survival gates at
depth one.  It does not prove the required multidepth path family.

## 1. Full-strip ceiling

For the earlier full cyclic-strip hypergraph,

\[
K=4\ell(J+1),\qquad
\Gamma/D\ge
\frac{2}{m+1}\exp(-O(J^2/m)).
\]

The ABKV hypothesis `e^(2K) Gamma logD=o(D)` implies

\[
8\ell J\le(1+o(1))\log m.
\]

If the word overhead vanishes, `J/ell->0`, and therefore

\[
J^2=(J/\ell)(\ell J)=o(\log m).
\]

Thus the `J=o(sqrt(log m))` ceiling is rigorous for this exact
full-strip/ABKV architecture.

## 2. Short-run collision lemma

Let a coordinate have an internal one-run on middle path vertices
`T_a,...,T_(a+r-1)`.  The transition into the run adds that coordinate, and
the transition out removes it.  Comparing

\[
\bigcap_{j=a-1}^{a+r-1}T_j
\quad\text{and}\quad
\bigcap_{j=a}^{a+r}T_j
\]

shows both set differences would have to consist of the run coordinate,
which is absent at the opposite endpoint.  Hence the intersections are
equal.  Different short runs map injectively to their `(start,length)`
adjacent-window collisions because a Johnson transition adds only one
coordinate.  Therefore

\[
\rho_H\le C_H.
\]

## 3. Endpoint-capped erosion identities

For one middle path `T_0,...,T_(L-1)`, define

\[
A_j=\bigcap_{i=\max(0,j-H)}^{\min(L-1,j)}T_i,
\qquad 0\le j\le L+H-1.
\]

Each entry is nonempty because at most `H` coordinates can be lost over an
`H`-edge window.  If there is no internal one-run of length at most `H`, the
following literal contiguous-union identities hold:

\[
T_i=\bigcup_{j=i}^{i+H}A_j,
\tag{3.1}
\]

\[
\bigcap_{s=0}^{q}T_{i+s}
=\bigcup_{j=i+q}^{i+H}A_j,
\qquad 0\le q\le H,
\tag{3.2}
\]

and

\[
\bigcup_{s=0}^{q}T_{i+s}
=\bigcup_{j=i}^{i+H+q}A_j.
\tag{3.3}
\]

For (3.1)--(3.2), take the one-run `[u,v]` containing the required middle
indices.  An internal run has length at least `H+1`, so there is an erosion
window `[j-H,j]` inside `[u,v]` with `j` in the displayed range.  Boundary
runs are handled by the truncated endpoint windows.  Equation (3.3) follows
by unioning the overlapping index ranges in (3.1).

Thus a path with `L` middle vertices costs exactly `L+H` entries and exposes
all of its correct-rank lower intersections and upper unions through depth
`H`.

For vertex-disjoint paths, appending omitted middle and shadow masks gives

\[
W+Hp+\sum_{q=1}^{H}(M_q^-+M_q^+).
\tag{3.4}
\]

## 4. Cut repair

Cut immediately before every short internal one-run begins.  No two such
runs begin at one transition, and cutting cannot create a new internal run.
The component count rises by at most `rho_H`.  At depth `q`, at most `q`
windows cross one cut on each of the lower and upper sides.  Applying (3.4)
after all cuts gives

\[
W+Hp+\sum_{q=1}^{H}(M_q^-+M_q^+)
 +(H^2+2H)\rho_H.
\tag{4.1}
\]

The coefficient is exact:

\[
H+2\sum_{q=1}^{H}q=H^2+2H.
\]

## 5. Exact depth-one word

For a nontrivial path component

\[
T_0,T_1,\ldots,T_\ell,
\qquad S_i=T_{i-1}\cap T_i,
\]

emit

\[
T_0,S_1,S_2,\ldots,S_\ell,T_\ell.
\tag{5.1}
\]

Every selected lower colour is literal.  Consecutive distinct facets give

\[
T_i=S_i\cup S_{i+1}
\]

for internal middle vertices.  For an internal edge, the three consecutive
facets `S_(i-1),S_i,S_(i+1)` have union `T_(i-1) union T_i`.  The first edge
uses `T_0,S_1,S_2`, the last uses
`S_(ell-1),S_ell,T_ell`, and a one-edge component uses its whole three-entry
block.  Hence every selected upper colour is also a contiguous OR.

If the forest has `e` edges and `c` nontrivial components, (5.1) has length
`e+2c`.  With distinct lower and upper colours, literal completion gives

\[
W+2(N-e)+c,
\qquad N=\binom{2m}{m-1}.
\tag{5.2}
\]

There is an equivalent endpoint-cap form which makes the spanning ledger
especially transparent.  For the same nontrivial path put

\[
 a_0=T_0\setminus T_1,
 \qquad a_\ell=T_\ell\setminus T_{\ell-1},
\]

and emit

\[
 a_0,S_1,\ldots,S_\ell,a_\ell.                  \tag{5.3}
\]

The endpoint middles are (a_0\cup S_1) and
(S_\ell\cup a_\ell); the internal middles and all upper colours use the
same two- and three-term identities as above.  For a spanning forest, add
each isolated middle vertex literally.  If (c_0) is the number of
isolated vertices, then

\[
 W=e+c+c_0
\]

and the pre-repair length of (5.3) is exactly

\[
 e+2c+c_0=W+c.                                   \tag{5.4}
\]

It already covers every middle set and all (e) selected lower and upper
colours.  Appending the (N-e) missing colours in each adjacent rank gives
the same exact completed length (5.2).  This formulation proves directly
that no endpoint pin or run condition is hidden in the depth-one transfer.

The trimmed one-coordinate lift of this word has length exactly twice the
even word and covers the four odd-dimensional ranks

\[
 m-1,m,m+1,m+2.
\]

Since

\[
 2\binom{2m}{m}
 =\binom{2m+1}{m}+{1\over m+1}\binom{2m}{m},
\]

the excess is one Catalan term, namely a (1/(2m+1)) fraction of the odd
width.  Thus the odd four-rank word also has length (W_{2m+1}+o(W_{2m+1})).

## 6. The required forest is genuinely available

The authoritative project statement is Section 47, items 203--205, of
`MATHEMATICAL_HANDOFF.md`, based on `ASYMPTOTIC_MATCHING.md`.  It constructs
a two-sided-rainbow linear forest with `W-o(W)` edges and `o(W)` components
after conflict-free matching and one-edge-per-cycle deletion.  Since

\[
N=W-\operatorname{Cat}_m=W-o(W),
\]

its edge count is also `N-o(W)`.  Substitution in (5.2) proves an actual
`W+o(W)` OR word for ranks `m-1,m,m+1`.

This must not be confused with the older Greene--Kleitman forest in Section
39: that explicit forest branches heavily and cannot be linearized after
only `o(W)` deletions.  The later conflict-free near-rainbow forest is the
one used here.

## 7. Remaining multidepth gate

At a tail-compatible depth `H`, it now suffices to construct vertex-disjoint
Johnson path families satisfying

\[
Hp+\sum_{q=1}^{H}(M_q^-+M_q^+)
 +(H^2+2H)\rho_H=o(W).
\]

This condition permits global nonmiddle duplicates; only missing distinct
shadows and local short coordinate runs are charged.  It remains unproved.
