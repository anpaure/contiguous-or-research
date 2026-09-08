# The user's native 35-cycle, exact 280-cycle graft, and rooted 291-word

Date: 2026-09-08.

Status: all supplied fixed-witness claims below independently verified by one bounded exact h100 run. The literal words and target-by-target interval witnesses are materialized. The construction and rooting prefix are user supplied; this note audits them and derives their precise finite consequences.

The three resulting linear words are optimal for their respective named target families. None covers the entire 17-cube, and no value of nu(17) or proof of nu(k)=B(k) follows. The separately mentioned 24,313-position static inventory was not supplied and was not verified.

## 1. Supplied period and coordinate convention

Coordinate x is bit x-1 in an integer mask. The exact base period is

    287,768,4106,16404,5648,3590,2308,4867,20997,8193,
    65538,21024,4385,68128,5152,416,2704,20880,86272,
    4610,129,84098,77952,18436,72320,35328,22658,8320,
    6912,2954,1672,554,440,122,318.

Let C={1,2,3,4,5}, u=6, v=7, w=8, a_i=9+i for 0<=i<8, and Z={17}. Let rho cycle coordinates 9 through 16 and fix the others. The eight input words are W_i=rho^i W.

The verifier computes the full cyclic recency state at every endpoint, rather than assuming an initialization. Every coordinate occurs within a period, so one full traversal determines the last-occurrence state independently of earlier history.

After positions 0 and 1, respectively, the states are exactly

    P_i=(C union {a_i} | {u} | {v} | {w} |
          {a_(i+1)} | ... | {a_(i-1)} | Z),
    Q_i=({a_i,a_(i+1)} | C | {u} | {v} | {w} |
          {a_(i+2)} | ... | {a_(i-1)} | Z),

with arm subscripts modulo eight. Each W_i has 251 distinct cyclic interval targets, including 105 targets below rank nine and 35 targets of rank nine. Its 35 cyclic triple unions are distinct rank-eight sets, and its 35 four-window unions are distinct rank-nine sets.

## 2. The graft is an actual eight-to-one cycle construction

The recency update by X prepends X and removes its coordinates from the old blocks, deleting empty blocks. Consequently

    T_({a_(i-1),a_i})(P_i)=Q_(i-1).

The arm a_i disappears from the first source block, leaving C. The arm a_(i-1) disappears from the last arm singleton. Every remaining block is in exactly the destination order. These are actual legal recency transitions.

Replace the eight old edges P_i to Q_i by P_i to Q_(i-1). Opening each old edge gives a path from Q_i around its original component through P_i. The new assignments link these eight paths cyclically in decreasing component order, producing one cycle with all 280 state occurrences exactly once.

The retained literal orientation is the concatenation, for i=7,6,...,0, of

    W_i[1],W_i[2],...,W_i[34],W_i[0].

It starts just after P_0 and returns to P_0. The verifier checks every resulting cyclic recency state against its named original state occurrence. In particular the complete state target inventory is preserved. A separate exhaustive cyclic interval scan confirms exact target-set equality, not merely equality of cardinalities.

The joined period has exactly 1,811 targets, including 807 below rank nine and 280 of rank nine. Its 280 cyclic rank-eight triple targets and 280 cyclic rank-nine four-window targets are all distinct. There are no lost or added cyclic interval targets relative to the union of the eight original target families.

The joint target counts by rank are

| Rank | Count | Rank | Count |
|---:|---:|---:|---:|
| 1 | 0 | 10 | 200 |
| 2 | 26 | 11 | 177 |
| 3 | 56 | 12 | 138 |
| 4 | 84 | 13 | 107 |
| 5 | 89 | 14 | 60 |
| 6 | 144 | 15 | 30 |
| 7 | 128 | 16 | 11 |
| 8 | 280 | 17 | 1 |
| 9 | 280 | | |

## 3. Explicit optimal linear openings for the named families

Use zero-based start indices. Rotate the base period to start at index 14 and append its first three letters. The resulting 38-letter linear word realizes exactly the same 251 targets as the base cycle.

Rotate the stored joined period to start at index 13 and append its first three letters. The resulting 283-letter linear word realizes exactly the same 1,811 targets as the eight-cycle union. Both requested starts succeeded on the first test; no alternative cut selection was needed. The edge immediately before these starts has index 13 and 12, respectively, which removes any ambiguity between a start index and a preceding cut-edge index.

Here is the lower bound for these particular target families. If a word covers M specified distinct rank-nine targets, select one witness for each. They form an interval antichain. For a word of length M+t their ordered starts and deadlines satisfy

    ell_i=i+alpha_i, r_i=i+beta_i,
    0<=alpha_i<=beta_i<=t.

Every interval of length at least t+1 contains a selected rank-nine witness. Thus every required lower-rank target needs an interval of length at most t. If Lambda distinct required targets have rank below nine, then

    Lambda <= tM+t(t+1)/2.

This argument only uses the M selected targets; it does not assume that the family is the full rank-nine layer.

