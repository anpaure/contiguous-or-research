# Mathematical research prompt for GPT Pro

You are taking over a research problem about universal contiguous-subarray OR
arrays.  Work primarily as a combinatorialist.  Computation may be used to
test or falsify a lemma on small cases, but do not make raw SAT/local search
the main contribution.

Read the attached `MATHEMATICAL_HANDOFF.md` completely before beginning.  Treat
its proved/conjectural distinctions as binding.  The objective is:

> For every integer `0 <= k < 20`, construct and certify a shortest array of
> masks below `2^k` whose nonempty contiguous-subarray ORs contain every mask.

Use `nu(k)` for the nonzero problem.  The original answer has one additional
literal zero: `N(k)=nu(k)+1` for `k>=1` and `N(0)=1`.

## Established ledger

Do not spend time rediscovering these facts.

1. The exact nonzero values are known through `k=10`, and also at `k=12`:

       nu(1..10) = 1,2,4,7,12,21,37,72,128,254,
       nu(12) = 926.

2. The rank-slack lower bound `B(k)` is proved.  Current sharp targets include

       k=11: 465 <= nu(11) <= 508,
       k=13: 1719 <= nu(13) <= 1852,
       k=14: 3434 <= nu(14) <= 3704.

3. The best proved general asymptotic construction is the complement-bridge
   Euler construction:

       W(k) <= nu(k) <= (sqrt(2)+o(1)) W(k),
       W(k)=binom(k,floor(k/2)).

   Wide-shadow erosion is only a conditional reduction theorem.  No
   near-width family of wide-shadow rows is known.

4. Exact optimal arrays at `k=9,10,12` exhibit the same hidden structure.  For
   delay two, `T=D^2 A` is a permutation of the middle layer, is a Johnson
   Hamilton path, and has complete upper union shadows.  At `k=10,12`, its
   adjacent and triple intersection shadows are also complete.  The factor
   labels are sparse subsets of the maximal intersection envelopes.

5. A new explicit `k=14` central skeleton is proved.  It is a Hamilton path
   through all 3432 rank-7 masks, and its adjacent intersections cover all
   3003 rank-6 masks.  It is obtained by braiding:

   - a cut of a `k=13` middle-levels cycle whose rank-7 path has all but one
     rank-6 intersection color; and
   - the complemented rank-8-union-complete `k=13` path, whose adjacent
     intersections cover all rank-5 masks.

   An endpoint repair makes the seam supply the one omitted rank-6 color.
   This is not yet an optimal OR array: factorability, upper shadows, and
   global lower labeling remain.

6. The exact pinnability theorem is available.  For a central row
   `T_1,...,T_M` and delay `d`, let

       E_j = intersection {T_i : max(1,j-d)<=i<=min(M,j)}.

   Assign each lower target `S` injectively to a short interval `J_S`.  For a
   coordinate `b`, define

       Z_b = {j : b in E_j} minus union{J_S : b notin S}.

   The assignments and central row are simultaneously realizable exactly when

       J_S intersects Z_b for every b in S,
       [i,i+d] intersects Z_b for every b in T_i.

   Thus complete maximal-intersection shadows are sufficient but not
   necessary.  Do not replace pinnability by the stronger erosion condition.

## Primary mathematical target: solve k=14

For `k=14`, put `M=binom(14,7)=3432` and `d=2`.  Seek an explicit ordering

    T_1,...,T_M

of every rank-7 mask exactly once such that:

1. every internal coordinate 1-run has length at least three;
2. the rank-6 adjacent-intersection envelopes are sufficiently rich to label
   every rank-6 target (complete coverage is the cleanest version);
3. every mask of rank greater than seven is the union of some consecutive
   segment of `T`;
4. the envelopes admit an injective assignment of all ranks 1--6 to singleton
   or adjacent-pair factor intervals satisfying the pin-survival theorem.

Any such row gives a length-3434 nonzero array and proves

    nu(14)=3434.

Try to construct it mathematically from the dual-path braid, the exact `k=12`
row, a symmetric-chain decomposition, or a middle-levels cycle.  Ordinary
Johnson Hamiltonicity is not enough: both edge colors and longer shadows must
be controlled.

### Suggested edge-color viewpoint

A Johnson edge between two rank-7 sets has two colors

    C = T_i intersection T_(i+1),  |C|=6,
    U = T_i union T_(i+1),         |U|=8.

Equivalently it is an incidence pair `C subset U` with `|U\C|=2`; the two
middle vertices are `C+x` and `C+y`.  A desired path uses 3431 such edges and
must cover both sets of 3003 colors, with 428 repetitions available on each
side.  Develop this as a two-colored Euler/trail/decomposition problem rather
than an unstructured permutation problem.  Look for:

- a decomposition of the rank-6/rank-8 incidence graph into alternating
  trails that splice into one Hamilton path;
- a symmetric-chain or middle-levels involution pairing lower and upper
  colors;
- an explicit switching lemma that merges trail components while preserving
  both color covers and the length-three coordinate-run condition;
- a recursive two-bit lift whose seam defects form a provably repairable
  bounded family.

The existing dual-path braid proves complete lower color coverage.  Determine
what additional orientation, complement, or interleaving condition makes its
upper colors complete without destroying the lower cover.

