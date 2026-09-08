# Full-union shields localize every exterior splice casualty

**Date:** 2026-08-05  
**Method:** interval containment and an explicit Johnson geodesic; no
computation or search  
**Status:** unconditional deck-localization theorem and sharp owner-level
shield.  It reduces the unbounded exterior cone of a rethread to a finite
quadratic collar whenever full-ground shields are planted on both sides of
the cuts.  It does not plant those shields in the PBBS factor or preserve
the lower compiler.

## 1. Arc reassembly

Let `Omega` be a ground set and let `T` be a disjoint union of cyclic words
whose letters are subsets of `Omega`.  Cut the cycles at `q` directed cuts.
The cuts divide `T` into directed arcs.  Let `T'` be any other cyclic
reassembly of the same directed arcs; the order inside every arc is
unchanged.

For a cut `c`, let `L_c` be the incoming arc and `R_c` the outgoing arc in
the **old** reassembly.  Fix `H>=1` and assume:

1. every arc has at least `H` letters;
2. the last `H` letters of every incoming arc have union `Omega`; and
3. the first `H` letters of every outgoing arc have union `Omega`.

Call these terminal words the left and right full-union shields.

### Theorem 1.1 (quadratic exterior localization)

Every value in the interval-union deck of `T` which is absent from the deck
of `T'` has an old witness which crosses exactly one cut and uses fewer than
`H` letters on each side of that cut.  Consequently the number of
occurrence-labelled old intervals which can lose a non-full value is at
most

\[
                              qH^2.                           \tag{1.1}
\]

In particular, every interval with an endpoint outside the two adjacent
`H`-collars is automatically safe.

#### Proof

An interval contained in one directed arc is copied literally into `T'`.
Thus a lost witness crosses at least one cut.

Suppose first that it crosses two or more cuts.  Between the first two
crossed cuts it contains a complete directed arc.  That arc contains the
right shield after its first cut (and the left shield before its second),
so the interval union is `Omega`.  The value `Omega` is still witnessed by
every shield in `T'` and is not lost.

Now suppose the interval crosses exactly one cut `c`.  If it uses at least
`H` letters on the incoming side, it contains the complete left shield of
`c`; if it uses at least `H` letters on the outgoing side, it contains the
complete right shield.  In either case its value is `Omega` and survives.
Therefore a non-full casualty uses between one and `H-1` letters on each
side.  There are fewer than `H^2` endpoint pairs at one cut and `q` cuts,
which proves (1.1).  \(\square\)

The theorem is value-independent.  It applies simultaneously to every
upper rank and does not require a pre-existing multiplicity estimate for
individual targets.

## 2. One-sided shields need a separate endpoint bound

Suppose all affected intervals have a fixed orientation: they begin in an
incoming body and enter a moved continuation, but never use the reverse cut.
If only the first `H` letters of every possible continuation have union
`Omega`, then every non-full casualty uses fewer than `H` outgoing letters.
This localizes only the **outgoing** endpoint.  The incoming endpoint can
still be arbitrarily far from the cut.

Consequently a one-sided shield gives `qH^2` only under an additional
hypothesis that the incoming endpoint has at most `H` possible positions
(for example, it already lies in a protected `H`-collar or is one fixed
opening endpoint).  Without that hypothesis the correct address bound is

\[
             H\sum_c |L_c|,                                \tag{2.1}
\]

up to the harmless endpoint convention, and can be unbounded in the PBBS
body length.  Orientation by itself therefore does not halve the cyclic
shield interface.

## 3. The sharp owner-level full-union geodesic

Assume now that every letter is a rank-`r` owner and consecutive letters
must be Johnson neighbours.  Any owner interval with union `Omega` has at
least

\[
                              |\Omega|-r+1                    \tag{3.1}
\]

letters: the first owner contributes `r` coordinates and every Johnson step
introduces at most one new coordinate.

This bound is attained.

### Theorem 3.1 (sharp Johnson shield)

