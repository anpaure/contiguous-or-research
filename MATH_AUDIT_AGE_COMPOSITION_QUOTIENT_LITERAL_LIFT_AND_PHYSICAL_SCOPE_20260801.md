# Audit of the age-composition quotient: exact fractional lift, nonfaithful physical projection

Date: 2026-08-01

Status: Theorem 2 of the supplied age-composition proposal is correct after
making its marking variables and partition-level lift explicit.  It is an
exact quotient of the fully symmetric **rank-only fractional** marked-trace
polytope.  It is not an exact quotient after one-copy owner identities,
literal root/pin imbalance, structural compiler incidences, or physical
Catalan topology are imposed.

No all-`k` existence or additive upper bound follows from this audit.

## 1. Corrected exact quotient

Let

\[
 \mathcal C_{r,d}=\{c=(c_0,\ldots,c_d):c_0>0,
                    c_i\ge0,\ \sum_i c_i=r\},
\]

and put `c->c'` when

\[
                         c'_{i+1}\le c_i
                         \quad(0\le i<d).              \tag{1.1}
\]

For a type `c`, define

\[
 s_j(c)=c_0+\cdots+c_{j-1},\qquad
 R(c)=\{s_j(c):1\le j\le d,\ s_j(c)<r\}.              \tag{1.2}
\]

`R(c)` is a set, not a multiset.

### Theorem 1.1 (marked age quotient)

For the invariant marked-trace polytope `ST_(k,r,d)` as defined in
`MATH_THEOREM_TRIANGULAR_MARKED_TRACE_CIRCULATION_AND_K6_BALANCED_CLOCK_20260801.md`,
a rank vector `q=(q_s)` lies in `ST_(k,r,d)` if and only if there are
nonnegative variables

\[
 f(c,c')\quad(c\to c'),\qquad m_s(c)\quad(1\le s<r),
\]

such that

\[
 \sum_{c'}f(c,c')=\sum_{c'}f(c',c)=:\pi(c),qquad
 \sum_c\pi(c)=1,                                      \tag{1.3}
\]

\[
 0\le m_s(c)\le \pi(c)\,\mathbf1_{\{s\in R(c)\}},
 \qquad \sum_c m_s(c)=q_s.                            \tag{1.4}
\]

Eliminating the independent variables `m_s(c)` gives exactly

\[
 q_s\le\sum_{c:s\in R(c)}\pi(c)\qquad(1\le s<r).      \tag{1.5}
\]

Thus the proposed inequalities are the correct mark-capacity inequalities
for the rank-only fractional model.

### Proof

Projection from a literal stationary trace sends every edge to the age type
of its `(d+1)`-letter window.  An element of new age `i+1` must have had old
age `i`, proving (1.1).  Flow conservation projects to (1.3).  Nested suffix
sets of equal rank are equal, so the number of distinct rank-`s` values
available on a type-`c` trace is one exactly when `s in R(c)`.  This proves
(1.4) and necessity.

For sufficiency, fix one literal rank-`r` owner `T`.  Let
`P_c(T)` be the set of ordered partitions

\[
                         T=C_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d,
                         \qquad |C_i|=c_i.             \tag{1.6}
\]

Join `P=(C_i)` to `P'=(C'_i)` exactly when

\[
                         C'_{i+1}\subseteq C_i
                         \quad(0\le i<d).              \tag{1.7}
\]

The relation between any two adjacent types is nonempty by (1.1) and is
invariant under `Sym(T)`.  Since `Sym(T)` is transitive on each `P_c(T)`, the
relation is biregular.  Give every arc in the `(c,c')` relation equal total
mass `f(c,c')`.  The mass entering and leaving each literal partition of
type `c` is then `pi(c)/|P_c(T)|`.

For an arc `P->P'`, append the nonempty letter `C'_0`.  Equation (1.7) and
the fact that both sides partition `T` imply

\[
 C'_0=C_d\cup\bigcup_{i<d}(C_i-C'_{i+1}).              \tag{1.8}
\]

Hence the last-occurrence ages update literally.  A directed partition
cycle therefore gives a periodic sequence of nonempty source letters whose
every `(d+1)`-window has owner `T`; this is a genuine de Bruijn circulation,
not only a formal type flow.  Decomposing the finite conserved flow into
cycles handles arbitrary real masses.

For `s in R(c)`, a uniformly distributed partition in `P_c(T)` makes its
rank-`s` suffix value uniform over the `binom(r,s)` subsets of `T`.  Split
the mass of type `c` into marked variants according to (1.4).  Marks at
different available ranks may coexist on the same atom, so there is no
cross-rank capacity inequality beyond (1.4).

Repeat the construction with mass one for every owner `T` and average under
`Sym(k)`.  A fixed rank-`s` target `S` is contained in
`binom(k-s,r-s)` owners and receives

\[
 {\binom{k-s}{r-s}\over\binom rs}\,q_s
     ={\binom kr\over\binom ks}\,q_s.                 \tag{1.9}
\]

At the triangular value
`q_s=(binom(k,s)-b_s)/binom(k,r)`, this is exactly
`1-b_s/binom(k,s)`.  This proves the literal fractional lift and the
targetwise marked loads. `square`

The age graph has

\[
                         |\mathcal C_{r,d}|
                             ={r+d-1\choose d},         \tag{1.10}
\]

