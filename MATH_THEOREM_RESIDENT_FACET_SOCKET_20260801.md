# Resident facet sockets for repairing one missing immediate-upper colour

Date: 2026-08-01  
Status: corrected unconditional local owner-layer theorem.  The original
version omitted boundary-cleanliness obligations for endpoint-zero and
outside-target coordinates; the exact conditions are now included below.
No global extraction, upper-deck preservation, path ordering, or lower-
compiler conclusion is claimed.

## 1. Statement

Let `h>=1`, let `U` be an `(r+1)`-set, and assume

\[
                              r\ge 2h+1.                 \tag{1.1}
\]

Choose distinct labels

\[
                  u_0,u_1,\ldots,u_{2h+1}\in U
\]

and put

\[
                  F_j=U\setminus\{u_j\},
                  \qquad 0\le j\le 2h+1.               \tag{1.2}
\]

Then the owner block

\[
                         F_0,F_1,\ldots,F_{2h+1}         \tag{1.3}
\]

has the following properties.

1. Its owners are distinct rank-`r` sets.
2. Every immediate upper colour is `U`:
   \[
                         F_j\cup F_{j+1}=U.              \tag{1.4}
   \]
3. Its `2h+1` immediate lower colours
   \[
             F_j\cap F_{j+1}=U\setminus\{u_j,u_{j+1}\} \tag{1.5}
   \]
   are pairwise distinct rank-`(r-1)` sets.
4. There is no strict internal positive coordinate run of length below
   `h+1`.  Write `ell(x)` for the positive suffix age immediately to the
   left of the block and `rho(x)` for the positive prefix age immediately
   to its right.  Call an age **clean** when it belongs to
   `{0} union [h+1,infinity)`.  The nontrivial staircase obligations are:
   \[
   \begin{array}{ll}
   u_j\ (1\le j\le h):
      &\text{left suffix age at least }h+1-j,\\[2mm]
   u_j\ (h+1\le j\le2h):
      &\text{right prefix age at least }j-h.
   \end{array}                                           \tag{1.6}
   \]
   In addition, `ell(u_0)` and `rho(u_(2h+1))` must be clean, and both
   `ell(x),rho(x)` must be clean for every `x notin U`.

Consequently, if the neighboring owner pieces supply the ages in (1.6)
and the displayed cleanliness conditions, the concatenated chronology is
depth-`h` resident across the whole socket.
The block realizes the missing upper target `U` at every one of its
`2h+1` seams while also providing `2h+1` distinct lower colours.

### Compact two-sided form

There is also a shorter socket when both exterior guards are available.
Choose only distinct labels `v_0,...,v_h in U` and use

\[
                    U-v_0,U-v_1,\ldots,U-v_h.           \tag{1.7}
\]

The coordinates in `U-{v_0,...,v_h}` have an internal all-one run of
exactly `h+1`, so they are automatically safe.  The exact exported ages
are

\[
\begin{array}{ll}
v_j\ (1\le j\le h):
   &\text{left suffix age at least }h+1-j,\\[1mm]
v_j\ (0\le j<h):
   &\text{right prefix age at least }j+1.
\end{array}                                             \tag{1.8}
\]

In addition to (1.8), `ell(v_0)` and `rho(v_h)` must be clean, and both
`ell(x),rho(x)` must be clean for every `x notin U`.  Under these exact
conditions, the compact block is resident, realizes `U` on all `h`
internal seams, and supplies `h` distinct rank-`(r-1)` intersections.  It
uses only `h+1` owner facets; unlike the `2h+2` form, its middle omitted
labels require extension from both sides.

## 2. Proof

Properties 1 and 2 are immediate from (1.2).  For property 3, equality of
two values in (1.5) would give equality of their two-element deleted-label
sets.  Two different edges of the simple label path

\[
                  u_0-u_1-\cdots-u_{2h+1}
\]

cannot have the same unordered endpoint pair, so all lower colours are
different.

For residence, a coordinate outside `U` has the all-zero trace.  A
coordinate in `U-{u_0,...,u_(2h+1)}` has the all-one trace and simply
transmits the incoming positive run through the socket.  Finally, the trace
of `u_j` is one at every position except `j`.  Its two positive pieces have
lengths

\[
                              j,\qquad 2h+1-j.           \tag{2.1}
\]

