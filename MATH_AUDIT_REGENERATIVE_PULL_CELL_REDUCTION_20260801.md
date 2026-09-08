# Audit of the regenerative pull--cell reduction

Date: 2026-08-01  
Status: implication validated after corrections; the required transition is
not yet constructed.  This note separates the new unconditional rows from
the clauses still hidden inside the proposed lemma.

## 1. Verdict

The following conditional statement is correct.

> If one fixed constant `c` and one same-parity transition work in every
> sufficiently large dimension, carrying every admissible sidecar of size at
> most `c` to another sidecar of size at most `c`, while preserving the full
> terminal OR word except for those carried targets, then
> `nu(k)<=B(k)+c` on both parities.

At the terminal dimension append the at most `c` carried masks as literal
letters.  They are paid once, not once per induction step.

The proposed regenerative pull--cell lemma is one sufficient realization of
this statement.  It is not a proved theorem: its clauses currently contain
four independent open bridges.

## 2. Rows which are proved

### 2.1 Endpoint chains

If a universal word has length `W+e`, the entire lower ideal partitions into
at most `W+e` inclusion chains, each of length at most `e`.  More precisely,
the chain assigned to right endpoint `j` has size at most `min(e,j)`.  This
gives the exact capacity

\[
  \Lambda\le eW+{e+1\choose2}.
\]

Thus `B(k)+O(1)` already contains an almost uniform, endpoint-serialized
chain-decomposition theorem.  The correct even-dimensional asymptotic is

\[
  \frac{2^k}{W}=\sqrt{\frac{\pi k}{2}}+O(k^{-1/2})
               =2d(k)+O(1),
\]

not its reciprocal.

### 2.2 The Greene--Kleitman central forest

The central triples of the Greene--Kleitman symmetric-chain decomposition
give every immediate lower and upper colour exactly once and have exactly
`Cat_m` components.  A complete acyclicity argument needs two facts: the
unmatched-symbol potential strictly falls along every oriented selected edge,
and every middle vertex has outdegree at most one.  Hence any undirected cycle
would have to be consistently directed, contradicting the potential.

The construction is not a linear forest: its maximum undirected degree can
be `m`.  It therefore does not by itself solve the ordered-diamond factor.

### 2.3 Bounded terminal eviction

Fix one final literal cap state and a matching `M_0` of old lower targets to
physical cells.  If selected tasks use distinct certified cells `b_i`, and
`D` is the **complete** set of cells whose old `M_0` realization fails after
all packet and cap changes, then all tasks and all but at most

\[
             |D\cap cells(M_0)|+h
\]

old targets remain matched.  The casualties may be appended at the terminal
dimension.

This removes zero-defect U5 from the additive-constant target.  It does not
remove the need to construct a final cap or certify complete remote damage.
Sidecar nonaccumulation is also separate: the next sidecar must have total
size at most `c`, including inherited debt.

### 2.4 A shortest resident collar

For every target Boolean-hex atom and depth `h`, the rotating-hole rail gives
the shortest possible private resident return path, of length `h+2`.  It has
an explicit depth-`h` wreath factorization, exact q1 palettes, and every
interval of at least three rail vertices has one union `Z`.  Its prefix and
suffix upper interfaces each have only three nested states.  For one fixed
hex choice its exact menu size is

\[
                         (m-2)(m-2)_h.
\]

This closes collar-internal residence and arbitrary-width upper support.
Exterior attachment and complete terminal damage are not consequences.

### 2.5 Fixed-H q1 planting

In the middle-levels incidence graph `ML_m`, every 2-bounded protected
subgraph with at most `m-2` edges extends to a spanning two-factor.  Therefore
any fixed bank of pairwise-disjoint plus-phase collar paths of total length
`O(Hd)` embeds for all sufficiently large `m`.

This proves the owner/q1 factor row.  The completion may still have `W/3`
components and need not cover the adjacent-upper palette.  A frozen `ML_4`
two-factor covers only 20 of the 21 relevant upper colours.

