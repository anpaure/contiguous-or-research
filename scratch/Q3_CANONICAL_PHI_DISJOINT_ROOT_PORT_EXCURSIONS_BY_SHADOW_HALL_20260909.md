# Disjoint five-step Phi excursions at every fixed-root port

Date: 2026-09-09. Status: proved conditional stage theorem; pure proof,
with no matching computation or new word construction executed.

**Later scope resolution:** the local disjoint-path theorem below remains
valid, but retaining ALL its first entrance incidences prevents completion
to any spanning strict canonical-Phi factor of residence at least2.
At least Cat_(r-1) of those Cat_r incidences must change. See the independently
reviewed [all-root entrance obstruction](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md).
Thus this whole fixed bank is not an extendible induction template.

The first11 collisions in the fixed prescribed-parent diagnostic can be
removed by changing the second old deletion. A further fixed deletion then
makes both11 banks and the output bank disjoint. For every r>=7 and every
residence-three canonical-Phi parent factor on all old rank-r states, this
produces pairwise vertex-disjoint five-step child excursions at all
Cat_r fixed-root ports. The theorem does not assemble a spanning factor,
preserve an all-rank target deck, or produce an optimal word.

## 1. Sources, attribution and hypotheses

This applies the existing small-family shadow/Hall argument in
[Catalan cap-two compression, Section1](../MATH_THEOREM_CATALAN_CAP_TWO_COMPRESSION_20260731.md)
and [the full-orbit note, Lemma5.1](../MATH_ATTACK_N_FULL_ORBIT_ESCAPE_AND_Q1_CYCLE_20260725.md).
It is not a new shadow theorem. The imported continuous shadow inequality
is stated in Peter Keevash, *Shadows and intersections: stability and new
proofs*, Introduction, page1: if a k-uniform family has cardinality
binom(x,k), x>=k real, then its lower shadow has cardinality at least
binom(x,k-1). [Primary paper](https://arxiv.org/pdf/0806.2023).

The canonical insertions, age convention and injective old-coordinate map
J used below are established in
[the sector-excursion proof, Sections4,7,9](CANONICAL_PHI_BALANCED_BLOCK_BARRIER_AND_MINIMAL_RUN_SECTOR_EXCURSION_20260909.md).
The new content is their application to the age-unrestricted second
deletion when q=3, and the deletion of the old root in the next step.
The repair and root-deletion closure were proposed by the root agent;
the induction agent independently audited and recorded them here.

Let the old alphabet have 2r+1 positions, r>=7. Phi adds the zero at the
first global minimum of the prefix walk, where ones contribute +1 and
zeros contribute -1. Let sigma be a permutation of all old rank-r states
such that

    sigma(L)=Phi(L)-d(L),  d(L) in L,

and every positive coordinate run in this parent factor has length at
least3. This includes its cyclic age histories; the factor need not be a
single cycle. Fix the physical root position u and list positions from u.
The root-aligned inputs are exactly L=0D, with D a Dyck word of semilength r.
There are Cat_r such inputs, and Phi(L)=L+u.

Append adjacent new coordinates a,b after the old word, initially10. At
each input L+a, use an actual lifted parent history with a held present and
b absent. Consequently a has age at least3 and the old ages dominate the
parent ages. Arbitrary independently declared ages are not an assumption.

## 2. Every second deletion is legal for q=3

Keep the first old deletion d=d(L) prescribed by the parent and put

    U=Phi(L)=L+u,       P=sigma(L)=U-d.

The first three states are

    X0=L+a,            X1=U,             X2=P+b.

The transitions insert u and b and delete a and d. They are canonical Phi
steps, by the prefix-walk argument in the source proof. Deleting a is
legal because its incoming age is at least3. Deleting d is legal because
it was already age at least3 in L and has survived the extra state X1.

Phi at X2 inserts a. Crucially, every old e in P minus {u}=L minus {d}
is present at X0, X1 and X2. Its age at this third deletion is therefore
at least3 even if it had age only1 at X0. Thus ANY such e is legal, giving

    X3=(P-e)+a+b.                                      (2.1)

This freedom is particular to this q=3 stage: these three states do not
by themselves certify age4 or any larger required age. No second-parent-
deletion restriction remains. The 00 old parts U and 01 old parts P are
injective across ports by the Phi matching and the parent permutation.

## 3. Hall makes the entire first11 bank injective

For each port define A_L=P minus {u}, an (r-1)-set. These sets are distinct.
Choosing e in A_L amounts to choosing an (r-2)-facet G_L of A_L, with

    K_L=P-e={u} union G_L,      X3=K_L+a+b.

We recall the precise small-family consequence of the continuous shadow
theorem. If a k-uniform family F has cardinality at most binom(2k-1,k),
then every subfamily E has at least |E| lower-shadow members. For nonempty
E write |E|=binom(x,k). Then k<=x<=2k-1 and

    |partial E| >= binom(x,k-1)
                 = |E| k/(x-k+1) >= |E|.

The empty subfamily is immediate. Applying Hall's theorem to incidence
between F and its (k-1)-shadow gives distinct facet representatives.

Here k=r-1. The exact size comparison is

    Cat_r / binom(2r-3,r-1) = 4(2r-1)/(r(r+1)) <= 1,   (3.1)

since r(r+1)-4(2r-1)=r(r-7)+4>=0 for r>=7. Thus Hall applies to ALL
subfamilies of the full root-port family, and there is a choice of the
e(L) for which all K_L are distinct. This is an integral assignment.
It may be materialized by any deterministic augmenting-path matching
algorithm, but no such algorithm has been run here. Reassigning a prior
port during augmentation remains legal because all its facet choices
have the same age guarantee from Section2.

The same argument works for any port subfamily whose size is at most
binom(2r-3,r-1). For r<7 this bound alone does not cover every root port;
no impossibility is asserted in those dimensions.

## 4. The injective old-coordinate map J

For an old (r-1)-set K on 2r+1 positions, its total prefix-walk height is
-3. Let kappa(K) be its first minimum zero and set J(K)=K+kappa(K).
When the child state is K11, the two final ones end at heights -2,-1;
they cannot precede the old global minimum. Therefore child Phi inserts
kappa(K) at an old position.

The map J is injective. If K first attains its minimum m<=-3 at position j,
flipping that zero raises every subsequent height by2. The minimum in J(K)
is m+1, last attained immediately before j. Thus K is recovered from J(K)
by deleting the up-step immediately after its last minimum. In particular
every J(K) has minimum at most -2. Conversely every old rank-r word with
minimum at most -2 arises this way; this exact image statement is already
proved in Section9 of the cited excursion note.

## 5. Delete the old root to finish all excursions disjointly

At X3=K+a+b the old root u has been present in exactly X1,X2,X3. It has
age3 and may now be deleted. Insert the forced old kappa(K) and set

    K'=J(K)-u,
    X4=K'+a+b,
    T=J(K'),
    X5=T+a.                                          (5.1)

The final step inserts the forced old kappa(K') and deletes b. The latter
has been present in X2,X3,X4, so that deletion is legal at age3. These
are the one internal11 step and the exit required for q=3.

All first K contain u. Since J(K) also contains u and J is injective,
K->K'=J(K)-u is injective. Every K' omits u, so the whole first11 and
second11 banks are disjoint. The output map K'->T=J(K') is injective.
Moreover T has old prefix minimum at most -2, whereas every initial
root-aligned L=0D has old minimum exactly -1. Hence the entire output10
bank avoids the entire initial10 bank, without protecting u to the end.

In fact kappa(K') cannot be u. Otherwise J(K')=K'+u=J(K), and injectivity
of J would imply K'=K, contradicting their opposite membership of u.
Thus T also omits u.

Together with the 00 and01 injections, sector labels now prove that ALL
six states in ALL paths are distinct:

    L+a -> U -> P+b -> K+a+b -> K'+a+b -> T+a.         (5.2)

These are pairwise vertex-disjoint five-transition paths in the child
middle-level graph. Because child Phi is a perfect matching, their five
intervening upper owners are also globally distinct. Explicitly they are

    U+a,  U+b,  P+a+b,  J(K)+a+b,  T+a+b.             (5.3)

Choosing a different Hall facet changes neither the first three lower
states nor the first three upper owners of its port. This local inventory
observation is not a claim about later upper targets or intervals.

## 6. Residence, boundary service and remaining global gates

The old root u is present in precisely X1,X2,X3, and b in precisely
X2,X3,X4. Their completed positive lower runs have length exactly3.
In (5.3), u occurs in the first four owners and not the fifth; b occurs
in the last four and not the first. Thus both have the controlled
four-owner positive runs relevant to a q=3 middle-window compiler.
The upper owner immediately before X0 in the lifted parent history omits
u: if it contained u, its old part would be L+u=Phi(L), repeating the
current matching owner at a distinct predecessor. This supplies the left
boundary of the asserted u-run as well as the displayed right boundary.
A Phi-directed continuation cannot immediately reinsert b after X5:
doing so would reuse its preceding upper owner, contradicting injectivity
of the Phi matching. The new a is present in X3,X4,X5 and has output age3.
All other coordinate runs closed by the path are the already justified
deletions of a,d,e. No minimum-run assertion depends on a numerical test.

The output age vector remains part of the interface. In particular,
kappa(K) and kappa(K') have output ages2 and1; a prescribed next old step
may be incompatible with those ages. Although outputs avoid every initial
root-aligned port, they can be other 10 states already used by an untouched
parent copy. No allocation or rethreading of that remaining inventory is
proved here. Nor do these paths alone cover the child middle layers,
preserve an arbitrary named target-prefix deck, prove all-rank OR coverage,
or provide a safe exact-budget linear opening.

For the actual19 parent, r=9 satisfies (3.1). The theorem therefore proves
that the 375 first11 collision pairs in the prescribed-second-deletion
diagnostic can be removed simultaneously and the repaired entrances
extended as in (5.2). It supplies an existence proof for this disjoint
path bank, not a materialized matching or a verified dimension21 word.

## 7. Review and execution status

The first11 Hall/age argument and the full five-step closure were
independently passed by the frontier agent and recorded in
[its audit](Q3_FIRST11_COLLISION_REPAIR_BY_SMALL_SHADOW_HALL_INDEPENDENT_AUDIT_20260909.md).
The root and induction agents independently checked the full root-deletion
closure. These are
internal mathematical reviews, not external certification.

No mathematical execution, matching run, alternate-port search, or new
literal construction was performed for this theorem. The earlier fixed
diagnostic and its 375 collisions remain unchanged and accurately scoped.
