# Two macrocell repairs: flexible shores and an incomparable-pair limitation

2026-09-08. Analytic deduction only; no solver or numerical computation. The repair budget is the 2.0448919776... s^9 principal allowance in BINARY10_PARTIAL_MACRO_COVER_REPAIR_LEDGER_20260908.md. No new 42-row bank is constructed here.

Audit status: full root audit PASS. The root checked the actual support-split charge, all displayed constants, absorption chain counts, and the incomparable-cell restriction proof, with the stated axis-support and centered-versus-noncentered scope limits.

Independent appendix-a audit also passes. Its designated-product guard is included explicitly in Section 2 below.

## 1. Repair shores need not have five coordinates each

The original binary-ten rows have five/five shores, but an added repair may use any disjoint support split. Let two missing patterns A<B be comparable, and let h be the number of changing coordinates, with 1<=h<=9. Put ALL h changing coordinates on the left shore and the 10-h unchanged coordinates on the right.

The left target poset is the ordinal sum of two [s]^h microboxes. Take an actual product SCD of [s]^h and join each chain to its corresponding copy in the upper box. This gives an actual ascending-chain partition with membership 2s^h and chain count w_h(s), where w_d(s) is the width of [s]^d. Every lower-box point precedes every upper-box point in the changing coordinates, so these joins are literal set inclusions.

The right shore is the common [s]^(10-h) microbox, with membership s^(10-h) and an actual SCD of w_(10-h)(s) chains. Pair every left chain with every right chain. The EXACT principal charge is

    2s^h w_(10-h)(s) + s^(10-h) w_h(s).                 (1)

Write rho_d=f_d(d/2), where f_d is the density of a sum of d Uniform[0,1] variables. The finite central-rank formula gives

    w_d(s)=rho_d s^(d-1)+O_d(s^(d-2)),

with the exact convention w_1(s)=1, rho_1=1. Hence (1) has coefficient

    R_h=rho_h+2rho_(10-h).                              (2)

The relevant elementary central coefficients are

    rho_2=1, rho_3=3/4, rho_4=2/3, rho_5=115/192,
    rho_6=11/20, rho_7=5887/11520, rho_8=151/315.

Also rho_9<=rho_8: convolution with a probability density cannot increase the maximum density, and each f_d is symmetric unimodal. These constants follow directly from

    f_d(x)=(1/(d-1)!) sum_j (-1)^j C(d,j)(x-j)_+^(d-1).

Consequently the following fully constructive bounds hold:

| Hamming distance h | Principal coefficient R_h |
| --- | --- |
| 1 | 1+2rho_9 <= 617/315 < 2 |
| 2 | 617/315 < 2 |
| 3 | 10207/5760 < 2 |
| 4 | 53/30 < 2 |
| 5 | 115/64 < 2 |
| 6 | 113/60 < 2 |
| 7 | 23167/11520 < 2.04 |

All seven bounds are below the available repair budget. In particular, the Hamming-distance-one case does admit a useful repair: its union is exactly [2s] times [s]^9, and isolating the [2s] chain gives charge s^9+2s w_9(s). The earlier five/five repair bound for that case was unnecessarily restrictive.

The incidence and compiler ledger is complete. The left/right chain families form a complete bipartite bridge graph, so its Euler construction pays the displayed membership/count expression with all multiplicities. It has one nontrivial connected component. Bridge endpoint corrections are lower degree. Absorbing the eleventh accumulator of length r multiplies the principal upper charge by at most r, because each absorbed left chain contributes membership rL and at most r product-SCD chains. That factor cancels in the actual-volume normalization, exactly as in the existing transfer. Complements are supplied by the reverse bridge arcs. The repair does not assume disjointness from the 42 original rows.

Formula (2) itself does not give a below-budget result at h=8 or 9. At h=10 there is no unchanged-coordinate shore and this construction is not a principal-order repair.

## 2. An incomparable pair cannot freely share new rectangle charge

Let A and B be two incomparable binary patterns, and let Q_A,Q_B be their [s]^10 microboxes. Consider any monotone rectangle C times D, where C and D are ascending set chains on complementary groups of the ten input axes: each input chain's entire physical support is assigned to one shore. The rectangle may contain additional, already-covered macroboxes. This is the support convention of the product-SCD and grouped-macrocell compilers under discussion; splitting one input chain's physical support between the two shores is outside this argument.

The bank's designated Cartesian products themselves must cover the two microboxes. Full complements are the paired-family bonus supplied elsewhere by the bridge compiler, as in the pivot-sign folding of A.5 and A.7. This section does not optimize arbitrary coverage obtained by mixing each product with its full complement.

For a macrocell Q_X, restrict each shore chain to the members lying in the corresponding projected microbox, obtaining subchains C_X,D_X. For product-index chains these are consecutive intervals, but consecutiveness is not needed; arbitrary off-grid intermediate members may simply be removed. Since the macrocell factors across this support split,

    (C times D) intersect Q_X = C_X times D_X.

Suppose the rectangle meets both Q_A and Q_B. The two projected patterns on each shore must be comparable, because they both occur on one ascending chain. Neither pair of projections can be equal: equality on one shore would put the entire incomparability on the other shore, where a single chain cannot meet both projections. Finally, the two shore comparisons must have opposite directions, since A and B are incomparable globally.

It follows that C_A and C_B are disjoint subchains, and so are D_A and D_B. Therefore

    (|C_A|+|D_A|)+(|C_B|+|D_B|) <= |C|+|D|.          (3)

If the rectangle meets only one box, its restricted charge is likewise at most its original charge. Split every rectangle in an arbitrary paired-rectangle repair bank into these cell intersections, retaining multiplicities. The result consists of two separate monotone-rectangle covers of Q_A and Q_B, at no larger total principal charge.

Thus, within the principal ledger sum(|C|+|D|) for axis-support rectangles, the optimal repair cost of two incomparable microboxes equals twice the infimum of the corresponding arbitrary one-microbox axis-support monotone-rectangle covering cost. The upper direction uses two separate copies; the lower direction is (3) and the fact that the two microboxes are order-isomorphic.

In particular, a new-rectangle repair of an incomparable pair below 2.0448919776... s^9 would imply an individual microbox cover below 1.0224459888... s^9. Shared bridge vertices in the ordinary Euler ledger do not evade this statement: every incident rectangle arc still pays that bridge with its multiplicity.

## 3. Scope of the obstruction

The individual covers produced by restriction in Section 2 need not be centered product-SCD refinements. Therefore the 23771/22680 centered lower bound in TEN_EQUAL_CHAIN_CENTERED_RECTANGLE_REPAIR_BARRIER_20260908.md cannot automatically be applied to them. That would be an invalid inference from a centered obstruction to arbitrary monotone covers.

The argument does show that merely joining chains across the two incomparable holes cannot create a free saving in this paired-rectangle principal ledger. Progress would require a genuinely cheaper individual microbox cover, or leading-order sharing with the EXISTING 42-row bank, or a compiler that escapes the stated rectangle-charge ledger. In particular it does not establish a general below-budget repair for the equal-rank incomparable orbit arising in the frozen involution models.

These results strengthen the finite antecedent for comparable holes through distance seven. They do not supply an all-pairs repair theorem or an actual 42-row near-cover.