## 3. Rows which require correction

### 3.1 Prescribed Mütze pulls

For the canonical 2-factor and canonical flippable-pair 6-cycles in Gregor,
Mütze and Nummenpalo's short middle-levels proof, the 6-cycles are pairwise
**edge-disjoint**, and their noninterleaving property makes arbitrary subsets
noninterfering.  Thus a forest in that paper's auxiliary plane-tree graph can
be extended to a spanning tree and included in the resulting Hamilton cycle.

This theorem applies only to that canonical pull family on that canonical
2-factor.  No current result identifies a mixed-coatom packet or resident
rotating-hole collar with a canonical pull, nor embeds a prescribed packet
bank in the paper's base factor.  Therefore Mütze's spanning-tree argument
does not yet complete our packet topology.

Primary source: [Gregor--Mütze--Nummenpalo, A short proof of the middle
levels theorem](https://arxiv.org/abs/1710.08249), especially Propositions 2
and 3 and Section 5.

### 3.2 Terminal phase decoupling

The carried auxiliary phase and the terminal physical phase may use different
compiler matchings, cap states and upper-witness occurrences.  This removes
the unnecessarily strong requirement that every unary packet toggle preserve
one compiler.  It does not make the terminal plus state exist automatically;
that state still needs its own complete upper and bounded-damage certificates.

## 4. The four surviving bridges

1. **Bounded task birth.**  No theorem shows that every same-parity Pascal
   child exposes only `O(1)` compound tasks.  The exact conditional exposure
   relation is of the form `|U|<=4 Phi+b` after all topology, residence,
   upper and compiler debt have already been charged.  Raw finite transitions
   can expose bulk banks.

2. **Complete packet tickets.**  Prospective local packet families can be
   quadratic, and the resident rail itself has a much larger raw menu, but
   the strongest audited menu for one prescribed all-depth action is only
   linear.  No quadratic family is known in which every option simultaneously
   carries exterior upper ladders, rooted topology, a literal compiler cell,
   and its complete damage set.

3. **Upper-decorated bounded-component host.**  Fixed-H plus collars extend
   to a q1 two-factor, but not yet to one with `O(1)` components and only
   `O(1)` adjacent-upper holes.  Exact upper surjectivity and transparent
   cuts are stronger than the additive programme needs: opening `s`
   components loses at most `s` further upper witnesses, so `s+t=O(1)` may
   be appended once.  The near-factor/graphic-link normal form isolates this
   as one correlated matching statement.

4. **Bounded complete damage and regeneration.**  Local cell legality does
   not bound `|D cap cells(M_0)|`; remote common-cap shrinkage can route every
   nominally private option through one cap-one resource.  Even a bounded
   terminal casualty set must be mapped to a next admissible sidecar of total
   size at most the same constant.

The often-quoted conflict estimate `O(md)` is presently proved only for local
owner and immediate-palette resources after the target anchors are declared
private.  It is not proved for complete exterior-upper, topology and compiler
damage tickets.

## 5. Shortest honest missing theorem

A sufficient theorem, with no redundant phase-common U5 requirement, is:

> There are constants `c,H` and a same-parity transition such that every
> admissible sidecar of size at most `c` exposes at most `H` compound tasks;
> each task has a terminal plus packet carrying complete exterior-upper,
> q1/topology and literal-damage tickets; compatible choices plant in one
> `O(H)`-component host with only `O(H)` named upper holes; their complete damage meets at
> most `c` cells of one final reference matching; and the resulting total
> casualty set is again an admissible sidecar of size at most `c`.

This theorem implies `nu(k)<=B(k)+c`.  None of bounded task birth,
upper-decorated bounded-component completion, bounded complete damage, or sidecar
regeneration is currently proved.  The strongest progress is that residence,
internal higher support, the q1 factor extension, and perfect terminal U5 are
no longer among the missing rows.
