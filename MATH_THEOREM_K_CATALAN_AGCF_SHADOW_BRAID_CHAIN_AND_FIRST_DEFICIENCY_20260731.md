# The raw AGCF Shadow--Braid bridge, an exact `k=6` compiler, and the first recursive deficiency

Date: 2026-07-31  
Status: exact raw-even reduction; complete independently replayed `n=3,4,5`
gate audit; one new literal optimal `k=6` word; scoped intact-component
obstructions at `n=4,5`.  No interior-rethread theorem or all-parameter
`nu=B` theorem is claimed.

## 0. Result

An antipodal-geodesic Catalan forest is much closer to a compiler-ready
carrier than an arbitrary two-palette forest, but it is not itself the
downstream Shadow--Braid state.

For the raw even bridge `k=2n`, an AGCF supplies automatically:

1. every rank-`n` owner exactly once;
2. every immediate lower and upper turn exactly once; and
3. universal **internal** residence, because every coordinate flips once on
   every component.

It does not automatically supply:

1. a residence-compatible order and orientation of its components;
2. the all-width upper witness tower after the components are joined; or
3. one chain-aligned schedule and maximal common-cap lower compiler.

The exact small chain is:

| AGCF | even target | internal shadows | intact residence/compiler |
|---|---:|---|---|
| `n=3` | `k=6,d=1` | complete at every depth | **passes**; exactly 6 resident orders and 2 compiler orders |
| cyclic `n=4` | `k=8,d=2` | one lower/upper depth-3 hole | **fails**; at most 9 of 14 intact paths can be resident |
| nontransitive `n=5` | `k=10,d=2` | 8/15 depth-2 and 3/3 depth-3 lower/upper holes | **fails**; at most 4 of 42 intact paths can be resident |

Thus the first nonautomatic recursive row is already the global
residence/port relation at `n=4`.  All-width support also first fails at the
same parameter.  Common-cap feasibility is not a numerical failure there:
it is undefined until a physical chronology and schedule pass the earlier
rows.

At `n=3` the bridge closes completely.  It gives the new optimal word

```text
4 9 33 34 16 10 3 5 32 12 6 18 1 20 24 40 2 36 48 17 8
```

of length `21=B(6)`.  Literal replay covers all `63` nonempty masks.

At `n=5`, the complete internal-plus-one-seam provider atlas has one zero
row: the rank-eight target `0x27f`.  Hence no permutation or reversal of the
42 intact components can be upper-complete, even if arbitrary non-Johnson
seams are allowed.  This is the minimal static provider deficiency; an
interior rethread can change the atlas and is not ruled out.

The weakest recursive invariant is therefore occurrence-labelled.  It is
the joint relation of a collar-aware port path, protected upper witness
occurrences, the signed `q=1` cut/seam ledger, and one maximal common-cap
assignment.  Endpoint banks, turn palettes, rankwise hole counts, and scalar
residence margins are all proper projections of this state.

The same AGCF also has a pointed odd lift on `2n+1` coordinates.  That is a
different downstream interface.  This note audits the raw-even bridge used
for `k=6,8,10`; it does not silently identify the raw paths with their
pointed cycles.

## 1. Exact internal shadow identities

Let one AGCF component be

\[
 P=(X_0,X_1,\ldots,X_n),\qquad
 X_{i+1}=X_i-a_{i+1}+b_{i+1},                         \tag{1.1}
\]

where all `a_i` and all `b_i` are distinct and the two lists partition the
ground set.  For `i+q<=n`, define the literal upper and lower occurrences

\[
 U_q(P,i)=\bigcup_{t=0}^{q}X_{i+t},\qquad
 L_q(P,i)=\bigcap_{t=0}^{q}X_{i+t}.                    \tag{1.2}
\]

### Lemma 1.1 (geodesic window formula)

For every legal `(P,i,q)`,

\[
\begin{aligned}
 U_q(P,i)&=X_i\cup\{b_{i+1},\ldots,b_{i+q}\},\\
 L_q(P,i)&=X_i\setminus\{a_{i+1},\ldots,a_{i+q}\}.
\end{aligned}                                         \tag{1.3}
\]

