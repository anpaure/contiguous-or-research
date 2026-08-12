# Independent audit of uniform-block chainization and the K19 obstruction

**Date:** 2026-08-02  
**Audited theorem:**  
MATH_THEOREM_ALLK_UNIFORM_BLOCK_CHAINIZATION_AND_K19_NORMALITY_OBSTRUCTION_20260802.md

**Verdict:** PASS within the theorem's stated static scope.

The coupling, LYM/Dilworth consequence, K19 obstruction, one-extra-level
repair, and consecutive-packing asymptotic obstruction replay. No
all-\(k\) \(d+O(1)\) normal block system, literal source, or \(B+O(1)\)
theorem is certified. The K19 partial-rank split was subsequently proved
by the fixed-triple orbit construction; it is not a claim of this older
audit.

## 1. Symbolic coupling replay

For separated full-rank blocks \(I<J\), the proposed edge mass is

\[
 \mu(S,T)=\mathbf 1_{S\subset T}
 { {k\choose |S|}\over N_I N_J{|T|\choose |S|}}.       \tag{1.1}
\]

Fix \(S\) of rank \(s\). Summing first over rank \(t\in J\) gives

\[
 \sum_{\substack{T\supset S\\|T|=t}}\mu(S,T)
 ={ {k-s\choose t-s}{k\choose s}\over
    N_I N_J{t\choose s}}
 ={ {k\choose t}\over N_I N_J}.                        \tag{1.2}
\]

Summing (1.2) over \(t\in J\) gives \(1/N_I\). Fixing \(T\) and summing
over \(s\in I\) gives

\[
 \sum_{s\in I}{ {t\choose s}{k\choose s}\over
 N_I N_J{t\choose s}}={1\over N_J}.                    \tag{1.3}
\]

Thus both marginals are exactly uniform. The common-permutation quantile
construction independently confirms the interlaced extension: stochastic
order of the rank laws is necessary and sufficient.

A sampled chain meets an antichain at most once, so

\[
 \sum_i {|A\cap P_i|\over N_i}\le1.                   \tag{1.4}
\]

Taking \(M=\max_iN_i\) gives \(|A|\le M\), and a largest block gives
equality. Appending the \(W\) rank-\(r\) owners therefore forces one
owner in each of the \(W\) Dilworth chains. The owner-attachment
quantifier is sound in both parities.

## 2. Normalized Hall replay

Scale a uniform coupling from \(P\) to \(Q\) so each source supplies one
unit and every target has capacity \(|P|/|Q|\). The max-flow cut for
\(F\subseteq P\) is exactly

\[
 |F|\le {|P|\over|Q|}|N_Q(F)|.                       \tag{2.1}
\]

Total source supply equals total target capacity, so a saturating flow uses
every target capacity and gives both uniform marginals. Hence normalized
Hall is necessary and sufficient, not merely necessary.

Cardinality and non-isolation do not replace it. On \([6]\), let \(P\)
be all six singletons and

\[
 Q=\{12,34,35,36,45,46\}.
\]

Every vertex is incident and \(|P|=|Q|=6\), but the two sources
\(\{1\},\{2\}\) have the single neighbor \(12\). This negative control
confirms only that cardinality and non-isolation could not have proved the
K19 clause. The later fixed-triple orbit-flow certificate proves the needed
normalized Hall inequalities.

## 3. Exact K19 obstruction replay

The exact parameters are

\[
 W=92\,378,\qquad \Lambda=262\,143,\qquad d=3,\qquad h=0.
\]

Rank nine consumes one entire block. For a consecutive cut of ranks one
through eight:

\[
 \sum_{s=1}^7{19\choose s}=94\,183>W,\qquad
 {19\choose7}+{19\choose8}=125\,970>W.                \tag{3.1}
\]

Thus every cut fails. Minimizing the sum of the two capacity excesses over
all seven cuts gives exactly \(1\,805\).

The stronger interlaced proof also replays. Both non-top block masses are
at least \(77\,387\). Capacity separates ranks seven and eight and forces
ranks six and seven into the block \(A\) preceding the rank-eight block
\(B\). If \(t\) is the least rank at most five placed in \(B\),
stochastic order requires

\[
 { {19\choose t}\over\sum_{s<t}{19\choose s}}
 \le {|B|\over|A|}
 \le {92\,378\over77\,387}<1.194.                     \tag{3.2}
\]