For `j=0` or `j=2h+1`, the nonempty piece has length `2h+1>=h+1`.
For `1<=j<=h`, the right piece has length at least `h+1`, while the left
piece needs exactly `h+1-j` further occurrences from the preceding
chronology.  For `h+1<=j<=2h`, the left piece has length at least `h+1`,
while the right piece needs exactly `j-h` further occurrences from the
following chronology.  The zero at the first position terminates any
incoming `u_0` run, and the zero at the last position precedes any outgoing
`u_(2h+1)` run; those exterior runs must therefore be clean.  A coordinate
outside `U` sees zeros throughout the socket, so its two exterior runs are
also separated and must each be clean.  This proves the corrected (1.6)
interface and exhausts all coordinate runs.

For the compact form (1.7), the trace of `v_j` has positive pieces of
length `j` and `h-j`.  The first needs `h+1-j` occurrences from the left
when nonempty, and the second needs `j+1` occurrences from the right when
nonempty.  For `v_0`, the incoming run is terminated immediately and
must be clean; for `v_h`, the outgoing run starts after the terminal zero
and must be clean.  Every coordinate outside `U` again sees only zeros and
needs cleanliness on both sides.  Every unselected label of `U` has trace
`1^(h+1)` and is automatically safe.  This proves the corrected compact
interface; the palette claims follow from the same calculation as
(1.4)--(1.5).

The omitted cleanliness is essential.  Already for `h=1`, an outside-`U`
coordinate with a one-owner positive suffix on the left is followed by a
socket zero, creating a strict internal run of length one.  Likewise a
one-owner incoming `v_0` run is terminated by the first compact facet.

## 3. The k=17 calibration

For `k=17`, `r=9`, and `h=3`, condition (1.1) holds.  A socket uses eight
facets of a missing rank-10 colour `U`:

\[
                 U-u_0,U-u_1,\ldots,U-u_7.              \tag{3.1}
\]

The non-clean staircase entries are

\[
\begin{array}{c|ccc}
\text{left label}&u_1&u_2&u_3\\
\text{required age}&3&2&1
\end{array}
\qquad
\begin{array}{c|ccc}
\text{right label}&u_4&u_5&u_6\\
\text{required age}&1&2&3.
\end{array}                                             \tag{3.2}
\]

together with cleanliness of the left `u_0` age, the right `u_7` age,
and both exterior ages of every coordinate outside `U`.

Thus each of the fourteen cut colours left unsupported by the current
all-minimum-fragmentation one-seam relaxation has a constant-size candidate
macro shape.  Extracting eight arbitrary owners can require at most sixteen
new cuts, so fourteen disjoint sockets have the crude scalar bound `224`,
below the current `1120` lower-cell reserve.  This scalar observation is not
a construction: facet overlap, newly destroyed upper witnesses, the global
piece order, and the literal lower compiler must all still be audited.

The compact version uses four facets

\[
                       U-v_0,U-v_1,U-v_2,U-v_3           \tag{3.3}
\]

with exact guards

\[
\begin{array}{c|ccc}
\text{left label}&v_1&v_2&v_3\\
\text{required age}&3&2&1
\end{array}
\qquad
\begin{array}{c|ccc}
\text{right label}&v_0&v_1&v_2\\
\text{required age}&1&2&3.
\end{array}                                             \tag{3.4}
\]

together with cleanliness of the left `v_0` age, the right `v_3` age,
and both exterior ages outside `U`.

Its crude extraction bound is eight cuts per target, or `112` for fourteen
disjoint sockets.  Whether the required two-sided exterior guards coexist
with a low-casualty extraction is a finite incidence question, not part of
the local theorem.

## 4. Scope boundary

The theorem is an accepting local socket, not a deck-transparent move.
Removing its facets from an incumbent chronology can destroy unique upper
witnesses, and the same rank-`r` facet cannot be used in two sockets.  A
global application therefore needs either already exposed compatible
segments or a correlated extraction-and-rethread theorem charging every
new casualty.  The exact protected Hall, extraction, branching, topology,
and two-stratum interface is recorded in
`MATH_THEOREM_RESIDENT_FACET_SOCKET_PROTECTED_EXTRACTION_AND_CASCADE_20260801.md`.