In particular their ranks are exactly `n+q` and `n-q`.

#### Proof

Between `X_i` and `X_{i+q}`, each displayed `a` is deleted once and each
displayed `b` is added once.  No coordinate changes twice.  A deleted
coordinate is absent from at least one window member, while an added
coordinate is present in at least one; every unchanged coordinate has its
membership in all members.  This gives (1.3).  \(\square\)

For a target `S`, the correct protected state is not its multiplicity alone
but its occurrence set

\[
 \operatorname{Occ}^{+}_q(S)
   =\{(P,i):U_q(P,i)=S\},\qquad
 \operatorname{Occ}^{-}_q(S)
   =\{(P,i):L_q(P,i)=S\}.                              \tag{1.4}
\]

The AGCF axioms make `q=0` and both `q=1` palettes exact.  They say nothing
about (1.4) for `q>=2`.

There is one scope warning.  After a general braid, a rank-`n+q` target may
be witnessed by more than `q+1` owners because of stalls or non-Johnson
jumps.  Thus (1.4) is an exact minimal-width ledger on the sealed geodesic
face, not a universal normal form.  The unrestricted recursive state must
store an arbitrary-interval occurrence or one explicitly protected witness
span for every target.

## 2. Exact intact-block residence relation

On every AGCF component, each coordinate word is monotone with one change.
It therefore has no bounded internal positive or zero run.  Short runs can
appear only when oriented components are concatenated.

For an oriented component `P` and coordinate `x`, let

\[
 p_x(P)=\text{length of its initial 1-arm},\qquad
 s_x(P)=\text{length of its terminal 1-arm}.           \tag{2.1}
\]

Fix the required positive-run threshold `h=d+1`.  Put an arc from oriented
`P` to oriented `Q` exactly when, for every coordinate `x`, the run closed at
their seam has length at least `h`.  Explicitly, the tested length is

\[
 \begin{cases}
 s_x(P)+p_x(Q),&P_{\rm end}(x)=Q_{\rm start}(x)=1,\\
 s_x(P),&P_{\rm end}(x)=1, Q_{\rm start}(x)=0,\\
 p_x(Q),&P_{\rm end}(x)=0, Q_{\rm start}(x)=1,
 \end{cases}                                           \tag{2.2}
\]

and there is no positive seam run in the fourth case.  For the strict
Johnson-seam face, also require

\[
                    |P_{\rm end}\mathbin\triangle Q_{\rm start}|=2. \tag{2.3}
\]

### Theorem 2.1 (paired-orientation port criterion)

An intact-component chronology with minimum internal positive run at least
`h` exists if and only if the digraph (2.2) has a directed Hamilton path
using exactly one of the two orientations of every AGCF component.  On the
Johnson face add (2.3).

#### Proof

Every coordinate changes once inside each component, so it has both bit
values there.  Consequently a maximal positive run meeting a seam is
contained in the terminal arm of the left component and the initial arm of
the right component.  It cannot retain an unclosed all-one state through a
whole component.  Hence (2.2) tests every newly internal run and only such a
run.  Choosing all components once is precisely a paired-orientation
Hamilton path.  \(\square\)

For the flat depth-`d` schedule, the standard erosion theorem now gives the
maximal envelope exactly.  If `T` is the concatenated owner chronology and

\[
 E_p=\bigcap_{i:i\le p\le i+d}T_i,                    \tag{2.4}
\]

then (2.2) along the path is equivalent to nonempty envelopes and

\[
                       \bigcup_{p=i}^{i+d}E_p=T_i.     \tag{2.5}
\]

This closes physical inversion only.  It does not choose lower cells or a
common cap.

Arbitrary seams are load-bearing.  A central chronology need not be a
Johnson walk; the retained optimal `k=8` chronology itself has two
non-Johnson transitions.  The unrestricted counts below, not the stricter
Johnson counts, are therefore the architecture-independent no-gos.

## 3. Exact proper-upper provider atlas