## Second target: prove a factor-labeling theorem

The successful finite constructions suggest a general theorem stronger than
case-by-case SAT but weaker than maximal erosion.

For delay two, define internal envelopes

    F_i = T_(i-1) intersection T_i,
    E_i = T_(i-2) intersection T_(i-1) intersection T_i.

The factor must choose nonempty `A_i subset E_i`, while
`A_i union A_(i+1) subset F_i`.  In the exact `k=12` optimum, most labels equal
their maximal envelope and a sparse set is shrunk to enumerate lower masks.

Seek a Hall-type, matching, absorption, nibble, or local-lemma result of the
following form:

> If a middle-layer path has prescribed run expansion and sufficiently
> uniform envelope multiplicities, then all lower masks can be injected into
> short intervals while retaining a legal coordinate pin in every assigned
> target interval and every central window.

Work out the exact bipartite or hypergraph object.  State verifiable Hall
conditions.  Try first to prove a finite theorem specialized to `k=14,d=2`;
then identify an asymptotic version.  A proof that the known `k=14` lower-color
skeleton is labelable after a mathematically specified switching operation
would be a major result.

## Third target: classify equality in the unrestricted problem

Do not assume every optimum has a fixed row `T=D^d A`.  Use the monotone-band
normal form.

For one witness interval for each central mask in length `M+d`, sorted by left
endpoint,

    I_i=[i+alpha_i,i+beta_i],
    0<=alpha_1<=...<=alpha_M<=d,
    0<=beta_1<=...<=beta_M<=d,
    alpha_i<=beta_i.

For `k=14,d=2`, this path lies in only six triangular states and changes state
at most four times.  Classify all possible regimes.  Try to prove one of:

1. every length-3434 optimum can be transformed into the fixed length-three
   central-row form without increasing length; or
2. every non-fixed regime violates a rank/shadow/endpoint capacity inequality;
   or
3. the finitely many regime types reduce to explicit combinatorial objects
   comparable to the fixed-row path.

Use interval containment, endpoint matchings, Kruskal--Katona shadows, LYM,
and the submodularity of union.  A theorem here would turn success or failure
of the fixed-row construction into a statement about the unrestricted optimum.

For odd dimensions, use the proved two-colored middle-layer forest theorem
rather than assuming one Hamilton path.  At `k=11,d=3`, any optimum forces at
most six alternating path components and nearly all central masks are
two-sided flags.  Seek a switching theorem that joins these components or a
counting obstruction that rules out the remaining endpoint schedules.

## Fourth target: a proved recursive lift

Formalize the pattern

    odd middle-levels object -> complemented dual path -> next even central row.

Prove a lift theorem with explicit hypotheses on:

- omitted lower color and endpoint containment;
- complete upper colors of the dual path;
- coordinate-run inheritance;
- lower pin-survival under the factor delay drop;
- all seam-crossing upper union shadows.

The current `k=13 -> k=14` braid proves only the central enumeration and lower
edge-color part.  Isolate the exact extra endpoint/shadow hypotheses that make
the lift universal.  Then check whether the exact `k=12` structure supplies
those hypotheses recursively.

Do not use physical padding at every recursive node.  Any recursive overhead
must satisfy `s(k)h=o(W(k))`; a recursion with `Theta(W(k))` padded seams is not
near-width.  Prefer cyclic globalization or virtual endpoint signatures
resolved by one final matching.

## Lower-bound route if construction fails

Try to strengthen the rank-slack bound using dependencies among overlapping
short intervals.  Raw interval counting treats all windows as independent,
which they are not.  Promising sources of additional inequalities are:

- consecutive suffix OR chains sharing all but one entry;
- forced collisions between rank-`r-1` and rank-`r+1` shadows of central
  witnesses;
- endpoint-set intersections across several adjacent ranks;
- Hall deficiencies in the target-to-short-interval assignment;
- the at-most-`2d+1` regime structure of the monotone band path.

A rigorous lower bound `nu(11)>465`, `nu(13)>1719`, or `nu(14)>3434` would be
as valuable as a construction, but an UNSAT result for a fixed-row ansatz is
not an unrestricted lower bound.

## Required working style and deliverable

1. Begin with a short theorem ledger: inherited proved facts, inherited
   conjectures, and the exact new statement you will attack.
2. Select one primary lemma.  Push it to a proof or a precise counterexample;
   do not merely list literature or restate the original problem.
3. Give complete combinatorial proofs line by line.  Explicitly identify every
   place where cyclic versus linear endpoints matter.
4. If a construction theorem is proved, give deterministic pseudocode and
   C++17/20 generation and verification code.  The verifier must enumerate
   distinct suffix ORs independently.
5. If the proof stops, return the strongest proved intermediate lemma, the
   exact remaining implication, and a sharply narrowed next target.  Never
   label a heuristic row, a conditional erosion, or a fixed-ansatz failure as
   the solution of the unrestricted problem.

The preferred outcome is a mathematical construction proving
`nu(14)=3434`, because it would provide a new exact base and a concrete test of
the dual-path/pinnability theory.  The preferred general outcome is a proved
two-sided central-path theorem plus a Hall/nibble factor-labeling theorem.