For \(t=1,\ldots,5\), the left side is

\[
 \infty,\quad 9,\quad {969\over190},\quad
 {3876\over1159},\quad {11628\over5035},
\]

and its minimum exceeds \(2.30\). This independently proves failure of
every whole-rank uniform coupling. It does not address arbitrary
uncompressed depth-three chain partitions.

The four-block repair has exact loads

\[
 43\,795,\quad50\,388,\quad75\,582,\quad92\,378,
\]

all at most \(W\). The same coupling proof therefore gives a static
depth-four owner factor.

For the proposed depth-three partial split, the two capacity inequalities
independently give

\[
 50\,388+75\,582-W=33\,592
 \le |X|\le
 W-43\,795=48\,583.                                  \tag{3.3}
\]

No normalized-Hall claim for any such \(X\) was found or assumed.

## 4. Consecutive-packing audit

The exact program

    scratch/audit_allk_uniform_block_chainization_20260802.py

implements both:

1. longest-prefix greedy packing; and
2. an independent suffix dynamic programme over every possible next cut.

The two counts agree for every \(3\le k\le121\). The first odd
post-K17 failure at deadline depth is K19. The first odd failure of the
\(d+1\) consecutive budget is

\[
                         k=121,\qquad d=7,\qquad g=9. \tag{4.1}
\]

The program also enumerates all eight capacity-feasible ordered K14
whole-rank pairs and all 48 capacity-feasible ordered K19 pairs; both have
zero stochastically ordered pairs. Its exact output is

    PASS exact uniform-block chainization arithmetic
    first_post_K17_consecutive_depth_failure=19
    K19_W=92378 d=3 h=0 min_unsplit_casualties=1805
    K19_capacity_feasible_ordered_whole_rank_pairs=48 normal_pairs=0
    K19_rank7_split_interval=[33592,48583]
    K19_four_block_loads=43795,50388,75582,92378
    first_odd_consecutive_Bplus1_failure=121 d=7 blocks=9
    growth_probes=[(121, 7, 9, 8), (501, 15, 17, 16),
                   (1001, 20, 24, 24), (2001, 29, 34, 33)]

The asymptotic proof is not inferred from those probes. For
\(k=2m+1\) and \(j=x\sqrt m+O(1)\),

\[
 {{2m+1\choose m-j}\over{2m+1\choose m}}
 =\prod_{\ell=0}^{j-1}{m-\ell\over m+2+\ell}
 =e^{-x^2+o(1)}.                                      \tag{4.2}
\]

A fixed \(\Theta(\sqrt m)\) band has every rank mass in
\((W/2,3W/4)\). All but at most two of those ranks occupy singleton
consecutive blocks and waste at least \(W/4\) each. Since
\(d=\Lambda/W+O(1)\), this proves
\(g-d=\Omega(\sqrt k)\).

## 5. Nonconsecutive control

The K31 interlaced blocks

\[
 \{1,\ldots,10,12\},\quad\{11,13\},\quad\{14\},\quad\{15\}
\]

have the four audited masses

\[
 217\,093\,713,\quad290\,925\,390,\quad
 265\,182\,525,\quad300\,540\,195=W.
\]

The sole nonautomatic stochastic threshold is

\[
 {141\,120\,525\over217\,093\,713}
 <
 {206\,253\,075\over290\,925\,390}.                   \tag{5.1}
\]

Thus K31 really does repair a five-block consecutive profile with four
interlaced blocks. This control prevents the consecutive asymptotic
obstruction from being overstated as a no-go for all generalized block
systems.

## 6. Fail-closed scope

The audit certifies only a static chain factor. The following remain
**UNPROVED**:

* RBS_C for any absolute \(C\);
* a common literal overlap/Euler serialization;
* endpoint aperture and global address/history consistency;
* residence, upper witnesses, common-cap and compiler closure;
* a cross-depth regenerative relay on the same frozen host; and
* any \(\nu(k)\le B(k)+O(1)\) conclusion.

This audit therefore does not import either of the uncorrected
Catalan-pivot reductions flagged in the current handoff.

The formerly open K19 rank-seven split is closed in
`MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md`;
the explicit auxiliary three-layer poset there is needed before inferring
chain length three from Dilworth.
