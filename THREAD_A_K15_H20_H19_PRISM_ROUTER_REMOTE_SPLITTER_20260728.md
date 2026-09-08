# Thread A: the H20 prism router and the remote H19 ladder splitter

Date: 2026-07-28

## 1. Status

This note proves an exact statement about the frozen resident/all-upper
`k=15` carrier.  It does **not** prove the exact contiguous-OR formula.

Let `P0`, `P1`, and `P2` be the three middle paths in

```text
scratch/k15_segment_braid_hall20_zero6.json
scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json.
```

Then

\[
 P_0\xrightarrow{\operatorname{RF}(180,2764,4210)}P_1
 \xrightarrow{\operatorname{FR}(123,722,4710)}P_2.       \tag{1.1}
\]

The matching ranks, Hall deficiencies, and canonical DM shores are

\[
\begin{array}{c|ccc}
 &P_0&P_1&P_2\\ \hline
\nu&16363&16363&16364\\
\operatorname{def}&20&20&19\\
(|D_L|,|D_R|)&(677,657)&(677,657)&(516,497).
\end{array}                                                \tag{1.2}
\]

All three paths are permutations of the 6435 rank-eight masks, are Johnson
paths, and satisfy depth-three residence.  Their lower-hole vectors are all

\[
(4,18,11,1,0,0,0),                                      \tag{1.3}
\]

their upper-hole vectors are zero, and their six zero-candidate targets are
unchanged.  Thus (1.1) is a genuine Hall descent with no loss of support.
Shadow multiplicities are not all invariant: “no loss” here means equality
of the support sets at every displayed depth.

The mechanism has two logically separate parts:

1. the first braid is a rank-neutral Boolean-prism pivot which transports a
   legal oriented edge to the middle cut of the second braid;
2. the second braid refines one terminal pair-row into two singleton rows in
   the remote component rooted at 24610 and gains one matching unit.

The first move supplies **chronological legality**, not the Hall gain.

## 2. Exact profile-cancellation lemma

Fix a labeled target set \(T\).  A physical compiler state is represented,
for Hall purposes, by the multiset

\[
 \mathcal P=\{\!\{\Gamma(c):c\text{ is a physical cell}\}\!\},
 \qquad \Gamma(c)\subseteq T,                             \tag{2.1}
\]

of its right-neighborhood columns.  For a column multiset \(\mathcal A\),
write \(r(\mathcal A)\) for the maximum matching rank of its incidence
graph.  Given two states, let

\[
 \mathcal C=\mathcal P\wedge\mathcal P',\qquad
 \mathcal E=\mathcal P-\mathcal C,\qquad
 \mathcal E'=\mathcal P'-\mathcal C.                     \tag{2.2}
\]

Define the incremental capacity

\[
 \kappa_{\mathcal C}(\mathcal E)
   =r(\mathcal C+\mathcal E)-r(\mathcal C).               \tag{2.3}
\]

**Lemma 2.1 (exact cancellation).**

