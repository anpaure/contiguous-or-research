# K17 compressed-normal no-singleton chain recoupling is two-matroid intersection

Date: 2026-08-02

## Statement

Let

\[
 L=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 M={[17]\choose7},\qquad
 R={[17]\choose8}.
\]

Their sizes are

\[
 |L|=21,777,qquad |M|=19,448,qquad |R|=24,310.
\]

Let `T_L` be the transversal matroid on ground set `M disjoint-union R`
presented by the containment graph from `L`: a receiver set is independent
when its members can be matched injectively to distinct contained low
targets.  Its rank is 21,777.

Let `T_7` be the transversal matroid on ground set `R` presented by the
rank-seven/rank-eight containment graph.  Its rank is 19,448.  Define the
matroid on `M disjoint-union R`

\[
 N=T_7^*\oplus U_{16,915,M}.                         \tag{1}
\]

### Theorem 1 (common-basis equivalence)

The following objects are equivalent.

1. A **compressed-normal** partition of all 65,535 nonempty targets of ranks
   at most eight into 24,310 inclusion chains, each ending in a distinct
   rank-eight target, with length histogram

   \[
     (n_1,n_2,n_3)=(0,7,395,16,915).
   \]

   Here compressed-normal means that every chain contains at most one member
   of `L`; equivalently, every length-three chain has the form `L-M-R`.

2. A common basis `C` of `T_L` and `N`.

Consequently the compressed-normal static no-singleton chain-recoupling face
is ordinary two-matroid intersection.  It has the exact Edmonds min--max
criterion

\[
 r_{T_L}(X)+r_N((M\dot\cup R)\setminus X)\ge21,777
 \quad\text{for every }X\subseteq M\dot\cup R.       \tag{2}
\]

This theorem supplies a root-bank-changing recoupling face available after
the rank-seven fixed-root SCC obstruction.  The SCC result requires such a
change only for a move-each-defect architecture; indirect socket repair of an
unchanged label remains logically possible.  The common-basis theorem is
stronger than the frozen bottom-relocation matching inside the
compressed-normal face and does not require a three-dimensional matching
there.

The qualifier is essential.  The histogram alone does not force
compressed-normality.  If `a,b,c,d` count chains of types `L-L-R`, `L-M-R`,
`L-R`, and `M-R`, respectively, the same counts permit

\[
 b=16,915-a,\qquad c=4,862-a,\qquad d=2,533+a
\]

for any `0 <= a <= 4,862`.  Those `L-L-R` faces are not represented by the
two matroids in this theorem.

## Proof

Suppose first that `C` is a common basis.  Since `C` is a basis of the direct
sum in (1),

\[
 |C\cap M|=16,915,qquad |C\cap R|=4,862.             \tag{3}
\]

Because `C` is a basis of `T_L`, match every member of `L` bijectively to a
containing receiver in `C`.  If the receiver lies in `M`, this supplies the
first edge of a length-three chain.  If it lies in `R`, it supplies a direct
length-two chain.

Put

\[
 B=R\setminus(C\cap R).
\]

The set `C cap R` is a basis of `T_7^*`, so its complement `B` is a basis of
`T_7`.  Match every rank-seven target bijectively to a containing root in
`B`.

Now concatenate the two matchings.  Every `m in C cap M` has one low
predecessor and one rank-eight successor, giving 16,915 length-three chains.
Every `m notin C` has only its rank-eight successor, giving

\[
 |M|-16,915=2,533
\]

length-two chains.  Every root in `C cap R` has its direct low predecessor,
giving another 4,862 length-two chains.  Hence

\[
 2,533+4,862=7,395.
\]

Every low, rank-seven, and rank-eight target is used exactly once, and all
edges are containments.  This constructs object 1.

Conversely, start from a compressed-normal chain partition in object 1.  Let `C cap M` be the
rank-seven targets having a low predecessor, and let `C cap R` be the roots
having a direct low predecessor.  The first edges of the chains match every
low target bijectively to `C`, so `C` is a basis of `T_L`.  The rank-seven
successor edges match every member of `M` to

\[
 B=R\setminus(C\cap R),
\]

so `B` is a basis of `T_7`, and therefore `C cap R` is a basis of `T_7^*`.
The length histogram forces `|C cap M|=16,915`.  Thus `C` is a basis of `N`
and hence a common basis.  This proves the equivalence.

Equation (2) is Edmonds' common-base theorem applied to two matroids of rank
21,777 on the same ground set.  QED.

## Algorithmic consequence

Weighted matroid intersection can change the rank-seven receiver-root bank
while retaining exact target use and the no-singleton histogram within the
compressed-normal face.  The rank
oracles are ordinary bipartite maximum matchings:

- one on low targets versus `M disjoint-union R`;
- one on rank-seven targets versus `R`, followed by the standard dual-rank
  formula and the uniform-matroid term in (1).

Thus a receiver-element objective—for example, penalizing the current roots
which host the 162 SCC-singleton target labels—is a legitimate weighted
common-basis problem.  This is an outer allocation objective, not a proof
that retiring precisely those roots is sufficient: an exchanged basis still
needs compatible matching witnesses and occurrence-labelled sockets.

## What remains nonmatroidal

The theorem deliberately stops before occurrence-labelled socket selection.
For a common basis `C`, one must still choose representing matchings with:

- every direct `L -> R` chain carrying a common-phase short socket;
- every `M -> R` chain whose `M` has no low predecessor carrying a
  common-phase short socket;
- mutually compatible predecessor/successor hosts, flags, and physical
  cells;
- the protected/private bank or a regenerated replacement;
- supplier Hall, residual long-state flow, one chronology, residence,
  upper/source/compiler closure.

Marginal socket positivity is edge-labelled, not merely a weight of the
common-basis element.  In variables `x_(m,r)` and `y_(l,m/r)`, a
socket-negative rank-seven/root edge obeys the implication

\[
 x_{m,r}\le\sum_l y_{l,m}.                            \tag{4}
\]

These cross-matching implications are not proved to preserve matroidality or
total unimodularity.  The exact next gate is therefore a socket-labelled
common-basis lift, not static chainization.

## Finite witness

The authenticated raw-warm47 table has histogram `(0,7395,16915)`, is
compressed-normal, and directly yields one common basis:

- its 16,915 long-chain middles form `C cap M`;
- its 4,862 roots with direct rank-at-most-six predecessors form `C cap R`;
- the chain edges witness the `T_L` basis matching;
- the 19,448 rank-seven/root edges witness the complementary `T_7` basis.

The companion audit reconstructs these sets and matchings directly from the
literal table.  This finite witness proves both matroid ranks used above and
checks that the abstract equivalence binds to the current K17 payload data.

Evidence:

- `scratch/audit_root_k17_no_singleton_common_basis_witness_20260802.cpp`, SHA-256 `8798df9a884ea734c2cfac73e5224914249aeaff52004259f8784c781ffa7bf7`;
- `scratch/k17_fixed_p2_role_moving_escape_20260802/no_singleton_common_basis.audit.json`, SHA-256 `b670975d64177e4c618e075f78e3dadac31f1a4116290f83322058c249140995`;
- authenticated table SHA-256 `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`.

The independent H100 O3 replay is frozen under
`/home/amodo/or15/work/root_k17_no_singleton_common_basis_20260802/` and
reproduces the source, table, and audit hashes.

Scope exclusions: chain partitions containing `L-L-R` chains, socket/state
compatibility, carrier chronology, residence, upper shadows, common cap,
compiler, source, and a universal word.
