# Independent audit of K17 three-level normal chainization

**Date:** 2026-08-02  
**Verdict:** **PASS**, with one wording clarification for the lollipop
application.  The theorem proves an exact static depth-three partition and
its attachment to any incidence phase having a perfect matching.  It does
not serialize the attached chains into one chronology and does not establish
residence, upper shadows, common-cap feasibility, or a K17 word.

Audited source:

```text
MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md
SHA-256 6fa4056052919edabd0914c8744b5dc137f2c8f9dff54ed313ecf0e58af57279
```

## 1. Exact arithmetic

For

\[
 P_0=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 P_1={[17]\choose7},\qquad P_2={[17]\choose8},
\]

the displayed sizes independently recompute as

\[
\begin{aligned}
 |P_0|
 &=17+136+680+2380+6188+12376=21777,\\
 |P_1|&=19448,\\
 |P_2|&=24310.
\end{aligned}
\]

Their sum is

\[
 21777+19448+24310=65535
   =\sum_{s=1}^{8}{17\choose s},
\]

so the compressed poset contains every nonempty target of rank at most eight
exactly once.  The adjacent rank-seven/rank-eight incidence identity also
checks literally:

\[
 10|P_1|=194480=8|P_2|.
\]

Thus the numerical statements in (2.1) and (3.3) are exact.

## 2. The first coupling

For an original-rank-`s` element `S` of `P_0`, the number of containing
rank-seven sets is `\({17-s\choose7-s}\)`.  Hence

\[
 \sum_{T\supset S}\frac{1}{|P_0|{17-s\choose7-s}}
 =\frac1{|P_0|}.
\]

For fixed `T` of rank seven, the second marginal is

\[
 \frac1{|P_0|}
 \sum_{s=1}^{6}
 \frac{{7\choose s}}{{17-s\choose7-s}}.
\]

The identity used in the source is correct because both sides equal

\[
 \frac{7!\,(17-7)!}{s!\,(17-s)!}
 =\frac{{17\choose s}}{{17\choose7}}.
\]

Consequently the sum is

\[
 \frac1{|P_0|}\frac{\sum_{s=1}^{6}{17\choose s}}{{17\choose7}}
 =\frac1{|P_1|}.
\]

There is therefore a genuine containment-supported coupling with uniform
marginals on `P_0` and `P_1`; no integrality assumption is being smuggled
into this step.

## 3. Gluing the two couplings

For the rank-seven/rank-eight coupling, each rank-seven set has ten upper
neighbors and each rank-eight set has eight lower neighbors.  The weight
`1/(10|P_1|)` therefore gives marginals `1/|P_1|` and `1/|P_2|`.

The phrase "couple conditionally" can be made explicit.  If
\(\mu_{01}\) and \(\mu_{12}\) denote the two edge measures, set

\[
 \pi(S,T,U)=|P_1|\,\mu_{01}(S,T)\mu_{12}(T,U).
\]

Then \(\pi\) is supported only on \(S\subset T\subset U\), has total mass
one, and its three vertex marginals are respectively

\[
 1/|P_0|,\qquad 1/|P_1|,\qquad 1/|P_2|.
\]

This verifies the only probabilistic composition used by the proof.

## 4. LYM, width, and the integral conclusion

Every sampled triple is one inclusion chain.  An antichain `A` can therefore
meet it at most once, and linearity of expectation gives

\[
 \frac{|A_0|}{21777}+
 \frac{|A_1|}{19448}+
 \frac{|A_2|}{24310}\le 1.
\]

Since each denominator on the left is at most `24310`,

\[
 |A|/24310\le 1.
\]

The whole top level is an antichain of size `24310`, so the width is exactly
`24310`.  Dilworth now supplies the required **integral** partition into
`24310` chains.  This is not merely a fractional-chain conclusion.

There are exactly `24310` top elements, and two top elements cannot lie in
one chain.  Hence every chain in the partition contains exactly one
rank-eight element.  The compressed poset has three levels, so every chain
has at most three elements.  This proves Theorem 1 exactly as stated.

## 5. Owner attachment and the lollipop qualification

If a rank-eight/rank-nine incidence graph has a perfect matching, match the
unique rank-eight top `U` of every chain to an owner `R`.  All earlier chain
members lie inside `U`, and `U` is a proper subset of the rank-nine owner.
Thus every member assigned to `R` is a proper subset of `R`, and Corollary 2
is valid.

For a bipartite two-factor, alternating every even cycle supplies the needed
perfect matching.  The authenticated K17 augmented factor is a lollipop, not
literally a two-factor: all ordinary vertices have degree two, the rank-eight
root `M` has degree one, and the rank-eight root `D` has degree three.  Its
perfect matching is nevertheless elementary.  Write the tail as

