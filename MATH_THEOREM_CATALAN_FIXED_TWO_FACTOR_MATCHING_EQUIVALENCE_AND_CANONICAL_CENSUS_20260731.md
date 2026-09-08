# Fixed Middle-Levels two-factors: one matching theorem and the sharp raw-MMM boundary

Date: 2026-07-31  
Status: exact fixed-factor characterization; exact finite raw-MMM census;
no all-dimension decorated-factor, residence, deep-shadow, or contiguous-OR theorem

## 0. Verdict

Fixing a spanning two-factor does not leave a vague ``decoration'' problem.
It leaves exactly one bipartite perfect-matching problem.

Equivalently, after choosing the upper-turn representatives, it leaves one
global gap-versus-lower-colour Hall matching.  The only additional condition
needed for a Catalan **linear** matching is the componentwise trace test.  A
particularly useful automatic slice is

\[
       q_C-r_C>0\quad\hbox{and}\quad q_C-r_C\equiv1\pmod2
       \tag{0.1}
\]

on every hit factor component, where `q_C` is its number of vertices on one
shore and `r_C` is its number of selected upper turns.

The raw MMM factor passes this exact gate maximally through project `m=4`:
at `m=4` all `16,384` upper SDRs pass gap Hall and all have residual quotas
`(7,7)`.  It fails first at project `m=5`, before Hall, because three turn
colours on each shore are absent.  Thus the fixed-factor reduction gives a
sharp finite obstruction to using the unrepaired canonical factor as an
all-`m` theorem; it simultaneously shows that the obstruction is not
topology or trace parity.

This note consolidates the corrected factor-level reduction and adds the
exhaustive canonical-factor census.  It does not claim that the accepting
factor exists in every dimension.

## 1. The factor-supported diamond graph

Fix `m>=2`, put

\[
 \Omega=[2m-1],\qquad
 Q={2m-1\choose m-1}={2m-1\choose m},\qquad
 P={2m-1\choose m-2}={2m-1\choose m+1},
 \tag{1.1}
\]

and `K=Q-P=Cat_m`.  Let `F` be a spanning two-factor of
`ML(2m-1)`.  Write one component in alternating order as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.             \tag{1.2}
\]

Its turns are

\[
             u_i=B_{i-1}\cup B_i,
 \qquad      \ell_i=A_i\cap A_{i+1}.              \tag{1.3}
\]

Adjoin a new point `infinity`.  Define the factor-supported diamond graph
`G_F` with shores

\[
 \mathcal L={\Omega\choose m-1}
       \sqcup\bigl(\infty+{\Omega\choose m-2}\bigr),
 \qquad
 \mathcal U=\bigl(\infty+{\Omega\choose m}\bigr)
       \sqcup{\Omega\choose m+1}.                 \tag{1.4}
\]

It has exactly the following inclusion edges.

1. Every factor incidence `A--B` gives `A -- (infinity+B)`.
2. Every `A_i` gives its upper-turn edge `A_i -- u_i`.
3. Every `B_i` gives its lower-turn edge
   `(infinity+ell_i) -- (infinity+B_i)`.

Each edge is a Boolean diamond: its endpoints differ by two elements.  Its
physical lift is the Johnson edge between the two intermediate rank-`m`
sets.

## 2. Perfect matchings are exactly alternating decorations

### Theorem 2.1 (fixed-factor matching equivalence)

Perfect matchings of `G_F` are in bijection with the following data.

* Selected `A` occurrences whose upper turns enumerate
  `binom(Omega,m+1)` exactly once.
* Selected `B` occurrences whose lower turns enumerate
  `binom(Omega,m-2)` exactly once.
* On each marked factor component, cyclic alternation of selected shore
  types and the forced residual matching between consecutive marks.
* On each unmarked component, either of the two alternating residual phases.

In particular, a factor-supported componentwise alternating decoration is
not a second object: it is precisely a perfect matching of `G_F`.

#### Proof

Every outer upper vertex `u in binom(Omega,m+1)` has neighbours only among
the `A` occurrences whose turn is `u`.  A perfect matching therefore chooses
one such occurrence for every upper colour.  Dually it chooses one `B`
occurrence for every lower colour.

After deleting those turn-matched occurrences, the only available edges are
factor incidences.  On one factor cycle, the remaining vertices admit a
perfect matching exactly when every residual arc between consecutive marks
has even order.  This is equivalent to consecutive marked occurrences
having opposite shores, including the cyclic last-to-first pair.  A marked
component then has a unique residual matching.  If no occurrence is marked,
the even factor cycle has its two alternating matching phases.

Conversely these data cover every outer colour vertex, every selected
occurrence, and every residual occurrence exactly once, hence form a perfect
matching of `G_F`.  The constructions are inverse. \(\square\)

