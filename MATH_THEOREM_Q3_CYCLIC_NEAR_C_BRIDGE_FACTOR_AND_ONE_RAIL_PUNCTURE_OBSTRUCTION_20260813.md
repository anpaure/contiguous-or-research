# A cyclic q=3 near-C bridge factor and the exact one-rail puncture obstruction

**Date:** 2026-08-13

**Status:** unconditional positive factor theorem on eleven reduced labels,
plus an exact obstruction to the smallest local one-owner refactorization.
The factor uses actual period-10 closed rails with distance-one near-C
cores and covers every named owner exactly once. It does not yet give the
common reserve obtained at q=2.

## 1. Reduced owner model

Put q=3 and fix a (c-1)-set C0. On the reduced label group Z_11, the
owner [abcd] denotes C0 union {a,b,c,d}. For r in Z_11 use the core
K_r=C0 union {r}. After designating C=K_0, every K_r with r nonzero is
the distance-one bridge core C-0+r.

For a cyclic word sigma=(v_0,...,v_9) listing Z_11 minus {r}, let
Q(r;sigma) be the period-10 rail with core K_r. Its complete owner deck is

    D Q(r;sigma) = {[r v_i v_(i+1) v_(i+2)] : i in Z_10}.       (1.1)

The period is legal because 10 >= 2(q+1)=8.

## 2. Three base cycles

Use the following three cycles on Z_11 minus {0}:

    sigma_1 = (1,2,3,4,6,9,5,10,7,8),
    sigma_2 = (1,5,9,2,4,8,7,6,3,10),
    sigma_3 = (1,6,9,3,8,10,2,4,5,7).                         (2.1)

Their complete reduced decks at centre zero are

    D Q(0;sigma_1) = {
      0123,0234,0346,0469,0569,059(10),057(10),078(10),0178,0128},

    D Q(0;sigma_2) = {
      0159,0259,0249,0248,0478,0678,0367,036(10),013(10),015(10)},

    D Q(0;sigma_3) = {
      0169,0369,0389,038(10),028(10),024(10),0245,0457,0157,0167}.
                                                                    (2.2)

Parentheses only distinguish the two-digit label 10. For r in Z_11,
let sigma_j+r mean coordinatewise addition modulo 11.

### Theorem 2.1 (cyclic q=3 bridge factor)

The collection

    F_3 = {Q(r;sigma_j+r) : r in Z_11, j in {1,2,3}}             (2.3)

is a simple closed-rail factor of all reduced named owners:

    sum_(Q in F_3) f(Q) = sum_(A in binom(Z_11,4)) e_(C0 union A). (2.4)

Thus 33 nonnegative period-10 rails cover all

    33 * 10 = binom(11,4) = 330                                  (2.5)

owners exactly once.

#### Proof

Every four-subset of Z_11 has a free translation orbit: since 11 is
prime, a nonempty proper subset has no nonzero period. There are

    binom(11,4)/11 = 30                                          (2.6)

translation orbits.

Each of the 30 owners in (2.2) lies in a different translation orbit.
This is an exact finite check: translate an owner so that each of its
four labels is zero in turn, sort the resulting four residues, and take
the lexicographically least tuple. The 30 resulting canonical tuples are
distinct. Hence (2.2) gives one representative from every orbit.
Developing by all 11 translations gives every four-subset exactly once.
Equation (2.4) follows from the deck formula (1.1). Every coefficient is
one, so the factor is nonnegative and simple. QED.

This is a structural improvement over the scalar point-signature
calculation: it assigns an actual bridge core and an actual cyclic
period-10 order to every one of the 330 named owners.

## 3. Exact obstruction to deleting one owner from one factor rail

Designate H=[0123]. By simplicity of the factor, H occurs only in
Q(0;sigma_1). Let

    P = D Q(0;sigma_1) minus {H}.                                (3.1)

Thus

    P = {0234,0346,0469,0569,059(10),057(10),078(10),0178,0128}. (3.2)

### Theorem 3.1 (one-rail puncture is not a rail union)

There is no legal q=3 rail of period 8, 9, or 10 whose complete owner deck
is contained in P. Consequently P is not a nonnegative union of legal
closed rails.

#### Proof

Every legal rail has period at least 2(q+1)=8. Since |P|=9, any rail
contained in P would have period 8 or 9; period 10 is included in the
explicit audit as a harmless superset check.

For each possible centre r in Z_11, retain the triples A-r for owners
A in P containing r. A candidate rail is then exactly a simple cyclic
word of length N in {8,9,10}, avoiding r, all of whose cyclic
three-windows belong to this retained triple family.

