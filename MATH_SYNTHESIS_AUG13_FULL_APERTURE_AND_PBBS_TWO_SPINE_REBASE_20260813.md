# Two exact central spines and the remaining correlation theorem

**Date:** 2026-08-13  
**Status:** proof-status synthesis; no unconditional `B(k)+O(1)` conclusion
is claimed

## 0. Target and corrected accounting

Let

\[
 R=\lceil k/2\rceil,\qquad W=\binom kR,\qquad
 d=\min\left\{t:tW+\binom{t+1}{2}\ge
          \sum_{j<R}\binom kj\right\},              \tag{0.1}
\]

and `B(k)=W+d`.  The open objective is

\[
                         \nu(k)\le B(k)+O(1).        \tag{0.2}
\]

Topology defect is counted in excess of one component: defect zero means
one nonempty Euler component.

The old principal uncertainty was whether the middle owners admit any
positive integral factor compatible with the lower rows.  That uncertainty
has now been removed twice, in two different architectures.  Each exact
spine fails at a different subsequent correlation.

## 1. Spine A: full-aperture MSW factor

Put `q=d+1`.

### 1.1 Odd dimension

For `k=2m+1`, `R=m+1`, take an MSW factor of the `m`-sets into cyclic
`m`-window decks.  On one cyclic order define source letters

\[
                         A_i=I_i^{m-q+2}.            \tag{1.1}
\]

Then

\[
 \bigcup_{j=0}^{q-1}A_{i+j}=I_i^{m+1},\qquad
 \bigcup_{j=0}^{q-2}A_{i+j}=I_i^m.                 \tag{1.2}
\]

Complementation and the MSW factor theorem prove that the first row
partitions every rank-`m+1` owner and the second partitions every rank-`m`
target, both exactly.  Coordinate owner traces are

\[
                         1^{m+1}0^m,                 \tag{1.3}
\]

so the cycles are biresident far beyond the required threshold `q`.

### 1.2 Even dimension

For `k=2m`, fix `x` and use an MSW factor on the remaining `2m-1` points.
The two source shores

\[
 A_i^0=I_i^{m-q+1},\qquad
 A_i^1=\{x\}\cup I_i^{m-q}                         \tag{1.4}
\]

partition respectively the rank-`m` owners avoiding and containing `x`.
The no-`x` rank-`m-1` lower shore is also exact.  The with-`x` lower shore
is the concrete second-shadow row `x+I^{m-2}` and is not automatically
surjective.

Thus exact positive owner rounding is no longer open in either parity.

### 1.3 The upper row is chronology-rigid

For one coordinate, every flat inverse of the trace (1.3) has source
support on one safe interval `E`, contains both endpoints of `E`, and has
successive support gaps at most `q`.  Therefore every proper source cell
of length at least `q` which intersects `E` contains a forced support
point.  Equivalently, on every long cell

\[
                         M_C=U_C.                    \tag{1.5}
\]

All owner and strict-upper interval unions are consequently determined by
the owner chronology, independently of source-letter capping.  In
particular the immediate-upper row is exactly the cyclic `(m+2)`-interval
deck.

This proves that upper completion cannot be postponed to the lower compiler
or the common cap.

### 1.4 Canonical MSW fails linearly

The canonical MSW orders miss at least

\[
 (m-3)\operatorname {Cat}_{m-2}-{2W\over m+2}
       =\left({1\over32}-o(1)\right)W               \tag{1.6}
\]

rank-`m-1` cyclic intervals, equivalently immediate-upper rank-`m+2`
targets.  Hence no bounded or polynomial local patch of the canonical
orders can work.  A proof using Spine A needs a globally different wreath
factor or a Catalan-scale coherent rethread.

### 1.5 Target capacity is not the obstruction

In the inclusion graph between rank `m-1` targets and rank `m` owners,
König edge-colouring gives two matchings saturating all targets.  Pairing
their two parents gives one Johnson edge of every intersection colour and
owner degree at most two.  The resulting graph has exactly

\[
                   W-\binom{2m+1}{m-1}={2W\over m+2}             \tag{1.7}
\]

path/isolate components; cycles may also occur.  Independently, a Rado
argument selects one edge of every colour as a forest.  Thus ordinary
Hall, owner capacity, and graphic rank all pass.  The open statement is
their joint chronological completion into a shadow-covering wreath factor
or double-turn Middle Levels chronology.

At `m=4` such a noncanonical factor exists explicitly, so there is no
universal divisibility obstruction.

## 2. Spine B: PBBS all-depth factor

Let `f` be the canonical periodic box-ball permutation of the middle
`m`-sets and set `g=f^2`.  The antipodal two-matching lift

\[
 M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c             \tag{2.1}
\]

is an exact incidence two-factor.  After suppressing the rank-`m` shore,
every rank-`m` lower colour occurs exactly once.

### 2.1 All-depth support is already exact

Along the directed `g`-cycles, for every `1<=s<=m` and every rank-`m-s`
target `S`, there is an `(s+1)`-owner intersection equal to `S`; the
correct-rank load lies between `1` and `binom(2s+1,s)`.  Complementation
gives the upper tower.  At depth one the bare centered PBBS factor has
angle loads between one and three, so every immediate shadow target is
covered.