\[
 r(\mathcal P')-r(\mathcal P)
 =\kappa_{\mathcal C}(\mathcal E')
  -\kappa_{\mathcal C}(\mathcal E).                      \tag{2.4}
\]

**Proof.**  Relabeling right vertices having the same neighborhood does not
change a bipartite matching problem.  Hence
\(r(\mathcal P)=r(\mathcal C+\mathcal E)\) and similarly for
\(\mathcal P'\).  Subtraction gives (2.4).  \(\square\)

This lemma concerns Hall rank only.  Cancellation forgets physical cell
addresses, chronology, residence, shadow multiplicities, and owner pins;
those are audited separately below.

For the first arrow of (1.1), exact full-profile cancellation gives

\[
 |\mathcal C_{01}|=19298,quad r(\mathcal C_{01})=16354,
 \quad |\mathcal E_0|=|\mathcal E_1|=13,
 \quad \kappa_{\mathcal C_{01}}(\mathcal E_0)
      =\kappa_{\mathcal C_{01}}(\mathcal E_1)=9.          \tag{2.5}
\]

For the second arrow,

\[
 |\mathcal C_{12}|=19277,quad r(\mathcal C_{12})=16343,
 \quad |\mathcal E_1|=|\mathcal E_2|=34,
 \quad \kappa_{\mathcal C_{12}}(\mathcal E_1)=20,
 \quad \kappa_{\mathcal C_{12}}(\mathcal E_2)=21.       \tag{2.6}
\]

Equations (2.4)--(2.6) prove the global ranks in (1.2).

## 3. The normalized Boolean-prism pivot

For a family \(\mathcal X\) of masks and a coordinate \(c\) absent from
every member, put

\[
 \mathcal X_c=\{X\cup\{c\}:X\in\mathcal X\}.             \tag{3.1}
\]

Take

\[
 K=8218=\{1,3,4,13\},qquad
 Q=\{K,K_2,K_{10},K_{2,10}\},qquad a=0,quad b=6.       \tag{3.2}
\]

Let \(L\) be the disjoint union of the two old canonical component shores
rooted at 8217 and 8218.  Their sizes are respectively \(161/160\) and
\(160/159\).  Project the physical profiles to \(L\), delete empty
projections, and cancel only **after** this projection.  The common projected
bank has 317 columns and rank 317.  The complete residual identity is

\[
 \boxed{
 \{\!\{Q\cup Q_b,\ Q_a\}\!\}
 \longmapsto
 \{\!\{Q_b,\ Q\cup Q_a\}\!\}.}                         \tag{3.3}
\]

Both sides extend the common bank to 319 columns and rank 319.

The identity is incidence-neutral.  The three families \(Q,Q_a,Q_b\) are
pairwise disjoint and

\[
 \mathbf1_{Q\cup Q_b}+\mathbf1_{Q_a}
 =\mathbf1_{Q_b}+\mathbf1_{Q\cup Q_a}.                   \tag{3.4}
\]

What changes is connectivity.  Before the pivot, \(Q\cup Q_b\) and
\(Q_a\) lie in the two separate deficient components.  Afterwards the
column \(Q\cup Q_a\) meets both shores.  The exact DM census is therefore

\[
 (161/160)_{8217}\sqcup(160/159)_{8218}
 \longmapsto(321/319)_{8216}.                             \tag{3.5}
\]

The target union is unchanged, the total gap remains two, and the missing
native traces of the merged component are exactly

\[
 \{8217,8218\}.                                           \tag{3.6}
\]

Thus a useful neutral router need not compress DM mass: it may instead join
two unit-gap components by a degree-preserving prism pivot.

The rank assertion in (3.3) is essential.  Incidence identity (3.4), or the
sizes of the four Boolean faces alone, does not imply matching-rank
neutrality in an arbitrary surrounding bank.

## 4. Exact index transport and chronological legalization

For a path written as \(A|B|C|D\), the `RF` braid is

\[
 A|B|C|D\longmapsto A|\overleftarrow C|B|D.              \tag{4.1}
\]

For the first move in (1.1), \(|C|=1447\), and the pullback from positions
of \(P_1\) to positions of \(P_0\) is

\[
 \tau(i)=
 \begin{cases}
 i,&i<180,\\
 4390-i,&180\le i\le1626,\\
 i-1447,&1627\le i\le4210,\\
 i,&i\ge4211.
 \end{cases}                                              \tag{4.2}
\]

Consequently the later cut edge is transported as

\[
 (P_1[721],P_1[722])
 =(P_0[3669],P_0[3668])=(20266,18346),                    \tag{4.3}
\]

in place of the original edge

\[
 (P_0[721],P_0[722])=(9081,25401).                        \tag{4.4}
\]

The following elementary port test explains why this matters.

**Lemma 4.1 (FR seam-port test).**  Let \(P\) be a path of length \(n\), let
the zero-based cuts satisfy \(1\le a<u\le v<n-1\), and let

\[
 P=A|B|C|D,\qquad
 P'=A|C|\overleftarrow B|D,                               \tag{4.5}
\]

with cuts \(a,u,v+1\).  All internal path edges survive, possibly with
orientation reversed.  The only new undirected edges are

\[
 \{P[a-1],P[u]\},\qquad
 \{P[v],P[u-1]\},\qquad
 \{P[a],P[v+1]\}.                                        \tag{4.6}
\]

Hence (4.5) is a Johnson path if and only if all three pairs in (4.6) are
Johnson edges.

**Proof.**  Read the last and first vertices at each of the three new
concatenation seams in (4.5).  Every other consecutive pair was consecutive
in \(A,B,C,D\), possibly in reverse order.  \(\square\)

For `FR(123,722,4710)` on \(P_1\), the three pairs in (4.6) are

\[
 (26410,18346),\qquad(20386,20266),\qquad(26530,28450),   \tag{4.7}
\]

each of symmetric-difference size two.  On \(P_0\) directly, the first two
would instead be

\[
 (26410,25401),\qquad(20386,9081),                        \tag{4.8}
\]

of symmetric-difference sizes four and ten.  The direct braid has bad
Johnson edges at positions 122 and 4111.  Thus the first RF braid is a
literal legality router for the second braid.

Lemma 4.1 does not by itself prove depth-three residence or compiler
legality.  Those properties depend on the endpoint-conditioned collars, not
only on the three seam edges.  In the frozen route the complete collars pass
the independent audit.

## 5. The remote four-vertex ladder splitter

Let \(S\) be the 161-target component shore of \(P_1\) rooted at

\[
 v_0=24610=\{1,5,13,14\}.                                \tag{5.1}
\]

Define the nested chain

\[
 v_1=(v_0)_{10}=25634,\qquad
 v_2=(v_0)_{9,10}=26146,\qquad
 v_3=(v_0)_{8,9,10}=26402.                               \tag{5.2}
\]

After projection to \(S\) and cancellation, the common bank
\(\mathcal B\) has 159 columns and rank 159.  The exact residual replacement
is

\[
 \boxed{
 \{\!\{\{v_2,v_3\}\}\!\}
 \longmapsto
 \{\!\{\{v_0,v_1\},\{v_2\},\{v_3\}\}\!\}.}          \tag{5.3}
\]

Its rank table is

\[
\begin{array}{c|cc}
\text{bank}&\text{rank}&\text{columns}\\ \hline
\mathcal B&159&159\\
\mathcal B+\{\{v_2,v_3\}\}&160&160\\
\mathcal B+\{\{v_2\},\{v_3\}\}&161&161\\
\mathcal B+\{\{v_0,v_1\},\{v_2\},\{v_3\}\}&161&162.
\end{array}                                               \tag{5.4}
\]

Thus the two singleton columns, not the collateral root-edge copy, supply
the new matching unit.  The 161 targets become saturated, with one surplus
right column.  The complete old \(161/160\) component disappears from the
final canonical DM shore.

The physical realization of (5.3) is especially rigid:

\[
\begin{array}{c|ccc|c}
 &\text{cell}&\text{depth}&\text{start}&\text{projected shore}\\ \hline
\text{old}&12998&2&123&\{v_2,v_3\}\\
\text{new}&4713&0&4713&\{v_0,v_1\}\\
&11150&1&4712&\{v_2\}\\
&17586&2&4711&\{v_3\}.
\end{array}                                               \tag{5.5}
\]

It is a consecutive depth-0/1/2 ladder at starts 4713, 4712, 4711.  This is
the predictive signature: search for a legal braid collar which replaces a
terminal pair-column by its two singleton columns; any additional root-edge
column is harmless dump capacity.  The surrounding common bank must still
be checked, since a formal split need not extend a common matching.

## 6. Router--splitter descent theorem

The preceding mechanism can be stated without reference to the frozen
numbers.

**Theorem 6.1 (sufficient neutral-router/remote-splitter criterion).**
Let \(P_0,P_1,P_2\) be physical compiler states on the same labeled target
set.  Assume:

1. \(P_0\to P_1\) is a legal braid, and its full profile cancellation has
   equal old and new incremental capacities;
2. on two canonical DM components of \(P_0\), the projected residual is the
   prism pivot (3.3), both complete projected banks have the same rank, the
   target union \(L\) is unchanged, and a global maximum matching of
   \(P_1\) has exactly two unmatched left vertices in \(L\) whose global
   alternating-reachable left and right sets are exactly \(L\) and a set
   \(R\) of size equal to the sum of the two old right-shore sizes;
3. \(P_1\to P_2\) is a legal braid, and on a different unit-gap canonical
   component its projected residual has the form (5.3);
4. if \(S\) is that component's target shore, the common projected bank has
   a matching of size \(|S|-2\) which saturates exactly
   \(S\setminus\{v_2,v_3\}\), so adjoining the two singleton columns
   saturates the component;
5. full-profile cancellation for \(P_1\to P_2\) has new incremental
   capacity exactly one larger than the old capacity.

Then \(r(P_1)=r(P_0)\), the two components in condition 2 merge with their
gaps added, and

\[
 r(P_2)=r(P_1)+1.                                        \tag{6.1}
\]

Because the labeled target set is fixed, the Hall deficiency drops by
exactly one.  If, in addition, the final canonical DM census removes
precisely the component in condition 3 and introduces no new deficient
target, then that census identifies the complete local source of the drop.

**Proof.**  Condition 1 and Lemma 2.1 give the first rank equality.  The
global alternating-reachability hypothesis in condition 2 says exactly that
the two old shores form one canonical DM component in the new state.  Its
target and right-shore sizes add, while equality of the projected ranks
excludes a rank loss; hence its gap is the sum of the old gaps.  Under
condition 4, the singleton
columns match the two targets left free by the common-bank matching, hence
the selected unit-gap component is left-perfect after the split.  Condition
5 and Lemma 2.1 give (6.1) globally, including all collateral profiles.
The final census assertion then identifies which canonical deficient shore
has disappeared.
\(\square\)

Condition 5 cannot be replaced by the local motif alone: collateral columns
may interact with other tight shores.  Conversely, the first prism pivot is
not Hall-causal; its role is to put the required oriented edge and collar at
the second cut.

## 7. A proof-safe candidate rule

For a proposed `FR(a,u,v)` splitter on a current path \(P\), first choose an
oriented internal edge \((y_0,y_1)\) satisfying

\[
 P[a-1]\sim y_1,\qquad P[v]\sim y_0,\qquad P[a]\sim P[v+1],          \tag{7.1}
\]

where \(\sim\) denotes Johnson adjacency.  An `RF(r,s,t)` router can place
the reversed source edge at \((u-1,u)\) exactly when

\[
 (r+t-(u-1),\ r+t-u)                                     \tag{7.2}
\]

are its original source indices and \(u-1,u\) lie in the reversed block.
Then apply, in order:

1. the router's own three-seam Johnson test;
2. the complete depth-three endpoint-collar and residence test;
3. the full physical-profile cancellation test
   \(\kappa_{\mathcal C}(\mathcal E_{\mathrm{old}})
     =\kappa_{\mathcal C}(\mathcal E_{\mathrm{new}})\);
4. equality of the complete lower and upper support sets at every
   \(q=1,\ldots,7\) required by the frozen carrier;
5. the splitter seam, collar, residence, and full-shadow tests;
6. the projected terminal-pair refinement test (5.3);
7. the full splitter capacity test with gain one.

This rule is a safe positive-candidate generator.  It is not a pruning
theorem: a successful router need not use the prism pivot (3.3), and a Hall
gain may arise from a different projected Markov move.

## 8. Full-collar fingerprints and verification

For reproducibility, the full residual profile-size histograms are

\[
\begin{array}{c|cc}
 &\text{deleted}&\text{inserted}\\ \hline
P_0\to P_1&\{4:8,8:5\}&\{4:2,8:10,16:1\}\\
P_1\to P_2&\{2:5,4:15,8:12,16:2\}&\{2:3,4:15,8:15,16:1\}.
\end{array}                                               \tag{8.1}
\]

Their sorted target-mask multiset digests are respectively

```text
6c824ed056631423783d0b2931d60744ae9c467e56ed17242b8af2f4051b0f2d
5a37c4f9aa345a001082c613c462add7acdb767827793a542fbb42a2eba87fcb
8f36dd02602c8e6d87ed1451cd83e60e935a68bc0c906a224c47711c4b9d7325
9a45f75b3534934d1790d362692b17f6a9e05484e2e78f281fb8d67b001b6c94
```

The frozen state hashes are

```text
P0  9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
P1  eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51
P2  86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

The lightweight independent checker

```text
scratch/threadA_audit_k15_h20_h19_prism_router.py
```

rebuilds the three physical graphs and checks every displayed rank, profile
identity, index pullback, seam pair, component size, native missing root,
and physical ladder address.  Its certificate is

```text
scratch/threadA_k15_h20_h19_prism_router_audit.json.
```

The broader independent audit

```text
scratch/audit_k15_h19_root8216_chain_independent.py
scratch/audit_k15_h19_root8216_chain_independent.json
```

also verifies the full shadow tower, residence, canonical DM censuses, and
the final 497 distinct native pins.  After reserving those pins, the residual
rank is 15867, so the pin-plus-residual total is the final matching rank
16364.  This remains a frozen-carrier certificate, not a completion of the
six zero targets or a proof of the exact formula.