\[
 M=L_0-U_1-L_1-\cdots-U_t-L_t=D.
\]

The leaf edge `L_0U_1` is forced, after which the matching propagates as
`L_{i-1}U_i` along the tail.  This leaves `D` for either alternating matching
of the residual even cycle.  So the source sentence "the leaf forces the
tail matching, after which the remaining even cycle alternates" is sound
when "forces" is read as this propagation along the entire tail.  It would
be slightly clearer to say this explicitly, but no theorem correction is
needed.

## 6. Exact `d=3` scope

The theorem closes the following static K17 row:

* all `65535` nonempty lower named targets are assigned once;
* there are exactly `24310` owner-indexed rows;
* each row contains at most three nested targets;
* every target in a row is contained in the row's rank-eight top and hence
  in its matched rank-nine owner.

This justifies the phrase "depth-three payload table" and shows there is no
unmatched target and no need for a fourth static slot.

It does **not** prove that the three entries of each row occur as suffix or
prefix unions of a literal source word.  In particular it does not impose:

1. a cyclic or rooted-Euler order on the owner rows;
2. statewise age/history balance;
3. the prescribed pivot collar or global address consistency;
4. residence of the resulting chronology;
5. immediate or deeper upper-shadow coverage;
6. common-cap/Hall compatibility or a universal word.

Thus, in the current `PCS` interface, equitable lower-chain allocation at
`k=17,d=3` is closed, while chronology/state balance and the upper/residence
rows remain genuinely separate.

## 7. Dimension dependence

The proof is genuinely special to this compressed size ordering.  At the
next literal analogue, `k=19`, one would use original ranks `1` through `7`
in the compressed bottom and ranks `8,9` above it.  Then

\[
 \sum_{s=1}^{7}{19\choose s}=94183
 >{19\choose9}=92378.
\]

So the top is no longer the largest compressed level; the argument cannot
give one top-ended chain per owner without changing the state.  This confirms
the source's warning and prevents treating the K17 table as an all-`m`
chainization theorem.

## 8. Independent constructive-table replay

The theorem's new Section 5 is also independently authenticated.  I wrote a
separate O3 C++ parser which does not use the builder's Hopcroft--Karp or
replay code.  It reads the frozen payload, the complete `218790`-row
incidence map, and the residence-2018 primary model independently.  It
checks:

* every incidence-map variable occurs exactly once and every selected edge
  is a legal rank-eight/rank-nine containment;
* the selected factor has exactly `48620` distinct incidences;
* every payload row has declared length one, two, or three, is strictly
  nested, ends at its declared rank-eight root, and lies in its declared
  rank-nine owner;
* every payload root--owner edge is selected in the frozen factor;
* every nonempty target of ranks one through eight occurs exactly once;
* every rank-eight root and every rank-nine owner occurs exactly once.

The independent result is

```text
PASS rows=24310 targets=65535 roots=24310 owners=24310 selected=48620
chain lengths 1,2,3                  1748,3899,18663
target ranks 1,...,8
  17,136,680,2380,6188,12376,19448,24310
selected root degrees 0,1,2,3        0,1,24308,1
selected owner degrees 0,1,2,3       0,0,24310,0
```

The root/owner uniqueness plus membership of all `24310` table edges in the
selected factor independently proves that the table itself is attached by a
perfect incidence phase.  The degree histogram also independently recovers
the leaf/branch lollipop signature used in Section 5 above.

Frozen independent artifacts:

```text
scratch/audit_k_k17_exact_depth3_owner_payload_independent_20260802.cpp
  SHA-256 d4ad3556caa01d96b82be88562ea201762643c5e68fab3ebb43a72d8d710814e
scratch/k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.independent.audit.json
  SHA-256 b9a50eb60bf338e7750404a77be85fcb9aba15ef8676e53dc3d9b0ae75567e1c
```

The independently replayed payload has SHA-256
`029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1`,
matching the theorem.  This authenticates the static table and its selected
incidence phase only; it deliberately does not replay the factor's complete
CNF, chronology, residence, upper deck, common cap, compiler, or word.

## 9. Final scope verdict

The theorem is proof-safe as an unconditional finite static result.  Its
proper use in Protected Catalan--pivot work is to remove the K17 lower
named-target allocation row from the finite interface.  It is positive
structural evidence that this row can coexist with any chosen owner phase
having a perfect matching, including the authenticated lollipop phase.  It
now also supplies one independently replayed literal static table on the
residence-2018 lollipop phase.  It does not by itself strengthen the all-`m`
upper-exact/resident host theorem and must not be cited as a chronology or
compiler construction.