## 3. The exact upper-SDR/gap-Hall form

Fix an upper-turn SDR `I`, and let `I_C` be its occurrences on component
`C`.  Put

\[
                         r_C=|I_C|.                 \tag{3.1}
\]

If `r_C>0`, orient the component and make one occurrence-labelled cyclic
gap from every selected `A` occurrence to the next one.  The gap contains
the `B` occurrences strictly after the first selected `A` and strictly
before the next.  These gaps partition all `B` occurrences of every hit
component, and their total number is

\[
                         \sum_C r_C=P.              \tag{3.2}
\]

Let `Gamma_F(I)` be the bipartite multigraph whose left shore is the set of
oriented gap occurrences and whose right shore is
`binom(Omega,m-2)`.  A gap is joined to colour `ell` once for every
occurrence `B_j` in that gap with `ell_j=ell`.  The parallel-edge label
remembers the selected `B_j` and hence the trace.

### Theorem 3.1 (global component-gap Hall)

The upper SDR `I` extends to a perfect matching of `G_F` if and only if
`Gamma_F(I)` has a perfect matching.  Equivalently,

\[
                         |N(S)|\ge |S|               \tag{3.3}
\]

for every set of oriented gaps `S`.

#### Proof

Between consecutive selected `A` occurrences, shore alternation requires
exactly one selected `B` occurrence.  Hence an extension chooses one lower
colour from each gap, with every lower colour used once.  This is a perfect
matching of `Gamma_F(I)`.  Conversely, choose the occurrence labelling each
matched gap-colour edge.  The gaps are disjoint, the lower colours are
bijective, and the marked order on every hit component is
`A,B,A,B,...`.  Components missed by `I` stay wholly unmarked and take an
arbitrary residual phase.  Theorem 2.1 applies.  Hall's theorem gives
(3.3). \(\square\)

Thus the exact fixed-factor existence statement is simply

\[
 \boxed{\exists\text{ upper SDR }I:
              \Gamma_F(I)\text{ has a perfect matching}.}       \tag{3.4}
\]

For a **linear** diamond matching the matched occurrence labels must also
pass the trace test below.

## 4. Exact trace test and automatic parity slices

Encode selected and residual occurrences around a component by a cyclic
binary word of length `2q_C`, with `1` for a selected turn.  Its physical
lift has the following exact topology.

* The all-zero trace gives `q_C` disjoint cross edges.
* The all-one trace gives two disjoint same-rail cycles.
* A mixed trace gives one cycle exactly when every positive zero-run has
  length two and every one-run has odd length; otherwise it is a forest.

The first line follows from either residual phase.  The second follows
because all `A` turns form one rail cycle and all `B` turns the other.  In
the mixed case, a one-run transmits the physical route exactly when it is
odd, while a residual zero-run transmits exactly when it has length two.
The route closes precisely when every block transmits.

Put

\[
                         z_C=q_C-r_C.                \tag{4.1}
\]

### Corollary 4.1 (positive odd residual)

If `C` is hit and `z_C` is positive and odd, then **every** gap-matching
extension on `C` is trace-safe.

#### Proof

There are `2z_C` zeroes and `2r_C` ones.  On the exceptional mixed face,
the zeroes form exactly `z_C` runs of length two, so there are also `z_C`
one-runs.  If all one-runs were odd, their total parity would be the parity
of `z_C`, but their total length is `2r_C`, which is even.  Odd `z_C` is a
contradiction.  Positivity excludes the all-one trace. \(\square\)

The same count gives the complete **numerical danger window**.  On the
exceptional mixed face the `z_C` one-runs are positive and odd and have
total length `2r_C`.  Therefore exceptionality requires

\[
                    z_C\equiv0\pmod2,
       \qquad       2\le z_C\le2r_C.                \tag{4.2}
\]

Consequently a hit component is automatically safe whenever

\[
 z_C>0\quad\hbox{and}\quad
 \bigl(z_C\text{ is odd}\ \text{or}\ z_C>2r_C\bigr).             \tag{4.3}
\]

The second clause is the sparse-mark slice `q_C>3r_C`; for example one
selected turn on each shore is automatically safe on every component with
`q_C>=4`, even when its residual is even.  Conditions (4.2) are only the
numerical window in which the cyclic trace can be exceptional, not a claim
that every quota in that window is bad.

This yields two useful automatic slices.

1. **Hamilton slice.**  If `F` is Hamilton then
   `z=Q-P=Cat_m`.  Therefore whenever `Cat_m` is odd, every alternating
   decoration is automatically linear.  By the standard Catalan parity
   criterion, this holds exactly when

   \[
                            m=2^a-1.                 \tag{4.4}
   \]

