# Audit of the growing-uniformity Pippenger--Spencer claim and the annular leave

Date: 2026-07-26

## 0. Verdict

The proposed black-box application of Pippenger--Spencer is not valid.
The classical theorem has fixed uniformity, and the quantitative results of
Grable, Alon--Kim--Spencer, Vu, and Gould--Kelly retain explicit or hidden
dependence on the uniformity.  None of their published statements gives a
matching leave of order (N/\sqrt m) when the edge size grows like (m).

The underlying slow-bite idea remains live.  Marking at rate
(c/(kD)) would remove order (1/k) of the vertices per bite, so
(O(k\log m)) successfully regenerated bites would reach density
(m^{-1/2}).  Proving that regeneration uniformly is a new theorem; it is
not a corollary of the classical nibble.

Finally, correlating the root leave across annular ranks does not by itself
save a factor (\sqrt m).  In the synchronized common-core configuration
hypergraph that correlation is already built in, and the exact hole identity
still requires a root leave (o(N/\sqrt m)).

## 1. The quantifier error

The compact Pippenger--Spencer formulation is

> for every fixed (k) and fixed (\varepsilon>0), there is a
> (\delta=\delta(k,\varepsilon)>0) ... .

For a sequence (k=k(m)\to\infty), knowing only
(\Delta_2/D=O(m^{-2})\) does not imply

\[
   {\Delta_2\over D}<\delta(k(m),\varepsilon(m)).
\]

This would require a quantitative lower bound for
(\delta(k,\varepsilon)), uniform in (k).  The classical theorem supplies
none.

There cannot be a uniformity-free version depending only on
(\Delta_2/D=o(1)).  In the line hypergraph of a projective plane of order
(q),

\[
 N=q^2+q+1,\qquad k=D=q+1,\qquad \Delta_2=1,
\]

so (\Delta_2/D\to0), but every two edges meet and the maximum matching has
size one.  In particular, the asserted estimate

\[
 \varepsilon\lesssim(\Delta_2/D)^c+(\log N/D)^{c'}
\]

with absolute positive (c,c') is false.  Any growing-uniformity theorem
must charge additional (k)-dependent geometry.

The original Pippenger--Spencer abstract explicitly says "for some fixed
(k)".  The standard nearly-perfect-matching formulation likewise begins
"Let (r) be fixed".

## 2. The classical proofs do use the uniformity

Alon--Kim--Spencer prove, for a simple (k)-uniform regular hypergraph,

\[
  |V\setminus V(M)|=O_k\!\left(ND^{-1/(k-1)}\right)
  \qquad(k>3),
\]

where the implicit constants depend on (k).  Their one-bite theorem begins
"Let (k\ge3) be fixed" and chooses constants (K,D_{\min}) depending on
(k).  In their bite, an edge is marked with probability (1/D); the
one-bite covered fraction is asymptotic to (e^{-k}), not an
absolute-constant bite.  Their iteration therefore does not justify the
asserted replacement by (c/k) with absolute error bounds.

Grable's quoted quantitative leave is

\[
 O_k\!\left(
 N(D/\log N)^{-1/(2k-1+\varepsilon)}
 \right),
\]

again with (D) required to be sufficiently large as a function of
(k,\varepsilon).  Vu's bounds contain the same growing-uniformity
bottlenecks through the full codegree sequence.  The 2025 Gould--Kelly
theorem is stated under the hierarchy

\[
  1/D\ll1/A\ll\gamma\ll1/k,
\]

so it too is a fixed-(k) theorem, not a uniform theorem for
(k=\Theta(\log N)).

Thus a direct proof with bite probability (c/(kD)) may be possible because
our (D) is enormous, but it must track all (k)-dependence.  It cannot be
cited as Pippenger--Spencer "verbatim".

## 3. Keep the two catalogues distinct

For the repaired promotion-ring owner catalogue, the exact audited maximum
relative pair codegree is

\[
 {\Delta_2\over D}={2+o(1)\over m^2}.
\]

The antipodal (\Theta(1/m)) pair from the unrestricted wreath catalogue is
not present after the repair.  Hence the proposed correction from
(m^{-2}) to (m^{-1}) is wrong for this catalogue.

For the synchronized common-core tight-path configuration hypergraph, the
edge has a root plus

\[
 k=(\sqrt\pi+o(1))m^{3/2}
\]

target vertices, and vertical adjacent-rank pairs give

\[
 {\Delta_2\over D}=\Theta(1/m).
\]

These are different hypergraphs and their nibble thresholds cannot be
interchanged.

For the first Gaussian-annulus packet hypergraph itself, with packet size
(n=2m), the same exact computation gives

\[
 {\Delta_2\over D}={2\over(m-q_0)(m+q_0)}=(2+o(1))m^{-2}.
\]

The disjoint-pair ratio is exponentially smaller.  Thus the suggested
replacement by a (\Theta(1/m)) maximum is also false in that catalogue.
More importantly, the factor that a growing-rank theorem has to pay is not
just (\Delta_2/D): here

\[
 (2m){\Delta_2\over D}\log N_{q_0}\longrightarrow 8\log2,
\]

so the known variable-rank criterion is exactly constant-critical, not
clear by a factor (m^2).

## 4. The annular summation is critical

If a separate rank-(q) matching leaves
(\ell_q\asymp N_q/\sqrt m), then with (q=a\sqrt m) and
(N_q=(1+o(1))We^{-a^2}),

\[
 \sum_q\ell_q
  \asymp {1\over\sqrt m}\sum_q N_q
  \asymp W\int e^{-a^2}\,da
  =\Theta(W).
\]

So the user's critical-annulus arithmetic is correct for separate rankwise
leaves.

But making the missed roots identical at all ranks does not automatically
divide this by (\sqrt m), because targets at different ranks are distinct.
For the synchronized common-core configuration hypergraph, a matching (Q)
has the exact aggregate-hole identity

\[
 \mathfrak H(Q)=\Delta+k(N-|Q|),
 \qquad
 \Delta=o(W),\quad
 k=(\sqrt\pi+o(1))m^{3/2},\quad
 N=(1+o(1)){W\over m}.
\]

Thus a shared root leave (N-|Q|\asymp N/\sqrt m) gives

\[
 k(N-|Q|)=\Theta(W),
\]

not (O(W/\sqrt m)).  The exact sufficient and necessary scale for this
configuration formulation is

\[
             N-|Q|=o(N/\sqrt m).
\]

Correlation can still help only if it changes the per-missed-root target
cost (for example through a completion/absorber), not merely by choosing the
same missed roots at all depths.

## 5. Correct remaining theorem

The useful unresolved statement is therefore not classical PS, but a
catalogue-specific slow-bite theorem:

1. choose marks at rate (c/(kD));
2. prove degree and actual-link regeneration for (O(k\log m)) bites;
3. exploit the repaired path influence bound (which gives one-bite tails
   (e^{-\Omega(m^2)})); and
4. control the predictable accepted-loss drift, not only martingale noise.

For the repaired owner catalogue, an (o(N)) root leave suffices for the
owner packing.  For the synchronized all-rank configuration hypergraph, the
stronger (o(N/\sqrt m)) leave is required.  Neither conclusion currently
follows from a published black box.