so the exponential literal state space is genuinely removed from this one
fractional rank projection.

## 2. What literal information the quotient does preserve

### 2.1 Owner identities, fractionally

The lift above restores every literal owner identity: it constructs a
separate conserved flow of total mass one inside each named owner `T`.
Flows from different owners may meet at the same de Bruijn vertex, but each
owner flow is already balanced before they are summed.

This is exactly what equations (1.4) and (1.6) of the marked-trace LP ask
fractionally.  It is not an ordering of the owners.

### 2.2 Suffix-value distinctness

Suffix unions are nested.  Two of them have the same rank if and only if
they are the same set.  Therefore replacing the partial-sum list by the set
`R(c)` loses no distinct suffix occurrence capacity.  A zero age class
creates a repeated value and correctly contributes only one markable value.

### 2.3 Rank-only mark capacity

For one type occurrence, every different rank in `R(c)` corresponds to a
different physical suffix address and value.  All such ranks may be marked
simultaneously.  Hence the local rank-capacity region is the box in (1.4),
and the coordinatewise inequalities (1.5) are sufficient.

These three conclusions remain valid only before structural guards or a
one-copy requirement are added.

## 3. Where the quotient ceases to be faithful

### 3.1 One-copy owners and physical owner transitions

The sufficiency proof deliberately realizes every transition inside one
fixed owner.  A one-vertex type self-loop can therefore lift to one private
cycle in every owner.  The type support is connected, while the literal
owner support may have `W=binom(k,r)` components and no edge changing the
owner.

Consequently the quotient does not encode:

* exactly one selected trace edge per owner;
* a simple ordering of all owner identities;
* Johnson adjacency of consecutive owners;
* lower- or upper-q1 rainbowness; or
* a Hamilton path/cycle or rooted Catalan connector.

Adding any of these requirements invalidates the `if and only if` unless
the quotient is enlarged by the corresponding owner-transition data.

### 3.2 Literal connectedness, roots and fixed pins

Flow balance survives projection, but connected support does not.  A type
cycle may lift to many disjoint literal cycles.  Likewise, a prescribed
boundary comparator or singleton root contributes imbalance at specific
order-`d` literal states.  Age type records neither the ordered state nor
the location of that imbalance.

Thus a zero type circulation does not solve the coloured Euler/root problem
and cannot absorb fixed comparator arcs without an additional literal
boundary equation.

### 3.3 Compiler occurrence labels and common-cap legality

Equation (1.9) is a fractional average over every owner containing `S` and
over every age partition of that owner.  After denominator clearing it uses
many copies of the same owner and many candidate suffix addresses.

The physical compiler instead needs one injective occurrence assignment:
one legal cell for every target, no cell used twice, under the same envelope,
guard and positional cap as the owner chronology.  Those structural zeros
break the stabilizer transitivity used in the lift.  An arbitrary guarded
subrelation of (1.7) need not be biregular, and rank-uniform marking need not
respect its Hall cuts.

Therefore Theorem 1.1 does not prove an occurrence-labelled compiler SDR or
even fractional feasibility after the actual common-cap structural zeros
are imposed.

### 3.4 Integral mark capacities

The box (1.4) is exact for splittable mass.  It does not say that, after one
trace is selected per owner, the available physical suffix cells can be
matched integrally to all targets.  The missing statement is the same
coloured one-copy/common-cap correlation already isolated in the handoff.

## 4. Exact status of the proposal's later steps

Theorem 2 is a valid reduction, not a nonemptiness theorem.  The proposed
unit-descent circulation lemma is still needed to show that the actual
triangular vector `q` satisfies (1.3)--(1.5) for general `d`.

Even if that lemma is proved, the following gates remain independent:

1. **One-copy coloured Euler rounding.**  Select exactly one trace per
   owner while preserving literal state balance and all target payloads.
   Existing parity/lattice examples show that a rational stationary
   circulation does not imply this.
2. **Connected rooted literal support.**  Join the selected traces with
   `O(1)` route-inspection cost and retain the boundary/comparator pins.
3. **Owner/Catalan topology.**  Obtain a simple Johnson chronology, both q1
   palettes, the rooted Catalan connector and the prescribed packet paths.
4. **Residence across joins.**  A closed literal trace cycle is resident,
   but opening or joining its components exports the exact capped age/run
   state; type balance alone does not heal it.
5. **Arbitrary-width upper witnesses.**  The quotient records only proper
   suffix ranks below `r`; it contains no provider data for higher interval
   unions.
6. **Occurrence-level lower compilation.**  Solve one guarded common-cap
   SDR on the same physical chronology, including the boundary board and
   every fixed macro.
7. **Regeneration.**  Carry the connected/rooted/guarded state through the
   same-parity recursion without accumulating components or sidecars.

Accordingly, the quotient removes a real exponential nuisance from the
fractional clock gate.  It does not remove the physical Catalan connector or
common-cap theorem, and it does not improve the certified numerical bounds
by itself.

## 5. Recommended corrected statement

The proposal's headline should be read as:

> The `Sym(k)`-invariant, rank-only fractional marked-trace projection has
> an exact age-composition quotient.  The remaining fractional question is
> a circulation coupling of the required age profiles.

It should not be read as:

> Literal traces with named owners and compiler occurrences have an exact
> age-only quotient.

The latter is false once one-copy selection, literal pins, structural
compiler zeros, or Catalan topology are restored.