For a sealed component `P`, store its complete internal upper deck together
with its prefix and suffix union chains.  If an interval in a concatenation
crosses two seams, it contains one entire intermediate antipodal path.  The
union of that path is the full `2n`-set.  Therefore:

### Lemma 3.1 (one-seam completeness for proper targets)

Every proper upper target in an intact-component concatenation is witnessed
either wholly inside one component or by a suffix of one component joined
to a prefix of the next.  The union of all such internal and ordered
one-seam occurrences is the complete provider atlas for proper upper
targets over every component order and orientation.

This lemma makes a zero row in that atlas a solver-free obstruction to every
intact-component braid.  It is stronger than a fixed-width hole count.

If paths are cut internally, the exact replacement is the signed
occurrence ledger

\[
                  m(S)-D(S)+A(S)\ge1,                 \tag{3.1}
\]

where `D` and `A` count deleted and added **literal witness spans**.  A
rankwise count without occurrence identities cannot decide (3.1).

## 4. The full `n=3` bridge is positive

Number the five stored AGCF paths in their theorem order.  Take order

\[
                         (0,4,1,2,3)                   \tag{4.1}
\]

and reverse stored paths `1` and `3` (the third and fifth entries of
(4.1)), equivalently use stored-index reversal vector

\[
                         (0,0,1,0,1).                  \tag{4.2}
\]

The resulting chronology is

\[
\begin{split}
T={}&(13,41,35,50,26,11,7,37,44,14,22,19,\\
    &21,28,56,42,38,52,49,25).
\end{split}                                             \tag{4.3}
\]

All four seams happen to be Johnson edges, although that is not required by
the general compiler theorem.  Exhausting all `5! 2^5` intact orders gives
exactly six depth-one-resident orders.

For `d=1`, every lower cell is a singleton position: every interval of two
or more positions contains a complete middle interval `[i,i+1]`.  There are
exactly 21 lower targets, namely the six singletons and fifteen pairs.  An
exact dynamic program over these 21 targets leaves two feasible resident
orders.  For (4.3) it returns

\[
\begin{split}
Q={}&(4,9,33,34,16,10,3,5,32,12,6,18,\\
    &1,20,24,40,2,36,48,17,8).
\end{split}                                             \tag{4.4}
\]

### Theorem 4.1 (literal optimal `k=6` compilation)

The word (4.4) has length `21=B(6)`, satisfies `DQ=T`, and its interval ORs
are exactly all 63 nonempty six-bit masks.

Moreover, assign every lower target `S` to the unique singleton position
whose letter is `S`.  Then \(Q_p\subseteq E_p\), and the maximal common cap is

\[
 A_p=E_p\cap\bigcap_{S:p\in M(S)}S=E_p\cap Q_p=Q_p.    \tag{4.5}
\]

Equations (2.5) and (4.4) make every middle and assigned-lower OR exact.
Thus this is a literal maximal-common-cap certificate, not merely an
uncapped Hall matching.

The frozen word has SHA-256

```text
05114959e6761b19c0377f9a90531be70c1304393255f867cf757f78dd5f839b
```

including its terminal newline.

## 5. The first failure is `n=4`

For the cyclic `n=4` parent used by the explicit `n=5` construction, the
exact reachable residence-state counts by number of distinct intact blocks
are

\[
 28,42,56,70,84,91,84,56,28,0                         \tag{5.1}
\]

for lengths `1,...,10`; hence no resident prefix has ten blocks, while the
forest has fourteen.  With Johnson seams the counts are

\[
                         28,28,14,14,14,14,14,0.       \tag{5.2}
\]

The independent exact-cover `n=4` AGCF and the separate direct-recursive
fixture fail even earlier.  Thus (5.1), rather than a special symmetry, is
the relevant obstruction for the parent actually used at `n=5`.

Its sealed internal minimal-width tower is complete except at depth three:

\[
        L_3\text{ misses }0x80,\qquad
        U_3\text{ misses }0x7f.                        \tag{5.3}
\]

The target `0x7f` does have possible one-seam providers, so (5.3) is not an
all-order no-go.  It does prove that all-width service is a new recursive
row, independent of the exact `q=1` palettes.

