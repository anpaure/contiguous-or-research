# Independent audit of the post-hoc vertical-rounding obstruction

## Verdict

The depth-two obstruction is mathematically sound.  In particular, the
following conclusions survive the audit:

\[
 \mathbb E E_2\le {W\over m(m-1)},\qquad E_2=o(W)\quad\hbox{with high
 probability},
\]

the certified depth-two ledger forces (R_2=(1-o(1))W), every unaltered
post-hoc queue packing has ((1-o(1))W) high components, and any alteration
producing (o(W)) components must touch at least
((1/2-o(1))W) center annotations.

All precision corrections identified below were applied to the final theorem
note: it now uses the relaxed forced-prefix graph, states mutual tuple
independence and `r<m`, adds the McDiarmid bound, restricts the power-law
all-depth shorthand to fixed `q`, and formulates alteration using final high
radii and the adaptive maximal graph.  A final reinspection found no remaining
mathematical error.

There are, however, several exactness and scope corrections worth making.

## 1. Rotor transition law

For consecutive queue centers

\[
S=\{z_t,\ldots,z_{t+m-1}\},\qquad
S'=\{z_{t+1},\ldots,z_{t+m}\},
\]

the forced relations

\[
 S'=S-\{x_0\}+\{a\},\qquad
 (y'_1,\ldots,y'_e)=(x_0,y_1,\ldots,y_{e-1})
\]

and, when (e<r),

\[
 (x'_0,\ldots,x'_{e-1})=(x_1,\ldots,x_e)
\]

are exact.

When (e=r), the displayed prefix condition

\[
 (x'_0,\ldots,x'_{r-2})=(x_1,\ldots,x_{r-1})
\]

is necessary but is not by itself the full transition condition.  If
(r<m), the final new lower flag is (z_{t+r}), so it must lie in

\[
 S\setminus\{x_0,\ldots,x_{r-1}\};
\]

in particular it cannot be the incoming coordinate (a=z_{t+m}).  If
(r=m), the remaining new lower coordinate is automatically (a).

Accordingly, there are two clean ways to state the theorem.

1. Define (E_2) to be the **relaxed forced-prefix graph**.  Every genuine
   rotor transition is an edge of this graph, which is all the later path
   arguments need.  Then the probability in the equal-radius case is exactly
   the displayed forced-prefix probability.
2. Define (E_2) using genuine transitions.  Then the displayed probability
   is an upper bound, rather than an exact value.  For (r=e<m), the exact
   value (when the prescribed coordinates are legal) has the additional
   factor
   
   \[
     {m-r\over m-r+1}.
   \]

The current proof remains valid because it only needs an upper bound and a
necessary graph.  The title “exact rotor transition law” and the phrase
“either zero or” the value in (14) should be adjusted to remove the ambiguity.

The product probabilities also use mutual independence of the lower and
upper ordered tuples at a fixed center.  This is evidently intended, but it
should be stated explicitly alongside independence across centers.

## 2. Compatibility probability

Fixing a tail of radius (r\ge2), there are at most (m) possible incoming
coordinates.  For a head of radius (e\le r), the forced-prefix probability
is

\[
 {1\over (m)_e^2}\quad(e<r),
 \qquad
 {1\over (m)_{r-1}(m)_r}\quad(e=r).
\]

Both are at most

\[
 {1\over m^2(m-1)},
\]

with the relaxed maximum at (r=e=2).  Hence

\[
 \mathbb E E_2\le {R_2\over m(m-1)}\le {W\over m(m-1)}.
\]

The adaptive-radius maximal graph is also correct: after independently
sampling an ordered lower pair and upper pair at every center, every genuine
future high transition must satisfy

\[
 x'_0=x_1,\qquad (y'_1,y'_2)=(x_0,y_1),
\]

whose probability for a fixed incoming coordinate is
(1/[m^2(m-1)]).  Thus choosing the high-center set after observing the
flags does not evade the estimate.

The introduction currently says that (E_2=O(W/m^2)) with high probability,
whereas the written Markov argument proves only (E_2=o(W)) with high
probability.  Either weaken the introduction to the proved statement or add
the following bounded-differences observation.  Changing one center's
annotation affects at most (m) possible outgoing and (m^2) possible
incoming directed Johnson-neighbor pairs.  McDiarmid's inequality therefore
gives, for example,

\[
 \Pr\left(E_2>{2W\over m(m-1)}\right)
 \le \exp\bigl(-\Omega(W/m^8)\bigr).
\]

This supplies the stronger introductory claim.

The all-depth estimate

\[
 \mathbb E E_q\le
 |\{S:r(S)\ge q\}|{m\over (m)_{q-1}(m)_q}
\]

is exact as an upper bound.  Its subsequent notation
(O(Wm^{-2q+2})) is valid for fixed (q), but not uniformly for growing
(q).  It should be qualified as fixed-depth asymptotics or replaced by the
falling-factorial expression.

## 3. Certified ledger

If every middle center is owned once and supplies exactly one certified
depth-two lower occurrence precisely when its radius is at least two, then

\[
 T_2^-=R_2.
\]

The exact deficit identity gives

\[
 R_2=N_2+D_2^--M_2^-,
\]

and

\[
 {N_2\over W}={m(m-1)\over(m+1)(m+2)}=1-O(1/m).
\]

Thus (D_2^-+M_2^-=o(W)) implies
(R_2=(1-o(1))W).  No sign or ownership error is present.  It would help to
say explicitly that “duplicate plus missing” refers to the certified
occurrence ledger, not incidental OR values of the eventual literal word.

## 4. Components and reset cost

Along a nonincreasing-radius queue atom, the high centers form an initial
segment.  A segment with (k) high centers uses (k-1) distinct directed
edges of the relaxed compatibility graph.  Vertex-disjointness therefore
gives

\[
 R_{2,\mathrm{cov}}-p_2\le E_2,
\]

and hence (p_2=(1-o(1))W).

The numerical reset lower bound applies to the separately initialized
standard literal atom.  Its exact formula

\[
 \#\text{centers}+2d_0+1
\]

assumes (d_0<m), so that the reset/core entries are nonempty.  This is the
regime used in every growing central band, but it should be stated.  The
argument is not a lower bound for arbitrary shared-reset words, and the note
correctly excludes those in its final scope paragraph.

## 5. Alteration bound

After deleting the altered centers from (p) final paths, there are at most
(p+|C|) surviving unaltered high runs.  If (U) unaltered high centers
survive, those runs contain at least

\[
 U-(p+|C|)
\]

original compatible edges.  Therefore

\[
 U\le E_2+p+|C|.
\]

At most (|C|) additional covered high centers are altered, yielding

\[
 (1-o(1))W\le E_2+p+2|C|.
\]

The claimed ((1/2-o(1))W) alteration lower bound is correct.

For complete precision, “high centers” should mean centers of final radius
at least two, and (C) should include every center at which the radius or
either relevant ordered depth-two flag is changed.  When the initial radii
are themselves selected after the flags, (E_2) in this argument should be
the adaptive maximal forced-prefix graph.

## Bottom line

No correction changes the substantive obstruction.  Independent vertical
annotations leave only (o(W)) usable high adjacencies, while a near-lossless
depth-two ledger needs ((1-o(1))W) high centers.  The post-hoc path packing
therefore has linearly many components, and repairing it into (o(W))
components requires changing a linear number of center annotations.
