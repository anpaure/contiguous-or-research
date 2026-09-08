# Audit of the attached Ucycle/MTF exploration

Date: 2026-07-25

Source audited:
`/Users/amir.nuriyev/.codex/attachments/5cbf00c3-efea-412b-bac1-236b8158104d/pasted-text.txt`.

Method: pure mathematical audit. No computation or web search.

## 0. Overall verdict

The attachment is a duplicated, unfinished stream of exploration, not a
proof note. It contains several correct standard reductions and useful
heuristics, but no new theorem which advances the calibrated constant-one
frontier. Its central asserted reduction

\[
 \nu(k)=(1+o(1))W(k)
 \quad\Longleftrightarrow\quad
 \text{a central near-Ucycle with good shadows exists}
\]

is false as stated: singleton recency words are a sufficient restricted
architecture, not a necessary normal form for general set-valued OR
words. The growing common-top packet construction is already a concrete
counterexample to the alleged necessity of one global FIFO Ucycle as a
proof architecture.

The attachment neither proves a near-Ucycle nor supplies a valid
growing-uniformity matching theorem. Its product construction stops before
a coherent statement and the file then repeats its opening text.

## 1. Correct claims

### 1.1 Endpoint-chain lower bound

At one right endpoint the suffix unions form an inclusion chain, hence
contain at most one middle-rank set. Therefore every universal word has
length at least (W(k)). This is correct and already established.

### 1.2 Ordered-partition/MTF dictionary

The recency blocks of a word form an ordered partition, and its prefix
unions are exactly the suffix ORs ending at the current position. MTF on a
permutation state is ordinary move-to-front. These statements are correct.

### 1.3 Singleton FIFO subproblem

If every touch is a singleton outside the current top (m), then the
middle owner is the set of the last (m) symbols and evolves by FIFO
Johnson steps. A perfect singleton construction is therefore a Ucycle for
the middle layer. The ordered-((m-1))-tuple de Bruijn digraph and the
``choose one ordering per (m)-set so that the selected edges are
Eulerian'' formulation are correct for this restricted problem.

### 1.4 Basic Ucycle arithmetic

For (n=2m+1), a perfect middle Ucycle would use every coordinate

\[
 \frac1n\binom{2m+1}{m}=\operatorname{Cat}_m
\]

times. Consecutive equal middle windows forbid a symbol from returning at
the immediate FIFO exit. A minimum recurrence gap at least (m+H) would
indeed make every ordinary window through length (m+H) injective. None
of these observations constructs such a sequence.

### 1.5 Random and isolated-reset warnings

Independent or random-walk occupancy at mean about one leaves a positive
fraction of shallow targets uncovered. A path-hypergraph ABKV argument
with one reset per growing path encounters an exponential-in-uniformity
condition and cannot reach mesoscopic path length. These qualitative
warnings agree with the audited project record, although the attachment's
degree/codegree estimates are heuristic rather than proved.

### 1.6 De Bruijn circuit splicing principle

Two directed circuits in a selected de Bruijn subgraph can be merged if
they share a directed state. This is a valid Eulerian observation. The
attachment does not show that the MSW wreath circuits have enough shared
ordered states, nor construct legal surgeries which create them.

## 2. Unsupported or false claims

### 2.1 Permutation states are not without loss of generality

The attachment repeatedly concludes that near optimality forces almost
every state to be a permutation and hence forces a near-Ucycle. The middle
rank only forces almost every endpoint to expose a new middle set. It does
not force that middle set to occur at singleton depth (m), nor force the
entire state to be a permutation. Block-MTF and common-top promotion paths
give valid alternative dynamics.

Thus ``the reduction to near-Ucycles is unavoidable'' and the claimed
equivalence with the original conjecture are false.

### 2.2 The trailing-singleton distribution is not derived

Lines 39--43 assert that the number (T) of trailing singleton blocks has

\[
 \Pr(T\ge q)\simeq e^{-q^2/m}
\]

and is forced to follow the SCD radius law. Coverage counts only impose
lower bounds on the number of endpoints capable of exposing a given rank;
they do not determine a probability distribution on block structures.
The attachment later notices that full permutation states overexpose all
ranks, contradicting its earlier ``forced distribution'' conclusion.

### 2.3 Depth-reset claims are unproved

The one-step nonincrease lemma for two consecutive distinct middle owners
is a known conditional statement. The later assertion that every
non-middle-exposing step can increase the next middle depth by at most one,
and hence that the global depth process has only (R) units of upward
variation, is not proved and is not a consequence of the cited one-step
lemma.

### 2.4 Static block partial-sum closure is inapplicable

The claim that all block-boundary partial sums form unions of arithmetic
progressions modulo (m) treats a dynamically changing MTF partition as
one fixed block sequence. The attachment itself subsequently observes that
recency blocks are altered by overlaps with future masks. No valid global
periodicity theorem follows.

### 2.5 Upper shadows do not follow from a middle Ucycle

A middle Ucycle controls length-(m) FIFO windows only. Longer recency
prefixes can contain returns, and shorter windows need not cover their
ranks. The attachment correctly notices this at several places, but later
continues to speak as if a near-Ucycle alone were equivalent to constant
one. The additional gap and all-depth coverage requirements are major,
unproved conditions.

### 2.6 Ucycle divisibility statement for (n=2m)

The assertion that (2m\nmid\binom{2m}{m}) always holds is false; for
example

\[
 \binom{12}{6}/12=77.
\]

Divisibility is a necessary condition in the cyclic singleton problem,
not a uniform obstruction for every even central parameter.

### 2.7 Path-hypergraph nibble calculation is heuristic

The estimates

\[
 \Delta_2/D\approx L/m^2
\]

and the resulting (L\lesssim\log m) ABKV ceiling are not derived with
an exact path census, endpoint convention, or common degree. They point in
the same direction as the proved isolated-reset ceiling elsewhere, but do
not constitute a new proof.

### 2.8 Product construction is incomplete

The proposed two-profile periodic construction reaches a contradiction in
its own state count, is then reconsidered, and never states a valid word or
coverage theorem. The source ends by repeating its opening discussion.

## 3. Comparison with the current top-packet frontier

The attachment does not engage the stronger current architecture:

1. choose (H\sim\sqrt{m\log m}) so that one packet per top has total
   capacity (W-o(W)) and reset cost (o(W));
2. use a reservoir to restrict hard discrepancy to
   (Q\sim\sqrt{m\log\log m});
3. use complementary promotion segments so two paths per top retain
   (M-O(1)) distinct owners;
4. use four-order rectangles to isolate one hard lower or upper rank while
   preserving the middle and every other hard rank; and
5. exploit that these rectangles generate the full integral
   point-incidence kernel, leaving positivity/availability rather than a
   parity obstruction.

The attachment's global near-Ucycle route is therefore neither necessary
nor closer to completion than the calibrated packet route.

## 4. Genuinely useful residue

The only reusable content is a clean restricted formulation:

> Select one ordering of each middle set so that the corresponding edges
> in the ordered-((m-1))-tuple de Bruijn digraph form an Eulerian subgraph
> with few components, and impose long recurrence gaps for upper shadows.

This is mathematically valid as a sufficient singleton-word problem. It is
also at least as hard as the unresolved central near-Ucycle problem and
does not supply the missing construction.

No claimed theorem in the attachment changes the confidence or status of
the coefficient-one proof.