Since no intact resident chronology exists, its flat envelopes and exact
common-cap instance are not terminal objects.  Reporting a Hall number at
this point would conflate a projected lower atlas with a physical compiler.

## 6. The explicit `n=5` deficiency

For the nontransitive `C7`-equivariant AGCF, the exact unrestricted
residence-state counts are

\[
                         84,154,70,14,0                \tag{6.1}
\]

for prefix lengths one through five.  No five intact components can occur
in a depth-two-resident chronology, while the factor has 42 components.
On the Johnson face the counts are

\[
                         84,98,42,0.                   \tag{6.2}
\]

The internal minimal-width defects are

\[
\begin{array}{c|c|l}
\text{depth}&\text{shore}&\text{holes}\\ \hline
2&\text{lower}&0x00d,0x01a,0x023,0x034,0x046,0x051,0x068,0x380,\\
2&\text{upper}&0x07f,0x39d,0x3a7,0x3ab,0x3ad,0x3b5,0x3ba,
 0x3ce,0x3d3,0x3d5,0x3d6,0x3da,0x3e9,0x3ea,0x3f4,\\
3&\text{lower}&0x180,0x280,0x300,\\
3&\text{upper}&0x0ff,0x17f,0x27f.
\end{array}                                             \tag{6.3}
\]

The lower depth-two holes are one free `C7` orbit plus one fixed mask; the
upper depth-two holes are two free orbits plus one fixed mask.  The depth-
three holes are fixed under the residual rotation.

More decisively, exhaustive construction of the complete atlas in Lemma
3.1 leaves exactly one zero-provider proper upper target:

\[
                              \boxed{0x27f}.            \tag{6.4}
\]

All other 17 internally missing proper upper targets have at least one
oriented one-seam provider.  Thus (6.4) is the exact static deficiency-one
certificate.  It does not assert that the other 17 can be served
simultaneously by one component order.

There is also a quantitative surgery consequence.  Suppose `c` internal
cuts hit `s<=c` of the 42 paths.  There remain `42-s` whole blocks and at
most `s+c+1` runs of whole blocks separated by split fragments.  Equation
(6.1) allows at most four whole blocks per run, so

\[
                         42-s\le4(s+c+1).              \tag{6.5}
\]

For `c<=4` this is impossible; hence at least five internal cuts are needed.
On the Johnson face (6.2) replaces four by three and forces at least six.
This lower bound concerns descendants obtained by cutting and reordering
the fixed paths.  General alternating edge exchanges can evade it.

The retained optimal `answers/k10.word` is not a hidden intact ordering:
its depth-two chronology shares only 24 of the AGCF's 210 internal edges.
An intact ordering would retain all 210.  No `n=5`-derived word is therefore
emitted.  An extensive interior rethread remains a live route.

## 7. What the authenticated direct chain does and does not add

The strict direct-edgewise chain supplies exact immediate palettes and
physical path forests, not AGCFs.  Its raw internal audit is:

\[
\begin{array}{c|c|c|c}
n&\text{forbidden positive runs at the even deadline}
 &\text{lower holes at depths }2,3&\text{upper holes at depths }2,3\\ \hline
3&0&(0,0)&(0,0)\\
4&17&(1,1)&(1,1)\\
5&44&(4,3)&(3,4).
\end{array}                                             \tag{7.1}
\]

Thus the direct chain independently confirms the same boundary: immediate
turn exactness and graphic topology do not preserve residence or the deep
window tower at `n=4`.  Its facet margins and common-basis rows are useful
upstream selection data, but they are not downstream Shadow--Braid
acceptance.

The known optimal `k=6,8,10` chronologies share respectively only

\[
                         3/15,\quad6/56,\quad24/210     \tag{7.2}
\]

internal factor edges with the displayed AGCFs.  The new word (4.4), rather
than the retained `answers/k06.word`, is the positive intact `n=3`
calibration.

## 8. Weakest recursive invariant

For a family of occurrence-labelled fragments at deadline `d`, define the
raw Shadow--Braid relation