Put `n=|Omega|` and `h=n-r`.  Choose disjoint sets

\[
 X=\{x_1,\ldots,x_h\},\qquad
 Y=\{y_1,\ldots,y_h\},\qquad |K|=2r-n,
\]

whose union is `Omega`.  (In the central cases `2r>=n`.)  Define

\[
 T_j=K\cup\{y_1,\ldots,y_j\}
          \cup\{x_{j+1},\ldots,x_h\},
 \qquad 0\le j\le h.                                      \tag{3.2}
\]

Then:

1. every `T_j` has rank `r`;
2. `T_(j+1)=T_j-x_(j+1)+y_(j+1)`;
3. the `h+1=n-r+1` owners are distinct;
4. their union is `Omega`; and
5. all lower and upper q1 colours on the path are separately distinct.

Hence (3.2) is a shortest possible full-union owner shield.

#### Proof

The rank identity is

\[
             |K|+|X|=2r-n+n-r=r.
\]

The transition formula and distinctness are immediate.  Every `x_i` occurs
at the initial end and every `y_i` at the terminal end, while `K` is
permanent, so the complete union is `Omega`.

At transition `j`, the lower colour is

\[
 K\cup\{y_1,\ldots,y_j\}\cup\{x_{j+2},\ldots,x_h\},
\]

and the upper colour is that set together with
`x_(j+1),y_(j+1)`.  Their prefix/suffix indices recover `j`, proving both
injectivities.  Lower bound (3.1) proves sharpness.  \(\square\)

For the odd central owner layer `n=2m-1,r=m`, the shield has exactly `m`
owners and a one-coordinate permanent core.  For `n=2m,r=m`, it has
`m+1` owners and empty permanent core.

## 4. Consequence for the common-history `C8`

The common-history rethread has four changed hinges.  If the four old
continuation arcs are prospectively furnished with both prefix and suffix
full-union owner shields of length `H`, Theorem 1.1 replaces the present exponential
exterior cone by at most

\[
                              4H^2                            \tag{4.1}

\]

occurrence addresses.  The owner-level minimum is
`H>=k-r+1=Theta(k)`, and Theorem 3.1 attains it before residence collars and
factor planting are imposed.  Thus the shield route is polynomial, but it
is not an `O(d)` local graft: `d=Theta(sqrt k)` while the sharp full-union
shield has length `Theta(k)`.

There are generally eight oriented shield occurrences: one prefix and one
suffix on each of four arcs.  A bank of only four shields suffices only if
an additional construction makes the prefix and suffix requirements overlap
on every arc (for example, by making the complete arc itself one shield).
No such overlap is assumed here.

The exact remaining shield theorem is:

> Plant the eight oriented owner/q1-disjoint, depth-`d` resident shield
> occurrences required at the prefix and suffix ends of the four arcs (or
> prove a four-block overlap construction), attach them to the PBBS bodies,
> and retain the lower compiler and typed cap.

If that theorem is proved, arbitrary-width exterior upper preservation
reduces to a finite polynomial backup bank.  Neither the small protected
factor theorem (whose allowance is only `O(k)` incidences with a smaller
constant) nor the current PBBS relative-graft theorem supplies these
shields automatically.

## 5. Scope

Proved here:

1. exact localization of all long splice damage under full-union shields;
2. a quadratic address bound independent of upper rank; and
3. the shortest possible full-union Johnson shield.

Not proved here:

1. depth-`d` literal/source realization of all shields in one chronology;
2. protected factor extension of their union;
3. backup packing for the remaining `O(k^2)` local addresses;
4. lower/common-cap compatibility; or
5. any all-dimensional universal-word bound.

## 6. Dependencies

The unshielded exterior-cone gate is Section 6 of

`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`.

The arc theorem is applied here to the **rank-`r` owner chronology**.  Its
interval deck is the upper owner-OR deck.  A depth-`d` source antecedent for
the shield, source-interval preservation, and the strict-lower compiler are
not consequences of Theorem 1.1 or Theorem 3.1.