The exhaustive finite check enumerates the eleven possible centres, all
N-subsets of the ten possible toggle labels, and all cyclic orders rooted
at the least support label and quotiented by reversal. It checks every
cyclic three-window. No order survives. The accompanying verifier
implements precisely this enumeration. Hence no one rail is contained in
P. Since a nonempty union of legal rails would already contain at least
eight owners, while P has only nine, it could contain only one rail; that
possibility has just been excluded. QED.

Thus the natural all-owner cyclic factor is not itself a one-owner
absorber after puncturing the unique rail through H. At least one of the
following catalogue expansions is necessary:

1. include additional complete rails before deleting H;
2. use a compound refactorization involving owners outside the punctured
   deck; or
3. introduce additional legal periods/supports in a larger reduced ground
   set.

The obstruction is stronger than a period-sum congruence: it checks every
named owner and every cyclic order in the punctured support.

### Proposition 3.2 (the first period-balanced atom is also absent)

Restrict the positive shore to five rails of the cyclic factor (2.3), one
of them the unique rail through H. If the negative shore is required to
use five period-8 rails and one period-9 rail, then no positive one-owner
trade exists.

#### Proof

There are binom(32,4)=35,960 choices of the other four positive factor
rails. The exact point/core/unused ledger leaves only 135 choices. For
each survivor, enumerate every period-8 and period-9 rail whose complete
deck lies in the 49-owner punctured positive union, then solve the exact
cover requiring five of the former and one of the latter. No cover
exists.

This computation ran on the H100 host `arboghast`, with eight CPU workers,
using

`scratch/search_q3_five10_to_five8_one9_bridge_20260813.py`.

The frozen summary was

    host=arboghast workers=8 scope_centres=11
    choices=35960 role_feasible=135
    NONE checked=135 elapsed=0.11

The script reconstructs every deck from its named centre and cyclic word,
checks multiplicity one in the 33-rail factor, and performs an exact
recursive owner cover. Thus the result is a finite exhaustive obstruction,
not a failed heuristic search. QED.

The period equation 5*10-1=5*8+1*9 makes this the direct q=3 analogue of
the short q=2 atom. Proposition 3.2 shows that the q=3 reserve must use a
larger positive shore, a different feasible period profile, or a larger
reduced ground set.

## 4. Relation to the q=2 atom and the all-q pattern

The q=2 common reserve is a local reorientation trade: one simple
3-uniform owner hypergraph has two assignments of a core centre, and each
centre link is a union of legal cycles on the two shores. It is not a
Boolean cube or cross-polytope.

Theorem 2.1 exhibits the corresponding q=3 ambient object: a cyclic
decomposition of the complete 4-uniform owner hypergraph into centred
tight cycles. The number of translation orbits of (q+1)-subsets of
Z_(2q+1) is

    binom(2q+1,q+1)/(2q+1) = binom(2q,q)/(q+1),                  (4.1)

the Catalan number C_q. For q=2 this gives two orbit types; for q=3 it
gives five. This Catalan orbit count, rather than a 2^q-vertex cube count,
is the exact cyclic combinatorial pattern behind the small factors.

Equation (4.1) alone does not prove that the orbit representatives can be
grouped into legal rail decks for every q. Nor does the complete q=3
factor imply a one-owner trade. Theorem 3.1 identifies the first positive
gate sharply: a q=3 common reserve must use a compound neighbourhood
beyond the single factor rail through H.

## 5. Verification and scope

The dependency-free verifier

`scratch/verify_q3_cyclic_bridge_factor_and_one_rail_obstruction_20260813.py`

checks:

1. all 33 core/cycle assignments in (2.3);
2. all 330 named owners and multiplicity one;
3. the unique occurrence of H;
4. the complete nine-owner punctured list (3.2); and
5. every legal period-8/9/10 rail potentially contained in that list.

The H100 search script for Proposition 3.2 is

`scratch/search_q3_five10_to_five8_one9_bridge_20260813.py`.

The H100 SHA-256 digests are

    0e0f241dff20c02450dae1491ba526388a80968630ba33fd3392b493e2ae46db
      verify_q3_cyclic_bridge_factor_and_one_rail_obstruction_20260813.py

    0310937360c04ba251ae63df2ae5165f5c43817874eb0870be191bb3b0fbf13d
      search_q3_five10_to_five8_one9_bridge_20260813.py

    01e5fa21bc3468cbf4d3c34b3488aa9728c13daec1a9238d70d609e9c0b8aab2
      q3_atom_full.out

    8354aeceb0ed4db016bb4250a1d7b973fc91d01de115d4a7fd2e7329692e9bc7
      verify_q3_factor.out

The result is a genuine nonnegative/simple q=3 bridge factor and a
genuine positive obstruction to its smallest puncture. It does not claim
a q=3 common reserve, an all-q factor theorem, a separating character for
the full mixed-core catalogue, or that any signed lattice identity is a
positive decomposition.