2. **Component-private quota slice.**  If every upper turn colour occurs
   on only one factor component, then every upper SDR has the forced quota

   \[
       r_C=|\{u:\ u\text{ occurs on }C\}|.           \tag{4.5}
   \]

   If all positive forced residuals `q_C-r_C` are odd, trace linearity is
   automatic before Hall is tested.

There is also a free global parity check on this sufficient slice.  If `H`
is the set of hit components and every `z_C` for `C in H` is odd, then

\[
 |H|\equiv \operatorname {Cat}_m-
              \sum_{C\notin H}q_C\pmod2.             \tag{4.6}
\]

In particular, if every component is hit, the component count must have the
same parity as `Cat_m`.  Failure of this congruence excludes only the
all-odd sufficient slice; it does not exclude a trace-safe decoration using
an even residual outside the danger face.

When the lift is trace-safe, component `C` contributes exactly `z_C`
physical paths.  Summing gives

\[
                  \sum_Cz_C=Q-P=\operatorname {Cat}_m.           \tag{4.7}
\]

## 5. Exact raw-MMM census

The independent audit reconstructs the raw canonical MMM factor from the
Dyck rotation map, extracts its ordered components, enumerates every upper
SDR through project `m=4`, and runs the exact gap-Hall matching test.  The
result is:

\[
\begin{array}{c|c|r|r|r|c}
m&q_C\text{ values}&\#\text{ upper SDRs}&\#\text{ gap Hall}
 &\#\text{ odd-residual Hall}&\text{verdict}\\ \hline
2&(3)&3&3&0&\text{safe direct trace}\\
3&(10)&32&32&32&\text{all pass}\\
4&(21,14)&16384&16384&16384&\text{all pass}\\
5&(36,72,18)&0&0&0&\text{absent colours}.
\end{array}                                                     \tag{5.1}
\]

At `m=4` the turn colours are component-private.  Every upper SDR has

\[
                  (r_C)=(14,7),\qquad (z_C)=(7,7),               \tag{5.2}
\]

and every one of the `2^14=16,384` choices passes gap Hall.  Thus all
fixed-factor global coupling and all trace parity are benign at this last
positive raw dimension.

At `m=5`, each shore realizes only `81` of its required `84` colours.  In
the audit's zero-based bit convention the missing lower colours are

\[
       73,146,292
       =\{\{0,3,6\},\{1,4,7\},\{2,5,8\}\},          \tag{5.3}
\]

and the missing upper colours are their complements

\[
                         438,365,219.                \tag{5.4}
\]

They are the period-three rotation orbit.  The corresponding outer
vertices of `G_F` have degree zero, so no perfect matching exists.  This is
a sharper failure than gap Hall or trace parity and proves:

> The unrepaired canonical MMM factor cannot itself furnish an all-`m`
> decorated-factor theorem; project `m=5` is the first obstruction.

It does not obstruct preliminary rethreading, a repaired factor, or another
two-factor.  Indeed the known `m=5` incidence-hex repair supplies a positive
decorable factor.

## 6. What remains

For a fixed factor the central problem is now completely discrete:

\[
 \boxed{
  \text{upper-turn SDR}
  +\text{ one global component-gap Hall matching}
  +\text{ local trace safety}.}
 \tag{6.1}
\]

The positive-odd row can remove the last condition before any matching is
solved.  It does not remove the correlated upper-SDR/gap-Hall choice, and
the raw-MMM census proves that factor repair is unavoidable from `m=5`
onward.

Even an all-`m` decorated-factor theorem would settle only the central
Catalan Linear Matching gate.  It would not by itself supply coordinate
residence, deeper shadows, seam chronology/voltage, or the common integral
compiler required for the full identity `nu(k)=B(k)`.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_fixed_two_factor_canonical_census_20260731.py
```

The audit:

* reconstructs the canonical factors at project `m=2,3,4,5`;
* checks the literal degree-two component decomposition;
* enumerates every upper SDR for `m<=4`;
* builds every occurrence-labelled gap graph and runs exact bipartite
  matching;
* reconstructs a lower occurrence witness and checks the cyclic trace; and
* verifies the three absent lower colours and complementary upper colours
  at `m=5`.

Frozen artifacts:

* `scratch/audit_catalan_fixed_two_factor_canonical_census_20260731.py`,
  SHA-256
  `8c91b1d552f302fcd934ec396c4f77d43ccb15297e40f4fd0a13f1eaf1ca5957`;
* `scratch/catalan_fixed_two_factor_canonical_census_20260731.audit.json`,
  SHA-256
  `a14206fafd6242417fff423f4b4b2443619c73954a76338012818d27be15471d`,
  payload SHA-256
  `4cc6e94fbd00c69e2dbdc6086bffa42f0206323a37e4ab3a7f249849c6775f4c`.

The audit is finite evidence for (5.1), not an all-dimension proof.