\[
             \mathsf{RSB}_d=
             (\mathsf{Port}_d,\mathsf{Upper},
              \mathsf{Q1},\mathsf{Comp}).              \tag{8.1}
\]

Its four coordinates are as follows.

1. **Port and residence.**  Store both orientations of every fragment, its
   endpoint masks, the first and last `d+1` coordinate bits, and the exact
   truncated run automaton.  Store the permitted connector relation and a
   selected component path/topology.  For intact AGCF components this
   reduces to Theorem 2.1; after interior cuts the full automaton is needed.
2. **All-width upper service.**  Store a protected occurrence span for every
   required upper target, or equivalently the internal/prefix/suffix decks
   and the exact cut/connector replacement relation.  A transition must
   preserve one literal occurrence, not merely positive multiplicity before
   and after projection.
3. **Immediate palette and topology.**  Store the lower and upper labels of
   every deleted or added seam, the endpoints they connect, and the boundary
   cells reserved to replace lost `q=1` colours.  Exact internal palettes do
   not make an arbitrary opening neutral.
4. **Compiler relation.**  Store the chain-aligned schedule, maximal
   envelopes, positional pins, the injective lower-target/cell assignment,
   and

   \[
       A_p=E_p\cap\bigcap_{S:p\in M(S)}S,              \tag{8.2}
   \]

   with nonemptiness and exact middle/lower replay.  For cells meeting a
   future exchange halo, also store a guarded alternating linkage to a
   private replacement bank.

### Theorem 8.1 (exact recursive acceptance)

A raw-even fragment braid yields a length-`B(2n)` universal word exactly
when one tuple of (8.1) simultaneously supplies a legal chronology,
residence/envelope replay, all proper upper targets, all lost immediate
palette obligations, and the maximal common-cap equations.

#### Proof

The port coordinate materializes the owner chronology and the residence
automaton.  The upper coordinate gives the arbitrary-width clause of the
master carrier theorem.  The `q=1` coordinate records the exact physical
cut and join changes.  Finally (8.2) is the maximal-common-cap equivalence
for all lower targets.  These four clauses are precisely the hypotheses of
the master staircase--pin--common-cap theorem.  Conversely, restricting any
literal word certificate to its fragments, witness spans, seams, schedule
and target-cell assignment gives one tuple of (8.1).  \(\square\)

The relation (8.1), or its exact boundary projection, is the weakest safe
recursive invariant against arbitrary future braids.  A bounded-size
version requires an additional privacy hypothesis: all but boundedly many
shadow and compiler obligations must have protected witnesses wholly inside
sealed fragments.  AGCF alone does not imply that privacy.

## 9. Reproducibility and scope

The exact audit and its new `k=6` word are

```text
scratch/audit_k_catalan_agcf_shadow_braid_chain_20260731.py
scratch/k_catalan_agcf_shadow_braid_chain_20260731.audit.json
scratch/k_catalan_agcf_n3_compiled_optimal_k6_20260731.word
```

The audit reconstructs the three AGCFs from their frozen sources, verifies
owners/turns/geodesics, computes every internal fixed-width shadow,
enumerates the exact residence port states, exhausts the `n=3` compiler,
builds the complete `n=5` proper-upper one-seam atlas, replays the direct
chain, and verifies the retained optimal words before comparing edge sets.

The `n=4,5` conclusions are no-gos only for intact components, with the
explicit cut lower bound (6.5).  They do not rule out interior rethreading,
nonflat schedules, or a different AGCF.  Common-cap is marked undefined
upstream rather than falsely declared `UNSAT`.

Frozen artifact hashes are

```text
audit script  ca928174ecb74f2fedb82c128f60c021a16566041db12ad69a9eb99a02ee12af
audit JSON    881e502c40ab82e2442a63761a184825992ded37d6c7290fffb3faa153491df4
k=6 word      05114959e6761b19c0377f9a90531be70c1304393255f867cf757f78dd5f839b
```

The script regenerates the JSON byte-for-byte.  Its canonical payload hash
is `d6bea5f4aa3097b06291a4f73cd7b02fe2e9c19c6d102ab47ec84abc6e63402f`.