For the base family, (M,Lambda)=(35,105). Delay two has only 73 short slots, so every realizing word has length at least 38. For the joined family, (M,Lambda)=(280,807); delay two has only 563 short slots, so every realizing word has length at least 283. The two literal openings attain these lower bounds.

## 4. The fully initialized 291-letter word

The user supplied the permutation

    pi=(17,16,15,14,13,12,11,10,8,7,6,1,2,3,4,9,5).

Start with its first three coordinates as singleton letters. Then, for one-based j=4,...,12, append the six-set {pi_j,...,pi_(j+5)}. The resulting 12 letters are

    65536,32768,16384,16000,7872,3808,
    1761,739,231,111,303,287.

Starting from the empty recency state, this prefix ends exactly at P_0. Continue through components 7,6,...,1, each from its position 1 through position 34 and then position 0. Finally traverse component 0 from position 1 through 34. In the stored joined orientation, this is simply

    rooted291 = rooting_prefix12 + joined280[:-1].

All 280 original state occurrences are realized: P_0 is already the prefix endpoint and the other 279 occur in the appended traversal. The complete original 1,811-target family is retained.

The resulting linear word has 1,876 distinct interval targets. Its 288 four-windows are distinct rank-nine sets. Of its 289 triple windows, the first is the rank-three union {17,16,15}, and all other 288 are distinct rank-eight sets. No old middle owner or triple facet is dropped.

The rooted word has 836 distinct targets below rank nine and 288 at rank nine. Delay two supplies only 579 short slots, whereas delay three supplies 870. Therefore this word too attains its target-family endpoint lower bound:

    minimum length for its complete 1,876-target family = 291.

This last optimality consequence is an independent deduction from the verified target census; it is not a full-cube equality.

| Literal word | Distinct targets | Required rank-nine targets | Required targets below nine | Proven minimum length |
|---|---:|---:|---:|---:|
| Base opening | 251 | 35 | 105 | 38 |
| Joined opening | 1,811 | 280 | 807 | 283 |
| Rooted construction | 1,876 | 288 | 836 | 291 |

## 5. The exact rank-potential identity

For a recency state P let b_s(P) count its prefix unions of size below s. Start from the empty state, so b_s(P_0)=0. At each new letter, every new prefix union is either that letter or its union with an old prefix. Old prefixes of size at least s cannot create a below-s union. Hence

    b_s(P_j)-b_s(P_(j-1))<=1.

If the increase is one, all old below-s prefixes must still contribute distinct below-s unions, and the new letter contributes another. Any rank-s union at that step must consequently arise from an old prefix already of rank s. Since union cannot shrink it, the target equals that old prefix and is not a new rank-s target.

Let D_s be the number of distinct rank-s targets in the word, let L_s be the sum of all negative changes in b_s in absolute value, and let E_s count steps introducing no new rank-s target at which b_s does not increase. At most one rank-s target can occur in any one state's strictly increasing prefix menu. Thus D_s also counts the steps introducing a new rank-s target.

Write U_s for the number of unit increases of b_s. The preceding argument partitions all non-new-target steps into those U_s increases and the E_s other steps. Therefore

    N-D_s=U_s+E_s,
    b_s(P_N)=U_s-L_s,

and elimination proves the exact identity

    N-D_s=L_s+b_s(P_N)+E_s.

The verifier checks this identity and its stepwise hypotheses for every rank 1 through 17 on the rooted word. At rank nine it obtains

    N=291, D_9=288, L_9=0, b_9(P_N)=3, E_9=0.

At rank eight, for comparison, it obtains D_8=288, L_8=1, b_8(P_N)=2, E_8=0, again giving 291-288=3. The complete rank-nine step ledger is retained.

## 6. Exact artifacts and verification scope

All artifacts are in

    scratch/native35_user_graft_20260908/

The directly usable words are

    native35_base_cycle.word
    native280_joined_cycle.word
    native38_base_optimal_linear.word
    native283_joint_optimal_linear.word
    native12_rooting_prefix.word
    native291_rooted_word.word

All eight rotated input periods are also included. The principal certificate is `native35_graft_certificate.json`; `native35_graft_targets_and_witnesses.json` gives a literal start, length, and wrap flag for every target in the base, joined cycle, both openings, and rooted word. `native291_rank9_potential_steps.json` records every rank-nine potential step.

The standalone verifier is retained both as

    scratch/verify_user_native35_recency_graft_20260908.py
    scratch/native35_user_graft_20260908/verify.py.

The single mathematical run used

    /home/amodo/exact-b-native35-user-graft-20260908/verify.py

on h100, with limits of 90 CPU seconds, 110 wall seconds, and 1 GiB address space. Its status was

    PASS fixed user native35 / graft280 / rooted291 verification.

The enumeration is exhaustive for these fixed words. It is not a random search, a construction of the unavailable static inventory, or a verification of a 24,313-letter universal word. The current 1513-owner PBBS bank was not changed.