Thus PBBS solves the support problem which canonical MSW fails.

### 2.2 The exact PBBS obstruction is residence/serialization

PBBS components can have length a multiple of `2m+1`, and their coordinate
traces can have positive runs shorter than `q`.  All-depth support alone
does not imply a flat antecedent.  If `nu_H` is the maximum number of
edge-disjoint positive runs of length at most `H`, the established literal
compiler ledger is

\[
 L_H\le W+2H\operatorname {Cat}_m
              +2(5H-1)\nu_H.                       \tag{2.2}
\]

At `H=o(sqrt m)` this yields a coefficient-one central band, but at the
critical physical depth `H=Theta(sqrt m)` the known estimate lacks the
required vanishing factor.  Pure Hamiltonization cannot manufacture it:
the short-run packing number is Lipschitz in the number of changed seams.

Spine B therefore asks for a residence-improving global PBBS braid, not a
new shadow theorem.

## 3. Singleton service is separately closed at incidence level

Minimal period-`2q+1` rails with three protected guard positions can cap
their remaining `2q-2` active source positions simultaneously to
singletons while preserving both the owner and immediate-lower rows.  A
family of

\[
                         O(k/q)                     \tag{3.1}
\]

far-core rails covers all `k` singleton targets, uses `k+O(k/q+q)` owners,
and is owner/q1-disjoint.  Its low exposure permits protected Ore--Ryser
completion to an exact spanning owner/q1 two-factor.

This eliminates singleton capacity and owner/q1 coinstantiation as an
independent obstruction.  The remaining task is to insert this linear-size
protected bank into a resident Spine-A or Spine-B chronology, rather than
accept an arbitrary nonresident Ore completion.

## 4. Global fusion cannot be treated marginally

For literal full-aperture source blocks, splicing `s` component seams
changes exactly `s(ell-1)` width-`ell` crossing cells.  Even correct rank at
the immediate-upper row imposes `q` intersection equations at each seam.
An addresswise zero-current splice between two distinct MSW components is
impossible for `q>=4`: its forced collar normal form makes the two orders
share a rank-`m+1` owner.

Hence a Latin successor rule or an uncoloured two-factor is insufficient.
A successful MSW fusion must be a cross-address tensor trade whose complete
occurrence current vanishes, or it must start from an already connected
double-turn chronology.  For PBBS, fusion is secondary to short-run repair.

## 5. Exact strict-lower compiler boundary

For the odd full-aperture source and a short cell `C=[i,i+ell-1]`,
`1<=ell<q`, one has

\[
 U_C=I_i^{m-q+ell+1},\qquad
 M_C=I_i^ell\mathbin{\dot\cup}I_{i+m-q+1}^ell.      \tag{5.1}
\]

A target `S` is individually realizable in `C` exactly when

\[
                         M_C\subseteq S\subseteq U_C.             \tag{5.2}
\]

The mandatory mask has size `2ell`, so the unchanged full-aperture
chronology cannot realize a singleton.  Section 3 supplies the necessary
minimal-run reserve.  What remains is the simultaneous CNF/common-cap
selection after that reserve and the chosen global chronology have been
coinstantiated.

## 6. Revised critical path

The proof now has two honest alternatives.

### Route A: chronological double turn

1. Construct a rank-middle chronology exact on owners and immediate lower
   turns, and surjective on immediate upper turns.
2. Strengthen or choose it so all coordinate positive runs are at least
   `q`, or plant the guarded singleton bank without destroying residence.
3. Prove all wider upper rows, ideally by a common all-width current
   theorem.
4. Solve the explicit short-cell CNF and typed common-cap linkage on that
   same chronology.

### Route B: PBBS residence braid

1. Starting from the exact PBBS all-depth factor, repair or cluster all
   positive runs below `q` with no loss of the all-depth occurrence tower.
2. Serialize to `O(1)` components (or retain `O(Cat_m)` components only if
   their collar cost is absorbed without changing length `B(k)+O(1)`).
3. Plant the guarded singleton bank and solve the literal lower/common-cap
   system.

Neither route has a remaining signed-lattice or scalar-capacity mystery.
Both are now occurrence-level correlation problems.

## 7. Proof-status table

| Row | Spine A (full aperture) | Spine B (PBBS) |
|---|---|---|
| exact middle owners | proved | proved |
| immediate lower exactness | proved odd; one even shore open | proved |
| all-depth target support | canonical upper fails linearly | proved |
| critical `q` residence | proved componentwise | open globally |
| singleton providers | guarded reserve proved, integration open | same |
| `O(1)` Euler components | global tensor/double-turn open | not the first gate |
| literal strict-lower CNF | exact local criterion; simultaneous open | compiler correlation open |
| common cap | conditional rank theorem only | conditional rank theorem only |
| `nu(k)<=B(k)+O(1)` | not yet proved | not yet proved |

The decisive conceptual gain is that the former monolithic “integral rail
rounding” gate has split into two concrete, opposing defects.  The next
theorem must transfer the best property of one spine to the other: PBBS-like
shadow completeness into a resident double-turn chronology, or MSW-like
long residence into the PBBS all-depth carrier.
